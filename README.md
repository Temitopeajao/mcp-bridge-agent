# MCP Bridge Agent: Multi-Source Intelligence Orchestrator

A production-ready, local-first agentic system that bridges siloed organizational data using the **Model Context Protocol (MCP)**. Built at **Ex Machina Technologies**.

---

## 🚀 The Problem

Enterprise data is often trapped in inconsistent formats — SQL databases, PDF archives, and live API streams. Connecting an LLM to these sources traditionally required custom, brittle glue code for every new integration.

## 💡 The Solution

By leveraging **p-agent** as an orchestrator and **MCP** as the communication layer, this system treats data sources as plug-and-play modules. It uses **Gemma 2** (9B/27B) as a local reasoning engine, ensuring sensitive data never leaves the local environment.

---

## 🏗️ Core Architecture

| Component | Role |
|---|---|
| `p-agent` | Orchestrator — handles the execution loop and tool selection |
| `Gemma 2` (via Ollama) | Reasoning engine — processes queries and synthesizes multi-source data |
| MCP PostgreSQL Server | Structured data source |
| MCP Filesystem Server | Unstructured data source |

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **Agent Framework:** [p-agent](https://github.com/lastmile-ai/p-agent)
- **Local LLM:** Google Gemma 2 (Ollama)
- **Protocol:** Model Context Protocol (MCP)

---

## 📥 Quick Start

**1. Pull the model:**
```bash
ollama run gemma2
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Run the orchestrator:**
```bash
python main.py
```

---

## 📈 Enterprise Value

**🔒 Data Sovereignty**
100% local execution — suitable for privacy-compliant industries with no external data exposure.

**⚡ Scalability**
New data sources can be added by spinning up an MCP server. No changes needed to the agent logic.

**💰 Cost Efficiency**
Eliminates per-token billing for high-volume internal data analysis.

---

*Developed by **Temitope Ajao**, Founder of Ex Machina Technologies.*
