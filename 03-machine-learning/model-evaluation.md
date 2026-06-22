# Model Evaluation

> Rigorous methods for measuring, diagnosing, and improving model performance. Covers cross-validation, metrics, confusion matrices, ROC/AUC, and the bias-variance tradeoff.

**Last Reviewed:** 2026-06

**Prerequisites:** [Supervised Learning](supervised-learning.md), [Probability & Statistics](../01-foundations/mathematics/probability-statistics.md)

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| Scikit-learn — Model Evaluation Guide | Beginner | [Link](https://example.com/sklearn-evaluation) | Complete API reference for metrics and CV |
| *An Introduction to Statistical Learning* — Chapter 2 (Bias-Variance) & 5 (Resampling) | Beginner | [Link](https://example.com/islr-cv) | Clear treatment of CV and bias-variance |
| *Approximate Statistical Tests for Comparing Classification Algorithms* (Dietterich, 1998) | Advanced | [Link](https://example.com/stat-tests-paper) | Formal comparison of classifiers |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| StatQuest: Cross-Validation | Beginner | [Link](https://example.com/statquest-cv) | k-fold, LOOCV, and when to use each |
| StatQuest: AUC and ROC Curves | Beginner | [Link](https://example.com/statquest-auc) | Intuitive explanation of ROC space |
| Confusion Matrix — Intuitive Explanation | Beginner | [Link](https://example.com/confusion-vid) | Precision, recall, F1 with visual aids |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| Kaggle — Machine Learning Explainability | Beginner | [Link](https://example.com/kaggle-explain) | SHAP, permutation importance, partial dependence plots |
| Stanford CS229 — Evaluation & Diagnostics | Intermediate | [Link](https://example.com/cs229-eval) | Learning curves, error analysis, A/B testing |
| Coursera — Model Evaluation and Validation (UW) | Intermediate | [Link](https://example.com/coursera-ml-eval) | In-depth on bias-variance and cross-validation |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| ROC Curve Explorer | Beginner | [Link](https://example.com/roc-playground) | Adjust threshold and watch TPR/FPR change |
| Bias-Variance Tradeoff Simulator | Intermediate | [Link](https://example.com/bias-variance-sim) | See underfit ↔ overfit with model complexity |
| Confusion Matrix Visualizer | Beginner | [Link](https://example.com/confusion-viz) | Enter predictions and see all metrics update |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *The Relationship Between Precision-Recall and ROC Curves* (Davis & Goadrich, 2006) | Intermediate | [Link](https://example.com/pr-vs-roc) | When to use PR over ROC |
| *A Study of Cross-Validation and Bootstrap for Accuracy Estimation* (Kohavi, 1995) | Intermediate | [Link](https://example.com/kohavi-cv) | Empirical comparison of CV variants |
| *Regularization and Variable Selection via the Elastic Net* (Zou & Hastie, 2005) | Advanced | [Link](https://example.com/elastic-net) | Relates to bias-variance via regularization |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| Cross-Validation with scikit-learn | Beginner | [Link](https://example.com/sklearn-cv) | k-fold, stratified, grouped, and time-series splits |
| Plotting ROC Curves in Python | Beginner | [Link](https://example.com/roc-plot) | Matplotlib-based ROC visualization |
| Learning Curves Diagnostic Notebook | Intermediate | [Link](https://example.com/learning-curves) | Diagnose bias-variance from train/val curves |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *Understanding the Bias-Variance Tradeoff* (Scott Fortmann-Roe) | Intermediate | [Link](https://example.com/bias-variance-blog) | Classic blog post with clear diagrams |
| *ROC Curves — What Are They and How to Use Them* | Beginner | [Link](https://example.com/roc-blog) | Practical guide for practitioners |
| *Why Accuracy Is a Misleading Metric* | Beginner | [Link](https://example.com/accuracy-misleading) | Imbalanced classification case studies |

---

## Key Concepts Checklist

- [ ] Holdout validation (train/validation/test split)
- [ ] k-fold cross-validation (stratified, repeated, grouped)
- [ ] Leave-One-Out CV (LOOCV) and its tradeoffs
- [ ] Confusion matrix (TP, TN, FP, FN)
- [ ] Classification metrics (accuracy, precision, recall, F1, specificity)
- [ ] ROC curve and AUC (TPR vs FPR, threshold selection)
- [ ] Precision-Recall curves (when classes are imbalanced)
- [ ] Regression metrics (MSE, RMSE, MAE, R², adjusted R²)
- [ ] Bias-variance tradeoff (underfitting vs overfitting)
- [ ] Learning curves (diagnosing bias/variance with dataset size)
- [ ] Feature importance (permutation importance, SHAP, coefficient magnitude)
- [ ] Statistical significance testing (McNemar's test, paired t-test)

---

## Projects / Practice

| Project | Description |
|---|---|
| Compare CV Strategies | Evaluate k-fold, stratified, and repeated CV on an imbalanced dataset |
| Build a Metrics Dashboard | Create a single-function report that prints confusion matrix, ROC-AUC, PR-AUC, and classification report |
| Bias-Variance Diagnosis | Train models of increasing complexity on a small dataset and plot learning curves |

---

## See also

- [Supervised Learning](supervised-learning.md) — models whose outputs you need to evaluate
- [Ensemble Methods](ensemble-methods.md) — OOB scores, early stopping for evaluation
- [Feature Engineering](feature-engineering.md) — feature importance and selection metrics
- [Classic ML Frameworks](classic-ml-frameworks.md) — scikit-learn's `cross_val_score`, GridSearchCV
