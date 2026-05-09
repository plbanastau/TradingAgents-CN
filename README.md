# TradingAgents-CN 🤖📈

> 基于多智能体框架的中国股票市场交易分析系统

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Docker](https://img.shields.io/badge/Docker-支持-blue.svg)](https://www.docker.com/)

## 简介

TradingAgents-CN 是 [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) 的 Fork 版本，专注于中国 A 股市场的多智能体协作交易分析框架。系统通过多个专业 AI 智能体协同工作，对股票进行深度分析并生成交易建议。

> 📝 **个人备注**：本 Fork 主要用于学习和研究多智能体框架在 A 股市场的应用，重点关注 DeepSeek 模型的集成效果。

## 核心特性

- 🤖 **多智能体协作**：分析师、研究员、风控、交易员等多角色智能体协同决策
- 📊 **A股数据支持**：集成 AKShare、Tushare 等中国金融数据源
- 🧠 **多模型支持**：兼容 OpenAI、DeepSeek、Qwen、Ollama 等主流大模型
- 📰 **新闻情感分析**：实时抓取财经新闻并进行情感分析
- 🐳 **Docker 部署**：一键容器化部署，开箱即用
- 📈 **回测框架**：支持历史数据回测验证策略有效性

## 快速开始

### 环境要求

- Python 3.10+
- Docker & Docker Compose（可选）
- Redis（用于缓存，可选）

### 本地安装

```bash
# 克隆仓库
git clone https://github.com/your-username/TradingAgents-CN.git
cd TradingAgents-CN

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
# 编辑 .env 文件，填入必要的 API Key
```

### Docker 部署

```bash
# 复制 Docker 环境配置
cp .env.docker .env

# 启动服务
docker-compose up -d
```

## 配置说明

参考 `.env.example` 文件进行配置，主要配置项：

| 配置项 | 说明 | 必填 |
|--------|------|------|
| `OPENAI_API_KEY` | OpenAI API 密钥 | 可选 |
| `DEEPSEEK_API_KEY` | DeepSeek API 密钥 | 可选 |
| `DASHSCOPE_API_KEY` | 阿里云通义千问 API 密钥 | 可选 |
| `TUSHARE_TOKEN` | Tushare 数据接口 Token | 推荐 |
| `FINNHUB_API_KEY` | Finnhub 金融数据 API | 可选 |

> ⚠️ 至少需要配置一个大模型 API Key 才能正常运行

> 💡 **个人推荐**：优先使用 DeepSeek，性价比较高，对中文金融文本的理解效果也不错。

## 项目结构

```
TradingAgents-CN/
├── tradingagents/          # 核心框架代码
│   ├── agents/             # 各类智能体实现
│   ├── dataflows/          # 数据流处理模块
│   ├── graph/              # 智能体协作图
│   └── utils/              # 工具函数
├── cli/                    # 命令行界面
├── web/                    # Web 界面（开发中）
├── tests/                  # 测试用例
├── docs/                   # 文档
├── docker-compose.yml      # Docker 编排配置
├── .env.example            # 环境变量示例
└── requirements.txt        # Python 依赖
```

## 使用示例

```python
from tradingagents import TradingAgentsGraph

# 初始化交易分析框架
ta = TradingAgentsGraph()

# 分析股票
result = ta.analyze(
    ticker="600036",  # 招商银行
    date="2024-01-15"
)

print(result["recommendation"])  # 买入/持有/卖出
print(result["analysis"])        # 详细分析报告
```

> 💡 **个人测试记录**：用 `000858`（五粮液）和 `300750`（宁德时代）跑过几次，DeepSeek 的分析逻辑比较清晰，但新闻抓取偶尔会有延迟，建议分析前先确认数据源连通性。另外测试时建议将 `date` 参数设置为**前一个交易日**，避免当天数据不完整导致分析结果偏差。

## 贡献指南

欢迎提交 Issue 和 Pull Request！请先阅读 [贡献指南](CONTRIBUTING.md)。

## 问题反馈

- 🐛 Bug 报告：[GitHub Issues](../../issues/new?template=bug_report.md)
- 💡 功能建议：[GitHub Issues](../../issues/new?template=feature_request.md)
- 📖 文档问题：[GitHub Issues](../../issues/new?template=documentation.md)

## 许可证

本项目基于 [MIT License](LICENSE) 开源。

## 致谢

- 原项目：[hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN)
- 上游项目：[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)
