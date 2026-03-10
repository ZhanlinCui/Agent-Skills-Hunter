#!/usr/bin/env python3
"""
Daily News 数据库操作脚本

命令：
  init           - 初始化数据库
  add-items      - 添加条目（自动去重）
  list-pending   - 列出待处理条目
  update-summary - 更新摘要
  list-today     - 列出今日内容
  list-range     - 列出日期范围内容
  list-sources   - 列出所有信源
  stats          - 统计信息
  last-report    - 获取上次日报日期

使用示例：
  python3 db.py init --db ./data/news.db
  python3 db.py add-items --db ./data/news.db --source claude-blog --items '[...]'
  python3 db.py list-pending --db ./data/news.db --limit 10
  python3 db.py update-summary --db ./data/news.db --id 1 --data '{...}'
  python3 db.py list-today --db ./data/news.db
  python3 db.py list-range --db ./data/news.db --from 2026-01-10 --to 2026-01-15
  python3 db.py last-report --db ./data/news.db
"""

import argparse
import json
import sqlite3
from datetime import datetime, date
from pathlib import Path


def get_db(db_path: str) -> sqlite3.Connection:
    """获取数据库连接"""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(db_path: str) -> dict:
    """初始化数据库"""
    # 确保目录存在
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)

    conn = get_db(db_path)
    conn.executescript("""
        -- 内容元数据表
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source_id TEXT NOT NULL,
            url TEXT UNIQUE NOT NULL,
            title TEXT NOT NULL,
            published_at TEXT,
            discovered_at TEXT NOT NULL,
            status TEXT DEFAULT 'pending'
        );

        -- 摘要表
        CREATE TABLE IF NOT EXISTS summaries (
            item_id INTEGER PRIMARY KEY,
            summary TEXT NOT NULL,
            relevance_score INTEGER,
            relevance_reason TEXT,
            keywords TEXT,
            summarized_at TEXT NOT NULL,
            FOREIGN KEY (item_id) REFERENCES items(id)
        );

        -- 日报记录表
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT UNIQUE NOT NULL,
            item_count INTEGER,
            high_relevance_count INTEGER,
            created_at TEXT NOT NULL,
            file_path TEXT
        );

        -- 索引
        CREATE INDEX IF NOT EXISTS idx_items_status ON items(status);
        CREATE INDEX IF NOT EXISTS idx_items_source ON items(source_id);
        CREATE INDEX IF NOT EXISTS idx_items_discovered ON items(discovered_at);
    """)
    conn.commit()
    conn.close()

    return {"status": "initialized", "path": db_path}


def add_items(db_path: str, source_id: str, items: list) -> dict:
    """添加条目（自动去重）"""
    conn = get_db(db_path)
    now = datetime.now().isoformat()

    added = 0
    skipped = 0

    for item in items:
        try:
            conn.execute(
                """INSERT INTO items (source_id, url, title, published_at, discovered_at)
                   VALUES (?, ?, ?, ?, ?)""",
                (source_id, item["url"], item["title"], item.get("published_at"), now)
            )
            added += 1
        except sqlite3.IntegrityError:
            # URL 已存在
            skipped += 1

    conn.commit()
    conn.close()

    return {
        "status": "ok",
        "source_id": source_id,
        "added": added,
        "skipped": skipped,
        "total": len(items)
    }


def list_pending(db_path: str, limit: int = 10) -> list:
    """列出待处理条目"""
    conn = get_db(db_path)
    rows = conn.execute(
        """SELECT id, source_id, url, title, published_at, discovered_at
           FROM items
           WHERE status = 'pending'
           ORDER BY discovered_at DESC
           LIMIT ?""",
        (limit,)
    ).fetchall()
    conn.close()

    return [dict(r) for r in rows]


