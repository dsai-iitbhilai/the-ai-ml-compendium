# Agentic AI — Case Studies

> *Real-world agent deployments, production learnings, and architectural decisions.*

**Last Reviewed:** 2026-06

## Case Study 1 — Customer Support Agent (Large E-Commerce)

**Context:** A Fortune-500 retailer replaced its intent-based chatbot with a ReAct agent backed by a product catalogue, order-status API, and returns workflow.

| Aspect | Detail |
|--------|--------|
| **Framework** | LangGraph + Claude 3.5 Sonnet |
| **Tools** | 12 tools: search products, check order, initiate return, escalate to human |
| **Memory** | Conversation summary + vector store of past interactions |
| **Human-in-loop** | Triggered on refund amounts > $100 or repeated dissatisfaction |
| **Outcome** | 38 % reduction in human escalations; avg handle time improved 42 % |

**Key lesson:** Add a *confidence threshold* — when the agent's internal log-probability of its next action is low, defer to a human immediately rather than hallucinating a bad answer.

---

## Case Study 2 — Automated Code Review Agent (SaaS Startup)

**Context:** A 40-person engineering team deployed an agent that reviews every PR against coding standards, security rules, and test coverage.

| Aspect | Detail |
|--------|--------|
| **Framework** | Custom supervisor + sub-agents (1 per review category) |
| **Tools** | `read_file`, `run_linter`, `search_semgrep_rules`, `post_comment` |
| **Model** | GPT-4o for the supervisor; GPT-4o-mini for individual reviewers |
| **Prompt Strategy** | Few-shot examples from past human reviews per category |
| **Outcome** | 73 % of PR comments accepted by developers; 12 % reduction in security bugs reaching production |

**Key lesson:** Give reviewers *clear personas and guardrails* — the security reviewer must never suggest code changes, only flag risks. This prevents the agent from accidentally introducing vulnerabilities.

---

## Case Study 3 — Research Analyst Agent (Investment Bank)

**Context:** An internal agent that ingests earnings calls, SEC filings, and news to produce structured investment memos.

| Aspect | Detail |
|--------|--------|
| **Framework** | AutoGen — multi-agent team (Researcher, Analyst, Writer) |
| **Tools** | Web search, PDF parser, SEC EDGAR API, DCF calculator |
| **Memory** | Long-term vector store for company profiles; short-term for the current memo session |
| **Routing** | Supervisor agent routes queries to the correct sub-agent based on tool set |
| **Outcome** | 4× faster memo generation; analysts now edit rather than draft from scratch |

**Key lesson:** Agents *must* cite sources by paragraph number — compliance requires full auditability. Use structured output schemas that include a `citations` array field.

---

## Case Study 4 — Supply Chain Optimisation (Manufacturing)

**Context:** A multinational manufacturer used agents to monitor supply-chain alerts and propose re-routing decisions.

| Aspect | Detail |
|--------|--------|
| **Framework** | LangGraph + custom MCP servers for each ERP system |
| **Tools** | `check_inventory`, `forecast_delay`, `reroute_shipment`, `notify_team` |
| **Model** | Claude Opus for planning; Sonnet for execution |
| **State persistence** | Postgres-backed checkpointing for long-running planning sessions |
| **Outcome** | 22 % reduction in delayed orders during a 6-month pilot |

**Key lesson:** Long-running agents need *checkpoint and resume* — supply-chain plans take hours. Without persistence, a single crash loses all progress.

---


## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| *Anthropic — Evaluating Agents* | Intermediate | <https://docs.anthropic.com/en/docs/build-with-claude/agentic> | Best practices on grading non-deterministic outputs and building evaluation pipelines. |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| *Agentic Systems at Intercom* | Intermediate | <https://www.youtube.com/watch?v=_iG_k2ZEdbA> | Practical teardown of deploying and evaluating customer-facing AI agents at scale. |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *AgentBench: Evaluating LLMs as Agents* (Liu et al., 2023) | Advanced | <https://arxiv.org/abs/2308.03688> | A comprehensive framework evaluating LLMs as agents across varied interactive environments. |
| *WebArena: A Realistic Web Environment for Agent Evaluation* (Zhou et al., 2024) | Advanced | <https://arxiv.org/abs/2307.13854> | Highly realistic web environment for testing autonomous web navigation. |
| *GAIA: a benchmark for General AI Assistants* (Mialon et al., 2023) | Advanced | <https://arxiv.org/abs/2311.12983> | Meta's benchmark for testing reasoning, multi-modality, and tool-use proficiency [cite: 1.4.2, 1.4.3]. |
| *Gaia2: Benchmarking LLM Agents on Dynamic and Asynchronous Environments* (Froger et al., 2026) | Advanced | <https://arxiv.org/abs/2602.11964> | Evaluates agents operating under temporal constraints in evolving environments [cite: 1.4.1]. |
| *SWE-Bench++: A Framework for the Scalable Generation of Software Engineering Benchmarks* (Wang et al., 2025) | Advanced | <https://arxiv.org/abs/2512.17419> | Automates benchmark generation from live GitHub pull requests across 11 programming languages [cite: 1.1.2]. |
| *OSWorld-MCP: Benchmarking MCP Tool Invocation In Computer-Use Agents* | Advanced | <https://arxiv.org/html/2510.24563v2> | Assesses dynamic interaction between direct GUI operations and external tool calls [cite: 1.2.1]. |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| *AgentBench* | Advanced | <https://github.com/THUDM/AgentBench> | The official repository and evaluation suite for the AgentBench paper. |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *How Klarna's AI Assistant Handled 2.3M Conversations* | Intermediate | <https://www.klarna.com/international/press/klarna-ai-assistant/> | Case study showing how Klarna's agent resolves tasks in under 2 minutes across 35 languages [cite: 1.3.3]. |
| *Building a Code Review Agent at Scale* | Advanced | <https://www.cursor.com/blog/code-review-agent> | Behind-the-scenes engineering breakdown of building autonomous coding workflows. |
| *Replit Agent — From IDE to Agentic Coding* | Intermediate | <https://blog.replit.com/agent> | Details the transition from copilot autocomplete patterns to agentic goal-completion. |

---

## Recurring Themes

1. **Human-in-the-loop at key decision boundaries** — not every step, but high-risk or low-confidence ones.
2. **Observability is non-negotiable** — every production deployment uses tracing (LangSmith, AgentOps, custom OpenTelemetry).
3. **Cost management** — cheap models for routine tasks, expensive models for planning / high-stakes decisions.
4. **Crawl → Walk → Run** — start with a single agent + 2 tools, expand to multi-agent only when the bottleneck is clear.
