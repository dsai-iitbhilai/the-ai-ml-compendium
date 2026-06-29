# CNN & Computer Vision

> Convolutional Neural Networks (CNNs) and modern computer vision techniques for understanding images and videos. Covers image classification, object detection, segmentation, transfer learning, and vision transformers.

**Last Reviewed:** 2026-06

**Prerequisites:**
- [04 – Deep Learning / README](README.md)
- [Neural Network Fundamentals](neural-network-fundamentals.md)
- [Linear Algebra](../01-foundations/mathematics/linear-algebra.md)

---

# Learning Roadmap

```
Image Data
     │
     ▼
Image Processing Basics
     │
     ▼
Convolution Operation
     │
     ▼
CNN Architecture
     │
     ▼
Training CNNs
     │
     ▼
Transfer Learning
     │
     ▼
Object Detection
     │
     ▼
Image Segmentation
     │
     ▼
Vision Transformers
```

---

# Resources

## 📘 Documentation & Books

| Title | Level | Link | Notes |
|---|---|---|---|
| Dive into Deep Learning – Computer Vision | Beginner | https://d2l.ai/chapter_computer-vision/index.html | Free interactive textbook |
| Deep Learning Book (Goodfellow) – CNN Chapter | Intermediate | https://www.deeplearningbook.org/ | Mathematical foundations |
| Understanding Deep Learning (Prince) | Intermediate | https://udlbook.github.io/udlbook/ | Modern deep learning textbook |
| PyTorch Vision Tutorials | Beginner | https://pytorch.org/tutorials/intermediate/torchvision_tutorial.html | Official detection & segmentation tutorials |
| TorchVision Documentation | Beginner | https://pytorch.org/vision/stable/index.html | Models, datasets, transforms |
| OpenCV Documentation | Beginner | https://docs.opencv.org/ | Image processing library |

---

## 🎥 Videos

| Title | Level | Link | Notes |
|---|---|---|---|
| 3Blue1Brown – CNNs Explained | Beginner | https://www.youtube.com/watch?v=KuXjwB4LzSA | Best intuition for convolution |
| Stanford CS231n Lecture Series | Intermediate | https://www.youtube.com/playlist?list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv | Gold-standard CV lectures |
| MIT 6.S191 Computer Vision | Intermediate | https://www.youtube.com/@MITDeepLearning | Modern CV concepts |
| Yannic Kilcher Paper Reviews | Advanced | https://www.youtube.com/@YannicKilcher | CNN architectures explained |
| Aladdin Persson CNN Playlist | Beginner | https://www.youtube.com/@AladdinPersson | Excellent PyTorch implementations |

---

## 🎓 Courses

| Title | Level | Link | Notes |
|---|---|---|---|
| DeepLearning.AI – CNNs | Beginner | https://www.coursera.org/learn/convolutional-neural-networks | Andrew Ng |
| fast.ai Practical Deep Learning | Beginner | https://course.fast.ai/ | Top-down learning |
| Stanford CS231n | Intermediate | https://cs231n.stanford.edu/ | Best university course |
| MIT 6.S191 | Intermediate | https://introtodeeplearning.com/ | Modern CV |
| Kaggle Computer Vision Micro-course | Beginner | https://www.kaggle.com/learn/computer-vision | Hands-on notebooks |

---

## 🕹 Interactive Visualizers

| Title | Level | Link | Notes |
|---|---|---|---|
| CNN Explainer | Beginner | https://poloclub.github.io/cnn-explainer/ | Best CNN visualization |
| ConvNetJS Demo | Beginner | https://cs.stanford.edu/people/karpathy/convnetjs/ | Browser CNN demo |
| TensorFlow Playground | Beginner | https://playground.tensorflow.org/ | Neural network intuition |
| Distill Feature Visualization | Intermediate | https://distill.pub/2017/feature-visualization/ | Internal CNN representations |
| Activation Atlas | Advanced | https://distill.pub/2019/activation-atlas/ | Feature space exploration |

---

## 📄 Research Papers

| Title | Level | Link | Notes |
|---|---|---|---|
| LeNet-5 (1998) | Beginner | http://yann.lecun.com/exdb/publis/pdf/lecun-98.pdf | First successful CNN |
| AlexNet (2012) | Intermediate | https://papers.nips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf | Started deep learning revolution |
| VGGNet (2014) | Intermediate | https://arxiv.org/abs/1409.1556 | Simple deep architecture |
| GoogLeNet/Inception (2014) | Intermediate | https://arxiv.org/abs/1409.4842 | Inception modules |
| ResNet (2015) | Intermediate | https://arxiv.org/abs/1512.03385 | Residual learning |
| DenseNet | Intermediate | https://arxiv.org/abs/1608.06993 | Dense connections |
| MobileNetV2 | Intermediate | https://arxiv.org/abs/1801.04381 | Efficient CNN |
| EfficientNet | Intermediate | https://arxiv.org/abs/1905.11946 | Compound scaling |
| YOLO | Intermediate | https://arxiv.org/abs/1506.02640 | Real-time detection |
| Faster R-CNN | Advanced | https://arxiv.org/abs/1506.01497 | Two-stage detector |
| U-Net | Intermediate | https://arxiv.org/abs/1505.04597 | Segmentation |
| Vision Transformer | Advanced | https://arxiv.org/abs/2010.11929 | CNN alternative |

