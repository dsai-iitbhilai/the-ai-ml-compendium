# CI/CD for Machine Learning (MLOps)

> Automating the machine learning lifecycle: experiment tracking, data versioning, continuous training (CT), and continuous deployment (CD). This file covers the transition from static Jupyter notebooks to highly orchestrated, reproducible production pipelines.

**Last Reviewed:** 2026-06

**Prerequisites:** [Tool Use & Function Calling](../docs/06-agentic-ai/fundamentals/tool-use-and-function-calling.md) · [Agent Evaluation & Production](../visualizers-and-playgrounds/README.md)

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| *MLflow Documentation* | Intermediate | <https://mlflow.org/docs/latest/index.html> | The industry standard for experiment tracking, model registry, and serving packaging. |
| *DVC (Data Version Control) Docs* | Intermediate | <https://dvc.org/doc> | Essential for versioning large datasets and connecting them to Git commits via DAGs. |
| *ZenML Documentation* | Intermediate | <https://docs.zenml.io/> | Python-first MLOps framework that creates agnostic pipelines across AWS, GCP, and local environments. |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| *Building ML Pipelines with TFX* (Google Cloud) | Advanced | <https://www.youtube.com/watch?v=VDGhtZAwuWc> | Production pipeline orchestration using TensorFlow Extended (TFX) for massive scale. |
| *MLOps for Beginners* (FreeCodeCamp) | Beginner | <https://www.youtube.com/watch?v=mDjeX9v6Dpo> | Excellent crash course covering MLflow, DVC, and GitHub actions setup. |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| *MLOps Specialization* (DeepLearning.AI) | Intermediate | <https://www.deeplearning.ai/courses/machine-learning-engineering-for-production-mlops/> | Comprehensive 4-course track by Andrew Ng covering the full CI/CD/CT lifecycle. |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| *Weights & Biases (WandB)* | Intermediate | <https://wandb.ai/site> | Leading SaaS platform for visualizing hyperparameter sweeps, GPU utilization, and model artifacts in real-time. |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *Hidden Technical Debt in Machine Learning Systems* (Sculley et al., 2015) | Beginner | <https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems.pdf> | The seminal paper from Google explaining why ML code is only 5% of a production ML system. |
| *Machine Learning Operations (MLOps): Overview, Definition, and Architecture* (Kreuzberger et al., 2023) | Intermediate | <https://arxiv.org/abs/2205.02302> | Academic literature review formalizing the architecture of CI/CD/CT loops. |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| *GitHub Actions ML Pipeline Example* | Intermediate | <https://github.com/iterative/cml> | Continuous Machine Learning (CML) library for injecting model training metrics directly into GitHub PR comments. |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *ML CI/CD Best Practices* (neptune.ai) | Intermediate | <https://neptune.ai/blog/ml-ci-cd-machine-learning-pipeline> | Detailed branch strategies, pipeline stages, and artifact management for ML engineering teams. |
| *MLOps: Continuous delivery and automation pipelines in ML* (Google) | Advanced | <https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning> | Defines MLOps Level 0 (Manual), Level 1 (Pipeline Automation), and Level 2 (CI/CD Pipeline Automation). |

---

## ML Pipeline Stages (CI/CD/CT View)

Unlike traditional software engineering (CI/CD), Machine Learning introduces Continuous Training (CT) — automatically retraining models as data distributions drift.

```text
Code Commit → Lint/Test → Train → Evaluate → Register → Deploy → Monitor
    ↑                                                              │
    └──────────────────── Continuous Training (CT) ────────────────┘
```

---

## Experiment Tracking & Registry

| Tool | Key Features |
|---|---|
| **MLflow** | Open-source; excellent Model Registry (Staging/Production tags); integrates heavily with Databricks. |
| **Weights & Biases** | SaaS; visually rich dashboards, collaborative reports, automated hyperparameter sweeping. |
| **Neptune.ai** | Flexible metadata store specializing in handling complex, unstructured artifact data. |
| **Comet.ml** | Experiment comparison, dataset versioning, and robust enterprise deployment management. |

---

## Model Registry & Deployment Patterns

- **Staging / QA:** A protected environment where a newly trained model is tested for latency and integration before seeing real traffic.
- **Production (Active):** The live model handling user inference requests.
- **Shadow Mode (Champion/Challenger):** The new model (Challenger) receives real production traffic alongside the current model (Champion), but its predictions are only logged, not returned to the user, to ensure zero-risk evaluation.
- **Canary Release:** Progressively routing a small percentage of traffic (e.g., 5%) to the new model to monitor for fatal errors before a full rollout.
- **A/B Testing:** Routing traffic mathematically (50/50) to evaluate business metrics (e.g., click-through rate) between two models.

---

## Automation Triggers (CI/CD)

| Trigger Event | Automated Action |
|---|---|
| **Code Push (`main`)** | Run unit tests (`pytest`), lint code (`flake8`), build Docker containers, and test API endpoints. |
| **Data Version Update (`dvc push`)** | Trigger full retraining pipeline via GitHub Actions using the newly versioned dataset. |
| **Scheduled (Cron)** | Execute batch inference, evaluate performance against a golden dataset, and push metrics to a dashboard. |
| **Monitor Drift Alert** | Automatically initiate a `Data Extraction → Preprocessing → Training` pipeline when statistical drift is detected in live production inputs. |

---

## Tools for Pipeline Orchestration (DAGs)

- **Kubeflow Pipelines:** Kubernetes-native orchestration; ideal for massive scale but carries high infrastructure complexity.
- **TFX (TensorFlow Extended):** Google's production framework tailored specifically for the TensorFlow ecosystem.
- **ZenML:** Highly ergonomic, Pythonic MLOps framework that allows you to swap backends (e.g., switching from local execution to Vertex AI) by changing a single configuration line.
- **Apache Airflow / Prefect:** General-purpose data engineering DAG orchestrators frequently adapted to trigger ML training stages.
- **Flyte:** Strongly typed, highly scalable workflow orchestration engine built by Lyft, excelling in versioned ML tasks.

---

## Key Concepts Checklist

- **Data Versioning (DVC):** Understanding that `git` cannot handle 100GB datasets. Connecting object storage (S3) to Git commits using `.dvc` pointers.
- **Level 1 vs Level 2 MLOps:** Recognizing the transition from automating the *training of the model* (Level 1) to automating the *deployment of the training pipeline itself* (Level 2).
- **Data Drift vs. Concept Drift:** Identifying when the input data features change distribution (Data Drift) versus when the mathematical mapping between inputs and the target variable changes (Concept Drift).
- **Model Serving Latency:** Evaluating whether to deploy via REST API (e.g., FastAPI), gRPC for microsecond inter-service latency, or Batch processing for offline analytics.

---

## See also

- [Agent Evaluation & Production](../visualizers-and-playgrounds/README.md) — How to evaluate non-deterministic models before pushing to the staging registry.
- [Tool Use & Function Calling](../docs/06-agentic-ai/fundamentals/tool-use-and-function-calling.md) — Monitoring error rates on production APIs used by models.