# Agentic AI Learning Path

> For builders who want to create **autonomous AI agents, multi-agent systems, and tool-using LLM applications**.

## Path Overview

Focus on reasoning loops, tool integration, memory, multi-agent orchestration, and safety.

## Prerequisites

- Comfortable with Python and async programming
- Familiarity with LLMs and prompt engineering (see [GenAI Engineer Track](./genai-engineer-track.md))

## Core Modules

| Step | Module | Key Resources | Goal |
|---|---|---|---|
| 1 | [Module 05 — GenAI (Agents Section)](../05-generative-ai/README.md) | ReAct, tool use, agent loops | Understand agent architecture |
| 2 | [Module 05 — GenAI (Multi-Agent)](../05-generative-ai/README.md) | LangGraph, AutoGen, CrewAI | Multi-agent orchestration |
| 3 | [Module 08 — Advanced Projects](../08-projects-and-examples/advanced/) | Build a multi-agent system | Hands-on implementation |

## Elective Modules

| Module | When to Take |
|---|---|
| [Module 04 — NLP](../05-generative-ai/README.md) | If needing stronger NLP foundations |
| [Module 06 — Advanced Topics](../06-agentic-ai/README.md) | RLHF, preference optimization |
| [Module 07 — MLOps](../07-mlops-and-deployment/) | Deploying agents in production |

## Projects

| Project | Module Connection | Skills |
|---|---|---|
| [Multi-Agent System with RAG](../08-projects-and-examples/advanced/#multi-agent-system-with-rag) | 05-GenAI | LangGraph, tool use, memory |
| [Personal AI Tutor](../08-projects-and-examples/end-to-end-systems/#personal-ai-tutor) | 05-GenAI, 08-Projects | Multi-agent + RAG + TTS |

## Key Frameworks & Tools

| Tool | Purpose |
|---|---|
| **LangGraph** | Build stateful, multi-actor agent applications |
| **AutoGen** | Multi-agent conversation framework (Microsoft) |
| **CrewAI** | Role-based agent orchestration |
| **Semantic Kernel** | AI orchestration for enterprise (Microsoft) |
| **Google ADK** | Agent Development Kit for Gemini agents |

## Agent Design Patterns

| Pattern | Description |
|---|---|
| **ReAct** | Reasoning + Acting loop (self-prompting) |
| **Plan-and-Execute** | Decompose task, then execute sub-steps |
| **Reflection** | Agent critiques its own output and iterates |
| **Tool Use** | LLM calls external APIs, databases, or code executors |
| **Memory** | Short-term (conversation history) and long-term (vector DB) |
| **Human-in-the-Loop** | Agent pauses and requests human input at critical decisions |

## Safety & Alignment

- **Guardrails** — prevent harmful or off-policy actions
- **Observability** — trace agent decisions and tool calls
- **Rate Limiting** — prevent runaway costs from infinite loops
- **Sandboxing** — isolate code execution environments

---

> **Last Reviewed:** 2026-06
