# 摘要生成提示词

## 获取正文

根据信源 method 文件的 `detail_method` 字段选择获取方式：

| detail_method | 获取方式 | 说明 |
|---------------|---------|------|
| `fetch` | WebFetch 工具 | 快速，适合服务端渲染页面 |
| `browser` | Playwright 浏览器 | 慢，适合 JS 渲染页面 |
| 未指定 | 默认 `fetch` | 优先尝试快速方式 |

## 输入

- **正文内容**: 来自 WebFetch 或 browser_snapshot
- **用户画像**: 来自 profile.yaml 的 interests 和 keywords

## 任务

生成结构化摘要，包含以下字段：

### 1. summary（摘要）

100-150 字精准摘要，要求：
- 提取核心观点和关键数据
- 避免空洞开头（如"本文介绍了..."、"这篇文章讲述了..."）
- 直接陈述内容，保留具体名称、数据、结论
- 如有版本号、数字、日期等具体信息必须保留

### 2. relevance_score（相关度评分）

根据用户画像评分，1-5 分：

| 评分 | 条件 |
|------|------|
| 5 | 匹配多个 high_priority_keywords |
| 4 | 匹配 high_priority_keywords 或高度相关多个 interests |
| 3 | 相关 interests |
| 2 | 间接相关 |
| 1 | 低相关但有信息价值 |

### 3. relevance_reason（相关原因）

一句话说明评分原因，例如：
- "涉及 Claude Agent 最新进展"
- "GPT-5 重大功能更新"
- "AI 创业融资案例"

### 4. keywords（关键词）

从正文提取 3-5 个关键词，用于后续检索和分类。

## 输出格式

```json
{
  "summary": "...",
  "relevance_score": 4,
  "relevance_reason": "...",
  "keywords": ["keyword1", "keyword2", "keyword3"]
}
```

## 示例

**输入正文**:
> Claude Code 新增 Cowork 功能，这是一个研究预览版本，让用户可以在传统 IDE 之外使用 Claude 进行协作...

**输入画像**:
```yaml
interests: ["AI/人工智能", "Agent/智能体"]
high_priority_keywords: ["Claude", "Agent", "发布"]
```

**输出**:
```json
{
  "summary": "Claude Code 新增 Cowork 功能（研究预览版），支持在 IDE 之外的场景使用，包括文档编辑、数据分析等。用户可通过自然语言指令完成复杂工作流，支持多文件协作和上下文保持。这是 Anthropic 将 Claude 能力扩展到更广泛工作场景的重要一步。",
  "relevance_score": 5,
  "relevance_reason": "Claude 重大功能发布，涉及 Agent 能力扩展",
  "keywords": ["Claude Code", "Cowork", "Agent", "功能发布", "Anthropic"]
}
```
