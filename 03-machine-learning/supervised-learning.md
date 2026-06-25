# Supervised Learning

> Algorithms that learn a mapping from inputs to labeled outputs. Covers regression and classification, from linear models through decision trees and support vector machines.

**Last Reviewed:** 2026-06

**Prerequisites:** [03 – Machine Learning / README](README.md), [Linear Algebra](../01-foundations/mathematics/linear-algebra.md), [Probability & Statistics](../01-foundations/mathematics/probability-statistics.md)

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| *An Introduction to Statistical Learning (ISLR 2nd Ed.)* — Chapters 2–7 | Beginner | https://www.statlearning.com | Best starting point for supervised learning (Free PDF) |
| Scikit-learn User Guide — Supervised Learning | Beginner | https://scikit-learn.org/stable/supervised_learning.html | Official docs with working code examples |
| *Elements of Statistical Learning (ESL)* | Advanced | https://hastie.su.domains/ElemStatLearn/ | Mathematical depth for practitioners (Free PDF) |
| *Understanding Machine Learning: From Theory to Algorithms* | Advanced | https://www.cs.huji.ac.il/~shais/UnderstandingMachineLearning | Excellent theoretical treatment (Free PDF) |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| StatQuest: Linear Regression & Logistic Regression Playlist | Beginner | https://www.youtube.com/@statquest | Clear, animated intuition |
| Stanford CS229 — Machine Learning Lectures (Andrew Ng) | Intermediate | https://see.stanford.edu/Course/CS229 | Classic lecture series |
| Google ML Crash Course — Classification | Beginner | https://developers.google.com/machine-learning/crash-course/classification | Interactive lessons and visuals |
| MIT 6.036 — Introduction to Machine Learning | Intermediate | https://ocw.mit.edu/courses/6-036-introduction-to-machine-learning-fall-2020/ | Strong theoretical foundations |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| Supervised Machine Learning: Regression & Classification (Andrew Ng) | Beginner | https://www.coursera.org/learn/machine-learning | Modern ML introduction |
| Kaggle — Intro to Machine Learning | Beginner | https://www.kaggle.com/learn/intro-to-machine-learning | Free micro-course with decision trees and random forests |
| Georgia Tech CS 4641 — Machine Learning | Intermediate | https://omscs.gatech.edu/cs-7641-machine-learning | University-level ML course |
| Google Machine Learning Crash Course | Beginner | https://developers.google.com/machine-learning/crash-course | Free practical ML curriculum |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| DTreeViz | Beginner | https://github.com/parrt/dtreeviz | Visualize exactly how decision trees split |
| TensorFlow Playground | Beginner | https://playground.tensorflow.org | Interactive classification and decision boundaries |
| SVM Explorer | Intermediate | https://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html | Explore effects of C and gamma |
| KNN Interactive Visualization | Beginner | https://mlu-explain.github.io/knn/ | Understand nearest-neighbor classification |
| Yellowbrick Visual Diagnostics | Intermediate | https://www.scikit-yb.org | Underrated toolkit for visual model analysis |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *Least Angle Regression* (Efron et al., 2004) | Advanced | https://arxiv.org/abs/math/0406456 | Efficient algorithm for Lasso |
| *LIBSVM: A Library for Support Vector Machines* (Chang & Lin, 2011) | Intermediate | https://www.csie.ntu.edu.tw/~cjlin/papers/libsvm.pdf | Widely-cited SVM implementation paper |
| *XGBoost: A Scalable Tree Boosting System* (Chen & Guestrin, 2016) | Advanced | https://arxiv.org/abs/1603.02754 | Foundation of modern gradient boosting |
| *Random Forests* (Breiman, 2001) | Advanced | https://www.stat.berkeley.edu/~breiman/randomforest2001.pdf | Landmark tree ensemble paper |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| Scikit-learn: Linear Regression Example | Beginner | https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html | Minimal working example |
| Logistic Regression Example | Beginner | https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic.html | Binary classification walkthrough |
| Multi-class Classification with SVM | Intermediate | https://scikit-learn.org/stable/auto_examples/svm/index.html | One-vs-one and one-vs-rest strategies |
| KNN from Scratch in NumPy | Intermediate | https://github.com/eriklindernoren/ML-From-Scratch | Understand the algorithm by building it |
| Decision Tree Visualization Example | Beginner | https://scikit-learn.org/stable/modules/tree.html | Build and visualize trees |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *Understanding the Bias-Variance Tradeoff* (Scott Fortmann-Roe) | Intermediate | https://scott.fortmann-roe.com/docs/BiasVariance.html | One of the clearest explanations available |
| *A Visual Introduction to k-Nearest Neighbors* | Beginner | https://www.ibm.com/think/topics/knn | Friendly diagrams and examples |
| *The Illustrated Guide to Logistic Regression* | Beginner | https://mlu-explain.github.io/logistic-regression/ | Interactive explanation |
| *Interpretable Machine Learning* (Molnar) | Intermediate | https://christophm.github.io/interpretable-ml-book/ | Model interpretation and diagnostics |

---



## Key Concepts Checklist

- [ ] Linear regression (OLS, assumptions, interpretability)
- [ ] Ridge and Lasso regression (regularization, L1 vs L2)
- [ ] Logistic regression (sigmoid, decision boundary, log-loss)
- [ ] Support vector machines (max-margin, kernels, soft margin)
- [ ] Decision trees (splitting criteria, pruning, overfitting)
- [ ] k-Nearest Neighbors (distance metrics, curse of dimensionality)
- [ ] Naive Bayes (conditional independence, Bayes' theorem)
- [ ] Evaluation metrics for classification (accuracy, precision, recall, F1, ROC-AUC)
- [ ] Evaluation metrics for regression (MSE, RMSE, MAE, R²)
- [ ] Hyperparameter tuning (grid search, random search)

---

## Projects / Practice

| Project | Description |
|---|---|
| House Price Prediction | Build and compare linear, ridge, and lasso regression on the Ames Housing dataset |
| Spam Classifier | Use logistic regression, Naive Bayes, and SVM on the UCI Spambase dataset |
| Car Evaluation Classifier | Train a decision tree and k-NN on the Car Evaluation dataset; compare accuracy vs interpretability |

---

## See also

- [Ensemble Methods](ensemble-methods.md) — random forests, gradient boosting, XGBoost, LightGBM
- [Model Evaluation](model-evaluation.md) — cross-validation, metrics, confusion matrices, ROC/AUC
- [Feature Engineering](feature-engineering.md) — encoding, scaling, and feature selection
- [Classic ML Frameworks](classic-ml-frameworks.md) — scikit-learn, XGBoost, LightGBM, CatBoost
- [Unsupervised Learning](unsupervised-learning.md) — clustering and dimensionality reduction
- [Linear Algebra](../01-foundations/mathematics/linear-algebra.md) — vectors, matrices, projections
- [Probability & Statistics](../01-foundations/mathematics/probability-statistics.md) — likelihood, Bayes' theorem, inference
- [Playgrounds](playgrounds.md) — interactive decision boundary and classifier visualizations
- [🤖 Machine Learning](README.md)

---
