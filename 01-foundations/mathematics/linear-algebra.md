# Linear Algebra

> The language of data: vectors, matrices, linear transformations, and decompositions. Arguably the most important math topic for ML.

**Last Reviewed:** 2026-06

**Prerequisites:** High‑school algebra · [01 – Foundations / README](../README.md)

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| MIT OCW 18.06 — Lecture Notes | Beginner | https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/pages/lecture-notes/ | Companion notes to Strang's legendary lectures |
| Introduction to Linear Algebra (Strang, 6th ed.) — Textbook Site | Beginner | https://math.mit.edu/~gs/linearalgebra/ila6/indexila6.html | Classic textbook; clear intuition for core concepts |
| The Matrix Cookbook (PDF) | Intermediate | https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf | Handy reference of identities, derivatives, and decompositions |
| Immersive Linear Algebra (Online Book) | Beginner | http://immersivemath.com/ila/index.html | Fully interactive textbook with embedded visualizations |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| 3Blue1Brown — Essence of Linear Algebra | Beginner | https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab | Best-in-class animated intuition for vectors, spans, and transformations |
| MIT 18.06 — Linear Algebra (Gilbert Strang) | Beginner | https://www.youtube.com/playlist?list=PL49CF3715CB9EF31D | Gold-standard full lecture series — 34 lectures |
| StatQuest: Linear Algebra Fundamentals | Beginner | https://www.youtube.com/playlist?list=PLblh5JKOoLUIcdlgu78MnlATeyx4cEVeR | Bite-sized, intuition-first explanations |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| Khan Academy — Linear Algebra | Beginner | https://www.khanacademy.org/math/linear-algebra | Free, self-paced with exercises |
| Mathematics for Machine Learning: Linear Algebra (Coursera / Imperial College) | Beginner | https://www.coursera.org/learn/linear-algebra-machine-learning | Short, practical course focused on ML applications |
| fast.ai — Computational Linear Algebra | Intermediate | https://github.com/fastai/numerical-linear-algebra | Top-down, code-first approach to numerical methods |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| Interactive Linear Algebra (Georgia Tech) | Beginner | https://textbooks.math.gatech.edu/ila/ | Interactive textbook — visualize vectors, spans, and transformations |
| Eigenvectors and Eigenvalues Explained Visually | Beginner | https://setosa.io/ev/eigenvectors-and-eigenvalues/ | Drag-to-explore eigenvalue visualization |
| Matrix Multiplication Visualizer | Beginner | http://matrixmultiplication.xyz/ | Step-through matmul animation |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| Finding Structure with Randomness: Probabilistic Algorithms for Constructing Approximate Matrix Decompositions (Halko, Martinsson, Tropp) | Advanced | https://arxiv.org/abs/0909.4061 | Foundational paper for scalable randomized SVD |
| Attention Is All You Need (Vaswani et al.) | Advanced | https://arxiv.org/abs/1706.03762 | See how linear algebra (matrix multiply, softmax) powers modern Transformers |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| NumPy — Linear Algebra Routines | Beginner | https://numpy.org/doc/stable/reference/routines.linalg.html | Official NumPy reference for linalg operations |
| Scikit-learn — Decomposition | Intermediate | https://scikit-learn.org/stable/modules/decomposition.html | PCA, SVD, NMF and more — practical decompositions |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| A Visual Intro to NumPy and Data Representation (Jay Alammar) | Beginner | https://jalammar.github.io/visual-numpy/ | Rich visual walkthrough of NumPy arrays and operations |
| The SVD — A Geometric Interpretation (Gregory Gundersen) | Intermediate | https://gregorygundersen.com/blog/2018/12/10/svd/ | One of the clearest geometric explanations of SVD |

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
