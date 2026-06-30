# MCP — Model Context Protocol

> An open protocol for connecting LLMs to external tools and data sources. This file covers the architecture of MCP, distinguishing between Tools, Resources, and Prompts, and explains how to implement custom servers using `stdio` and `SSE` transports.

**Last Reviewed:** 2026-06

**Prerequisites:** [Tool Use & Function Calling](../../docs/06-agentic-ai/fundamentals/tool-use-and-function-calling.md) · [Agent Fundamentals](../../docs/06-agentic-ai/fundamentals/agent-fundamentals.md)

> ⚠️ **Fast-moving section** — MCP is under active development. Server implementations, client libraries, and the spec itself evolve quickly. Verify against official docs.

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| *Model Context Protocol Specification* | Intermediate | <https://spec.modelcontextprotocol.io/> | The official, definitive documentation of the JSON-RPC message structure and capability negotiation. |
| *MCP Quick Start (Anthropic)* | Beginner | <https://modelcontextprotocol.io/quickstart> | Step-by-step guide to connecting your first MCP server to Claude Desktop. |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| *MCP Explained — AI Tooling Standard* | Intermediate | <https://www.youtube.com/watch?v=qTj8K287vHw> | Breakdown of the protocol design and why a universal abstraction layer for LLM tooling is necessary. |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| *MCP Inspector* | Intermediate | <https://github.com/modelcontextprotocol/inspector> | An essential local web-based debugging tool for testing your custom MCP server's `stdio` endpoints before connecting them to an LLM. |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| *MCP Python SDK* | Intermediate | <https://github.com/modelcontextprotocol/python-sdk> | The official Python SDK for building both MCP servers and MCP clients. |
| *MCP TypeScript SDK* | Intermediate | <https://github.com/modelcontextprotocol/typescript-sdk> | The official TS/JS SDK for building MCP servers and clients. |
| *Awesome MCP Servers* | Beginner | <https://github.com/modelcontextprotocol/servers> | A curated list of production-ready MCP servers (GitHub, Postgres, Slack, File System). |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *Introducing the Model Context Protocol* | Beginner | <https://www.anthropic.com/news/model-context-protocol> | Anthropic's launch announcement explaining the vision for MCP. |
| *MCP: The USB-C for AI Tools* | Beginner | <https://www.anthropic.com/engineering/mcp-usb-c-for-ai> | Conceptual deep-dive into standardizing tool boundaries across different model providers. |

---

## Architecture

**Model Context Protocol (MCP)** replaces ad-hoc tool integrations with a uniform JSON-RPC interface — functioning as a universal "USB-C port" for AI agents to connect to external systems.

```text
┌─────────────┐       MCP Transport      ┌──────────────┐
│  LLM Host   │ ◄─────────────────────►  │  MCP Server  │
│  (Client)   │   (stdio / SSE / HTTP)   │              │
│             │                          │ ┌──────────┐ │
│  - Claude   │     ListTools            │ │ Tool(s)  │ │
│  - VS Code  │     CallTool             │ │ Resource │ │
│  - CLI      │     ListResources        │ │ Prompt   │ │
│  - LangGraph│     ReadResource         │ └──────────┘ │
└─────────────┘                          └──────────────┘
```

---

## Core Concepts

| Concept | Description |
|---------|-------------|
| **Transport** | Communication channel: `stdio` (subprocess pipe/stdout), `sse` (HTTP streaming for remote servers). |
| **Tools** | Executable functions the server exposes; defined with a name, description, and JSON Schema input. Tools cause side effects (e.g., `git commit`). |
| **Resources** | Data objects the server exposes (files, DB rows, API results) addressable by a unique URI (`file://` or `postgres://`). Resources are read-only. |
| **Prompts** | Pre-baked prompt templates the server offers to the host, allowing the server to dictate how its tools should be used. |
| **Capabilities** | During initialization, a server advertises which features (tools, resources, prompts, logging) it supports. |

---

## MCP Lifecycle

1. **Initialize:** The client and server exchange protocol versions and capabilities.
2. **Discovery (`ListTools` / `ListResources`):** The client asks for available tools/resources; the server returns the JSON schemas and URIs.
3. **Execution (`CallTool`):** The client invokes a tool by name with arguments; the server executes the code and returns the result.
4. **Subscription (Optional):** The client subscribes to resource change notifications (e.g., getting pinged when a log file updates).

---

## Building an MCP Server (Minimal Python Example)

```python
# server.py
from mcp.server.fastmcp import FastMCP

# FastMCP abstracts away the raw JSON-RPC handling
app = FastMCP("weather-server")

@app.tool()
async def get_weather(city: str) -> str:
    """Get weather for a city."""
    # In a real app, this calls a weather API
    return f"The temperature in {city} is 22°C and clear."

if __name__ == "__main__":
    # Runs on stdio by default for local execution
    app.run()
```

---

## Ecosystem & Adoption

- **Servers:** High-quality implementations exist for Filesystems, GitHub, Slack, PostgreSQL, Brave Search, and Kubernetes.
- **Hosts (Clients):** Claude Desktop, Cursor, VS Code (via GitHub Copilot agent mode), and Zed.
- **Orchestration:** LangGraph, LlamaIndex, and AutoGen are natively integrating MCP clients, allowing their orchestration graphs to consume remote MCP servers transparently without writing custom wrapper functions.

---

## Key Concepts Checklist

- **Transport Protocols:** Understanding when to use `stdio` (for local, secure subprocess execution like Claude Desktop) vs. `SSE/HTTP` (for remote, distributed API servers).
- **Tool vs. Resource:** Tools are for execution and side effects (`POST/PUT`); Resources are for injecting context and reading data (`GET`).
- **Security Boundaries:** Recognizing that MCP shifts the responsibility of tool execution away from the LLM host (the client) and onto the specialized MCP Server environment.
- **FastMCP:** Utilizing high-level libraries like `FastMCP` (Python) to auto-generate JSON schemas from type hints instead of writing raw JSON-RPC handlers.

---

## Projects / Practice

| Project | Description |
|---|---|
| **Local Database MCP Server** | Build an MCP server in Python using `FastMCP` that connects to a local SQLite database. Expose a `Resource` that lists all table schemas, and a `Tool` that allows the LLM to execute `SELECT` queries safely. Connect this server to Claude Desktop via `stdio`. |
| **Remote SSE Search Server** | Build an MCP Server using TypeScript that wraps a web search API (like Tavily or DuckDuckGo). Instead of `stdio`, configure the transport to use Server-Sent Events (SSE) and host it on a local port. Write a simple Python MCP Client script to connect to it over HTTP. |
| **Agentic Framework Integration** | Spin up the official `mcp-server-github` repository locally. Using LangGraph, write an agent that natively attaches to the GitHub MCP server, reads a specific issue from a repository (using `ReadResource`), and uses a tool to post a comment on that issue. |

---

## See also

- [Tool Use & Function Calling](../../docs/06-agentic-ai/fundamentals/tool-use-and-function-calling.md) — The underlying JSON schema and payload mechanisms that MCP standardizes.
- [Agent Frameworks](../../docs/06-agentic-ai/current-tooling/frameworks.md) — How frameworks like LangGraph integrate MCP clients into their orchestration loops.