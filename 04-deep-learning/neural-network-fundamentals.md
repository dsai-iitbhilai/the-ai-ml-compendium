# Neural Network Fundamentals

> The mathematical and computational foundation of deep learning. Learn how neural networks learn through forward propagation, backpropagation, optimization, and regularization before moving to CNNs, Transformers, and LLMs.

**Last Reviewed:** 2026-06

**Prerequisites:** [04 – Deep Learning / README](README.md) · [Linear Algebra](../01-foundations/mathematics/linear-algebra.md) · [Calculus](../01-foundations/mathematics/calculus.md) · [Optimization](../01-foundations/mathematics/optimization.md)

---

> 💡 **Tip:** Don't just memorize equations. Implement a tiny neural network from scratch using NumPy once—you'll understand deep learning far better than by only using PyTorch.

---

# Learning Roadmap

```text
Perceptron
      ↓
Activation Functions
      ↓
Forward Propagation
      ↓
Loss Functions
      ↓
Backpropagation
      ↓
Gradient Descent
      ↓
Optimizers (Adam, SGD...)
      ↓
Regularization
      ↓
Weight Initialization
      ↓
Training Deep Networks
```

---

# Resources

## 📘 Documentation & Books

| Title | Level | Link | Notes |
|---|---|---|---|
| Dive into Deep Learning | Beginner | <https://d2l.ai> | Best free deep learning book with code in PyTorch, MXNet, JAX & TensorFlow |
| Deep Learning (Goodfellow, Bengio & Courville) | Intermediate | <https://www.deeplearningbook.org> | The deep learning "Bible" |
| Understanding Deep Learning (Simon Prince) | Intermediate | <https://udlbook.github.io/udlbook/> | Modern explanations with strong mathematical intuition |
| Neural Networks and Deep Learning (Michael Nielsen) | Beginner | <http://neuralnetworksanddeeplearning.com> | Outstanding intuitive explanation of backpropagation |

---

## 🎥 Videos

| Title | Level | Link | Notes |
|---|---|---|---|
| 3Blue1Brown — Neural Networks Series | Beginner | <https://www.youtube.com/watch?v=aircAruvnKk> | Best visual intuition available |
| Andrej Karpathy — Neural Networks: Zero to Hero | Intermediate | <https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ> | Build neural networks completely from scratch |
| StatQuest — Neural Networks | Beginner | <https://www.youtube.com/@statquest> | Beginner-friendly explanations |
| Stanford CS231n Lecture 4 | Intermediate | <https://www.youtube.com/watch?v=gYpoJMlgyXA> | Forward & Backpropagation |

---

## 🎓 Courses

| Title | Level | Link | Notes |
|---|---|---|---|
| DeepLearning.AI — Neural Networks and Deep Learning | Beginner | <https://www.coursera.org/learn/neural-networks-deep-learning> | Andrew Ng's famous course |
| fast.ai Practical Deep Learning | Beginner | <https://course.fast.ai> | Learn by building real models |
| MIT 6.S191 Deep Learning | Intermediate | <https://introtodeeplearning.com> | Excellent lectures and labs |
| Dive into Deep Learning Interactive Course | Beginner | <https://d2l.ai> | Free with executable notebooks |

---

## 🕹 Interactive Visualizers

| Title | Level | Link | Notes |
|---|---|---|---|
| TensorFlow Playground | Beginner | <https://playground.tensorflow.org> | Best visualization of neural networks |
| NN-SVG | Beginner | <https://alexlenail.me/NN-SVG> | Draw and visualize architectures |
| ConvNetJS Demo | Beginner | <https://cs.stanford.edu/people/karpathy/convnetjs> | Interactive neural network demos |
| CNN Explainer | Intermediate | <https://poloclub.github.io/cnn-explainer> | Interactive convolution visualization |

---

## 📄 Must Read Papers

| Title | Level | Link | Notes |
|---|---|---|---|
| Learning Representations by Back-propagating Errors (1986) | Intermediate | <https://www.nature.com/articles/323533a0> | Birth of backpropagation |
| Understanding the Difficulty of Training Deep Feedforward Neural Networks | Advanced | <https://proceedings.mlr.press/v9/glorot10a.html> | Xavier Initialization |
| Deep Sparse Rectifier Neural Networks | Advanced | <https://proceedings.mlr.press/v15/glorot11a.html> | ReLU paper |
| Delving Deep into Rectifiers | Advanced | <https://arxiv.org/abs/1502.01852> | He Initialization |

