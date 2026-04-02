# CLAUDE.md 配置指南

> CLAUDE.md 是 Claude Code 的项目级配置文件，用于定义项目上下文、编码规范和 Agent 行为。

## 概述

CLAUDE.md 文件放置在项目根目录，Claude Code 在每次会话开始时自动读取。它是告诉 Claude Code 你的项目约定、技术栈和工作偏好的主要方式。

## 文件位置（优先级从高到低）

1. `CLAUDE.md` — 项目根目录（最常用）
2. `.claude/CLAUDE.md` — Claude 配置目录
3. `CLAUDE.local.md` — 本地覆盖（不提交到 Git）
4. `~/.claude/CLAUDE.md` — 全局配置（所有项目生效）

## 推荐结构

```markdown
# Project: MyApp

## Tech Stack
- Frontend: React 19 + TypeScript 5 + Tailwind CSS 4
- Backend: Python 3.12 + FastAPI
- Database: PostgreSQL 16 + Redis
- Testing: Vitest (frontend), Pytest (backend)

## Code Style
- Use functional components with hooks (no class components)
- Follow Google Python Style Guide
- Maximum line length: 100 characters
- Use absolute imports with @ alias

## Commands
- Build: `npm run build`
- Test: `npm test`
- Lint: `npm run lint`
- Type check: `npx tsc --noEmit`

## Architecture
- `/src/components` — Reusable UI components
- `/src/features` — Feature-specific modules
- `/src/lib` — Shared utilities and API client
- `/api` — FastAPI backend

## Rules
- Always run tests before suggesting a commit
- Use conventional commits (feat:, fix:, docs:, etc.)
- Never modify migration files — create new ones
- Keep PR scope small — one feature per PR

## Context
- We use Stripe for payments (API v2024-12)
- Auth is handled by Clerk
- CI runs on GitHub Actions
```

## 最佳实践

1. **保持简洁** — 只写 Claude 需要知道的信息
2. **包含命令** — 构建、测试、lint 命令让 Claude 能自动验证
3. **说明架构** — 帮助 Claude 理解代码组织方式
4. **定义规则** — 明确的约束比模糊的建议更有效
5. **版本控制** — 将 CLAUDE.md 提交到 Git，CLAUDE.local.md 放入 .gitignore

## 相关配置

| 平台 | 配置文件 |
|------|----------|
| Claude Code | `CLAUDE.md` |
| OpenAI Codex | `AGENTS.md` |
| Gemini CLI | `GEMINI.md` |
| Cursor | `.cursor/rules/*.mdc` |
| GitHub Copilot | `.github/copilot-instructions.md` |
| Windsurf | `.windsurfrules` |

---

> 来源: [Anthropic Claude Code 文档](https://docs.anthropic.com/en/docs/claude-code)
