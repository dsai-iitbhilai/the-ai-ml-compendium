# Containers & Orchestration for ML

> Packaging Machine Learning workloads into reproducible environments using Docker and orchestrating their deployment, scaling, and networking at scale using Kubernetes.

**Last Reviewed:** 2026-06

**Prerequisites:** [CI/CD for Machine Learning](../docs/07-mlops-and-deployment/ci-cd-for-ml.md) · Linux Fundamentals

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| *Docker Official Docs — Get Started* | Beginner | <https://docs.docker.com/get-started/> | Foundational guide to building, tagging, and pushing container images. |
| *Kubernetes Official Tutorials* | Intermediate | <https://kubernetes.io/docs/tutorials/> | Step-by-step introduction to pods, deployments, and services. |
| *KServe Documentation* | Advanced | <https://kserve.github.io/website/latest/> | Standard serverless machine learning inferencing on Kubernetes. |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| *Machine Learning on Kubernetes (KubeCon)* | Advanced | <https://www.youtube.com/watch?v=FjS63i00d4k> | Real-world talks from the CNCF on running ML workloads and GPU sharing on K8s. |
| *Docker for Data Science & ML* | Beginner | <https://www.youtube.com/watch?v=pTFZEBq_zCQ> | Quick crash course on packaging Python environments and models into images. |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| *Deploying Machine Learning Models in Production* (Coursera) | Intermediate | <https://www.coursera.org/learn/deploying-machine-learning-models> | Focuses on containerization and cloud-native deployment architectures. |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| *NVIDIA NGC Deep Learning Containers* | Intermediate | <https://catalog.ngc.nvidia.com/containers> | The industry standard, highly optimized base Dockerfiles for PyTorch, TensorFlow, and JAX with pre-compiled CUDA layers. |
| *Kubeflow Manifests* | Advanced | <https://github.com/kubeflow/manifests> | Declarative Kubernetes manifests (Kustomize/Helm) to deploy the entire Kubeflow stack. |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *Running GPUs on Kubernetes Engine* (Google Cloud) | Advanced | <https://cloud.google.com/kubernetes-engine/docs/how-to/gpus> | Configuring node pools, GPU scheduling, and Multi-Instance GPUs (MIG) for ML workloads. |
| *Dockerizing Python Applications for ML* | Intermediate | <https://testdriven.io/blog/docker-best-practices/> | Extensive guide on layer caching and minimizing final image sizes. |

---

## Containerization Best Practices for ML

- **Slim Base Images:** Use stripped-down bases (e.g., `python:3.11-slim` or `ubuntu:22.04`) and install only the strictly required system dependencies to reduce the attack surface and download times.
- **Layer Caching:** Order your `Dockerfile` from the least frequently changed layers to the most. Install system packages (`apt-get`) first, then Python dependencies (`pip install -r requirements.txt`), and finally copy your source code.
- **Externalize Model Weights:** Never bake massive `.safetensors` or `.bin` files directly into the Docker image. Mount them at runtime via Persistent Volumes (PVs) or download them from S3/GCS dynamically to keep image pulls fast.
- **Multi-stage Builds:** Use an initial "builder" stage to compile C++ extensions or heavy libraries, then copy only the compiled binaries to the final, lightweight production image.

---

## Kubernetes Concepts for ML

| Concept | ML Relevance |
|---|---|
| **Pods & Deployments** | Running multiple identical replicas of a model server (e.g., vLLM or FastAPI) to handle concurrent traffic. |
| **Services & Ingress** | Exposing the inference endpoints to the internet or internal microservices, often handling TLS termination. |
| **Horizontal Pod Autoscaler (HPA)** | Scaling the number of model replicas dynamically based on Custom Metrics (e.g., Inference QPS, GPU Memory Utilization). |
| **Jobs & CronJobs** | Triggering isolated batch inference workloads, data ingestion pipelines, or overnight model retraining. |
| **Custom Resource Definitions (CRDs)** | Extending Kubernetes specifically for ML: `InferenceService` (KServe), `TFJob`, or `PyTorchJob` for distributed training. |
| **Node Pools & Taints** | Isolating expensive GPU nodes from cheap CPU nodes using taints and tolerations so standard web microservices don't consume GPU resources. |

---

## Key Concepts Checklist

- **Docker Layer Mathematics:** Understanding that each `RUN`, `COPY`, and `ADD` command creates a new hashed filesystem delta. Combining commands (`RUN apt-get update && apt-get install`) prevents bloat.
- **CUDA and Container Runtime:** Knowing how `nvidia-container-toolkit` bridges the host machine's GPU drivers to the isolated Docker container.
- **K8s Scheduling:** Defining `requests` and `limits` in Pod specs. A Pod requesting `nvidia.com/gpu: 1` will mathematically block that GPU from being used by other pods unless MIG (Multi-Instance GPU) or Time-Slicing is enabled.
- **Liveness and Readiness Probes:** Configuring endpoints to ensure Kubernetes does not route traffic to a massive LLM container until it has fully finished loading weights into VRAM.

---

## Useful Helm Charts

- [`kserve/kserve`](https://github.com/kserve/kserve/tree/master/charts/kserve-resources) — Deploy KServe with all dependencies (Knative, Istio) for serverless ML inferencing.
- [`seldonio/seldon-core`](https://github.com/SeldonIO/seldon-core/tree/master/helm-charts) — Seldon Core operator for advanced ML serving graphs (A/B testing, Shadow mode, Ensembles).
- [`kubeflow/manifests`](https://github.com/kubeflow/manifests) — Deploying the full Kubeflow stack (Pipelines, Jupyter Notebooks, Katib).

---

## See also

- [CI/CD for Machine Learning](../docs/07-mlops-and-deployment/ci-cd-for-ml.md) — How Docker images are built and pushed to registries (ECR/GCR) during automated pipelines.
- [Agent Evaluation & Production](README.md) — How the orchestration layer provisions sandboxed Docker environments for code-execution agents.