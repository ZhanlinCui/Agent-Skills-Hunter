# Ultimate Agent Skills Collection

<div align="center">

<img src="https://img.shields.io/badge/技能-51+-blueviolet?style=for-the-badge" alt="技能数量" />
<img src="https://img.shields.io/badge/品质-精选-gold?style=for-the-badge" alt="品质" />
<img src="https://img.shields.io/badge/许可证-MIT-green?style=for-the-badge" alt="许可证" />
<img src="https://img.shields.io/badge/语言-6种-blue?style=for-the-badge" alt="语言" />

<br />

<img src="https://img.shields.io/github/stars/ZhanlinCui/Ultimate-Agent-Skills-Collection?style=social" alt="Stars" />
<img src="https://img.shields.io/github/forks/ZhanlinCui/Ultimate-Agent-Skills-Collection?style=social" alt="Forks" />
<img src="https://img.shields.io/github/last-commit/ZhanlinCui/Ultimate-Agent-Skills-Collection" alt="最近提交" />
<img src="https://img.shields.io/github/contributors/ZhanlinCui/Ultimate-Agent-Skills-Collection" alt="贡献者" />

**互联网上最全面的生产级 Agent 技能库**

*不只是链接 — 包含脚本、模板和参考文档的完整实现，开箱即用。*

[English](./README.md) | [繁體中文](./README.zh-TW.md) | [日本語](./README.ja.md) | [한국어](./README.ko.md) | [Español](./README.es.md)

</div>

---

## 目录

