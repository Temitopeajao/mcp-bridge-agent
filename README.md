```markdown
# MCP Bridge Agent: Multi-Source Intelligence Orchestrator

This repository implements a production-ready, local-first agentic system designed to bridge the gap between siloed organizational data. Built at **Ex Machina Technologies**, this project demonstrates how to use the **Model Context Protocol (MCP)** to provide an LLM with secure, standardized access to disparate data sources.

## 🚀 The Problem
Enterprise data is often trapped in inconsistent formats—SQL databases, PDF archives, and API streams. Traditionally, connecting an LLM to these sources required custom, brittle "glue code" for every new integration.

## 💡 The Solution
By leveraging **p-agent** as an orchestrator and **MCP** as the communication layer, this system treats data sources as plug-and-play modules. It uses **Gemma 2** (9B/27B) as a local reasoning engine to ensure that sensitive data never leaves the local environment.

### Core Architecture
* **Orchestrator:** `p-agent` handles the execution loop and tool selection.
* **Reasoning Engine:** `Gemma 2` (via Ollama) processes queries and synthesizes multi-source data.
* **Standardized Tools:** MCP Clients connect to a PostgreSQL server (Structured) and a Filesystem server (Unstructured).

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Agent Framework:** [p-agent](https://github.com/lastmile-ai/p-agent)
* **Local LLM:** Google Gemma 2 (Ollama)
* **Protocol:** Model Context Protocol (MCP)

## 📥 Quick Start
1. **Pull the Model:** `ollama run gemma2`
2. **Install Dependencies:** `pip install -r requirements.txt`
3. **Run the Orchestrator:**
```bash
python main.py
