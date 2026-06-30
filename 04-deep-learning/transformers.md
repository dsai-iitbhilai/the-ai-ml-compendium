# Transformers

> The transformer architecture, self-attention mechanisms, and the foundation models that reshaped NLP and beyond. Covers the original Transformer, BERT, GPT, encoder-decoder models, multimodal transformers, and modern LLM architectures.

**Last Reviewed:** 2026-06

**Prerequisites:** [04 – Deep Learning / README](README.md), [Neural Network Fundamentals](neural-network-fundamentals.md), [RNN & Sequence Models](rnn-sequence-models.md) (recommended)

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| Hugging Face Transformers Documentation | Beginner | <https://huggingface.co/docs/transformers> | Complete documentation with tutorials |
| Dive into Deep Learning — Attention & Transformers | Beginner | <https://d2l.ai/chapter_attention-mechanisms-and-transformers/index.html> | Excellent implementation-first approach |
| Speech and Language Processing (Jurafsky & Martin) | Intermediate | <https://web.stanford.edu/~jurafsky/slp3/> | Gold-standard NLP textbook |
| Illustrated Transformer (Jay Alammar) | Beginner | <https://jalammar.github.io/illustrated-transformer/> | Best visual explanation of transformers |
| Understanding Deep Learning | Intermediate | <https://udlbook.github.io/udlbook/> | Modern explanation of attention mechanisms |

---

### 🎥 Videos

| Title | Level | Link | Notes |
|---|---|---|---|
| 3Blue1Brown — Attention in Transformers | Beginner | <https://youtu.be/eMlx5fFNoYc> | Best visual intuition |
| Andrej Karpathy — Let's Build GPT From Scratch | Intermediate | <https://www.youtube.com/watch?v=kCc8FmEb1nY> | Must-watch implementation |
| Stanford CS224N Transformer Lecture | Intermediate | <https://www.youtube.com/playlist?list=PLoROMvodv4rOSH4v6133s9LFPRHjEmbmJ> | University-quality lectures |
| Yannic Kilcher — Attention Is All You Need | Advanced | <https://www.youtube.com/results?search_query=yannic+kilcher+attention+is+all+you+need> | Detailed paper walkthrough |
| Sebastian Raschka — LLM From Scratch | Intermediate | <https://www.youtube.com/@SebastianRaschka> | Practical transformer implementation |

---

### 🎓 Courses

| Title | Level | Link | Notes |
|---|---|---|---|
| Hugging Face NLP Course | Beginner | <https://huggingface.co/learn/nlp-course> | Best free transformers course |
| Stanford CS224N | Intermediate | <https://web.stanford.edu/class/cs224n/> | Premier NLP course |
| DeepLearning.AI NLP Specialization | Intermediate | <https://www.coursera.org/specializations/natural-language-processing> | Attention, transformers, BERT |
| Fast.ai Practical Deep Learning | Beginner | <https://course.fast.ai/> | Uses transformers in practice |
| Full Stack Deep Learning | Advanced | <https://fullstackdeeplearning.com/> | Production LLM systems |

---

### 🕹️ Interactive Visualizers

| Title | Level | Link | Notes |
|---|---|---|---|
| Transformer Explainer (Poloclub) | Beginner | <https://poloclub.github.io/transformer-explainer/> | Interactive transformer visualization |
| BertViz | Beginner | <https://github.com/jessevig/bertviz> | Visualize attention heads |
| TensorFlow Playground | Beginner | <https://playground.tensorflow.org> | Neural network intuition |
| Attention Visualizer | Intermediate | <https://bbycroft.net/llm> | Interactive LLM visualization |
| LLM Visualization | Intermediate | <https://jalammar.github.io/illustrated-transformer/> | Step-by-step diagrams |

---

### 📄 Papers

