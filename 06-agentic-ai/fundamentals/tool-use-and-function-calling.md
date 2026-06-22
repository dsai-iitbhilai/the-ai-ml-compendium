# Tool Use & Function Calling

> *Bridging language models to external systems through structured function-calling APIs.*

**Last Reviewed:** 2026-06

## Overview

Function calling (or tool use) is the mechanism by which an LLM requests the execution of an external function. The model outputs a structured JSON payload — typically a function name and arguments — which the runtime dispatches to the real implementation and feeds the result back as a new message.

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Tool Definition** | A JSON Schema description of a function (name, description, parameters) provided in the system/user prompt or API parameter. |
| **Structured Output** | Enforcing the model to emit valid JSON matching a schema — critical for reliable tool parsing. |
| **Parallel Tool Calls** | The model requests multiple tools in a single turn; the runtime executes them concurrently. |
| **Streaming Tools** | Tool calls are streamed token-by-token (or as partial JSON) for low-latency UIs. |
| **`tool_choice`** | Controls whether the model must use a tool, may use a tool, or must not. Values: `auto`, `any`/`required`, `none`, or a specific tool name. |

## Tool Definition Example (OpenAI format)

```json
{
  "type": "function",
  "function": {
    "name": "get_weather",
    "description": "Get current temperature for a city.",
    "parameters": {
      "type": "object",
      "properties": {
        "city": { "type": "string", "description": "City name" },
        "unit": { "type": "string", "enum": ["celsius", "fahrenheit"] }
      },
      "required": ["city"]
    }
  }
}
```

## Provider Comparison

| Provider | API Style | Structured Output | Streaming Support |
|----------|-----------|------------------|-------------------|
| OpenAI | `tools` param on chat completion | `response_format: { type: "json_schema", ... }` | Yes (delta) |
| Anthropic | `tools` block in messages | `thinking` mode with tool-use content blocks | Yes (content block streaming) |
| Google Gemini | `tools` / `function_declarations` | `response_schema` on generation config | Yes |
| Open-source | Mirrors OpenAI schema (vLLM, TGI, LiteLLM) | Depends on backend | Varies |

## Resource Table

| Category | Title | Level | Link |
|----------|-------|-------|------|
| 📘 Docs | OpenAI — Function Calling Guide | Beginner | https://platform.openai.com/docs/guides/function-calling |
| 📘 Docs | Anthropic — Tool Use | Beginner | https://docs.anthropic.com/en/docs/build-with-claude/tool-use |
| 📘 Docs | Google Gemini — Function Calling | Beginner | https://ai.google.dev/gemini-api/docs/function-calling |
| 📄 Paper | "Toolformer: Language Models Can Teach Themselves to Use Tools" (Schick et al., 2023) | Advanced | https://arxiv.org/abs/2302.04761 |
| 💻 Code/Notebook | OpenAI Function Calling Cookbook | Intermediate | https://cookbook.openai.com/examples/how_to_call_functions_with_chat_models |
| 🎥 Video | Structured Outputs & Tool Calling (Anthropic) | Intermediate | https://www.youtube.com/watch?v=GZ7O4w0X6fA |
| 🎓 Course | DeepLearning.AI — Function Calling with OpenAI | Beginner | https://www.deeplearning.ai/short-courses/function-calling-with-openai/ |
| 📰 Blog | "A Practical Guide to Tool Calling in LLMs" | Intermediate | https://www.anthropic.com/engineering/tool-use-practical-guide |

## Common Pitfalls

- **Token-heavy tool schemas** — large JSON Schema definitions eat context window; compress descriptions or use shorthand.
- **Non-deterministic tool selection** — the model may call the wrong tool; include robust validation and fallbacks.
- **Partial / malformed JSON** — use constrained decoding (guidance, outlines) or schema-constrained generation APIs.
- **Tool output overflows** — truncate or summarise tool results before re-injecting into context.
