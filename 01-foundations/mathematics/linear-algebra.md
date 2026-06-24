# Linear Algebra

> The language of data: vectors, matrices, linear transformations, and decompositions. Arguably the most important math topic for ML.

**Last Reviewed:** 2026-06

**Prerequisites:** High‑school algebra · [01 – Foundations / README](../README.md)

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| *Linear Algebra and Its Applications* (Strang, 6th ed.) | Beginner | https://www.cengage.com/c/linear-algebra-and-its-applications-6e-strang/9780357764626/ | Classic textbook; clear intuition (Paid) |
| MIT OCW *Linear Algebra* lecture notes | Intermediate | https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/ | Companion to Strang's lectures |
| *The Matrix Cookbook* | Intermediate | https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf | Handy reference of identities and derivatives |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| MIT 18.06 — Linear Algebra (Gilbert Strang) | Beginner | https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/ | Gold-standard lecture series |
| 3Blue1Brown — Essence of Linear Algebra | Beginner | https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr | Animated intuition for core concepts |
| Linear Algebra for Machine Learning (YouTube playlist) | Intermediate | https://www.youtube.com/playlist?list=PLEiEAq2VkUULgQ9M2RieQh-vUyn3jQj7A | Focused on ML applications |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| Linear Algebra — Khan Academy | Beginner | https://www.khanacademy.org/math/linear-algebra | Free, self-paced |
| Imperial College — Mathematics for Machine Learning: Linear Algebra (Coursera) | Beginner | https://www.coursera.org/learn/linear-algebra-machine-learning | Short, practical course |
| Stanford CS229 – Linear Algebra Review | Intermediate | https://cs229.stanford.edu/section/cs229-linalg.pdf | Concise review notes for ML |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| Interactive Linear Algebra (Georgia Tech) | Beginner | https://textbooks.math.gatech.edu/ila/ | Visualize vectors, spans, and transformations |
| Matrix Multiplication Visualizer | Beginner | https://academo.org/demos/matrix-multiplication/ | Step-through matrix multiplication |
| Eigendecomposition Explorer | Intermediate | https://setosa.io/ev/eigenvectors-and-eigenvalues/ | Interactive eigenvalue/eigenvector exploration |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *Eigendecomposition vs. SVD* (tutorial) | Intermediate | https://web.stanford.edu/class/cs168/l/l9.pdf | Clear comparison of the two factorisations |
| *Finding Structure with Randomness: Probabilistic Algorithms for Constructing Approximate Matrix Decompositions* (Halko, Martinsson, Tropp) | Advanced | https://arxiv.org/abs/0909.4061 | Foundational paper for scalable SVD |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| NumPy Linear Algebra Quickstart | Beginner | https://numpy.org/doc/stable/reference/routines.linalg.html | Official NumPy linear algebra documentation |
| Implementing PCA from Scratch | Intermediate | https://github.com/eriklindernoren/ML-From-Scratch/blob/master/mlfromscratch/unsupervised_learning/principal_component_analysis.py | Ties SVD to PCA |
| Autograd & Jacobians with JAX | Advanced | https://jax.readthedocs.io/en/latest/advanced-autodiff.html | Compute higher-order derivatives |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *Understanding the Dot Product* | Beginner | https://betterexplained.com/articles/vector-calculus-understanding-the-dot-product/ | Friendly walk-through |
| *The Singular Value Decomposition (SVD) — A Geometric View* | Intermediate | https://setosa.io/ev/singular-value-decomposition/ | Rich geometric intuition and diagrams |

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
