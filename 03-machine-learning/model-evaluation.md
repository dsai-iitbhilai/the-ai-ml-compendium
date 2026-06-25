# Model Evaluation

> Rigorous methods for measuring, diagnosing, and improving model performance. Covers cross-validation, metrics, confusion matrices, ROC/AUC, and the bias-variance tradeoff.

**Last Reviewed:** 2026-06

**Prerequisites:** [Supervised Learning](supervised-learning.md), [Probability & Statistics](../01-foundations/mathematics/probability-statistics.md)

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| Scikit-learn — Model Evaluation Guide | Beginner | https://scikit-learn.org/stable/modules/model_evaluation.html | Complete API reference for metrics and cross-validation |
| *An Introduction to Statistical Learning (ISLR)* — Chapters 2 & 5 | Beginner | https://www.statlearning.com/ | Free textbook covering bias-variance and resampling |
| *Approximate Statistical Tests for Comparing Classification Algorithms* (Dietterich, 1998) | Advanced | https://direct.mit.edu/neco/article/10/7/1895/6224/Approximate-Statistical-Tests-for-Comparing | Formal comparison of classifiers |
| *Interpretable Machine Learning* (Molnar) | Intermediate | https://christophm.github.io/interpretable-ml-book/ | Excellent free resource on evaluation and explainability |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| StatQuest: Cross Validation | Beginner | https://www.youtube.com/watch?v=fSytzGwwBVw | k-fold, LOOCV, and when to use each |
| StatQuest: ROC and AUC | Beginner | https://www.youtube.com/watch?v=4jRBRDbJemM | Intuitive explanation of ROC space |
| StatQuest: Precision, Recall, Sensitivity and Specificity | Beginner | https://www.youtube.com/watch?v=vP06aMoz4v8 | Confusion matrix metrics explained |
| Google ML Crash Course — Classification Metrics | Beginner | https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall | Practical industry perspective |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| Kaggle — Machine Learning Explainability | Beginner | https://www.kaggle.com/learn/machine-learning-explainability | SHAP, permutation importance, PDPs |
| Stanford CS229 — Evaluation & Diagnostics Notes | Intermediate | https://cs229.stanford.edu/ | Learning curves, error analysis, diagnostics |
| Google Machine Learning Crash Course | Beginner | https://developers.google.com/machine-learning/crash-course | Includes evaluation metrics and validation |
| fast.ai Practical Deep Learning | Intermediate | https://course.fast.ai/ | Strong practical treatment of validation and metrics |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| ROC Curve Interactive Explorer | Beginner | https://mlu-explain.github.io/roc-auc/ | Adjust thresholds and observe ROC changes |
| Google ML Visualization Modules | Beginner | https://pair.withgoogle.com/explorables/ | Interactive ML concepts and metrics |
| TensorFlow Playground | Beginner | https://playground.tensorflow.org/ | Visualize decision boundaries and overfitting |
| SHAP Interactive Examples | Intermediate | https://shap.readthedocs.io/en/latest/example_notebooks.html | Feature importance and model diagnostics |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *The Relationship Between Precision-Recall and ROC Curves* (Davis & Goadrich, 2006) | Intermediate | https://dl.acm.org/doi/10.1145/1143844.1143874 | When PR curves are preferable |
| *A Study of Cross-Validation and Bootstrap for Accuracy Estimation* (Kohavi, 1995) | Intermediate | https://www.ijcai.org/Proceedings/95-2/Papers/016.pdf | Classic comparison of validation strategies |
| *Regularization and Variable Selection via the Elastic Net* (Zou & Hastie, 2005) | Advanced | https://academic.oup.com/jrsssb/article/67/2/301/7109482 | Connects regularization to bias-variance |
| *Visualizing the Loss Landscape of Neural Nets* (Li et al., 2018) | Advanced | https://arxiv.org/abs/1712.09913 | Useful intuition about generalization |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| Cross-Validation with scikit-learn | Beginner | https://scikit-learn.org/stable/modules/cross_validation.html | k-fold, stratified, grouped, and time-series splits |
| ROC Curve Example | Beginner | https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html | ROC visualization in Python |
| Learning Curves Example | Intermediate | https://scikit-learn.org/stable/auto_examples/model_selection/plot_learning_curve.html | Diagnose bias-variance issues |
| Yellowbrick Model Evaluation Gallery | Intermediate | https://www.scikit-yb.org/en/latest/api/model_selection/index.html | Underrated visual diagnostics library |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *Understanding the Bias-Variance Tradeoff* (Scott Fortmann-Roe) | Intermediate | https://scott.fortmann-roe.com/docs/BiasVariance.html | One of the clearest explanations available |
| *ROC Curves and Precision-Recall Curves Explained* | Beginner | https://glassboxmedicine.com/2019/03/02/measuring-performance-auprc/ | Practical guide with examples |
| *Why Accuracy Is Not Enough* | Beginner | https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall | Imbalanced classification perspective |
| *A Gentle Introduction to Cross-Validation* | Beginner | https://machinelearningmastery.com/k-fold-cross-validation/ | Widely referenced practical guide |
| *Yellowbrick: Visual Analysis for Machine Learning* | Intermediate | https://www.scikit-yb.org/ | Underrated toolkit for evaluation and diagnostics |

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
- [Ensemble Methods](ensemble-methods.md) — OOB scores, early stopping, and validation
- [Feature Engineering](feature-engineering.md) — feature importance and selection metrics
- [Classic ML Frameworks](classic-ml-frameworks.md) — scikit-learn's `cross_val_score`, `GridSearchCV`, and evaluation APIs
- [Probability & Statistics](../01-foundations/mathematics/probability-statistics.md) — statistical significance, confidence intervals, and hypothesis testing
- [🧩 Visualizers](../01-foundations/visualizers.md) — interactive ROC, bias-variance, and diagnostics tools
- [🤖 Machine Learning](README.md)
---
