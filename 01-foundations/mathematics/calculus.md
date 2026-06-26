# Calculus

> Derivatives, integrals, and multivariate calculus — the engine behind gradient-based learning.

**Last Reviewed:** 2026-06

**Prerequisites:** [Linear Algebra](linear-algebra.md) · High-school calculus

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| *Calculus: Early Transcendentals* (Stewart, 9th ed.) | Beginner | https://www.cengage.com/c/calculus-early-transcendentals-9e-stewart/9781337613927PF/ | Standard university text (Paid) |
| *Calculus Made Easy* (Thompson) | Beginner | https://www.gutenberg.org/ebooks/33283 | Light, intuitive introduction |
| *The Calculus Lifesaver* (Banner) | Intermediate | https://press.princeton.edu/books/paperback/9780691130880/the-calculus-lifesaver | Great for review and problem-solving (Paid)|

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| 3Blue1Brown — Essence of Calculus | Beginner | https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr | Intuitive animated series |
| MIT 18.01 — Single Variable Calculus | Beginner | https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010 | Full lecture course |
| MIT 18.02 — Multivariable Calculus | Intermediate | https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010 | Gradients, curl, line integrals |
| Gradient Descent, How Neural Networks Learn (3Blue1Brown) | Intermediate | https://www.youtube.com/watch?v=aircAruvnKk | Connects calculus to ML |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| Calculus — Khan Academy | Beginner | https://www.khanacademy.org/math/calculus-1 | Free mastery-based course |
| Imperial College — Mathematics for ML: Multivariate Calculus (Coursera) | Intermediate | https://www.coursera.org/learn/multivariate-calculus-machine-learning | ML-focused multivariate calc |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| Derivative Visualizer (Desmos) | Beginner | https://www.desmos.com/calculator | Slider-based derivative explorer |
| 3D Gradient Plotter (GeoGebra 3D Graphing) | Intermediate | https://www.geogebra.org/3d | Visualise gradients on surfaces |
| Backpropagation Visualizer (TensorFlow Playground) | Advanced | https://playground.tensorflow.org | Step through neural network learning and gradients |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *Automatic Differentiation in Machine Learning: a Survey* (Baydin et al.) | Intermediate | https://arxiv.org/abs/1502.05767 | Comprehensive overview of autodiff |
| *The Chain Rule* (Paul's Online Math Notes) | Beginner | https://tutorial.math.lamar.edu/classes/calci/chainrule.aspx | Pedagogical treatment |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| Symbolic Differentiation with SymPy | Beginner | https://docs.sympy.org/latest/tutorials/intro-tutorial/calculus.html | Introductory notebook |
| Implementing Gradient Descent from Scratch | Intermediate | https://github.com/lionelmessi6410/Neural-Networks-from-Scratch | NumPy-only GD on a simple function |
| Automatic Differentiation with JAX | Advanced | https://jax.readthedocs.io/en/latest/automatic-differentiation.html | Build and explore autodiff workflows |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *A Visual Guide to the Chain Rule* | Beginner | https://betterexplained.com/articles/derivatives-product-power-chain | Diagrams make it click |
| *Why Momentum Works* | Intermediate | https://distill.pub/2017/momentum | Calculus intuition behind momentum |

---

## Key Concepts Checklist

- [ ] Limits, continuity, derivatives (single-variable)
- [ ] Product, quotient, and chain rules
- [ ] Integrals and the Fundamental Theorem of Calculus
- [ ] Partial derivatives and gradients
- [ ] Directional derivatives
- [ ] Jacobian and Hessian matrices
- [ ] The chain rule in multivariate settings
- [ ] Taylor series and linearisation
- [ ] Lagrange multipliers (constrained optimisation)
- [ ] Automatic differentiation (forward- and reverse-mode)

---

## Projects / Practice

| Project | Description |
|---|---|
| Gradient Descent Visualiser | Plot the path of GD on a 2D surface from different starting points |
| Backpropagation by Hand | Compute gradients for a 2-layer network with pen and paper, then verify with code |
| Optimise a Simple Cost Function | Use SciPy optimisers on `f(x)=x^2 + 5\sin(x)` and compare results |

---

## See also

- [Linear Algebra](linear-algebra.md) — Jacobians and Hessians are matrices; gradients live in vector spaces
- [Optimization](optimization.md) — gradient descent and its variants are direct applications of calculus
- [🧩 Visualizers](../visualizers.md) — interactive tools for derivatives and gradient descent
- [🔢 Mathematics](../README.md)