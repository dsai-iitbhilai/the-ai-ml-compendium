# Multi-Agent Systems

> Orchestrating multiple specialised agents that delegate, coordinate, and communicate. This file covers communication topologies (Supervisor, Peer-to-Peer, Mesh), delegation patterns, and multi-agent frameworks (AutoGen, CrewAI, LangGraph, Swarm).

**Last Reviewed:** 2026-06

**Prerequisites:** [Agent Fundamentals](agent-fundamentals.md) · [Tool Use & Function Calling](../../docs/06-agentic-ai/fundamentals/tool-use-and-function-calling.md)

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| *OpenAI — Agent Hand-off Patterns* | Intermediate | <https://platform.openai.com/docs/guides/agents#handoffs> | Best practices for stateless hand-offs and transferring execution context between agents. |
| *LangGraph — Multi-Agent Supervisor* | Intermediate | <https://langchain-ai.github.io/langgraph/tutorials/multi_agent/agent_supervisor/> | Building a stateful graph where a supervisor dynamically routes tasks to worker nodes. |
| *CrewAI Core Documentation* | Beginner | <https://docs.crewai.com/> | Framework focused on role-playing agents, sequential processes, and hierarchical task delegation. |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| *Multi-Agent Patterns in Production* (CrewAI) | Intermediate | <https://www.youtube.com/watch?v=qHr6mHf0GmM> | Real-world engineering breakdown of deploying multi-agent systems and handling edge cases. |
| *Building Multi-Agent Workflows with LangGraph* | Advanced | <https://www.youtube.com/watch?v=x-PXYu2vM-U> | Deep dive into cyclic graphs, persistence, and human-in-the-loop multi-agent design. |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| *DeepLearning.AI — Multi AI Agent Systems with CrewAI* | Beginner | <https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/> | Hands-on introduction to assigning roles, goals, and tools to collaborative agents. |
| *DeepLearning.AI — AI Agentic Design Patterns with AutoGen* | Advanced | <https://www.deeplearning.ai/short-courses/ai-agentic-design-patterns-with-autogen/> | Focuses on multi-agent conversational frameworks, state transitions, and task delegation. |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| *LangSmith Trace Dashboard* | Intermediate | <https://smith.langchain.com/> | Essential for observing complex multi-agent interactions, spotting infinite loops, and tracking token burn per agent. |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *AutoGen: Enabling Next-Gen LLM Applications* (Wu et al., 2023) | Advanced | <https://arxiv.org/abs/2308.08155> | Introduces a generalized framework for multi-agent conversation programming. |
| *Communicative Agents for Software Development (ChatDev)* (Qian et al., 2023) | Advanced | <https://arxiv.org/abs/2307.07924> | Virtual software company powered by agents mimicking CEOs, CTOs, and programmers. |
| *MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework* (Hong et al., 2023) | Advanced | <https://arxiv.org/abs/2308.00352> | Enforces Standard Operating Procedures (SOPs) on agents to reduce hallucination in complex tasks. |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| *OpenAI Swarm Repository* | Intermediate | <https://github.com/openai/swarm> | Lightweight, educational framework demonstrating ergonomic, stateless multi-agent handoffs. |
| *AutoGen Multi-Agent Example* | Intermediate | <https://github.com/microsoft/autogen/blob/main/notebooks/agentchat_multi_task_chat.ipynb> | Jupyter notebook demonstrating how to set up group chats and proxy agents. |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *Scaling Agentic Systems with Multi-Agent Orchestration* | Intermediate | <https://www.anthropic.com/engineering/multi-agent-orchestration> | Real-world architectural strategies from Anthropic on scaling multi-agent deployment. |

---

## Communication Topologies

| Topology | Description | Use Case |
|----------|-------------|----------|
| **Supervisor / Orchestrator** | Central agent delegates to specialized workers. | Code generation (PM → Coder → Reviewer). |
| **Peer-to-Peer (Debate)** | Agents exchange messages autonomously without a central boss. | Research synthesis, peer fact-checking, adversarial generation. |
| **Pipeline (Sequential)** | Sequential hand-off between agents, functioning like an assembly line. | ETL pipelines, extensive document processing. |
| **Network / Mesh** | Agents discover and message each other dynamically based on state. | Complex simulations, generative game environments. |
| **Shared Blackboard** | Agents read/write to a common state store (memory bank) rather than passing messages. | Multi-step analysis, complex long-term planning. |

---

## Key Patterns

### Supervisor Pattern
```text
User Input → Supervisor Agent
                 │
                 ├── Researcher Agent (web search, summarize)
                 ├── Coder Agent (write Python, run tests)
                 └── Reviewer Agent (critique, suggest fixes)
                 │
           Supervisor consolidates → Final response to User
```

### Delegation & Hand-off
- **Explicit Delegation:** The supervisor strictly dictates which agent handles the next conversational turn.
- **Tool-Based Hand-off:** Agents expose a `transfer_to_<agent>` tool that returns a specific control string, shifting the execution context to a peer.
- **Broadcast / Gather:** The supervisor broadcasts a task to all workers, asynchronously collects the results, and synthesises them into a unified output.

---

## Design Considerations (Checklist)

- [ ] **Context Window Management:** Shared history across agents grows exponentially. Implement summarization, semantic routing, or selective memory to prevent context limit exhaustion.
- [ ] **Naming & Identity:** Give agents distinct, rigid personas and clear operational constraints so the LLM does not confuse roles (e.g., Coder vs. Reviewer).
- [ ] **State Transition Logic:** Formulate the mathematical constraints for state transitions in graph-based orchestrators (e.g., defining conditions where transition probability $P(s_{t+1}|s_t, a_t)$ forces a loop break).
- [ ] **Observability:** Trace inter-agent messages religiously. The vast majority of system failures, infinite loops, and hallucinations occur at hand-off boundaries.

---

## Projects / Practice

| Project | Description |
|---|---|
| **Multi-Agent Distributed Scraper** | Build a scalable web-scraping cluster using `Selenium` and `BeautifulSoup` driven by a `LangGraph` supervisor. The supervisor delegates target URLs to dynamic worker agents that execute JavaScript extraction, followed by a validator agent that mathematically scores data completeness before writing to a database. |
| **End-to-End MLOps Code Factory** | Implement a fully autonomous software team using `MetaGPT`. Integrate the agents with a CI/CD pipeline via GitHub Actions. The agents must collaborate to write a machine learning script utilizing `Pandas` and `Scikit-learn`, deploy it into a containerized test environment, and mathematically debug any failing test outputs autonomously. |
| **Stateless Handoff Mathematics** | Create a from-scratch Python implementation of the `OpenAI Swarm` pattern. Define the handoff between agents as a Markov Decision Process (MDP) and write detailed mathematical documentation explaining how context variables are preserved across transitions without shared memory. |

---

## See also

- [Agent Fundamentals](agent-fundamentals.md) — Core mechanics of the ReAct loop powering the individual agents.
- [Tool Use & Function Calling](../../docs/06-agentic-ai/fundamentals/tool-use-and-function-calling.md) — The underlying mechanism enabling tool-based handoffs and delegation.
- [MLOps](../../visualizers-and-playgrounds/README.md) — Scalable engineering practices for deploying heavily orchestrated LLM systems in production.