# Ultimate Agent Skills Collection

<div align="center">

<img src="https://img.shields.io/badge/스킬-51+-blueviolet?style=for-the-badge" alt="스킬 수" />
<img src="https://img.shields.io/badge/품질-프리미엄-gold?style=for-the-badge" alt="품질" />
<img src="https://img.shields.io/badge/라이선스-MIT-green?style=for-the-badge" alt="라이선스" />
<img src="https://img.shields.io/badge/언어-6종-blue?style=for-the-badge" alt="언어" />

<br />

<img src="https://img.shields.io/github/stars/ZhanlinCui/Ultimate-Agent-Skills-Collection?style=social" alt="Stars" />
<img src="https://img.shields.io/github/forks/ZhanlinCui/Ultimate-Agent-Skills-Collection?style=social" alt="Forks" />
<img src="https://img.shields.io/github/last-commit/ZhanlinCui/Ultimate-Agent-Skills-Collection" alt="최근 커밋" />
<img src="https://img.shields.io/github/contributors/ZhanlinCui/Ultimate-Agent-Skills-Collection" alt="기여자" />

**인터넷에서 가장 포괄적인 프로덕션 레디 Agent 스킬 라이브러리**

*단순한 링크가 아닙니다 — 스크립트, 템플릿, 레퍼런스를 포함한 완전한 구현으로, 바로 사용할 수 있습니다.*

[English](./README.md) | [简体中文](./README.zh-CN.md) | [繁體中文](./README.zh-TW.md) | [日本語](./README.ja.md) | [Español](./README.es.md)

</div>

---

## 목차

