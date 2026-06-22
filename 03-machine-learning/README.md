# 03 — Machine Learning

> From theory to practice: the core algorithms, workflows, and tools that power modern machine learning. This module covers supervised and unsupervised learning, ensemble methods, evaluation, feature engineering, and hands-on frameworks.

**Last Reviewed:** 2026-06

**Prerequisites:** [01 – Foundations](../01-foundations/README.md), [02 – Data Science](../02-data-science/README.md)

---

## Overview

Machine learning is the study of algorithms that improve through experience. This module covers the classical ML toolkit — everything from linear regression to gradient boosting — along with the evaluation practices and feature-engineering techniques needed to apply them effectively.

| Sub‑page | Est. Hours | Priority |
|---|---|---|
| [Supervised Learning](supervised-learning.md) | 15–20 | Essential |
| [Unsupervised Learning](unsupervised-learning.md) | 10–15 | Essential |
| [Ensemble Methods](ensemble-methods.md) | 10–15 | Essential |
| [Model Evaluation](model-evaluation.md) | 8–12 | Essential |
| [Feature Engineering](feature-engineering.md) | 8–12 | Important |
| [Classic ML Frameworks](classic-ml-frameworks.md) | 4–6 | Important |
| [Playgrounds](playgrounds.md) | — | Supplementary |

---

## Prerequisite Map

```
┌─────────────────────────────────────────────┐
│            01 – Foundations                   │
│  (linear algebra, calculus, prob & stats,    │
│   Python, NumPy, pandas)                     │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│            02 – Data Science                 │
│  (wrangling, EDA, statistics, SQL)           │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│          03 – Machine Learning               │
│                                             │
│  Supervised ──► Unsupervised                │
│       │              │                      │
│       ▼              ▼                      │
│  Ensemble ───────► Model Evaluation         │
│       │                    │                │
│       ▼                    ▼                │
│  Feature Engineering  Frameworks            │
│                                    │        │
│                               Playgrounds   │
└─────────────────────────────────────────────┘
```

---

## How to Use

1. Start with **Supervised Learning** — regression and classification are the bedrock.
2. Move to **Unsupervised Learning** for clustering and dimensionality reduction.
3. Study **Ensemble Methods** to boost performance with random forests and gradient boosting.
4. Learn **Model Evaluation** to measure and diagnose your models properly.
5. Practice **Feature Engineering** to get the most out of your data.
6. Explore **Classic ML Frameworks** and **Playgrounds** for hands-on practice.

---

## Reference Textbooks

| Title | Author(s) | Used In |
|---|---|---|
| *The Elements of Statistical Learning* (ESL) | Hastie, Tibshirani, Friedman | All topics |
| *An Introduction to Statistical Learning* (ISLR) | James, Witten, Hastie, Tibshirani | Supervised, Evaluation |
| *Pattern Recognition and Machine Learning* (PRML) | Bishop | Theory-heavy reference |
| *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* | Géron | Frameworks, Practice |
| *Machine Learning Engineering* | Huyen | Feature Engineering, Evaluation |

---

## See also

- [04 – Deep Learning](../04-deep-learning/README.md) — neural network–based approaches (once created)
- [🧩 Visualizers & Playgrounds](../../visualizers-and-playgrounds/README.md) — interactive ML demos
- [Templates / Resource Entry Template](../templates/resource-entry-template.md)
