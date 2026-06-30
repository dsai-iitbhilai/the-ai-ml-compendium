# Advanced Projects

> Research-level and production-grade projects involving distributed training, large-scale data, or novel architectures.

## Project List

| Project | Description | Skills Practiced | Dataset |
|---|---|---|---|
| **Distributed LLM Fine-Tuning** | Fine-tune a 7B+ parameter model across multiple GPUs | FSDP/DeepSpeed, LoRA, parallelism | Alpaca / OpenAssistant |
| **Production Recommendation System** | Real-time recommender with feature store + AB testing | Kafka, Redis, feature engineering at scale | Amazon Reviews |
| **Self-Supervised Vision Model** | Contrastive learning (SimCLR/MoCo) on ImageNet subset | SSL, augmentations, ResNet backbone | ImageNet-100 / STL-10 |
| **ML Pipeline on Kubernetes** | Full Kubeflow pipeline with auto-scaling | KF Pipelines, KServe, Argo workflows | Custom (synthetic) |
| **Multi-Agent System with RAG** | LLM agents with tool use, memory, and retrieval | LangGraph/AutoGen, vector DBs, planning | Wikipedia / custom KB |

## Resource Table

| Category | Title | Description | Level |
|---|---|---|---|
|  Paper | [LoRA: Low-Rank Adaptation of LLMs](https://example.com/lora-paper) | Parameter-efficient fine-tuning | Advanced |
|  Code/Notebook | [LLM Fine-Tuning with DeepSpeed](https://example.com/deepspeed-llm) | Distributed training configuration and scripts | Advanced |
|  Docs | [Kubeflow Pipeline SDK Guide](https://example.com/kubeflow-sdk) | Building and compiling pipelines programmatically | Advanced |
|  Video | [Multi-Agent Systems with LangGraph — DeepLearning.AI](https://example.com/langgraph-agent) | Building agentic workflows | Advanced |
|  Blog | [Building a Real-Time Recommender at Pinterest](https://example.com/pinterest-recsys) | Industrial recommendation architecture | Advanced |
|  Course | [Stanford CS329 — Systems for ML](https://example.com/cs329) | Distributed systems for machine learning | Advanced |

## Infrastructure Considerations

- Multi-GPU training (DDP, FSDP, DeepSpeed)
- Gradient checkpointing and mixed precision
- Distributed data loading and caching
- Model parallelism vs. data parallelism
- CI/CD with automated evaluation benchmarks

---

> **Last Reviewed:** 2026-06
