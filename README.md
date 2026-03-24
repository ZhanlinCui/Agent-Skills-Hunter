# Ultimate Agent Skills Collection

<div align="center">

<img src="https://img.shields.io/badge/Skills-51+-blueviolet?style=for-the-badge" alt="Skills Count" />
<img src="https://img.shields.io/badge/Quality-Premium-gold?style=for-the-badge" alt="Quality" />
<img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License" />
<img src="https://img.shields.io/badge/Languages-6-blue?style=for-the-badge" alt="Languages" />

<br />

<img src="https://img.shields.io/github/stars/ZhanlinCui/Ultimate-Agent-Skills-Collection?style=social" alt="Stars" />
<img src="https://img.shields.io/github/forks/ZhanlinCui/Ultimate-Agent-Skills-Collection?style=social" alt="Forks" />
<img src="https://img.shields.io/github/last-commit/ZhanlinCui/Ultimate-Agent-Skills-Collection" alt="Last Commit" />
<img src="https://img.shields.io/github/contributors/ZhanlinCui/Ultimate-Agent-Skills-Collection" alt="Contributors" />

**The Most Comprehensive Production-Ready Agent Skills Library on the Internet**

*Not just links — real implementations with scripts, templates, and references you can use today.*

[简体中文](./README.zh-CN.md) | [繁體中文](./README.zh-TW.md) | [日本語](./README.ja.md) | [한국어](./README.ko.md) | [Español](./README.es.md)

</div>

---

## Table of Contents

