# Agent Frameworks

> *A point-in-time survey of the most widely used agentic frameworks.*

**Last Reviewed:** 2026-06

> ⚠️ **Fast-moving section** — SDK versions, APIs, and recommended patterns change frequently. Verify against official docs.

## Framework Comparison

| Framework | Maintainer | Graph Model | Memory Persistence | Multi-Agent | Key Strength |
|-----------|-----------|-------------|--------------------|-------------|----------------|
| **LangGraph** | LangChain | Stateful graph (nodes + edges) | Built-in (checkpointing) | Yes | Granular control, production tracing |
| **CrewAI** | CrewAI | Role-based sequential/hierarchical | Via callbacks | Yes | Simple role abstraction |
| **AutoGen** | Microsoft | Agent chat (conversable agents) | Extensible | Yes | Research breadth, strong multi-agent |
| **Claude Agent SDK** | Anthropic | Loop with tool-use + hand-off | Automatic (context) | Via hand-off | First-class Claude support |
| **Swarm** | OpenAI (experimental) | Lightweight hand-off graph | Minimal | Yes | Minimal, educational, easy to fork |

## When to Use What

- **LangGraph** — production pipelines, complex branching logic, fine-grained observability.
- **CrewAI** — rapid prototyping of role-based teams; good entry point for multi-agent.
- **AutoGen** — research experiments, multi-agent conversation patterns, custom agent topologies.
- **Claude Agent SDK** — building agents specifically for Claude; tight integration with Anthropic's API.
- **Swarm** — learning the hand-off pattern; small prototypes. Not recommended for production.

## Key Features to Evaluate

- **State persistence** — can the agent survive a crash or run over multiple days?
- **Human-in-the-loop** — does the framework support pausing for human approval?
- **Streaming** — real-time token and tool-call streaming to the UI.
- **Tracing / Observability** — LangSmith (LangGraph), AgentOps, custom OpenTelemetry.
- **Model agnosticism** — can you swap between OpenAI / Anthropic / open-source?

## Resource Table

| Category | Title | Level | Link |
|----------|-------|-------|------|
| 📘 Docs | LangGraph Documentation | Beginner | https://langchain-ai.github.io/langgraph/ |
| 📘 Docs | CrewAI Documentation | Beginner | https://docs.crewai.com/ |
| 📘 Docs | AutoGen Documentation | Intermediate | https://microsoft.github.io/autogen/ |
| 📘 Docs | Claude Agent SDK (Anthropic) | Beginner | https://docs.anthropic.com/en/docs/agents-and-tools/agent-sdk |
| 📘 Docs | OpenAI Swarm (GitHub) | Intermediate | https://github.com/openai/swarm |
| 🎥 Video | "LangGraph in Production" — LangChain | Intermediate | https://www.youtube.com/watch?v=JqG1U1iSs6w |
| 🎓 Course | DeepLearning.AI — AI Agents in LangGraph | Beginner | https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/ |
| 💻 Code/Notebook | LangGraph Quick Start | Beginner | https://github.com/langchain-ai/langgraph/blob/main/examples/quickstart.ipynb |

## Framework Lifecycle Considerations

- **Vendor lock-in** — LangGraph pushes towards LangChain ecosystem; AutoGen favours Azure OpenAI.
- **Maintenance velocity** — Swarm is experimental and rarely updated; LangGraph and AutoGen have active releases.
- **Community & support** — LangGraph has the largest community; CrewAI is growing fast for role-based workflows.
