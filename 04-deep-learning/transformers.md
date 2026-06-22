# Transformers

> The transformer architecture, self-attention mechanisms, and the foundation models that reshaped NLP and beyond. Covers the original Transformer, BERT, GPT, and modern variants.

**Last Reviewed:** 2026-06

**Prerequisites:** [04 – Deep Learning / README](README.md), [Neural Network Fundamentals](neural-network-fundamentals.md), [RNN & Sequence Models](rnn-sequence-models.md) (recommended)

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| *Understanding Deep Learning* — Chapters 11–12 (Prince) | Intermediate | [Link](https://example.com/udl-ch11-12) | Modern treatment of attention and transformers |
| *Dive into Deep Learning* — Chapter 11 (Attention & Transformers) | Intermediate | [Link](https://example.com/d2l-attention) | Code-first: implement attention, transformer, BERT |
| *Speech and Language Processing* — Chapter 9 (Jurafsky & Martin) | Intermediate | [Link](https://example.com/slp-ch9) | NLP-focused transformer coverage |
| Hugging Face — *Transformers Documentation* | Beginner | [Link](https://example.com/hf-transformers-docs) | Practical API reference |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| 3Blue1Brown — *Attention in Transformers, Visually Explained* | Beginner | [Link](https://example.com/3b1b-attention) | Best visual intuition for self-attention |
| Stanford CS224n — *Transformer Lectures (2023)* | Intermediate | [Link](https://example.com/cs224n-transformer) | In-depth university lecture on the Transformer |
| Yannic Kilcher — *Attention is All You Need* (Paper Walkthrough) | Intermediate | [Link](https://example.com/yk-attention-paper) | Detailed breakdown of the original transformer paper |
| Andrej Karpathy — *Let's build GPT from scratch* | Advanced | [Link](https://example.com/karpathy-gpt-scratch) | Build a GPT-style transformer line by line |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| Coursera — *Natural Language Processing with Attention Models* (DeepLearning.AI) | Intermediate | [Link](https://example.com/coursera-attention) | Covers attention, transformers, T5, BERT |
| Hugging Face — *NLP Course* (Transformers) | Beginner | [Link](https://example.com/hf-course) | Fine-tune pre-trained models on real tasks |
| Stanford CS224n — *Full Course (2024)* | Intermediate | [Link](https://example.com/cs224n-2024) | Cutting-edge NLP course with transformer focus |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| BertViz — *Attention Visualization* | Beginner | [Link](https://example.com/bertviz) | Interactive attention head visualization |
| Transformer Explainer (Poloclub) | Beginner | [Link](https://example.com/transformer-explainer) | Step-through of the full transformer architecture |
| *The Illustrated Transformer* (Jay Alammar) | Beginner | [Link](https://example.com/illustrated-transformer) | Animated diagrams of attention, multi-head, positional encoding |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *Attention is All You Need* (Vaswani et al., 2017) | Intermediate | [Link](https://example.com/attention-paper) | The original Transformer paper — foundational reading |
| *BERT: Pre-training of Deep Bidirectional Transformers* (Devlin et al., 2019) | Intermediate | [Link](https://example.com/bert-paper) | Bidirectional pre-training for language understanding |
| *Language Models are Few-Shot Learners* (Brown et al., 2020) | Advanced | [Link](https://example.com/gpt3-paper) | GPT-3 scaling laws and in-context learning |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| *The Annotated Transformer* (Harvard NLP) | Intermediate | [Link](https://example.com/annotated-transformer) | Line-by-line implementation of Transformer in PyTorch |
| nanoGPT (Andrej Karpathy) | Advanced | [Link](https://example.com/nanogpt) | Minimal, clean GPT implementation for training and fine-tuning |
| Hugging Face — *Fine-tune BERT for Text Classification* | Beginner | [Link](https://example.com/hf-bert-finetune) | Quick tutorial using the transformers library |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *The Illustrated Transformer* (Jay Alammar) | Beginner | [Link](https://example.com/illustrated-transformer-blog) | Visual guide that complements the paper |
| *The Illustrated BERT, ELMo, and co.* (Jay Alammar) | Beginner | [Link](https://example.com/illustrated-bert) | How BERT builds on the transformer |
| *Transformers from Scratch* (Peter Bloem) | Intermediate | [Link](https://example.com/transformers-scratch) | Clear blog series implementing a transformer in PyTorch |

---

## Key Concepts Checklist

- [ ] Self-attention mechanism (Q, K, V; scaled dot-product)
- [ ] Multi-head attention
- [ ] Positional encoding (sinusoidal, learned, RoPE)
- [ ] Transformer encoder (Bidirectional, BERT-style)
- [ ] Transformer decoder (Causal masking, GPT-style)
- [ ] Encoder-decoder Transformer (Original, T5-style)
- [ ] Layer normalization and residual connections in transformers
- [ ] Pre-training objectives (MLM, autoregressive, prefix LM)
- [ ] Fine-tuning and transfer learning
- [ ] Scaling laws and emergent abilities
- [ ] Efficient attention variants (Flash Attention, Linformer)

---

## Projects / Practice

| Project | Description |
|---|---|
| Implement a Transformer from scratch | Build a small character-level transformer for text generation |
| Fine-tune BERT on a classification task | Use Hugging Face to fine-tune for sentiment or topic classification |
| Pre-train a small GPT | Train a nanoGPT on a small corpus; observe scaling with size and data |

---

## See also

- [RNN & Sequence Models](rnn-sequence-models.md) — the predecessors to transformers
- [Frameworks](frameworks.md) — Hugging Face, PyTorch for transformer development
- [Visualizers](visualizers.md) — BertViz, Transformer Explainer for interactive exploration
