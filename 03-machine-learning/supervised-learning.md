# Supervised Learning

> Algorithms that learn a mapping from inputs to labeled outputs. Covers regression and classification, from linear models through decision trees and support vector machines.

**Last Reviewed:** 2026-06

**Prerequisites:** [03 – Machine Learning / README](README.md), [Linear Algebra](../01-foundations/mathematics/linear-algebra.md), [Probability & Statistics](../01-foundations/mathematics/probability-statistics.md)

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| *An Introduction to Statistical Learning* — Chapters 2–7 | Beginner | [Link](https://example.com/islr-ch2-7) | Best starting point for supervised learning |
| Scikit-learn User Guide — Supervised Learning | Beginner | [Link](https://example.com/sklearn-supervised) | Official docs with working code examples |
| *Elements of Statistical Learning* — Chapters 3–12 | Advanced | [Link](https://example.com/esl-ch3-12) | Mathematical depth for practitioners |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| StatQuest: Linear Regression & Logistic Regression | Beginner | [Link](https://example.com/statquest-regression) | Clear, animated intuition |
| Stanford CS229 — Supervised Learning Lectures (Andrew Ng) | Intermediate | [Link](https://example.com/cs229-supervised) | Classic lecture series |
| Decision Trees (3Blue1Brown-style explainer) | Beginner | [Link](https://example.com/dt-viz-explainer) | Visual walkthrough of tree splitting |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| Supervised Machine Learning: Regression & Classification (Coursera) | Beginner | [Link](https://example.com/coursera-supervised) | Andrew Ng's updated ML course, first course |
| Kaggle — Intro to Machine Learning | Beginner | [Link](https://example.com/kaggle-intro-ml) | Free micro-course, decision trees + random forests |
| Georgia Tech — CS 4641: Machine Learning | Intermediate | [Link](https://example.com/gt-cs4641) | University course with theory and projects |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| Decision Tree Visualizer (dtreeviz) | Beginner | [Link](https://example.com/dtreeviz) | See exactly how trees split |
| SVM with RBF Kernel Explorer | Intermediate | [Link](https://example.com/svm-playground) | Tweak C and gamma, watch decision boundary change |
| k-NN Decision Boundary Visualizer | Beginner | [Link](https://example.com/knn-viz) | Adjust k and distance metric interactively |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *Least Angle Regression* (Efron et al., 2004) | Advanced | [Link](https://example.com/lars-paper) | Efficient algorithm for Lasso |
| *LIBSVM: A Library for Support Vector Machines* (Chang & Lin, 2011) | Intermediate | [Link](https://example.com/libsvm-paper) | Widely-cited SVM implementation paper |
| *XGBoost: A Scalable Tree Boosting System* (Chen & Guestrin, 2016) | Advanced | [Link](https://example.com/xgboost-paper) | Foundation for modern gradient boosting |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| scikit-learn: Linear Regression Example | Beginner | [Link](https://example.com/sklearn-linreg) | Minimal working example |
| Multi-class Classification with SVM | Intermediate | [Link](https://example.com/svm-multiclass) | One-vs-one and one-vs-rest strategies |
| k-NN from Scratch in NumPy | Intermediate | [Link](https://example.com/knn-scratch) | Understand the algorithm by building it |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *Understanding the Bias-Variance Tradeoff* (Scott Fortmann-Roe) | Intermediate | [Link](https://example.com/bias-variance-blog) | Clear, visual explanation |
| *A Visual Introduction to k-Nearest Neighbors* | Beginner | [Link](https://example.com/knn-visual-blog) | Friendly diagrams and examples |

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

- [Ensemble Methods](ensemble-methods.md) — random forests, gradient boosting, XGBoost
- [Model Evaluation](model-evaluation.md) — cross-validation, metrics, confusion matrix, ROC/AUC
- [Feature Engineering](feature-engineering.md) — encoding, scaling, selection for supervised tasks
- [Classic ML Frameworks](classic-ml-frameworks.md) — scikit-learn, XGBoost, LightGBM
- [Unsupervised Learning](unsupervised-learning.md) — clustering and dimensionality reduction
