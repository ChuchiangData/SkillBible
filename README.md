# SkillBible 「永乐大典」

> **The Ultimate Collection of AI Agent Skills, System Prompts & Tools**
>
> 汇聚全网公开的 AI Agent 技能、系统提示、工具定义和框架资源。按类别/领域分类，方便检索和复用。

[![GitHub stars](https://img.shields.io/github/stars/ChuchiangData/SkillBible?style=social)](https://github.com/ChuchiangData/SkillBible)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

## 目录

- [01 - System Prompts（系统提示）](#01---system-prompts系统提示)
- [02 - Agent Skills（Agent 技能）](#02---agent-skillsagent-技能)
- [03 - Prompt Libraries（提示词库）](#03---prompt-libraries提示词库)
- [04 - Agent Frameworks（Agent 框架）](#04---agent-frameworksagent-框架)
- [05 - MCP Servers（MCP 服务器）](#05---mcp-serversmcp-服务器)
- [06 - GPT Store（GPT 商店）](#06---gpt-storegpt-商店)
- [07 - IDE Configs（IDE 配置）](#07---ide-configside-配置)
- [08 - Domain Skills（领域技能）](#08---domain-skills领域技能)
- [09 - Awesome Lists（资源列表）](#09---awesome-lists资源列表)
- [10 - References（引用来源）](#10---references引用来源)

---

## 01 - System Prompts（系统提示）

30+ AI 产品的完整系统提示和工具定义。

```
01-System-Prompts/
├── ChatGPT/              # OpenAI ChatGPT 系列
├── Claude/               # Anthropic Claude & Claude Code
│   ├── claude-code.txt          # Claude Code 系统提示
│   ├── claude-code-2.0.txt      # Claude Code 2.0
│   ├── claude-sonnet-4.5.txt    # Claude Sonnet 4.5
│   └── claude-sonnet-4.6.txt    # Claude Sonnet 4.6
├── Gemini/               # Google Gemini & Gemini CLI
│   ├── gemini-ai-studio.txt     # Gemini AI Studio
│   └── gemini-cli.txt           # Gemini CLI
├── Grok/                 # xAI Grok (官方开源 AGPL-3.0)
│   ├── grok4_system_turn_prompt_v8.j2
│   ├── grok4p1_thinking_system_turn_prompt_v2.j2
│   ├── grok3_official0330_p1.j2
│   └── ...10 个官方提示文件
├── Copilot/              # GitHub Copilot / VS Code Agent
├── Cursor/               # Cursor AI Editor
│   ├── cursor-agent-2.0.txt     # Cursor Agent 2.0
│   └── cursor-chat.txt          # Cursor Chat
├── Windsurf/             # Windsurf (Codeium)
│   └── windsurf-wave11.txt      # Wave 11
├── Devin/                # Devin AI (Cognition)
│   ├── devin-ai.txt
│   └── devin-deepwiki.txt
└── Others/               # 其他 AI 产品
    ├── perplexity.txt           # Perplexity AI
    ├── v0.txt                   # Vercel v0
    ├── lovable.txt              # Lovable
    ├── manus.txt                # Manus AI
    ├── replit.txt               # Replit
    ├── bolt.txt                 # Bolt.new
    ├── cline.txt                # Cline
    ├── notion-ai.txt            # Notion AI
    ├── cluely.txt               # Cluely
    ├── kiro-vibe.txt            # Kiro (AWS)
    ├── trae.txt                 # Trae (ByteDance)
    ├── augment-code.txt         # Augment Code
    ├── codex-cli.txt            # OpenAI Codex CLI
    ├── warp.txt                 # Warp.dev
    ├── xcode.txt                # Apple Xcode AI
    └── ...更多
```

**主要来源**: [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) (130K+ stars), [xai-org/grok-prompts](https://github.com/xai-org/grok-prompts) (官方)

---

## 02 - Agent Skills（Agent 技能）

可复用的 Agent 技能定义，兼容 Claude Code、Codex、Gemini CLI、Cursor 等。

```
02-Agent-Skills/
├── Claude-Code-Skills/   # Anthropic 官方 Skills (SKILL.md)
│   ├── algorithmic-art.md       # 算法艺术生成
│   ├── brand-guidelines.md      # 品牌指南
│   ├── canvas-design.md         # Canvas 设计
│   ├── claude-api.md            # Claude API 集成
│   ├── doc-coauthoring.md       # 文档协作
│   ├── docx.md                  # Word 文档处理
│   ├── frontend-design.md       # 前端设计
│   ├── internal-comms.md        # 内部通信
│   ├── mcp-builder.md           # MCP 服务器构建
│   ├── pdf.md                   # PDF 处理
│   ├── pptx.md                  # PPT 处理
│   ├── skill-creator.md         # 技能创建器（元技能）
│   ├── slack-gif-creator.md     # Slack GIF 创建
│   ├── theme-factory.md         # 主题工厂
│   ├── web-artifacts-builder.md # Web 工件构建
│   ├── webapp-testing.md        # Web 应用测试
│   └── xlsx.md                  # Excel 处理
├── Cursor-Rules/         # Cursor 规则
├── Codex-Agents/         # Codex Agent 配置
├── Gemini-CLI/           # Gemini CLI 配置
├── Cybersecurity/        # 网络安全技能
└── General-Purpose/      # 通用技能
```

**主要来源**: [anthropics/skills](https://github.com/anthropics/skills) (官方), [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)

---

## 03 - Prompt Libraries（提示词库）

1,596 条提示词，按领域分类。

```
03-Prompt-Libraries/
├── Role-Play/            # 角色扮演提示 (1,035 条)
├── Coding/               # 编程开发提示 (149 条)
├── Creative/             # 创意艺术提示 (136 条)
├── Business/             # 商业管理提示 (83 条)
├── Writing/              # 写作创作提示 (71 条)
├── Research/             # 研究分析提示 (71 条)
├── Education/            # 教育培训提示 (51 条)
└── awesome-chatgpt-prompts.csv  # 原始数据
```

**来源**: [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) (143K+ stars, CC0 1.0)

---

## 04 - Agent Frameworks（Agent 框架）

主流 Agent 框架对比和工具介绍。

```
04-Agent-Frameworks/
├── frameworks-overview.md  # 框架综合对比
├── AutoGPT/              # AutoGPT (167K stars, MIT)
├── CrewAI/               # CrewAI 多 Agent 协作 (47K stars, MIT)
├── LangChain/            # LangChain 工程平台 (75K stars, MIT)
├── Semantic-Kernel/      # 微软 SK (MIT)
├── AutoGen/              # 微软 AutoGen (MIT)
├── SmoLAgents/           # HuggingFace 极简 Agent (Apache 2.0)
├── OpenHands/            # OpenHands 编码 Agent (61K stars, MIT)
└── SWE-Agent/            # Princeton SWE-agent (MIT)
```

---

## 05 - MCP Servers（MCP 服务器）

Model Context Protocol 服务器资源，AI Agent 的通用工具协议。

```
05-MCP-Servers/
├── Official/
│   └── mcp-official-servers.md  # 官方参考实现 (MIT)
└── Community/
    └── awesome-mcp-servers.md   # 社区服务器列表 (7,260+ 服务器)
```

**来源**: [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers), [wong2/awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers)

---

## 06 - GPT Store（GPT 商店）

自定义 GPT 提示和 GPT Actions 指南。

```
06-GPT-Store/
├── Top-GPTs/
│   └── gpts-leaked-prompts.md   # 热门 GPT 提示索引
└── GPT-Actions/
    └── gpt-actions-guide.md     # GPT Actions 开发指南
```

**来源**: [linexjlin/GPTs](https://github.com/linexjlin/GPTs), [OpenAI Docs](https://platform.openai.com/docs/actions)

---

## 07 - IDE Configs（IDE 配置）

各 AI 编码助手的项目配置文件指南。

```
07-IDE-Configs/
├── CLAUDE-md/
│   └── claude-md-guide.md       # CLAUDE.md 配置指南
├── AGENTS-md/
│   └── agents-md-guide.md       # AGENTS.md (OpenAI Codex) 指南
├── GEMINI-md/
│   └── gemini-md-guide.md       # GEMINI.md (Gemini CLI) 指南
└── Cursor-Rules/
    └── awesome-cursorrules.md   # Cursor Rules 合集
```

---

## 08 - Domain Skills（领域技能）

按专业领域分类的高质量 Agent 提示词，每个领域 6-10 个精选提示。

```
08-Domain-Skills/
├── Data-Science/         # 数据科学 (EDA、ML、SQL、NLP)
├── DevOps/               # DevOps/SRE (Docker、K8s、CI/CD、Terraform)
├── Frontend/             # 前端开发 (React、Vue、Next.js、CSS)
├── Backend/              # 后端开发 (API、微服务、数据库、缓存)
├── Mobile/               # 移动开发 (iOS、Android、React Native、Flutter)
├── Security/             # 网络安全 (渗透测试、DFIR、云安全)
└── Design/               # 设计 (UI/UX、设计系统、用户研究)
```

---

## 09 - Awesome Lists（资源列表）

AI Agent 领域所有重要 Awesome Lists 的索引。

```
09-Awesome-Lists/
└── awesome-lists-index.md  # 40+ Awesome Lists 汇总索引
```

---

## 10 - References（引用来源）

```
10-References/
├── sources.md              # 完整来源和许可证信息
└── agent-skills-spec.md    # Agent Skills (SKILL.md) 规范说明
```

---

## 主要来源一览

| 来源 | 类型 | 许可证 |
|------|------|--------|
| [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | 30+ AI 工具系统提示 | - |
| [xai-org/grok-prompts](https://github.com/xai-org/grok-prompts) | Grok 官方提示 | AGPL-3.0 |
| [anthropics/skills](https://github.com/anthropics/skills) | Claude Code 官方技能 | Anthropic |
| [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) | 1,596 条提示词 | CC0 1.0 |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | MCP 官方服务器 | MIT |
| [openai/codex](https://github.com/openai/codex) | OpenAI Codex Agent | Apache 2.0 |
| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | Gemini CLI Agent | Apache 2.0 |
| [PatrickJS/awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) | Cursor 规则合集 | - |
| [linexjlin/GPTs](https://github.com/linexjlin/GPTs) | GPT Store 提示 | - |

完整来源列表见 [10-References/sources.md](10-References/sources.md)

---

## 使用方式

### 浏览和复用提示词
直接浏览对应目录下的 Markdown 文件，复制到你的 AI 工具中使用。

### 安装 Claude Code Skills
```bash
# 将 SKILL.md 文件复制到你的项目
cp -r 02-Agent-Skills/Claude-Code-Skills/pdf.md .claude/skills/pdf/SKILL.md
```

### 配置 IDE Agent
参考 `07-IDE-Configs/` 中的指南配置你的 CLAUDE.md、AGENTS.md 或 Cursor Rules。

---

## 贡献

欢迎通过 Pull Request 贡献新的 Skills、Prompts 或来源！请确保：

1. 注明来源和许可证
2. 按现有目录结构分类
3. 使用 Markdown 格式

---

## 声明

本项目仅用于学习和研究目的。所有内容版权归原作者所有。如有侵权请提交 Issue，我们将及时处理。

This project is for educational and research purposes only. All copyrights belong to the original authors. If you believe any content infringes your rights, please open an issue.

---

## License

MIT License - 本项目结构和原创内容。收录的第三方内容遵循其原始许可证。
