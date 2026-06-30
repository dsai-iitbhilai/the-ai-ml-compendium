# Tool Use & Function Calling

> Bridging language models to external systems through structured function-calling APIs. This file covers JSON Schema constraints, parallel execution, constrained decoding topologies, and provider-specific runtime abstractions.

**Last Reviewed:** 2026-06

**Prerequisites:** [Prompt Engineering](../../05-generative-ai/prompt-engineering.md) · [Agent Fundamentals](agent-fundamentals.md)

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| *OpenAI — Function Calling Guide* | Beginner | <https://platform.openai.com/docs/guides/function-calling> | Official guide covering tool arrays, parallel execution, and structured outputs. |
| *Anthropic — Tool Use* | Intermediate | <https://docs.anthropic.com/en/docs/build-with-claude/tool-use> | Excellent guide on the theory of tool use, XML formatting for agents, and handling errors. |
| *Google Gemini — Function Calling* | Beginner | <https://ai.google.dev/gemini-api/docs/function-calling> | Guide to configuring `function_declarations` in the Gemini API. |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| *Structured Outputs & Tool Calling* | Intermediate | <https://www.youtube.com/watch?v=GZ7O4w0X6fA> | Breakdown of forcing LLMs to output reliable data schemas using function calling. |
| *Berkeley Function Calling Leaderboard (BFCL)* | Advanced | <https://www.youtube.com/watch?v=x9q-n3v3Vv0> | Deep dive into how open-source models are benchmarked for API execution accuracy. |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| *DeepLearning.AI — Function Calling with OpenAI* | Beginner | <https://www.deeplearning.ai/short-courses/function-calling-with-openai/> | Hands-on tutorial on converting natural language into API calls. |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| *OpenAI Playground (Chat)* | Beginner | <https://platform.openai.com/playground/chat> | Native interface to define JSON schemas and test if the model triggers the tool correctly. |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *Toolformer: Language Models Can Teach Themselves to Use Tools* (Schick et al., 2023) | Advanced | <https://arxiv.org/abs/2302.04761> | Foundational paper on pretraining models to emit API calls via self-supervised learning. |
| *Gorilla: Large Language Model Connected with Massive APIs* (Patil et al., 2023) | Advanced | <https://arxiv.org/abs/2305.15334> | Evaluates how fine-tuning enables models to write accurate API calls and adapt to schema changes. |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| *OpenAI Function Calling Cookbook* | Intermediate | <https://cookbook.openai.com/examples/how_to_call_functions_with_chat_models> | Official Python examples for single, parallel, and streaming function calls. |
| *Instructor* | Advanced | <https://github.com/jxnl/instructor> | Library built on `pydantic` that forces structured JSON output and handles tool-call validation/retries. |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *A Practical Guide to Tool Calling in LLMs* | Intermediate | <https://www.anthropic.com/engineering/tool-use-practical-guide> | Real-world engineering tips on schema design, context limits, and failure states. |

---

## Tool Definition Architecture

**JSON Schema Example (OpenAI / Gemini format):**
```json
{
  "type": "function",
  "function": {
    "name": "get_weather",
    "description": "Get current temperature for a city. Call this when the user asks about weather.",
    "parameters": {
      "type": "object",
      "properties": {
        "city": { "type": "string", "description": "City name, e.g., Paris" },
        "unit": { "type": "string", "enum": ["celsius", "fahrenheit"] }
      },
      "required": ["city"]
    }
  }
}
```

---

## Provider Implementation Comparison

| Provider | API Abstraction | Structured Output Method | Streaming Support |
|----------|-----------------|--------------------------|-------------------|
| **OpenAI** | `tools` array on chat completion | `response_format: { type: "json_schema" }` | Yes (JSON chunk deltas) |
| **Anthropic** | `tools` block in messages | Native XML/JSON block detection | Yes (Content block streaming) |
| **Gemini** | `function_declarations` | `response_schema` in generation config | Yes |
| **OSS (vLLM)** | OpenAI-compatible `tools` endpoint | Constrained decoding (Regex, FSMs via Outlines) | Varies by serving engine |

---

## Key Concepts Checklist

- **Structured Outputs (Constrained Decoding):** Using Finite State Machines (FSMs) or regex masks at the logits level to guarantee 100% valid JSON matching a `pydantic` schema.
- **Parallel Tool Calls:** Processing an array of simultaneous independent tool requests (e.g., checking weather for 5 cities) asynchronously before returning observations to the LLM.
- **`tool_choice` Semantics:** Forcing the LLM to use a specific tool (`tool_choice: {"name": "X"}`), letting it decide (`auto`), or disabling tools (`none`).
- **Streaming Execution:** Parsing partial JSON buffers token-by-token so the UI can render loading states before the LLM finishes emitting the arguments.
- **Fault Tolerance:** Designing the tool runtime to catch exceptions (e.g., API timeouts) and return them as an `observation` so the LLM can self-correct and try again.

---

## Projects / Practice

| Project | Description |
|---|---|
| **Constrained Text-to-SQL Agent** | Build an agent that takes natural language, queries a local SQLite database schema, and generates a SQL query. Use `Instructor` or `Outlines` to strictly bind the output to a validated Pydantic model before executing the query, preventing syntax hallucinations. |
| **Parallel API Aggregator** | Create a financial research assistant using the `asyncio` library and OpenAI parallel tool calling. When asked to "Compare AAPL, MSFT, and GOOGL", the model should emit three parallel `get_stock_data` function calls, which your runtime executes concurrently to reduce total latency. |
| **Resilient Error-Handling Loop** | Write a tool-calling loop that intentionally connects to a flaky dummy API. Program the system prompt to teach the model how to read HTTP 500 errors or timeout exceptions returned in the `tool_message` block and dynamically adjust its retry strategy or switch to a fallback API. |

---

## See also

- [Agent Fundamentals](agent-fundamentals.md) — How tool calling fits into the broader ReAct loop and autonomous planning.
- [Prompt Engineering](../../05-generative-ai/prompt-engineering.md) — Structuring system prompts to accurately describe tool behaviors and boundaries.
- [MLOps](../../07-mlops-and-deployment/README.md) — Monitoring and observing latency/token usage for extensive tool-calling pipelines.