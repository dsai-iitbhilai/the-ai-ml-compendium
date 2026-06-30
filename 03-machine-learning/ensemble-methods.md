# Ensemble Methods

> Combining multiple models to achieve better performance than any single model. Covers bagging, random forests, gradient boosting, and modern implementations like XGBoost and LightGBM.

**Last Reviewed:** 2026-06

**Prerequisites:** [Supervised Learning](supervised-learning.md) (decision trees in particular)

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| Scikit-learn — Ensemble Methods User Guide | Beginner | <https://scikit-learn.org/stable/modules/ensemble.html> | Official docs with code for RF, GBM, AdaBoost |
| XGBoost Documentation | Intermediate | <https://xgboost.readthedocs.io/en/stable/> | Parameters, tuning guide, and tutorials |
| LightGBM Documentation | Intermediate | <https://lightgbm.readthedocs.io/en/latest/> | Leaf-wise growth, categorical feature support |
| *Elements of Statistical Learning* — Chapters 15–16 | Advanced | <https://hastie.su.domains/ElemStatLearn/> | Theoretical foundation for boosting and bagging (Free) |
| CatBoost Documentation | Intermediate | <https://catboost.ai/docs/> | Ordered boosting and categorical feature handling |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| StatQuest: Random Forests Clearly Explained | Beginner | <https://www.youtube.com/watch?v=J4Wdy0Wc_xQ> | Excellent intuition for bagging and RF |
| StatQuest: Gradient Boosting Clearly Explained | Beginner | <https://www.youtube.com/watch?v=3CC4N4z3GJc> | Step-by-step walkthrough of boosting |
| XGBoost Explained (Data School) | Intermediate | <https://www.youtube.com/watch?v=OtD8wVaFm6E> | Covers tuning and feature importance |
| CatBoost Explained | Intermediate | <https://www.youtube.com/watch?v=tpl9GoB0B3A> | Native handling of categorical features |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| Kaggle — Intermediate Machine Learning | Beginner | <https://www.kaggle.com/learn/intermediate-machine-learning> | Random forests, XGBoost, leakage, pipelines |
| Harvard CS109A — Ensemble Methods Lecture | Intermediate | <https://harvard-iacs.github.io/2017-CS109A/sections/s-section8/notebook/> | Academic treatment with examples |
| Fast.ai Machine Learning Course | Intermediate | <https://course18.fast.ai/ml> | Practical gradient boosting with real datasets |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| Yellowbrick Feature Importances | Intermediate | <https://www.scikit-yb.org/en/latest/api/model_selection/importances.html> | Visualise ensemble feature importance |
| Scikit-learn Algorithm Cheat Sheet | Beginner | <https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html> | Interactive estimator selection |
| SHAP Interactive Examples | Intermediate | <https://shap.readthedocs.io/en/latest/example_notebooks.html> | Understand boosting model predictions |
| TensorFlow Playground | Beginner | <https://playground.tensorflow.org> | Useful for intuition about ensemble-like decision boundaries |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *Random Forests* (Breiman, 2001) | Advanced | <https://link.springer.com/article/10.1023/A:1010933404324> | Seminal paper introducing random forests |
| *Greedy Function Approximation: A Gradient Boosting Machine* (Friedman, 2001) | Advanced | <https://projecteuclid.org/journals/annals-of-statistics/volume-29/issue-5/Greedy-Function-Approximation-A-Gradient-Boosting-Machine/10.1214/aos/1013203451.full> | Original gradient boosting paper |
| *XGBoost: A Scalable Tree Boosting System* (Chen & Guestrin, 2016) | Advanced | <https://arxiv.org/abs/1603.02754> | Industrial-strength boosting |
| *LightGBM: A Highly Efficient Gradient Boosting Decision Tree* (Ke et al., 2017) | Advanced | <https://proceedings.neurips.cc/paper_files/paper/2017/hash/6449f44a102fde848669bdd9eb6b76fa-Abstract.html> | GOSS and EFB innovations |
| *CatBoost: Unbiased Boosting with Categorical Features* (Prokhorenkova et al., 2018) | Advanced | <https://arxiv.org/abs/1706.09516> | Ordered boosting and symmetric trees |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| Random Forest Classifier with scikit-learn | Beginner | <https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html> | Official RF example |
| XGBoost Python Examples | Intermediate | <https://xgboost.readthedocs.io/en/stable/python/examples/index.html> | Training, tuning, and early stopping |
| LightGBM Examples | Intermediate | <https://github.com/microsoft/LightGBM/tree/master/examples> | Official examples repository |
| CatBoost Tutorials | Intermediate | <https://github.com/catboost/tutorials> | Official notebooks and examples |
| Implementing Gradient Boosting from Scratch | Advanced | <https://github.com/eriklindernoren/ML-From-Scratch/blob/master/mlfromscratch/supervised_learning/gradient_boosting.py> | Understand internals from source code |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *A Visual Guide to Gradient Boosting* | Beginner | <https://explained.ai/gradient-boosting/> | One of the clearest boosting explanations online |
| *CatBoost vs LightGBM vs XGBoost: Which One to Use?* | Intermediate | <https://neptune.ai/blog/xgboost-vs-lightgbm> | Practical comparison and benchmarks |
| *Stacking, Blending, and Voting Ensembles* | Intermediate | <https://machinelearningmastery.com/stacking-ensemble-machine-learning-with-python/> | Combining diverse models effectively |
| *Interpretable Boosting Machines (EBM)* | Intermediate | <https://interpret.ml/docs/ebm.html> | Underrated glass-box ensemble method |

---

## Key Concepts Checklist

- Bagging (bootstrap aggregation, variance reduction)
- Random forests (feature subsampling, out-of-bag error, variable importance)
- Boosting (additive modeling, stagewise fitting, residual correction)
- Gradient boosting (loss function, gradient descent in function space)
- XGBoost (regularized boosting, column block, cache-aware access)
- LightGBM (GOSS, EFB, leaf-wise tree growth)
- CatBoost (ordered boosting, symmetric trees, categorical encoding)
- Stacking / Blending (meta-learner, base model diversity)
- Hyperparameter tuning for ensembles (n_estimators, learning_rate, subsample, max_depth)
- Early stopping and monitoring (validation set, OOB score)

---

## Projects / Practice

| Project | Description |
|---|---|
| Tabular Playground — Kaggle Competitions | Apply RF, XGBoost, LightGBM to a regression or classification task |
| Stacking Toolkit | Build a meta-ensemble using RF, XGBoost, and a linear model as base learners |
| Hyperparameter Optimization Study | Systematic comparison of grid search, random search, and Bayesian optimization for boosting |

---

## See also

- [Supervised Learning](supervised-learning.md) — base learners (decision trees, linear models)
- [Model Evaluation](model-evaluation.md) — cross-validation, OOB scoring, feature importance
- [Classic ML Frameworks](classic-ml-frameworks.md) — scikit-learn, XGBoost, LightGBM, CatBoost
- [Feature Engineering](feature-engineering.md) — prepares data for tree- and linear-based ensembles
