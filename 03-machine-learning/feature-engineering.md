# Feature Engineering

> The process of transforming raw data into features that better represent the underlying problem. Covers selection, extraction, encoding, and scaling.

**Last Reviewed:** 2026-06

**Prerequisites:** [02 – Data Science / Data Wrangling](../02-data-science/data-wrangling.md), [Supervised Learning](supervised-learning.md)

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| Scikit-learn — Preprocessing & Feature Selection Guide | Beginner | [Link](https://example.com/sklearn-preprocessing) | Official docs: encoders, scalers, selectors |
| *Feature Engineering for Machine Learning* (Zheng & Casari, 2018) | Beginner | [Link](https://example.com/feat-eng-book) | Practical cookbook with Python examples |
| *Feature Engineering and Selection* (Kuhn & Johnson, 2019) | Intermediate | [Link](https://example.com/feat-eng-kuhn) | Theory-grounded with R/Python code |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| Feature Scaling — Standardization vs Normalization | Beginner | [Link](https://example.com/scale-video) | When to use StandardScaler vs MinMaxScaler |
| One-Hot Encoding vs Label Encoding | Beginner | [Link](https://example.com/encoding-video) | Categorical variable encoding explained |
| Feature Selection in Machine Learning | Intermediate | [Link](https://example.com/feat-select-video) | Filter, wrapper, and embedded methods |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| Kaggle — Feature Engineering Micro-Course | Beginner | [Link](https://example.com/kaggle-feat-eng) | Free: target encoding, binning, PCA features |
| Coursera — Feature Engineering (Google Cloud) | Intermediate | [Link](https://example.com/gcp-feat-eng) | Production-oriented feature engineering |
| DataCamp — Feature Engineering for ML in Python | Beginner | [Link](https://example.com/datacamp-feat-eng) | Interactive exercises with real datasets |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| Feature Scaling Visualizer | Beginner | [Link](https://example.com/scaling-viz) | See how StandardScaler, MinMax, Robust affect distributions |
| One-Hot vs Target Encoding Explorer | Intermediate | [Link](https://example.com/encoding-viz) | Compare encoding schemes on categorical data |
| PCA Feature Projection Viewer | Intermediate | [Link](https://example.com/pca-projection) | Visualize variance captured by each principal component |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *Feature Selection Based on Mutual Information* (Battiti, 1994) | Advanced | [Link](https://example.com/mutual-info-paper) | Early work on filter-based selection |
| *Regularization and Variable Selection via the Elastic Net* (Zou & Hastie, 2005) | Advanced | [Link](https://example.com/elastic-net) | Embedded feature selection with L1/L2 |
| *Target Encoding Done Right* (Micci-Barreca, 2001) | Intermediate | [Link](https://example.com/target-encoding) | Avoiding target leakage with cross-validation |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| Scaling & Encoding Pipeline with scikit-learn | Beginner | [Link](https://example.com/sklearn-pipeline) | ColumnTransformer example |
| Recursive Feature Elimination (RFE) — Notebook | Intermediate | [Link](https://example.com/rfe-notebook) | Wrapper-based feature selection |
| Automated Feature Engineering with Featuretools | Intermediate | [Link](https://example.com/featuretools-demo) | Deep feature synthesis for relational data |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *A Comprehensive Guide to Encoding Categorical Variables* | Beginner | [Link](https://example.com/encoding-blog) | One-hot, label, ordinal, target, and binary encoding |
| *Feature Engineering: The Secret to Kaggle Success* | Intermediate | [Link](https://example.com/kaggle-feat-secret) | Practical tips from top competitors |
| *Don't Use One-Hot Encoding for High-Cardinality Features* | Intermediate | [Link](https://example.com/high-cardinality) | Alternatives: target encoding, hashing, embedding |

---

## Key Concepts Checklist

- [ ] Scaling methods (StandardScaler, MinMaxScaler, RobustScaler, MaxAbsScaler)
- [ ] Normalization vs standardization
- [ ] Categorical encoding (one-hot, label, ordinal, target, binary, frequency)
- [ ] Handling high-cardinality categoricals
- [ ] Feature selection (filter: correlation, chi², mutual info; wrapper: RFE, forward/backward; embedded: Lasso, tree importance)
- [ ] Feature extraction (PCA, LDA, t-SNE, autoencoders)
- [ ] Polynomial features and interaction terms
- [ ] Binning and discretization
- [ ] Target leakage — what it is and how to avoid it
- [ ] Pipelines (ColumnTransformer, Pipeline, FeatureUnion)
- [ ] Automated feature engineering (Featuretools, tsfresh)

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
