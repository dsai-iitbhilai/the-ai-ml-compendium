# LLM Fundamentals

Large Language Models (LLMs) are transformer-based neural networks trained on vast text corpora. This file covers their architecture (decoder-only, encoder-decoder), training pipeline (pretraining → SFT → RLHF), scaling laws, tokenization strategies, and inference mechanics.

## Resources

| Category | Title | Description | Level | Last Reviewed |
|----------|-------|-------------|-------|---------------|
| 📘 Docs | [HuggingFace NLP Course — Transformers](https://huggingface.co/learn/nlp-course/chapter1/1) | Comprehensive walkthrough of the Transformer architecture and how LLMs work under the hood | Beginner | 2026-06 |
| 📄 Paper | [Scaling Laws for Neural Language Models (Kaplan et al., 2020)](https://arxiv.org/abs/2001.08361) | Foundational paper establishing power-law scaling relationships between model size, data, and compute | Intermediate | 2026-06 |
| 📄 Paper | [Hopfield Networks is All You Need (Ramsauer et al., 2020)](https://arxiv.org/abs/2008.02217) | Connects modern Hopfield networks to transformer attention, providing a theoretical lens | Advanced | 2026-06 |
| 🎓 Course | [Stanford CS224N — Transformers & Pretraining](https://web.stanford.edu/class/cs224n/) | Lecture series covering the evolution from RNNs to GPT-family architectures | Intermediate | 2026-06 |
| 💻 Code/Notebook | [llama.cpu — inference in pure C](https://github.com/example/llama.cpu) | Minimal CPU-based inference engine demonstrating tokenization, KV-cache, and sampling | Advanced | 2026-06 |
| 📰 Blog | [Illustrated Transformer (Jay Alammar)](https://jalammar.github.io/illustrated-transformer/) | Visual deep-dive into attention, multi-head attention, and positional encodings | Beginner | 2026-06 |
| 🎥 Video | [3Blue1Brown — Transformers & Attention](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) | Intuitive animated explanation of attention mechanisms and transformer blocks | Beginner | 2026-06 |

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Decoder-only** | Autoregressive architecture (GPT family); predicts next token given previous tokens |
| **Encoder-decoder** | Sequence-to-sequence architecture (T5, BART); separate encoder reads input, decoder generates |
| **Pretraining** | Language modeling objective on trillions of tokens (next-token prediction / masked LM) |
| **Scaling laws** | Predictable improvement in loss with increases in parameters, data, and compute |
| **Tokenization** | Subword splitting (BPE, SentencePiece, tiktoken) mapping text to vocabulary IDs |
| **KV-cache** | Caching key/value tensors during autoregressive decoding to avoid recomputation |
| **Temperature / Top-p** | Sampling parameters controlling output randomness and diversity |
| **Context window** | Maximum number of tokens the model can attend to in a single forward pass |

## Training Pipeline Stages

1. **Pretraining** — next-token prediction on diverse internet-scale corpora (compute-intensive)
2. **Supervised Fine-Tuning (SFT)** — instruction-following on human-written demonstrations
3. **Reward Modeling (RM)** — train a model to score output quality
4. **Reinforcement Learning from Human Feedback (RLHF)** — optimize the LLM against the reward model (PPO / DPO)

## References

- [Attention Is All You Need (Vaswani et al., 2017)](https://arxiv.org/abs/1706.03762)
- [Training Language Models to Follow Instructions (Ouyang et al., 2022)](https://arxiv.org/abs/2203.02155)
- [The Annotated Transformer (Harvard NLP)](https://nlp.seas.harvard.edu/2018/04/03/attention.html)
