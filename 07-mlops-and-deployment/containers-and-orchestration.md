# Containers & Orchestration for ML

> Packaging ML workloads with Docker and orchestrating them with Kubernetes.

## Resource Table

| Category | Title | Description | Level |
|---|---|---|---|
| 📘 Docs | [Docker Official Docs — Get Started](https://example.com/docker-start) | Container basics and best practices | Beginner |
| 📘 Docs | [Kubernetes Official Tutorials](https://example.com/k8s-tutorials) | Learning Kubernetes from scratch | Intermediate |
| 🎓 Course | [Docker for Data Scientists — Coursera](https://example.com/docker-ds) | Docker tailored for ML workflows | Beginner |
| 🎥 Video | [Kubernetes for ML Engineers — KubeCon Talk](https://example.com/kubecon-ml) | ML-specific K8s patterns and CRDs | Advanced |
| 💻 Code/Notebook | [ML Dockerfiles Cookbook](https://example.com/ml-dockerfiles) | Optimized Dockerfiles for PyTorch, TF, JAX | Intermediate |
| 📰 Blog | [Running GPUs on Kubernetes — Google Cloud Blog](https://example.com/gpu-k8s) | GPU scheduling, MIG, node pools | Advanced |

## Containerization Best Practices for ML

- Use slim base images (e.g., `python:3.11-slim`) and install only required system deps
- Layer caching — install system packages first, then Python deps, then model artifacts
- Keep model weights out of the image (use volume mounts or object storage)
- Multi-stage builds for reducing final image size

## Kubernetes Concepts for ML

| Concept | ML Relevance |
|---|---|
| **Pods & Deployments** | Running model server replicas |
| **Services & Ingress** | Exposing inference endpoints |
| **Horizontal Pod Autoscaler** | Scaling based on inference QPS/CPU/GPU |
| **Jobs & CronJobs** | Batch inference and retraining |
| **Custom Resource Definitions (CRDs)** | KServe `InferenceService`, TFJob, PyTorchJob |
| **Node Pools** | GPU vs. CPU node separation |

## Useful Helm Charts

- [`kserve/kserve`](https://example.com/kserve-helm) — Deploy KServe with dependencies
- [`seldonio/seldon-core`](https://example.com/seldon-helm) — Seldon Core operator
- [`kubeflow/kubeflow`](https://example.com/kubeflow-helm) — Full Kubeflow stack

---

> **Last Reviewed:** 2026-06
