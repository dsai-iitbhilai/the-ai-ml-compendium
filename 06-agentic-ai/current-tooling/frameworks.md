# Agent Frameworks

> A point-in-time survey of the most widely used agentic orchestration frameworks. This file compares their state-machine topologies, persistence layers, and production readiness.

**Last Reviewed:** 2026-06

**Prerequisites:** [Agent Fundamentals](../../docs/06-agentic-ai/fundamentals/agent-fundamentals.md) · [Multi-Agent Systems](../../docs/06-agentic-ai/fundamentals/multi-agent-systems.md)

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| *LangGraph Documentation* | Intermediate | <https://langchain-ai.github.io/langgraph/> | Official guide to building stateful, cyclic graphs for production orchestration. |
| *CrewAI Documentation* | Beginner | <https://docs.crewai.com/> | Framework focused on role-playing agents, sequential processes, and hierarchical task delegation. |
| *AutoGen Documentation* | Intermediate | <https://microsoft.github.io/autogen/0.2/> | Microsoft's framework for multi-agent conversational patterns and custom topologies. |
| *Claude Agent SDK (Anthropic)* | Beginner | <https://docs.anthropic.com/en/docs/build-with-claude/tool-use> | Best practices for building ReAct loops tightly integrated with Claude's XML/tool protocols. |
| *OpenAI Swarm (GitHub)* | Intermediate | <https://github.com/openai/swarm> | Lightweight, educational framework demonstrating ergonomic, stateless multi-agent handoffs. |
| *Semantic Kernel (Microsoft)* | Advanced | <https://learn.microsoft.com/en-us/semantic-kernel/> | Enterprise-grade SDK integrating LLMs with existing C#/Python codebases using "plugins". |
| *DSPy Documentation* | Advanced | <https://dspy-docs.vercel.app/> | Framework treating prompts as hyperparameters, moving away from string hacking to compiled modules. |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| *LangGraph in Production* | Intermediate | <https://www.youtube.com/watch?v=JqG1U1iSs6w> | Breakdown of deploying LangGraph flows, handling persistence, and managing state across sessions. |
| *CrewAI Full Course* | Beginner | <https://www.youtube.com/watch?v=tjem-i8Xw-E> | Crash course on building AI crews for research, writing, and financial analysis. |
| *Intro to DSPy (Stanford NLP)* | Advanced | <https://www.youtube.com/watch?v=41EfOY0Ldkc> | Explains the mathematical intuition behind replacing manual prompt engineering with compiled signatures. |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| *DeepLearning.AI — AI Agents in LangGraph* | Beginner | <https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/> | Hands-on introduction to building cyclic workflows and state machines. |
| *DeepLearning.AI — Multi AI Agent Systems with CrewAI* | Beginner | <https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/> | Hands-on introduction to assigning roles, goals, and tools to collaborative agents. |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| *LangGraph Studio* | Intermediate | <https://langchain-ai.github.io/langgraph/how-tos/langgraph-studio/> | Local visual IDE for debugging, tracing, and modifying LangGraph state machines in real-time. |
| *AgentOps Dashboard* | Advanced | <https://www.agentops.ai/> | Production observability platform tailored for tracking multi-agent framework metrics (CrewAI, AutoGen). |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| *LangGraph Quick Start* | Beginner | <https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/introduction.ipynb> | Jupyter notebook demonstrating how to set up basic nodes, edges, and state. |
| *AutoGen Multi-Agent Example* | Intermediate | <https://github.com/microsoft/autogen/blob/main/notebooks/agentchat_multi_task_chat.ipynb> | Jupyter notebook demonstrating how to set up group chats and proxy agents. |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *Evaluating LLM Agent Frameworks* | Intermediate | <https://towardsdatascience.com/evaluating-llm-agent-frameworks-autogen-crewai-langgraph-c86720d20914> | Detailed architectural comparison of AutoGen vs. CrewAI vs. LangGraph. |
| *DSPy: Programming over Prompting* | Advanced | <https://towardsdatascience.com/intro-to-dspy-goodbye-prompting-hello-programming-4ca1c6ce3eb9> | Argues for the necessity of programmatic prompt compilation in complex agentic pipelines. |

