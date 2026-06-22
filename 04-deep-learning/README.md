# 04 — Deep Learning

> Neural networks at scale: from the perceptron through transformers. This module covers the architecture, theory, and practice of deep learning, including CNNs, RNNs, transformers, and the frameworks used to build them.

**Last Reviewed:** 2026-06

**Prerequisites:** [01 – Foundations](../01-foundations/README.md), [03 – Machine Learning](../03-machine-learning/README.md)

---

## Overview

Deep learning extends classical machine learning with multi-layer neural networks capable of learning hierarchical representations. This module covers the fundamental building blocks — backpropagation, activation functions, and gradient-based optimization — then builds up to modern architectures including CNNs, RNNs/LSTMs, and transformers.

| Sub‑page | Est. Hours | Priority |
|---|---|---|
| [Neural Network Fundamentals](neural-network-fundamentals.md) | 12–18 | Essential |
| [CNN & Computer Vision](cnn-computer-vision.md) | 15–20 | Essential |
| [RNN & Sequence Models](rnn-sequence-models.md) | 10–15 | Important |
| [Transformers](transformers.md) | 15–20 | Essential |
| [Frameworks](frameworks.md) | 8–12 | Essential |
| [Visualizers](visualizers.md) | — | Supplementary |

---

## Prerequisite Map

```
┌─────────────────────────────────────────────┐
│            01 – Foundations                   │
│  (linear algebra, calculus, prob & stats,    │
│   Python, NumPy, pandas, optimization)       │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│            03 – Machine Learning             │
│  (supervised learning, model evaluation,     │
│   feature engineering)                       │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│          04 – Deep Learning                  │
│                                             │
│  Neural Net Fundamentals                    │
│       │                                     │
│       ├────► CNN & Computer Vision          │
│       ├────► RNN & Sequence Models          │
│       │            │                        │
│       │            ▼                        │
│       ├────► Transformers                   │
│       │                                     │
│       ├────► Frameworks                     │
│       └────► Visualizers                    │
└─────────────────────────────────────────────┘
```

---

## How to Use

1. Start with **Neural Network Fundamentals** — the perceptron, backpropagation, and gradient descent are essential for everything that follows.
2. Study **CNN & Computer Vision** for spatial data and image tasks.
3. Study **RNN & Sequence Models** for temporal or sequential data.
4. Move to **Transformers** — the dominant architecture for NLP and beyond.
5. Practice with **Frameworks** (PyTorch, TensorFlow, JAX) to implement what you learn.
6. Explore **Visualizers** for interactive intuition throughout.

---

## Reference Textbooks

| Title | Author(s) | Used In |
|---|---|---|
| *Deep Learning* (The Deep Learning Book) | Goodfellow, Bengio, Courville | All topics |
| *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* | Géron | Frameworks, CNNs, RNNs |
| *Deep Learning with Python* | Chollet | Keras/TF focus, CV, NLP |
| *Understanding Deep Learning* | Prince | Theory, transformers, attention |
| *Speech and Language Processing* | Jurafsky & Martin | RNNs, Transformers (NLP focus) |
| *Dive into Deep Learning* | Zhang, Lipton, Li, Smola | Code-first interactive textbook |

---

## See also

- [05 – Reinforcement Learning](../05-reinforcement-learning/README.md) — deep RL extensions (once created)
- [🧩 Visualizers & Playgrounds](../../visualizers-and-playgrounds/README.md) — interactive DL demos
- [Templates / Resource Entry Template](../templates/resource-entry-template.md)
