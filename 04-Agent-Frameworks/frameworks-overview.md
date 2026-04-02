# Agent 框架概览

> 主流 AI Agent 框架对比和介绍。

---

## 框架对比表

| 框架 | Stars | 语言 | 许可证 | 特点 |
|------|-------|------|--------|------|
| [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | 167K+ | Python | MIT | 最早的自主 Agent，组件化架构 |
| [LangChain](https://github.com/langchain-ai/langchain) | 75K+ | Python/JS | MIT | 最大的 Agent 工程平台，丰富的工具集成 |
| [OpenHands](https://github.com/All-Hands-AI/OpenHands) | 61.4K+ | Python | MIT | 云编码 Agent，53% SWE-Bench 解决率 |
| [CrewAI](https://github.com/crewAIInc/crewAI) | 47.4K+ | Python | MIT | 多 Agent 角色协作框架 |
| [smolagents](https://github.com/huggingface/smolagents) | 26.3K+ | Python | Apache 2.0 | HuggingFace 极简 Agent (~1000行核心) |
| [DSPy](https://github.com/stanfordnlp/dspy) | 23K+ | Python | MIT | Stanford 的 LLM 编程框架 |
| [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | - | C#/Python/Java | MIT | 微软模型无关 Agent SDK |
| [AutoGen](https://github.com/microsoft/autogen) | - | Python/.NET | MIT | 微软多 Agent 对话框架 |
| [OpenAI Codex](https://github.com/openai/codex) | - | TypeScript | Apache 2.0 | OpenAI 官方编码 Agent |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | - | TypeScript | Apache 2.0 | Google 官方 Agent CLI |

## AutoGPT

**定位**: 最早也是最著名的自主 AI Agent 框架
- 自动任务分解和迭代规划
- 组件化架构（原插件系统已升级）
- Web 浏览、文件操作、代码执行
- GitHub: [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)

## CrewAI

**定位**: 角色扮演多 Agent 协作框架
- 每个 Agent 有角色、目标和背景故事
- Task 驱动的工作流
- 丰富的工具库：文件、Web、数据库、API
- 工具仓库: [crewAIInc/crewAI-tools](https://github.com/crewAIInc/crewAI-tools)

### CrewAI 内置工具
- FileReadTool, DirectoryReadTool
- SeleniumScrapingTool, WebsiteSearchTool
- PostgreSQLSearchTool, MySQLSearchTool
- MongoDBSearchTool, QdrantSearchTool
- SerperDevTool, EXASearchTool
- DALLETool, VisionTool
- CodeInterpreterTool

## LangChain

**定位**: 最全面的 Agent 工程平台
- 数百个第三方工具集成
- LangGraph 用于有状态的多步骤 Agent
- LangSmith 用于观测和评估
- LangChain Hub 提供共享 Prompt 模板

## Semantic Kernel

**定位**: 微软企业级 Agent SDK
- 支持 C#、Python、Java
- 插件体系 (Native Functions + Prompt Templates)
- OpenAPI 和 MCP 集成
- Azure AI Services 深度集成

## AutoGen

**定位**: 微软多 Agent 对话框架
- Agent 之间通过对话协作
- 支持人机协作 (Human-in-the-loop)
- 代码执行沙箱
- 正在合并进 Microsoft Agent Framework

## smolagents (HuggingFace)

**定位**: 极简主义 Agent 框架
- 核心代码仅约 1000 行
- Code-first Agent（Agent 通过写代码来使用工具）
- 原生支持 MCP 和 LangChain 工具
- 可使用任何 HuggingFace Hub 模型

## OpenHands

**定位**: 开源云编码 Agent（原 OpenDevin）
- Software Agent SDK
- 53% SWE-Bench 解决率
- 支持 Web 浏览、Shell、代码编辑
- GitHub Issue 自动解决

---

> 来源: 各框架官方 GitHub 仓库。数据截至 2026 年 4 月。
