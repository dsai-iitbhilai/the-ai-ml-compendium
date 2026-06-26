# Classic ML Frameworks

> The essential libraries for building, training, and evaluating classical machine learning models in Python.

**Last Reviewed:** 2026-06

**Prerequisites:** [Supervised Learning](supervised-learning.md), [Python for AI](../01-foundations/programming/python-for-ai.md)

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| Scikit-learn — User Guide & API Reference | Beginner | https://scikit-learn.org/stable/user_guide.html | Complete reference for classical ML models |
| XGBoost Documentation | Intermediate | https://xgboost.readthedocs.io/en/stable/ | Parameters, GPU support, distributed training |
| LightGBM Documentation | Intermediate | https://lightgbm.readthedocs.io/en/latest/ | Leaf-wise growth, categorical feature handling |
| CatBoost Documentation | Intermediate | https://catboost.ai/docs/ | Ordered boosting, native categorical support |
| imbalanced-learn Documentation | Intermediate | https://imbalanced-learn.org/stable/ | Resampling and ensemble methods for imbalanced data |
| Yellowbrick Documentation | Intermediate | https://www.scikit-yb.org/en/latest/ | Visual diagnostics for scikit-learn models |
| PyCaret Documentation | Intermediate | https://pycaret.gitbook.io/docs/ | Low-code ML experimentation framework |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| Scikit-learn Crash Course — Corey Schafer | Beginner | https://www.youtube.com/watch?v=0B5eIE_1vpU | Full walkthrough of sklearn workflows |
| Machine Learning with Scikit-learn (freeCodeCamp) | Beginner | https://www.youtube.com/watch?v=i_LwzRVP7bg | End-to-end practical introduction |
| XGBoost Explained (Data School) | Intermediate | https://www.youtube.com/watch?v=OtD8wVaFm6E | Feature importance and tuning |
| CatBoost Tutorial | Intermediate | https://www.youtube.com/watch?v=tpl9GoB0B3A | Native categorical handling |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| Kaggle — Intro to Machine Learning | Beginner | https://www.kaggle.com/learn/intro-to-machine-learning | Hands-on scikit-learn introduction |
| Kaggle — Intermediate Machine Learning | Intermediate | https://www.kaggle.com/learn/intermediate-machine-learning | Pipelines, leakage, XGBoost |
| Applied Machine Learning in Python (University of Michigan) | Intermediate | https://www.coursera.org/learn/python-machine-learning | Practical sklearn-focused course |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| Yellowbrick Visual Diagnostics | Intermediate | https://www.scikit-yb.org/en/latest/ | Model evaluation and diagnostics |
| Scikit-learn Algorithm Cheat Sheet | Beginner | https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html | Choose the right estimator |
| ExplainerDashboard | Intermediate | https://explainerdashboard.readthedocs.io/en/latest/ | Interactive model explanations |
| SHAP Interactive Examples | Intermediate | https://shap.readthedocs.io/en/latest/example_notebooks.html | Feature attribution visualizations |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *Scikit-learn: Machine Learning in Python* (Pedregosa et al., 2011) | Intermediate | https://jmlr.org/papers/v12/pedregosa11a.html | Original sklearn paper |
| *XGBoost: A Scalable Tree Boosting System* (Chen & Guestrin, 2016) | Advanced | https://arxiv.org/abs/1603.02754 | Industrial-grade boosting |
| *LightGBM: A Highly Efficient Gradient Boosting Decision Tree* (Ke et al., 2017) | Advanced | https://proceedings.neurips.cc/paper_files/paper/2017/hash/6449f44a102fde848669bdd9eb6b76fa-Abstract.html | GOSS and EFB innovations |
| *CatBoost: Unbiased Boosting with Categorical Features* (Prokhorenkova et al., 2018) | Advanced | https://arxiv.org/abs/1706.09516 | Ordered boosting |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| Scikit-learn Pipeline + GridSearchCV | Beginner | https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html | End-to-end ColumnTransformer example |
| XGBoost Documentation Examples | Intermediate | https://xgboost.readthedocs.io/en/stable/python/examples/index.html | Official examples |
| LightGBM Examples | Intermediate | https://github.com/microsoft/LightGBM/tree/master/examples | Official training examples |
| Handling Imbalanced Data with imbalanced-learn | Intermediate | https://imbalanced-learn.org/stable/auto_examples/index.html | SMOTE and resampling examples |
| PyCaret Tutorials | Intermediate | https://pycaret.gitbook.io/docs/learn-pycaret/official-blog | AutoML workflows |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *Scikit-learn, XGBoost, LightGBM, CatBoost: A Complete Comparison* | Intermediate | https://neptune.ai/blog/xgboost-vs-lightgbm | Practical framework comparison |
| *Building Robust Pipelines with scikit-learn* | Beginner | https://scikit-learn.org/stable/modules/compose.html | Reproducible ML workflows |
| *Interpreting Machine Learning Models with SHAP* | Intermediate | https://christophm.github.io/interpretable-ml-book/shap.html | Explainability for tree models |

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