- [Agent Skills란?](#-agent-skills란)
- [이 컬렉션이 다른 이유](#-이-컬렉션이-다른-이유)
- [호환 가능한 AI 에이전트](#-호환-가능한-ai-에이전트)
- [빠른 시작](#-빠른-시작)
- [스킬 디렉토리](#-스킬-디렉토리)
- [공식 스킬 레퍼런스](#-공식-스킬-레퍼런스)
- [커뮤니티 스킬 & 컬렉션](#-커뮤니티-스킬--컬렉션)
- [IDE/Agent 설정](#-ideagent-설정)
- [공식 튜토리얼 & 가이드](#-공식-튜토리얼--가이드)
- [FAQ](#-faq)
- [기여하기](#-기여하기)
- [라이선스](#-라이선스)
- [Star 기록](#-star-기록)
- [참고 자료](#-참고-자료)

---

## 📖 Agent Skills란?

**Agent Skills**는 AI 어시스턴트를 위한 "사용 가이드"입니다. AI가 모든 것을 미리 알 필요 없이, 스킬을 통해 필요할 때 새로운 능력을 배울 수 있습니다 — 요리책을 외우게 하는 대신 레시피 카드를 건네주는 것과 같습니다.

스킬은 AI에게 특정 작업 수행 방법을 가르치는 지시 파일(`SKILL.md`)이 포함된 폴더입니다.

### 스킬 작동 방식

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│   탐색       │ ──▶ │    로드      │ ──▶ │    사용      │
│ (이름 확인)   │     │ (전체 읽기)   │     │ (작업 수행)   │
└─────────────┘     └──────────────┘     └─────────────┘
```

1. **탐색** — AI가 사용 가능한 스킬 목록(이름과 간단한 설명)을 확인
2. **로드** — 스킬이 필요할 때 AI가 전체 지시를 읽음
3. **사용** — AI가 지시를 따르고 헬퍼 스크립트, 템플릿, 레퍼런스를 활용

스킬은 **지시**이며 코드가 아닙니다. AI는 가이드를 읽듯이 읽고 단계를 따릅니다.

---

## 🌟 이 컬렉션이 다른 이유

대부분의 "awesome" 스킬 목록은 외부 저장소를 가리키는 **링크 디렉토리**에 불과합니다. 이 컬렉션은 근본적으로 다릅니다:

| 기능 | 링크 디렉토리 | **이 컬렉션** |
|------|-------------|-------------|
| 콘텐츠 | 외부 링크만 | **51+ 완전한 스킬 구현** |
| 스크립트 | ❌ | ✅ 14+ 스킬에 헬퍼 스크립트 |
| 템플릿 | ❌ | ✅ 바로 사용 가능한 템플릿 |
| 레퍼런스 | ❌ | ✅ 엄선된 참고 문서 |
| 사용성 | 50+ 저장소 방문 필요 | **한 번 클론으로 모두 사용 가능** |
| 품질 | 편차가 큼 | **엄선 및 테스트 완료** |
| IDE 지원 | 제한적 | **10+ IDE 원클릭 설정** |
| 설치 프로그램 | ❌ | ✅ **원클릭 설치 스크립트** |

---

## 🔌 호환 가능한 AI 에이전트

| Agent | 스킬 경로 | 문서 |
|-------|----------|------|
| Claude Code | `~/.claude/skills/` | [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills) |
| Claude.ai | UI를 통해 업로드 | [support.claude.com](https://support.claude.com/en/articles/12512180-using-skills-in-claude) |
| GitHub Copilot | `.github/skills/` | [docs.github.com](https://docs.github.com/copilot/concepts/agents/about-agent-skills) |
| VS Code | `.github/skills/` | [code.visualstudio.com](https://code.visualstudio.com/docs/copilot/customization/agent-skills) |
| Codex (OpenAI) | `~/.codex/skills/` | [developers.openai.com](https://developers.openai.com/codex/skills) |
| Antigravity (Google) | `~/.gemini/antigravity/skills/` | [antigravity.google](https://antigravity.google/docs/skills) |
| Gemini CLI | `~/.gemini/skills/` | [geminicli.com](https://geminicli.com/docs/cli/skills/) |
| Kiro | 프로젝트 스킬 | [kiro.dev](https://kiro.dev/docs/skills/) |
| Cursor | `~/.cursor/skills/` | 스킬 표준 호환 |
| Windsurf | `~/.codeium/windsurf/skills/` | 스킬 표준 호환 |
| OpenCode | `~/.config/opencode/skill/` | 스킬 표준 호환 |
| Amp | `~/.config/agents/skills/` | 스킬 표준 호환 |

---

## 🚀 빠른 시작

### 방법 1: 원클릭 설치 (권장)

```bash
git clone https://github.com/ZhanlinCui/Ultimate-Agent-Skills-Collection.git
cd Ultimate-Agent-Skills-Collection
chmod +x install.sh
./install.sh
```

### 방법 2: 수동 설정

```bash
git clone https://github.com/ZhanlinCui/Ultimate-Agent-Skills-Collection.git ~/.agents/skills
mkdir -p ~/.cursor
ln -sf ~/.agents/skills ~/.cursor/skills
```

---

## 📂 스킬 디렉토리

### 🎨 크리에이티브 & 디자인

| 스킬 | 설명 | 포함 |
|------|------|------|
| **[algorithmic-art](./creative/algorithmic-art/)** | p5.js를 사용한 제너러티브 아트 제작 | `scripts` `templates` |
| **[canvas-design](./creative/canvas-design/)** | 디자인 철학을 활용한 .png 및 .pdf 비주얼 아트 제작 | `fonts` |
| **[frontend-design](./creative/frontend-design/)** | 뛰어난 디자인 품질의 프로덕션급 프런트엔드 인터페이스 구축 | |
| **[brand-guidelines](./creative/brand-guidelines/)** | 공식 브랜드 색상과 타이포그래피 적용 | |
| **[theme-factory](./creative/theme-factory/)** | 10+ 프리셋 테마 또는 커스텀 테마 즉시 생성 | `templates` |
| **[slack-gif-creator](./creative/slack-gif-creator/)** | Slack에 최적화된 애니메이션 GIF 제작 | `scripts` |
| **[ui-ux-pro-max](./creative/ui-ux-pro-max/)** | 궁극의 UI/UX 디자인 인텔리전스: 50+ 스타일, 97 색상 팔레트, 57 폰트 페어링 | `scripts` `references` |

### 📄 문서 스킬

| 스킬 | 설명 | 포함 |
|------|------|------|
| **[docx](./docs/docx/)** | 변경 추적 및 댓글 기능을 갖춘 Word 문서 생성/편집 | `scripts` `templates` `references` |
| **[pdf](./docs/pdf/)** | PDF 조작 — 텍스트/테이블 추출, 생성, 병합/분할, 폼 처리 | `scripts` |
| **[pptx](./docs/pptx/)** | PowerPoint 프레젠테이션 생성/편집, 레이아웃, 발표자 노트 | `scripts` `references` |
| **[xlsx](./docs/xlsx/)** | 스프레드시트 생성/편집, 수식, 서식, 데이터 분석 | `scripts` |
| **[doc-coauthoring](./docs/doc-coauthoring/)** | 문서 및 제안서 공동 작성 구조화 워크플로 | |
| **[internal-comms](./docs/internal-comms/)** | 내부 커뮤니케이션 작성: 상태 보고서, 뉴스레터, FAQ, 인시던트 보고서 | `templates` |
| **[github-release-assistant](./docs/github-release-assistant/)** | 이중 언어 GitHub 릴리스 문서 생성 (영어 + 중국어) | `scripts` `templates` `references` |

### 📝 Obsidian 지식 관리

| 스킬 | 설명 | 포함 |
|------|------|------|
| **[obsidian-helper](./obsidian/obsidian-helper/)** | `/daily`, `/capture`, `/review` 명령 지원 스마트 노트 어시스턴트 | `scripts` `references` |
| **[obsidian-bases](./obsidian/obsidian-bases/)** | Obsidian Bases (.base 파일) 생성: 뷰, 필터, 수식, 요약 | |
| **[obsidian-markdown](./obsidian/obsidian-markdown/)** | Obsidian 플레이버 마크다운 완전 가이드 | |
| **[project-to-obsidian](./obsidian/project-to-obsidian/)** | 코드 프로젝트를 Obsidian 지식 베이스로 변환 | `scripts` `templates` |
| **[json-canvas](./obsidian/json-canvas/)** | JSON Canvas 파일(.canvas) 생성: 노드, 엣지, 그룹, 플로차트, 마인드맵 | |

### 🛠️ 개발 & 기술

| 스킬 | 설명 | 포함 |
|------|------|------|
| **[mcp-builder](./dev/mcp-builder/)** | 고품질 MCP(Model Context Protocol) 서버 제작 | `scripts` `templates` |
| **[webapp-testing](./dev/webapp-testing/)** | Playwright를 사용한 로컬 웹 앱 테스트 | `scripts` |
| **[web-artifacts-builder](./dev/web-artifacts-builder/)** | React, Tailwind, shadcn/ui를 사용한 복합 HTML 아티팩트 구축 | `scripts` |
| **[skill-creator](./dev/skill-creator/)** | 효과적인 AI Agent 스킬 생성 가이드 | `scripts` `templates` |
| **[deploying-to-production](./dev/deploying-to-production/)** | GitHub 저장소 생성 및 Vercel 배포 자동화 | |
| **[internationalizing-websites](./dev/internationalizing-websites/)** | Next.js에 다국어 지원 및 SEO 설정 추가 | `scripts` `templates` |

### 🔍 SEO & 성능

| 스킬 | 설명 | 포함 |
|------|------|------|
| **[google-official-seo-guide](./seo/google-official-seo-guide/)** | Google 공식 SEO 가이드: 검색 최적화, 크롤링, 인덱싱 모범 사례 | `references` |
| **[web-performance-seo](./seo/web-performance-seo/)** | PageSpeed/Lighthouse 접근성 오류 수정으로 SEO 최적화 | |

### 🧠 계획 & 워크플로

| 스킬 | 설명 | 포함 |
|------|------|------|
| **[planning-with-files](./planning/planning-with-files/)** | Manus 스타일 파일 기반 계획: task_plan.md, findings.md, progress.md | `scripts` `templates` |
| **[writing-plans](./planning/writing-plans/)** | 코딩 전 다단계 작업의 구조화 계획 작성 | |
| **[executing-plans](./planning/executing-plans/)** | 리뷰 체크포인트가 포함된 구현 계획 실행 | |
| **[brainstorming](./planning/brainstorming/)** | 구현 전 사용자 의도, 요구사항, 설계 탐색 | |
| **[chat-compactor](./planning/chat-compactor/)** | AI 에이전트의 세션 간 연속성을 위한 세션 요약 생성 | |

### 🐛 디버깅 & 품질

| 스킬 | 설명 | 포함 |
|------|------|------|
| **[systematic-debugging](./quality/systematic-debugging/)** | 체계적 디버깅: 수정 전 근본 원인 분석 | `scripts` `references` |
| **[test-driven-development](./quality/test-driven-development/)** | TDD 워크플로: 테스트 먼저, 구현 나중에 | `templates` |
| **[verification-before-completion](./quality/verification-before-completion/)** | 완료 선언 전 작업 검증 | |
| **[receiving-code-review](./quality/receiving-code-review/)** | 코드 리뷰 피드백의 기술적 엄밀한 처리 | |
| **[requesting-code-review](./quality/requesting-code-review/)** | 완료된 작업에 대한 포괄적 코드 리뷰 요청 | `templates` |

### 🤖 Agent 오케스트레이션

| 스킬 | 설명 | 포함 |
|------|------|------|
| **[dispatching-parallel-agents](./agent/dispatching-parallel-agents/)** | 2+ 독립 작업을 병렬 서브에이전트에 디스패치 | |
| **[subagent-driven-development](./agent/subagent-driven-development/)** | 전문 서브에이전트로 계획 실행 | `scripts` `templates` |
| **[using-superpowers](./agent/using-superpowers/)** | 대화에서 스킬을 찾고 사용하는 방법 확립 | |
| **[writing-skills](./agent/writing-skills/)** | 배포 전 스킬 생성, 편집, 검증 | `scripts` `templates` `examples` |

### 🔧 Git & 개발 워크플로

| 스킬 | 설명 | 포함 |
|------|------|------|
| **[using-git-worktrees](./git-workflow/using-git-worktrees/)** | 기능 개발을 위한 격리된 git worktree 생성 | |
| **[finishing-a-development-branch](./git-workflow/finishing-a-development-branch/)** | 완료 가이드: 병합, PR, 정리 옵션 | |

### 🔗 통합 & 자동화

| 스킬 | 설명 | 포함 |
|------|------|------|
| **[notebooklm](./integration/notebooklm/)** | 브라우저 자동화를 통한 Google NotebookLM 쿼리 | `scripts` |
| **[x-article-publisher](./integration/x-article-publisher/)** | Markdown 기사를 X(Twitter) Articles에 게시 | `scripts` |
| **[doc-sync-tool](./integration/doc-sync-tool/)** | 프로젝트 간 Agents.md 등 파일 자동 동기화 | `scripts` |
| **[daily-news](./integration/daily-news/)** | 3단계 일일 뉴스 리포트 생성기: 메타데이터 수집→요약 생성→리포트 출력. 커스텀 소스 지원 | `scripts` `references` |
| **[web-access](./integration/web-access/)** | AI 에이전트에게 진정한 웹 브라우징 능력 부여: WebSearch→WebFetch→브라우저 CDP 모드 스마트 채널 선택 | `scripts` `references` |

### 🔺 Vercel 공식

| 스킬 | 설명 | 포함 |
|------|------|------|
| **[vercel-deploy](./vercel/vercel-deploy/)** | Vercel에 원클릭 배포, 인증 불필요 | `scripts` |
| **[vercel-react-best-practices](./vercel/vercel-react-best-practices/)** | Vercel 엔지니어링팀의 45가지 React/Next.js 성능 규칙 | `rules` |
| **[vercel-web-design-guidelines](./vercel/vercel-web-design-guidelines/)** | 웹 인터페이스 가이드라인 준수를 위한 UI 코드 리뷰 | |

---

## 📚 공식 스킬 레퍼런스

### Anthropic (Claude)

| 스킬 | 설명 | 소스 |
|------|------|------|
| docx | Word 문서 생성/편집/분석, 변경 추적 지원 | [anthropics/skills](https://github.com/anthropics/skills) |
| xlsx | 스프레드시트 조작: 수식, 차트, 데이터 변환 | [anthropics/skills](https://github.com/anthropics/skills) |
| pptx | 슬라이드 읽기/생성/조정 | [anthropics/skills](https://github.com/anthropics/skills) |
| pdf | PDF에서 텍스트, 테이블, 메타데이터 추출 | [anthropics/skills](https://github.com/anthropics/skills) |

### HuggingFace

| 스킬 | 설명 | 소스 |
|------|------|------|
| hf_dataset_creator | 구조화된 훈련 데이터셋 생성용 프롬프트, 템플릿, 스크립트 | [huggingface/skills](https://github.com/huggingface/skills) |
| hf_model_evaluation | 평가 작업 오케스트레이션, 보고서 생성, 메트릭 매핑 | [huggingface/skills](https://github.com/huggingface/skills) |
| hf-llm-trainer | 가이드, 헬퍼 스크립트, 비용 추정기 포함 포괄적 훈련 스킬 | [huggingface/skills](https://github.com/huggingface/skills) |
| hf-paper-publisher | Hugging Face Hub에서 연구 논문 출판 및 관리 도구 | [huggingface/skills](https://github.com/huggingface/skills) |

---

## 🌐 커뮤니티 스킬 & 컬렉션

| 저장소 | 설명 |
|--------|------|
| [anthropics/skills](https://github.com/anthropics/skills) | Anthropic 공식 컬렉션 |
| [openai/skills](https://github.com/openai/skills) | OpenAI Codex 공식 스킬 카탈로그 |
| [huggingface/skills](https://github.com/huggingface/skills) | HuggingFace 스킬 |
| [heilcheng/awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills) | 스킬 링크 & 리소스 큐레이션 목록 |
| [dmgrok/agent_skills_directory](https://github.com/dmgrok/agent_skills_directory) | npm 스타일 스킬 CLI |
| [karanb192/awesome-claude-skills](https://github.com/karanb192/awesome-claude-skills) | 50+ 검증된 Claude 스킬 |

---

## ⚙️ IDE/Agent 설정

```bash
git clone https://github.com/ZhanlinCui/Ultimate-Agent-Skills-Collection.git ~/.agents/skills
```

| IDE | 기본 스킬 경로 | 심볼릭 링크 명령 |
|-----|--------------|----------------|
| **Cursor** | `~/.cursor/skills/` | `mkdir -p ~/.cursor && ln -sf ~/.agents/skills ~/.cursor/skills` |
| **Claude Code** | `~/.claude/skills/` | `mkdir -p ~/.claude && ln -sf ~/.agents/skills ~/.claude/skills` |
| **GitHub Copilot** | `~/.copilot/skills/` | `mkdir -p ~/.copilot && ln -sf ~/.agents/skills ~/.copilot/skills` |
| **Codex (OpenAI)** | `~/.codex/skills/` | `mkdir -p ~/.codex && ln -sf ~/.agents/skills ~/.codex/skills` |
| **Windsurf** | `~/.codeium/windsurf/skills/` | `mkdir -p ~/.codeium/windsurf && ln -sf ~/.agents/skills ~/.codeium/windsurf/skills` |

---

## 📖 공식 튜토리얼 & 가이드

- [Claude에서 Skills 사용하기](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [커스텀 Skills 만들기](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- [Claude Code Skills 문서](https://code.claude.com/docs/en/skills)
- [Agent Skills에 대하여](https://docs.github.com/copilot/concepts/agents/about-agent-skills) — GitHub
- [VS Code Agent Skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills)
- [MCP 공식 문서](https://modelcontextprotocol.io/)

---

## ❓ FAQ

### Agent Skills란 무엇인가요?

AI 어시스턴트에게 특정 작업 수행 방법을 가르치는 지시 파일입니다. 필요할 때만 로드되어 AI가 빠르고 집중력 있게 유지됩니다.

### 이 컬렉션은 다른 스킬 컬렉션과 어떻게 다른가요?

대부분의 컬렉션은 **링크 디렉토리**입니다. 이 컬렉션은 스크립트, 템플릿, 레퍼런스 문서를 포함한 **51+ 완전한 스킬 구현**을 제공합니다.

### Agent Skills와 파인튜닝의 차이점은?

파인튜닝은 AI의 사고를 영구적으로 변경합니다(비용이 많이 들고 업데이트가 어려움). Agent Skills는 단순한 지시 파일로, AI 자체를 변경하지 않고 언제든 업데이트, 교환, 공유할 수 있습니다.

### Agent Skills와 MCP의 차이점은?

상호 보완적입니다:
- **Agent Skills** = AI에게 *방법*을 가르침 (워크플로, 모범 사례)
- **MCP** = AI가 *접근*하도록 도움 (API, 데이터베이스, 외부 도구)

### 여러 IDE에서 동시에 사용할 수 있나요?

네! `install.sh` 스크립트를 사용하면 모든 IDE에 동시에 스킬을 설정할 수 있습니다.

---

## 🤝 기여하기

기여를 환영합니다! **[CONTRIBUTING.md](CONTRIBUTING.md)**에서 전체 가이드라인을 확인하세요.

---

## 📜 라이선스

MIT License — [LICENSE](LICENSE)를 참조하세요.

---

## ⭐ Star 기록

<a href="https://star-history.com/#ZhanlinCui/Ultimate-Agent-Skills-Collection&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=ZhanlinCui/Ultimate-Agent-Skills-Collection&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=ZhanlinCui/Ultimate-Agent-Skills-Collection&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=ZhanlinCui/Ultimate-Agent-Skills-Collection&type=Date" />
 </picture>
</a>

---

## 📚 참고 자료

- [Anthropic: Claude에서 Skills 사용하기](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [Claude Code Skills 문서](https://code.claude.com/docs/en/skills)
- [GitHub Copilot: Agent Skills에 대하여](https://docs.github.com/copilot/concepts/agents/about-agent-skills)
- [OpenAI Codex Skills](https://developers.openai.com/codex/skills)
- [Model Context Protocol 문서](https://modelcontextprotocol.io/)

---

<div align="center">

**AI Agent 커뮤니티를 위해 ❤️ 로 제작**

*궁극의 프로덕션 레디 Agent 스킬 라이브러리*

</div>
