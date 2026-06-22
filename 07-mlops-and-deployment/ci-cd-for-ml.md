# CI/CD for Machine Learning

> Automating ML pipelines: experiment tracking, model versioning, and continuous training/deployment.

## Resource Table

| Category | Title | Description | Level |
|---|---|---|---|
| 📘 Docs | [MLflow Documentation](https://example.com/mlflow-docs) | Experiment tracking, model registry, serving | Intermediate |
| 📘 Docs | [DVC (Data Version Control) Docs](https://example.com/dvc-docs) | Versioning datasets and ML pipelines | Intermediate |
| 💻 Code/Notebook | [GitHub Actions ML Pipeline Example](https://example.com/gh-actions-ml) | CI/CD template for training + deployment | Intermediate |
| 🎓 Course | [MLOps Specialization — DeepLearning.AI](https://example.com/dla-mlops) | Full MLOps lifecycle with CI/CD emphasis | Intermediate |
| 📰 Blog | [ML CI/CD Best Practices — neptune.ai](https://example.com/neptune-cicd) | Branch strategies, pipeline stages, artifact management | Intermediate |
| 🎥 Video | [Building ML Pipelines with TFX — Google I/O](https://example.com/tfx-video) | Production pipeline orchestration with TFX | Advanced |

## ML Pipeline Stages (CI/CD View)

```
Code Commit → Lint/Test → Train → Evaluate → Register → Deploy → Monitor
    ↑                                                              │
    └──────────────────── Continuous Training ─────────────────────┘
```

## Experiment Tracking

| Tool | Key Features |
|---|---|
| **MLflow Tracking** | Log params, metrics, artifacts; UI for comparison |
| **Weights & Biases** | Rich dashboards, sweeps, reports |
| **Neptune.ai** | Metadata store with flexible UI |
| **Comet.ml** | Experiment comparison and collaboration |

## Model Registry Patterns

- **Staging** → QA/validation environment
- **Production** → live inference (with rollback)
- **Champion/Challenger** — compare multiple models in shadow mode
- **Canary** — progressively shift traffic to new model

## Automation Examples

| Trigger | Action |
|---|---|
| Push to `main` (code change) | Run unit tests, lint, build container |
| New data version in DVC | Trigger retraining pipeline |
| Scheduled (daily/weekly) | Batch training + evaluation + registry push |
| Drift alert | Trigger automatic retraining with latest data |

## Tools for Pipeline Orchestration

- **TFX** — Google's production ML pipeline framework
- **Kubeflow Pipelines** — K8s-native pipeline orchestration
- **ZenML** — MLOps framework with pluggable backends
- **Airflow / Prefect** — general DAG orchestration, often used for ML
- **Flyte** — typed, versioned workflow orchestration for ML

---

> **Last Reviewed:** 2026-06
