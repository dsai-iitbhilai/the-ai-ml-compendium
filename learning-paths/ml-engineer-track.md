# ML Engineer Learning Path

> For software engineers or DevOps practitioners who want to **build, deploy, and maintain production ML systems**.

## Path Overview

Focus on infrastructure, pipelines, serving, and reliability. Less emphasis on model architecture research.

## Core Modules

| Step | Module | Key Resources | Goal |
|---|---|---|---|
| 1 | [Module 01 — ML Fundamentals](../01-foundations/README.md) | ML lifecycle, types of ML systems | ML-specific terminology |
| 2 | [Module 07 — MLOps & Deployment](../07-mlops-and-deployment/) | Model serving, Docker, K8s, CI/CD | Deploy a model to production |
| 3 | [Module 07 — Containers & Orchestration](../07-mlops-and-deployment/containers-and-orchestration.md) | Docker, Kubernetes | Containerized ML workloads |
| 4 | [Module 07 — CI/CD for ML](../07-mlops-and-deployment/ci-cd-for-ml.md) | MLflow, DVC, pipeline automation | Automate retraining pipeline |

## Elective Modules

| Module | When to Take |
|---|---|
| [Module 03 — Deep Learning](../04-deep-learning/README.md) | If serving neural network models |
| [Module 05 — GenAI](../05-generative-ai/README.md) | If deploying LLMs and RAG systems |
| [Module 04 — NLP](../05-generative-ai/README.md) | If working on text-based models |
| [Module 02 — ML Algorithms](../03-machine-learning/README.md) | If building traditional ML models |

## Projects

| Project | Module Connection | Skills |
|---|---|---|
| [ML Pipeline on Kubernetes](../08-projects-and-examples/advanced/#ml-pipeline-on-kubernetes) | 07-MLOps | KF Pipelines, KServe |
| [Image Search Engine](../08-projects-and-examples/end-to-end-systems/#image-search-engine) | 03-DL, 07-MLOps | CLIP, vector DB, API |
| [Document QA System](../08-projects-and-examples/end-to-end-systems/#document-question-answering-system) | 05-GenAI, 07-MLOps | RAG, LangChain, deployment |

## Additional Focus Areas

- **Infrastructure as Code** — Terraform, Pulumi for ML infra
- **Feature Stores** — Feast, Tecton for feature management
- **Model Monitoring** — Evidently, WhyLabs for drift detection
- **Cost Optimization** — GPU utilization, spot instances, caching

---

> **Last Reviewed:** 2026-06