def list_pending_by_date(db_path: str, from_date: str, to_date: str = None, limit: int = 50) -> list:
    """
    按日期范围列出待处理条目（兜底过滤）

    Args:
        from_date: 开始日期 (YYYY-MM-DD)
        to_date: 结束日期 (YYYY-MM-DD)，默认今天
        limit: 最大条数
    """
    conn = get_db(db_path)

    if to_date is None:
        to_date = date.today().isoformat()

    rows = conn.execute(
        """SELECT id, source_id, url, title, published_at, discovered_at
           FROM items
           WHERE status = 'pending'
             AND (published_at IS NULL OR date(published_at) BETWEEN ? AND ?)
           ORDER BY published_at DESC NULLS LAST, discovered_at DESC
           LIMIT ?""",
        (from_date, to_date, limit)
    ).fetchall()
    conn.close()

    return [dict(r) for r in rows]


def update_summary(db_path: str, item_id: int, data: dict) -> dict:
    """更新摘要"""
    conn = get_db(db_path)
    now = datetime.now().isoformat()

    # 插入或更新摘要
    conn.execute(
        """INSERT OR REPLACE INTO summaries
           (item_id, summary, relevance_score, relevance_reason, keywords, summarized_at)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (
            item_id,
            data["summary"],
            data.get("relevance_score"),
            data.get("relevance_reason"),
            json.dumps(data.get("keywords", [])),
            now
        )
    )

    # 更新条目状态
    conn.execute(
        "UPDATE items SET status = 'summarized' WHERE id = ?",
        (item_id,)
    )

    conn.commit()
    conn.close()

    return {"status": "ok", "item_id": item_id}


def list_today(db_path: str) -> list:
    """列出今日内容（含摘要）"""
    conn = get_db(db_path)
    today = date.today().isoformat()

    rows = conn.execute(
        """SELECT
             i.id, i.source_id, i.url, i.title, i.published_at, i.discovered_at, i.status,
             s.summary, s.relevance_score, s.relevance_reason, s.keywords
           FROM items i
           LEFT JOIN summaries s ON i.id = s.item_id
           WHERE date(i.discovered_at) = ?
           ORDER BY s.relevance_score DESC NULLS LAST, i.discovered_at DESC""",
        (today,)
    ).fetchall()
    conn.close()

    result = []
    for r in rows:
        item = dict(r)
        # 解析 keywords JSON
        if item.get("keywords"):
            try:
                item["keywords"] = json.loads(item["keywords"])
            except json.JSONDecodeError:
                item["keywords"] = []
        result.append(item)

    return result


def list_range(db_path: str, from_date: str, to_date: str) -> list:
    """列出日期范围内容（含摘要）"""
    conn = get_db(db_path)

    rows = conn.execute(
        """SELECT
             i.id, i.source_id, i.url, i.title, i.published_at, i.discovered_at, i.status,
             s.summary, s.relevance_score, s.relevance_reason, s.keywords
           FROM items i
           LEFT JOIN summaries s ON i.id = s.item_id
           WHERE date(i.discovered_at) BETWEEN ? AND ?
           ORDER BY s.relevance_score DESC NULLS LAST, i.discovered_at DESC""",
        (from_date, to_date)
    ).fetchall()
    conn.close()

    result = []
    for r in rows:
        item = dict(r)
        if item.get("keywords"):
            try:
                item["keywords"] = json.loads(item["keywords"])
            except json.JSONDecodeError:
                item["keywords"] = []
        result.append(item)

    return result


def last_report(db_path: str) -> dict:
    """获取上次日报信息"""
    conn = get_db(db_path)
    row = conn.execute(
        """SELECT date, item_count, high_relevance_count, created_at, file_path
           FROM reports
           ORDER BY date DESC
           LIMIT 1"""
    ).fetchone()
    conn.close()

    if row:
        return dict(row)
    return {"date": None, "message": "No reports found"}


def list_sources(db_path: str) -> list:
    """列出所有信源及统计"""
    conn = get_db(db_path)
    rows = conn.execute(
        """SELECT
             source_id,
             COUNT(*) as total_items,
             SUM(CASE WHEN status = 'pending' THEN 1 ELSE 0 END) as pending_count,
             MAX(discovered_at) as last_discovered
           FROM items
           GROUP BY source_id
           ORDER BY last_discovered DESC"""
    ).fetchall()
    conn.close()

    return [dict(r) for r in rows]


def stats(db_path: str) -> dict:
    """统计信息"""
    conn = get_db(db_path)

    # 总条目数
    total = conn.execute("SELECT COUNT(*) FROM items").fetchone()[0]

    # 按状态统计
    status_counts = {}
    for row in conn.execute("SELECT status, COUNT(*) FROM items GROUP BY status"):
        status_counts[row[0]] = row[1]

    # 今日新增
    today = date.today().isoformat()
    today_count = conn.execute(
        "SELECT COUNT(*) FROM items WHERE date(discovered_at) = ?",
        (today,)
    ).fetchone()[0]

    # 信源数
    source_count = conn.execute(
        "SELECT COUNT(DISTINCT source_id) FROM items"
    ).fetchone()[0]

    # 高相关内容数（4-5星）
    high_relevance = conn.execute(
        "SELECT COUNT(*) FROM summaries WHERE relevance_score >= 4"
    ).fetchone()[0]

    conn.close()

    return {
        "total_items": total,
        "status_counts": status_counts,
        "today_count": today_count,
        "source_count": source_count,
        "high_relevance_count": high_relevance
    }


def record_report(db_path: str, report_date: str, item_count: int, high_count: int, file_path: str) -> dict:
    """记录日报"""
    conn = get_db(db_path)
    now = datetime.now().isoformat()

    try:
        conn.execute(
            """INSERT INTO reports (date, item_count, high_relevance_count, created_at, file_path)
               VALUES (?, ?, ?, ?, ?)""",
            (report_date, item_count, high_count, now, file_path)
        )
        conn.commit()
        status = "created"
    except sqlite3.IntegrityError:
        # 已存在，更新
        conn.execute(
            """UPDATE reports
               SET item_count = ?, high_relevance_count = ?, created_at = ?, file_path = ?
               WHERE date = ?""",
            (item_count, high_count, now, file_path, report_date)
        )
        conn.commit()
        status = "updated"

    conn.close()
    return {"status": status, "date": report_date}


# ==================== 增量抓取相关功能 ====================

def check_existing_urls(db_path: str, urls: list) -> set:
    """批量检查 URL 是否已存在

    Args:
        urls: 要检查的 URL 列表

    Returns:
        已存在的 URL 集合
    """
    if not urls:
        return set()

    conn = get_db(db_path)
    placeholders = ','.join(['?' for _ in urls])
    rows = conn.execute(
        f"SELECT url FROM items WHERE url IN ({placeholders})",
        tuple(urls)
    ).fetchall()
    conn.close()

    return set(row[0] for row in rows)


def add_items_incremental(db_path: str, source_id: str, items: list, date_range_start: str = None) -> dict:
    """增量添加条目（带预检查和同步日志）

    Args:
        date_range_start: 抓取日期范围的开始日期（用于记录日志）
    """
    conn = get_db(db_path)
    now = datetime.now().isoformat()

    # 1. 批量检查已存在的 URL
    urls = [item["url"] for item in items]
    existing_urls = check_existing_urls(db_path, urls)

    # 2. 过滤新条目
    new_items = []
    duplicates = []
    for item in items:
        if item["url"] in existing_urls:
            duplicates.append(item)
        else:
            new_items.append(item)

    # 3. 入库新条目
    added = 0
    for item in new_items:
        try:
            conn.execute(
                """INSERT INTO items (source_id, url, title, published_at, discovered_at)
                   VALUES (?, ?, ?, ?, ?)""",
                (source_id, item["url"], item["title"], item.get("published_at"), now)
            )
            added += 1
        except sqlite3.IntegrityError:
            # 并发情况下可能仍有重复
            duplicates.append(item)

    # 4. 记录同步日志
    if items:
        latest_date = max(
            (item.get("published_at", "") for item in items if item.get("published_at")),
            default=""
        )
        conn.execute(
            """INSERT INTO source_sync_log
               (source_id, sync_date, items_fetched, items_new, items_duplicate,
                latest_item_date, date_range_start, created_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (source_id, now[:10], len(items), added, len(duplicates),
             latest_date, date_range_start, now)
        )

        # 5. 更新 source_status
        total_fetched = conn.execute(
            "SELECT COUNT(*) FROM items WHERE source_id = ?",
            (source_id,)
        ).fetchone()[0]

        conn.execute(
            """INSERT INTO source_status (source_id, last_fetched_date, last_fetched_count,
               total_items_fetched, updated_at)
               VALUES (?, ?, ?, ?, ?)
               ON CONFLICT(source_id) DO UPDATE SET
               last_fetched_date = excluded.last_fetched_date,
               last_fetched_count = excluded.last_fetched_count,
               total_items_fetched = excluded.total_items_fetched,
               updated_at = excluded.updated_at""",
            (source_id, now[:10], added, total_fetched, now)
        )

    conn.commit()
    conn.close()

    return {
        "status": "ok",
        "source_id": source_id,
        "fetched": len(items),
        "added": added,
        "duplicates": len(duplicates),
        "duplicate_urls": [d["url"] for d in duplicates[:5]]  # 只显示前5个
    }


def get_source_status(db_path: str, source_id: str = None) -> dict:
    """获取信源同步状态"""
    conn = get_db(db_path)

    if source_id:
        row = conn.execute(
            """SELECT source_id, last_fetched_date, last_fetched_count,
               total_items_fetched, updated_at
               FROM source_status WHERE source_id = ?""",
            (source_id,)
        ).fetchone()
        conn.close()
        return dict(row) if row else {"source_id": source_id, "last_fetched_date": None}
    else:
        rows = conn.execute(
            """SELECT source_id, last_fetched_date, last_fetched_count,
               total_items_fetched, updated_at
               FROM source_status ORDER BY updated_at DESC"""
        ).fetchall()
        conn.close()
        return [dict(r) for r in rows]


def list_sync_log(db_path: str, source_id: str = None, limit: int = 10) -> list:
    """获取同步日志"""
    conn = get_db(db_path)

    if source_id:
        rows = conn.execute(
            """SELECT * FROM source_sync_log
               WHERE source_id = ?
               ORDER BY sync_date DESC LIMIT ?""",
            (source_id, limit)
        ).fetchall()
    else:
        rows = conn.execute(
            """SELECT * FROM source_sync_log
               ORDER BY sync_date DESC LIMIT ?""",
            (limit,)
        ).fetchall()

    conn.close()
    return [dict(r) for r in rows]


def main():
    parser = argparse.ArgumentParser(description="Daily News Database Operations")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # init
    init_parser = subparsers.add_parser("init", help="Initialize database")
    init_parser.add_argument("--db", required=True, help="Database path")

    # add-items
    add_parser = subparsers.add_parser("add-items", help="Add items")
    add_parser.add_argument("--db", required=True, help="Database path")
    add_parser.add_argument("--source", required=True, help="Source ID")
    add_parser.add_argument("--items", required=True, help="Items JSON")

    # list-pending
    pending_parser = subparsers.add_parser("list-pending", help="List pending items")
    pending_parser.add_argument("--db", required=True, help="Database path")
    pending_parser.add_argument("--limit", type=int, default=10, help="Max items")

    # update-summary
    summary_parser = subparsers.add_parser("update-summary", help="Update summary")
    summary_parser.add_argument("--db", required=True, help="Database path")
    summary_parser.add_argument("--id", required=True, type=int, help="Item ID")
    summary_parser.add_argument("--data", required=True, help="Summary JSON")

    # list-today
    today_parser = subparsers.add_parser("list-today", help="List today's items")
    today_parser.add_argument("--db", required=True, help="Database path")

    # list-range
    range_parser = subparsers.add_parser("list-range", help="List items in date range")
    range_parser.add_argument("--db", required=True, help="Database path")
    range_parser.add_argument("--from", dest="from_date", required=True, help="Start date (YYYY-MM-DD)")
    range_parser.add_argument("--to", dest="to_date", required=True, help="End date (YYYY-MM-DD)")

    # last-report
    last_report_parser = subparsers.add_parser("last-report", help="Get last report info")
    last_report_parser.add_argument("--db", required=True, help="Database path")

    # list-sources
    sources_parser = subparsers.add_parser("list-sources", help="List sources")
    sources_parser.add_argument("--db", required=True, help="Database path")

    # stats
    stats_parser = subparsers.add_parser("stats", help="Show statistics")
    stats_parser.add_argument("--db", required=True, help="Database path")

    # record-report
    report_parser = subparsers.add_parser("record-report", help="Record report")
    report_parser.add_argument("--db", required=True, help="Database path")
    report_parser.add_argument("--date", required=True, help="Report date (YYYY-MM-DD)")
    report_parser.add_argument("--items", required=True, type=int, help="Item count")
    report_parser.add_argument("--high", required=True, type=int, help="High relevance count")
    report_parser.add_argument("--file", required=True, help="Output file path")

    # add-items-incremental (增量抓取)
    incremental_parser = subparsers.add_parser("add-items-incremental", help="Add items with incremental check")
    incremental_parser.add_argument("--db", required=True, help="Database path")
    incremental_parser.add_argument("--source", required=True, help="Source ID")
    incremental_parser.add_argument("--items", required=True, help="Items JSON")
    incremental_parser.add_argument("--since", help="Date range start (YYYY-MM-DD)")

    # check-existing (批量检查URL)
    check_parser = subparsers.add_parser("check-existing", help="Check if URLs exist")
    check_parser.add_argument("--db", required=True, help="Database path")
    check_parser.add_argument("--urls", required=True, help="URLs JSON array")

    # source-status (获取信源状态)
    status_parser = subparsers.add_parser("source-status", help="Get source sync status")
    status_parser.add_argument("--db", required=True, help="Database path")
    status_parser.add_argument("--source", help="Source ID (optional)")

    # sync-log (获取同步日志)
    log_parser = subparsers.add_parser("sync-log", help="Get sync log")
    log_parser.add_argument("--db", required=True, help="Database path")
    log_parser.add_argument("--source", help="Source ID filter")
    log_parser.add_argument("--limit", type=int, default=10, help="Max entries")

    args = parser.parse_args()

    if args.command == "init":
        result = init_db(args.db)
    elif args.command == "add-items":
        items = json.loads(args.items)
        result = add_items(args.db, args.source, items)
    elif args.command == "list-pending":
        result = list_pending(args.db, args.limit)
    elif args.command == "update-summary":
        data = json.loads(args.data)
        result = update_summary(args.db, args.id, data)
    elif args.command == "list-today":
        result = list_today(args.db)
    elif args.command == "list-range":
        result = list_range(args.db, args.from_date, args.to_date)
    elif args.command == "last-report":
        result = last_report(args.db)
    elif args.command == "list-sources":
        result = list_sources(args.db)
    elif args.command == "stats":
        result = stats(args.db)
    elif args.command == "record-report":
        result = record_report(args.db, args.date, args.items, args.high, args.file)
    elif args.command == "add-items-incremental":
        items = json.loads(args.items)
        result = add_items_incremental(args.db, args.source, items, args.since)
    elif args.command == "check-existing":
        urls = json.loads(args.urls)
        existing = check_existing_urls(args.db, urls)
        result = {"existing_urls": list(existing), "count": len(existing)}
    elif args.command == "source-status":
        result = get_source_status(args.db, args.source)
    elif args.command == "sync-log":
        result = list_sync_log(args.db, args.source, args.limit)
    else:
        parser.print_help()
        return

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
