# CNN & Computer Vision

> Convolutional neural networks for visual understanding. From image classification and object detection to semantic segmentation and generative vision.

**Last Reviewed:** 2026-06

**Prerequisites:** [04 – Deep Learning / README](README.md), [Neural Network Fundamentals](neural-network-fundamentals.md), [Linear Algebra](../01-foundations/mathematics/linear-algebra.md)

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| *Deep Learning* — Chapter 9 (Goodfellow et al.) | Intermediate | [Link](https://example.com/deeplearningbook-ch9) | Convolutional networks theory and design principles |
| *Understanding Deep Learning* — Chapter 9 (Prince) | Intermediate | [Link](https://example.com/udl-ch9) | CNNs from first principles with modern context |
| PyTorch — *TorchVision Tutorials* | Beginner | [Link](https://example.com/torchvision-docs) | Official CV models, datasets, and transforms |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| 3Blue1Brown — *Convolutional Neural Networks* | Beginner | [Link](https://example.com/3b1b-cnn) | Visual explanation of convolution, pooling, and feature hierarchies |
| Stanford CS231n — *Full Lecture Series (Winter 2016)* | Intermediate | [Link](https://example.com/cs231n-winter2016) | Definitive university course on CNNs for visual recognition |
| Yannic Kilcher — *Breakdown of ResNet / DenseNet / EfficientNet* | Advanced | [Link](https://example.com/yk-cnn-architectures) | Detailed paper walkthroughs of influential architectures |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| Coursera — *Convolutional Neural Networks* (DeepLearning.AI) | Beginner | [Link](https://example.com/coursera-cnn) | Andrew Ng's second DL course; covers CNNs, object detection, face recognition |
| Fast.ai — *Computer Vision with CNNs* | Beginner | [Link](https://example.com/fastai-cv) | Top-down: train production models from day one |
| MIT 6.S191 — *Computer Vision* (Alexander Amini) | Intermediate | [Link](https://example.com/mit-6s191-cv) | Modern CV including transformers for vision |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| CNN Explainer (Poloclub) | Beginner | [Link](https://example.com/cnn-explainer) | Interactive CNN with real-time convolution, pooling, and activation visualization |
| DeepViz — *Feature Map Visualizer* | Beginner | [Link](https://example.com/deepviz) | Feed any image; see intermediate feature maps across layers |
| t-SNE Embedding of ImageNet Classes | Intermediate | [Link](https://example.com/imagenet-tsne) | Visual similarity landscape of 1000 classes |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *ImageNet Classification with Deep Convolutional Neural Networks* (Krizhevsky et al., 2012) | Intermediate | [Link](https://example.com/alexnet) | AlexNet — the paper that sparked the deep learning revolution |
| *Deep Residual Learning for Image Recognition* (He et al., 2016) | Intermediate | [Link](https://example.com/resnet) | ResNet — skip connections enabling very deep networks |
| *You Only Look Once: Unified, Real-Time Object Detection* (Redmon et al., 2016) | Intermediate | [Link](https://example.com/yolo) | YOLO — first unified real-time object detection system |
| *U-Net: Convolutional Networks for Biomedical Image Segmentation* (Ronneberger et al., 2015) | Advanced | [Link](https://example.com/unet) | U-Net — influential encoder-decoder for segmentation |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| CNN for CIFAR-10 Classification (PyTorch) | Beginner | [Link](https://example.com/cifar10-cnn) | Train a simple CNN from scratch on CIFAR-10 |
| Object Detection with Faster R-CNN (Detectron2) | Intermediate | [Link](https://example.com/detectron2-tutorial) | Meta's Detectron2 walkthrough |
| Semantic Segmentation with UNet (PyTorch) | Intermediate | [Link](https://example.com/unet-pytorch) | Full implementation of U-Net for segmentation tasks |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *An Overview of CNN Architectures* (Towards Data Science) | Beginner | [Link](https://example.com/cnn-architectures-overview) | Clear comparison of LeNet, AlexNet, VGG, ResNet, Inception |
| *How Do Convolutional Layers Work in Deep Learning* (KDnuggets) | Beginner | [Link](https://example.com/cnn-layers-blog) | Intuitive guide to channels, kernels, strides, and padding |

---

## Key Concepts Checklist

- [ ] Convolution operation (kernel, stride, padding, dilation)
- [ ] Pooling layers (max, average, global average)
- [ ] Feature hierarchy (low → mid → high-level features)
- [ ] Classic architectures (LeNet, AlexNet, VGG, ResNet, Inception, EfficientNet)
- [ ] Transfer learning and fine-tuning
- [ ] Data augmentation for vision
- [ ] Object detection (Faster R-CNN, YOLO, SSD)
- [ ] Semantic / instance segmentation (U-Net, Mask R-CNN)
- [ ] Vision transformers (ViT, Swin)
- [ ] Generative vision (DCGAN, VQ-VAE, Stable Diffusion basics)

---

## Projects / Practice

| Project | Description |
|---|---|
| Cats vs Dogs Classifier | Train a CNN from scratch; compare with a fine-tuned ResNet |
| Object Detection Pipeline | Use a pre-trained YOLO or DETR model; run inference on custom images |
| Segmentation on Medical Images | Implement U-Net for cell membrane segmentation (Kaggle data) |

---

## See also

- [Transformers](transformers.md) — Vision Transformers (ViT) as an alternative to convolutions
- [Frameworks](frameworks.md) — PyTorch/TensorFlow vision libraries
- [Visualizers](visualizers.md) — CNN Explainer and interactive feature visualization
