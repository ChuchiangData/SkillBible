# AGENTS.md 配置指南 (OpenAI Codex)

> AGENTS.md 是 OpenAI Codex CLI 的项目级配置文件，用于定义 Agent 行为、项目上下文和编码规范。
> 来源: [openai/codex](https://github.com/openai/codex) (Apache 2.0)

## 概述

AGENTS.md 文件是 Codex CLI 在开始工作前自动读取的指令文件。它的设计受 CLAUDE.md 启发，但有自己的格式约定。

## 文件位置

- `AGENTS.md` — 项目根目录
- 子目录中的 `AGENTS.md` 仅在该目录的代码被修改时生效

## 推荐结构

```markdown
# AGENTS.md

## Overview
Brief project description and purpose.

## Setup
Commands to build and run the project:
- Install: `npm install`
- Build: `npm run build`
- Test: `npm test`

## Code Style
- Use TypeScript strict mode
- Prefer async/await over callbacks
- Use ESM imports

## Architecture Notes
Key architectural decisions and patterns.

## Testing
- Run `npm test` after any code change
- Test files go next to source files with .test.ts suffix
```

## 与 CLAUDE.md 的区别

| 特性 | AGENTS.md (Codex) | CLAUDE.md (Claude Code) |
|------|-------------------|-------------------------|
| 子目录支持 | 是（按目录生效） | 是 |
| 本地覆盖 | 无 | CLAUDE.local.md |
| 全局配置 | 无 | ~/.claude/CLAUDE.md |
| 格式 | Markdown | Markdown |

---

> 来源: [openai/codex](https://github.com/openai/codex)
