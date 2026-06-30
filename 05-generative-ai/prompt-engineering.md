# Prompt Engineering

> Prompt engineering is the practice of designing input text and optimization architectures to reliably elicit desired outputs from LLMs. This file covers programmatic prompting, logical reasoning topologies (CoT, ToT, GoT), structured outputs, and framework-driven optimization for agentic systems.

**Last Reviewed:** 2026-06

**Prerequisites:** [LLM Fundamentals](llm-fundamentals.md) · Probability Theory · Graph Theory

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| *OpenAI Prompt Engineering Guide* | Beginner | <https://platform.openai.com/docs/guides/prompt-engineering> | Official baseline strategies: clear instructions, few-shot examples, and delimiters. |
| *Anthropic Prompt Engineering Guide* | Beginner | <https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering> | Claude-specific techniques focusing heavily on XML tag structuring. |
| *DSPy Documentation* | Advanced | <https://dspy-docs.vercel.app/> | Framework for mathematically optimizing language model prompts and weights programmatically. |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| *Stanford XCS224U: Prompting and RLHF* | Intermediate | <https://www.youtube.com/watch?v=s0Hivn4c3V4> | Christopher Potts discussing the theoretical and empirical foundations of prompt design. |
| *Building LLM applications for production* | Advanced | <https://www.youtube.com/watch?v=cOJE0nO18sM> | Chip Huyen's breakdown of scaling prompt-based applications and managing MLOps drift. |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| *DeepLearning.AI — Prompt Engineering for ChatGPT* | Beginner | <https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/> | Hands-on introduction covering iterative prompt development by Andrew Ng. |
| *LLM Mastery: Programmatic Prompting* | Advanced | <https://www.oreilly.com/library/view/programming-large-language/9781098150493/> | Focuses on moving from manual string manipulation to structured, compiled LLM calls. |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| *OpenAI Playground* | Beginner | <https://platform.openai.com/playground> | Interactive sandbox for testing system prompts, temperature, and top-p sampling. |
| *Anthropic Console* | Intermediate | <https://console.anthropic.com/> | Excellent environment for debugging multi-turn agentic interactions and evaluating XML schemas. |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *Chain-of-Thought Prompting Elicits Reasoning* (Wei et al., 2022) | Intermediate | <https://arxiv.org/abs/2201.11903> | Demonstrates that forcing step-by-step intermediate representations improves multi-step logic. |
| *Tree of Thoughts* (Yao et al., 2023) | Advanced | <https://arxiv.org/abs/2305.10601> | Extends CoT via algorithmic design, utilizing tree search (DFS/BFS) over reasoning paths. |
| *Graph of Thoughts* (Besta et al., 2023) | Advanced | <https://arxiv.org/abs/2308.09687> | Models reasoning as a Directed Acyclic Graph (DAG), enabling non-sequential, synergistic thought combination. |
| *The Prompt Report* (White et al., 2023) | Intermediate | <https://arxiv.org/abs/2306.11309> | A systematic survey of over 30 prompting techniques and their mathematical efficacy. |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| *PromptBench* | Advanced | <https://github.com/microsoft/promptbench> | Framework for systematically evaluating prompt robustness across adversarial and OOD perturbations. |
| *DSPy* | Advanced | <https://github.com/stanfordnlp/dspy> | Eliminates manual prompt engineering by compiling and optimizing LLM pipelines directly. |
| *Outlines* | Advanced | <https://github.com/outlines-dev/outlines> | Provides neural text generation with strict structural constraints (JSON, Regex) at the logits level. |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *LLM Powered Autonomous Agents* (Lilian Weng) | Advanced | <https://lilianweng.github.io/posts/2023-06-23-agent/> | Deep dive into ReAct patterns, where reasoning traces are interleaved with external tool calls. |
| *Prompt Engineering is Dead* | Intermediate | <https://spectrum.ieee.org/prompt-engineering-is-dead> | Argues the necessity of shifting toward programmatic optimization (like DSPy) over manual hacking. |

---

## Key Concepts Checklist

- **Zero-shot & Few-shot Learning:** Formulating queries where the model infers $P(y|x)$ purely from pretraining vs. mapping $P(y|x, E)$ where $E$ is a set of $k$ examples.
- **Chain-of-Thought (CoT):** Decomposing the generation probability into $P(y, z|x) = P(z|x)P(y|x, z)$ where $z = \{z_1, z_2, \dots, z_n\}$ represents intermediate logical states.
- **Tree of Thoughts (ToT):** Framing reasoning as heuristic search over a tree space, applying algorithmic design (e.g., Divide and Conquer, BFS) to state evaluation.
- **ReAct Pattern:** Interleaving reasoning and acting, formalized as generating sequences of thoughts $t_i$, actions $a_i$, and observations $o_i$ to ground the LLM in external environments.
- **Structured Outputs:** Enforcing schema validity (e.g., JSON) by manipulating the token probability distribution mask during autoregressive decoding.
- **Self-Consistency:** Generating multiple independent CoT paths and applying a marginalization process (usually majority voting) over the final answer space.
- **Programmatic Optimization:** Treating prompts as trainable hyperparameters rather than static strings, utilizing metric-driven compilation (e.g., via DSPy).

---

## Projects / Practice

| Project | Description |
|---|---|
| **Graph-Based Automated Reasoning Engine** | Implement a Graph of Thoughts (GoT) reasoning system entirely in Python. Model the reasoning process mathematically as a directed graph where vertices are intermediate thought states and edges are transformations. Use this engine to solve complex statistical programming scenarios, incorporating backtracking and dynamic programming principles for state evaluation. |
| **Agentic Web Scraping MLOps Pipeline** | Construct a scalable, end-to-end data extraction agent. Utilize `Selenium` and `BeautifulSoup` for DOM interaction, but route the parsing logic through a local LLM constrained by `Outlines` to strictly output validated JSON schemas. Deploy this pipeline as a containerized microservice with CI/CD integration, ensuring robust error handling for dynamic JavaScript elements. |
| **Programmatic Prompt Optimization Microservice** | Abandon manual prompt tuning. Build a production-grade text classification API that leverages `DSPy`'s `BootstrapFewShotWithRandomSearch` algorithm. Mathematically optimize your prompt topology by defining a custom metric using `Scikit-learn` (e.g., F1-score) to evaluate outputs over a validation set, compiling the final architecture for high-throughput deployment. |

---

## See also

- [Agentic AI](../visualizers-and-playgrounds/README.md) — Expanding reasoning techniques into autonomous loops and sophisticated tool-calling frameworks.
- [LLM Fundamentals](llm-fundamentals.md) — The underlying transformer architecture, KV-caching, and scaling laws that make these prompting topologies function.
- [MLOps](../visualizers-and-playgrounds/README.md) — Strategies for versioning, evaluating, and deploying these optimized prompt pipelines in production environments.

## References

- [Pre-train, Prompt, and Predict (Liu et al., 2021)](https://arxiv.org/abs/2107.13586)
- [Graph of Thoughts (Besta et al., 2023)](https://arxiv.org/abs/2308.09687)
- [The Prompt Report (White et al., 2023)](https://arxiv.org/abs/2306.11309)