---

## 💻 Code & Notebooks

| Title | Level | Link | Notes |
|---|---|---|---|
| PyTorch CIFAR-10 Tutorial | Beginner | https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html | First CNN |
| TensorFlow Image Classification | Beginner | https://www.tensorflow.org/tutorials/images/classification | Official tutorial |
| Detectron2 Tutorials | Intermediate | https://detectron2.readthedocs.io/ | Detection & segmentation |
| Ultralytics YOLO Docs | Beginner | https://docs.ultralytics.com/ | Modern YOLO implementation |
| OpenMMLab | Advanced | https://github.com/open-mmlab | Large CV ecosystem |

---

## 📰 Blogs

| Title | Level | Link | Notes |
|---|---|---|---|
| Lilian Weng – Object Detection | Intermediate | https://lilianweng.github.io/posts/2018-12-27-object-recognition-part-4/ | Excellent detector overview |
| PyImageSearch | Beginner | https://pyimagesearch.com/ | Practical OpenCV & DL tutorials |
| Papers with Code – Computer Vision | Intermediate | https://paperswithcode.com/area/computer-vision | Papers + implementations |
| LearnOpenCV | Beginner | https://learnopencv.com/ | Underrated practical resource |
| TheAISummer | Intermediate | https://theaisummer.com/ | High-quality vision articles |

---

# Key Concepts Checklist

## Image Processing
- [ ] Pixels and color spaces (RGB, HSV, Grayscale)
- [ ] Image transformations
- [ ] Histogram equalization
- [ ] Edge detection

## CNN Fundamentals
- [ ] Convolution
- [ ] Kernels
- [ ] Filters
- [ ] Padding
- [ ] Stride
- [ ] Dilation
- [ ] Pooling
- [ ] Feature maps
- [ ] Receptive field

## CNN Architectures
- [ ] LeNet
- [ ] AlexNet
- [ ] VGG
- [ ] GoogLeNet
- [ ] ResNet
- [ ] DenseNet
- [ ] MobileNet
- [ ] EfficientNet

## Training CNNs
- [ ] Data augmentation
- [ ] Batch Normalization
- [ ] Dropout
- [ ] Transfer learning
- [ ] Fine-tuning

## Object Detection
- [ ] Bounding boxes
- [ ] IoU
- [ ] NMS
- [ ] Faster R-CNN
- [ ] YOLO
- [ ] SSD
- [ ] DETR

## Segmentation
- [ ] Semantic segmentation
- [ ] Instance segmentation
- [ ] Panoptic segmentation
- [ ] U-Net
- [ ] Mask R-CNN

## Vision Transformers
- [ ] Patch embeddings
- [ ] ViT
- [ ] Swin Transformer
- [ ] Hybrid CNN + ViT

## Evaluation Metrics
- [ ] Accuracy
- [ ] Precision
- [ ] Recall
- [ ] F1-score
- [ ] IoU
- [ ] Dice Score
- [ ] mAP

---

# Projects

| Project | Skills |
|----------|--------|
| Cats vs Dogs Classification | CNN fundamentals |
| CIFAR-10 Image Classification | Multi-class classification |
| Flower Species Classification | Transfer learning |
| Facial Emotion Recognition | Fine-tuning |
| Pneumonia Detection (Chest X-rays) | Medical imaging |
| YOLO Object Detection | Detection pipeline |
| Vehicle Detection from Traffic Cameras | Real-world detection |
| Road Lane Detection | OpenCV + CNN |
| U-Net Cell Segmentation | Semantic segmentation |
| Satellite Image Segmentation | Remote sensing |
| Food Image Recognition | Large-scale classification |
| Fashion Product Search | Feature extraction |

---

# Recommended Learning Order

1. Image basics
2. Convolution operation
3. CNN architecture
4. Pooling & feature maps
5. Training CNNs
6. LeNet
7. AlexNet
8. VGG
9. ResNet
10. Transfer Learning
11. Data Augmentation
12. Object Detection
13. Segmentation
14. Vision Transformers
15. Image Generation Basics

---

# See Also

- [Neural Network Fundamentals](neural-network-fundamentals.md)
- [Transformers](transformers.md)
- [Generative AI](generative-ai.md)
- [PyTorch](frameworks.md)
- [TensorFlow](frameworks.md)
- [Visualizers](visualizers.md)
- [Projects](../08-projects-and-examples/README.md)