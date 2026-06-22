# MCP — Model Context Protocol

> *An open protocol for connecting LLMs to external tools and data sources.*

**Last Reviewed:** 2026-06

> ⚠️ **Fast-moving section** — MCP is under active development. Server implementations, client libraries, and the spec itself evolve quickly.

## Overview

**Model Context Protocol (MCP)** is an open standard (originally proposed by Anthropic) that defines how LLM hosts (clients) discover and invoke tools exposed by MCP servers. It replaces ad-hoc tool integrations with a uniform interface — similar to how USB standardised peripheral connectivity.

## Architecture

```
┌─────────────┐      MCP Transport      ┌──────────────┐
│  LLM Host   │ ◄─────────────────────► │  MCP Server   │
│  (Client)   │   (stdio / SSE / WebRPC) │               │
│             │                          │ ┌───────────┐ │
│  - Claude   │     ListTools            │ │ Tool(s)   │ │
│  - VS Code  │     CallTool             │ │ Resource  │ │
│  - CLI      │     ListResources        │ │ Prompt    │ │
│  - LangGraph│     ReadResource         │ └───────────┘ │
└─────────────┘                          └──────────────┘
```

## Core Concepts

| Concept | Description |
|---------|-------------|
| **Transport** | Communication channel: `stdio` (subprocess pipe), `sse` (HTTP streaming), or WebRPC. |
| **Tools** | Functions the server exposes; defined with a name, description, and input schema. |
| **Resources** | Data objects the server exposes (files, DB rows, API results) addressable by URI. |
| **Prompts** | Pre-baked prompt templates the server offers to the host. |
| **Capabilities** | A server advertises which features (tools, resources, prompts) it supports. |

## Lifecycle

1. **Initialise** — client and server exchange protocol version and capabilities.
2. **ListTools** — client asks for available tools; server returns tool schemas.
3. **CallTool** — client invokes a tool by name with arguments; server returns result.
4. **(Optional) Subscribe** — client subscribes to resource change notifications.

## Resource Table

| Category | Title | Level | Link |
|----------|-------|-------|------|
| 📘 Docs | MCP Specification | Intermediate | https://spec.modelcontextprotocol.io/ |
| 📘 Docs | MCP Quick Start (Anthropic) | Beginner | https://modelcontextprotocol.io/quickstart |
| 💻 Code/Notebook | MCP Python SDK | Intermediate | https://github.com/modelcontextprotocol/python-sdk |
| 💻 Code/Notebook | MCP TypeScript SDK | Intermediate | https://github.com/modelcontextprotocol/typescript-sdk |
| 📰 Blog | "Introducing the Model Context Protocol" (Anthropic) | Beginner | https://www.anthropic.com/news/model-context-protocol |
| 🎥 Video | MCP Explained — AI Tooling Standard | Intermediate | https://www.youtube.com/watch?v=9Gs4cFEMlKw |
| 🕹️ Visualizer | MCP Inspector (Debug Tool) | Intermediate | https://github.com/modelcontextprotocol/inspector |
| 📰 Blog | "MCP: The USB-C for AI Tools" | Beginner | https://www.anthropic.com/engineering/mcp-usb-c-for-ai |

## Building an MCP Server (Minimal Example)

```python
# server.py
from mcp.server import Server, stdio_server

app = Server("weather-server")

@app.list_tools()
async def list_tools():
    return [{
        "name": "get_weather",
        "description": "Get weather for a city",
        "inputSchema": {
            "type": "object",
            "properties": {"city": {"type": "string"}},
            "required": ["city"]
        }
    }]

@app.call_tool()
async def call_tool(name: str, args: dict):
    if name == "get_weather":
        return {"temperature": 22, "conditions": "clear"}
    raise ValueError(f"Unknown tool: {name}")

if __name__ == "__main__":
    stdio_server.run(app)
```

## Ecosystem & Adoption

- **MCP servers** exist for filesystem, GitHub, Slack, PostgreSQL, Brave Search, and many more.
- **Hosts** include Claude Desktop, VS Code (via GitHub Copilot agent mode), and several CLI tools.
- **LangGraph / AutoGen** are integrating MCP as a tool-source layer, letting agents consume MCP servers transparently.