---

## Framework Comparison

| Framework | Maintainer | Graph Model | Memory Persistence | Multi-Agent | Key Strength |
|-----------|-----------|-------------|--------------------|-------------|----------------|
| **LangGraph** | LangChain | Stateful graph (nodes + edges) | Built-in (checkpointing) | Yes | Granular control, production tracing, Human-in-the-loop (HITL) |
| **CrewAI** | CrewAI | Role-based sequential/hierarchical | Via callbacks / DB | Yes | Simple role abstraction, highly accessible API |
| **AutoGen** | Microsoft | Agent chat (conversable agents) | Extensible | Yes | Research breadth, highly customizable multi-agent protocols |
| **Semantic Kernel**| Microsoft | Imperative Plugin Architecture | Extensible | Native (V1.0+) | Enterprise integration (C# / Java), strong Azure ties |
| **Claude Agent SDK**| Anthropic | Loop with tool-use + hand-off | Automatic (context) | Via hand-off | Ergonomic API directly mirroring Anthropic's XML standards |
| **Swarm** | OpenAI | Lightweight hand-off graph | Minimal (stateless) | Yes | Educational, minimal abstraction, extremely easy to fork |
| **DSPy** | Stanford NLP | Compiled Neural Pipelines | Custom Modules | Yes | Replaces manual prompt engineering with mathematically optimized signatures |

---

## When to Use What

- **LangGraph:** You need production pipelines, complex branching logic (loops), state persistence across days, and fine-grained observability via LangSmith.
- **CrewAI:** You want to rapidly prototype a multi-agent team (e.g., Researcher + Writer + Editor) with minimal boilerplate. Excellent for sequential tasks.
- **AutoGen:** You are building research experiments, complex multi-agent conversation patterns, or custom agent debate topologies.
- **Semantic Kernel:** You are an enterprise shop writing in C# or Java, heavily invested in the Azure ecosystem, and need to bind LLMs to existing enterprise APIs.
- **Claude Agent SDK:** You are building an agent strictly for Claude models and want to utilize their native XML blocks and tool-use mechanics perfectly.
- **Swarm:** You want to learn the mathematics of agent hand-offs without navigating the bloat of a massive library. Not recommended for production.
- **DSPy:** You are dealing with highly complex, metric-driven pipelines (e.g., Multi-hop RAG) where manual prompt tuning is failing.

---

## Key Features to Evaluate (Checklist)

- [ ] **State Persistence:** Can the framework's state machine serialize to a database (Postgres/Redis) allowing the agent to survive a crash or run over multiple days?
- [ ] **Human-in-the-Loop (HITL):** Does the framework support explicitly pausing execution at a node boundary to await human approval (crucial for executing database writes or sending emails)?
- [ ] **Streaming Execution:** Does the runtime support parsing and streaming partial tool-call JSON tokens to the UI before the LLM finishes generating the arguments?
- [ ] **Observability:** Does it natively support tracing platforms like LangSmith, AgentOps, or custom OpenTelemetry implementations?
- [ ] **Model Agnosticism:** Does the framework tightly couple you to OpenAI, or can you effortlessly swap the engine to an open-source model running on vLLM?

---

## Framework Lifecycle Considerations

- **Vendor Lock-in:** LangGraph nudges you heavily towards the LangChain ecosystem; AutoGen and Semantic Kernel heavily favor Azure/OpenAI.
- **Maintenance Velocity:** Swarm is purely experimental; LangGraph, AutoGen, and CrewAI have extremely active release cycles.
- **Abstraction Leaks:** The more "magic" a framework handles (like CrewAI), the harder it is to debug when an LLM inevitably gets stuck in an infinite loop or hallucinates a tool argument.

---

## See also

- [Agent Fundamentals](../../docs/06-agentic-ai/fundamentals/agent-fundamentals.md) — Core mechanics of the ReAct loop powering these frameworks.
- [Multi-Agent Systems](../../docs/06-agentic-ai/fundamentals/multi-agent-systems.md) — The theoretical communication topologies these frameworks attempt to solve.
- [Agent Evaluation & Production](../../visualizers-and-playgrounds/README.md) — Benchmarks required before taking these frameworks into production.