| Title | Level | Link | Notes |
|---|---|---|---|
| Attention Is All You Need (2017) | Intermediate | <https://arxiv.org/abs/1706.03762> | Original Transformer paper |
| BERT (2018) | Intermediate | <https://arxiv.org/abs/1810.04805> | Bidirectional encoder |
| GPT-2 (2019) | Intermediate | <https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf> | Large-scale autoregressive LM |
| Language Models are Few-Shot Learners (GPT-3) | Advanced | <https://arxiv.org/abs/2005.14165> | GPT-3 |
| RoFormer (RoPE) | Advanced | <https://arxiv.org/abs/2104.09864> | Rotary Position Embeddings |
| FlashAttention | Advanced | <https://arxiv.org/abs/2205.14135> | Efficient attention |
| LLaMA | Advanced | <https://arxiv.org/abs/2302.13971> | Meta's foundation model |
| LoRA | Intermediate | <https://arxiv.org/abs/2106.09685> | Efficient fine-tuning |

---

### 💻 Code & Notebooks

| Title | Level | Link | Notes |
|---|---|---|---|
| The Annotated Transformer | Intermediate | <https://nlp.seas.harvard.edu/annotated-transformer/> | Best line-by-line implementation |
| nanoGPT | Intermediate | <https://github.com/karpathy/nanoGPT> | Minimal GPT implementation |
| minGPT | Intermediate | <https://github.com/karpathy/minGPT> | Educational GPT |
| Hugging Face Course Notebooks | Beginner | <https://github.com/huggingface/course> | Companion notebooks |
| Transformers Examples | Intermediate | <https://github.com/huggingface/transformers/tree/main/examples> | Official training scripts |
| LLM From Scratch | Intermediate | <https://github.com/rasbt/LLMs-from-scratch> | Build GPT from scratch |

---

### 📰 Blogs & Articles

| Title | Level | Link | Notes |
|---|---|---|---|
| Illustrated Transformer | Beginner | <https://jalammar.github.io/illustrated-transformer/> | Classic visual guide |
| Illustrated GPT-2 | Beginner | <https://jalammar.github.io/illustrated-gpt2/> | GPT architecture explained |
| Illustrated BERT | Beginner | <https://jalammar.github.io/illustrated-bert/> | BERT intuition |
| Transformer Family Tree | Intermediate | <https://lilianweng.github.io/posts/2020-04-07-the-transformer-family/> | Evolution of transformer models |
| Lilian Weng's LLM Blog | Advanced | <https://lilianweng.github.io/> | Excellent deep dives |
| Sebastian Raschka Blog | Intermediate | <https://sebastianraschka.com/blog/> | Modern LLM tutorials |

---

## Key Concepts Checklist

### Foundations

- Why RNNs struggle with long sequences
- Attention intuition
- Self-attention
- Query, Key, Value
- Scaled dot-product attention
- Multi-head attention
- Positional encoding
- Residual connections
- Layer normalization
- Feed-forward networks

### Transformer Architectures

- Encoder
- Decoder
- Encoder-decoder
- BERT architecture
- GPT architecture
- T5 architecture

### Training

- Masked Language Modeling (MLM)
- Causal Language Modeling (CLM)
- Next Sentence Prediction
- Teacher forcing
- Fine-tuning
- Transfer learning

### Modern LLM Techniques

- RoPE
- KV Cache
- Flash Attention
- LoRA
- QLoRA
- PEFT
- Quantization
- RLHF
- DPO

### Applications

- Text classification
- Summarization
- Translation
- Question answering
- Text generation
- Code generation
- Vision Transformers (ViT)
- Multimodal Transformers

---

## Projects / Practice

| Project | Description |
|------|------|
| Self-Attention from Scratch | Implement attention in NumPy |
| Transformer from Scratch | Build encoder and decoder using PyTorch |
| Character-Level GPT | Train nanoGPT on Shakespeare |
| Fine-tune BERT | Sentiment classification with Hugging Face |
| Fine-tune Llama using LoRA | Parameter-efficient fine-tuning |
| Build a Chatbot | Create an instruction-following assistant |
| Document Question Answering | Retrieval + Transformer |
| Vision Transformer Classifier | Train ViT on CIFAR-10 |

---

## See also

- [RNN & Sequence Models](rnn-sequence-models.md) — predecessors to attention
- [LLMs & Generative AI](../visualizers-and-playgrounds/README.md) — prompt engineering, instruction tuning, RLHF
- [Frameworks](frameworks.md) — PyTorch, Hugging Face, TensorFlow
- [MLOps](../07-mlops-and-deployment/README.md) — deploying transformer models
- [Visualizers](visualizers.md) — attention visualizers and interactive transformer demos