# WebFetch 智能获取

适用于可被 WebFetch 直接解析的网页（大多数现代网站）。

## 使用方式

workspace method 文件设置：
```yaml
extends: webfetch-smart
```

## 执行步骤

1. **获取页面内容**
   ```
   WebFetch
   url: <source_url>
   prompt: 提取所有文章/帖子列表，包括标题、链接、发布日期。返回 JSON 数组格式。
   ```

2. **处理结果**
   - 补全相对链接为完整 URL
   - 标准化日期格式
   - 过滤无效条目

3. **输出格式**
   ```json
   [
     {"title": "...", "url": "https://...", "published_at": "YYYY-MM-DD"}
   ]
   ```

## 适用场景

- 静态网站
- 服务端渲染页面
- 大多数博客、新闻站点

## 不适用场景

- 需要登录的页面
- 强反爬虫保护的站点
- 纯 JS 渲染且 WebFetch 无法解析的页面（改用 browser-smart）
