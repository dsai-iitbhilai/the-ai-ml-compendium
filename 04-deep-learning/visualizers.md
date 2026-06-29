# Visualizers & Interactive Demos

> Interactive tools for building intuition about machine learning and deep learning. Explore neural networks, optimization, CNNs, RNNs, transformers, embeddings, and model interpretability through hands-on visualizations.

**Last Reviewed:** 2026-06

**Prerequisites:** None (recommended alongside every ML/DL topic)

---

## Resources

### 📘 Docs & References

| Title | Level | Link | Notes |
|------|------|------|------|
| Distill | Intermediate | https://distill.pub/ | Beautiful interactive deep learning articles |
| The Neural Network Zoo | Beginner | https://www.asimovinstitute.org/neural-network-zoo/ | Visual map of neural network architectures |
| Google PAIR Guidebook | Beginner | https://pair.withgoogle.com/guidebook/ | Human-centered AI design and interpretability |
| TensorFlow Playground Documentation | Beginner | https://playground.tensorflow.org | Learn neural networks interactively |

---

### 🎥 Videos

| Title | Level | Link | Notes |
|------|------|------|------|
| 3Blue1Brown – Neural Networks Series | Beginner | https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr | Best visual introduction to deep learning |
| 3Blue1Brown – Attention in Transformers | Beginner | https://youtu.be/eMlx5fFNoYc | Self-attention visualization |
| StatQuest – Neural Networks | Beginner | https://www.youtube.com/@statquest | Excellent conceptual explanations |
| Andrej Karpathy – Build GPT From Scratch | Intermediate | https://www.youtube.com/watch?v=kCc8FmEb1nY | Watch a transformer come together |

---

### 🕹️ Interactive Visualizers

| Tool | Topic | Link | Notes |
|------|------|------|------|
| TensorFlow Playground | Neural Networks | https://playground.tensorflow.org | Train a neural network in your browser |
| CNN Explainer | CNNs | https://poloclub.github.io/cnn-explainer/ | Interactive convolution visualization |
| Transformer Explainer | Transformers | https://poloclub.github.io/transformer-explainer/ | End-to-end transformer walkthrough |
| Attention Visualizer | LLMs | https://bbycroft.net/llm | Interactive transformer internals |
| BertViz | Attention | https://github.com/jessevig/bertviz | Explore attention heads |
| Embedding Projector | Embeddings | https://projector.tensorflow.org | Visualize embeddings with PCA and t-SNE |
| ConvNetJS Demo | CNNs | https://cs.stanford.edu/people/karpathy/convnetjs/ | Browser-based CNN experiments |
| NN SVG | Architecture Design | https://alexlenail.me/NN-SVG/ | Draw publication-quality architectures |
| Netron | Model Inspection | https://netron.app | Visualize ONNX, PyTorch and TensorFlow models |
| Weights & Biases Reports | Training | https://wandb.ai/site/reports | Interactive experiment dashboards |

---

### 📄 Papers

| Paper | Level | Link | Notes |
|------|------|------|------|
| Visualizing Data using t-SNE | Intermediate | https://www.jmlr.org/papers/v9/vandermaaten08a.html | Classic dimensionality reduction paper |
| Building Blocks of Interpretability | Intermediate | https://distill.pub/2018/building-blocks/ | Distill visualization article |
| Feature Visualization | Intermediate | https://distill.pub/2017/feature-visualization/ | Understanding learned features |
| The Building Blocks of Interpretability | Advanced | https://distill.pub/2018/building-blocks/ | Neural feature interpretation |

---

### 💻 Libraries & Tools

| Tool | Level | Link | Notes |
|------|------|------|------|
| TensorBoard | Beginner | https://www.tensorflow.org/tensorboard | Training metrics and graphs |
| TorchLens | Intermediate | https://github.com/johnmarktaylor91/torchlens | Visualize PyTorch internals |
| Captum | Intermediate | https://captum.ai/ | Model interpretability for PyTorch |
| Netron | Beginner | https://netron.app | Inspect model architectures |
| HiddenLayer | Intermediate | https://github.com/waleedka/hiddenlayer | Neural network visualization |
| SHAP | Intermediate | https://shap.readthedocs.io | Explain ML model predictions |
| LIME | Intermediate | https://lime-ml.readthedocs.io | Local interpretable explanations |

---

### 📰 Articles & Blogs

| Title | Level | Link | Notes |
|------|------|------|------|
| How to Use t-SNE Effectively | Intermediate | https://distill.pub/2016/misread-tsne/ | Learn common t-SNE mistakes |
| The Illustrated Transformer | Beginner | https://jalammar.github.io/illustrated-transformer/ | Visual transformer explanation |
| The Illustrated BERT | Beginner | https://jalammar.github.io/illustrated-bert/ | BERT visualization |
| The Illustrated GPT-2 | Beginner | https://jalammar.github.io/illustrated-gpt2/ | GPT architecture explained |
| Feature Visualization | Intermediate | https://distill.pub/2017/feature-visualization/ | CNN feature maps |

---

## Key Concepts Checklist

### Optimization

- [ ] Gradient descent
- [ ] SGD vs Adam
- [ ] Learning rate effects
- [ ] Loss landscapes
- [ ] Vanishing gradients
- [ ] Exploding gradients

### Neural Networks

- [ ] Decision boundaries
- [ ] Hidden layer representations
- [ ] Activation functions
- [ ] Backpropagation
- [ ] Computational graphs

### CNNs

- [ ] Convolution
- [ ] Filters
- [ ] Feature maps
- [ ] Pooling
- [ ] Class activation maps (CAM)
- [ ] Grad-CAM

### Sequence Models

- [ ] RNN unrolling
- [ ] Hidden states
- [ ] LSTM gates
- [ ] GRU gates
- [ ] Sequence generation

### Transformers

- [ ] Self-attention
- [ ] Multi-head attention
- [ ] Positional encoding
- [ ] Encoder
- [ ] Decoder
- [ ] Attention heatmaps

### Embeddings

- [ ] Word embeddings
- [ ] PCA visualization
- [ ] t-SNE
- [ ] UMAP
- [ ] Semantic clusters

### Explainability

- [ ] SHAP
- [ ] LIME
- [ ] Integrated Gradients
- [ ] Saliency Maps
- [ ] Feature importance

---

## Practice

| Exercise | Goal |
|------|------|
| TensorFlow Playground | Learn how activation, learning rate and layers affect training |
| CNN Explainer | Understand kernels and feature maps |
| Transformer Explainer | Follow token embeddings through attention |
| BertViz | Inspect attention heads in BERT |
| Embedding Projector | Explore word embeddings using PCA and t-SNE |
| Netron | Inspect pretrained ONNX and PyTorch models |
| TensorBoard | Monitor a training run |
| SHAP Dashboard | Explain predictions of an XGBoost model |

---

## See also

- [Neural Network Fundamentals](neural-network-fundamentals.md)
- [CNN & Computer Vision](cnn-computer-vision.md)
- [RNN & Sequence Models](rnn-sequence-models.md)
- [Transformers](transformers.md)
- [Machine Learning](../03-machine-learning/README.md)
- [Frameworks](frameworks.md)