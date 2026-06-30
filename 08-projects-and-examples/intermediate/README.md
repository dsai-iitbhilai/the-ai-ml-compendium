# Intermediate Projects

> Multi-component projects requiring production data pipelines, model evaluation frameworks, and deployment.

**Last Reviewed:** 2026-06

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| *DVC + MLflow Ingestion Tutorial* | Intermediate | <https://dvc.org/doc/use-cases/versioning-data-and-models> | Setting up data version files alongside automated tracking tags. |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| *Deploy FastAPI Models to Production* | Intermediate | <https://www.youtube.com/watch?v=F5jwEBaJptM> | Full walkthrough mapping REST API serialization paths and container hosting. |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| *Applied ML with Python* | Intermediate | <https://www.coursera.org/learn/applied-machine-learning-with-python> | Focuses on pipeline architecture selection and advanced validation heuristics. |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| *BERT Sentiment Fine-Tuning Recipe* | Intermediate | <https://huggingface.co/docs/transformers/tasks/sequence_classification> | Comprehensive PyTorch loop compiling text tokens into encoder projections. |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *Building a Recommender System in PyTorch* | Intermediate | <https://magazine.sebastianraschka.com/> | Deep technical guide covering matrix factorization layers and dot-product loss. |

---

## Project Specifications

### 1. Customer Churn Predictor
* **Description:** Identify high-risk subscriber accounts before subscription cycles exhaust.
* **Skills Practiced:** Class imbalance mitigation via SMOTE, XGBoost configuration, structural validation pipelines.
* **Dataset:** [Telco Churn Dataset (Kaggle)](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

### 2. Movie Recommender System
* **Description:** Synthesize personalized matrix prediction graphs matching user indices to content tags.
* **Skills Practiced:** Collaborative filtering, SVD/Matrix Factorization, embedding space calculations.
* **Dataset:** [MovieLens Dataset (GroupLens)](https://grouplens.org/datasets/movielens/)

### 3. Image Classifier Web App
* **Description:** Bundle a convolutional computer vision block inside a clean service gateway.
* **Skills Practiced:** ResNet Transfer Learning, FastAPI interface definition, standalone Docker build configurations.
* **Dataset:** [CIFAR-10 Dataset](https://www.cs.toronto.edu/~kriz/cifar.html)

### 4. Time Series Forecasting System
* **Description:** Predict numerical demand trends or asset movements across explicit temporal fields.
* **Skills Practiced:** Stationarity tests (ADF), LSTM sequential design, Prophet seasonal trends.
* **Dataset:** [Yahoo Finance Historical Feeds](https://finance.yahoo.com/)

### 5. Sentiment Analysis Pipeline
* **Description:** Parse deep linguistic emotional signals from text strings through transformer fine-tuning.
* **Skills Practiced:** HuggingFace `Trainer` configuration, custom tokenizers, gradient descent parameter freezing.
* **Dataset:** [IMDb Movie Reviews Dataset](https://huggingface.co/datasets/imdb)

---

## Suggested Extensions

* Implement an explicit A/B testing framework or shadow routing pattern via the API router.
* Establish automated workflow retraining tasks using GitHub Actions when data signatures fluctuate.
* Containerize the components securely using a multi-stage `docker-compose.yml` framework.
* Inject continuous drift tracking loops via `Evidently AI` reporting profiles.

---

## See also

- [Fine-Tuning & PEFT](../../05-generative-ai/fine-tuning-and-peft.md)
- [CI/CD for Machine Learning](../../07-mlops-and-deployment/ci-cd-for-ml.md)
- [Monitoring & Observability](../../07-mlops-and-deployment/monitoring-and-observability.md)
