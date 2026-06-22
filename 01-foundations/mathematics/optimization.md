# Optimization

> Choosing the best element from a set of alternatives — at the heart of almost every ML training algorithm.

**Last Reviewed:** 2026-06

**Prerequisites:** [Calculus](calculus.md) · [Linear Algebra](linear-algebra.md) · [Probability & Statistics](probability-statistics.md) (helpful)

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| *Convex Optimization* (Boyd & Vandenberghe) | Advanced | [Link](https://example.com/boyd-cvx) | The definitive convex opt reference |
| *Numerical Optimization* (Nocedal & Wright) | Advanced | [Link](https://example.com/nocedal-wright) | Comprehensive numerical methods |
| *Algorithms for Optimization* (Kochenderfer & Wheeler) | Intermediate | [Link](https://example.com/kochenderfer-opt) | Modern, accessible, with Julia examples |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| Stanford EE364a — Convex Optimization (Boyd) | Advanced | [Link](https://example.com/ee364a) | Full course with slides and homework |
| Gradient Descent and Variants (StatQuest) | Beginner | [Link](https://example.com/statquest-gd) | Gentle intro to GD, SGD, Adam |
| Why Momentum & Adam Work (DeepLearning.ai) | Intermediate | [Link](https://example.com/andrew-opt) | Clear intuition for modern optimisers |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| Optimization for Machine Learning (MIT 6.881) | Advanced | [Link](https://example.com/mit-6-881) | Advanced but practical |
| Introduction to Optimization (Coursera — Melbourne) | Intermediate | [Link](https://example.com/coursera-opt) | LP, QP, and nonlinear opt |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| Gradient Descent Visualiser | Beginner | [Link](https://example.com/gd-viz) | Watch GD on 2D surfaces |
| Optimisation Sandbox (Distill) | Intermediate | [Link](https://example.com/distill-opt) | Compare SGD, Adam, RMSProp interactively |
| Convex Sets Visualiser | Intermediate | [Link](https://example.com/convex-viz) | Understand convexity intuitively |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *Adam: A Method for Stochastic Optimization* (Kingma & Ba) | Intermediate | [Link](https://example.com/adam-paper) | One of the most cited optimiser papers |
| *Understanding the Difficulty of Training Deep Feedforward Neural Networks* (Glorot & Bengio) | Advanced | [Link](https://example.com/glorot-init) | Connects optimisation and initialisation |
| *Dropout: A Simple Way to Prevent Neural Networks from Overfitting* (Srivastava et al.) | Intermediate | [Link](https://example.com/dropout) | Regularisation as optimisation trick |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| Implementing SGD, Momentum, Adam from Scratch | Intermediate | [Link](https://example.com/opt-scratch) | NumPy implementations |
| Convex Optimisation with CVXPY | Intermediate | [Link](https://example.com/cvxpy-intro) | Solve real problems with CVXPY |
| Hyperparameter Optimisation (Grid / Random / Bayesian) | Intermediate | [Link](https://example.com/hparam-opt) | Scikit‑learn + Optuna |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *An Overview of Gradient Descent Optimization Algorithms* (Ruder) | Intermediate | [Link](https://example.com/ruder-gd) | Comprehensive survey blog |
| *Why Gradient Descent Works (and When It Doesn't)* | Beginner | [Link](https://example.com/gd-works) | Intuition + visualisations |

---

## Key Concepts Checklist

- [ ] Unconstrained vs. constrained optimisation
- [ ] Convex sets and convex functions
- [ ] First‑order optimality conditions (gradient = 0)
- [ ] Gradient descent and its variants (SGD, Momentum, NAG)
- [ ] Adaptive methods (AdaGrad, RMSProp, Adam)
- [ ] Newton's method and quasi‑Newton (BFGS, L‑BFGS)
- [ ] Lagrange duality and KKT conditions
- [ ] Stochastic vs. batch vs. mini‑batch
- [ ] Learning rate schedules
- [ ] Constrained opt (linear programming, quadratic programming)

---

## Projects / Practice

| Project | Description |
|---|---|
| Compare Optimisers on Rosenbrock's Banana | Plot convergence paths for GD, Momentum, Adam |
| Train a Logistic Regression with SGD | Implement from scratch and compare to scikit‑learn |
| Portfolio Optimisation (Markowitz) | Use convex optimisation to find the efficient frontier |

---

## See also

- [Calculus](calculus.md) — gradients and Hessians are the building blocks
- [Linear Algebra](linear-algebra.md) — convex sets, quadratic forms, KKT linear systems
- [Python for AI](../programming/python-for-ai.md) — SciPy and CVXPY ecosystem
- [🧩 Visualizers](../visualizers.md) — optimisation sandboxes
- [🔢 Mathematics](../README.md)
