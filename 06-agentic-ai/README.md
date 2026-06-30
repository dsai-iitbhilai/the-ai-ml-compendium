# 06 — Agentic AI

> *Building autonomous systems that reason, plan, and act using tools and models.*

**Last Reviewed:** 2026-06

## Overview

Agentic AI systems extend generative models beyond single-turn Q&A by equipping them with **memory**, **tool-use**, **planning**, and **multi-step reasoning**. Agents perceive environments, break down goals into sub-tasks, call external functions, reflect on results, and adapt—enabling autonomous workflows from code generation to browser automation to supply-chain optimisation.

This module covers the theory behind agent loops, the ReAct pattern, function-calling APIs, multi-agent coordination, and the current framework & protocol landscape. Because the tooling layer (frameworks, MCP, model providers) evolves rapidly, several sections are marked as **fast-moving** — they represent a point-in-time snapshot and should be supplemented with official docs.

## Prerequisites

- [**05 — Generative AI**](../05-generative-ai/README.md) — transformers, prompt engineering, LLM inference, alignment

## Sections

| # | Section | Level | Description |
|---|---------|-------|-------------|
| 1 | [Fundamentals / Agent Fundamentals](fundamentals/agent-fundamentals.md) | Intermediate | Agent loops, ReAct, planning, memory, tool-use theory |
| 2 | [Fundamentals / Tool Use & Function Calling](fundamentals/tool-use-and-function-calling.md) | Advanced | Function-calling APIs, tool definition, structured output |
| 3 | [Fundamentals / Multi-Agent Systems](fundamentals/multi-agent-systems.md) | Advanced | Coordination, delegation, communication topologies |
| 4 | [Current Tooling / Frameworks](current-tooling/frameworks.md) | Intermediate | LangGraph, CrewAI, AutoGen, Claude Agent SDK, Swarm |
| 5 | [Current Tooling / MCP (Model Context Protocol)](current-tooling/mcp-model-context-protocol.md) | Intermediate | MCP protocol, servers, clients, tool discovery |
| 6 | [Case Studies](case-studies.md) | Advanced | Real-world agent deployments and production lessons |

> ** Fast-moving content** — Sections 4 and 5 cover rapidly evolving tooling. APIs, SDK versions, and best-practices change frequently. Cross-reference with official documentation before building production systems.

## How to Use This Module

1. Start with **Agent Fundamentals** to understand the core reasoning loop.
2. Move to **Tool Use & Function Calling** for the implementation surface between model and tools.
3. Explore **Multi-Agent Systems** for patterns that scale beyond a single agent.
4. Survey the **Frameworks** and **MCP** sections to choose your stack.
5. Read **Case Studies** to internalise real-world pitfalls and solutions.
