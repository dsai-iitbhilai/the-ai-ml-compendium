# Agent Fundamentals

> The core reasoning loop: perceive → think → act → observe. This file covers the ReAct pattern, planning strategies (Tree-of-Thought, hierarchical), memory architectures (short-term, episodic, semantic), and tool-use theory for building autonomous LLM systems.

**Last Reviewed:** 2026-06

**Prerequisites:** [Prompt Engineering](../../05-generative-ai/prompt-engineering.md) · [LLM Fundamentals](../../05-generative-ai/llm-fundamentals.md)

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| *OpenAI — Tool Use & Agents* | Beginner | <https://platform.openai.com/docs/guides/function-calling> | Official guide on how to bind external functions to the LLM reasoning loop. |
| *Anthropic — Building Effective Agents* | Intermediate | <https://docs.anthropic.com/en/docs/build-with-claude/tool-use> | Excellent guide on the theory of tool use, XML formatting for agents, and ReAct paradigms. |
| *LangChain Conceptual Guide — Agents* | Intermediate | <https://python.langchain.com/docs/concepts/#agents> | Breakdown of ReAct, Plan-and-Execute, and OpenAI Tools agents. |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| *Intro to Large Language Models (Andrej Karpathy)* | Beginner | <https://www.youtube.com/watch?v=zjkBMFhNj_g> | The final third of this video brilliantly breaks down how LLMs are evolving into system-level agents. |
| *Agentic Workflows (Andrew Ng)* | Beginner | <https://www.youtube.com/watch?v=sal78wqfbRQ> | Overview of four key agentic design patterns: Reflection, Tool Use, Planning, and Multi-agent collaboration. |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| *DeepLearning.AI — Building Agentic RAG with LlamaIndex* | Intermediate | <https://www.deeplearning.ai/short-courses/building-agentic-rag-with-llamaindex/> | Moving beyond simple retrieval into dynamic query planning and routing. |
| *DeepLearning.AI — AI Agentic Design Patterns with AutoGen* | Advanced | <https://www.deeplearning.ai/short-courses/ai-agentic-design-patterns-with-autogen/> | Focuses on multi-agent conversational frameworks and task delegation. |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| *LangSmith* | Intermediate | <https://smith.langchain.com/> | Essential observability platform to visually trace the exact multi-step logic trees of your agents. |
| *AgentOps* | Advanced | <https://www.agentops.ai/> | Agent observability dashboard to track token costs, tool failure rates, and execution time per step. |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *ReAct: Synergizing Reasoning and Acting* (Yao et al., 2023) | Intermediate | <https://arxiv.org/abs/2210.03629> | The seminal paper that defined the interleaved Thought, Action, Observation loop. |
| *Chain-of-Thought Prompting Elicits Reasoning* (Wei et al., 2022) | Beginner | <https://arxiv.org/abs/2201.11903> | The precursor to ReAct—proving that explicit reasoning traces improve logic. |
| *Generative Agents: Interactive Simulacra* (Park et al., 2023) | Advanced | <https://arxiv.org/abs/2304.03442> | The "Stanford Smallville" paper introducing episodic memory, reflection, and planning for autonomous agents. |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| *ReAct Pattern from Scratch (Anthropic Cookbook)* | Advanced | <https://github.com/anthropics/anthropic-cookbook/blob/main/patterns/agents/basic_agent.py> | Pure Python implementation of an agent loop without the bloat of external frameworks. |
| *LangGraph Multi-Agent Workflows* | Advanced | <https://github.com/langchain-ai/langgraph> | Building cyclic, stateful multi-agent systems using graph theory. |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *LLM Powered Autonomous Agents* (Lilian Weng) | Intermediate | <https://lilianweng.github.io/posts/2023-06-23-agent/> | One of the most cited breakdowns of agent architecture (Planning, Memory, Tool Use). |

---

## Core Concepts

| Concept | Description |
|---------|-------------|
| **Agent Loop** | Infinite `while` cycle where the model receives an observation, produces a thought/action, and processes the result before the next step. |
| **ReAct Pattern** | Interleaving Reason (chain-of-thought traces) with Act (tool calls) so that reasoning is grounded in external feedback. |
| **Planning** | Decomposing a goal into a sequence or DAG of sub-steps; can be done upfront (plan-then-execute) or dynamically (re-plan on failure). |
| **Memory** | Short-term (conversation history, context window) and long-term (vector store, structured summaries, episodic buffers). |
| **Tool-Use Theory** | Abstraction that maps a model's generated function call to an external capability (API, code exec, search) with structured I/O contracts. |

---

## The ReAct Loop (Simplified)

```text
User Input
    ↓
┌─ LLM ──────────────────────┐
│ Thought: I need to look up │
│ the weather in Paris.      │
│ Action: get_weather(city=  │
│          "Paris")          │
└────────────────────────────┘
    ↓
  Tool Call → Observation: "22°C, clear"
    ↓
┌─ LLM ──────────────────────┐
│ Thought: Now I have the    │
│ weather. Respond to user.  │
│ Answer: It's 22°C and      │
│         clear in Paris.    │
└────────────────────────────┘
    ↓
  Final output to user
```

---

## Planning Strategies

| Strategy | Pros | Cons |
|----------|------|------|
| **Plan-then-Execute** | Simple, predictable | Brittle if environmental assumptions change midway through execution. |
| **Re-planning (ReAct)** | Adaptable to failures | Can loop indefinitely or get stuck in repetitive action traps. |
| **Tree-of-Thought (ToT)** | Explores multiple branches | Computationally expensive and slow. |
| **Hierarchical** | Manages high complexity | Hard to design the meta-controller and state routers. |

---

## Key Concepts Checklist

- **The Loop:** Understanding the state machine mechanics that keep an LLM generating sequential actions until a stop condition is met.
- **Structured Outputs:** Using JSON schemas or strict XML to guarantee the LLM outputs a valid function payload.
- **Memory:** The difference between semantic memory (RAG vector spaces) and episodic memory (time-series event logging).
- **Failure Recovery:** Designing prompts and tools that explicitly teach the model how to read an error trace and correct its subsequent tool call.

---

## Projects / Practice

| Project | Description |
|---|---|
| **Zero-Framework ReAct Loop** | Write a complete agentic loop entirely in raw Python using just the `openai` or `anthropic` SDK. Build an agent that can search Wikipedia and calculate math equations without using LangChain, relying strictly on a `while` loop and string parsing. |
| **Stateful LangGraph Agent** | Move from sequential loops to a Directed Cyclic Graph (DCG) using `LangGraph`. Build a customer support agent that routes complaints, searches a database, and explicitly asks a human for approval (human-in-the-loop) before executing a refund tool. |
| **Multi-Agent Coding Team** | Use `AutoGen` or `CrewAI` to deploy a multi-agent system consisting of a "Coder", a "Reviewer", and an "Executor". Have them collaboratively write, test, and debug a Python script in a local Docker sandbox until it passes a given test suite. |

---

## See also

- [Prompt Engineering](../../05-generative-ai/prompt-engineering.md) — The foundation for writing robust system prompts that guide ReAct logic.
- [RAG Systems](../../05-generative-ai/rag-systems.md) — How agents access and index long-term semantic memory.
- [MLOps](../../07-mlops-and-deployment/README.md) — Managing the observability, cost-tracking, and deployment of stochastic agent loops.