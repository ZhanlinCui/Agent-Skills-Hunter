# 日报生成提示词

## 生成前：确认日期范围

在生成日报前，询问用户日期范围：

> 要生成哪个范围的日报？
> 1. 只要今天（默认）
> 2. 补上最近几天（自动检测上次日报日期）
> 3. 指定日期范围

根据选择查询数据库：
```bash
# 今天
python3 scripts/db.py list-today --db <workspace>/data/news.db

# 指定日期范围（需扩展 db.py 支持）
python3 scripts/db.py list-range --db <workspace>/data/news.db --from 2026-01-10 --to 2026-01-15
```

## 输入字段

- `title` - 标题
- `url` - 链接
- `source_id` - 来源标识
- `summary` - 摘要（直接使用）
- `relevance_score` - 相关度（1-5）
- `published_at` - 发布时间

## 日报结构

```markdown
# Daily News - {{DATE}}

## 导读

- **主题1**：具体内容
- **主题2**：具体内容

---

## 五星推荐

**[{{title}}]({{url}})**
{{summary}}
`{{source_id}}` · `{{published_at}}`

## 四星推荐
...

## 值得一看
...

## 其他
...
```

## 生成规则

### 1. 导读

用要点形式总结今日趋势：
- 3-5 个要点
- 格式：`- **主题**：具体内容`
- 基于五星内容提炼

### 2. 按优先级分组

| 分组 | relevance_score |
|------|-----------------|
| 五星推荐 | 5 |
| 四星推荐 | 4 |
| 值得一看 | 3 |
| 其他 | 1-2 |

### 3. 条目格式

```markdown
**[{{title}}]({{url}})**
{{summary}}
`{{source_id}}` · `{{published_at}}`
```

- 标题加粗带链接
- 摘要独立一行，直接引用数据库
- 来源和日期用行内代码，`·` 分隔
- 条目间空一行

### 4. 空组处理

无对应内容的分组不显示。

## 示例

```markdown
## 五星推荐

**[OpenAI partners with Cerebras](https://openai.com/index/cerebras-partnership)**
OpenAI 与 Cerebras 达成合作，将新增 750MW 超低延迟 AI 算力。Cerebras 的芯片架构将大规模计算、内存和带宽集成在单个芯片上，消除传统硬件的推理瓶颈。
`OpenAI` · `2026-01-14`

**[Cowork: Claude Code for the rest of your work](https://claude.com/blog/cowork-research-preview)**
Cowork 是 Claude Code 面向非编程场景的延伸，支持文件整理、表格生成、报告起草等任务。
`Claude Blog` · `2026-01-12`
```