---

## 💻 Code & Implementations

| Title | Level | Link | Notes |
|---|---|---|---|
| micrograd | Intermediate | <https://github.com/karpathy/micrograd> | Build autograd from scratch |
| makemore | Intermediate | <https://github.com/karpathy/makemore> | Neural network implementation from scratch |
| PyTorch 60 Minute Blitz | Beginner | <https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html> | Official PyTorch tutorial |
| Dive into Deep Learning Notebooks | Beginner | <https://github.com/d2l-ai/d2l-en> | Every chapter has runnable notebooks |

---

## 📰 Articles & Blogs

| Title | Level | Link | Notes |
|---|---|---|---|
| Yes, You Should Understand Backprop | Intermediate | <https://karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b> | Karpathy explains why |
| Distill — Feature Visualization | Intermediate | <https://distill.pub> | Beautiful deep learning visualizations |
| Lil'Log | Intermediate | <https://lilianweng.github.io> | Deep learning concepts explained clearly |
| Michael Nielsen's Blog | Beginner | <http://neuralnetworksanddeeplearning.com> | Excellent mathematical intuition |

---

# Key Concepts Checklist

## Foundations

- [ ] Biological neuron vs artificial neuron
- [ ] Perceptron
- [ ] XOR problem
- [ ] Multi-layer Perceptron (MLP)

---

## Forward Pass

- [ ] Matrix multiplication
- [ ] Bias terms
- [ ] Weighted sum
- [ ] Activation functions

---

## Activation Functions

- [ ] Sigmoid
- [ ] Tanh
- [ ] ReLU
- [ ] Leaky ReLU
- [ ] ELU
- [ ] GELU
- [ ] Softmax

---

## Loss Functions

- [ ] Mean Squared Error
- [ ] Mean Absolute Error
- [ ] Binary Cross Entropy
- [ ] Categorical Cross Entropy
- [ ] Hinge Loss

---

## Backpropagation

- [ ] Computational graph
- [ ] Chain Rule
- [ ] Gradient computation
- [ ] Automatic Differentiation

---

## Optimization

- [ ] Batch Gradient Descent
- [ ] Mini-batch Gradient Descent
- [ ] SGD
- [ ] Momentum
- [ ] RMSProp
- [ ] Adam
- [ ] AdamW

---

## Weight Initialization

- [ ] Random Initialization
- [ ] Xavier Initialization
- [ ] He Initialization

---

## Regularization

- [ ] L1 Regularization
- [ ] L2 Regularization
- [ ] Dropout
- [ ] Batch Normalization
- [ ] Early Stopping

---

## Training

- [ ] Learning Rate
- [ ] Batch Size
- [ ] Epoch
- [ ] Validation Set
- [ ] Learning Rate Scheduling

---

## Common Problems

- [ ] Vanishing Gradient
- [ ] Exploding Gradient
- [ ] Underfitting
- [ ] Overfitting
- [ ] Dead ReLU

---

# Practice Projects

| Project | Skills |
|----------|--------|
| Perceptron from Scratch | Matrix multiplication, activation |
| Neural Network from Scratch (NumPy) | Forward & Backpropagation |
| MNIST Digit Classifier | MLP training |
| Fashion-MNIST Classifier | Hyperparameter tuning |
| Compare Optimizers | SGD vs Adam vs RMSProp |
| Activation Function Comparison | ReLU vs GELU vs Tanh |
| Weight Initialization Experiment | Xavier vs He |
| Visualize Hidden Layer Features | Representation learning |

---

# Suggested Learning Order

```text
Perceptron
    ↓
Activation Functions
    ↓
Forward Propagation
    ↓
Loss Functions
    ↓
Backpropagation
    ↓
Gradient Descent
    ↓
Optimizers
    ↓
Regularization
    ↓
Weight Initialization
    ↓
Training Neural Networks
    ↓
PyTorch Implementation
    ↓
CNNs
    ↓
Transformers
```

---

# See also

- [Frameworks](frameworks.md) — Implement these concepts using PyTorch, TensorFlow, and JAX
- [CNN & Computer Vision](cnn-computer-vision.md) — Extend MLPs using convolutions
- [Transformers](transformers.md) — Modern architectures beyond CNNs
- [Optimization](../01-foundations/mathematics/optimization.md) — Mathematical foundation of gradient descent
- [Visualizers & Playgrounds](../visualizers-and-playgrounds/README.md) — Interactive tools for neural network intuition