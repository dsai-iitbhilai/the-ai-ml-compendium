# Linear Algebra

> The language of data: vectors, matrices, linear transformations, and decompositions. Arguably the most important math topic for ML.

**Last Reviewed:** 2026-06

**Prerequisites:** High‑school algebra · [01 – Foundations / README](../README.md)

---

## Resources

### 📘 Docs & Textbooks

| Resource | Type | Level | Last Reviewed | Notes |
|---|---|---|---|---|
| [MIT OCW 18.06 — Lecture Notes](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/pages/lecture-notes/) | 📘 Docs | Beginner | 2026-06 | Companion notes to Strang's legendary lectures |
| [Introduction to Linear Algebra (Strang, 6th ed.) — Textbook Site](https://math.mit.edu/~gs/linearalgebra/ila6/indexila6.html) | 📘 Docs | Beginner | 2026-06 | Classic textbook; clear intuition for core concepts |
| [The Matrix Cookbook (PDF)](https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf) | 📘 Docs | Intermediate | 2026-06 | Handy reference of identities, derivatives, and decompositions |
| [Immersive Linear Algebra (Online Book)](http://immersivemath.com/ila/index.html) | 📘 Docs | Beginner | 2026-06 | Fully interactive textbook with embedded visualizations |

### 🎥 Video

| Resource | Type | Level | Last Reviewed | Notes |
|---|---|---|---|---|
| [3Blue1Brown — Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) | 🎥 Video | Beginner | 2026-06 | Best-in-class animated intuition for vectors, spans, and transformations |
| [MIT 18.06 — Linear Algebra (Gilbert Strang)](https://www.youtube.com/playlist?list=PL49CF3715CB9EF31D) | 🎥 Video | Beginner | 2026-06 | Gold-standard full lecture series — 34 lectures |
| [StatQuest: Linear Algebra Fundamentals](https://www.youtube.com/playlist?list=PLblh5JKOoLUIcdlgu78MnlATeyx4cEVeR) | 🎥 Video | Beginner | 2026-06 | Bite-sized, intuition-first explanations |

### 🎓 Course

| Resource | Type | Level | Last Reviewed | Notes |
|---|---|---|---|---|
| [Khan Academy — Linear Algebra](https://www.khanacademy.org/math/linear-algebra) | 🎓 Course | Beginner | 2026-06 | Free, self-paced with exercises |
| [Mathematics for Machine Learning: Linear Algebra (Coursera / Imperial College)](https://www.coursera.org/learn/linear-algebra-machine-learning) | 🎓 Course | Beginner | 2026-06 | Short, practical course focused on ML applications |
| [fast.ai — Computational Linear Algebra](https://github.com/fastai/numerical-linear-algebra) | 🎓 Course | Intermediate | 2026-06 | Top-down, code-first approach to numerical methods |

### 🕹️ Visualizer / Playground

| Resource | Type | Level | Last Reviewed | Notes |
|---|---|---|---|---|
| [Interactive Linear Algebra (Georgia Tech)](https://textbooks.math.gatech.edu/ila/) | 🕹️ Visualizer/Playground | Beginner | 2026-06 | Interactive textbook — visualize vectors, spans, and transformations |
| [Eigenvectors and Eigenvalues Explained Visually](https://setosa.io/ev/eigenvectors-and-eigenvalues/) | 🕹️ Visualizer/Playground | Beginner | 2026-06 | Drag-to-explore eigenvalue visualization |
| [Matrix Multiplication Visualizer](http://matrixmultiplication.xyz/) | 🕹️ Visualizer/Playground | Beginner | 2026-06 | Step-through matmul animation |

### 📄 Paper

| Resource | Type | Level | Last Reviewed | Notes |
|---|---|---|---|---|
| [Finding Structure with Randomness: Probabilistic Algorithms for Constructing Approximate Matrix Decompositions (Halko, Martinsson, Tropp)](https://arxiv.org/abs/0909.4061) | 📄 Paper | Advanced | 2026-06 | Foundational paper for scalable randomized SVD |
| [Attention Is All You Need (Vaswani et al.)](https://arxiv.org/abs/1706.03762) | 📄 Paper | Advanced | 2026-06 | See how linear algebra (matrix multiply, softmax) powers modern Transformers |

### 💻 Code / Notebook

| Resource | Type | Level | Last Reviewed | Notes |
|---|---|---|---|---|
| [NumPy — Linear Algebra Routines](https://numpy.org/doc/stable/reference/routines.linalg.html) | 💻 Code/Notebook | Beginner | 2026-06 | Official NumPy reference for linalg operations |
| [Scikit-learn — Decomposition](https://scikit-learn.org/stable/modules/decomposition.html) | 💻 Code/Notebook | Intermediate | 2026-06 | PCA, SVD, NMF and more — practical decompositions |

### 📰 Blog

| Resource | Type | Level | Last Reviewed | Notes |
|---|---|---|---|---|
| [A Visual Intro to NumPy and Data Representation (Jay Alammar)](https://jalammar.github.io/visual-numpy/) | 📰 Blog | Beginner | 2026-06 | Rich visual walkthrough of NumPy arrays and operations |
| [The SVD — A Geometric Interpretation (Gregory Gundersen)](https://gregorygundersen.com/blog/2018/12/10/svd/) | 📰 Blog | Intermediate | 2026-06 | One of the clearest geometric explanations of SVD |

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