- [What Are Agent Skills?](#-what-are-agent-skills)
- [Why This Collection is Different](#-why-this-collection-is-different)
- [Compatible Agents](#-compatible-agents)
- [Quick Start](#-quick-start)
- [Skills Directory](#-skills-directory)
- [Official Skills References](#-official-skills-references)
- [Community Skills & Collections](#-community-skills--collections)
- [IDE/Agent Configuration](#-ideagent-configuration)
- [Official Tutorials and Guides](#-official-tutorials-and-guides)
- [FAQ](#-faq)
- [Contributing](#-contributing)
- [License](#-license)
- [Star History](#-star-history)
- [References](#-references)

---

## 📖 What Are Agent Skills?

Agent Skills are modular instruction packages that extend what AI coding agents can do. Each skill is a self-contained folder with a `SKILL.md` file (the core instructions) plus optional scripts, templates, and references. When you ask an AI agent to perform a task, it dynamically loads the relevant skill and follows the instructions — no fine-tuning, no API changes, no configuration.

This standard is supported by Claude, Copilot, Codex, Gemini, and more. Skills are portable across all compatible agents.

---

## 🌟 Why This Collection — Not Another Link List

There are many "awesome lists" that collect links to skills scattered across GitHub. **This project takes a completely different approach**: every skill lives here, fully implemented, ready to use.

| | Link Lists | **This Library** |
|---|---|---|
| **What you get** | URLs to 50+ external repos | **51+ complete implementations in one repo** |
| **Scripts** | Go find them yourself | **23 skills include working scripts** |
| **Templates** | None | **14 skills include ready-to-use templates** |
| **Install** | Manual, per-repo | **`skillctl` CLI — one command** |
| **Manage** | Can't | **Enable/disable per IDE, per skill** |
| **Update** | `git pull` each repo | **`skillctl update` — one command** |
| **Quality** | Unverified | **CI-validated structure + frontmatter** |

### Core Advantages

- **`skillctl` CLI** — The first skill manager. Search, enable, disable, update skills per IDE from your terminal
- **51+ Complete Skills** — Not links. Real `SKILL.md` + scripts + templates + references, all in one repo
- **11 IDE Support** — Cursor, Claude Code, Copilot, VS Code, Codex, Windsurf, Gemini CLI, and more
- **Per-Skill Control** — Don't want all 51? Enable only what you need per IDE
- **CI Validated** — GitHub Actions verify every SKILL.md has valid structure
- **6 Languages** — EN, 简体中文, 繁體中文, 日本語, 한국어, Español

---

## 🔌 Compatible Agents

This collection works with all major AI coding agents that support the skill standard:

| Agent | Skill Path | Documentation |
|-------|-----------|---------------|
| Claude Code | `~/.claude/skills/` | [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills) |
| Claude.ai | Upload via UI | [support.claude.com](https://support.claude.com/en/articles/12512180-using-skills-in-claude) |
| GitHub Copilot | `.github/skills/` | [docs.github.com](https://docs.github.com/copilot/concepts/agents/about-agent-skills) |
| VS Code | `.github/skills/` | [code.visualstudio.com](https://code.visualstudio.com/docs/copilot/customization/agent-skills) |
| Codex (OpenAI) | `~/.codex/skills/` | [developers.openai.com](https://developers.openai.com/codex/skills) |
| Antigravity (Google) | `~/.gemini/antigravity/skills/` | [antigravity.google](https://antigravity.google/docs/skills) |
| Gemini CLI | `~/.gemini/skills/` | [geminicli.com](https://geminicli.com/docs/cli/skills/) |
| Kiro | Project skills | [kiro.dev](https://kiro.dev/docs/skills/) |
| Cursor | `~/.cursor/skills/` | Skill-compatible |
| Windsurf | `~/.codeium/windsurf/skills/` | Skill-compatible |
| OpenCode | `~/.config/opencode/skill/` | Skill-compatible |
| Amp | `~/.config/agents/skills/` | Skill-compatible |

---

## 🚀 Quick Start

### 1. Clone & Use `skillctl` (Recommended)

```bash
git clone https://github.com/ZhanlinCui/Ultimate-Agent-Skills-Collection.git ~/agent-skills
cd ~/agent-skills

# See all available skills
./skillctl list

# Set up all skills for your IDE
./skillctl setup cursor        # or: claude, copilot, codex, windsurf...
./skillctl setup all           # configure all detected IDEs at once

# Enable/disable individual skills
./skillctl enable cursor docx
./skillctl disable cursor xlsx
./skillctl search "testing"
./skillctl status
./skillctl update              # pull latest from GitHub
```

### 2. Interactive Installer (Alternative)

```bash
chmod +x install.sh && ./install.sh
```

### 3. Manual Symlink

```bash
git clone https://github.com/ZhanlinCui/Ultimate-Agent-Skills-Collection.git ~/.agents/skills
mkdir -p ~/.cursor && ln -sf ~/.agents/skills ~/.cursor/skills
```

---

## 📂 Skills Directory

### 🎨 Creative & Design

| Skill | Description | Includes |
|-------|-------------|----------|
| **[algorithmic-art](./creative/algorithmic-art/)** | Create generative art using p5.js with seeded randomness and interactive parameter exploration | `scripts` `templates` |
| **[canvas-design](./creative/canvas-design/)** | Create beautiful visual art in .png and .pdf documents using design philosophy | `fonts` |
| **[frontend-design](./creative/frontend-design/)** | Build distinctive, production-grade frontend interfaces with exceptional design quality | |
| **[brand-guidelines](./creative/brand-guidelines/)** | Apply official brand colors and typography to artifacts | |
| **[theme-factory](./creative/theme-factory/)** | Style artifacts with 10+ pre-set themes or generate custom themes on-the-fly | `templates` |
| **[slack-gif-creator](./creative/slack-gif-creator/)** | Create animated GIFs optimized for Slack with proper constraints | `scripts` |
| **[ui-ux-pro-max](./creative/ui-ux-pro-max/)** | Ultimate UI/UX design intelligence: 50+ styles, 97 color palettes, 57 font pairings, 99 UX guidelines. Supports 10 tech stacks | `scripts` `references` |

### 📄 Document Skills

| Skill | Description | Includes |
|-------|-------------|----------|
| **[docx](./docs/docx/)** | Comprehensive Word document creation, editing with tracked changes and comments | `scripts` `templates` `references` |
| **[pdf](./docs/pdf/)** | PDF manipulation — extract text/tables, create, merge/split, handle forms | `scripts` |
| **[pptx](./docs/pptx/)** | PowerPoint presentation creation, editing, layouts, and speaker notes | `scripts` `references` |
| **[xlsx](./docs/xlsx/)** | Spreadsheet creation, editing with formulas, formatting, and data analysis | `scripts` |
| **[doc-coauthoring](./docs/doc-coauthoring/)** | Structured workflow for co-authoring documentation and proposals | |
| **[internal-comms](./docs/internal-comms/)** | Write internal communications: status reports, newsletters, FAQs, incident reports | `templates` |
| **[github-release-assistant](./docs/github-release-assistant/)** | Generate bilingual GitHub release documentation (English + Chinese) | `scripts` `templates` `references` |

### 📝 Obsidian Knowledge Management

| Skill | Description | Includes |
|-------|-------------|----------|
| **[obsidian-helper](./obsidian/obsidian-helper/)** | Smart note assistant with `/daily`, `/capture`, `/review` commands. Deep MCP integration | `scripts` `references` |
| **[obsidian-bases](./obsidian/obsidian-bases/)** | Create Obsidian Bases (.base files) with views, filters, formulas, and summaries | |
| **[obsidian-markdown](./obsidian/obsidian-markdown/)** | Complete Obsidian Flavored Markdown guide: wikilinks, embeds, callouts, properties, Mermaid, LaTeX | |
| **[project-to-obsidian](./obsidian/project-to-obsidian/)** | Convert code projects to Obsidian knowledge bases. Auto-generate API docs, architecture, module docs | `scripts` `templates` |
| **[json-canvas](./obsidian/json-canvas/)** | Create JSON Canvas files (.canvas) for Obsidian: nodes, edges, groups, flowcharts, mind maps | |

### 🛠️ Development & Technical

| Skill | Description | Includes |
|-------|-------------|----------|
| **[mcp-builder](./dev/mcp-builder/)** | Create high-quality MCP (Model Context Protocol) servers for LLM integrations | `scripts` `templates` |
| **[webapp-testing](./dev/webapp-testing/)** | Test local web applications using Playwright with screenshots and logs | `scripts` |
| **[web-artifacts-builder](./dev/web-artifacts-builder/)** | Build complex HTML artifacts with React, Tailwind, and shadcn/ui | `scripts` |
| **[skill-creator](./dev/skill-creator/)** | Guide for creating effective skills that extend AI agent capabilities | `scripts` `templates` |
| **[deploying-to-production](./dev/deploying-to-production/)** | Automate GitHub repository creation and Vercel deployment | |
| **[internationalizing-websites](./dev/internationalizing-websites/)** | Add multi-language support to Next.js with proper SEO configuration | `scripts` `templates` |

### 🔍 SEO & Performance

| Skill | Description | Includes |
|-------|-------------|----------|
| **[google-official-seo-guide](./seo/google-official-seo-guide/)** | Official Google SEO guide: search optimization, crawling, indexing best practices | `references` |
| **[web-performance-seo](./seo/web-performance-seo/)** | Fix PageSpeed/Lighthouse accessibility errors for SEO optimization | |

### 🧠 Planning & Workflow

| Skill | Description | Includes |
|-------|-------------|----------|
| **[planning-with-files](./planning/planning-with-files/)** | Manus-style file-based planning with task_plan.md, findings.md, progress.md | `scripts` `templates` |
| **[writing-plans](./planning/writing-plans/)** | Create structured plans for multi-step tasks before coding | |
| **[executing-plans](./planning/executing-plans/)** | Execute written implementation plans with review checkpoints | |
| **[brainstorming](./planning/brainstorming/)** | Explore user intent, requirements and design before implementation | |
| **[chat-compactor](./planning/chat-compactor/)** | Generate session summaries for AI agent continuity across sessions | |

### 🐛 Debugging & Quality

| Skill | Description | Includes |
|-------|-------------|----------|
| **[systematic-debugging](./quality/systematic-debugging/)** | Systematic approach to debugging: root cause analysis before fixes | `scripts` `references` |
| **[test-driven-development](./quality/test-driven-development/)** | TDD workflow: write tests first, then implementation | `templates` |
| **[verification-before-completion](./quality/verification-before-completion/)** | Verify work is complete before claiming success | |
| **[receiving-code-review](./quality/receiving-code-review/)** | Handle code review feedback with technical rigor | |
| **[requesting-code-review](./quality/requesting-code-review/)** | Request thorough code reviews for completed work | `templates` |

### 🤖 Agent Orchestration

| Skill | Description | Includes |
|-------|-------------|----------|
| **[dispatching-parallel-agents](./agent/dispatching-parallel-agents/)** | Dispatch 2+ independent tasks to parallel subagents | |
| **[subagent-driven-development](./agent/subagent-driven-development/)** | Execute plans with specialized subagents for each task | `scripts` `templates` |
| **[using-superpowers](./agent/using-superpowers/)** | Establish how to find and use skills in conversations | |
| **[writing-skills](./agent/writing-skills/)** | Create, edit, and verify skills before deployment | `scripts` `templates` `examples` |

### 🔧 Git & Development Workflow

| Skill | Description | Includes |
|-------|-------------|----------|
| **[using-git-worktrees](./git-workflow/using-git-worktrees/)** | Create isolated git worktrees for feature development | |
| **[finishing-a-development-branch](./git-workflow/finishing-a-development-branch/)** | Guide completion: merge, PR, or cleanup options | |

### 🔗 Integration & Automation

| Skill | Description | Includes |
|-------|-------------|----------|
| **[notebooklm](./integration/notebooklm/)** | Query Google NotebookLM for source-grounded answers via browser automation | `scripts` |
| **[x-article-publisher](./integration/x-article-publisher/)** | Publish Markdown articles to X (Twitter) Articles with proper formatting | `scripts` |
| **[doc-sync-tool](./integration/doc-sync-tool/)** | Auto-sync Agents.md, claude.md, gemini.md files across projects | `scripts` |
| **[daily-news](./integration/daily-news/)** | Three-phase daily news report generator: fetch metadata, generate summaries, output reports. Custom sources supported | `scripts` `references` |
| **[web-access](./integration/web-access/)** | Enable AI agents to truly browse the web: smart channel selection from WebSearch to WebFetch to browser CDP mode | `scripts` `references` |

### 🔺 Vercel Official

| Skill | Description | Includes |
|-------|-------------|----------|
| **[vercel-deploy](./vercel/vercel-deploy/)** | Deploy any project to Vercel instantly. No auth required — returns preview URL | `scripts` |
| **[vercel-react-best-practices](./vercel/vercel-react-best-practices/)** | 45 performance rules for React/Next.js from Vercel Engineering | `rules` |
| **[vercel-web-design-guidelines](./vercel/vercel-web-design-guidelines/)** | Review UI code for Web Interface Guidelines compliance. Accessibility, UX audit | |

---

## 📚 Official Skills References

These are official skill implementations from AI platform providers:

### Anthropic (Claude)

| Skill | Description | Source |
|-------|-------------|--------|
| docx | Create, edit, analyze Word documents with tracked changes | [anthropics/skills](https://github.com/anthropics/skills) |
| xlsx | Spreadsheet manipulation: formulas, charts, data transformations | [anthropics/skills](https://github.com/anthropics/skills) |
| pptx | Read, generate, and adjust slides, layouts, templates | [anthropics/skills](https://github.com/anthropics/skills) |
| pdf | Extract text, tables, metadata from PDFs | [anthropics/skills](https://github.com/anthropics/skills) |

### OpenAI (Codex)

| Skill Scope | Location | Suggested Use |
|-------------|----------|---------------|
| REPO | `$CWD/.codex/skills` | Skills relevant to a working folder |
| USER | `~/.codex/skills` | Personal skills for any repository |
| ADMIN | `/etc/codex/skills` | SDK scripts, automation skills |
| SYSTEM | Bundled with Codex | Built-in skills like skill-creator |

### HuggingFace

| Skill | Description | Source |
|-------|-------------|--------|
| hf_dataset_creator | Prompts, templates, and scripts for creating structured training datasets | [huggingface/skills](https://github.com/huggingface/skills) |
| hf_model_evaluation | Orchestrating evaluation jobs, generating reports, and mapping metrics | [huggingface/skills](https://github.com/huggingface/skills) |
| hf-llm-trainer | Comprehensive training skill with guidance, helper scripts, cost estimators | [huggingface/skills](https://github.com/huggingface/skills) |
| hf-paper-publisher | Tools for publishing and managing research papers on Hugging Face Hub | [huggingface/skills](https://github.com/huggingface/skills) |

---

## 🌐 Community Skills & Collections

Verified community-maintained skills and collections worth exploring:

| Repository | Description |
|------------|-------------|
| [anthropics/skills](https://github.com/anthropics/skills) | Official Anthropic collection (document editing, data analysis) |
| [openai/skills](https://github.com/openai/skills) | Official OpenAI Codex skills catalog |
| [huggingface/skills](https://github.com/huggingface/skills) | HuggingFace skills (compatible with Claude, Codex, Gemini) |
| [heilcheng/awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills) | Curated list of skill links and resources |
| [skillcreatorai/Ai-Agent-Skills](https://github.com/skillcreatorai/Ai-Agent-Skills) | SkillCreator.ai collection with CLI installer |
| [agentskill.sh](https://agentskill.sh) | 44k+ skills directory with security scanning |
| [dmgrok/agent_skills_directory](https://github.com/dmgrok/agent_skills_directory) | npm-like CLI for skills — aggregates 177+ skills from 24 providers |
| [gotalab/skillport](https://github.com/gotalab/skillport) | Skills distribution via CLI or MCP |
| [karanb192/awesome-claude-skills](https://github.com/karanb192/awesome-claude-skills) | 50+ verified skills for Claude Code and Claude.ai |
| [transloadit/skills](https://github.com/transloadit/skills) | Media processing: video encoding, image manipulation, OCR |
| [SkyworkAI/Skywork-Skills](https://github.com/SkyworkAI/Skywork-Skills) | Official Skywork agent skills for AI office workflows: PPT, documents, Excel, design, search, and music |

---

## ⚙️ IDE/Agent Configuration

### Quick Setup (All IDEs)

```bash
# Clone the collection
git clone https://github.com/ZhanlinCui/Ultimate-Agent-Skills-Collection.git ~/.agents/skills
```

### Supported IDEs & Configuration Paths

| IDE | Default Skill Path | Symlink Command |
|-----|-------------------|-----------------|
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

### All-in-One Setup Script

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

echo "✅ Skills configured for all IDEs!"
```

---

## 📖 Official Tutorials and Guides

### Claude & Anthropic

- [Using Skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude) — Official quick start guide
- [How to Create Custom Skills](https://support.claude.com/en/articles/12512198-creating-custom-skills) — Step-by-step authoring
- [Claude Code Skills Documentation](https://code.claude.com/docs/en/skills) — Official reference

### GitHub Copilot & VS Code

- [About Agent Skills](https://docs.github.com/copilot/concepts/agents/about-agent-skills) — GitHub documentation
- [VS Code Agent Skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills) — VS Code integration

### OpenAI Codex

- [Codex Skills Documentation](https://developers.openai.com/codex/skills) — Official reference

### Model Context Protocol (MCP)

- [MCP Official Documentation](https://modelcontextprotocol.io/) — The open standard
- [Build Your First MCP Server](https://modelcontextprotocol.io/docs/first-server) — Python/TypeScript guide
- [MCP Server Examples](https://github.com/modelcontextprotocol/servers) — Official server implementations

---

## ❓ FAQ

### What are Agent Skills?

Agent Skills are instruction files that teach AI assistants how to do specific tasks. Think of them as "how-to guides" that the AI reads and follows. They only load when needed, so the AI stays fast and focused.

### How is this different from other skill collections?

Most collections are **link directories** — they list links to external repositories. This collection contains **51+ complete skill implementations** with scripts, templates, and reference documentation. Clone once and you have everything ready to use.

### How are Agent Skills different from fine-tuning?

Fine-tuning permanently changes how an AI thinks (expensive and hard to update). Agent Skills are just instruction files — you can update, swap, or share them anytime without touching the AI itself.

### What's the difference between Agent Skills and MCP?

They complement each other:
- **Agent Skills** = teach the AI *how* to do something (workflows, best practices)
- **MCP** = help the AI *access* things (APIs, databases, external tools)

### Which AI tools support Agent Skills?

Currently supported: **Claude** (Claude.ai and Claude Code), **GitHub Copilot**, **VS Code**, **Codex** (OpenAI), **Antigravity** (Google), **Gemini CLI**, **Kiro**, **Cursor**, **Windsurf**, **OpenCode**, and **Amp**. The list is growing.

### Do Agent Skills run code?

No. Skills are text instructions — the AI reads and follows them like a recipe. Some skills *include* helper scripts that the AI *can* execute, but the skill itself is just instructions.

### How do I create my own skill?

1. Create a folder with a `SKILL.md` file containing a name and description
2. Write clear, step-by-step instructions
3. Optionally add scripts, templates, or references
4. Place it in your IDE's skill directory
5. Full guide: [How to create custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)

### Can I use these skills with multiple IDEs at the same time?

Yes! Use the `install.sh` script or the all-in-one setup script above to configure skills for all your IDEs simultaneously. Skills are just files — they work across any compatible agent.

---

## 🏷️ Skills Quick Reference

| Category | Count | Highlights |
|----------|-------|------------|
| 🎨 Creative & Design | 7 | algorithmic-art, frontend-design, ui-ux-pro-max |
| 📄 Document Skills | 7 | docx, pdf, pptx, xlsx |
| 📝 Obsidian Knowledge | 5 | obsidian-helper, obsidian-bases, project-to-obsidian |
| 🛠️ Development | 6 | mcp-builder, webapp-testing, skill-creator |
| 🔍 SEO & Performance | 2 | google-official-seo-guide, web-performance-seo |
| 🧠 Planning & Workflow | 5 | planning-with-files, chat-compactor |
| 🐛 Debugging & Quality | 5 | systematic-debugging, test-driven-development |
| 🤖 Agent Orchestration | 4 | dispatching-parallel-agents, subagent-driven-development |
| 🔧 Git & Workflow | 2 | using-git-worktrees, finishing-a-development-branch |
| 🔗 Integration | 5 | notebooklm, x-article-publisher, daily-news, web-access |
| 🔺 Vercel Official | 3 | vercel-deploy, vercel-react-best-practices |

### Skill Structure

Every skill follows a consistent structure:

```
skill-name/
├── SKILL.md          # Main instructions (required)
├── scripts/          # Helper scripts (optional)
├── templates/        # Template files (optional)
├── references/       # Documentation (optional)
└── examples/         # Usage examples (optional)
```

---

## 🤝 Contributing

We welcome contributions! See **[CONTRIBUTING.md](CONTRIBUTING.md)** for full guidelines.

Quick summary:

1. Fork this repository
2. Create a skill folder with `SKILL.md` (and optional scripts/templates)
3. Add your skill to the correct category in README
4. Submit a Pull Request

Quality requirements:
- `SKILL.md` must include valid frontmatter (`name`, `description`)
- Clear, actionable instructions
- No promotional or marketing language
- Under 500 lines for optimal performance
- Scripts must be tested

---

## 📜 License

MIT License — see [LICENSE](LICENSE) for details.

---

## ⭐ Star History

<a href="https://star-history.com/#ZhanlinCui/Ultimate-Agent-Skills-Collection&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=ZhanlinCui/Ultimate-Agent-Skills-Collection&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=ZhanlinCui/Ultimate-Agent-Skills-Collection&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=ZhanlinCui/Ultimate-Agent-Skills-Collection&type=Date" />
 </picture>
</a>

---

## 📚 References

- [Anthropic: Using Skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [Anthropic: Creating Custom Skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- [Claude Code Skills Documentation](https://code.claude.com/docs/en/skills)
- [GitHub Copilot: About Agent Skills](https://docs.github.com/copilot/concepts/agents/about-agent-skills)
- [VS Code Agent Skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills)
- [OpenAI Codex Skills](https://developers.openai.com/codex/skills)
- [Google Antigravity Skills](https://antigravity.google/docs/skills)
- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)

---

<div align="center">

**Made with ❤️ for the AI Agent Community**

*The Ultimate Production-Ready Agent Skills Library*

</div>