- [什么是 Agent Skills？](#-什么是-agent-skills)
- [为什么选择这个合集？](#-为什么选择这个合集)
- [兼容的 AI 代理](#-兼容的-ai-代理)
- [快速开始](#-快速开始)
- [技能目录](#-技能目录)
- [官方技能参考](#-官方技能参考)
- [社区技能与合集](#-社区技能与合集)
- [IDE/Agent 配置](#-ideagent-配置)
- [官方教程与指南](#-官方教程与指南)
- [常见问题](#-常见问题)
- [参与贡献](#-参与贡献)
- [许可证](#-许可证)
- [Star 历史](#-star-历史)
- [参考资料](#-参考资料)

---

## 📖 什么是 Agent Skills？

Agent Skills 是扩展 AI 编程代理能力的模块化指令包。每个技能是一个独立的文件夹，包含 `SKILL.md`（核心指令）以及可选的脚本、模板和参考文档。当你让 AI 代理执行任务时，它会动态加载相关技能并按照指令执行 — 无需微调、无需 API 更改、无需复杂配置。

该标准受 Claude、Copilot、Codex、Gemini 等主流平台支持，技能可在所有兼容代理间通用。

---

## 🌟 为什么选这个 — 而不是另一个链接列表

互联网上有很多"awesome 列表"收集散落在 GitHub 各处的技能链接。**本项目采用完全不同的方式**：每个技能都在这里，完整实现，即取即用。

| | 链接列表 | **本技能库** |
|---|---|---|
| **你得到什么** | 指向 50+ 外部仓库的 URL | **51+ 完整实现，一个仓库搞定** |
| **脚本** | 自己去各个仓库找 | **23 个技能附带可运行脚本** |
| **模板** | 没有 | **14 个技能附带即用模板** |
| **安装** | 手动，逐个仓库 | **`skillctl` CLI — 一条命令** |
| **管理** | 做不到 | **按 IDE、按技能启用/停用** |
| **更新** | 每个仓库单独 `git pull` | **`skillctl update` — 一条命令** |
| **质量** | 未经验证 | **CI 自动验证结构和元数据** |

### 核心优势

- **`skillctl` CLI** — 首个技能管理器。从终端搜索、启用、停用、更新技能，按 IDE 精确控制
- **51+ 完整技能** — 不是链接。真实的 `SKILL.md` + 脚本 + 模板 + 参考文档，全在一个仓库
- **11 个 IDE 支持** — Cursor、Claude Code、Copilot、VS Code、Codex、Windsurf、Gemini CLI 等
- **按技能控制** — 不想要全部 51 个？按 IDE 只启用你需要的
- **CI 验证** — GitHub Actions 验证每个 SKILL.md 的结构有效性
- **6 种语言** — EN、简体中文、繁體中文、日本語、한국어、Español

---

## 🔌 兼容的 AI 代理

本合集兼容所有支持 Skill 标准的主流 AI 编码代理：

| Agent | 技能路径 | 文档 |
|-------|---------|------|
| Claude Code | `~/.claude/skills/` | [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills) |
| Claude.ai | 通过 UI 上传 | [support.claude.com](https://support.claude.com/en/articles/12512180-using-skills-in-claude) |
| GitHub Copilot | `.github/skills/` | [docs.github.com](https://docs.github.com/copilot/concepts/agents/about-agent-skills) |
| VS Code | `.github/skills/` | [code.visualstudio.com](https://code.visualstudio.com/docs/copilot/customization/agent-skills) |
| Codex (OpenAI) | `~/.codex/skills/` | [developers.openai.com](https://developers.openai.com/codex/skills) |
| Antigravity (Google) | `~/.gemini/antigravity/skills/` | [antigravity.google](https://antigravity.google/docs/skills) |
| Gemini CLI | `~/.gemini/skills/` | [geminicli.com](https://geminicli.com/docs/cli/skills/) |
| Kiro | 项目级 Skills | [kiro.dev](https://kiro.dev/docs/skills/) |
| Cursor | `~/.cursor/skills/` | 兼容 Skill 标准 |
| Windsurf | `~/.codeium/windsurf/skills/` | 兼容 Skill 标准 |
| OpenCode | `~/.config/opencode/skill/` | 兼容 Skill 标准 |
| Amp | `~/.config/agents/skills/` | 兼容 Skill 标准 |

---

## 🚀 快速开始

### 1. 克隆并使用 `skillctl`（推荐）

```bash
git clone https://github.com/ZhanlinCui/Ultimate-Agent-Skills-Collection.git ~/agent-skills
cd ~/agent-skills

# 查看所有可用技能
./skillctl list

# 为你的 IDE 配置技能
./skillctl setup cursor        # 或：claude, copilot, codex, windsurf...
./skillctl setup all           # 一次配置所有检测到的 IDE

# 按需启用/停用单个技能
./skillctl enable cursor docx
./skillctl disable cursor xlsx
./skillctl search "testing"
./skillctl status              # 查看各 IDE 的技能状态
./skillctl update              # 从 GitHub 拉取最新版本
```

### 2. 交互式安装器

```bash
chmod +x install.sh && ./install.sh
```

### 3. 手动符号链接

```bash
git clone https://github.com/ZhanlinCui/Ultimate-Agent-Skills-Collection.git ~/.agents/skills
mkdir -p ~/.cursor && ln -sf ~/.agents/skills ~/.cursor/skills
```

---

## 📂 技能目录

### 🎨 创意与设计

| 技能 | 描述 | 包含 |
|------|------|------|
| **[algorithmic-art](./creative/algorithmic-art/)** | 使用 p5.js 创建生成式艺术，支持种子随机数和交互参数探索 | `scripts` `templates` |
| **[canvas-design](./creative/canvas-design/)** | 使用设计理念创建精美的 .png 和 .pdf 可视化艺术作品 | `fonts` |
| **[frontend-design](./creative/frontend-design/)** | 构建独特的生产级前端界面，卓越的设计品质 | |
| **[brand-guidelines](./creative/brand-guidelines/)** | 将官方品牌色彩和字体应用到制品中 | |
| **[theme-factory](./creative/theme-factory/)** | 使用 10+ 预设主题或即时生成自定义主题 | `templates` |
| **[slack-gif-creator](./creative/slack-gif-creator/)** | 创建为 Slack 优化的动画 GIF | `scripts` |
| **[ui-ux-pro-max](./creative/ui-ux-pro-max/)** | 终极 UI/UX 设计智能：50+ 样式、97 配色方案、57 字体配对、99 UX 准则，支持 10 技术栈 | `scripts` `references` |

### 📄 文档技能

| 技能 | 描述 | 包含 |
|------|------|------|
| **[docx](./docs/docx/)** | 全面的 Word 文档创建、编辑，支持修订和批注 | `scripts` `templates` `references` |
| **[pdf](./docs/pdf/)** | PDF 操作 — 提取文本/表格、创建、合并/拆分、处理表单 | `scripts` |
| **[pptx](./docs/pptx/)** | PowerPoint 演示文稿创建、编辑、布局和演讲者备注 | `scripts` `references` |
| **[xlsx](./docs/xlsx/)** | 电子表格创建、编辑，支持公式、格式和数据分析 | `scripts` |
| **[doc-coauthoring](./docs/doc-coauthoring/)** | 文档和提案协作编写的结构化工作流 | |
| **[internal-comms](./docs/internal-comms/)** | 编写内部通信：状态报告、简报、FAQ、事故报告 | `templates` |
| **[github-release-assistant](./docs/github-release-assistant/)** | 生成双语 GitHub 发布文档（英文 + 中文） | `scripts` `templates` `references` |

### 📝 Obsidian 知识管理

| 技能 | 描述 | 包含 |
|------|------|------|
| **[obsidian-helper](./obsidian/obsidian-helper/)** | 智能笔记助手，支持 `/daily`、`/capture`、`/review` 命令，深度 MCP 集成 | `scripts` `references` |
| **[obsidian-bases](./obsidian/obsidian-bases/)** | 创建 Obsidian Bases (.base 文件)，支持视图、过滤器、公式和摘要 | |
| **[obsidian-markdown](./obsidian/obsidian-markdown/)** | 完整的 Obsidian 风格 Markdown 指南：wikilinks、嵌入、标注、属性、Mermaid、LaTeX | |
| **[project-to-obsidian](./obsidian/project-to-obsidian/)** | 将代码项目转换为 Obsidian 知识库，自动生成 API 文档、架构和模块文档 | `scripts` `templates` |
| **[json-canvas](./obsidian/json-canvas/)** | 创建 JSON Canvas 文件（.canvas），支持节点、边、组、流程图、思维导图 | |

### 🛠️ 开发与技术

| 技能 | 描述 | 包含 |
|------|------|------|
| **[mcp-builder](./dev/mcp-builder/)** | 创建高质量的 MCP（模型上下文协议）服务器 | `scripts` `templates` |
| **[webapp-testing](./dev/webapp-testing/)** | 使用 Playwright 测试本地 Web 应用，支持截图和日志 | `scripts` |
| **[web-artifacts-builder](./dev/web-artifacts-builder/)** | 使用 React、Tailwind 和 shadcn/ui 构建复杂 HTML 制品 | `scripts` |
| **[skill-creator](./dev/skill-creator/)** | 创建有效的 AI Agent 技能扩展指南 | `scripts` `templates` |
| **[deploying-to-production](./dev/deploying-to-production/)** | 自动化 GitHub 仓库创建和 Vercel 部署 | |
| **[internationalizing-websites](./dev/internationalizing-websites/)** | 为 Next.js 添加多语言支持和 SEO 配置 | `scripts` `templates` |

### 🔍 SEO 与性能

| 技能 | 描述 | 包含 |
|------|------|------|
| **[google-official-seo-guide](./seo/google-official-seo-guide/)** | 谷歌官方 SEO 指南：搜索优化、爬取、索引最佳实践 | `references` |
| **[web-performance-seo](./seo/web-performance-seo/)** | 修复 PageSpeed/Lighthouse 可访问性问题以优化 SEO | |

### 🧠 计划与工作流

| 技能 | 描述 | 包含 |
|------|------|------|
| **[planning-with-files](./planning/planning-with-files/)** | Manus 风格的文件规划：task_plan.md、findings.md、progress.md | `scripts` `templates` |
| **[writing-plans](./planning/writing-plans/)** | 在编码前创建多步骤任务的结构化计划 | |
| **[executing-plans](./planning/executing-plans/)** | 带审查检查点的实施计划执行 | |
| **[brainstorming](./planning/brainstorming/)** | 实施前探索用户意图、需求和设计 | |
| **[chat-compactor](./planning/chat-compactor/)** | 生成会话摘要以实现 AI Agent 跨会话连续性 | |

### 🐛 调试与质量

| 技能 | 描述 | 包含 |
|------|------|------|
| **[systematic-debugging](./quality/systematic-debugging/)** | 系统化调试方法：修复前先做根因分析 | `scripts` `references` |
| **[test-driven-development](./quality/test-driven-development/)** | TDD 工作流：先写测试，再写实现 | `templates` |
| **[verification-before-completion](./quality/verification-before-completion/)** | 声明完成前验证工作是否真正完成 | |
| **[receiving-code-review](./quality/receiving-code-review/)** | 以技术严谨性处理代码审查反馈 | |
| **[requesting-code-review](./quality/requesting-code-review/)** | 为已完成的工作请求全面的代码审查 | `templates` |

### 🤖 Agent 编排

| 技能 | 描述 | 包含 |
|------|------|------|
| **[dispatching-parallel-agents](./agent/dispatching-parallel-agents/)** | 将 2+ 个独立任务分派给并行子 Agent | |
| **[subagent-driven-development](./agent/subagent-driven-development/)** | 使用专门的子 Agent 执行计划中的每个任务 | `scripts` `templates` |
| **[using-superpowers](./agent/using-superpowers/)** | 确定如何在对话中查找和使用技能 | |
| **[writing-skills](./agent/writing-skills/)** | 在部署前创建、编辑和验证技能 | `scripts` `templates` `examples` |

### 🔧 Git 与开发工作流

| 技能 | 描述 | 包含 |
|------|------|------|
| **[using-git-worktrees](./git-workflow/using-git-worktrees/)** | 为功能开发创建隔离的 git worktree | |
| **[finishing-a-development-branch](./git-workflow/finishing-a-development-branch/)** | 引导完成：合并、PR 或清理选项 | |

### 🔗 集成与自动化

| 技能 | 描述 | 包含 |
|------|------|------|
| **[notebooklm](./integration/notebooklm/)** | 通过浏览器自动化查询 Google NotebookLM | `scripts` |
| **[x-article-publisher](./integration/x-article-publisher/)** | 将 Markdown 文章发布到 X（Twitter）Articles | `scripts` |
| **[doc-sync-tool](./integration/doc-sync-tool/)** | 跨项目自动同步 Agents.md、claude.md、gemini.md 文件 | `scripts` |
| **[daily-news](./integration/daily-news/)** | 每日资讯日报生成器：三阶段工作流（获取元数据→生成摘要→输出日报），支持自定义信源 | `scripts` `references` |
| **[web-access](./integration/web-access/)** | 让 AI Agent 真正能上网：智能通道选择（WebSearch→WebFetch→浏览器 CDP），持久化登录态 | `scripts` `references` |

### 🔺 Vercel 官方

| 技能 | 描述 | 包含 |
|------|------|------|
| **[vercel-deploy](./vercel/vercel-deploy/)** | 一键部署任何项目到 Vercel，无需认证，返回预览 URL | `scripts` |
| **[vercel-react-best-practices](./vercel/vercel-react-best-practices/)** | Vercel 工程团队出品的 45 条 React/Next.js 性能规则 | `rules` |
| **[vercel-web-design-guidelines](./vercel/vercel-web-design-guidelines/)** | 审查 UI 代码是否符合 Web 界面准则，可访问性和 UX 审计 | |

---

## 📚 官方技能参考

这些是 AI 平台提供商的官方技能实现：

### Anthropic (Claude)

| 技能 | 描述 | 来源 |
|------|------|------|
| docx | 创建、编辑、分析 Word 文档，支持修订 | [anthropics/skills](https://github.com/anthropics/skills) |
| xlsx | 电子表格操作：公式、图表、数据转换 | [anthropics/skills](https://github.com/anthropics/skills) |
| pptx | 读取、生成和调整幻灯片、布局、模板 | [anthropics/skills](https://github.com/anthropics/skills) |
| pdf | 从 PDF 提取文本、表格、元数据 | [anthropics/skills](https://github.com/anthropics/skills) |

### OpenAI (Codex)

| 技能范围 | 路径 | 建议用途 |
|---------|------|---------|
| REPO | `$CWD/.codex/skills` | 与工作目录相关的技能 |
| USER | `~/.codex/skills` | 适用于所有仓库的个人技能 |
| ADMIN | `/etc/codex/skills` | SDK 脚本、自动化技能 |
| SYSTEM | Codex 内置 | 内置技能如 skill-creator |

### HuggingFace

| 技能 | 描述 | 来源 |
|------|------|------|
| hf_dataset_creator | 创建结构化训练数据集的提示、模板和脚本 | [huggingface/skills](https://github.com/huggingface/skills) |
| hf_model_evaluation | 编排评估任务、生成报告和映射指标 | [huggingface/skills](https://github.com/huggingface/skills) |
| hf-llm-trainer | 包含指导、辅助脚本和成本估算器的全面训练技能 | [huggingface/skills](https://github.com/huggingface/skills) |
| hf-paper-publisher | 在 Hugging Face Hub 上发布和管理研究论文的工具 | [huggingface/skills](https://github.com/huggingface/skills) |

---

## 🌐 社区技能与合集

值得探索的经过验证的社区维护技能和合集：

| 仓库 | 描述 |
|------|------|
| [anthropics/skills](https://github.com/anthropics/skills) | Anthropic 官方合集（文档编辑、数据分析） |
| [openai/skills](https://github.com/openai/skills) | OpenAI Codex 官方技能目录 |
| [huggingface/skills](https://github.com/huggingface/skills) | HuggingFace 技能（兼容 Claude、Codex、Gemini） |
| [heilcheng/awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills) | 技能链接和资源精选列表 |
| [skillcreatorai/Ai-Agent-Skills](https://github.com/skillcreatorai/Ai-Agent-Skills) | SkillCreator.ai 合集，附带 CLI 安装器 |
| [agentskill.sh](https://agentskill.sh) | 44k+ 技能目录，带安全扫描 |
| [dmgrok/agent_skills_directory](https://github.com/dmgrok/agent_skills_directory) | npm 风格的技能 CLI — 聚合 24 个提供商的 177+ 技能 |
| [gotalab/skillport](https://github.com/gotalab/skillport) | 通过 CLI 或 MCP 分发技能 |
| [karanb192/awesome-claude-skills](https://github.com/karanb192/awesome-claude-skills) | 50+ 经验证的 Claude Code 和 Claude.ai 技能 |
| [transloadit/skills](https://github.com/transloadit/skills) | 媒体处理：视频编码、图像处理、OCR |

---

## ⚙️ IDE/Agent 配置

### 快速配置（所有 IDE）

```bash
# 克隆合集
git clone https://github.com/ZhanlinCui/Ultimate-Agent-Skills-Collection.git ~/.agents/skills
```

### 支持的 IDE 与配置路径

| IDE | 默认技能路径 | 符号链接命令 |
|-----|------------|------------|
| **Cursor** | `~/.cursor/skills/` | `mkdir -p ~/.cursor && ln -sf ~/.agents/skills ~/.cursor/skills` |
| **Claude Code** | `~/.claude/skills/` | `mkdir -p ~/.claude && ln -sf ~/.agents/skills ~/.claude/skills` |
| **GitHub Copilot** | `~/.copilot/skills/` | `mkdir -p ~/.copilot && ln -sf ~/.agents/skills ~/.copilot/skills` |
| **VS Code** | `.github/skills/` | `mkdir -p ~/.copilot && ln -sf ~/.agents/skills ~/.copilot/skills` |
| **Codex (OpenAI)** | `~/.codex/skills/` | `mkdir -p ~/.codex && ln -sf ~/.agents/skills ~/.codex/skills` |
| **Antigravity** | `~/.gemini/antigravity/skills/` | `mkdir -p ~/.gemini/antigravity && ln -sf ~/.agents/skills ~/.gemini/antigravity/skills` |
| **Gemini CLI** | `~/.gemini/skills/` | `mkdir -p ~/.gemini && ln -sf ~/.agents/skills ~/.gemini/skills` |
| **Windsurf** | `~/.codeium/windsurf/skills/` | `mkdir -p ~/.codeium/windsurf && ln -sf ~/.agents/skills ~/.codeium/windsurf/skills` |
| **OpenCode** | `~/.config/opencode/skill/` | `mkdir -p ~/.config/opencode && ln -sf ~/.agents/skills ~/.config/opencode/skill` |
| **Amp** | `~/.config/agents/skills/` | `mkdir -p ~/.config/agents && ln -sf ~/.agents/skills ~/.config/agents/skills` |
| **iFlow** | `~/.iflow/skills/` | `mkdir -p ~/.iflow && ln -sf ~/.agents/skills ~/.iflow/skills` |

### 一键配置所有 IDE

```bash
git clone https://github.com/ZhanlinCui/Ultimate-Agent-Skills-Collection.git ~/.agents/skills

mkdir -p ~/.cursor ~/.claude ~/.copilot ~/.codex ~/.gemini ~/.gemini/antigravity \
         ~/.codeium/windsurf ~/.config/opencode ~/.config/agents ~/.iflow

ln -sf ~/.agents/skills ~/.cursor/skills
ln -sf ~/.agents/skills ~/.claude/skills
ln -sf ~/.agents/skills ~/.copilot/skills
ln -sf ~/.agents/skills ~/.codex/skills
ln -sf ~/.agents/skills ~/.gemini/skills
ln -sf ~/.agents/skills ~/.gemini/antigravity/skills
ln -sf ~/.agents/skills ~/.codeium/windsurf/skills
ln -sf ~/.agents/skills ~/.config/opencode/skill
ln -sf ~/.agents/skills ~/.config/agents/skills
ln -sf ~/.agents/skills ~/.iflow/skills

echo "✅ 所有 IDE 技能配置完成！"
```

---

## 📖 官方教程与指南

### Claude & Anthropic

- [在 Claude 中使用 Skills](https://support.claude.com/en/articles/12512180-using-skills-in-claude) — 官方快速入门
- [如何创建自定义 Skills](https://support.claude.com/en/articles/12512198-creating-custom-skills) — 分步创建指南
- [Claude Code Skills 文档](https://code.claude.com/docs/en/skills) — 官方参考

### GitHub Copilot & VS Code

- [关于 Agent Skills](https://docs.github.com/copilot/concepts/agents/about-agent-skills) — GitHub 文档
- [VS Code Agent Skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills) — VS Code 集成

### OpenAI Codex

- [Codex Skills 文档](https://developers.openai.com/codex/skills) — 官方参考

### 模型上下文协议 (MCP)

- [MCP 官方文档](https://modelcontextprotocol.io/) — 开放标准
- [构建你的第一个 MCP Server](https://modelcontextprotocol.io/docs/first-server) — Python/TypeScript 指南
- [MCP Server 示例](https://github.com/modelcontextprotocol/servers) — 官方服务器实现

---

## ❓ 常见问题

### 什么是 Agent Skills？

Agent Skills 是教 AI 助手如何完成特定任务的指令文件。把它们想象成 AI 阅读和遵循的"操作指南"。它们按需加载，所以 AI 保持快速和专注。

### 这个合集和其他技能合集有什么不同？

大多数合集是**链接目录** — 它们列出指向外部仓库的链接。这个合集包含 **51+ 完整技能实现**，附带脚本、模板和参考文档。克隆一次就能获得所有可用的内容。

### Agent Skills 和微调有什么区别？

微调永久改变 AI 的思维方式（昂贵且难以更新）。Agent Skills 只是指令文件 — 你可以随时更新、替换或分享，无需修改 AI 本身。

### Agent Skills 和 MCP 有什么区别？

它们互为补充：
- **Agent Skills** = 教 AI *如何*做某事（工作流、最佳实践）
- **MCP** = 帮助 AI *访问*事物（API、数据库、外部工具）

### 哪些 AI 工具支持 Agent Skills？

目前支持：**Claude**（Claude.ai 和 Claude Code）、**GitHub Copilot**、**VS Code**、**Codex**（OpenAI）、**Antigravity**（Google）、**Gemini CLI**、**Kiro**、**Cursor**、**Windsurf**、**OpenCode** 和 **Amp**。支持列表还在增长。

### Agent Skills 会执行代码吗？

不会。Skills 是文本指令 — AI 像读食谱一样阅读并遵循。某些 Skills 包含 AI *可以*执行的辅助脚本，但 Skill 本身只是指令。

### 如何创建自己的 Skill？

1. 创建包含 `SKILL.md` 的文件夹（含名称和描述）
2. 编写清晰、分步的指令
3. 可选地添加脚本、模板或参考文档
4. 放入你的 IDE 技能目录
5. 完整指南：[如何创建自定义 Skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)

### 可以同时在多个 IDE 中使用这些技能吗？

可以！使用 `install.sh` 脚本或上面的一键配置脚本，同时为所有 IDE 配置技能。Skills 只是文件 — 它们可以在任何兼容的 Agent 中使用。

---

## 🏷️ 技能快速参考

| 分类 | 数量 | 亮点 |
|------|------|------|
| 🎨 创意与设计 | 7 | algorithmic-art, frontend-design, ui-ux-pro-max |
| 📄 文档技能 | 7 | docx, pdf, pptx, xlsx |
| 📝 Obsidian 知识管理 | 5 | obsidian-helper, obsidian-bases, project-to-obsidian |
| 🛠️ 开发与技术 | 6 | mcp-builder, webapp-testing, skill-creator |
| 🔍 SEO 与性能 | 2 | google-official-seo-guide, web-performance-seo |
| 🧠 计划与工作流 | 5 | planning-with-files, chat-compactor |
| 🐛 调试与质量 | 5 | systematic-debugging, test-driven-development |
| 🤖 Agent 编排 | 4 | dispatching-parallel-agents, subagent-driven-development |
| 🔧 Git 与工作流 | 2 | using-git-worktrees, finishing-a-development-branch |
| 🔗 集成与自动化 | 5 | notebooklm, x-article-publisher, daily-news, web-access |
| 🔺 Vercel 官方 | 3 | vercel-deploy, vercel-react-best-practices |

### 技能结构

每个技能遵循一致的结构：

```
skill-name/
├── SKILL.md          # 主要指令（必需）
├── scripts/          # 辅助脚本（可选）
├── templates/        # 模板文件（可选）
├── references/       # 参考文档（可选）
└── examples/         # 使用示例（可选）
```

---

## 🤝 参与贡献

我们欢迎贡献！请查看 **[CONTRIBUTING.md](CONTRIBUTING.md)** 了解完整指南。

快速摘要：

1. Fork 本仓库
2. 创建包含 `SKILL.md` 的技能文件夹（以及可选的脚本/模板）
3. 将技能添加到 README 中正确的分类
4. 提交 Pull Request

质量要求：
- `SKILL.md` 必须包含有效的 frontmatter（`name`、`description`）
- 指令清晰、可操作
- 不含推广或营销语言
- 500 行以内以获得最佳性能
- 脚本必须经过测试

---

## 📜 许可证

MIT 许可证 — 详见 [LICENSE](LICENSE)。

---

## ⭐ Star 历史

<a href="https://star-history.com/#ZhanlinCui/Ultimate-Agent-Skills-Collection&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=ZhanlinCui/Ultimate-Agent-Skills-Collection&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=ZhanlinCui/Ultimate-Agent-Skills-Collection&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=ZhanlinCui/Ultimate-Agent-Skills-Collection&type=Date" />
 </picture>
</a>

---

## 📚 参考资料

- [Anthropic: 在 Claude 中使用 Skills](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [Anthropic: 创建自定义 Skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- [Claude Code Skills 文档](https://code.claude.com/docs/en/skills)
- [GitHub Copilot: 关于 Agent Skills](https://docs.github.com/copilot/concepts/agents/about-agent-skills)
- [VS Code Agent Skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills)
- [OpenAI Codex Skills](https://developers.openai.com/codex/skills)
- [Google Antigravity Skills](https://antigravity.google/docs/skills)
- [模型上下文协议文档](https://modelcontextprotocol.io/)

---

<div align="center">

**为 AI Agent 社区用心打造 ❤️**

*终极生产级 Agent 技能库*

</div>
