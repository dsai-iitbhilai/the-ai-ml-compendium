# Frameworks

> PyTorch, TensorFlow, JAX, and the ecosystem of tools that power deep learning research and production. This page focuses on framework selection, core APIs, and best practices.

**Last Reviewed:** 2026-06

**Prerequisites:** [04 – Deep Learning / README](README.md), [Neural Network Fundamentals](neural-network-fundamentals.md), [Python for AI](../01-foundations/programming/python-for-ai.md)

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| PyTorch Documentation (pytorch.org) | Beginner | [Link](https://example.com/pytorch-docs) | Official docs; best place to start for PyTorch |
| TensorFlow Core Documentation | Beginner | [Link](https://example.com/tensorflow-docs) | Official TF 2.x documentation and guides |
| JAX Documentation & Quickstart | Intermediate | [Link](https://example.com/jax-docs) | Official JAX docs; functional transformations |
| *Dive into Deep Learning* — Multi-framework edition | Beginner | [Link](https://example.com/d2l-frameworks) | Code examples in PyTorch, TF, JAX side by side |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| PyTorch Tutorials (Full Course) — freeCodeCamp | Beginner | [Link](https://example.com/fcc-pytorch) | Comprehensive 4-hour PyTorch walkthrough |
| TensorFlow 2.0 Complete Course — Tech With Tim | Beginner | [Link](https://example.com/tf2-course) | Hands-on TF from basics to deployment |
| JAX from Scratch (PyImageSearch) | Intermediate | [Link](https://example.com/jax-from-scratch) | Understanding JAX's functional paradigm and `vmap`/`pmap` |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| PyTorch for Deep Learning (Learn PyTorch) | Beginner | [Link](https://example.com/learn-pytorch) | Free course from zero to production CNN/transformer |
| TensorFlow Developer Certificate (Coursera) | Beginner | [Link](https://example.com/tf-certificate) | Official TF certificate program |
| JAX & Flax — Full Stack Deep Learning | Advanced | [Link](https://example.com/fsdl-jax) | Research-level JAX for large-scale training |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| *TensorFlow Playground* | Beginner | [Link](https://example.com/tf-playground) | Not framework-specific; see core concepts live |
| PyTorch — *Computational Graph Visualizer* | Intermediate | [Link](https://example.com/torchviz) | Visualize the autograd graph of your model |
| Netron — *Model Architecture Viewer* | Beginner | [Link](https://example.com/netron) | Inspect ONNX, PyTorch, TF model files |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *PyTorch: An Imperative Style, High-Performance Deep Learning Library* (Paszke et al., 2019) | Intermediate | [Link](https://example.com/pytorch-paper) | PyTorch system design and performance |
| *TensorFlow: A System for Large-Scale Machine Learning* (Abadi et al., 2016) | Intermediate | [Link](https://example.com/tensorflow-paper) | TensorFlow architecture and distributed design |
| *JAX: Composable Transformations of Python+NumPy Programs* (Bradbury et al., 2018) | Advanced | [Link](https://example.com/jax-paper) | JAX's just-in-time compilation and automatic differentiation |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| PyTorch — *60 Minute Blitz* | Beginner | [Link](https://example.com/pytorch-blitz) | Official quickstart tutorial |
| TensorFlow — *Neural Machine Translation with Attention* | Intermediate | [Link](https://example.com/tf-nmt) | End-to-end model building in TF |
| JAX — *Training a ResNet on ImageNet with Flax* | Advanced | [Link](https://example.com/jax-resnet) | Full training pipeline using JAX, Flax, Optax |
| Flax / Haiku / Equinox Comparison | Advanced | [Link](https://example.com/jax-lib-comparison) | Choosing among JAX neural network libraries |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *PyTorch vs TensorFlow in 2026* (The Gradient) | Beginner | [Link](https://example.com/pytorch-vs-tf) | Current state of the framework landscape |
| *Why JAX is the Future of Deep Learning* (Julia Evans) | Intermediate | [Link](https://example.com/why-jax) | JAX's transform-everywhere philosophy explained |

---

## Key Concepts Checklist

- [ ] Tensor operations and GPU acceleration
- [ ] Autograd / automatic differentiation
- [ ] Building and training models (Module/Model class)
- [ ] Data loading and preprocessing (DataLoader, tf.data)
- [ ] Optimizers (SGD, Adam, AdamW, Lion)
- [ ] Learning rate schedules (cosine, warmup, OneCycle)
- [ ] Checkpointing and model serialization
- [ ] Mixed-precision training (amp, bfloat16)
- [ ] Distributed training (DDP, FSDP, TF Strategy)
- [ ] Experiment tracking (TensorBoard, W&B, MLflow)
- [ ] Model deployment (TorchScript, ONNX, TF Serving, TFLite)

---

## Projects / Practice

| Project | Description |
|---|---|
| Multi-framework Toy Model | Implement the same MLP in PyTorch, TF, and JAX; compare APIs and ergonomics |
| Training Loop Builder | Build a custom training loop with mixed precision, logging, and checkpointing |
| Distributed Training Demo | Set up a simple DDP (PyTorch) or TF Strategy example on multi-GPU |

---

## See also

- [Neural Network Fundamentals](neural-network-fundamentals.md) — concepts you'll implement with these frameworks
- [CNN & Computer Vision](cnn-computer-vision.md) — TorchVision, TF Vision, and JAX vision libraries
- [Transformers](transformers.md) — Hugging Face Transformers and their integration with all three frameworks
