# Model Serving, Inference & APIs

> How to take a trained model and expose it as a highly scalable, production-grade inference endpoint. This file covers inference engines, dynamic batching, REST/gRPC protocols, and modern LLM-specific optimizations like PagedAttention.

**Last Reviewed:** 2026-06

**Prerequisites:** [Containers & Orchestration for ML](../docs/07-mlops-and-deployment/containers-and-orchestration.md) · [LLM Fundamentals](../docs/05-generative-ai/llm-fundamentals.md)

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| *NVIDIA Triton Inference Server* | Advanced | <https://github.com/triton-inference-server/server> | Official repository for the industry-standard multi-framework serving engine. |
| *BentoML Documentation* | Intermediate | <https://docs.bentoml.com/> | Python-first framework for packaging and deploying models as microservices. |
| *vLLM Documentation* | Advanced | <https://docs.vllm.ai/> | Essential documentation for high-throughput and memory-efficient LLM serving. |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| *Serving ML Models in Production* (PyCon) | Intermediate | <https://www.youtube.com/watch?v=F5jwEBaJptM> | Practical serving patterns, REST vs. gRPC, and common latency pitfalls. |
| *High-Throughput Generative Inference with vLLM* | Advanced | <https://www.youtube.com/watch?v=80bIUJ8XyCg> | Deep dive into PagedAttention and continuous batching mechanics for LLMs. |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| *Full Stack Deep Learning — Deployment* | Intermediate | <https://fullstackdeeplearning.com/> | Comprehensive module covering serverless vs. dedicated hosting and endpoint testing. |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| *Triton Model Analyzer* | Advanced | <https://github.com/triton-inference-server/model_analyzer> | CLI tool to visualize GPU memory usage and throughput to find the optimal dynamic batching configuration. |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *Efficient Memory Management for Large Language Model Serving with PagedAttention* (Kwon et al., 2023) | Advanced | <https://arxiv.org/abs/2309.06180> | The foundational paper behind `vLLM` that solved the KV-cache fragmentation problem. |
| *Orca: A Distributed Serving System for Transformer-Based Generative Models* (Yu et al., 2022) | Advanced | <https://arxiv.org/abs/2203.08913> | Introduces iteration-level (continuous) batching for generative LLMs. |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| *Triton Client Examples* | Intermediate | <https://github.com/triton-inference-server/client> | Python and C++ client scripts for hitting gRPC and REST inference endpoints. |
| *BentoML Quickstarts* | Beginner | <https://github.com/bentoml/BentoML/tree/main/examples> | Boilerplate examples for packaging PyTorch, scikit-learn, and LLMs into "Bentos". |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *ML Serving at Scale* (Netflix Tech Blog) | Advanced | <https://netflixtechblog.com/ml-model-serving-at-scale-a94f31cfa750> | Real-world architectural breakdown of Netflix's unified inference infrastructure. |
| *High-performance LLM inference in production* (Baseten) | Intermediate | <https://www.baseten.co/blog/> | Excellent engineering blogs on optimizing TTFT (Time To First Token) and token generation rates. |

---

## Key Tools Comparison

| Tool | Purpose | Key Strength |
|---|---|---|
| **Triton Inference Server** | Multi-framework (TF, PyTorch, ONNX) standard serving. | Concurrent model execution, GPU utilization optimization, dynamic batching. |
| **vLLM** | LLM-specific serving engine. | PagedAttention, continuous batching, massive throughput improvements. |
| **Text Generation Inference (TGI)** | HuggingFace's LLM server. | Native integration with the HF Hub, Rust-based router, tensor parallelism. |
| **BentoML** | Pythonic model packaging framework. | Extremely fast transition from Jupyter notebook to containerized microservice. |
| **TorchServe** | PyTorch-native serving. | First-class PyTorch ecosystem support, robust versioning and model state logging. |
| **KServe** | Kubernetes-native model serving. | Serverless auto-scaling (scale-to-zero) via Knative integrations. |

---

## Serving Architecture Patterns

- **Online (Real-Time) Inference:** Low-latency REST (JSON) or gRPC (Protobuf) endpoints for individual synchronous predictions.
- **Batch Inference:** Scheduled or event-driven asynchronous processing of large datasets (e.g., scoring millions of rows in a data warehouse nightly).
- **Streaming Inference:** Real-time predictions continuously reading from and writing to event streams (e.g., Apache Kafka, Flink) for fraud detection.
- **Serverless (Scale-to-Zero):** Utilizing cloud functions or Knative to spin up models only upon request, heavily minimizing costs for sporadic workloads.

---

## Key Concepts Checklist

- **Dynamic Batching:** Configuring the server to wait a few milliseconds (the batching window) to group concurrent requests into a single matrix multiplication operation on the GPU, maximizing throughput.
- **Continuous Batching (LLMs):** Unlike traditional batching, this technique dynamically adds new requests to the batch matrix at the *iteration* level (token by token) rather than waiting for an entire generation sequence to finish.
- **gRPC vs. REST:** Recognizing that for high-throughput image or tensor payloads, gRPC (using serialized Protocol Buffers over HTTP/2) drastically outperforms standard JSON REST API overhead.
- **Model Quantization:** Serving models converted to FP16, INT8, or AWQ formats (e.g., via TensorRT) to reduce VRAM footprints and improve memory bandwidth latency.
- **Cold Starts:** Understanding the latency penalty of loading gigabytes of model weights from disk to VRAM when a serverless endpoint scales from 0 to 1 replica.

---

## See also

- [Containers & Orchestration for ML](../docs/07-mlops-and-deployment/containers-and-orchestration.md) — How these serving engines are ultimately deployed to Kubernetes clusters.
- [LLM Fundamentals](../docs/05-generative-ai/llm-fundamentals.md) — The transformer mathematics underlying KV-Caching and PagedAttention.