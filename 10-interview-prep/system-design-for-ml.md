# ML System Design Interview Prep

> How to approach ML system design interview questions — frameworks, patterns, and practice resources.

**Last Reviewed:** 2026-06

## Resource Table

## Resources

### 📘 Docs

| Title | Level | Link | Notes |
|---|---|---|---|
| *ML System Design — GitHub Repo (chiphuyen)* | Advanced | https://github.com/chiphuyen/machine-learning-systems-design | A booklet on machine learning systems design with exercises [cite: 1.1.1]. |
| *Designing ML Systems Resources (chiphuyen)* | Advanced | https://github.com/chiphuyen/dmls-book | Summaries and resources for Designing Machine Learning Systems book (Chip Huyen, O'Reilly 2022) [cite: 1.1.2]. |
| *Full-Stack Deep Learning — System Design Syllabus* | Intermediate | https://fullstackdeeplearning.com/ | Curriculum covering production ML architecture patterns |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| *ML System Design Interview — YouTube Series* | Advanced | https://www.youtube.com/@MLOpsCommunity | Mock interviews for common ML system design prompts |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *Designing a Recommendation System — ByteByteGo* | Advanced | https://bytebytego.com/ | Real-world recsys architecture walkthrough |
| *Real-Time Machine Learning — Chip Huyen* | Advanced | https://huyenchip.com/2020/12/27/real-time-machine-learning.html | Explores challenges and solutions for online prediction and continuous learning [cite: 1.2.2]. |
| *Prepare for ML Engineer Interview* | Intermediate | https://medium.com/marvelous-mlops/prepare-for-ml-engineer-interview-cfe0e54cb951 | Guide covering coding and ML system design interviews [cite: 1.2.5]. |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| *Grokking the ML System Design Interview* | Advanced | https://www.educative.io/courses/grokking-the-machine-learning-interview | Structured prep with common question patterns |


## Design Framework (5-Step)

| Step | Description | Time |
|---|---|---|
| **1. Clarify Requirements** | Ask about scale, latency, accuracy, data volume, constraints | 5 min |
| **2. Data Pipeline** | Data sources, storage, preprocessing, feature engineering | 5 min |
| **3. Model Selection** | Candidate models, tradeoffs, baseline approach | 5 min |
| **4. Training & Evaluation** | Offline validation, experiment tracking, hyperparameter tuning | 5 min |
| **5. Serving & Monitoring** | Deployment strategy, scaling, drift detection, A/B testing | 10 min |

## Common ML System Design Questions

| Question | Domain |
|---|---|
| Design a YouTube video recommendation system | RecSys |
| Design a fraud detection system | Anomaly Detection |
| Design a search ranking system (e.g., Google Search) | Ranking / IR |
| Design an ad click-through rate (CTR) prediction system | Ad Tech |
| Design a ride-sharing ETA prediction system (e.g., Uber) | Regression |
| Design an LLM-powered customer support chatbot | GenAI / Agents |
| Design a content moderation system (e.g., toxic comment detection) | NLP / Classification |

## Scoring Rubric (What Interviewers Look For)

| Criterion | Weight |
|---|---|
| **Problem scoping** — asking the right clarifying questions | 20% |
| **Tradeoff awareness** — justifying choices between alternatives | 25% |
| **System design depth** — from data to deployment | 30% |
| **Scalability & reliability** — handling scale, failures, latency | 15% |
| **Communication** — structured, clear, collaborative | 10% |