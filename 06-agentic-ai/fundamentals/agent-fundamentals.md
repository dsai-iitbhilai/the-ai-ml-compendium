# Agent Fundamentals

> *The core reasoning loop: perceive → think → act → observe.*

**Last Reviewed:** 2026-06

## Core Concepts

| Concept | Description |
|---------|-------------|
| **Agent Loop** | Infinite cycle where the model receives an observation, produces a thought/action, and processes the result before the next step. |
| **ReAct Pattern** | Interleaving **Reason** (chain-of-thought traces) with **Act** (tool calls) so that reasoning is grounded in external feedback. |
| **Planning** | Decomposing a goal into a sequence or DAG of sub-steps; can be done upfront (plan-then-execute) or dynamically (re-plan on failure). |
| **Memory** | Short-term (conversation history, context window) and long-term (vector store, structured summaries, episodic buffers). |
| **Tool-Use Theory** | Abstraction that maps a model's generated function call to an external capability (API, code exec, search, etc.) with structured I/O contracts. |

## ReAct Loop (Simplified)

```
User Input
    ↓
┌─ LLM ──────────────────────┐
│  Thought: I need to look up │
│  the weather in Paris.      │
│  Action: get_weather(city=  │
│           "Paris")          │
└─────────────────────────────┘
    ↓
  Tool Call → Observation: "22°C, clear"
    ↓
┌─ LLM ──────────────────────┐
│  Thought: Now I have the   │
│  weather. Respond to user. │
│  Answer:  It's 22°C and    │
│           clear in Paris.  │
└─────────────────────────────┘
    ↓
  Final output to user
```

## Planning Strategies

| Strategy | Pros | Cons |
|----------|------|------|
| **Plan-then-Execute** | Simple, predictable | Brittle if assumptions change |
| **Re-planning (ReAct-style)** | Adaptable | Can loop indefinitely |
| **Tree-of-Thought** | Explores multiple branches | Expensive |
| **Hierarchical** | Manages complexity | Hard to design the meta-controller |

## Resource Table

| Category | Title | Level | Link |
|----------|-------|-------|------|
| 📘 Docs | OpenAI — Building an agent | Beginner | https://platform.openai.com/docs/guides/agents |
| 📘 Docs | Anthropic — Agent building guide | Intermediate | https://docs.anthropic.com/en/docs/build-with-claude/agentic |
| 📄 Paper | "ReAct: Synergizing Reasoning and Acting in Language Models" (Yao et al., 2023) | Intermediate | https://arxiv.org/abs/2210.03629 |
| 📄 Paper | "Chain-of-Thought Prompting Elicits Reasoning in LLMs" (Wei et al., 2022) | Beginner | https://arxiv.org/abs/2201.11903 |
| 🎥 Video | AI Agents — A Deep Dive (Andrej Karpathy) | Intermediate | https://www.youtube.com/watch?v=fJ1g6eDvSDE |
| 📰 Blog | "The Agent Loop" — Lilian Weng | Intermediate | https://lilianweng.github.io/posts/2023-06-23-agent/ |
| 💻 Code/Notebook | ReAct Pattern from Scratch (Python) | Advanced | https://github.com/anthropics/anthropic-cookbook/blob/main/patterns/agents/basic_agent.py |
| 🎓 Course | DeepLearning.AI — Building Agentic RAG with LlamaIndex | Intermediate | https://www.deeplearning.ai/short-courses/building-agentic-rag-with-llamaindex/ |

## Key Takeaways

- The **ReAct pattern** is the backbone of most modern agent frameworks.
- **Planning** can be static or dynamic; dynamic planning incurs latency and cost but is more robust.
- **Memory** is the hardest unsolved problem — most production systems use a hybrid of context window + vector retrieval.
