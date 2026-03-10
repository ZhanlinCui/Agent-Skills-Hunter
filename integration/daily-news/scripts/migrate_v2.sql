-- Daily News Database Migration V2
-- 添加增量抓取相关表

-- 1. 信源同步日志表
CREATE TABLE IF NOT EXISTS source_sync_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_id TEXT NOT NULL,
    sync_date TEXT NOT NULL,
    items_fetched INTEGER DEFAULT 0,
    items_new INTEGER DEFAULT 0,
    items_duplicate INTEGER DEFAULT 0,
    items_skipped INTEGER DEFAULT 0,  -- 因日期限制跳过的条目
    latest_item_date TEXT,
    date_range_start TEXT,
    date_range_end TEXT,
    created_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_sync_log_source ON source_sync_log(source_id);
CREATE INDEX IF NOT EXISTS idx_sync_log_date ON source_sync_log(sync_date);

-- 2. 信源状态表（快速查询用）
CREATE TABLE IF NOT EXISTS source_status (
    source_id TEXT PRIMARY KEY,
    last_fetched_date TEXT,
    last_fetched_count INTEGER DEFAULT 0,
    total_items_fetched INTEGER DEFAULT 0,
    total_items_unique INTEGER DEFAULT 0,
    first_fetch_date TEXT,
    updated_at TEXT NOT NULL
);

-- 3. 添加 URL 哈希索引（加速去重查询）
-- 注意：SQLite 不支持直接函数索引，使用触发器维护
CREATE INDEX IF NOT EXISTS idx_items_url_prefix ON items(url);

-- 迁移完成标记
CREATE TABLE IF NOT EXISTS schema_version (
    version INTEGER PRIMARY KEY,
    applied_at TEXT NOT NULL,
    description TEXT
);

INSERT INTO schema_version (version, applied_at, description)
VALUES (2, datetime('now'), 'Add incremental fetch support: source_sync_log, source_status tables');
