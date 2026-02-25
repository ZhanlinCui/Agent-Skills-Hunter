# Ultimate Agent Skills Collection

<div align="center">

<img src="https://img.shields.io/badge/Skills-49+-blueviolet?style=for-the-badge" alt="Skills Count" />
<img src="https://img.shields.io/badge/Calidad-Premium-gold?style=for-the-badge" alt="Calidad" />
<img src="https://img.shields.io/badge/Licencia-MIT-green?style=for-the-badge" alt="Licencia" />
<img src="https://img.shields.io/badge/Idiomas-6-blue?style=for-the-badge" alt="Idiomas" />

<br />

<img src="https://img.shields.io/github/stars/ZhanlinCui/Ultimate-Agent-Skills-Collection?style=social" alt="Stars" />
<img src="https://img.shields.io/github/forks/ZhanlinCui/Ultimate-Agent-Skills-Collection?style=social" alt="Forks" />
<img src="https://img.shields.io/github/last-commit/ZhanlinCui/Ultimate-Agent-Skills-Collection" alt="Último Commit" />
<img src="https://img.shields.io/github/contributors/ZhanlinCui/Ultimate-Agent-Skills-Collection" alt="Contribuidores" />

**La biblioteca de Agent Skills lista para producción más completa de Internet**

*No solo enlaces — implementaciones completas con scripts, plantillas y referencias, listas para usar hoy.*

[English](./README.md) | [简体中文](./README.zh-CN.md) | [繁體中文](./README.zh-TW.md) | [日本語](./README.ja.md) | [한국어](./README.ko.md)

</div>

---

## Tabla de Contenidos

