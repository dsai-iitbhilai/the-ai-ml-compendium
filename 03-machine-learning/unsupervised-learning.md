# Unsupervised Learning

> Finding hidden structure in unlabeled data. Covers clustering, dimensionality reduction, anomaly detection, and representation learning.

**Last Reviewed:** 2026-06

**Prerequisites:** [03 – Machine Learning / README](README.md), [Linear Algebra](../01-foundations/mathematics/linear-algebra.md) (especially SVD and eigendecomposition)

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---------|---------|---------|---------|
| Scikit-learn User Guide — Clustering | Beginner | https://scikit-learn.org/stable/modules/clustering.html | Official clustering documentation |
| UMAP Documentation | Intermediate | https://umap-learn.readthedocs.io | Comprehensive UMAP guide |
| HDBSCAN Documentation | Intermediate | https://hdbscan.readthedocs.io | Excellent density-based clustering library |
| *Elements of Statistical Learning* (Ch. 14–15) | Advanced | https://hastie.su.domains/ElemStatLearn | Theoretical foundation |
| *Pattern Recognition and Machine Learning* (Bishop) | Advanced | https://www.microsoft.com/en-us/research/people/cmbishop/prml-book | Classic reference for GMMs and EM |
| Stanford CS229 Notes | Intermediate | https://cs229.stanford.edu/notes_archive/cs229-notes7a.pdf | Unsupervised learning notes |
| mlcourse.ai Topic 7 | Intermediate | https://mlcourse.ai/book/topic07/topic7_unsupervised_learning.html | Free and underrated |

---

### 🎥 Video

| Title | Level | Link | Notes |
|---------|---------|---------|---------|
| StatQuest: K-Means Clustering | Beginner | https://www.youtube.com/watch?v=4b5d3muPQmA | Best beginner explanation |
| StatQuest: PCA Clearly Explained | Beginner | https://www.youtube.com/watch?v=FgakZw6K1QQ | PCA intuition |
| StatQuest: Hierarchical Clustering | Beginner | https://www.youtube.com/watch?v=7xHsRkOdVwo | Dendrograms explained |
| Stanford CS229 — Unsupervised Learning | Intermediate | https://www.youtube.com/playlist?list=PLA89DCFA6ADACE599 | K-means, EM, PCA |
| DBSCAN Explained | Beginner | https://www.youtube.com/watch?v=RDZUdRSDOok | Density-based clustering |
| t-SNE Explained | Intermediate | https://www.youtube.com/watch?v=NEaUSP4YerM | Dimensionality reduction intuition |
| UMAP Explained | Intermediate | https://www.youtube.com/watch?v=eN0wFzBA4Sc | Modern alternative to t-SNE |

---

### 🎓 Courses

| Title | Level | Link | Notes |
|---------|---------|---------|---------|
| Machine Learning Specialization (Andrew Ng) | Beginner | https://www.coursera.org/specializations/machine-learning-introduction | Clustering and anomaly detection module |
| Stanford CS229 | Intermediate | https://cs229.stanford.edu | Strong theoretical treatment |
| mlcourse.ai | Intermediate | https://mlcourse.ai | Free and highly underrated |
| Fast.ai Practical Machine Learning | Intermediate | https://course.fast.ai | Practical implementation |
| MIT 6.390 Intro to ML | Intermediate | https://introml.mit.edu | Modern free ML course |

---

### 🕹️ Visualizers & Playgrounds

| Title | Level | Link | Notes |
|---------|---------|---------|---------|
| K-Means Visualizer | Beginner | https://www.naftaliharris.com/blog/visualizing-k-means-clustering | Watch centroids converge |
| DBSCAN Visualizer | Intermediate | https://www.naftaliharris.com/blog/visualizing-dbscan-clustering | Interactive DBSCAN demo |
| PCA Explorer | Intermediate | https://setosa.io/ev/principal-component-analysis | Best PCA visualization |
| TensorFlow Embedding Projector | Intermediate | https://projector.tensorflow.org | Explore embeddings |
| Distill Visualizations | Intermediate | https://distill.pub | Interactive ML explanations |
| UMAP Interactive Tutorial | Intermediate | https://pair-code.github.io/understanding-umap | Excellent visual intuition |

---

### 📄 Papers

