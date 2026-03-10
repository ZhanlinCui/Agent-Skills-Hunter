#!/usr/bin/env python3
"""
RSS/Atom Feed 通用获取方法

使用方式：
  python3 rss.py --url "https://example.com/feed.xml" [--limit 20]

输出：JSON 格式的文章元数据列表

依赖：pip install feedparser
"""

import argparse
import json
import sys
from datetime import datetime

try:
    import feedparser
except ImportError:
    print(json.dumps({"error": "Missing dependency. Install with: pip install feedparser"}))
    sys.exit(1)


def parse_date(entry) -> str | None:
    """从 entry 提取日期，返回 ISO 格式字符串"""
    for attr in ["published_parsed", "updated_parsed", "created_parsed"]:
        parsed = getattr(entry, attr, None)
        if parsed:
            try:
                return datetime(*parsed[:6]).isoformat()
            except (TypeError, ValueError):
                continue
    return None


def fetch(url: str, limit: int | None = None) -> list | dict:
    """
    获取 RSS/Atom feed 内容

    Args:
        url: Feed URL
        limit: 最大条目数（None 表示不限制）

    Returns:
        文章列表或错误信息
    """
    feed = feedparser.parse(url)

    # 检查解析错误
    if feed.bozo and not feed.entries:
        return {"error": f"Failed to parse feed: {feed.bozo_exception}"}

    items = []
    entries = feed.entries[:limit] if limit else feed.entries

    for entry in entries:
        item = {
            "title": getattr(entry, "title", "").strip(),
            "url": getattr(entry, "link", ""),
        }

        # 提取日期
        date = parse_date(entry)
        if date:
            item["published_at"] = date

        # 只添加有效条目
        if item.get("url") and item.get("title"):
            items.append(item)

    return items


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch RSS/Atom feed")
    parser.add_argument("--url", required=True, help="Feed URL")
    parser.add_argument("--limit", type=int, help="Max items to fetch")
    args = parser.parse_args()

    result = fetch(args.url, args.limit)
    print(json.dumps(result, ensure_ascii=False, indent=2))
