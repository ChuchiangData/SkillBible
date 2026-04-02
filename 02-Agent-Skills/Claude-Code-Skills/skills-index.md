# Claude Code Skills - Master Index

> **Compiled**: 2026-04-02
> **Purpose**: Comprehensive index of all known Claude Code skills from official and community sources

---

## How Skills Work

Claude Code Skills are specialized folders containing a `SKILL.md` file (YAML frontmatter + markdown instructions) along with optional scripts, templates, and reference files. Skills use progressive disclosure: metadata (~100 tokens) loads for scanning, full instructions (<5k tokens) load when relevant, and bundled resources load only as needed.

**Availability**: Pro, Max, Team, and Enterprise Claude plans. Not available on free tier.

**Cross-compatibility**: Since December 2025, the SKILL.md format is an open standard adopted by Claude Code, OpenAI Codex CLI, ChatGPT, Gemini CLI, Cursor, Aider, Windsurf, and others.

---

## Official Anthropic Skills (17 skills)

> **Source**: [github.com/anthropics/skills](https://github.com/anthropics/skills)
> **License**: Apache 2.0 (most); Source-available (document skills)
> **Full details**: [official-anthropic-skills.md](official-anthropic-skills.md)

### Creative & Design (5 skills)

| # | Skill | Description | Triggers On |
|---|-------|-------------|-------------|
| 1 | **algorithmic-art** | Generative art via p5.js with seeded randomness and interactive parameter exploration | "generative art", "p5.js", algorithmic/procedural art requests |
| 2 | **canvas-design** | Museum-quality visual art in .png/.pdf using design philosophy manifesto approach | Poster, art, design, or static visual piece requests |
| 3 | **frontend-design** | Distinctive, production-grade frontend interfaces avoiding generic "AI slop" | Web components, pages, dashboards, React, HTML/CSS, styling/beautifying |
| 4 | **slack-gif-creator** | Animated GIFs optimized for Slack with validation and animation utilities | "make me a GIF", animated GIF for Slack |
| 5 | **theme-factory** | 10 pre-set themes (colors/fonts) for slides, docs, landing pages; custom theme generation | Theme, styling, color palette, fonts for artifacts |

### Development & Technical (5 skills)

| # | Skill | Description | Triggers On |
|---|-------|-------------|-------------|
| 6 | **claude-api** | Build apps with Claude API/Anthropic SDK; multi-language, model selection, thinking/effort config | `import anthropic`, Claude API, SDK usage |
| 7 | **mcp-builder** | Create MCP servers for LLM-external service integration (TypeScript/Python) | MCP server, Model Context Protocol, external API integration |
| 8 | **web-artifacts-builder** | Multi-component claude.ai HTML artifacts (React + Tailwind + shadcn/ui) | Complex artifacts needing state management, routing, shadcn/ui |
| 9 | **webapp-testing** | Test local web apps using Playwright (screenshots, logs, UI verification) | Test webapp, Playwright, browser testing, screenshot |
| 10 | **skill-creator** | Create, modify, evaluate, and benchmark skills | Create skill, edit skill, run evals, skill optimization |

### Document Skills (4 skills)

| # | Skill | Description | Triggers On |
|---|-------|-------------|-------------|
| 11 | **docx** | Create, read, edit Word documents with docx-js (create) or XML unpack/edit/repack (edit) | "Word doc", ".docx", report, memo, letter, template |
| 12 | **pdf** | Full PDF processing: read, merge, split, rotate, watermark, create, OCR, forms, encrypt | ".pdf", any PDF operation |
| 13 | **pptx** | Create, read, edit PowerPoint presentations with design-forward guidelines and mandatory QA | "slides", "presentation", "deck", ".pptx" |
| 14 | **xlsx** | Create, read, edit spreadsheets with formula support and financial model standards | "spreadsheet", ".xlsx", ".csv", Excel, formulas |

### Enterprise & Communication (3 skills)

| # | Skill | Description | Triggers On |
|---|-------|-------------|-------------|
| 15 | **brand-guidelines** | Anthropic brand colors (#d97757 orange, #6a9bcc blue, #788c5d green) and typography (Poppins/Lora) | Brand colors, styling, visual formatting, Anthropic brand |
| 16 | **doc-coauthoring** | 3-stage doc co-authoring: Context Gathering, Refinement & Structure, Reader Testing | "write a doc", "draft a proposal", PRD, design doc, RFC |
| 17 | **internal-comms** | Internal communications templates: 3P updates, newsletters, FAQs, incident reports | Status report, 3P update, newsletter, FAQ, internal comms |

---

## Community Skills Collections (5+ major repositories)

> **Full details**: [community-claude-skills.md](community-claude-skills.md)

### alirezarezvani/claude-skills -- 223 Skills across 9 Domains

> **Source**: [github.com/alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)
> **Browse**: [alirezarezvani.github.io/claude-skills/skills/](https://alirezarezvani.github.io/claude-skills/skills/)

| Domain | Count | Key Skills |
|--------|-------|------------|
| Engineering Core | 36 | senior-architect, senior-frontend, senior-backend, senior-fullstack, senior-qa, senior-devops, senior-secops, code-reviewer, senior-security, aws-solution-architect, ms365-tenant-manager, senior-data-engineer |
| Engineering POWERFUL | 36 | Enhanced versions of core engineering with advanced automation and patterns |
| Product Team | 15 | product-manager, product-analyst, product-designer, user-researcher, technical-writer |
| Marketing | 44 | content-creator, marketing-demand-acquisition, product-marketing, app-store-optimization, social-media-analyzer, seo-specialist, email-marketing, brand-strategist, growth-hacker, copywriter |
| Project Management | 7 | scrum-master, project-coordinator, release-manager, risk-analyst |
| C-Level Advisory | 34 | ceo-advisor, cto-advisor, cfo-advisor, cmo-advisor, coo-advisor, ciso-advisor, cpo-advisor, cdo-advisor, chro-advisor |
| Regulatory & QM | 14 | compliance-auditor, quality-manager, gdpr-specialist, sox-compliance, iso-auditor |
| Business & Growth | 5 | business-analyst, growth-strategist, market-researcher |
| Finance | 3 | financial-analyst, saas-metrics, financial-controller |

**Also includes**: 23 agents, 22 slash commands, 298 Python automation tools, 416 reference guides.

---

### obra/superpowers -- 20+ Battle-Tested Dev Skills

> **Source**: [github.com/obra/superpowers](https://github.com/obra/superpowers)
> **Community skills**: [github.com/obra/superpowers-skills](https://github.com/obra/superpowers-skills)

| Skill/Command | Description |
|---------------|-------------|
| /brainstorm | Collaborative brainstorming for design decisions |
| /write-plan | Write structured implementation plans |
| /execute-plan | Execute plans step-by-step with verification |
| using-superpowers | Meta-skill teaching Claude the superpowers framework |
| TDD skills | Test-driven development workflow |
| Debugging skills | Systematic debugging and root cause analysis |
| Collaboration skills | Human-AI pair programming patterns |
| skills-search | Discover available skills |

---

### sickn33/antigravity-awesome-skills -- 1,340+ Skills

> **Source**: [github.com/sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)

The largest aggregated collection. Includes installer CLI, bundles, workflows, and both official and community skill collections. Compatible with Claude Code, Cursor, Codex CLI, Gemini CLI, and Antigravity.

---

### travisvn/awesome-claude-skills -- Curated Directory

> **Source**: [github.com/travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills)

Not a skills repo but a curated "awesome list" linking to the best skills, resources, and tools across the ecosystem. Categories include Official Skills, Community Skills, Documentation, Tutorials, Security & Best Practices.

**Individual community skills referenced**: youtube-transcript, video-downloader, image-enhancer, article-extractor, content-research-writer.

---

### karanb192/awesome-claude-skills -- 50+ Verified Skills

> **Source**: [github.com/karanb192/awesome-claude-skills](https://github.com/karanb192/awesome-claude-skills)

50+ verified skills covering TDD, debugging, git workflows, document processing, and more.

---

### Additional Resources

| Resource | Description | Link |
|----------|-------------|------|
| SkillsMP | Agent Skills Marketplace for Claude, Codex, ChatGPT | [skillsmp.com](https://skillsmp.com/) |
| Claude Code Docs | Official skill documentation | [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills) |
| Claude Help Center | How to create custom skills | [support.claude.com](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) |
| Notion Skills | Notion integration skills for Claude | [notion.so/notiondevs](https://www.notion.so/notiondevs/Notion-Skills-for-Claude-28da4445d27180c7af1df7d8615723d0) |

---

## Skills by Use Case

### For Software Engineers

| Need | Recommended Skills | Source |
|------|--------------------|--------|
| Build with Claude API | claude-api | Official |
| Create MCP servers | mcp-builder | Official |
| Test web apps | webapp-testing | Official |
| Create new skills | skill-creator | Official |
| TDD workflow | TDD skills | obra/superpowers |
| Code review | code-reviewer | alirezarezvani |
| Architecture decisions | senior-architect | alirezarezvani |
| Debugging | Debugging skills | obra/superpowers |
| DevOps/CI-CD | senior-devops | alirezarezvani |
| Security review | senior-security, senior-secops | alirezarezvani |

### For Designers & Creatives

| Need | Recommended Skills | Source |
|------|--------------------|--------|
| Generative art | algorithmic-art | Official |
| Visual design/posters | canvas-design | Official |
| Frontend UI/UX | frontend-design | Official |
| Slack GIFs | slack-gif-creator | Official |
| Theme/branding | theme-factory, brand-guidelines | Official |
| React artifacts | web-artifacts-builder | Official |

### For Document Production

| Need | Recommended Skills | Source |
|------|--------------------|--------|
| Word documents | docx | Official |
| PDF processing | pdf | Official |
| Presentations | pptx | Official |
| Spreadsheets | xlsx | Official |
| Co-author docs | doc-coauthoring | Official |
| Internal comms | internal-comms | Official |

### For Business & Management

| Need | Recommended Skills | Source |
|------|--------------------|--------|
| Product management | product-manager | alirezarezvani |
| Marketing content | content-creator, copywriter | alirezarezvani |
| SEO optimization | seo-specialist | alirezarezvani |
| Project management | scrum-master | alirezarezvani |
| Financial modeling | financial-analyst | alirezarezvani |
| Strategic planning | ceo-advisor, cto-advisor | alirezarezvani |
| Compliance | compliance-auditor, gdpr-specialist | alirezarezvani |

### For Content & Research

| Need | Recommended Skills | Source |
|------|--------------------|--------|
| YouTube transcripts | youtube-transcript | Community |
| Article extraction | article-extractor | Community |
| Content research | content-research-writer | Community |
| Image enhancement | image-enhancer | Community |

---

## Quick Start: Installing Skills

### In Claude Code

```bash
# Official Anthropic skills
/plugin marketplace add anthropics/skills

# Community skills (alirezarezvani)
# See https://github.com/alirezarezvani/claude-skills/blob/main/INSTALLATION.md

# Obra superpowers
# See https://github.com/obra/superpowers README
```

### Custom Skills

Create your own skill by placing a folder with a `SKILL.md` file in your project's `.claude/skills/` directory:

```
your-project/
  .claude/
    skills/
      my-custom-skill/
        SKILL.md
```

SKILL.md format:

```yaml
---
name: my-custom-skill
description: Clear description of when Claude should use this skill
---

# My Custom Skill

Instructions for Claude to follow when this skill is active.

## Guidelines
- Guideline 1
- Guideline 2
```

---

## Statistics Summary

| Source | Skills Count | Domains |
|--------|-------------|---------|
| anthropics/skills (Official) | 17 | 4 categories (Creative, Dev, Document, Enterprise) |
| alirezarezvani/claude-skills | 223 | 9 domains (Engineering, Product, Marketing, PM, C-Level, Regulatory, Business, Finance) |
| obra/superpowers | 20+ | Software development methodology |
| sickn33/antigravity-awesome-skills | 1,340+ | Aggregated from multiple sources |
| karanb192/awesome-claude-skills | 50+ | TDD, debugging, git, documents |
| **Total unique skills (estimated)** | **~1,500+** | **All professional domains** |

---

## Sources & Attribution

- **Official Anthropic Skills**: [github.com/anthropics/skills](https://github.com/anthropics/skills) -- Apache 2.0 / Source-available
- **alirezarezvani/claude-skills**: [github.com/alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) -- 220+ skills, 9 domains
- **travisvn/awesome-claude-skills**: [github.com/travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) -- Curated directory
- **obra/superpowers**: [github.com/obra/superpowers](https://github.com/obra/superpowers) -- Dev methodology skills
- **sickn33/antigravity-awesome-skills**: [github.com/sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) -- 1,340+ aggregated skills
- **karanb192/awesome-claude-skills**: [github.com/karanb192/awesome-claude-skills](https://github.com/karanb192/awesome-claude-skills) -- 50+ verified skills
- **SkillsMP Marketplace**: [skillsmp.com](https://skillsmp.com/)
- **Claude Code Docs**: [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills)
- **Claude Help Center**: [support.claude.com](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
- **Best Claude Code Skills (2026)**: [dev.to/raxxostudios](https://dev.to/raxxostudios/best-claude-code-skills-plugins-2026-guide-4ak4)
- **Firecrawl Blog**: [firecrawl.dev/blog/best-claude-code-skills](https://www.firecrawl.dev/blog/best-claude-code-skills)
- **Analytics Vidhya**: [analyticsvidhya.com](https://www.analyticsvidhya.com/blog/2026/03/claude-skills-custom-skills-on-claude-code/)
