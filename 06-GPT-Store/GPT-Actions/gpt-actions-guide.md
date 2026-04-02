# GPT Actions 指南

> GPT Actions 允许自定义 GPT 通过 RESTful API 调用外部服务。
> 来源: [OpenAI 官方文档](https://platform.openai.com/docs/actions)

## 概述

GPT Actions 使用 OpenAPI 3.x 规范定义 API Schema，让 ChatGPT 的自定义 GPT 能够调用外部 API。这是扩展 GPT 能力的官方方式。

## 基本结构

```yaml
openapi: 3.1.0
info:
  title: My API
  version: 1.0.0
servers:
  - url: https://api.example.com
paths:
  /search:
    get:
      operationId: searchItems
      summary: Search for items
      parameters:
        - name: query
          in: query
          required: true
          schema:
            type: string
          description: The search query
      responses:
        '200':
          description: Search results
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: string
                    title:
                      type: string
```

## 认证方式

1. **无认证** — 公开 API
2. **API Key** — 通过 Header 或 Query 参数
3. **OAuth 2.0** — 用户授权流程

## 常见 Actions 示例

| 用途 | API | 说明 |
|------|-----|------|
| 搜索 | Serper/Tavily | Web 搜索集成 |
| 代码 | GitHub API | 仓库操作 |
| 邮件 | Gmail API | 发送和读取邮件 |
| 日历 | Google Calendar | 日程管理 |
| 数据库 | Supabase | 数据 CRUD |
| 文件 | Google Drive | 文件管理 |
| 通知 | Slack | 发送消息 |

## 最佳实践

1. **描述清晰** — operationId 和 summary 要让 GPT 理解何时调用
2. **参数详尽** — 每个参数都写 description
3. **响应明确** — 定义完整的 response schema
4. **错误处理** — 包含常见错误响应
5. **最小权限** — 只暴露必要的 API 端点

## 与 MCP 的区别

| 特性 | GPT Actions | MCP |
|------|------------|-----|
| 协议 | REST/OpenAPI | JSON-RPC |
| 平台 | 仅 ChatGPT | 跨平台 |
| 认证 | OAuth/API Key | 按服务器实现 |
| 发现 | GPT Store | 手动配置 |
| 实时 | 否 | 支持 SSE |

---

> 来源: [OpenAI Platform Docs](https://platform.openai.com/docs/actions)
> 社区资源: [agisota/gpt-actions](https://github.com/agisota/gpt-actions)
