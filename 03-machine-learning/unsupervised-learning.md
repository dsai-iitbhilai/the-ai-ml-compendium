# Unsupervised Learning

> Finding hidden structure in unlabeled data. Covers clustering, dimensionality reduction, and anomaly detection.

**Last Reviewed:** 2026-06

**Prerequisites:** [03 – Machine Learning / README](README.md), [Linear Algebra](../01-foundations/mathematics/linear-algebra.md) (especially SVD and eigendecomposition)

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| Scikit-learn User Guide — Clustering | Beginner | [Link](https://example.com/sklearn-clustering) | Overview of all supported clustering algorithms |
| *Elements of Statistical Learning* — Chapters 14–15 | Advanced | [Link](https://example.com/esl-ch14-15) | Unsupervised learning theory and methods |
| UMAP Documentation | Intermediate | [Link](https://example.com/umap-docs) | Comprehensive guide to UMAP parameters |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| StatQuest: K-Means Clustering | Beginner | [Link](https://example.com/statquest-kmeans) | Gentle introduction to k-means |
| t-SNE Explained — 3Blue1Brown | Intermediate | [Link](https://example.com/3b1b-tsne) | Intuitive explanation of t-SNE mechanics |
| DBSCAN Clustering Explained | Beginner | [Link](https://example.com/dbscan-video) | Density-based clustering with examples |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| Unsupervised Learning, Recommenders, Reinforcement Learning (Coursera) | Beginner | [Link](https://example.com/coursera-unsupervised) | Andrew Ng — clustering and anomaly detection module |
| Stanford CS229 — Unsupervised Learning | Intermediate | [Link](https://example.com/cs229-unsupervised) | K-means, GMMs, EM algorithm, and PCA |
| DeepLearning.AI — Unsupervised Learning (Short Course) | Intermediate | [Link](https://example.com/dla-unsupervised) | Practical clustering with scikit-learn |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| K-Means Visualizer (Stanford) | Beginner | [Link](https://example.com/kmeans-viz) | Watch centroids converge step by step |
| DBSCAN Interactive Demo | Intermediate | [Link](https://example.com/dbscan-demo) | Tweak eps and minPts in real time |
| PCA vs t-SNE vs UMAP Explorer | Intermediate | [Link](https://example.com/dimred-playground) | Compare dimensionality reduction techniques on the same dataset |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *k-means++: The Advantages of Careful Seeding* (Arthur & Vassilvitskii, 2007) | Intermediate | [Link](https://example.com/kmeanspp-paper) | Improved k-means initialization |
| *t-SNE: Visualizing Data Using t-SNE* (van der Maaten & Hinton, 2008) | Advanced | [Link](https://example.com/tsne-paper) | Original t-SNE paper |
| *UMAP: Uniform Manifold Approximation and Projection* (McInnes et al., 2018) | Advanced | [Link](https://example.com/umap-paper) | Faster and often better than t-SNE |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| K-Means from Scratch | Intermediate | [Link](https://example.com/kmeans-scratch) | Implement Lloyd's algorithm in NumPy |
| PCA from Scratch | Intermediate | [Link](https://example.com/pca-scratch) | Tie SVD to dimensionality reduction |
| Anomaly Detection with Isolation Forest | Intermediate | [Link](https://example.com/isolation-forest) | Practical notebook comparing IF to LOF |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *Visualizing MNIST: PCA vs t-SNE vs UMAP* | Beginner | [Link](https://example.com/mnist-vis-blog) | See how each method embeds the digit dataset |
| *How to Choose a Clustering Algorithm* | Intermediate | [Link](https://example.com/clustering-guide) | Decision tree for picking the right method |
| *Anomaly Detection: A Practical Guide* | Intermediate | [Link](https://example.com/anomaly-guide) | Covers IF, LOF, and autoencoder-based methods |

---

## Key Concepts Checklist

- [ ] K-means clustering (Lloyd's algorithm, initialization, elbow method)
- [ ] DBSCAN (density-reachability, core points, border points)
- [ ] Hierarchical clustering (agglomerative, dendrograms, linkage criteria)
- [ ] Gaussian Mixture Models (soft clustering, EM algorithm)
- [ ] Principal Component Analysis (SVD formulation, explained variance, whitening)
- [ ] t-SNE (perplexity, stochastic neighbor embedding)
- [ ] UMAP (manifold learning, topological approach)
- [ ] Anomaly detection (Isolation Forest, LOF, one-class SVM)
- [ ] Cluster validation (silhouette score, Davies–Bouldin index)
- [ ] Curse of dimensionality and its effect on distances

---

## Projects / Practice

| Project | Description |
|---|---|
| Customer Segmentation | Use K-means, DBSCAN, and hierarchical clustering to segment retail customers |
| Image Compression with K-Means | Reduce the color palette of an image by clustering pixel colors |
| Anomaly Detection on Credit Card Transactions | Apply Isolation Forest and LOF to detect fraudulent transactions |

---

## See also

- [Supervised Learning](supervised-learning.md) — labeled counterpart to clustering and anomaly detection
- [Feature Engineering](feature-engineering.md) — PCA as a feature extraction tool
- [Model Evaluation](model-evaluation.md) — silhouette score, Davies–Bouldin index for clustering
- [Playgrounds](playgrounds.md) — interactive demos of clustering and dimensionality reduction
