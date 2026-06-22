# 01 — Foundations

> Solid grounding in the mathematical and programming fundamentals required for AI/ML. Master these before proceeding to later modules.

**Last Reviewed:** 2026-06

---

## Overview

This module covers the core prerequisites for understanding modern machine learning: linear algebra, calculus, probability & statistics, optimization, and the programming skills needed to implement algorithms.

| Sub‑page | Est. Hours | Priority |
|---|---|---|
| [Mathematics / Linear Algebra](mathematics/linear-algebra.md) | 20–30 | Essential |
| [Mathematics / Calculus](mathematics/calculus.md) | 15–25 | Essential |
| [Mathematics / Probability & Statistics](mathematics/probability-statistics.md) | 12–20 | Essential |
| [Mathematics / Optimization](mathematics/optimization.md) | 8–12 | Important |
| [Programming / Python for AI](programming/python-for-ai.md) | 10–15 | Essential |
| [Programming / Data Structures & Algorithms](programming/data-structures-algorithms.md) | 8–12 | Helpful |
| [🧩 Visualizers](visualizers.md) | — | Supplementary |

---

## Prerequisite Map

```
┌──────────────────────────────────────────────────────────────┐
│                 High‑School Math & Basic Coding               │
└───────────┬──────────────────────────────┬───────────────────┘
            │                              │
            ▼                              ▼
┌──────────────────────┐     ┌──────────────────────────────┐
│   Linear Algebra      │     │  Python for AI                │
│   (vectors, matrices, │     │  (NumPy, pandas, matplotlib)  │
│    eigendecomposition)│     │                              │
└──────────┬────────────┘     └──────────────┬───────────────┘
           │                                 │
           ▼                                 ▼
┌──────────────────────┐     ┌──────────────────────────────┐
│   Calculus            │     │  Data Structures & Algos      │
│   (derivatives,       │     │  (arrays, hash tables,        │
│    gradients, chain   │     │   recursion, big‑O)           │
│    rule)              │     │                              │
└──────────┬────────────┘     └──────────────┬───────────────┘
           │                                 │
           ▼                                 ▼
┌──────────────────────┐     ┌──────────────────────────────┐
│ Probability & Stats   │     │  Optimization                 │
│ (distributions,       │◄────┤  (gradient descent,           │
│  Bayes, hypothesis    │     │   convexity, constrained)     │
│  testing)             │     │                              │
└──────────┬────────────┘     └──────────────┬───────────────┘
           │                                 │
           └─────────────┬───────────────────┘
                         ▼
          ┌──────────────────────────────────┐
          │    02 – Supervised Learning       │
          └──────────────────────────────────┘
```

All sub‑pages link back here. Visualizers can be used alongside any topic.

---

## How to Use

1. Start with **Linear Algebra** and **Python for AI** if you are new.
2. Work through **Calculus** and **Probability & Statistics** next.
3. Finish with **Optimization** and optionally **DSA**.
4. Use the [🧩 Visualizers](visualizers.md) anytime you need an interactive intuition builder.

---

## Reference Textbooks

| Title | Author(s) | Used In |
|---|---|---|
| *Linear Algebra and Its Applications* | Strang | Linear Algebra |
| *Calculus: Early Transcendentals* | Stewart | Calculus |
| *Probability and Statistics for Engineers and Scientists* | Walpole et al. | Probability & Stats |
| *Convex Optimization* | Boyd & Vandenberghe | Optimization |
| *Python Data Science Handbook* | VanderPlas | Python for AI |
| *Introduction to Algorithms* (CLRS) | Cormen et al. | DSA |

---

## See also

- [NN SVG](https://nn-svg.example.com) — interactive neural net diagrams
- [03 – Deep Learning](../03-deep-learning/README.md) (once created)
