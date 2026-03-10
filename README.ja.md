# Ultimate Agent Skills Collection

<div align="center">

<img src="https://img.shields.io/badge/スキル-51+-blueviolet?style=for-the-badge" alt="スキル数" />
<img src="https://img.shields.io/badge/品質-プレミアム-gold?style=for-the-badge" alt="品質" />
<img src="https://img.shields.io/badge/ライセンス-MIT-green?style=for-the-badge" alt="ライセンス" />
<img src="https://img.shields.io/badge/言語-6種-blue?style=for-the-badge" alt="言語" />

<br />

<img src="https://img.shields.io/github/stars/ZhanlinCui/Ultimate-Agent-Skills-Collection?style=social" alt="Stars" />
<img src="https://img.shields.io/github/forks/ZhanlinCui/Ultimate-Agent-Skills-Collection?style=social" alt="Forks" />
<img src="https://img.shields.io/github/last-commit/ZhanlinCui/Ultimate-Agent-Skills-Collection" alt="最終コミット" />
<img src="https://img.shields.io/github/contributors/ZhanlinCui/Ultimate-Agent-Skills-Collection" alt="コントリビューター" />

**インターネット上で最も包括的な本番対応 Agent スキルライブラリ**

*リンクだけではありません — スクリプト、テンプレート、リファレンスを含む完全な実装で、すぐに使えます。*

[English](./README.md) | [简体中文](./README.zh-CN.md) | [繁體中文](./README.zh-TW.md) | [한국어](./README.ko.md) | [Español](./README.es.md)

</div>

---

## 目次

