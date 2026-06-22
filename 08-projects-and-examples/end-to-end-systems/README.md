# End-to-End Systems

> Complete system examples that tie together model development, API serving, frontend, and infrastructure.

## Project List

| Project | Stack | Complexity |
|---|---|---|
| **Real-Time Sentiment Dashboard** | FastAPI + React + WebSocket + BERT | Intermediate |
| **Document Question-Answering System** | RAG pipeline (ChromaDB + LLM + LangChain) + Streamlit | Intermediate |
| **Image Search Engine** | CLIP embeddings + Qdrant + FastAPI + Next.js | Advanced |
| **ML Model Marketplace** | Model registry + BentoML + React + Auth0 | Advanced |
| **Personal AI Tutor** | Multi-agent system + RAG + TTS/SpeechRecognition | Advanced |

## Resource Table

| Category | Title | Description | Level |
|---|---|---|---|
| 💻 Code/Notebook | [Full-Stack RAG App (ChromaDB + Ollama)](https://example.com/fullstack-rag) | Complete local RAG system with UI | Intermediate |
| 💻 Code/Notebook | [CLIP Image Search Deployment](https://example.com/clip-search) | End-to-end image similarity search | Advanced |
| 🎓 Course | [Full Stack Deep Learning](https://example.com/fsdl-course) | Hands-on course building production ML systems | Intermediate |
| 📰 Blog | [Architecting ML Systems — MLflow + FastAPI + React](https://example.com/architecting-ml) | System design patterns for ML apps | Intermediate |
| 🎥 Video | [Building a Production ML App in 1 Hour](https://example.com/prod-ml-app) | Live coding a full-stack ML project | Intermediate |
| 📘 Docs | [Streamlit + FastAPI Integration Guide](https://example.com/streamlit-fastapi) | Patterns for serving ML via Streamlit | Beginner |

## Architecture Template

```
Frontend (React/Streamlit)
    │
    ▼ HTTP / WebSocket
API Gateway (FastAPI / Flask)
    │
    ▼
Model Server (Triton / BentoML / KServe)
    │
    ▼
Data Layer (Postgres / Redis / Vector DB)
```

## Key Integration Points

- **API design** — sync vs. async endpoints, streaming responses, WebSocket
- **Caching** — Redis for model predictions (LRU / TTL)
- **Authentication** — API keys, JWT, OAuth for model access
- **Monitoring** — request logging, drift detection, uptime alerts
- **Deployment** — containerized, CI/CD pipeline, cloud or on-prem

---

> **Last Reviewed:** 2026-06
