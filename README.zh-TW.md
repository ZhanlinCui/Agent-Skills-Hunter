# Ultimate Agent Skills Collection

<div align="center">

<img src="https://img.shields.io/badge/技能-49+-blueviolet?style=for-the-badge" alt="技能數量" />
<img src="https://img.shields.io/badge/品質-精選-gold?style=for-the-badge" alt="品質" />
<img src="https://img.shields.io/badge/授權-MIT-green?style=for-the-badge" alt="授權" />
<img src="https://img.shields.io/badge/語言-6種-blue?style=for-the-badge" alt="語言" />

<br />

<img src="https://img.shields.io/github/stars/ZhanlinCui/Ultimate-Agent-Skills-Collection?style=social" alt="Stars" />
<img src="https://img.shields.io/github/forks/ZhanlinCui/Ultimate-Agent-Skills-Collection?style=social" alt="Forks" />
<img src="https://img.shields.io/github/last-commit/ZhanlinCui/Ultimate-Agent-Skills-Collection" alt="最近提交" />
<img src="https://img.shields.io/github/contributors/ZhanlinCui/Ultimate-Agent-Skills-Collection" alt="貢獻者" />

**網路上最全面的生產級 Agent 技能庫**

*不只是連結 — 包含腳本、範本和參考文件的完整實作，開箱即用。*

[English](./README.md) | [简体中文](./README.zh-CN.md) | [日本語](./README.ja.md) | [한국어](./README.ko.md) | [Español](./README.es.md)

</div>

---

## 目錄

