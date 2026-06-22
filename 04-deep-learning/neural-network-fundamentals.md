# Neural Network Fundamentals

> The core building blocks of deep learning: the perceptron, activation functions, backpropagation, and gradient-based optimization. This is the foundation for every architecture that follows.

**Last Reviewed:** 2026-06

**Prerequisites:** [04 – Deep Learning / README](README.md), [Linear Algebra](../01-foundations/mathematics/linear-algebra.md), [Calculus](../01-foundations/mathematics/calculus.md), [Optimization](../01-foundations/mathematics/optimization.md)

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| *Deep Learning* — Chapters 6–8 (Goodfellow et al.) | Intermediate | [Link](https://example.com/deeplearningbook-ch6-8) | Definitive reference on feedforward networks, regularization, optimization |
| *Understanding Deep Learning* — Chapters 3–5 (Prince) | Intermediate | [Link](https://example.com/udl-ch3-5) | Modern treatment with clear diagrams |
| *Dive into Deep Learning* — Chapters 4–5 (MLPs, backprop) | Beginner | [Link](https://example.com/d2l-mlp-backprop) | Code-first approach with JAX/PyTorch |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| 3Blue1Brown — *But what is a Neural Network?* | Beginner | [Link](https://example.com/3b1b-neural-network) | Best visual intuition for the series |
| StatQuest — *Neural Networks Explained* | Beginner | [Link](https://example.com/statquest-nn) | Clear step-through of forward and backward passes |
| Andrej Karpathy — *The spelled-out intro to neural networks and backpropagation* | Intermediate | [Link](https://example.com/karpathy-backprop) | Build and backprop through a micrograd from scratch |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| Stanford CS231n — *Neural Networks Part 1 & 2* | Intermediate | [Link](https://example.com/cs231n-nn) | Classic lectures on backprop, activation functions, and SGD |
| Coursera — *Neural Networks and Deep Learning* (DeepLearning.AI) | Beginner | [Link](https://example.com/coursera-nn) | Andrew Ng's first DL course |
| Fast.ai — *Practical Deep Learning for Coders* (Part 1) | Beginner | [Link](https://example.com/fastai-part1) | Top-down approach; implement and train on real data |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| TensorFlow Playground | Beginner | [Link](https://example.com/tf-playground) | Tweak layers, learning rate, activation; watch decision boundary form |
| NN SVG — *Neural Network Visualizer* | Beginner | [Link](https://example.com/nn-svg) | Interactive network diagrams for architecture design |
| Backpropagation Visualizer (Brilliant) | Beginner | [Link](https://example.com/backprop-viz) | Step-by-step animated backpropagation |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *A Learning Algorithm for Continually Running Fully Recurrent Neural Networks* (Rumelhart et al., 1986) | Intermediate | [Link](https://example.com/rumelhart-backprop) | The paper that popularized backpropagation |
| *Understanding the Difficulty of Training Deep Feedforward Neural Networks* (Glorot & Bengio, 2010) | Advanced | [Link](https://example.com/glorot-init) | Why initialization and activation choices matter |
| *Deep Sparse Rectifier Neural Networks* (Glorot et al., 2011) | Advanced | [Link](https://example.com/relu-paper) | Introduced ReLU, solved vanishing gradient in practice |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| micrograd — *Autograd from scratch* by Andrej Karpathy | Intermediate | [Link](https://example.com/micrograd) | Build a tiny autograd engine; understand backprop fully |
| Building a Neural Net from Scratch in NumPy | Intermediate | [Link](https://example.com/nn-from-scratch) | No frameworks; implement forward and backward pass |
| PyTorch Basic Autograd Tutorial | Beginner | [Link](https://example.com/pytorch-autograd) | Official PyTorch autograd walkthrough |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *Yes you should understand backprop* (Andrej Karpathy) | Intermediate | [Link](https://example.com/karpathy-backprop-blog) | Why backprop is worth knowing deeply |
| *A Visual Proof that Neural Networks Can Compute Any Function* (M. Nielsen) | Beginner | [Link](https://example.com/nielsen-universal) | Universal approximation theorem intuition |

---

## Key Concepts Checklist

- [ ] Perceptron and the XOR limitation
- [ ] Multi-layer perceptron (MLP) architecture
- [ ] Activation functions (sigmoid, tanh, ReLU, Leaky ReLU, GELU)
- [ ] Forward propagation
- [ ] Backpropagation (chain rule through computational graphs)
- [ ] Gradient descent variants (SGD, momentum, Adam, RMSprop)
- [ ] Weight initialization (Xavier/Glorot, He)
- [ ] Regularization (Dropout, Batch Normalization, weight decay)
- [ ] Loss functions (MSE, Cross-entropy, Hinge)
- [ ] Vanishing / exploding gradients
- [ ] Hyperparameter tuning (learning rate, batch size, epochs)

---

## Projects / Practice

| Project | Description |
|---|---|
| MLP from scratch | Implement forward/backward pass in NumPy; train on MNIST |
| Hyperparameter sweep | Train an MLP on Fashion-MNIST; compare activation functions, optimizers, learning rates |
| Feature visualization | Train a small network and visualize the learned features of hidden layers |

---

## See also

- [CNN & Computer Vision](cnn-computer-vision.md) — extending MLPs with convolutions
- [Frameworks](frameworks.md) — autograd and GPU training in practice
- [Visualizers](visualizers.md) — interactive demos for building intuition
