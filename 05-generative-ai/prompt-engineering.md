# Prompt Engineering

Prompt engineering is the practice of designing input text to reliably elicit desired outputs from LLMs. This file covers zero-shot and few-shot prompting, chain-of-thought reasoning, system vs. user messages, structured output formats, and prompt optimization patterns.

## Resources

| Category | Title | Description | Level | Last Reviewed |
|----------|-------|-------------|-------|---------------|
| 📘 Docs | [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering) | Official guide covering six core strategies: write clear instructions, provide examples, use delimiters, etc. | Beginner | 2026-06 |
| 📘 Docs | [Anthropic Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering) | Comprehensive guide with techniques specific to Claude, including XML tags and chain-of-thought | Beginner | 2026-06 |
| 📄 Paper | [Chain-of-Thought Prompting Elicits Reasoning (Wei et al., 2022)](https://arxiv.org/abs/2201.11903) | Demonstrates that step-by-step reasoning prompts drastically improve multi-step arithmetic and logic | Intermediate | 2026-06 |
| 📄 Paper | [Tree of Thoughts (Yao et al., 2023)](https://arxiv.org/abs/2305.10601) | Extends CoT with tree search over reasoning paths, enabling deliberate planning | Advanced | 2026-06 |
| 💻 Code/Notebook | [PromptBench — systematic evaluation](https://github.com/example/promptbench) | Framework for evaluating prompt robustness across adversarial, OOD, and style perturbations | Advanced | 2026-06 |
| 🕹️ Visualizer/Playground | [OpenAI Playground](https://platform.openai.com/playground) | Interactive chat and completion sandbox with adjustable system prompt, temperature, and top-p | Beginner | 2026-06 |
| 🎓 Course | [DeepLearning.AI — Prompt Engineering for ChatGPT](https://www.deeplearning.ai/short-courses/) | Short hands-on course by Isa Fulford & Andrew Ng covering iterative prompt development | Beginner | 2026-06 |

## Key Techniques

| Technique | Description |
|-----------|-------------|
| **Zero-shot** | Direct instruction without examples — relies entirely on the model's pretraining |
| **Few-shot** | Provide 2–5 input-output examples in the prompt before asking a new question |
| **Chain-of-Thought (CoT)** | Ask the model to "think step by step" or provide a reasoning trace |
| **Self-Consistency** | Run CoT multiple times and take a majority vote over final answers |
| **Tree of Thoughts (ToT)** | Explore multiple reasoning paths with lookahead and backtracking |
| **ReAct** | Interleave reasoning steps with tool calls (e.g., search, calculator) |
| **System Prompts** | Persistent instruction prepended to the conversation that sets behavior, tone, and constraints |
| **Structured Output** | Request JSON, XML, or markdown output with schema descriptions for reliable parsing |

## Prompt Structure Best Practices

1. **Be specific and direct** — "Summarize the article in 3 bullet points" rather than "Summarize this"
2. **Use delimiters** — Wrap input data in `"""` or ```` to separate instructions from content
3. **Provide examples** — Show the model the exact format you expect in few-shot demonstrations
4. **Break complex tasks into steps** — Chain subtasks with intermediate outputs
5. **Set role and constraints** — "You are a helpful coding assistant. Use TypeScript. Explain your reasoning."
6. **Iterate** — Test and refine prompts; small wording changes can have large effects

## References

- [Pre-train, Prompt, and Predict (Liu et al., 2021)](https://arxiv.org/abs/2107.13586)
- [Graph of Thoughts (Besta et al., 2023)](https://arxiv.org/abs/2308.09687)
- [The Prompt Report (White et al., 2023)](https://arxiv.org/abs/2306.11309)