| Title | Level | Link | Notes |
|---------|---------|---------|---------|
| *k-means++: The Advantages of Careful Seeding* | Intermediate | https://theory.stanford.edu/~sergei/papers/kMeansPP-soda.pdf | Better initialization |
| *DBSCAN: A Density-Based Algorithm* | Advanced | https://cdn.aaai.org/KDD/1996/KDD96-037.pdf | Original DBSCAN paper |
| *t-SNE: Visualizing Data Using t-SNE* | Advanced | https://jmlr.org/papers/v9/vandermaaten08a.html | Original t-SNE paper |
| *UMAP: Uniform Manifold Approximation and Projection* | Advanced | https://arxiv.org/abs/1802.03426 | Modern dimensionality reduction |
| *Isolation Forest* | Advanced | https://cs.nju.edu.cn/zhouzh/zhouzh.files/publication/icdm08b.pdf | Popular anomaly detection method |
| *HDBSCAN* | Advanced | https://joss.theoj.org/papers/10.21105/joss.00205 | Modern density clustering |

---

### 💻 Code & Notebooks

| Title | Level | Link | Notes |
|---------|---------|---------|---------|
| Scikit-Learn Clustering Examples | Beginner | https://scikit-learn.org/stable/auto_examples/cluster | Official examples |
| K-Means from Scratch | Intermediate | https://github.com/eriklindernoren/ML-From-Scratch | Learn internals |
| PCA from Scratch | Intermediate | https://github.com/rasbt/mlxtend | Understand SVD |
| UMAP Examples | Intermediate | https://umap-learn.readthedocs.io/en/latest/basic_usage.html | Practical UMAP |
| PyOD Examples | Intermediate | https://pyod.readthedocs.io | Anomaly detection toolkit |
| Awesome Clustering | Intermediate | https://github.com/annoviko/pyclustering | Underrated clustering library |

---

### 📰 Blogs & Guides

| Title | Level | Link | Notes |
|---------|---------|---------|---------|
| Understanding UMAP | Beginner | https://pair-code.github.io/understanding-umap | Outstanding visual guide |
| How to Choose a Clustering Algorithm | Intermediate | https://developers.google.com/machine-learning/clustering | Practical decision guide |
| Clustering Algorithms Explained | Intermediate | https://scikit-learn.org/stable/modules/clustering.html | Official comparisons |
| Anomaly Detection: A Practical Guide | Intermediate | https://pyod.readthedocs.io | Real-world anomaly detection |
| Distill Articles | Intermediate | https://distill.pub | Visual intuition for ML |
| Visualizing MNIST with PCA, t-SNE, and UMAP | Intermediate | https://umap-learn.readthedocs.io/en/latest/auto_examples/index.html | Excellent comparisons |

---

## Learning Path

### Stage 1 — Clustering

- [ ] K-Means
- [ ] K-Means++
- [ ] Elbow Method
- [ ] Silhouette Score
- [ ] Hierarchical Clustering
- [ ] DBSCAN
- [ ] HDBSCAN

### Stage 2 — Dimensionality Reduction

- [ ] PCA
- [ ] SVD
- [ ] Explained Variance
- [ ] Whitening
- [ ] t-SNE
- [ ] UMAP

### Stage 3 — Probabilistic Models

- [ ] Gaussian Mixture Models
- [ ] Expectation Maximization (EM)
- [ ] Density Estimation

### Stage 4 — Anomaly Detection

- [ ] Isolation Forest
- [ ] Local Outlier Factor (LOF)
- [ ] One-Class SVM
- [ ] Statistical Outlier Detection

---

## Projects / Practice

| Project | Description |
|----------|----------|
| Customer Segmentation | Compare K-Means, DBSCAN, HDBSCAN, and Agglomerative Clustering |
| Image Compression with K-Means | Reduce image color palettes using clustering |
| PCA vs t-SNE vs UMAP Benchmark | Compare embeddings on MNIST or Fashion-MNIST |
| Topic Clustering | Cluster sentence-transformer embeddings from news articles |
| Credit Card Fraud Detection | Isolation Forest, LOF, and One-Class SVM |
| Network Intrusion Detection | Apply anomaly detection to cybersecurity datasets |

---

## Interview Questions

- Why does K-Means struggle with non-convex clusters?
- K-Means vs GMM?
- DBSCAN vs HDBSCAN?
- PCA vs t-SNE vs UMAP?
- Why does t-SNE distort global structure?
- What does perplexity mean in t-SNE?
- How does Isolation Forest detect anomalies?
- Why is dimensionality reduction useful before clustering?
- How do you evaluate clustering without labels?

---

## See also

- [Supervised Learning](supervised-learning.md)
- [Feature Engineering](feature-engineering.md)
- [Model Evaluation](model-evaluation.md)
- [Playgrounds](playgrounds.md)
- [Embeddings](../04-deep-learning/embeddings.md)
- [Representation Learning](../04-deep-learning/representation-learning.md)