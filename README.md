<p align="center">
  <img src="assets/banner.png" alt="Skill Bible" width="600">
</p>

<h1 align="center">SkillBible 「永乐大典」</h1>

<p align="center">
  <strong>🚀 The Ultimate Collection of AI Agent Skills, System Prompts & Tools</strong><br>
  汇聚全网公开的 AI Agent 技能、系统提示、工具定义和框架资源。按类别/领域分类，方便检索和复用。本项目由上海珠江数据支持并发布。珠江数据是全球顶尖的拟真数据供应商，我们创造最优质的拟真数据及其解决方案，降低训练和数据获取的成本，支持客户项目长期稳定的技术部署和发展。
  
</p>

<p align="center">
  <a href="https://github.com/ChuchiangData/SkillBible"><img src="https://img.shields.io/github/stars/ChuchiangData/SkillBible?style=social" alt="GitHub stars"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
  <img src="https://img.shields.io/badge/skills-253%2B-brightgreen" alt="Skills count">
  <img src="https://img.shields.io/badge/domains-19-orange" alt="Domains">
</p>

---

## 📑 目录

| # | 分类 | 说明 |
|---|------|------|
| 📢 | [01 - System Prompts](#-01---system-prompts系统提示) | 30+ AI 产品系统提示 |
| 🛠️ | [02 - Agent Skills](#️-02---agent-skillsagent-技能) | Anthropic 官方 + 社区技能 |
| 📚 | [03 - Prompt Libraries](#-03---prompt-libraries提示词库) | 1,596 条分类提示词 |
| 🤖 | [04 - Agent Frameworks](#-04---agent-frameworksagent-框架) | 10 大框架对比 |
| 🔌 | [05 - MCP Servers](#-05---mcp-serversmcp-服务器) | 7,260+ MCP 服务器 |
| 🏪 | [06 - GPT Store](#-06---gpt-storegpt-商店) | GPT 提示 & Actions |
| ⚙️ | [07 - IDE Configs](#️-07---ide-configside-配置) | CLAUDE.md / AGENTS.md / Cursor |
| 🎯 | [08 - Domain Skills](#-08---domain-skills领域技能) | 19 个专业领域技能 |
| 📋 | [09 - Awesome Lists](#-09---awesome-lists资源列表) | 40+ Awesome Lists 索引 |
| 📖 | [10 - References](#-10---references引用来源) | 完整来源引用 |

---

## 📢 01 - System Prompts（系统提示）

> 30+ AI 产品的完整系统提示和工具定义。

```
01-System-Prompts/
├── 🤖 ChatGPT/              # OpenAI ChatGPT 系列
├── 🟣 Claude/               # Anthropic Claude & Claude Code
│   ├── claude-code.txt          # Claude Code 系统提示
│   ├── claude-code-2.0.txt      # Claude Code 2.0
│   ├── claude-sonnet-4.5.txt    # Claude Sonnet 4.5
│   └── claude-sonnet-4.6.txt    # Claude Sonnet 4.6
├── 💎 Gemini/               # Google Gemini & Gemini CLI
├── ⚡ Grok/                 # xAI Grok (官方开源 AGPL-3.0)
│   └── ...10 个官方提示文件
├── 🔷 Copilot/              # GitHub Copilot / VS Code Agent
├── 📐 Cursor/               # Cursor AI Editor
├── 🌊 Windsurf/             # Windsurf (Codeium)
├── 🧑‍💻 Devin/                # Devin AI (Cognition)
└── 📦 Others/               # 20+ 其他 AI 产品
    ├── perplexity.txt           # Perplexity AI
    ├── v0.txt                   # Vercel v0
    ├── lovable.txt              # Lovable
    ├── manus.txt                # Manus AI
    ├── bolt.txt                 # Bolt.new
    ├── cline.txt                # Cline
    ├── notion-ai.txt            # Notion AI
    ├── trae.txt                 # Trae (ByteDance)
    ├── kiro-vibe.txt            # Kiro (AWS)
    └── ...更多
```

**来源**: [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) ⭐130K+ · [xai-org/grok-prompts](https://github.com/xai-org/grok-prompts) (官方)

---

## 🛠️ 02 - Agent Skills（Agent 技能）

> 可复用的 Agent 技能定义，兼容 Claude Code、Codex、Gemini CLI、Cursor 等。

```
02-Agent-Skills/
├── 🟣 Claude-Code-Skills/   # Anthropic 官方 17 个 Skills
│   ├── algorithmic-art.md       # 🎨 算法艺术
│   ├── claude-api.md            # 🔗 Claude API
│   ├── docx.md                  # 📄 Word 文档
│   ├── pdf.md                   # 📕 PDF 处理
│   ├── pptx.md                  # 📊 PPT 处理
│   ├── xlsx.md                  # 📈 Excel 处理
│   ├── mcp-builder.md           # 🔌 MCP 构建
│   ├── skill-creator.md         # ✨ 技能创建器
│   ├── webapp-testing.md        # 🧪 Web 测试
│   └── ...更多
├── 📐 Cursor-Rules/
├── 🔷 Codex-Agents/
├── 💎 Gemini-CLI/
├── 🔒 Cybersecurity/
└── 🌐 General-Purpose/
```

**来源**: [anthropics/skills](https://github.com/anthropics/skills) (官方) · [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) 220+

---

## 📚 03 - Prompt Libraries（提示词库）

> 1,596 条提示词，自动按领域分类。

| 分类 | 数量 | 说明 |
|------|------|------|
| 🎭 Role-Play | 1,035 | 角色扮演提示 |
| 💻 Coding | 149 | 编程开发提示 |
| 🎨 Creative | 136 | 创意艺术提示 |
| 💼 Business | 83 | 商业管理提示 |
| ✍️ Writing | 71 | 写作创作提示 |
| 🔬 Research | 71 | 研究分析提示 |
| 🎓 Education | 51 | 教育培训提示 |

**来源**: [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) ⭐143K+ (CC0 1.0)

---

## 🤖 04 - Agent Frameworks（Agent 框架）

> 主流 Agent 框架对比和工具介绍。

| 框架 | Stars | 说明 |
|------|-------|------|
| 🦾 [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | 167K+ | 自主 AI Agent 先驱 |
| 🔗 [LangChain](https://github.com/langchain-ai/langchain) | 75K+ | 最全工具生态 |
| 🖐️ [OpenHands](https://github.com/All-Hands-AI/OpenHands) | 61K+ | 云编码 Agent |
| 🚢 [CrewAI](https://github.com/crewAIInc/crewAI) | 47K+ | 多 Agent 协作 |
| 🤗 [smolagents](https://github.com/huggingface/smolagents) | 26K+ | 极简 Agent |
| 🧠 [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | - | 微软企业级 SDK |
| 💬 [AutoGen](https://github.com/microsoft/autogen) | - | 微软多 Agent 对话 |

---

## 🔌 05 - MCP Servers（MCP 服务器）

> Model Context Protocol — AI Agent 的通用工具协议，7,260+ 服务器。

**来源**: [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) (MIT) · [wong2/awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers)

---

## 🏪 06 - GPT Store（GPT 商店）

> 自定义 GPT 提示和 GPT Actions 开发指南。

**来源**: [linexjlin/GPTs](https://github.com/linexjlin/GPTs) · [OpenAI Docs](https://platform.openai.com/docs/actions)

---

## ⚙️ 07 - IDE Configs（IDE 配置）

> 各 AI 编码助手的项目配置文件模板和指南。

| 配置文件 | 平台 | 说明 |
|----------|------|------|
| 🟣 `CLAUDE.md` | Claude Code | 项目上下文和指令 |
| 🟢 `AGENTS.md` | OpenAI Codex | Agent 行为定义 |
| 💎 `GEMINI.md` | Gemini CLI | Gemini 项目配置 |
| 📐 `.cursorrules` | Cursor | AI 编码规则 |

---

## 🎯 08 - Domain Skills（领域技能）

> **19 个专业领域**，融合自 10+ 个开源社区仓库的高质量 SKILL.md 技能文件。

### 💻 技术领域

| 领域 | 文件数 | 来源 | 说明 |
|------|--------|------|------|
| 🖥️ Frontend | 1 | 社区整理 | React, Vue, Next.js, CSS, a11y |
| ⚙️ Backend | 1 | 社区整理 | API, 微服务, 数据库, 缓存 |
| 📱 Mobile | 1 | 社区整理 | iOS, Android, React Native, Flutter |
| 🐳 DevOps | 1 | 社区整理 | Docker, K8s, CI/CD, Terraform, 监控 |
| 🔒 Security | 1 | 社区整理 | 渗透测试, DFIR, 云安全, DevSecOps |
| 🧪 QA & Testing | 9 | [fugazi/test-automation-skills-agents](https://github.com/fugazi/test-automation-skills-agents) | Playwright, Selenium, ISTQB, a11y |
| 🤖 AI/ML Research | 11 | [Orchestra-Research/AI-research-SKILLs](https://github.com/Orchestra-Research/AI-research-SKILLs) | LitGPT, Mamba, Axolotl, vLLM (MIT) |
| 🤖 Robotics | 11 | [arpitg1304/robotics-agent-skills](https://github.com/arpitg1304/robotics-agent-skills) | ROS1/2, 感知, Docker-ROS2 |
| ⛓️ Blockchain & Web3 | 1 | 社区整理 | Solidity, DeFi, ZK, NFT |

### 🔬 科学与研究

| 领域 | 文件数 | 来源 | 说明 |
|------|--------|------|------|
| 🧬 Scientific Research | 12 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | 生物信息学, 化学, 蛋白质工程 (MIT) |
| 📊 Data Science | 1 | 社区整理 | EDA, ML, SQL, NLP, A/B 测试 |
| 🎓 Education | 2 | [GarethManning/claude-education-skills](https://github.com/GarethManning/claude-education-skills) | 108 个循证教学法技能 |

### 💼 商业与专业

| 领域 | 文件数 | 来源 | 说明 |
|------|--------|------|------|
| 📣 Marketing & SEO | 16 | [kostja94/marketing-skills](https://github.com/kostja94/marketing-skills) | 160+ SEO, 广告, 内容, 分析 (MIT) |
| 📦 Product Management | 21 | [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills) | 47 技能, JTBD, RICE, Kano (CC BY-NC-SA) |
| ⚖️ Legal & Compliance | 21 | [lawvable/awesome-legal-skills](https://github.com/lawvable/awesome-legal-skills) | 合同, GDPR, NDA, 合规 (CC BY-NC-ND) |
| 💰 Finance | 15 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | C-suite 顾问, 财务分析, SaaS (MIT) |
| 📈 Sales & GTM | 16 | [gtmagents/gtm-agents](https://github.com/gtmagents/gtm-agents) | 92+ agents, 行业解决方案 (Apache 2.0) |
| 📋 Project Management | 10 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | Jira, Scrum, Confluence (MIT) |
| 🎨 Design | 1 | 社区整理 | UI/UX, 设计系统, 用户研究 |

---

## 📋 09 - Awesome Lists（资源列表）

> 40+ 个 AI Agent 领域最有价值的 Awesome Lists 索引。

---

## 📖 10 - References（引用来源）

> 完整来源列表、许可证信息和 Agent Skills (SKILL.md) 规范说明。

---

## 🌟 主要来源

| 来源 | 类型 | 许可证 |
|------|------|--------|
| [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | 🔑 30+ AI 工具系统提示 | - |
| [xai-org/grok-prompts](https://github.com/xai-org/grok-prompts) | ⚡ Grok 官方提示 | AGPL-3.0 |
| [anthropics/skills](https://github.com/anthropics/skills) | 🟣 Claude Code 官方技能 | Anthropic |
| [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) | 💬 1,596 条提示词 | CC0 1.0 |
| [kostja94/marketing-skills](https://github.com/kostja94/marketing-skills) | 📣 160+ 营销 SEO 技能 | MIT |
| [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | 🧬 136+ 科学研究技能 | MIT |
| [lawvable/awesome-legal-skills](https://github.com/lawvable/awesome-legal-skills) | ⚖️ 42+ 法律合规技能 | CC BY-NC-ND |
| [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills) | 📦 47 产品管理技能 | CC BY-NC-SA |
| [Orchestra-Research/AI-research-SKILLs](https://github.com/Orchestra-Research/AI-research-SKILLs) | 🤖 87 AI/ML 研究技能 | MIT |
| [gtmagents/gtm-agents](https://github.com/gtmagents/gtm-agents) | 📈 92+ 销售 GTM 技能 | Apache 2.0 |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | 🛠️ 220+ 多领域技能 | MIT |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | 🔌 MCP 官方服务器 | MIT |

完整来源列表见 [10-References/sources.md](10-References/sources.md)

---

## 🚀 快速使用

### 浏览和复用提示词
```bash
# 直接浏览目录，复制到你的 AI 工具中
cat 08-Domain-Skills/Marketing-SEO/analytics-seo-google-search-console.md
```

### 安装 Claude Code Skills
```bash
# 将 SKILL.md 文件复制到你的项目
mkdir -p .claude/skills/pdf
cp 02-Agent-Skills/Claude-Code-Skills/pdf.md .claude/skills/pdf/SKILL.md
```

### 配置 IDE Agent
```bash
# 参考模板配置你的 AI 编码助手
cat 07-IDE-Configs/CLAUDE-md/claude-md-guide.md
```

---

## 🤝 贡献

欢迎通过 Pull Request 贡献新的 Skills、Prompts 或来源！请确保：

1. ✅ 注明来源和许可证
2. ✅ 按现有目录结构分类
3. ✅ 使用 Markdown 格式
4. ✅ 确保内容质量（实际可用，不是水文）

---

## ⚠️ 声明

本项目仅用于学习和研究目的。所有内容版权归原作者所有。如有侵权请提交 Issue，我们将及时处理。

This project is for educational and research purposes only. All copyrights belong to the original authors. If you believe any content infringes your rights, please open an issue.

---

## 📜 License

MIT License — 本项目结构和原创内容。收录的第三方内容遵循其原始许可证。
