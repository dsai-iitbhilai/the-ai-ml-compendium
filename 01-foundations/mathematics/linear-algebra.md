# Linear Algebra

> The language of data: vectors, matrices, linear transformations, and decompositions. Arguably the most important math topic for ML.

**Last Reviewed:** 2026-06

**Prerequisites:** High‑school algebra · [01 – Foundations / README](../README.md)

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| *Linear Algebra and Its Applications* (Strang, 6th ed.) | Beginner | [Link](https://example.com/strang-linalg) | Classic textbook; clear intuition |
| MIT OCW *Linear Algebra* lecture notes | Intermediate | [Link](https://example.com/mit-ocw-la) | Companion to Strang's lectures |
| *The Matrix Cookbook* | Intermediate | [Link](https://example.com/matrix-cookbook) | Handy reference of identities and derivatives |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| MIT 18.06 — Linear Algebra (Gilbert Strang) | Beginner | [Link](https://example.com/mit-18-06) | Gold‑standard lecture series |
| 3Blue1Brown — Essence of Linear Algebra | Beginner | [Link](https://example.com/3b1b-la) | Animated intuition for core concepts |
| Linear Algebra for Machine Learning (YouTube playlist) | Intermediate | [Link](https://example.com/la-ml-playlist) | Focused on ML applications |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| Linear Algebra — Khan Academy | Beginner | [Link](https://example.com/khan-la) | Free, self‑paced |
| Imperial College — Mathematics for Machine Learning: Linear Algebra (Coursera) | Beginner | [Link](https://example.com/imperial-la) | Short, practical course |
| Stanford CS229 – Linear Algebra Review | Intermediate | [Link](https://example.com/cs229-la-review) | Concise review notes for ML |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| Interactive Linear Algebra (Georgia Tech) | Beginner | [Link](https://example.com/gt-interactive-la) | Visualize vectors, spans, and transformations |
| Matrix Multiplication Visualizer | Beginner | [Link](https://example.com/matmul-viz) | Step‑through matmul animation |
| Eigendecomposition Explorer | Intermediate | [Link](https://example.com/eigen-viz) | Play with eigenvalues and eigenvectors |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *Eigendecomposition vs. SVD* (tutorial) | Intermediate | [Link](https://example.com/eig-vs-svd) | Clear comparison of the two factorisations |
| *Randomized SVD* (Halko, Martinsson, Tropp) | Advanced | [Link](https://example.com/rand-svd) | Foundational paper for scalable SVD |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| NumPy Linear Algebra Quickstart | Beginner | [Link](https://example.com/numpy-la) | Official NumPy tutorial |
| Implementing PCA from Scratch | Intermediate | [Link](https://example.com/pca-scratch) | Notebook tying SVD to PCA |
| Autograd & Jacobians with JAX | Advanced | [Link](https://example.com/jax-autograd) | Compute higher‑order derivatives |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *Understanding the Dot Product* | Beginner | [Link](https://example.com/dot-product-blog) | Friendly walk‑through |
| *The Singular Value Decomposition (SVD) — A Geometric View* | Intermediate | [Link](https://example.com/svd-geometric) | Blog with rich diagrams |

---

## Key Concepts Checklist

- [ ] Vector spaces, subspaces, span, basis
- [ ] Linear transformations and their matrix representations
- [ ] Matrix multiplication (interpretations and properties)
- [ ] Determinant, trace, rank
- [ ] Systems of linear equations (Gaussian elimination, LU decomposition)
- [ ] Orthogonality, projections, Gram–Schmidt
- [ ] Eigenvalues and eigenvectors
- [ ] Singular Value Decomposition (SVD)
- [ ] Principal Component Analysis (PCA)
- [ ] Norms (L1, L2, Frobenius)

---

## Projects / Practice

| Project | Description |
|---|---|
| Image Compression with SVD | Compress a grayscale image by keeping only the top‑k singular values |
| Linear Regression via Normal Equation | Solve $w = (X^T X)^{-1} X^T y$ from scratch |
| PageRank Mini | Implement a simplified PageRank using eigendecomposition |

---

## See also

- [Calculus](calculus.md) — needed for understanding gradient‑based methods that build on linear algebra
- [Optimization](optimization.md) — convexity and descent methods rely heavily on vector spaces
- [🔢 Mathematics](../README.md) — back to mathematics index
- [🏠 Foundations / README](../README.md)
