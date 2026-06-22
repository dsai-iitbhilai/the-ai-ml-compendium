# Classic ML Frameworks

> The essential libraries for building, training, and evaluating classical machine learning models in Python.

**Last Reviewed:** 2026-06

**Prerequisites:** [Supervised Learning](supervised-learning.md), [Python for AI](../01-foundations/programming/python-for-ai.md)

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| Scikit-learn — User Guide & API Reference | Beginner | [Link](https://example.com/sklearn-docs) | Complete reference for all classical ML models |
| XGBoost Documentation | Intermediate | [Link](https://example.com/xgboost-docs) | Parameters, GPU support, distributed training |
| LightGBM Documentation | Intermediate | [Link](https://example.com/lightgbm-docs) | Leaf-wise growth, categorical feature handling |
| CatBoost Documentation | Intermediate | [Link](https://example.com/catboost-docs) | Ordered boosting, native categorical support |
| imbalanced-learn Documentation | Intermediate | [Link](https://example.com/imblearn-docs) | Resampling and ensemble methods for imbalanced data |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| Scikit-learn Crash Course — Corey Schafer | Beginner | [Link](https://example.com/sklearn-crash) | Full walkthrough: loading, training, evaluating |
| XGBoost Explained (Data School) | Intermediate | [Link](https://example.com/xgboost-dataschool) | Parameter tuning and feature importance |
| CatBoost Tutorial — Handling Categorical Data | Intermediate | [Link](https://example.com/catboost-tutorial) | How CatBoost handles categoricals natively |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| Kaggle — Intro to Machine Learning (scikit-learn) | Beginner | [Link](https://example.com/kaggle-intro-sklearn) | Hands-on intro with scikit-learn pipelines |
| Kaggle — Intermediate ML (XGBoost & LightGBM) | Intermediate | [Link](https://example.com/kaggle-intermediate-xgb) | XGBoost, LightGBM, and hyperparameter tuning |
| DataCamp — Machine Learning with scikit-learn | Beginner | [Link](https://example.com/datacamp-sklearn) | 4-hour interactive course |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| Yellowbrick — Visual Model Diagnostics | Intermediate | [Link](https://example.com/yellowbrick) | Scikit-learn-compatible visualizers for model evaluation |
| Scikit-learn Algorithm Cheat Sheet | Beginner | [Link](https://example.com/sklearn-cheatsheet) | Interactive flow chart for choosing estimators |
| XGBoost Parameter Explorer | Intermediate | [Link](https://example.com/xgb-params) | Interactive tuning of boosting parameters |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *Scikit-learn: Machine Learning in Python* (Pedregosa et al., 2011) | Intermediate | [Link](https://example.com/sklearn-paper) | The original JMLR paper |
| *XGBoost: A Scalable Tree Boosting System* (Chen & Guestrin, 2016) | Advanced | [Link](https://example.com/xgboost-paper) | Industrial-grade gradient boosting |
| *LightGBM: A Highly Efficient Gradient Boosting Decision Tree* (Ke et al., 2017) | Advanced | [Link](https://example.com/lightgbm-paper) | GOSS and EFB innovations |
| *CatBoost: Unbiased Boosting with Categorical Features* (Prokhorenkova et al., 2018) | Advanced | [Link](https://example.com/catboost-paper) | Ordered boosting and symmetric trees |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| Scikit-learn Pipeline + GridSearchCV | Beginner | [Link](https://example.com/sklearn-pipeline) | End-to-end with ColumnTransformer |
| XGBoost vs LightGBM vs CatBoost Benchmark | Intermediate | [Link](https://example.com/boosting-bench) | Speed, accuracy, and memory comparison |
| Handling Imbalanced Data with imbalanced-learn | Intermediate | [Link](https://example.com/imblearn-bench) | SMOTE, ADASYN, and balanced ensemble methods |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *Scikit-learn, XGBoost, LightGBM, CatBoost: A Complete Comparison* | Intermediate | [Link](https://example.com/framework-comparison) | When to reach for each library |
| *Building Robust Pipelines with scikit-learn* | Beginner | [Link](https://example.com/sklearn-pipelines-blog) | Reproducible ML workflow best practices |

---

## Key Concepts Checklist

- [ ] Scikit-learn API (fit, predict, transform, score, Pipeline)
- [ ] Scikit-learn preprocessing (ColumnTransformer, encoders, scalers)
- [ ] Model selection (cross_val_score, GridSearchCV, RandomizedSearchCV)
- [ ] XGBoost (DMatrix, custom objectives, early stopping, GPU training)
- [ ] LightGBM (Dataset, leaf-wise growth, categorical_feature param)
- [ ] CatBoost (CatBoostClassifier/Regressor, native categoricals, eval metrics)
- [ ] imbalanced-learn (SMOTE, RandomUnderSampler, BalancedRandomForest)
- [ ] Yellowbrick visualizers (confusion matrix, ROC, feature importance)
- [ ] Model persistence (joblib, pickle, ONNX export)
- [ ] Reproducibility (random_state, seeding, deterministic training)

---

## Projects / Practice

| Project | Description |
|---|---|
| Build a Scikit-learn Pipeline | Create a complete training pipeline with ColumnTransformer, model, and GridSearchCV |
| Boosting Showdown | Compare XGBoost, LightGBM, and CatBoost on the same dataset with tuned hyperparameters |
| Imbalanced Classification Benchmark | Use imbalanced-learn to combine SMOTE with different classifiers on a fraud dataset |

---

## See also

- [Supervised Learning](supervised-learning.md) — algorithms implemented in these frameworks
- [Ensemble Methods](ensemble-methods.md) — deeper dive into boosting and bagging
- [Feature Engineering](feature-engineering.md) — preprocessing components in scikit-learn
- [Model Evaluation](model-evaluation.md) — cross-validation and scoring in these frameworks