- [¿Qué son los Agent Skills?](#-qué-son-los-agent-skills)
- [¿Por qué esta colección es diferente?](#-por-qué-esta-colección-es-diferente)
- [Agentes compatibles](#-agentes-compatibles)
- [Inicio rápido](#-inicio-rápido)
- [Directorio de Skills](#-directorio-de-skills)
- [Referencias oficiales de Skills](#-referencias-oficiales-de-skills)
- [Skills y colecciones de la comunidad](#-skills-y-colecciones-de-la-comunidad)
- [Configuración IDE/Agent](#-configuración-ideagent)
- [Tutoriales y guías oficiales](#-tutoriales-y-guías-oficiales)
- [FAQ](#-faq)
- [Contribuir](#-contribuir)
- [Licencia](#-licencia)
- [Historial de Stars](#-historial-de-stars)
- [Referencias](#-referencias)

---

## 📖 ¿Qué son los Agent Skills?

Los **Agent Skills** son "guías prácticas" para asistentes de IA. En lugar de que la IA necesite saber todo de antemano, los skills le permiten aprender nuevas habilidades sobre la marcha — como darle a alguien una tarjeta de receta en vez de hacerle memorizar un libro de cocina entero.

Los skills son carpetas que contienen archivos de instrucciones (`SKILL.md`) que enseñan a una IA cómo realizar tareas específicas.

### Cómo funcionan los Skills

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│   Explorar   │ ──▶ │    Cargar    │ ──▶ │    Usar     │
│ (ver nombres)│     │ (leer todo)  │     │ (ejecutar)  │
└─────────────┘     └──────────────┘     └─────────────┘
```

1. **Explorar** — La IA ve una lista de skills disponibles (nombres y descripciones breves)
2. **Cargar** — Cuando se necesita un skill, la IA lee las instrucciones completas
3. **Usar** — La IA sigue las instrucciones y usa scripts auxiliares, plantillas o referencias

Los skills son **instrucciones**, no código. La IA los lee como un humano leería una guía, y luego sigue los pasos.

---

## 🌟 ¿Por qué esta colección es diferente?

La mayoría de las listas "awesome" de skills son solo **directorios de enlaces** que apuntan a repositorios externos. Esta colección es fundamentalmente diferente:

| Característica | Directorios de enlaces | **Esta colección** |
|---------------|----------------------|-------------------|
| Contenido | Solo enlaces externos | **49+ implementaciones completas** |
| Scripts | ❌ | ✅ 14+ skills con scripts auxiliares |
| Plantillas | ❌ | ✅ Plantillas listas para usar |
| Referencias | ❌ | ✅ Documentación de referencia curada |
| Usabilidad | Visitar 50+ repos | **Clonar una vez, usar todo** |
| Calidad | Varía mucho | **Curado y probado** |
| Soporte IDE | Limitado | **10+ IDEs configuración un clic** |
| Instalador | ❌ | ✅ **Script de instalación un clic** |

---

## 🔌 Agentes compatibles

| Agente | Ruta de Skills | Documentación |
|--------|---------------|---------------|
| Claude Code | `~/.claude/skills/` | [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills) |
| Claude.ai | Subir via UI | [support.claude.com](https://support.claude.com/en/articles/12512180-using-skills-in-claude) |
| GitHub Copilot | `.github/skills/` | [docs.github.com](https://docs.github.com/copilot/concepts/agents/about-agent-skills) |
| VS Code | `.github/skills/` | [code.visualstudio.com](https://code.visualstudio.com/docs/copilot/customization/agent-skills) |
| Codex (OpenAI) | `~/.codex/skills/` | [developers.openai.com](https://developers.openai.com/codex/skills) |
| Antigravity (Google) | `~/.gemini/antigravity/skills/` | [antigravity.google](https://antigravity.google/docs/skills) |
| Gemini CLI | `~/.gemini/skills/` | [geminicli.com](https://geminicli.com/docs/cli/skills/) |
| Kiro | Skills de proyecto | [kiro.dev](https://kiro.dev/docs/skills/) |
| Cursor | `~/.cursor/skills/` | Compatible con estándar de skills |
| Windsurf | `~/.codeium/windsurf/skills/` | Compatible con estándar de skills |
| OpenCode | `~/.config/opencode/skill/` | Compatible con estándar de skills |
| Amp | `~/.config/agents/skills/` | Compatible con estándar de skills |

---

## 🚀 Inicio rápido

### Opción 1: Instalación un clic (Recomendado)

```bash
git clone https://github.com/ZhanlinCui/Ultimate-Agent-Skills-Collection.git
cd Ultimate-Agent-Skills-Collection
chmod +x install.sh
./install.sh
```

### Opción 2: Configuración manual

```bash
git clone https://github.com/ZhanlinCui/Ultimate-Agent-Skills-Collection.git ~/.agents/skills
mkdir -p ~/.cursor
ln -sf ~/.agents/skills ~/.cursor/skills
```

---

## 📂 Directorio de Skills

### 🎨 Creativo y Diseño

| Skill | Descripción | Incluye |
|-------|-------------|---------|
| **[algorithmic-art](./creative/algorithmic-art/)** | Crear arte generativo usando p5.js | `scripts` `templates` |
| **[canvas-design](./creative/canvas-design/)** | Crear arte visual hermoso en .png y .pdf | `fonts` |
| **[frontend-design](./creative/frontend-design/)** | Construir interfaces frontend de nivel producción | |
| **[brand-guidelines](./creative/brand-guidelines/)** | Aplicar colores y tipografía oficial de marca | |
| **[theme-factory](./creative/theme-factory/)** | 10+ temas preestablecidos o temas personalizados al instante | `templates` |
| **[slack-gif-creator](./creative/slack-gif-creator/)** | Crear GIFs animados optimizados para Slack | `scripts` |
| **[ui-ux-pro-max](./creative/ui-ux-pro-max/)** | Inteligencia UI/UX definitiva: 50+ estilos, 97 paletas, 57 combinaciones de fuentes | `scripts` `references` |

### 📄 Skills de Documentos

| Skill | Descripción | Incluye |
|-------|-------------|---------|
| **[docx](./docs/docx/)** | Creación/edición integral de documentos Word con control de cambios | `scripts` `templates` `references` |
| **[pdf](./docs/pdf/)** | Manipulación de PDF — extraer texto/tablas, crear, combinar/dividir | `scripts` |
| **[pptx](./docs/pptx/)** | Creación/edición de presentaciones PowerPoint, diseños, notas | `scripts` `references` |
| **[xlsx](./docs/xlsx/)** | Creación/edición de hojas de cálculo, fórmulas, formato, análisis | `scripts` |
| **[doc-coauthoring](./docs/doc-coauthoring/)** | Flujo de trabajo estructurado para coautoría de documentos | |
| **[internal-comms](./docs/internal-comms/)** | Comunicaciones internas: reportes, newsletters, FAQ, incidentes | `templates` |
| **[github-release-assistant](./docs/github-release-assistant/)** | Documentación de releases bilingüe (inglés + chino) | `scripts` `templates` `references` |

### 📝 Gestión de Conocimiento Obsidian

| Skill | Descripción | Incluye |
|-------|-------------|---------|
| **[obsidian-helper](./obsidian/obsidian-helper/)** | Asistente de notas inteligente con comandos `/daily`, `/capture`, `/review` | `scripts` `references` |
| **[obsidian-bases](./obsidian/obsidian-bases/)** | Crear Obsidian Bases (.base) con vistas, filtros, fórmulas | |
| **[obsidian-markdown](./obsidian/obsidian-markdown/)** | Guía completa de Obsidian Flavored Markdown | |
| **[project-to-obsidian](./obsidian/project-to-obsidian/)** | Convertir proyectos de código en bases de conocimiento Obsidian | `scripts` `templates` |
| **[json-canvas](./obsidian/json-canvas/)** | Crear archivos JSON Canvas (.canvas) | |

### 🛠️ Desarrollo y Técnico

| Skill | Descripción | Incluye |
|-------|-------------|---------|
| **[mcp-builder](./dev/mcp-builder/)** | Crear servidores MCP de alta calidad | `scripts` `templates` |
| **[webapp-testing](./dev/webapp-testing/)** | Probar aplicaciones web locales con Playwright | `scripts` |
| **[web-artifacts-builder](./dev/web-artifacts-builder/)** | Construir artefactos HTML con React, Tailwind, shadcn/ui | `scripts` |
| **[skill-creator](./dev/skill-creator/)** | Guía para crear skills efectivos de AI Agent | `scripts` `templates` |
| **[deploying-to-production](./dev/deploying-to-production/)** | Automatizar creación de repos GitHub y deploy en Vercel | |
| **[internationalizing-websites](./dev/internationalizing-websites/)** | Agregar soporte multiidioma a Next.js con configuración SEO | `scripts` `templates` |

### 🔍 SEO y Rendimiento

| Skill | Descripción | Incluye |
|-------|-------------|---------|
| **[google-official-seo-guide](./seo/google-official-seo-guide/)** | Guía SEO oficial de Google | `references` |
| **[web-performance-seo](./seo/web-performance-seo/)** | Corregir errores de accesibilidad PageSpeed/Lighthouse | |

### 🧠 Planificación y Flujo de Trabajo

| Skill | Descripción | Incluye |
|-------|-------------|---------|
| **[planning-with-files](./planning/planning-with-files/)** | Planificación basada en archivos estilo Manus | `scripts` `templates` |
| **[writing-plans](./planning/writing-plans/)** | Crear planes estructurados antes de codificar | |
| **[executing-plans](./planning/executing-plans/)** | Ejecutar planes con puntos de revisión | |
| **[brainstorming](./planning/brainstorming/)** | Explorar intención, requisitos y diseño antes de implementar | |
| **[chat-compactor](./planning/chat-compactor/)** | Generar resúmenes de sesión para continuidad del agente | |

### 🐛 Depuración y Calidad

| Skill | Descripción | Incluye |
|-------|-------------|---------|
| **[systematic-debugging](./quality/systematic-debugging/)** | Depuración sistemática: análisis de causa raíz primero | `scripts` `references` |
| **[test-driven-development](./quality/test-driven-development/)** | Flujo TDD: pruebas primero, implementación después | `templates` |
| **[verification-before-completion](./quality/verification-before-completion/)** | Verificar antes de declarar completado | |
| **[receiving-code-review](./quality/receiving-code-review/)** | Manejar feedback de code review con rigor técnico | |
| **[requesting-code-review](./quality/requesting-code-review/)** | Solicitar revisiones de código exhaustivas | `templates` |

### 🤖 Orquestación de Agentes

| Skill | Descripción | Incluye |
|-------|-------------|---------|
| **[dispatching-parallel-agents](./agent/dispatching-parallel-agents/)** | Despachar 2+ tareas independientes a subagentes paralelos | |
| **[subagent-driven-development](./agent/subagent-driven-development/)** | Ejecutar planes con subagentes especializados | `scripts` `templates` |
| **[using-superpowers](./agent/using-superpowers/)** | Establecer cómo encontrar y usar skills en conversaciones | |
| **[writing-skills](./agent/writing-skills/)** | Crear, editar y verificar skills antes del despliegue | `scripts` `templates` `examples` |

### 🔧 Git y Flujo de Desarrollo

| Skill | Descripción | Incluye |
|-------|-------------|---------|
| **[using-git-worktrees](./git-workflow/using-git-worktrees/)** | Crear worktrees git aislados para desarrollo | |
| **[finishing-a-development-branch](./git-workflow/finishing-a-development-branch/)** | Guía de completado: merge, PR, o limpieza | |

### 🔗 Integración y Automatización

| Skill | Descripción | Incluye |
|-------|-------------|---------|
| **[notebooklm](./integration/notebooklm/)** | Consultar Google NotebookLM mediante automatización del navegador | `scripts` |
| **[x-article-publisher](./integration/x-article-publisher/)** | Publicar artículos Markdown en X (Twitter) Articles | `scripts` |
| **[doc-sync-tool](./integration/doc-sync-tool/)** | Sincronizar automáticamente archivos entre proyectos | `scripts` |

### 🔺 Vercel Oficial

| Skill | Descripción | Incluye |
|-------|-------------|---------|
| **[vercel-deploy](./vercel/vercel-deploy/)** | Deploy un clic a Vercel, sin autenticación necesaria | `scripts` |
| **[vercel-react-best-practices](./vercel/vercel-react-best-practices/)** | 45 reglas de rendimiento React/Next.js del equipo de Vercel | `rules` |
| **[vercel-web-design-guidelines](./vercel/vercel-web-design-guidelines/)** | Revisión de UI para cumplimiento de Directrices de Interfaz Web | |

---

## 📚 Referencias oficiales de Skills

### Anthropic (Claude)

| Skill | Descripción | Fuente |
|-------|-------------|--------|
| docx | Crear, editar, analizar documentos Word | [anthropics/skills](https://github.com/anthropics/skills) |
| xlsx | Manipulación de hojas de cálculo | [anthropics/skills](https://github.com/anthropics/skills) |
| pptx | Leer, generar y ajustar presentaciones | [anthropics/skills](https://github.com/anthropics/skills) |
| pdf | Extraer texto, tablas, metadatos de PDFs | [anthropics/skills](https://github.com/anthropics/skills) |

### HuggingFace

| Skill | Descripción | Fuente |
|-------|-------------|--------|
| hf_dataset_creator | Prompts, plantillas y scripts para crear datasets de entrenamiento | [huggingface/skills](https://github.com/huggingface/skills) |
| hf_model_evaluation | Orquestación de evaluación, generación de reportes | [huggingface/skills](https://github.com/huggingface/skills) |
| hf-llm-trainer | Skill de entrenamiento integral con estimadores de costos | [huggingface/skills](https://github.com/huggingface/skills) |
| hf-paper-publisher | Herramientas para publicar papers en Hugging Face Hub | [huggingface/skills](https://github.com/huggingface/skills) |

---

## 🌐 Skills y colecciones de la comunidad

| Repositorio | Descripción |
|-------------|-------------|
| [anthropics/skills](https://github.com/anthropics/skills) | Colección oficial de Anthropic |
| [openai/skills](https://github.com/openai/skills) | Catálogo oficial de skills Codex |
| [huggingface/skills](https://github.com/huggingface/skills) | Skills de HuggingFace |
| [heilcheng/awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills) | Lista curada de enlaces de skills |
| [dmgrok/agent_skills_directory](https://github.com/dmgrok/agent_skills_directory) | CLI estilo npm para skills |
| [karanb192/awesome-claude-skills](https://github.com/karanb192/awesome-claude-skills) | 50+ skills verificados para Claude |

---

## ⚙️ Configuración IDE/Agent

```bash
git clone https://github.com/ZhanlinCui/Ultimate-Agent-Skills-Collection.git ~/.agents/skills
```

| IDE | Ruta de Skills | Comando Symlink |
|-----|---------------|-----------------|
| **Cursor** | `~/.cursor/skills/` | `mkdir -p ~/.cursor && ln -sf ~/.agents/skills ~/.cursor/skills` |
| **Claude Code** | `~/.claude/skills/` | `mkdir -p ~/.claude && ln -sf ~/.agents/skills ~/.claude/skills` |
| **GitHub Copilot** | `~/.copilot/skills/` | `mkdir -p ~/.copilot && ln -sf ~/.agents/skills ~/.copilot/skills` |
| **Codex (OpenAI)** | `~/.codex/skills/` | `mkdir -p ~/.codex && ln -sf ~/.agents/skills ~/.codex/skills` |
| **Windsurf** | `~/.codeium/windsurf/skills/` | `mkdir -p ~/.codeium/windsurf && ln -sf ~/.agents/skills ~/.codeium/windsurf/skills` |

---

## 📖 Tutoriales y guías oficiales

- [Usar Skills en Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [Crear Skills personalizados](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- [Documentación Claude Code Skills](https://code.claude.com/docs/en/skills)
- [Sobre Agent Skills](https://docs.github.com/copilot/concepts/agents/about-agent-skills) — GitHub
- [VS Code Agent Skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills)
- [Documentación MCP](https://modelcontextprotocol.io/)

---

## ❓ FAQ

### ¿Qué son los Agent Skills?

Son archivos de instrucciones que enseñan a asistentes de IA cómo realizar tareas específicas. Se cargan solo cuando se necesitan, manteniendo la IA rápida y enfocada.

### ¿Cómo se diferencia esta colección de otras?

La mayoría son **directorios de enlaces**. Esta colección contiene **49+ implementaciones completas** con scripts, plantillas y documentación de referencia.

### ¿Cuál es la diferencia entre Agent Skills y fine-tuning?

El fine-tuning cambia permanentemente cómo piensa una IA (costoso y difícil de actualizar). Los Agent Skills son archivos de instrucciones que puedes actualizar, intercambiar o compartir sin modificar la IA.

### ¿Cuál es la diferencia entre Agent Skills y MCP?

Son complementarios:
- **Agent Skills** = enseñan a la IA *cómo* hacer algo (flujos de trabajo, mejores prácticas)
- **MCP** = ayudan a la IA a *acceder* a cosas (APIs, bases de datos, herramientas externas)

### ¿Puedo usarlos en varios IDEs simultáneamente?

¡Sí! Usa el script `install.sh` para configurar skills en todos tus IDEs a la vez.

---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Consulta **[CONTRIBUTING.md](CONTRIBUTING.md)** para las directrices completas.

---

## 📜 Licencia

MIT License — ver [LICENSE](LICENSE) para detalles.

---

## ⭐ Historial de Stars

<a href="https://star-history.com/#ZhanlinCui/Ultimate-Agent-Skills-Collection&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=ZhanlinCui/Ultimate-Agent-Skills-Collection&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=ZhanlinCui/Ultimate-Agent-Skills-Collection&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=ZhanlinCui/Ultimate-Agent-Skills-Collection&type=Date" />
 </picture>
</a>

---

## 📚 Referencias

- [Anthropic: Usar Skills en Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [Claude Code Skills](https://code.claude.com/docs/en/skills)
- [GitHub Copilot: Agent Skills](https://docs.github.com/copilot/concepts/agents/about-agent-skills)
- [OpenAI Codex Skills](https://developers.openai.com/codex/skills)
- [Model Context Protocol](https://modelcontextprotocol.io/)

---

<div align="center">

**Hecho con ❤️ para la comunidad de AI Agents**

*La biblioteca definitiva de Agent Skills lista para producción*

</div>
