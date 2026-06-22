# Calculus

> Derivatives, integrals, and multivariate calculus — the engine behind gradient‑based learning.

**Last Reviewed:** 2026-06

**Prerequisites:** [Linear Algebra](linear-algebra.md) · High‑school calculus

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| *Calculus: Early Transcendentals* (Stewart, 9th ed.) | Beginner | [Link](https://example.com/stewart-calc) | Standard university text |
| *Calculus Made Easy* (Thompson) | Beginner | [Link](https://example.com/calc-made-easy) | Light, intuitive introduction |
| *The Calculus Lifesaver* (Banner) | Intermediate | [Link](https://example.com/calc-lifesaver) | Great for review and problem‑solving |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| 3Blue1Brown — Essence of Calculus | Beginner | [Link](https://example.com/3b1b-calc) | Intuitive animated series |
| MIT 18.01 — Single Variable Calculus | Beginner | [Link](https://example.com/mit-18-01) | Full lecture course |
| MIT 18.02 — Multivariable Calculus | Intermediate | [Link](https://example.com/mit-18-02) | Gradients, curl, line integrals |
| Gradient Descent, How Neural Networks Learn (3Blue1Brown) | Intermediate | [Link](https://example.com/3b1b-gd) | Connects calculus to ML |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| Calculus — Khan Academy | Beginner | [Link](https://example.com/khan-calc) | Free mastery‑based course |
| Imperial College — Mathematics for ML: Multivariate Calculus (Coursera) | Intermediate | [Link](https://example.com/imperial-mvc) | ML‑focused multivariate calc |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| Derivative Visualizer (Desmos) | Beginner | [Link](https://example.com/desmos-derivative) | Slider‑based derivative explorer |
| 3D Gradient Plotter | Intermediate | [Link](https://example.com/gradient-3d) | Visualise gradients on surfaces |
| Backpropagation Calculator | Advanced | [Link](https://example.com/backprop-calc) | Step through the chain rule on a small net |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *Automatic Differentiation in Machine Learning: a Survey* (Baydin et al.) | Intermediate | [Link](https://example.com/autodiff-survey) | Comprehensive overview of autodiff |
| *The Chain Rule* (educational reprint) | Beginner | [Link](https://example.com/chain-rule-paper) | Pedagogical treatment |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| Symbolic Differentiation with SymPy | Beginner | [Link](https://example.com/sympy-diff) | Introductory notebook |
| Implementing Gradient Descent from Scratch | Intermediate | [Link](https://example.com/gd-scratch) | NumPy‑only GD on a simple function |
| Automatic Differentiation with JAX | Advanced | [Link](https://example.com/jax-autodiff) | Build a tiny autodiff engine |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *A Visual Guide to the Chain Rule* | Beginner | [Link](https://example.com/chain-rule-visual) | Diagrams make it click |
| *Why Momentum Works* | Intermediate | [Link](https://example.com/momentum-blog) | Calculus intuition behind momentum |

---

## Key Concepts Checklist

- [ ] Limits, continuity, derivatives (single‑variable)
- [ ] Product, quotient, and chain rules
- [ ] Integrals and the Fundamental Theorem of Calculus
- [ ] Partial derivatives and gradients
- [ ] Directional derivatives
- [ ] Jacobian and Hessian matrices
- [ ] The chain rule in multivariate settings
- [ ] Taylor series and linearisation
- [ ] Lagrange multipliers (constrained optimisation)
- [ ] Automatic differentiation (forward‑ and reverse‑mode)

---

## Projects / Practice

| Project | Description |
|---|---|
| Gradient Descent Visualiser | Plot the path of GD on a 2D surface from different starting points |
 | Backpropagation by Hand | Compute gradients for a 2‑layer network with pen and paper, then verify with code |
| Optimise a Simple Cost Function | Use SciPy optimisers on $f(x)=x^2 + 5\sin(x)$ and compare results |

---

## See also

- [Linear Algebra](linear-algebra.md) — Jacobians and Hessians are matrices; gradients live in vector spaces
- [Optimization](optimization.md) — gradient descent and its variants are direct applications of calculus
- [🧩 Visualizers](../visualizers.md) — interactive tools for derivatives and gradient descent
- [🔢 Mathematics](../README.md)
