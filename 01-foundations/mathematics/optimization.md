# Optimization

> Choosing the best element from a set of alternatives — at the heart of almost every ML training algorithm.

**Last Reviewed:** 2026-06

**Prerequisites:** [Calculus](calculus.md) · [Linear Algebra](linear-algebra.md) · [Probability & Statistics](probability-statistics.md) (helpful)

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| *Convex Optimization* (Boyd & Vandenberghe) | Advanced | <https://web.stanford.edu/~boyd/cvxbook/> | The definitive convex opt reference (Free) |
| *Numerical Optimization* (Nocedal & Wright) | Advanced | <https://link.springer.com/book/10.1007/978-0-387-40065-5> | Comprehensive numerical methods (Paid) |
| *Algorithms for Optimization* (Kochenderfer & Wheeler) | Intermediate | <https://algorithmsbook.com/optimization/> | Modern, accessible, with Julia examples |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| Stanford EE364a — Convex Optimization (Boyd) | Advanced | <https://see.stanford.edu/Course/EE364A> | Full course with slides and homework |
| Gradient Descent and Variants (StatQuest) | Beginner | <https://www.youtube.com/watch?v=sDv4f4s2SB8> | Gentle intro to GD, SGD, Adam |
| Why Momentum & Adam Work (DeepLearning.AI) | Intermediate | <https://www.youtube.com/watch?v=k8fTYJPd3_I> | Clear intuition for modern optimisers |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| Optimization for Machine Learning (MIT 6.7220 / 6.881) | Advanced | <https://www.mit.edu/~gfarina/2024/67220s24_L09_optimization/> | Advanced but practical |
| Introduction to Optimization (Coursera — Melbourne) | Intermediate | <https://www.coursera.org/learn/discrete-optimization> | LP, QP, and nonlinear optimisation |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| Gradient Descent Visualiser | Beginner | <https://www.geogebra.org/m/V74Px3zX> | Watch GD on 2D surfaces |
| Optimisation Sandbox (TensorFlow Playground) | Intermediate | <https://playground.tensorflow.org> | Explore optimisation and learning dynamics interactively |
| Convex Sets Visualiser | Intermediate | <https://www.geogebra.org/m/Ws7xN2A8> | Understand convexity intuitively |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *Adam: A Method for Stochastic Optimization* (Kingma & Ba) | Intermediate | <https://arxiv.org/abs/1412.6980> | One of the most cited optimiser papers |
| *Understanding the Difficulty of Training Deep Feedforward Neural Networks* (Glorot & Bengio) | Advanced | <https://proceedings.mlr.press/v9/glorot10a.html> | Connects optimisation and initialisation |
| *Dropout: A Simple Way to Prevent Neural Networks from Overfitting* (Srivastava et al.) | Intermediate | <https://jmlr.org/papers/v15/srivastava14a.html> | Regularisation as optimisation trick |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| Implementing SGD, Momentum, Adam from Scratch | Intermediate | <https://github.com/lionelmessi6410/Neural-Networks-from-Scratch> | NumPy implementations |
| Convex Optimisation with CVXPY | Intermediate | <https://www.cvxpy.org/examples/index.html> | Solve real problems with CVXPY |
| Hyperparameter Optimisation (Grid / Random / Bayesian) | Intermediate | <https://optuna.org/> | Scikit-learn + Optuna examples |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *An Overview of Gradient Descent Optimization Algorithms* (Ruder) | Intermediate | <https://ruder.io/optimizing-gradient-descent/> | Comprehensive survey blog |
| *Why Gradient Descent Works (and When It Doesn't)* | Beginner | <https://distill.pub/2017/momentum> | Intuition and visualisations |

---

## Key Concepts Checklist

- Unconstrained vs. constrained optimisation
- Convex sets and convex functions
- First‑order optimality conditions (gradient = 0)
- Gradient descent and its variants (SGD, Momentum, NAG)
- Adaptive methods (AdaGrad, RMSProp, Adam)
- Newton's method and quasi‑Newton (BFGS, L‑BFGS)
- Lagrange duality and KKT conditions
- Stochastic vs. batch vs. mini‑batch
- Learning rate schedules
- Constrained opt (linear programming, quadratic programming)

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
