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

## Resource Table

| Category | Title | Level | Link |
|----------|-------|-------|------|
| 📰 Blog | "How Klarna's AI Assistant Handled 2.3M Conversations" | Intermediate | https://www.klarna.com/international/press/klarna-ai-assistant/ |
| 📰 Blog | "Building a Code Review Agent at Scale" | Advanced | https://www.cursor.com/blog/code-review-agent |
| 📰 Blog | "Replit Agent — From IDE to Agentic Coding" | Intermediate | https://blog.replit.com/agent |
| 🎥 Video | "Agentic Systems at Intercom" | Intermediate | https://www.youtube.com/watch?v=_iG_k2ZEdbA |
| 📄 Paper | "AgentBench: Evaluating LLMs as Agents" (Liu et al., 2023) | Advanced | https://arxiv.org/abs/2308.03688 |
| 📄 Paper | "WebArena: A Realistic Web Environment for Agent Evaluation" (Zhou et al., 2024) | Advanced | https://arxiv.org/abs/2307.13854 |
| 💻 Code/Notebook | Agent Evaluation Suite (AgentBench) | Advanced | https://github.com/THUDM/AgentBench |

## Recurring Themes

1. **Human-in-the-loop at key decision boundaries** — not every step, but high-risk or low-confidence ones.
2. **Observability is non-negotiable** — every production deployment uses tracing (LangSmith, AgentOps, custom OpenTelemetry).
3. **Cost management** — cheap models for routine tasks, expensive models for planning / high-stakes decisions.
4. **Crawl → Walk → Run** — start with a single agent + 2 tools, expand to multi-agent only when the bottleneck is clear.
