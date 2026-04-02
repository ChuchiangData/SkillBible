# GEMINI.md 配置指南 (Google Gemini CLI)

> GEMINI.md 是 Google Gemini CLI 的项目级配置文件。
> 来源: [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) (Apache 2.0)

## 概述

Gemini CLI 在启动时读取 GEMINI.md 文件，获取项目上下文和指令。与 CLAUDE.md 和 AGENTS.md 类似。

## 文件位置

- `GEMINI.md` — 项目根目录
- 支持子目录中的 GEMINI.md

## 推荐结构

```markdown
# GEMINI.md

## Project
Name and description of the project.

## Tech Stack
Languages, frameworks, and tools used.

## Build & Test
- Build: `make build`
- Test: `make test`
- Lint: `make lint`

## Conventions
Coding style and architectural patterns.

## Important Notes
Critical context the agent should know.
```

## Gemini CLI 内置工具

Gemini CLI 提供以下内置工具：
- **Shell** — 执行终端命令
- **ReadFile** — 读取文件内容
- **WriteFile** — 写入文件
- **SearchFiles** — 搜索文件
- **WebFetch** — 获取网页内容
- **MCP** — 连接 MCP 服务器扩展功能

## 与其他 Agent 配置的对比

| Agent | 配置文件 | 开源 |
|-------|----------|------|
| Claude Code | CLAUDE.md | 否 |
| OpenAI Codex | AGENTS.md | 是 (Apache 2.0) |
| Gemini CLI | GEMINI.md | 是 (Apache 2.0) |
| Cursor | .cursor/rules/*.mdc | 否 |
| Windsurf | .windsurfrules | 否 |

---

> 来源: [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
