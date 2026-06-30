# Advanced Projects

> Research-level and production-grade projects involving distributed training, large-scale data, or novel architectures.

**Last Reviewed:** 2026-06

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| *DeepSpeed Configuration Guide* | Advanced | <https://www.deepspeed.ai/docs/config-json/> | Official schema guide for tuning multi-GPU ZeRO memory optimization. |
| *Kubeflow Pipelines SDK Reference* | Advanced | <https://www.kubeflow.org/docs/components/pipelines/v2/> | Building and compiling production pipelines programmatically. |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| *Building Multi-Agent Systems with LangGraph* | Advanced | <https://www.youtube.com/watch?v=x-PXYu2vM-U> | Deep dive into handling cyclic graphs, agent planning, and routing loops. |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| *Stanford CS329 — Systems for ML* | Advanced | <https://stanford-cs329s.github.io/> | Landmark syllabus detailing distributed systems, model testing, and data engineering. |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *LoRA: Low-Rank Adaptation of LLMs* (Hu et al., 2021) | Advanced | <https://arxiv.org/abs/2106.09685> | Parameters-efficient fine-tuning via matrix decomposition actualizaciones. |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| *DeepSpeed Reference Implementations* | Advanced | <https://github.com/microsoft/DeepSpeedExamples> | Production recipes for training foundation models across nodes. |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *Building a Real-Time Recommender at Pinterest* | Advanced | <https://medium.com/pinterest-engineering/building-a-real-time-user-profile-for-home-feed-recommendations-b2dae9545468> | Deep technical layout of sub-millisecond feature stores and scaling graphs. |

---

## Project Specifications

### 1. Distributed LLM Fine-Tuning
* **Description:** Fine-tune a foundation model (e.g., Llama-3 7B) using data parallelism across multi-GPU setups.
* **Skills Practiced:** DeepSpeed ZeRO (Stage 2/3), PyTorch FSDP, LoRA hyperparameter selection ($r, \alpha$).
* **Dataset:** [Alpaca Dataset (Stanford NLP)](https://github.com/tatsu-lab/stanford_alpaca)

### 2. Production Recommendation System
* **Description:** Build an event-driven retrieval and ranking recommendation pipeline with low-latency constraints.
* **Skills Practiced:** Message ingestion using Apache Kafka, fast item profile lookup with Redis, embedding generation.
* **Dataset:** [Amazon Product Reviews Dataset](https://amazon-reviews-2023.github.io/)

### 3. Self-Supervised Vision Model
* **Description:** Train an image backbone without human labels using contrastive learning representations.
* **Skills Practiced:** Data augmentations (color jitter, Gaussian blur), InfoNCE loss tuning, ResNet evaluation.
* **Dataset:** [STL-10 Dataset (Stanford Vision Lab)](https://cs.stanford.edu/~acoates/stl10/)

### 4. Enterprise ML Pipeline on Kubernetes
* **Description:** Create an autoscale-ready pipeline that automates training through model serving.
* **Skills Practiced:** Kubeflow Pipelines SDK compilation, Knative autoscaling, Argo workflow state definitions.
* **Dataset:** Custom / Synthetic Data Generator

### 5. Multi-Agent System with RAG
* **Description:** Deploy a stateful multi-agent team capable of tool routing, episodic memory retrieval, and dynamic planning.
* **Skills Practiced:** Stateful graph routing via LangGraph, vector database metadata slicing, exception trace backtracking.
* **Dataset:** [Wikipedia Dump Data](https://dumps.wikimedia.org/)

---

## Infrastructure Considerations

* **Multi-GPU training:** Utilizing DDP for simple data parallel steps, or FSDP/DeepSpeed for splitting optimizer states, gradients, and parameters when tensors exceed single VRAM capacities.
* **Gradient checkpointing & mixed precision:** Trading extra computation cycles for reduced memory footprints via `torch.cuda.amp` (FP16/BF16).
* **Distributed data loading:** Ensuring worker threads prevent GPU starvation by scaling up multi-threaded streaming pipelines.
* **CI/CD boundaries:** Shifting from standard application unit-testing to execution-based model validation over regression golden sets before model server deployment.

---

## See also

- [LLM Fundamentals](../../05-generative-ai/llm-fundamentals.md)
- [Multi-Agent Systems](../../06-agentic-ai/fundamentals/multi-agent-systems.md)
- [Containers & Orchestration for ML](../../07-mlops-and-deployment/containers-and-orchestration.md)