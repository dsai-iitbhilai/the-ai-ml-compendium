# Feature Engineering

> The process of transforming raw data into features that better represent the underlying problem. Covers selection, extraction, encoding, and scaling.

**Last Reviewed:** 2026-06

**Prerequisites:** [02 – Data Science / Data Wrangling](../02-data-science/data-wrangling.md), [Supervised Learning](supervised-learning.md)

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| Scikit-learn — Preprocessing & Feature Selection Guide | Beginner | <https://scikit-learn.org/stable/modules/preprocessing.html> | Official docs: encoders, scalers, selectors |
| *Feature Engineering for Machine Learning* (Zheng & Casari, 2018) | Beginner | <https://www.oreilly.com/library/view/feature-engineering-for/9781491953235/> | Practical cookbook with Python examples (Paid) |
| *Feature Engineering and Selection* (Kuhn & Johnson, 2019) | Intermediate | <https://bookdown.org/max/FES/> | Theory-grounded with practical examples (Free) |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| Feature Scaling — Standardization vs Normalization (StatQuest) | Beginner | <https://www.youtube.com/watch?v=822-rqxLdfs> | When and why scaling matters |
| One-Hot Encoding vs Label Encoding | Beginner | <https://www.youtube.com/watch?v=InZJ0jsi5bA> | Categorical encoding explained |
| Feature Selection in Machine Learning (StatQuest) | Intermediate | <https://www.youtube.com/watch?v=HMOI_lkzW08> | Filter, wrapper, and embedded methods |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| Kaggle — Feature Engineering Micro-Course | Beginner | <https://www.kaggle.com/learn/feature-engineering> | Free: target encoding, PCA, clustering features |
| Coursera — Feature Engineering (Google Cloud) | Intermediate | <https://www.coursera.org/learn/feature-engineering> | Production-oriented feature engineering |
| DataCamp — Feature Engineering for Machine Learning in Python | Beginner | <https://www.datacamp.com/courses/feature-engineering-for-machine-learning-in-python> | Interactive exercises |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| PCA Playground | Intermediate | <https://setosa.io/ev/principal-component-analysis/> | Visualize PCA projections and explained variance |
| Scikit-learn Algorithm Cheat Sheet | Beginner | <https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html> | Understand preprocessing/model choices |
| SHAP Interactive Examples | Intermediate | <https://shap.readthedocs.io/en/latest/example_notebooks.html> | Understand feature contributions |
| Featuretools Demo Gallery | Intermediate | <https://docs.featuretools.com/en/stable/getting_started/afe.html> | Automated feature engineering examples |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *Feature Selection Based on Mutual Information* (Battiti, 1994) | Advanced | <https://ieeexplore.ieee.org/document/368378> | Early work on filter-based selection |
| *Regularization and Variable Selection via the Elastic Net* (Zou & Hastie, 2005) | Advanced | <https://academic.oup.com/jrsssb/article/67/2/301/7109482> | Embedded feature selection with L1/L2 |
| *A Preprocessing Scheme for High-Cardinality Categorical Attributes* (Micci-Barreca, 2001) | Intermediate | <https://dl.acm.org/doi/10.1145/507533.507538> | Foundation of target encoding |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| Scaling & Encoding Pipeline with scikit-learn | Beginner | <https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html> | ColumnTransformer example |
| Recursive Feature Elimination (RFE) Example | Intermediate | <https://scikit-learn.org/stable/auto_examples/feature_selection/plot_rfe_with_cross_validation.html> | Wrapper-based feature selection |
| Automated Feature Engineering with Featuretools | Intermediate | <https://github.com/alteryx/featuretools/tree/main/docs/source/getting_started> | Deep feature synthesis |
| tsfresh Examples | Intermediate | <https://tsfresh.readthedocs.io/en/latest/text/introduction.html> | Automated time-series feature extraction |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *A Comprehensive Guide to Encoding Categorical Variables* | Beginner | <https://www.kdnuggets.com/2019/12/understanding-encoding-categorical-features.html> | One-hot, target, ordinal, frequency encoding |
| *Feature Engineering: The Secret Sauce of Machine Learning* | Intermediate | <https://christophm.github.io/interpretable-ml-book/feature-importance.html> | Practical feature engineering insights |
| *Don't Use One-Hot Encoding for High-Cardinality Features* | Intermediate | <https://maxhalford.github.io/blog/target-encoding/> | Alternatives: target encoding and hashing |
| *Featuretools: Automatically Creating Features from Relational Data* | Intermediate | <https://www.featuretools.com/> | Underrated automated feature engineering framework |

---

## Key Concepts Checklist

- Scaling methods (StandardScaler, MinMaxScaler, RobustScaler, MaxAbsScaler)
- Normalization vs standardization
- Categorical encoding (one-hot, label, ordinal, target, binary, frequency)
- Handling high-cardinality categoricals
- Feature selection (filter: correlation, chi², mutual info; wrapper: RFE, forward/backward; embedded: Lasso, tree importance)
- Feature extraction (PCA, LDA, t-SNE, autoencoders)
- Polynomial features and interaction terms
- Binning and discretization
- Target leakage — what it is and how to avoid it
- Pipelines (ColumnTransformer, Pipeline, FeatureUnion)
- Automated feature engineering (Featuretools, tsfresh)

---

## Projects / Practice

| Project | Description |
|---|---|
| Feature Engineering on House Prices | Apply scaling, encoding, polynomial features, and selection to the Ames dataset |
| Encoding Benchmark | Compare one-hot, target, and frequency encoding across linear and tree models |
| Automated Feature Pipeline | Build a reusable ColumnTransformer pipeline with scaling, encoding, and feature selection |

---

## See also

- [Supervised Learning](supervised-learning.md) — where engineered features are consumed
- [Model Evaluation](model-evaluation.md) — feature importance and selection metrics
- [Classic ML Frameworks](classic-ml-frameworks.md) — scikit-learn's `Pipeline`, `ColumnTransformer`, `SelectKBest`
- [02 – Data Science / Data Wrangling](../02-data-science/data-wrangling.md) — cleaning data before engineering features
