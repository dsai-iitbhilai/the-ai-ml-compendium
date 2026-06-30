# Monitoring & Observability for ML

> Tracking model performance in production: detecting statistical drift, logging high-dimensional predictions, estimating performance without ground truth, and alerting on degradation. This file bridges standard software telemetry with machine learning-specific evaluation.

**Last Reviewed:** 2026-06

**Prerequisites:** [Model Serving, Inference & APIs](../docs/07-mlops-and-deployment/model-serving.md) · Probability & Statistics

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| *Evidently AI Documentation* | Intermediate | <https://docs.evidentlyai.com/> | Open-source framework for evaluating, testing, and monitoring ML models in production. |
| *NannyML Documentation* | Advanced | <https://nannyml.readthedocs.io/> | Deep-dive into Confidence-Based Performance Estimation (CBPE) when ground truth is delayed. |
| *Arize Phoenix Docs* | Intermediate | <https://docs.arize.com/phoenix> | Specialized observability for LLMs, including tracing LangChain/LlamaIndex operations. |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| *Monitoring ML Models in Production* (GCP) | Intermediate | <https://www.youtube.com/watch?v=1F2b_11y3eU> | Architecture walkthrough for setting up continuous monitoring and alerting pipelines. |
| *Detecting Data Drift with KS and PSI* | Advanced | <https://www.youtube.com/watch?v=5rG4nOqWkSg> | Mathematical breakdown of the two most common drift detection algorithms. |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| *Arize Phoenix UI* | Beginner | <https://github.com/Arize-ai/phoenix> | Open-source UI for visualizing UMAP/t-SNE embedding drifts and agentic traces locally. |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *Failing Loudly: An Empirical Study of Methods for Detecting Dataset Shift* (Rabanser et al., 2019) | Advanced | <https://arxiv.org/abs/1810.11953> | Evaluates various statistical methods (PCA, KS, MMD) for detecting distribution shifts. |
| *A Survey on Concept Drift Adaptation* (Gama et al., 2014) | Advanced | <https://dl.acm.org/doi/10.1145/2523813> | The foundational paper on how models adapt when the relationship between $X$ and $Y$ changes. |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| *whylogs* | Intermediate | <https://github.com/whylabs/whylogs> | Open-source standard for data logging; uses Apache DataSketches to profile terabytes of data efficiently. |
| *Alibi Detect* | Advanced | <https://github.com/SeldonIO/alibi-detect> | Sophisticated library focused strictly on outlier, adversarial, and drift detection. |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *A Practical Guide to ML Model Monitoring* (NannyML) | Intermediate | <https://www.nannyml.com/blog/machine-learning-monitoring-guide> | Comprehensive breakdown of covariate shift vs. concept drift and when to alert. |
| *Monitoring Large Language Models (LLMs)* (Arize) | Advanced | <https://arize.com/blog-course/llm-monitoring-and-observability/> | Strategies for monitoring non-deterministic output quality and embedding drift. |

---

## Types of Drift (Mathematical Definitions)

| Drift Type | Mathematical Definition | Detection Method |
|---|---|---|
| **Data Drift (Covariate Shift)** | $P_{train}(X) 
eq P_{test}(X)$ while $P(Y\|X)$ remains constant. | Kolmogorov-Smirnov (KS) test, Population Stability Index (PSI), Kullback-Leibler (KL) Divergence. |
| **Concept Drift** | $P_{train}(Y\|X) 
eq P_{test}(Y\|X)$ while $P(X)$ may or may not change. | Error rate monitoring, Confidence-Based Performance Estimation (CBPE). |
| **Prior Probability Shift** | $P_{train}(Y) 
eq P_{test}(Y)$ while $P(X\|Y)$ remains constant. | Monitoring output percentiles, class imbalance shifts. |
| **Label Drift** | Change in the underlying ground truth distribution. | Delayed label analysis against predicted classes. |

---

## Observability Stack Components

- **Logging (Telemetry):** Capturing structured prediction logs (Input Features, Output Predictions, Latency, API Metadata). For LLMs, this includes the full prompt context and `temperature` settings.
- **Metrics (Prometheus):** Time-series aggregation of latency (p95, p99), throughput (RPS), error rates (HTTP 500s), and calculated drift scores.
- **Tracing (OpenTelemetry):** End-to-end request tracing spanning the API Gateway, the retrieval step (Vector DB), and the LLM generation step (crucial for RAG/Agentic pipelines).
- **Alerting (Grafana / PagerDuty):** Threshold-based triggers (e.g., "Alert if KS-statistic > 0.1 for 3 consecutive hours").
- **Dashboards:** Visualizing model health across staging (shadow mode) and production environments.

---

## Tools Comparison

| Tool | Focus | Strengths |
|---|---|---|
| **Evidently AI** | Drift detection & reporting | Rich Pandas-native reports, simple open-source integrations, visualizes feature-level drift. |
| **Whylogs (WhyLabs)** | Data profiling | Highly scalable; logs profiles instead of raw data to ensure privacy and low storage overhead. |
| **NannyML** | Performance estimation | Specializes in CBPE — estimating how a model is performing *before* ground truth labels arrive. |
| **Great Expectations** | Data quality validation | Declarative pipeline testing; prevents bad data from ever hitting the inference endpoint. |
| **Alibi Detect** | Algorithmic detection | Broad statistical test library (MMD, Fisher exact test) and adversarial attack detection. |
| **Arize Phoenix** | LLM Tracing | Purpose-built for embedding vector drift, RAG tracing, and chunk retrieval analysis. |

---

## Key Concepts Checklist

- **The Delayed Ground Truth Problem:** Recognizing that in the real world (e.g., credit card fraud), you may not know if a model's prediction was correct until weeks later, necessitating proxy metrics and CBPE.
- **System vs. ML Metrics:** Differentiating between infrastructure health (latency, CPU, memory) and statistical health (feature drift, model confidence, perplexity).
- **Statistical Windowing:** Defining the correct moving average window. Calculating drift over 10 minutes is too noisy; calculating over 1 month masks critical sudden shifts.
- **Dimensionality Reduction for Monitoring:** Using algorithms like UMAP or PCA to project high-dimensional embeddings (from LLMs or CV models) into 2D/3D space to visually and mathematically calculate cluster drift.

---

## See also

- [Model Serving, Inference & APIs](../docs/07-mlops-and-deployment/model-serving.md) — Where the telemetry instrumentation is physically injected.
- [CI/CD for Machine Learning](../docs/07-mlops-and-deployment/ci-cd-for-ml.md) — How a triggered drift alert automatically kicks off the continuous training (CT) pipeline.
- [Agent Evaluation & Production](README.md) — Correlating live observability traces back to offline benchmark performance.