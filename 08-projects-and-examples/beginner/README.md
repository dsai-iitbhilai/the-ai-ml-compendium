# Beginner Projects

> Hands-on projects designed for learners who know Python basics and are starting machine learning.

**Last Reviewed:** 2026-06

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| *Scikit-learn Getting Started* | Beginner | <https://scikit-learn.org/stable/getting_started.html> | The official quickstart guide detailing model configuration and dataset loading. |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| *Build Your First Machine Learning Model* | Beginner | <https://www.youtube.com/watch?v=i_LwzRmA_08> | Live coding walkthrough mapping fundamental algorithms in clean code. |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| *Kaggle Learn — Intro to ML* | Beginner | <https://www.kaggle.com/learn/intro-to-machine-learning> | Interactive micro-course detailing Decision Tree architectures. |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| *Titanic Complete Walkthrough Notebook* | Beginner | <https://www.kaggle.com/code/startupsci/titanic-data-science-solutions> | Comprehensive exploratory analysis and missing value encoding techniques. |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *Beginner ML Projects with Code* | Beginner | <https://machinelearningmastery.com/> | Foundational breakdowns of structural algorithm implementations. |

---

## Project Specifications

### 1. Titanic Survival Predictor (Binary Classification)
* **Description:** Predict passenger survival by modeling demographic and ticket metadata.
* **Skills Practiced:** Categorical One-Hot encoding, data imputation via pandas, Logistic Regression baseline validation.
* **Dataset:** [Kaggle Titanic Dataset](https://www.kaggle.com/c/titanic/data)

### 2. Spam vs. Ham Classifier (NLP Basics)
* **Description:** Classify incoming messages into legitimate or spam blocks.
* **Skills Practiced:** String tokenization, stop-word removal, TF-IDF representations, Naive Bayes evaluation.
* **Dataset:** [UCI SMS Spam Collection](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection)

### 3. House Price Predictor (Multivariate Regression)
* **Description:** Predict real estate pricing indexes using regional structural statistics.
* **Skills Practiced:** Linear Regression, feature normalization via StandardScaler, RMSE logging bounds.
* **Dataset:** [California Housing Dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html)

### 4. Iris Flower Classifier (Multi-Class Classification)
* **Description:** Classify plant species using morphological physical observations.
* **Skills Practiced:** Decision Trees, KNN, building and reading Confusion Matrices.
* **Dataset:** [Iris Dataset (UCI)](https://archive.ics.uci.edu/ml/datasets/iris)

### 5. MNIST Digit Recognizer (Computer Vision Neural Net)
* **Description:** Detect handwritten numeral drawings correctly through multi-class token scoring.
* **Skills Practiced:** Grayscale dimension reshaping, building simple PyTorch CNNs, Softmax probability distribution.
* **Dataset:** [MNIST Database](https://keras.io/api/datasets/mnist/)

---

## Getting Started

1. Set up an isolated python virtual environment (`python -m venv venv`) and execute `pip install scikit-learn pandas matplotlib seaborn`.
2. Choose one dataset destination above and run a clean baseline script.
3. Train at least two distinct algorithms on the splits and compare their mathematical performance.
4. Document a summary analyzing feature importances or error logs.

---

## See also

- [Beginner Projects](README.md)
- [Calculus](../../01-foundations/mathematics/calculus.md)