- [Agent Skills とは？](#-agent-skills-とは)
- [このコレクションが違う理由](#-このコレクションが違う理由)
- [互換性のある AI エージェント](#-互換性のある-ai-エージェント)
- [クイックスタート](#-クイックスタート)
- [スキルディレクトリ](#-スキルディレクトリ)
- [公式スキルリファレンス](#-公式スキルリファレンス)
- [コミュニティスキル＆コレクション](#-コミュニティスキルコレクション)
- [IDE/Agent 設定](#-ideagent-設定)
- [公式チュートリアル＆ガイド](#-公式チュートリアルガイド)
- [FAQ](#-faq)
- [コントリビュート](#-コントリビュート)
- [ライセンス](#-ライセンス)
- [Star 履歴](#-star-履歴)
- [参考資料](#-参考資料)

---

## 📖 Agent Skills とは？

**Agent Skills** はAIアシスタントのための「ハウツーガイド」です。AIが事前にすべてを知っている必要はなく、スキルによってオンデマンドで新しい能力を学べます — 料理本を丸暗記させるのではなく、レシピカードを渡すようなものです。

スキルは、AIに特定のタスクの実行方法を教える命令ファイル（`SKILL.md`）を含むフォルダです。AIに何かを頼むと、適切なスキルを見つけ、指示を読み、作業を開始します。

### スキルの仕組み

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│   ブラウズ    │ ──▶ │    ロード     │ ──▶ │    使用      │
│ (名前を確認)  │     │ (全文読込)    │     │ (タスク実行)  │
└─────────────┘     └──────────────┘     └─────────────┘
```

1. **ブラウズ** — AIが利用可能なスキルのリスト（名前と短い説明）を確認
2. **ロード** — スキルが必要な時、AIが完全な指示を読み込む
3. **使用** — AIが指示に従い、ヘルパースクリプト、テンプレート、リファレンスを活用

スキルは**命令**であり、コードではありません。AIは人間がガイドを読むように読み、手順に従います。

---

## 🌟 このコレクションが違う理由

多くの「awesome」スキルリストは、外部リポジトリへの**リンクディレクトリ**にすぎません。このコレクションは根本的に異なります：

| 特徴 | リンクディレクトリ | **このコレクション** |
|------|-----------------|-------------------|
| コンテンツ | 外部リンクのみ | **51+ 完全なスキル実装** |
| スクリプト | ❌ | ✅ 14+ スキルにヘルパースクリプト |
| テンプレート | ❌ | ✅ すぐに使えるテンプレート |
| リファレンス | ❌ | ✅ 厳選されたリファレンスドキュメント |
| 使いやすさ | 50+ のリポジトリを訪問 | **一度クローンですべて利用可能** |
| 品質 | ばらつきあり | **厳選・テスト済み** |
| IDE対応 | 限定的 | **10+ IDE ワンクリック設定** |
| インストーラー | ❌ | ✅ **ワンクリックインストールスクリプト** |

### 含まれるもの

- ✅ **51+ 本番対応スキル** — 完全な実装、リンクだけではない
- ✅ **スクリプト＆テンプレート** — ヘルパースクリプト、ドキュメントテンプレート、コードジェネレーター
- ✅ **10+ IDE 対応** — Cursor、Claude Code、Copilot、VS Code など
- ✅ **ワンクリックインストーラー** — `install.sh` がIDEを自動検出してスキルをインストール
- ✅ **6言語対応** — English、简体中文、繁體中文、日本語、한국어、Español
- ✅ **整理済み** — 11カテゴリ、一貫した構造、品質チェック済み

---

## 🔌 互換性のある AI エージェント

| Agent | スキルパス | ドキュメント |
|-------|----------|------------|
| Claude Code | `~/.claude/skills/` | [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills) |
| Claude.ai | UIからアップロード | [support.claude.com](https://support.claude.com/en/articles/12512180-using-skills-in-claude) |
| GitHub Copilot | `.github/skills/` | [docs.github.com](https://docs.github.com/copilot/concepts/agents/about-agent-skills) |
| VS Code | `.github/skills/` | [code.visualstudio.com](https://code.visualstudio.com/docs/copilot/customization/agent-skills) |
| Codex (OpenAI) | `~/.codex/skills/` | [developers.openai.com](https://developers.openai.com/codex/skills) |
| Antigravity (Google) | `~/.gemini/antigravity/skills/` | [antigravity.google](https://antigravity.google/docs/skills) |
| Gemini CLI | `~/.gemini/skills/` | [geminicli.com](https://geminicli.com/docs/cli/skills/) |
| Kiro | プロジェクトスキル | [kiro.dev](https://kiro.dev/docs/skills/) |
| Cursor | `~/.cursor/skills/` | スキル標準対応 |
| Windsurf | `~/.codeium/windsurf/skills/` | スキル標準対応 |
| OpenCode | `~/.config/opencode/skill/` | スキル標準対応 |
| Amp | `~/.config/agents/skills/` | スキル標準対応 |

---

## 🚀 クイックスタート

### 方法1：ワンクリックインストール（推奨）

```bash
git clone https://github.com/ZhanlinCui/Ultimate-Agent-Skills-Collection.git
cd Ultimate-Agent-Skills-Collection
chmod +x install.sh
./install.sh
```

### 方法2：手動セットアップ

```bash
git clone https://github.com/ZhanlinCui/Ultimate-Agent-Skills-Collection.git ~/.agents/skills
mkdir -p ~/.cursor
ln -sf ~/.agents/skills ~/.cursor/skills
```

---

## 📂 スキルディレクトリ

### 🎨 クリエイティブ＆デザイン

| スキル | 説明 | 含む |
|--------|------|------|
| **[algorithmic-art](./creative/algorithmic-art/)** | p5.jsを使用したジェネラティブアート作成 | `scripts` `templates` |
| **[canvas-design](./creative/canvas-design/)** | デザイン哲学を用いた美しいビジュアルアート作成 | `fonts` |
| **[frontend-design](./creative/frontend-design/)** | 卓越したデザイン品質のフロントエンドインターフェース構築 | |
| **[brand-guidelines](./creative/brand-guidelines/)** | 公式ブランドカラーとタイポグラフィの適用 | |
| **[theme-factory](./creative/theme-factory/)** | 10+プリセットテーマまたはカスタムテーマの生成 | `templates` |
| **[slack-gif-creator](./creative/slack-gif-creator/)** | Slack向けに最適化されたアニメーションGIF作成 | `scripts` |
| **[ui-ux-pro-max](./creative/ui-ux-pro-max/)** | 究極のUI/UXデザインインテリジェンス：50+スタイル、97配色、57フォントペアリング | `scripts` `references` |

### 📄 ドキュメントスキル

| スキル | 説明 | 含む |
|--------|------|------|
| **[docx](./docs/docx/)** | Word文書の包括的な作成・編集、変更履歴とコメント対応 | `scripts` `templates` `references` |
| **[pdf](./docs/pdf/)** | PDF操作 — テキスト/テーブル抽出、作成、結合/分割、フォーム処理 | `scripts` |
| **[pptx](./docs/pptx/)** | PowerPointプレゼンテーションの作成・編集、レイアウト、発表者ノート | `scripts` `references` |
| **[xlsx](./docs/xlsx/)** | スプレッドシートの作成・編集、数式・書式・データ分析 | `scripts` |
| **[doc-coauthoring](./docs/doc-coauthoring/)** | ドキュメントと提案書の共同執筆ワークフロー | |
| **[internal-comms](./docs/internal-comms/)** | 社内コミュニケーション：ステータスレポート、ニュースレター、FAQ、インシデントレポート | `templates` |
| **[github-release-assistant](./docs/github-release-assistant/)** | バイリンガルGitHubリリースドキュメント生成（英語+中国語） | `scripts` `templates` `references` |

### 📝 Obsidian ナレッジマネジメント

| スキル | 説明 | 含む |
|--------|------|------|
| **[obsidian-helper](./obsidian/obsidian-helper/)** | `/daily`、`/capture`、`/review`コマンド対応のスマートノートアシスタント | `scripts` `references` |
| **[obsidian-bases](./obsidian/obsidian-bases/)** | Obsidian Bases（.baseファイル）の作成：ビュー、フィルター、数式、サマリー | |
| **[obsidian-markdown](./obsidian/obsidian-markdown/)** | Obsidianフレーバー Markdown完全ガイド | |
| **[project-to-obsidian](./obsidian/project-to-obsidian/)** | コードプロジェクトをObsidianナレッジベースに変換 | `scripts` `templates` |
| **[json-canvas](./obsidian/json-canvas/)** | JSON Canvasファイル（.canvas）の作成 | |

### 🛠️ 開発＆テクニカル

| スキル | 説明 | 含む |
|--------|------|------|
| **[mcp-builder](./dev/mcp-builder/)** | 高品質MCP（Model Context Protocol）サーバーの作成 | `scripts` `templates` |
| **[webapp-testing](./dev/webapp-testing/)** | Playwrightを使用したWebアプリテスト | `scripts` |
| **[web-artifacts-builder](./dev/web-artifacts-builder/)** | React、Tailwind、shadcn/uiを使用した複合HTMLアーティファクト構築 | `scripts` |
| **[skill-creator](./dev/skill-creator/)** | 効果的なAI Agentスキル作成ガイド | `scripts` `templates` |
| **[deploying-to-production](./dev/deploying-to-production/)** | GitHubリポジトリ作成とVercelデプロイの自動化 | |
| **[internationalizing-websites](./dev/internationalizing-websites/)** | Next.jsへの多言語サポートとSEO設定の追加 | `scripts` `templates` |

### 🔍 SEO＆パフォーマンス

| スキル | 説明 | 含む |
|--------|------|------|
| **[google-official-seo-guide](./seo/google-official-seo-guide/)** | Google公式SEOガイド：検索最適化、クロール、インデックスのベストプラクティス | `references` |
| **[web-performance-seo](./seo/web-performance-seo/)** | PageSpeed/Lighthouseアクセシビリティエラーの修正 | |

### 🧠 プランニング＆ワークフロー

| スキル | 説明 | 含む |
|--------|------|------|
| **[planning-with-files](./planning/planning-with-files/)** | Manusスタイルのファイルベースプランニング | `scripts` `templates` |
| **[writing-plans](./planning/writing-plans/)** | コーディング前の構造化プラン作成 | |
| **[executing-plans](./planning/executing-plans/)** | レビューチェックポイント付きプラン実行 | |
| **[brainstorming](./planning/brainstorming/)** | 実装前のユーザー意図・要件・設計の探索 | |
| **[chat-compactor](./planning/chat-compactor/)** | AIエージェントのセッション間継続性のためのサマリー生成 | |

### 🐛 デバッグ＆品質

| スキル | 説明 | 含む |
|--------|------|------|
| **[systematic-debugging](./quality/systematic-debugging/)** | 体系的デバッグ：修正前の根本原因分析 | `scripts` `references` |
| **[test-driven-development](./quality/test-driven-development/)** | TDDワークフロー：テスト先行、実装後追い | `templates` |
| **[verification-before-completion](./quality/verification-before-completion/)** | 完了宣言前の作業検証 | |
| **[receiving-code-review](./quality/receiving-code-review/)** | コードレビューフィードバックの技術的厳密な処理 | |
| **[requesting-code-review](./quality/requesting-code-review/)** | 完了した作業の包括的コードレビュー依頼 | `templates` |

### 🤖 Agent オーケストレーション

| スキル | 説明 | 含む |
|--------|------|------|
| **[dispatching-parallel-agents](./agent/dispatching-parallel-agents/)** | 2+の独立タスクを並列サブエージェントにディスパッチ | |
| **[subagent-driven-development](./agent/subagent-driven-development/)** | 専門サブエージェントによるプラン実行 | `scripts` `templates` |
| **[using-superpowers](./agent/using-superpowers/)** | 会話中のスキル検索・使用方法の確立 | |
| **[writing-skills](./agent/writing-skills/)** | デプロイ前のスキル作成・編集・検証 | `scripts` `templates` `examples` |

### 🔧 Git＆開発ワークフロー

| スキル | 説明 | 含む |
|--------|------|------|
| **[using-git-worktrees](./git-workflow/using-git-worktrees/)** | 機能開発用の分離されたgit worktree作成 | |
| **[finishing-a-development-branch](./git-workflow/finishing-a-development-branch/)** | 完了ガイド：マージ、PR、クリーンアップオプション | |

### 🔗 インテグレーション＆自動化

| スキル | 説明 | 含む |
|--------|------|------|
| **[notebooklm](./integration/notebooklm/)** | ブラウザ自動化によるGoogle NotebookLMクエリ | `scripts` |
| **[x-article-publisher](./integration/x-article-publisher/)** | Markdown記事をX（Twitter）Articlesに公開 | `scripts` |
| **[doc-sync-tool](./integration/doc-sync-tool/)** | プロジェクト間でのAgents.md等の自動同期 | `scripts` |
| **[daily-news](./integration/daily-news/)** | 3段階の日刊ニュースレポート生成：メタデータ取得→要約生成→レポート出力。カスタムソース対応 | `scripts` `references` |
| **[web-access](./integration/web-access/)** | AIエージェントに真のWeb閲覧能力を：WebSearch→WebFetch→ブラウザCDPモードのスマートチャネル選択 | `scripts` `references` |

### 🔺 Vercel 公式

| スキル | 説明 | 含む |
|--------|------|------|
| **[vercel-deploy](./vercel/vercel-deploy/)** | Vercelへのワンクリックデプロイ、認証不要 | `scripts` |
| **[vercel-react-best-practices](./vercel/vercel-react-best-practices/)** | Vercelエンジニアリングチームによる45のReact/Next.jsパフォーマンスルール | `rules` |
| **[vercel-web-design-guidelines](./vercel/vercel-web-design-guidelines/)** | Webインターフェースガイドライン準拠のUIコードレビュー | |

---

## 📚 公式スキルリファレンス

### Anthropic (Claude)

| スキル | 説明 | ソース |
|--------|------|--------|
| docx | Word文書の作成・編集・分析、変更履歴対応 | [anthropics/skills](https://github.com/anthropics/skills) |
| xlsx | スプレッドシート操作：数式、チャート、データ変換 | [anthropics/skills](https://github.com/anthropics/skills) |
| pptx | スライドの読取・生成・調整 | [anthropics/skills](https://github.com/anthropics/skills) |
| pdf | PDFからテキスト、テーブル、メタデータを抽出 | [anthropics/skills](https://github.com/anthropics/skills) |

### OpenAI (Codex)

| スキルスコープ | パス | 推奨用途 |
|--------------|------|---------|
| REPO | `$CWD/.codex/skills` | 作業フォルダ関連のスキル |
| USER | `~/.codex/skills` | 全リポジトリ共通の個人スキル |
| ADMIN | `/etc/codex/skills` | SDKスクリプト、自動化スキル |
| SYSTEM | Codex内蔵 | skill-creator等の組み込みスキル |

### HuggingFace

| スキル | 説明 | ソース |
|--------|------|--------|
| hf_dataset_creator | 構造化トレーニングデータセット作成用プロンプト・テンプレート・スクリプト | [huggingface/skills](https://github.com/huggingface/skills) |
| hf_model_evaluation | 評価ジョブのオーケストレーション、レポート生成、メトリクスマッピング | [huggingface/skills](https://github.com/huggingface/skills) |
| hf-llm-trainer | ガイダンス、ヘルパースクリプト、コスト見積もり付きの包括的トレーニングスキル | [huggingface/skills](https://github.com/huggingface/skills) |
| hf-paper-publisher | Hugging Face Hubでの研究論文の公開・管理ツール | [huggingface/skills](https://github.com/huggingface/skills) |

---

## 🌐 コミュニティスキル＆コレクション

| リポジトリ | 説明 |
|-----------|------|
| [anthropics/skills](https://github.com/anthropics/skills) | Anthropic公式コレクション |
| [openai/skills](https://github.com/openai/skills) | OpenAI Codex公式スキルカタログ |
| [huggingface/skills](https://github.com/huggingface/skills) | HuggingFaceスキル |
| [heilcheng/awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills) | スキルリンク＆リソースのキュレーションリスト |
| [skillcreatorai/Ai-Agent-Skills](https://github.com/skillcreatorai/Ai-Agent-Skills) | SkillCreator.aiコレクション |
| [agentskill.sh](https://agentskill.sh) | 44k+スキルディレクトリ |
| [dmgrok/agent_skills_directory](https://github.com/dmgrok/agent_skills_directory) | npm風スキルCLI |
| [karanb192/awesome-claude-skills](https://github.com/karanb192/awesome-claude-skills) | 50+検証済みClaudeスキル |

---

## ⚙️ IDE/Agent 設定

### クイックセットアップ

```bash
git clone https://github.com/ZhanlinCui/Ultimate-Agent-Skills-Collection.git ~/.agents/skills
```

### 対応IDE＆設定パス

| IDE | デフォルトスキルパス | シンボリックリンクコマンド |
|-----|-------------------|----------------------|
| **Cursor** | `~/.cursor/skills/` | `mkdir -p ~/.cursor && ln -sf ~/.agents/skills ~/.cursor/skills` |
| **Claude Code** | `~/.claude/skills/` | `mkdir -p ~/.claude && ln -sf ~/.agents/skills ~/.claude/skills` |
| **GitHub Copilot** | `~/.copilot/skills/` | `mkdir -p ~/.copilot && ln -sf ~/.agents/skills ~/.copilot/skills` |
| **Codex (OpenAI)** | `~/.codex/skills/` | `mkdir -p ~/.codex && ln -sf ~/.agents/skills ~/.codex/skills` |
| **Antigravity** | `~/.gemini/antigravity/skills/` | `mkdir -p ~/.gemini/antigravity && ln -sf ~/.agents/skills ~/.gemini/antigravity/skills` |
| **Gemini CLI** | `~/.gemini/skills/` | `mkdir -p ~/.gemini && ln -sf ~/.agents/skills ~/.gemini/skills` |
| **Windsurf** | `~/.codeium/windsurf/skills/` | `mkdir -p ~/.codeium/windsurf && ln -sf ~/.agents/skills ~/.codeium/windsurf/skills` |
| **OpenCode** | `~/.config/opencode/skill/` | `mkdir -p ~/.config/opencode && ln -sf ~/.agents/skills ~/.config/opencode/skill` |
| **Amp** | `~/.config/agents/skills/` | `mkdir -p ~/.config/agents && ln -sf ~/.agents/skills ~/.config/agents/skills` |
| **iFlow** | `~/.iflow/skills/` | `mkdir -p ~/.iflow && ln -sf ~/.agents/skills ~/.iflow/skills` |

---

## 📖 公式チュートリアル＆ガイド

### Claude & Anthropic

- [ClaudeでSkillsを使う](https://support.claude.com/en/articles/12512180-using-skills-in-claude) — 公式クイックスタート
- [カスタムSkillsの作成方法](https://support.claude.com/en/articles/12512198-creating-custom-skills) — ステップバイステップガイド
- [Claude Code Skills ドキュメント](https://code.claude.com/docs/en/skills) — 公式リファレンス

### GitHub Copilot & VS Code

- [Agent Skillsについて](https://docs.github.com/copilot/concepts/agents/about-agent-skills) — GitHubドキュメント
- [VS Code Agent Skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills) — VS Code統合

### OpenAI Codex

- [Codex Skills ドキュメント](https://developers.openai.com/codex/skills) — 公式リファレンス

### Model Context Protocol (MCP)

- [MCP公式ドキュメント](https://modelcontextprotocol.io/) — オープンスタンダード
- [最初のMCP Serverを構築](https://modelcontextprotocol.io/docs/first-server) — Python/TypeScriptガイド

---

## ❓ FAQ

### Agent Skills とは何ですか？

Agent SkillsはAIアシスタントに特定のタスクの実行方法を教える命令ファイルです。必要な時だけ読み込まれるため、AIは高速で集中力を保てます。

### このコレクションは他のスキルコレクションとどう違いますか？

ほとんどのコレクションは外部リポジトリへのリンクを列挙する**リンクディレクトリ**です。このコレクションはスクリプト、テンプレート、リファレンスドキュメントを含む**51+の完全なスキル実装**を収録しています。

### Agent Skills とファインチューニングの違いは？

ファインチューニングはAIの思考を恒久的に変更します（高価で更新困難）。Agent Skillsは単なる命令ファイルで、AI自体を変更することなくいつでも更新・交換・共有できます。

### Agent Skills と MCP の違いは？

相互補完的です：
- **Agent Skills** = AIに*やり方*を教える（ワークフロー、ベストプラクティス）
- **MCP** = AIが*アクセス*するのを助ける（API、データベース、外部ツール）

### どのAIツールがAgent Skillsをサポートしていますか？

現在対応：**Claude**、**GitHub Copilot**、**VS Code**、**Codex**、**Antigravity**、**Gemini CLI**、**Kiro**、**Cursor**、**Windsurf**、**OpenCode**、**Amp**。

### 複数のIDEで同時に使えますか？

はい！`install.sh` スクリプトを使用すると、すべてのIDEに同時にスキルを設定できます。

---

## 🤝 コントリビュート

コントリビュートを歓迎します！完全なガイドラインは **[CONTRIBUTING.md](CONTRIBUTING.md)** をご覧ください。

---

## 📜 ライセンス

MIT License — 詳細は [LICENSE](LICENSE) をご覧ください。

---

## ⭐ Star 履歴

<a href="https://star-history.com/#ZhanlinCui/Ultimate-Agent-Skills-Collection&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=ZhanlinCui/Ultimate-Agent-Skills-Collection&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=ZhanlinCui/Ultimate-Agent-Skills-Collection&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=ZhanlinCui/Ultimate-Agent-Skills-Collection&type=Date" />
 </picture>
</a>

---

## 📚 参考資料

- [Anthropic: ClaudeでSkillsを使う](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [Anthropic: カスタムSkillsの作成](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- [Claude Code Skills ドキュメント](https://code.claude.com/docs/en/skills)
- [GitHub Copilot: Agent Skillsについて](https://docs.github.com/copilot/concepts/agents/about-agent-skills)
- [OpenAI Codex Skills](https://developers.openai.com/codex/skills)
- [Model Context Protocol ドキュメント](https://modelcontextprotocol.io/)

---

<div align="center">

**AI Agentコミュニティのために ❤️ を込めて作成**

*究極の本番対応 Agent スキルライブラリ*

</div>
