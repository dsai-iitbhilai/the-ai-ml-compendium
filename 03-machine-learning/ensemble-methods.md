# Ensemble Methods

> Combining multiple models to achieve better performance than any single model. Covers bagging, random forests, gradient boosting, and modern implementations like XGBoost and LightGBM.

**Last Reviewed:** 2026-06

**Prerequisites:** [Supervised Learning](supervised-learning.md) (decision trees in particular)

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| Scikit-learn — Ensemble Methods User Guide | Beginner | [Link](https://example.com/sklearn-ensemble) | Official docs with code for RF, GBM, AdaBoost |
| XGBoost Documentation | Intermediate | [Link](https://example.com/xgboost-docs) | Parameters, tuning guide, and tutorials |
| LightGBM Documentation | Intermediate | [Link](https://example.com/lightgbm-docs) | Leaf-wise growth, categorical feature support |
| *Elements of Statistical Learning* — Chapters 15–16 | Advanced | [Link](https://example.com/esl-ch15-16) | Theoretical foundation for boosting and bagging |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| StatQuest: Random Forests Clearly Explained | Beginner | [Link](https://example.com/statquest-rf) | Best first intuition for bagging and RF |
| StatQuest: Gradient Boosting Clearly Explained | Beginner | [Link](https://example.com/statquest-gbm) | Step-by-step walkthrough of boosting |
| XGBoost Explained (YouTube series) | Intermediate | [Link](https://example.com/xgboost-vid) | Covers regularization, tree pruning, and GPU training |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| Kaggle — Intermediate Machine Learning | Beginner | [Link](https://example.com/kaggle-intermediate-ml) | Hands-on: random forests, XGBoost, hyperparameter tuning |
| Harvard CS 109A — Ensemble Methods Lecture | Intermediate | [Link](https://example.com/harvard-cs109a-ensemble) | Academic lecture with case studies |
| Fast.ai — Introduction to Gradient Boosting | Intermediate | [Link](https://example.com/fastai-boosting) | Practical implementation with notebooks |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| Random Forest Explorer | Beginner | [Link](https://example.com/rf-explorer) | See how many trees reduce variance |
| Gradient Boosting Simulation | Intermediate | [Link](https://example.com/gbm-sim) | Step through each additive tree |
| XGBoost Parameter Tuning Playground | Intermediate | [Link](https://example.com/xgb-param-viz) | Adjust learning rate, max_depth, subsample in real time |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *Random Forests* (Breiman, 2001) | Advanced | [Link](https://example.com/breiman-rf) | Seminal paper introducing random forests |
| *Greedy Function Approximation: A Gradient Boosting Machine* (Friedman, 2001) | Advanced | [Link](https://example.com/friedman-gbm) | Original gradient boosting paper |
| *XGBoost: A Scalable Tree Boosting System* (Chen & Guestrin, 2016) | Advanced | [Link](https://example.com/xgboost-paper) | Industrial-strength boosting with system optimization |
| *LightGBM: A Highly Efficient Gradient Boosting Decision Tree* (Ke et al., 2017) | Advanced | [Link](https://example.com/lightgbm-paper) | GOSS and EFB innovations for speed |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| Random Forest Classifier with scikit-learn | Beginner | [Link](https://example.com/sklearn-rf) | Minimal working example on Iris |
| XGBoost — From API to Tuning | Intermediate | [Link](https://example.com/xgboost-tune) | Grid search and early stopping with XGBoost |
| LightGBM vs XGBoost Benchmark | Intermediate | [Link](https://example.com/lgbm-xgb-bench) | Speed and accuracy comparison on tabular data |
| Implementing Gradient Boosting from Scratch | Advanced | [Link](https://example.com/boosting-scratch) | Build a simple GBM in NumPy to understand internals |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *A Visual Guide to Gradient Boosting* | Beginner | [Link](https://example.com/visual-boosting) | Illustrations of each boosting iteration |
| *CatBoost vs LightGBM vs XGBoost: Which One to Use?* | Intermediate | [Link](https://example.com/catboost-vs-lgbm-xgb) | Practical comparison with benchmarks |
| *Stacking, Blending, and Voting Ensembles* | Intermediate | [Link](https://example.com/stacking-guide) | How to combine diverse models effectively |

---

## Key Concepts Checklist

- [ ] Bagging (bootstrap aggregation, variance reduction)
- [ ] Random forests (feature subsampling, out-of-bag error, variable importance)
- [ ] Boosting (additive modeling, stagewise fitting, residual correction)
- [ ] Gradient boosting (loss function, gradient descent in function space)
- [ ] XGBoost (regularized boosting, column block, cache-aware access)
- [ ] LightGBM (GOSS, EFB, leaf-wise tree growth)
- [ ] CatBoost (ordered boosting, symmetric trees, categorical encoding)
- [ ] Stacking / Blending (meta-learner, base model diversity)
- [ ] Hyperparameter tuning for ensembles (n_estimators, learning_rate, subsample, max_depth)
- [ ] Early stopping and monitoring (validation set, OOB score)

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
