# Multi-Agent Systems

> *Orchestrating multiple specialised agents that delegate, coordinate, and communicate.*

**Last Reviewed:** 2026-06

## Overview

A single agent has a bounded context window and limited tool surface. Multi-agent systems decompose complex workflows across **specialised sub-agents**, each with its own prompt, tools, memory, and sometimes model. A **supervisor** or **router** agent decides which sub-agent to invoke and how to merge results.

## Communication Topologies

| Topology | Description | Use Case |
|----------|-------------|----------|
| **Supervisor / Orchestrator** | Central agent delegates to workers | Code generation (PM → coder → reviewer) |
| **Peer-to-Peer (Debate)** | Agents exchange messages autonomously | Research synthesis, fact-checking |
| **Pipeline** | Sequential hand-off between agents | ETL pipelines, document processing |
| **Network / Mesh** | Agents discover and message each other dynamically | Simulation, game environments |
| **Shared Blackboard** | Agents read/write to a common state store | Multi-step analysis, planning |

## Key Patterns

### Supervisor Pattern

```
User → Supervisor
         ├── Researcher Agent (web search, summarise)
         ├── Coder Agent (write Python, run tests)
         └── Reviewer Agent (critique, suggest fixes)
         ↓
      Supervisor consolidates → Final response
```

### Delegation & Hand-off

- **Explicit delegation** — the supervisor names which agent should handle the next turn.
- **Tool-based hand-off** — agents expose a `transfer_to_<agent>` tool that the supervisor calls.
- **Broadcast / Gather** — the supervisor broadcasts a task, collects results, and synthesises.

## Resource Table

| Category | Title | Level | Link |
|----------|-------|-------|------|
| 📄 Paper | "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation" (Wu et al., 2023) | Advanced | https://arxiv.org/abs/2308.08155 |
| 📄 Paper | "Communicative Agents for Software Development" (Qian et al., 2023) — ChatDev | Advanced | https://arxiv.org/abs/2307.07924 |
| 📘 Docs | OpenAI — Agent Hand-off Patterns | Intermediate | https://platform.openai.com/docs/guides/agents#handoffs |
| 📘 Docs | LangGraph — Multi-Agent Supervisor | Intermediate | https://langchain-ai.github.io/langgraph/tutorials/multi_agent/agent_supervisor/ |
| 🎥 Video | "Multi-Agent Patterns in Production" (CrewAI) | Intermediate | https://www.youtube.com/watch?v=qHr6mHf0GmM |
| 💻 Code/Notebook | AutoGen Multi-Agent Example | Intermediate | https://github.com/microsoft/autogen/blob/main/notebooks/agentchat_multi_task_chat.ipynb |
| 🎓 Course | DeepLearning.AI — Multi AI Agent Systems with CrewAI | Beginner | https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/ |
| 📰 Blog | "Scaling Agentic Systems with Multi-Agent Orchestration" | Intermediate | https://www.anthropic.com/engineering/multi-agent-orchestration |

## Design Considerations

- **Context window management** — shared history across agents grows fast; consider summarisation or selective memory.
- **Naming & identity** — give agents clear personas so the model doesn't confuse roles.
- **Termination conditions** — define when the multi-agent loop ends (consensus, max turns, timeout).
- **Observability** — trace inter-agent messages; most failures happen at hand-off boundaries.
