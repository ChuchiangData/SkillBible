# Official Anthropic Skills - Complete Reference

> **Source**: [github.com/anthropics/skills](https://github.com/anthropics/skills)
> **License**: Apache 2.0 (most skills); Source-available for document skills (docx, pdf, pptx, xlsx)
> **Last fetched**: 2026-04-02

## Overview

The official Anthropic skills repository contains 17 production-ready skills organized into categories. Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks. Each skill has a `SKILL.md` file with YAML frontmatter defining when to trigger and markdown content with detailed instructions.

### Skill Structure

```
skill-folder/
  SKILL.md          # Required: YAML frontmatter + instructions
  scripts/          # Optional: helper scripts
  templates/        # Optional: document templates
  reference/        # Optional: reference files
  examples/         # Optional: example content
```

### YAML Frontmatter Format

```yaml
---
name: my-skill-name
description: A clear description of what this skill does and when to use it
---
```

### Installation (Claude Code)

```bash
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills
```

---

## Skills by Category

### Creative & Design

#### 1. algorithmic-art

- **Name**: `algorithmic-art`
- **Description**: Creates generative art through a two-step process: (1) Algorithmic Philosophy Creation (.md file) defining a computational aesthetic movement, and (2) p5.js Implementation (.html artifact) expressing the philosophy through interactive code.
- **Key Features**:
  - Seeded randomness for reproducible art
  - Interactive parameter controls (sliders, color pickers)
  - Seed navigation (previous/next/random/jump)
  - Self-contained single HTML artifact
  - Uses Anthropic branding template (Poppins/Lora fonts)
- **Process**: Creates a 4-6 paragraph manifesto describing computational processes, then implements in p5.js with interactive viewer
- **Philosophy Examples**: "Organic Turbulence" (Perlin noise flow fields), "Quantum Harmonics" (sine wave interference), "Recursive Whispers" (L-system branching), "Field Dynamics" (vector field particles), "Stochastic Crystallization" (circle packing/Voronoi)
- **Requirements**: Template-based viewer with fixed layout structure and Anthropic branding; customizable algorithm, parameters, and controls

---

#### 2. canvas-design

- **Name**: `canvas-design`
- **Description**: Create beautiful visual art in .png and .pdf documents using design philosophy. Use when the user asks to create a poster, piece of art, design, or other static piece. Create original visual designs, never copying existing artists' work.
- **Key Features**:
  - Two-step process: Design Philosophy Creation (.md) then Canvas Creation (.pdf/.png)
  - Museum/magazine quality output
  - Sophisticated subtle references embedded in art
  - Multi-page coffee table book option
- **Process**:
  1. Name a visual movement (1-2 words): "Brutalist Joy", "Chromatic Silence", "Metabolist Dreams"
  2. Write 4-6 paragraph manifesto emphasizing visual expression, spatial communication, minimal text
  3. Deduce subtle conceptual thread from user's request
  4. Express on canvas using design philosophy with expert craftsmanship
- **Philosophy Examples**: "Concrete Poetry" (monumental form + bold geometry), "Chromatic Language" (color as information system), "Analog Meditation" (texture + negative space), "Organic Systems" (natural clustering), "Geometric Silence" (grid-based precision)
- **Output**: Single downloadable .pdf or .png alongside design philosophy .md file

---

#### 3. frontend-design

- **Name**: `frontend-design`
- **Description**: Create distinctive, production-grade frontend interfaces with high design quality. Use when the user asks to build web components, pages, artifacts, posters, or applications. Generates creative, polished code and UI design that avoids generic AI aesthetics.
- **Key Features**:
  - Bold aesthetic direction (brutally minimal, maximalist chaos, retro-futuristic, etc.)
  - Production-grade functional code (HTML/CSS/JS, React, Vue)
  - Anti-"AI slop" guidelines
  - Context-specific character
- **Design Thinking Process**: Purpose, Tone, Constraints, Differentiation
- **Focus Areas**:
  - Typography: Distinctive, characterful font choices (avoid Arial, Inter, Roboto)
  - Color & Theme: CSS variables, dominant colors with sharp accents
  - Motion: CSS-only animations, scroll-triggering, hover states
  - Spatial Composition: Asymmetry, overlap, diagonal flow, grid-breaking
  - Backgrounds: Gradient meshes, noise textures, geometric patterns, grain overlays
- **Anti-patterns**: Overused fonts (Inter, Roboto), purple gradients on white, predictable layouts, cookie-cutter design

---

#### 4. slack-gif-creator

- **Name**: `slack-gif-creator`
- **Description**: Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users request animated GIFs for Slack.
- **Key Features**:
  - GIFBuilder for frame assembly and optimization
  - Validators for Slack compliance
  - Easing functions for smooth motion
  - Frame helper utilities
- **Slack Requirements**: Emoji GIFs: 128x128; Message GIFs: 480x480; FPS: 10-30; Colors: 48-128; Duration: under 3 seconds for emoji
- **Animation Concepts**: Shake/Vibrate, Pulse/Heartbeat, Bounce, Spin/Rotate, Fade In/Out, Slide, Zoom, Explode/Particle Burst
- **Dependencies**: PIL/Pillow, imageio, numpy

---

#### 5. theme-factory

- **Name**: `theme-factory`
- **Description**: Toolkit for styling artifacts with a theme. 10 pre-set themes with colors/fonts for slides, docs, reporting, HTML landing pages, etc. Can generate new themes on-the-fly.
- **10 Built-in Themes**:
  1. Ocean Depths - Professional and calming maritime theme
  2. Sunset Boulevard - Warm and vibrant sunset colors
  3. Forest Canopy - Natural and grounded earth tones
  4. Modern Minimalist - Clean and contemporary grayscale
  5. Golden Hour - Rich and warm autumnal palette
  6. Arctic Frost - Cool and crisp winter-inspired theme
  7. Desert Rose - Soft and sophisticated dusty tones
  8. Tech Innovation - Bold and modern tech aesthetic
  9. Botanical Garden - Fresh and organic garden colors
  10. Midnight Galaxy - Dramatic and cosmic deep tones
- **Process**: Show theme-showcase.pdf, ask for choice, apply colors and fonts consistently

---

### Development & Technical

#### 6. claude-api

- **Name**: `claude-api`
- **Description**: Build apps with the Claude API or Anthropic SDK. TRIGGER when code imports `anthropic`/`@anthropic-ai/sdk`/`claude_agent_sdk`, or user asks to use Claude API, Anthropic SDKs, or Agent SDK.
- **Key Features**:
  - Multi-language support (Python, TypeScript, Java, Go, Ruby, C#, PHP, cURL)
  - Auto-detects project language from file extensions
  - Decision tree for choosing between Single LLM Call, Workflow, or Agent
  - Current model reference table with pricing
  - Thinking & Effort configuration guidance
  - Compaction, Prompt Caching, and Streaming guidance
- **Default Model**: Claude Opus 4.6 (`claude-opus-4-6`) with adaptive thinking
- **Architecture Tiers**:
  - Single LLM Call: Classification, summarization, extraction, Q&A
  - Workflow: Claude API + tool use (code-controlled multi-step)
  - Agent: Claude API + tool use or Agent SDK (open-ended, model-driven)
- **Language-Specific Features**: Tool Runner support (Python, TypeScript, Java, Go, Ruby, PHP beta), Agent SDK (Python, TypeScript only)

---

#### 7. mcp-builder

- **Name**: `mcp-builder`
- **Description**: Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools.
- **Key Features**:
  - 4-phase development workflow (Research, Implementation, Review, Evaluations)
  - TypeScript recommended (good SDK support, execution environment compatibility)
  - Supports both Python (FastMCP) and TypeScript (MCP SDK)
  - Built-in evaluation creation guide
- **Phases**:
  1. Deep Research and Planning (API coverage, MCP protocol, framework docs)
  2. Implementation (project structure, core infrastructure, tools with Zod/Pydantic schemas)
  3. Review and Test (code quality, build verification, MCP Inspector)
  4. Create Evaluations (10 complex, realistic, verifiable test questions)
- **Tool Design**: Input schemas with Zod/Pydantic, output schemas for structured data, actionable error messages, pagination support, tool annotations (readOnlyHint, destructiveHint, etc.)

---

#### 8. web-artifacts-builder

- **Name**: `web-artifacts-builder`
- **Description**: Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components.
- **Stack**: React 18 + TypeScript + Vite + Parcel (bundling) + Tailwind CSS + shadcn/ui
- **Key Features**:
  - 40+ shadcn/ui components pre-installed
  - All Radix UI dependencies included
  - Bundles to single self-contained HTML file
  - Anti-"AI slop" design guidelines
- **Workflow**:
  1. `bash scripts/init-artifact.sh <project-name>` - Initialize project
  2. Edit generated code
  3. `bash scripts/bundle-artifact.sh` - Bundle to single HTML
  4. Display artifact to user
  5. Optional: Test with Playwright/Puppeteer

---

#### 9. webapp-testing

- **Name**: `webapp-testing`
- **Description**: Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs.
- **Key Features**:
  - Native Python Playwright scripts
  - Server lifecycle management (scripts/with_server.py)
  - Multi-server support (backend + frontend)
  - Reconnaissance-then-action pattern
- **Decision Tree**: Static HTML -> Read file directly -> Write Playwright script; Dynamic webapp -> Use with_server.py helper -> Navigate + wait for networkidle -> Screenshot/inspect DOM -> Execute actions
- **Best Practices**: Always headless chromium, wait for networkidle before inspection, use descriptive selectors (text=, role=, CSS, IDs)

---

#### 10. skill-creator

- **Name**: `skill-creator`
- **Description**: Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, optimize, run evals, benchmark performance, or optimize triggering descriptions.
- **Process**:
  1. Decide what the skill should do
  2. Write a draft skill
  3. Create test prompts and run Claude with the skill
  4. Evaluate results qualitatively and quantitatively
  5. Rewrite skill based on feedback
  6. Repeat until satisfied
  7. Expand test set for larger scale validation
- **Features**: Blind comparison between skill versions, description optimization for trigger accuracy, eval-viewer for result review

---

### Document Skills (Source-Available License)

#### 11. docx

- **Name**: `docx`
- **Description**: Use whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers on any mention of 'Word doc', 'word document', '.docx', or requests for formatted documents.
- **Key Features**:
  - Create new documents with docx-js (Node.js)
  - Edit existing documents via XML unpack/edit/repack
  - Read/analyze with pandoc
  - Convert .doc to .docx via LibreOffice
  - Table of Contents, headers/footers, page numbers
  - Tables with dual-width system
  - Images with alt text
  - Hyperlinks (external and internal bookmarks)
  - Lists (bullet and numbered via LevelFormat)
  - Multi-column layouts
  - Tracked changes and comments support
- **Critical Rules**: Always set page size explicitly (defaults to A4), use Arial font, dual widths for tables, WidthType.DXA only, never Unicode bullets, images require type parameter

---

#### 12. pdf

- **Name**: `pdf`
- **Description**: Use whenever the user wants to do anything with PDF files -- reading, extracting, combining, splitting, rotating, watermarking, creating, form filling, encrypting/decrypting, image extraction, OCR.
- **Key Libraries**:
  - pypdf: Basic operations (merge, split, rotate, encrypt)
  - pdfplumber: Text and table extraction
  - reportlab: PDF creation (Canvas and Platypus)
  - pytesseract + pdf2image: OCR for scanned PDFs
  - qpdf/pdftk: Command-line operations
- **Important**: Never use Unicode subscript/superscript characters in ReportLab PDFs (renders as black boxes); use `<sub>` and `<super>` XML tags instead

---

#### 13. pptx

- **Name**: `pptx`
- **Description**: Use any time a .pptx file is involved in any way -- as input, output, or both. Creating, reading, editing, combining, splitting, working with templates, layouts, speaker notes, or comments.
- **Key Features**:
  - Read content with markitdown
  - Edit existing via XML unpack/edit/repack
  - Create from scratch with pptxgenjs
  - 10 color palette presets
  - Font pairing recommendations
  - Mandatory QA with subagents for visual inspection
- **Design Principles**: Bold color palettes, every slide needs a visual element, varied layouts (two-column, icon+text rows, 2x2 grids, half-bleed images), large stat callouts, never repeat same layout
- **QA Process**: Content QA (markitdown extraction), Visual QA (convert to images, inspect with subagents), Verification loop until no new issues

---

#### 14. xlsx

- **Name**: `xlsx`
- **Description**: Use any time a spreadsheet file is the primary input or output. Creating, reading, editing .xlsx/.xlsm/.csv/.tsv files, cleaning messy data, format conversion.
- **Key Features**:
  - Data analysis with pandas
  - Formulas and formatting with openpyxl
  - Mandatory formula recalculation via LibreOffice (scripts/recalc.py)
  - Financial model color coding standards
  - Industry-standard number formatting
- **Critical Rules**: Always use Excel formulas (never hardcode calculated values), recalculate formulas after every save, verify zero formula errors
- **Financial Model Standards**: Blue text = inputs, Black = formulas, Green = cross-sheet links, Red = external links, Yellow background = key assumptions

---

### Enterprise & Communication

#### 15. brand-guidelines

- **Name**: `brand-guidelines`
- **Description**: Applies Anthropic's official brand colors and typography to any artifact. Use when brand colors, style guidelines, visual formatting, or company design standards apply.
- **Colors**: Dark (#141413), Light (#faf9f5), Mid Gray (#b0aea5), Light Gray (#e8e6dc), Orange (#d97757), Blue (#6a9bcc), Green (#788c5d)
- **Typography**: Headings = Poppins (Arial fallback), Body = Lora (Georgia fallback)
- **Features**: Smart font application (Poppins for 24pt+, Lora for body), automatic fallback, accent color cycling (orange, blue, green)

---

#### 16. doc-coauthoring

- **Name**: `doc-coauthoring`
- **Description**: Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals, technical specs, decision docs, or similar structured content.
- **3 Stages**:
  1. **Context Gathering**: User provides all relevant context while Claude asks clarifying questions. Supports info dumping, integration with Slack/Teams/Drive, and proactive gap identification.
  2. **Refinement & Structure**: Build document section by section through brainstorming (5-20 options), curation, drafting, and iterative refinement using str_replace edits.
  3. **Reader Testing**: Test document with fresh Claude instance (no context bleed) to catch blind spots. Predicts reader questions, tests with sub-agent, runs additional checks for ambiguity/contradictions.
- **Trigger Types**: PRD, design doc, decision doc, RFC, proposal, technical spec

---

#### 17. internal-comms

- **Name**: `internal-comms`
- **Description**: Resources to help write internal communications using company-preferred formats. Use for status reports, leadership updates, 3P updates, newsletters, FAQs, incident reports, project updates.
- **Communication Types**:
  - 3P updates (Progress, Plans, Problems)
  - Company newsletters
  - FAQ responses
  - Status reports
  - Leadership updates
  - Project updates
  - Incident reports
- **Process**: Identify communication type, load appropriate guideline from examples/ directory, follow specific formatting and tone instructions

---

## Skill Specification Summary

| # | Skill | Category | Trigger Keywords |
|---|-------|----------|-----------------|
| 1 | algorithmic-art | Creative & Design | generative art, p5.js, algorithmic, seeded art |
| 2 | canvas-design | Creative & Design | poster, art, design, static visual piece |
| 3 | frontend-design | Creative & Design | web components, pages, dashboards, React, HTML/CSS |
| 4 | slack-gif-creator | Creative & Design | animated GIF, Slack emoji, GIF for Slack |
| 5 | theme-factory | Creative & Design | theme, styling, color palette, fonts, branding |
| 6 | claude-api | Development | anthropic import, Claude API, SDK, Agent SDK |
| 7 | mcp-builder | Development | MCP server, Model Context Protocol, external API |
| 8 | web-artifacts-builder | Development | HTML artifact, React artifact, shadcn, complex artifact |
| 9 | webapp-testing | Development | test webapp, Playwright, browser testing, screenshot |
| 10 | skill-creator | Development | create skill, edit skill, skill eval, benchmark |
| 11 | docx | Document | Word doc, .docx, report, memo, letter, template |
| 12 | pdf | Document | PDF, .pdf, merge PDF, extract text, OCR |
| 13 | pptx | Document | slides, presentation, deck, .pptx |
| 14 | xlsx | Document | spreadsheet, .xlsx, .csv, Excel, formulas |
| 15 | brand-guidelines | Enterprise | brand colors, Anthropic styling, visual formatting |
| 16 | doc-coauthoring | Enterprise | write docs, draft proposal, technical spec, RFC |
| 17 | internal-comms | Enterprise | status report, 3P update, newsletter, FAQ, incident |
