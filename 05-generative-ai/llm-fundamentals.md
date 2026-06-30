# LLM Fundamentals

> Large Language Models (LLMs) are transformer-based neural networks trained on vast text corpora. This file covers their architecture (decoder-only, encoder-decoder), training pipeline (pretraining → SFT → RLHF), scaling laws, tokenization strategies, and inference mechanics.

**Last Reviewed:** 2026-06

**Prerequisites:** [Deep Learning](../visualizers-and-playgrounds/README.md) · Linear Algebra · Multivariate Calculus

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| *HuggingFace NLP Course — Transformers* | Beginner | <https://huggingface.co/learn/nlp-course/chapter1/1> | Comprehensive walkthrough of how LLMs work under the hood |
| *Understanding Deep Learning* (Simon J.D. Prince) | Advanced | <https://udlbook.github.io/udlbook/> | Exceptional, uncompromising mathematical breakdowns of transformer architecture |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| *Attention in Transformers* (3Blue1Brown) | Beginner | <https://www.youtube.com/watch?v=eMlx5fFNoYc> | Intuitive visual explanation of attention mechanisms |
| *Let's build GPT: from scratch, in code* (Andrej Karpathy) | Intermediate | <https://www.youtube.com/watch?v=kCc8FmEb1nY> | Step-by-step implementation of a transformer-based language model |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| *Stanford CS224N — NLP with Deep Learning* | Intermediate | <https://web.stanford.edu/class/cs224n/> | Foundational university lectures on GPT-family architectures |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| *LLM Visualization* (bbycroft) | Intermediate | <https://bbycroft.net/llm> | 3D interactive explorer of the exact tensor transformations in GPT architectures |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *Attention Is All You Need* (Vaswani et al., 2017) | Intermediate | <https://arxiv.org/abs/1706.03762> | The seminal paper introducing the transformer architecture |
| *Scaling Laws for Neural Language Models* (Kaplan et al., 2020) | Intermediate | <https://arxiv.org/abs/2001.08361> | Power-law relationships between model size, data, and compute |
| *Training Language Models to Follow Instructions* (Ouyang et al., 2022) | Advanced | <https://arxiv.org/abs/2203.02155> | The InstructGPT paper outlining the SFT and RLHF pipeline |
| *Hopfield Networks is All You Need* (Ramsauer et al., 2020) | Advanced | <https://arxiv.org/abs/2008.02217> | Provides a rigorous theoretical/mathematical lens on transformer attention |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| *llama.cpp* | Advanced | <https://github.com/ggerganov/llama.cpp> | High-performance C/C++ inference engine; explores KV-cache and tokenization at the metal level |
| *vLLM* | Advanced | <https://github.com/vllm-project/vllm> | Scalable LLM serving engine utilizing PagedAttention for production MLOps environments |
| *nanoGPT* | Intermediate | <https://github.com/karpathy/nanoGPT> | The simplest, fastest PyTorch repository for training/finetuning medium-sized GPTs |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *The Illustrated Transformer* (Jay Alammar) | Beginner | <https://jalammar.github.io/illustrated-transformer/> | Visual deep-dive into multi-head attention and positional encodings |
| *The Annotated Transformer* (Harvard NLP) | Intermediate | <https://nlp.seas.harvard.edu/2018/04/03/attention.html> | Line-by-line PyTorch implementation of the original Attention paper |

---

## Key Concepts Checklist

- Decoder-only (GPT) vs. Encoder-decoder (T5/BART) architectures
- Pretraining objectives (next-token prediction vs. masked language modeling)
- Scaling laws (predictable loss improvements via parameters, data, compute)
- Tokenization algorithms (BPE, SentencePiece, tiktoken)
- Memory optimization: KV-cache during autoregressive decoding
- Positional embeddings (Absolute, RoPE, ALiBi)
- Sampling parameters (Temperature, Top-p, Top-k)

---

## Training Pipeline Stages

1. **Pretraining** — Next-token prediction on diverse, internet-scale corpora (compute-intensive).
2. **Supervised Fine-Tuning (SFT)** — Instruction-following on human-written demonstrations.
3. **Reward Modeling (RM)** — Training a regression model to score output quality based on human preferences.
4. **Alignment (RLHF / DPO)** — Optimizing the LLM against the reward model using reinforcement learning (PPO) or directly optimizing preferences (DPO).

---

## Projects / Practice

| Project | Description |
|---|---|
| **Mathematical Self-Attention Derivation** | Derive the forward and backward passes of scaled dot-product attention entirely from scratch using NumPy, avoiding high-level PyTorch abstractions. |
| **High-Throughput Serving Endpoint** | Deploy an open-source LLM using `vLLM` via Docker. Implement continuous batching and PagedAttention to optimize for high concurrency in a scalable production environment. |
| **End-to-End Alignment Pipeline** | Fine-tune a base model on a custom preference dataset using Direct Preference Optimization (DPO), bypassing standard tutorials to build a robust, deployable alignment pipeline. |

---

## See also

- [Linear Algebra](../docs/01-foundations/mathematics/linear-algebra.md) — The fundamental matrix operations driving attention mechanisms.
- [Agentic AI](../visualizers-and-playgrounds/README.md) — Leveraging LLMs as reasoning engines within autonomous loops and tool-calling frameworks.
- [MLOps](../visualizers-and-playgrounds/README.md) — Scalable engineering practices for deploying and serving heavy machine learning models in production.

## References

- [Attention Is All You Need (Vaswani et al., 2017)](https://arxiv.org/abs/1706.03762)
- [Training Language Models to Follow Instructions (Ouyang et al., 2022)](https://arxiv.org/abs/2203.02155)
- [The Annotated Transformer (Harvard NLP)](https://nlp.seas.harvard.edu/2018/04/03/attention.html)