# Model Serving, Inference & APIs

> How to take a trained model and expose it as a production-grade inference endpoint.

## Resource Table

| Category | Title | Description | Level |
|---|---|---|---|
| 📘 Docs | [NVIDIA Triton Inference Server Docs](https://example.com/triton-docs) | Architecture, model configuration, perf analysis | Advanced |
| 📘 Docs | [BentoML Documentation](https://example.com/bentoml-docs) | Building bentos, serving, and deploying | Intermediate |
| 💻 Code/Notebook | [Triton Client Examples](https://example.com/triton-client) | Python/C++ clients for gRPC/REST inference | Intermediate |
| 📰 Blog | [ML Serving at Scale — Netflix Tech Blog](https://example.com/netflix-serving) | Real-world inference infrastructure patterns | Advanced |
| 🎥 Video | [Serving ML Models in Production — PyCon Talk](https://example.com/pycon-serving) | Practical serving patterns and pitfalls | Intermediate |
| 🎓 Course | [Full-Stack Deep Learning — Deployment Module](https://example.com/fsdl-serving) | End-to-end model serving walkthrough | Intermediate |

## Key Tools

| Tool | Purpose |
|---|---|
| **Triton Inference Server** | High-performance inference with dynamic batching, multi-framework, GPU support |
| **TorchServe** | PyTorch-native serving with model versioning and logging |
| **BentoML** | Python-first framework for packaging and deploying models |
| **KServe** | Kubernetes-native model serving with auto-scaling |
| **Seldon Core** | ML graph inference on Kubernetes |

## Serving Patterns

- **Online (real-time) inference** — REST/gRPC endpoints for individual predictions
- **Batch inference** — scheduled or event-driven processing of large data sets
- **Streaming inference** — real-time predictions on data streams (Kafka, Flink)
- **Hybrid serving** — combine online and batch in a single pipeline

## Performance Considerations

- **Batching** — dynamic vs. static batching tradeoffs
- **Model quantization** — FP16, INT8 to reduce latency
- **GPU vs. CPU serving** — cost-performance analysis
- **Cold start** — model loading times and warm-up strategies

---

> **Last Reviewed:** 2026-06