- [什麼是 Agent Skills？](#-什麼是-agent-skills)
- [為什麼選擇這個合集？](#-為什麼選擇這個合集)
- [相容的 AI 代理](#-相容的-ai-代理)
- [快速開始](#-快速開始)
- [技能目錄](#-技能目錄)
- [官方技能參考](#-官方技能參考)
- [社群技能與合集](#-社群技能與合集)
- [IDE/Agent 設定](#-ideagent-設定)
- [官方教學與指南](#-官方教學與指南)
- [常見問題](#-常見問題)
- [參與貢獻](#-參與貢獻)
- [授權條款](#-授權條款)
- [Star 歷史](#-star-歷史)
- [參考資料](#-參考資料)

---

## 📖 什麼是 Agent Skills？

**Agent Skills** 就像是 AI 助手的「操作指南」。AI 不需要事先知道所有事情，Skills 讓它可以按需學習新能力 — 就像給人一張食譜卡片，而不是讓他背下整本食譜。

Skills 是包含指令檔案（`SKILL.md`）的資料夾，用來教 AI 如何完成特定任務。當你讓 AI 做某件事時，它會找到合適的 Skill，讀取指令，然後開始工作。

### Skills 的運作原理

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│   瀏覽       │ ──▶ │    載入      │ ──▶ │    使用      │
│ (查看名稱)   │     │ (讀取完整)   │     │ (執行任務)   │
└─────────────┘     └──────────────┘     └─────────────┘
```

1. **瀏覽** — AI 看到可用 Skills 的清單（名稱和簡短描述）
2. **載入** — 當需要某個 Skill 時，AI 讀取完整指令
3. **使用** — AI 按照指令執行，並使用輔助腳本、範本或參考文件

Skills 是**指令**，不是程式碼。AI 像人類閱讀指南一樣讀取它們，然後按步驟執行。

---

## 🌟 為什麼選擇這個合集？

大多數「awesome」技能清單只是指向外部儲存庫的**連結目錄**。這個合集有本質區別：

| 特性 | 連結目錄 | **本合集** |
|------|---------|-----------|
| 內容 | 僅外部連結 | **49+ 完整技能實作** |
| 腳本 | ❌ | ✅ 14+ 技能包含輔助腳本 |
| 範本 | ❌ | ✅ 即用型範本 |
| 參考文件 | ❌ | ✅ 精選參考文件 |
| 可用性 | 需要造訪 50+ 個儲存庫 | **複製一次，全部可用** |
| 品質 | 參差不齊 | **經過精選和測試** |
| IDE 支援 | 有限 | **10+ IDE 一鍵設定** |
| 安裝器 | ❌ | ✅ **一鍵安裝腳本** |

### 你將獲得

- ✅ **49+ 生產級技能** — 完整實作，不只是連結
- ✅ **腳本與範本** — 輔助腳本、文件範本、程式碼產生器
- ✅ **10+ IDE 支援** — Cursor、Claude Code、Copilot、VS Code 等一鍵設定
- ✅ **一鍵安裝器** — `install.sh` 自動偵測你的 IDE 並安裝技能
- ✅ **6 種語言** — English、简体中文、繁體中文、日本語、한국어、Español
- ✅ **組織清晰** — 11 個分類，結構一致，品質把關

---

## 🔌 相容的 AI 代理

| Agent | 技能路徑 | 文件 |
|-------|---------|------|
| Claude Code | `~/.claude/skills/` | [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills) |
| Claude.ai | 透過 UI 上傳 | [support.claude.com](https://support.claude.com/en/articles/12512180-using-skills-in-claude) |
| GitHub Copilot | `.github/skills/` | [docs.github.com](https://docs.github.com/copilot/concepts/agents/about-agent-skills) |
| VS Code | `.github/skills/` | [code.visualstudio.com](https://code.visualstudio.com/docs/copilot/customization/agent-skills) |
| Codex (OpenAI) | `~/.codex/skills/` | [developers.openai.com](https://developers.openai.com/codex/skills) |
| Antigravity (Google) | `~/.gemini/antigravity/skills/` | [antigravity.google](https://antigravity.google/docs/skills) |
| Gemini CLI | `~/.gemini/skills/` | [geminicli.com](https://geminicli.com/docs/cli/skills/) |
| Kiro | 專案級 Skills | [kiro.dev](https://kiro.dev/docs/skills/) |
| Cursor | `~/.cursor/skills/` | 相容 Skill 標準 |
| Windsurf | `~/.codeium/windsurf/skills/` | 相容 Skill 標準 |
| OpenCode | `~/.config/opencode/skill/` | 相容 Skill 標準 |
| Amp | `~/.config/agents/skills/` | 相容 Skill 標準 |

---

## 🚀 快速開始

### 方式一：一鍵安裝（推薦）

```bash
git clone https://github.com/ZhanlinCui/Ultimate-Agent-Skills-Collection.git
cd Ultimate-Agent-Skills-Collection
chmod +x install.sh
./install.sh
```

### 方式二：手動設定

```bash
git clone https://github.com/ZhanlinCui/Ultimate-Agent-Skills-Collection.git ~/.agents/skills
mkdir -p ~/.cursor
ln -sf ~/.agents/skills ~/.cursor/skills
```

---

## 📂 技能目錄

### 🎨 創意與設計

| 技能 | 描述 | 包含 |
|------|------|------|
| **[algorithmic-art](./creative/algorithmic-art/)** | 使用 p5.js 建立生成式藝術 | `scripts` `templates` |
| **[canvas-design](./creative/canvas-design/)** | 使用設計理念建立精美的視覺藝術作品 | `fonts` |
| **[frontend-design](./creative/frontend-design/)** | 建構卓越設計品質的生產級前端介面 | |
| **[brand-guidelines](./creative/brand-guidelines/)** | 套用官方品牌色彩和字型 | |
| **[theme-factory](./creative/theme-factory/)** | 10+ 預設主題或即時生成自訂主題 | `templates` |
| **[slack-gif-creator](./creative/slack-gif-creator/)** | 建立為 Slack 最佳化的動畫 GIF | `scripts` |
| **[ui-ux-pro-max](./creative/ui-ux-pro-max/)** | 終極 UI/UX 設計智慧：50+ 樣式、97 配色方案、57 字型配對 | `scripts` `references` |

### 📄 文件技能

| 技能 | 描述 | 包含 |
|------|------|------|
| **[docx](./docs/docx/)** | 全面的 Word 文件建立、編輯，支援修訂和批註 | `scripts` `templates` `references` |
| **[pdf](./docs/pdf/)** | PDF 操作 — 擷取文字/表格、建立、合併/分割、處理表單 | `scripts` |
| **[pptx](./docs/pptx/)** | PowerPoint 簡報建立、編輯、版面配置和簡報者備忘稿 | `scripts` `references` |
| **[xlsx](./docs/xlsx/)** | 試算表建立、編輯，支援公式、格式和資料分析 | `scripts` |
| **[doc-coauthoring](./docs/doc-coauthoring/)** | 文件和提案協作撰寫的結構化工作流程 | |
| **[internal-comms](./docs/internal-comms/)** | 撰寫內部通訊：狀態報告、簡報、FAQ、事故報告 | `templates` |
| **[github-release-assistant](./docs/github-release-assistant/)** | 產生雙語 GitHub 發布文件（英文 + 中文） | `scripts` `templates` `references` |

### 📝 Obsidian 知識管理

| 技能 | 描述 | 包含 |
|------|------|------|
| **[obsidian-helper](./obsidian/obsidian-helper/)** | 智慧筆記助手，支援 `/daily`、`/capture`、`/review` 指令 | `scripts` `references` |
| **[obsidian-bases](./obsidian/obsidian-bases/)** | 建立 Obsidian Bases (.base 檔案)：檢視、篩選器、公式、摘要 | |
| **[obsidian-markdown](./obsidian/obsidian-markdown/)** | 完整的 Obsidian 風格 Markdown 指南 | |
| **[project-to-obsidian](./obsidian/project-to-obsidian/)** | 將程式碼專案轉換為 Obsidian 知識庫 | `scripts` `templates` |
| **[json-canvas](./obsidian/json-canvas/)** | 建立 JSON Canvas 檔案（.canvas） | |

### 🛠️ 開發與技術

| 技能 | 描述 | 包含 |
|------|------|------|
| **[mcp-builder](./dev/mcp-builder/)** | 建立高品質的 MCP 伺服器 | `scripts` `templates` |
| **[webapp-testing](./dev/webapp-testing/)** | 使用 Playwright 測試本機 Web 應用程式 | `scripts` |
| **[web-artifacts-builder](./dev/web-artifacts-builder/)** | 使用 React、Tailwind 和 shadcn/ui 建構複合 HTML 製品 | `scripts` |
| **[skill-creator](./dev/skill-creator/)** | 建立有效的 AI Agent 技能擴充指南 | `scripts` `templates` |
| **[deploying-to-production](./dev/deploying-to-production/)** | 自動化 GitHub 儲存庫建立和 Vercel 部署 | |
| **[internationalizing-websites](./dev/internationalizing-websites/)** | 為 Next.js 加入多語言支援和 SEO 設定 | `scripts` `templates` |

### 🔍 SEO 與效能

| 技能 | 描述 | 包含 |
|------|------|------|
| **[google-official-seo-guide](./seo/google-official-seo-guide/)** | Google 官方 SEO 指南 | `references` |
| **[web-performance-seo](./seo/web-performance-seo/)** | 修復 PageSpeed/Lighthouse 無障礙問題 | |

### 🧠 計劃與工作流程

| 技能 | 描述 | 包含 |
|------|------|------|
| **[planning-with-files](./planning/planning-with-files/)** | Manus 風格的檔案規劃 | `scripts` `templates` |
| **[writing-plans](./planning/writing-plans/)** | 在撰寫程式碼前建立結構化計劃 | |
| **[executing-plans](./planning/executing-plans/)** | 帶審查檢查點的實施計劃執行 | |
| **[brainstorming](./planning/brainstorming/)** | 實作前探索使用者意圖、需求和設計 | |
| **[chat-compactor](./planning/chat-compactor/)** | 產生工作階段摘要以實現 AI Agent 跨工作階段連續性 | |

### 🐛 除錯與品質

| 技能 | 描述 | 包含 |
|------|------|------|
| **[systematic-debugging](./quality/systematic-debugging/)** | 系統化除錯：修復前先做根因分析 | `scripts` `references` |
| **[test-driven-development](./quality/test-driven-development/)** | TDD 工作流程：先寫測試，再寫實作 | `templates` |
| **[verification-before-completion](./quality/verification-before-completion/)** | 宣告完成前驗證工作是否真正完成 | |
| **[receiving-code-review](./quality/receiving-code-review/)** | 以技術嚴謹性處理程式碼審查回饋 | |
| **[requesting-code-review](./quality/requesting-code-review/)** | 為已完成的工作要求全面的程式碼審查 | `templates` |

### 🤖 Agent 編排

| 技能 | 描述 | 包含 |
|------|------|------|
| **[dispatching-parallel-agents](./agent/dispatching-parallel-agents/)** | 將 2+ 個獨立任務分派給並行子 Agent | |
| **[subagent-driven-development](./agent/subagent-driven-development/)** | 使用專門的子 Agent 執行計劃中的每個任務 | `scripts` `templates` |
| **[using-superpowers](./agent/using-superpowers/)** | 確定如何在對話中尋找和使用技能 | |
| **[writing-skills](./agent/writing-skills/)** | 在部署前建立、編輯和驗證技能 | `scripts` `templates` `examples` |

### 🔧 Git 與開發工作流程

| 技能 | 描述 | 包含 |
|------|------|------|
| **[using-git-worktrees](./git-workflow/using-git-worktrees/)** | 為功能開發建立隔離的 git worktree | |
| **[finishing-a-development-branch](./git-workflow/finishing-a-development-branch/)** | 引導完成：合併、PR 或清理選項 | |

### 🔗 整合與自動化

| 技能 | 描述 | 包含 |
|------|------|------|
| **[notebooklm](./integration/notebooklm/)** | 透過瀏覽器自動化查詢 Google NotebookLM | `scripts` |
| **[x-article-publisher](./integration/x-article-publisher/)** | 將 Markdown 文章發布到 X（Twitter）Articles | `scripts` |
| **[doc-sync-tool](./integration/doc-sync-tool/)** | 跨專案自動同步 Agents.md 等檔案 | `scripts` |

### 🔺 Vercel 官方

| 技能 | 描述 | 包含 |
|------|------|------|
| **[vercel-deploy](./vercel/vercel-deploy/)** | 一鍵部署任何專案到 Vercel，無需認證 | `scripts` |
| **[vercel-react-best-practices](./vercel/vercel-react-best-practices/)** | Vercel 工程團隊出品的 45 條 React/Next.js 效能規則 | `rules` |
| **[vercel-web-design-guidelines](./vercel/vercel-web-design-guidelines/)** | 審查 UI 程式碼是否符合 Web 介面準則 | |

---

## 📚 官方技能參考

### Anthropic (Claude)

| 技能 | 描述 | 來源 |
|------|------|------|
| docx | 建立、編輯、分析 Word 文件 | [anthropics/skills](https://github.com/anthropics/skills) |
| xlsx | 試算表操作：公式、圖表、資料轉換 | [anthropics/skills](https://github.com/anthropics/skills) |
| pptx | 讀取、產生和調整投影片 | [anthropics/skills](https://github.com/anthropics/skills) |
| pdf | 從 PDF 擷取文字、表格、中繼資料 | [anthropics/skills](https://github.com/anthropics/skills) |

### HuggingFace

| 技能 | 描述 | 來源 |
|------|------|------|
| hf_dataset_creator | 建立結構化訓練資料集的提示、範本和腳本 | [huggingface/skills](https://github.com/huggingface/skills) |
| hf_model_evaluation | 編排評估任務、產生報告和對應指標 | [huggingface/skills](https://github.com/huggingface/skills) |
| hf-llm-trainer | 包含指導、輔助腳本和成本估算器的全面訓練技能 | [huggingface/skills](https://github.com/huggingface/skills) |
| hf-paper-publisher | 在 Hugging Face Hub 上發布和管理研究論文的工具 | [huggingface/skills](https://github.com/huggingface/skills) |

---

## 🌐 社群技能與合集

| 儲存庫 | 描述 |
|--------|------|
| [anthropics/skills](https://github.com/anthropics/skills) | Anthropic 官方合集 |
| [openai/skills](https://github.com/openai/skills) | OpenAI Codex 官方技能目錄 |
| [huggingface/skills](https://github.com/huggingface/skills) | HuggingFace 技能 |
| [heilcheng/awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills) | 技能連結和資源精選清單 |
| [dmgrok/agent_skills_directory](https://github.com/dmgrok/agent_skills_directory) | npm 風格的技能 CLI |
| [karanb192/awesome-claude-skills](https://github.com/karanb192/awesome-claude-skills) | 50+ 經驗證的 Claude 技能 |

---

## ⚙️ IDE/Agent 設定

```bash
git clone https://github.com/ZhanlinCui/Ultimate-Agent-Skills-Collection.git ~/.agents/skills
```

| IDE | 預設技能路徑 | 符號連結指令 |
|-----|------------|------------|
| **Cursor** | `~/.cursor/skills/` | `mkdir -p ~/.cursor && ln -sf ~/.agents/skills ~/.cursor/skills` |
| **Claude Code** | `~/.claude/skills/` | `mkdir -p ~/.claude && ln -sf ~/.agents/skills ~/.claude/skills` |
| **GitHub Copilot** | `~/.copilot/skills/` | `mkdir -p ~/.copilot && ln -sf ~/.agents/skills ~/.copilot/skills` |
| **Codex (OpenAI)** | `~/.codex/skills/` | `mkdir -p ~/.codex && ln -sf ~/.agents/skills ~/.codex/skills` |
| **Windsurf** | `~/.codeium/windsurf/skills/` | `mkdir -p ~/.codeium/windsurf && ln -sf ~/.agents/skills ~/.codeium/windsurf/skills` |

---

## 📖 官方教學與指南

- [在 Claude 中使用 Skills](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [如何建立自訂 Skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- [Claude Code Skills 文件](https://code.claude.com/docs/en/skills)
- [關於 Agent Skills](https://docs.github.com/copilot/concepts/agents/about-agent-skills) — GitHub
- [VS Code Agent Skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills)
- [MCP 官方文件](https://modelcontextprotocol.io/)

---

## ❓ 常見問題

### 什麼是 Agent Skills？

Agent Skills 是教 AI 助手如何完成特定任務的指令檔案。它們按需載入，所以 AI 保持快速和專注。

### 這個合集和其他技能合集有什麼不同？

大多數合集是**連結目錄**。這個合集包含 **49+ 完整技能實作**，附帶腳本、範本和參考文件。

### Agent Skills 和微調有什麼區別？

微調永久改變 AI 的思維方式（昂貴且難以更新）。Agent Skills 只是指令檔案，可以隨時更新、替換或分享。

### Agent Skills 和 MCP 有什麼區別？

互為補充：
- **Agent Skills** = 教 AI *如何*做某事
- **MCP** = 幫助 AI *存取*事物

### 可以同時在多個 IDE 中使用嗎？

可以！使用 `install.sh` 腳本同時為所有 IDE 設定技能。

---

## 🤝 參與貢獻

我們歡迎貢獻！請查看 **[CONTRIBUTING.md](CONTRIBUTING.md)** 了解完整指南。

---

## 📜 授權條款

MIT License — 詳見 [LICENSE](LICENSE)。

---

## ⭐ Star 歷史

<a href="https://star-history.com/#ZhanlinCui/Ultimate-Agent-Skills-Collection&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=ZhanlinCui/Ultimate-Agent-Skills-Collection&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=ZhanlinCui/Ultimate-Agent-Skills-Collection&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=ZhanlinCui/Ultimate-Agent-Skills-Collection&type=Date" />
 </picture>
</a>

---

## 📚 參考資料

- [Anthropic: 在 Claude 中使用 Skills](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [Claude Code Skills 文件](https://code.claude.com/docs/en/skills)
- [GitHub Copilot: 關於 Agent Skills](https://docs.github.com/copilot/concepts/agents/about-agent-skills)
- [OpenAI Codex Skills](https://developers.openai.com/codex/skills)
- [Model Context Protocol 文件](https://modelcontextprotocol.io/)

---

<div align="center">

**為 AI Agent 社群用心打造 ❤️**

*終極生產級 Agent 技能庫*

</div>
