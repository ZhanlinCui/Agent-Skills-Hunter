# Method 文件规范

Method 文件定义如何从信源获取内容。存放在 `<workspace>/methods/` 目录。

## 文件类型

| 类型 | 后缀 | 适用场景 |
|------|------|---------|
| 配置 | `.yaml` | 使用 extends 引用通用方法 |
| 脚本 | `.py` | 完全自定义获取逻辑 |
| 指引 | `.md` | 需要 AI 按步骤操作 |

推荐优先使用 `.yaml` 配置 + `extends`，简单清晰。

---

## 字段说明

| 字段 | 必需 | 说明 |
|------|------|------|
| `source_id` | 是 | 唯一标识，用于数据库关联 |
| `source_name` | 是 | 显示名称 |
| `source_url` | 是 | 信源首页 URL |
| `enabled` | 是 | 是否启用（true/false） |
| `extends` | 否 | 引用通用方法（见下文） |
| `detail_method` | 否 | 详情页获取方式（fetch/browser），默认 fetch |
| `date_range` | 否 | 日期范围过滤（见下文），默认无限制 |

### date_range 字段

控制只抓取特定日期范围内的内容，避免每次都抓取全部历史。

```yaml
# 示例：只抓最近 7 天的内容
date_range:
  type: relative
  days: 7

# 示例：只抓特定日期之后的内容
date_range:
  type: since
  date: "2026-01-01"

# 示例：抓特定日期范围
date_range:
  type: between
  from: "2026-01-01"
  to: "2026-01-31"
```

| type | 说明 |
|------|------|
| `relative` | 相对天数，如 `days: 7` 表示最近7天 |
| `since` | 从某个日期开始至今 |
| `between` | 特定日期区间 |

---

## extends 字段

引用 `references/methods/` 中的通用方法。

| 值 | 适用场景 | 说明 |
|----|---------|------|
| `rss` | 有 RSS 源 | 最快，自动解析 feed |
| `webfetch-smart` | 大多数网站 | WebFetch + AI 解析 |
| `browser-smart` | JS 渲染/反爬/需登录 | Browser MCP，用用户浏览器登录态 |

### 示例：RSS 信源

```yaml
# methods/anthropic-news.yaml
source_id: anthropic-news
source_name: Anthropic News
source_url: https://anthropic.com/rss.xml
enabled: true
extends: rss
detail_method: fetch
```

### 示例：普通网站

```yaml
# methods/claude-blog.yaml
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog
enabled: true
extends: webfetch-smart
detail_method: fetch
```

### 示例：需要登录的网站

```yaml
# methods/twitter-karpathy.yaml
source_id: twitter-karpathy
source_name: Karpathy Twitter
source_url: https://x.com/karpathy
enabled: true
extends: browser-smart
detail_method: browser
```

使用 Browser MCP，直接用用户浏览器的登录态。运行前需点击扩展连接。

---

## detail_method 字段

控制**阶段 2**获取详情页正文的方式。

| 值 | 工具 | 速度 | 适用场景 |
|----|------|------|---------|
| `fetch` | WebFetch | 快 | 服务端渲染页面（默认） |
| `browser` | Browser MCP | 慢 | JS 渲染或需登录 |

---

## 输出格式

无论哪种 method 类型，输出必须是 JSON 数组：

```json
[
  {
    "title": "文章标题",
    "url": "https://example.com/article/1",
    "published_at": "2026-01-15T10:00:00"
  }
]
```

| 字段 | 必需 | 说明 |
|------|------|------|
| `title` | 是 | 文章标题 |
| `url` | 是 | 文章链接（必须唯一） |
| `published_at` | 否 | 发布时间（ISO 8601） |
