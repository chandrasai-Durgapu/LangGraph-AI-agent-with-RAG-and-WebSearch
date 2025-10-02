# 🤖 LangGraph AI Agent with RAG and Web Search

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An advanced AI agent system that combines **LangGraph**, **Retrieval-Augmented Generation (RAG)**, and **Web Search** to answer complex queries by retrieving relevant documents and fetching live web data. Designed to simulate decision-making workflows using stateful graph-based agents.

---

## 🌐 Overview

This project demonstrates how to use:

- **LangGraph** to model stateful agents with memory and branching logic.
- **RAG** for contextual knowledge retrieval using local documents.
- **Web search tools** to enrich answers with real-time information.

The result is a hybrid AI agent that performs reasoning, retrieval, and live querying in one cohesive workflow.

---

## ✨ Features

- 🔁 **Stateful Agent Architecture** using LangGraph (node-based workflow)
- 📚 **Document Retrieval** with embeddings + vector search
- 🌍 **Live Web Search Integration** (e.g., Tavily, Bing, Google, etc.)
- 💬 **Context-aware Memory** for multi-turn chat
- ⚙️ Easy to extend with new tools or nodes
- 🚀 Designed for experimentation, research, or production-grade agents

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.10+
- API key for your preferred web search service (Tavily, Serper, Bing, etc.)
- Optional: Streamlit or FastAPI for UI

---

### 🛠️ Installation

 **Clone the Repository**

```bash
git clone https://github.com/chandrasai-Durgapu/LangGraph-AI-agent-with-RAG-and-WebSearch.git
cd LangGraph-AI-agent-with-RAG-and-WebSearch
```
## Create and Activate Environment
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```
## Install Dependencies
```bash
pip install -r requirements.txt
```
---
## Edit .env to include:
```bash
TAVILY_API_KEY=your_key_here
```
---
# Running the Agent
```bash
python main.py
```
---
## How It Works
LangGraph Flow

The agent is modeled as a graph of nodes, where each node can:

Perform a tool action (RAG, search, etc.)

Decide next steps based on conditions

Use memory/state to influence the path

## Tools

RAG Retriever: Embeds documents and retrieves chunks relevant to a query.

Web Search Tool: Queries live web (via Tavily or other) for current information.

## Memory

Each interaction persists context, allowing multi-turn logic and conversation memory using LangGraph's state management system.





