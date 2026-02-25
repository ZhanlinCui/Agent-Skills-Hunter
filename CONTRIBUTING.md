# Contributing to Ultimate Agent Skills Collection

Thank you for your interest in contributing! This guide will help you add new skills, improve existing ones, or help with translations.

[中文贡献指南](#中文贡献指南) | [日本語貢献ガイド](#日本語貢献ガイド)

---

## Table of Contents

- [Ways to Contribute](#ways-to-contribute)
- [Adding a New Skill](#adding-a-new-skill)
- [Improving an Existing Skill](#improving-an-existing-skill)
- [Translation Guidelines](#translation-guidelines)
- [Pull Request Process](#pull-request-process)
- [Quality Checklist](#quality-checklist)
- [What Will Get Your PR Closed](#what-will-get-your-pr-closed)

---

## Ways to Contribute

| Type | Description |
|------|-------------|
| **New Skill** | Add a complete skill folder with `SKILL.md` and optional scripts/templates |
| **Improvement** | Enhance existing skills with better instructions, scripts, or examples |
| **Bug Fix** | Fix errors in skill instructions or scripts |
| **Translation** | Help translate READMEs into new languages |
| **Documentation** | Improve project documentation, guides, or examples |

---

## Adding a New Skill

### Step 1: Create the Skill Folder

```
your-skill-name/
├── SKILL.md          # Required: Main instructions
├── scripts/          # Optional: Helper scripts
├── templates/        # Optional: Document/code templates
├── references/       # Optional: Reference documentation
└── examples/         # Optional: Usage examples
```

### Step 2: Write Your SKILL.md

Every `SKILL.md` must include frontmatter metadata:

```markdown
---
name: your-skill-name
description: A clear, one-line description of what this skill does and when to use it
version: "1.0"
---

# Your Skill Name

## Overview
[What this skill does and why it's useful]

## When to Use This Skill
- Use case 1
- Use case 2

## Instructions
[Step-by-step instructions for the AI agent]

## Examples
[Real-world usage examples]
```

### Step 3: Add to README

Add your skill to the appropriate category table in `README.md`:

```markdown
| **[your-skill-name](./your-skill-name/)** | Brief description of what the skill does |
```

### Step 4: Submit Your PR

- Use the **Skill Submission** issue template if you want feedback first
- Or go directly to a Pull Request

---

## Improving an Existing Skill

1. Check the skill's current state and identify what can be improved
2. Common improvements:
   - Add helper scripts to the `scripts/` folder
   - Add templates to `templates/`
   - Add reference documentation to `references/`
   - Improve SKILL.md instructions with better examples
   - Fix incorrect or outdated information
3. Explain your changes clearly in the PR description

---

## Translation Guidelines

This repository is maintained in **6 languages**:

| File | Language | Status |
|------|----------|--------|
| `README.md` | English | Source of truth |
| `README.zh-CN.md` | Simplified Chinese | Maintained |
| `README.ja.md` | Japanese | Maintained |
| `README.ko.md` | Korean | Maintained |
| `README.es.md` | Spanish | Maintained |
| `README.zh-TW.md` | Traditional Chinese | Maintained |

### Translation Rules

- **English README is the source of truth** — all other languages follow its structure
- **English-only PRs are fine** — maintainers will sync translations
- **Do NOT translate**: repository names, skill folder names, URLs, code blocks, CLI commands, technical identifiers
- **Do translate**: section headers, descriptions, explanatory text, FAQ answers
- Keep the same structure and section ordering across all files
- When updating a translated README, ensure it matches the current English version

---

## Pull Request Process

### Title Format

- Adding a skill: `feat: Add [skill-name] skill`
- Improving a skill: `improve: Enhance [skill-name] with [description]`
- Bug fix: `fix: [description]`
- Translation: `docs: Add/Update [language] translation`
- Documentation: `docs: [description]`

### PR Requirements

1. **One logical change per PR** — don't bundle unrelated changes
2. Ensure no merge conflicts with `main`
3. Fill out the PR template completely
4. All SKILL.md files must have valid frontmatter
5. Test any scripts you include

---

## Quality Checklist

Before submitting, verify:

- [ ] Skill folder follows the standard structure (`SKILL.md` + optional dirs)
- [ ] `SKILL.md` includes valid frontmatter (`name`, `description`)
- [ ] Instructions are clear, actionable, and agent-friendly
- [ ] No promotional or marketing language
- [ ] `SKILL.md` is under 500 lines for optimal performance
- [ ] Any scripts are tested and working
- [ ] No secrets, API keys, or sensitive data included
- [ ] Skill is placed in the correct category in README
- [ ] No duplicate of an existing skill

---

## What Will Get Your PR Closed

- Skill folder **missing `SKILL.md`**
- **Promotional or marketing language** in descriptions
- **Duplicate** of an existing skill without significant improvement
- **Broken scripts** that haven't been tested
- **Secrets or API keys** in any file
- **Unrelated changes** bundled together
- PR description is empty or unhelpful

---

## Questions?

- Open a [GitHub Issue](https://github.com/ZhanlinCui/Ultimate-Agent-Skills-Collection/issues) for questions
- Use the **Skill Submission** template to propose new skills
- Check existing issues before creating new ones

---

## 中文贡献指南

### 快速开始

1. Fork 本仓库
2. 创建技能文件夹，包含 `SKILL.md`
3. 将技能添加到 README 对应分类中
4. 提交 Pull Request

### 质量要求

- `SKILL.md` 必须包含 frontmatter 元数据
- 指令清晰、可操作
- 不含推广或营销语言
- 脚本必须经过测试

---

## 日本語貢献ガイド

### クイックスタート

1. このリポジトリをフォーク
2. `SKILL.md` を含むスキルフォルダを作成
3. README の適切なカテゴリにスキルを追加
4. プルリクエストを送信

### 品質要件

- `SKILL.md` にはフロントマターメタデータが必要
- 明確で実行可能な指示
- プロモーションやマーケティング言語は不可
- スクリプトはテスト済みであること
