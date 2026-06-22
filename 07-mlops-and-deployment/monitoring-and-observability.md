# Monitoring & Observability for ML

> Tracking model performance in production: detecting drift, logging predictions, and alerting on degradation.

## Resource Table

| Category | Title | Description | Level |
|---|---|---|---|
| 📘 Docs | [Evidently AI Documentation](https://example.com/evidently-docs) | Open-source drift detection and reporting | Intermediate |
| 📄 Paper | [Hidden Technical Debt in ML Systems — Google](https://example.com/ml-debt) | Foundational paper on ML system complexity | Intermediate |
| 💻 Code/Notebook | [Whylogs + WhyLabs Notebook Examples](https://example.com/whylabs-demo) | Logging profiles and monitoring dashboards | Intermediate |
| 🕹️ Visualizer/Playground | [Evidently Dashboard Demo](https://example.com/evidently-demo) | Interactive drift and model health dashboard | Beginner |
| 🎥 Video | [Monitoring ML Models in Production — MLOPs Meetup](https://example.com/ml-monitoring-video) | Real-world monitoring stack walkthrough | Advanced |
| 📰 Blog | [A Practical Guide to ML Model Monitoring — NannyML](https://example.com/nannyml-guide) | Data drift, concept drift, and alerting strategies | Intermediate |

## Types of Drift

| Drift Type | Description | Detection Method |
|---|---|---|
| **Data Drift** | Input distribution changes over time | Statistical tests (KS, chi-squared, JS divergence) |
| **Concept Drift** | Relationship between features and target changes | Performance monitoring, error analysis |
| **Prediction Drift** | Model output distribution shifts | Monitoring output percentiles, class balance |
| **Label Drift** | Ground truth distribution changes | Delayed label analysis |

## Observability Stack Components

- **Logging** — structured prediction logs (input, output, metadata)
- **Metrics** — latency, throughput, error rates, drift scores (Prometheus)
- **Tracing** — end-to-end request tracing (OpenTelemetry)
- **Alerting** — threshold-based and anomaly-based alerts (Grafana, PagerDuty)
- **Dashboards** — model health dashboards per deployment stage

## Tools Comparison

| Tool | Focus | Strengths |
|---|---|---|
| **Evidently AI** | Drift detection & reporting | Rich reports, open-source, easy integration |
| **Whylogs / WhyLabs** | Data logging & monitoring | Lightweight, scalable, LangKit for LLM |
| **NannyML** | Performance estimation without targets | Concept drift detection with CBPE |
| **Great Expectations** | Data quality validation | Declarative expectations, batch validation |
| **Alibi Detect** | Algorithmic drift detection | Broad statistical test library |

---

> **Last Reviewed:** 2026-06
