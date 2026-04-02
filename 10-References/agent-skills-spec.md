# Agent Skills 规范 (SKILL.md Specification)

> 来源: [agentskills.io](https://agentskills.io/specification) / [agentskills/agentskills](https://github.com/agentskills/agentskills)

## 概述

Agent Skills 是一种开放标准，定义了 AI Agent 可复用技能的文件格式。起源于 Anthropic Claude Code 的 SKILL.md，现已被 OpenAI Codex、GitHub Copilot、Cursor、Gemini CLI 等多个平台采用。

## SKILL.md 文件结构

一个 Skill 就是一个包含 `SKILL.md` 文件的文件夹：

```
my-skill/
├── SKILL.md          # 必需 - 技能定义和指令
├── scripts/          # 可选 - 辅助脚本
├── templates/        # 可选 - 模板文件
├── reference/        # 可选 - 参考文档
└── examples/         # 可选 - 示例文件
```

## SKILL.md 格式

```markdown
---
name: My Skill Name
description: 一句话描述技能用途
version: 1.0.0
triggers:
  - "关键词或条件"
  - "触发此技能的场景"
---

# 技能标题

## 概述
技能的详细说明。

## 指令
Agent 应该遵循的具体步骤。

## 规则
- 必须遵守的约束条件
- 质量标准

## 示例
输入输出示例。
```

## 关键字段

| 字段 | 必需 | 说明 |
|------|------|------|
| `name` | 是 | 技能名称 |
| `description` | 是 | 一行描述，用于匹配和检索 |
| `version` | 否 | 语义化版本号 |
| `triggers` | 否 | 触发条件列表 |

## 兼容平台

- **Claude Code** - 原生支持，放入 `.claude/skills/` 目录
- **OpenAI Codex** - 通过 AGENTS.md 兼容
- **GitHub Copilot** - 通过 .github/copilot-instructions.md 兼容
- **Cursor** - 通过 .cursor/rules/ 兼容
- **Gemini CLI** - 通过 GEMINI.md 兼容
- **Windsurf** - 通过 .windsurfrules 兼容

## 最佳实践

1. **单一职责** - 每个 Skill 只做一件事
2. **自包含** - 包含所有必要的脚本和模板
3. **明确触发条件** - 让 Agent 知道何时使用
4. **提供示例** - 帮助 Agent 理解预期输出
5. **版本管理** - 使用语义化版本号
