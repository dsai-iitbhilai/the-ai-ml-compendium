# RAG Systems

> Retrieval-Augmented Generation (RAG) combines an information retrieval step (searching a dense vector space) with an autoregressive generation step (an LLM producing an answer grounded in the retrieved context). This file covers vector database architectures, embedding topologies, advanced retrieval heuristics (hybrid search, HyDE), and systematic mathematical RAG evaluation.

**Last Reviewed:** 2026-06

**Prerequisites:** [LLM Fundamentals](llm-fundamentals.md) · [Prompt Engineering](prompt-engineering.md) · Linear Algebra

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| *LangChain RAG Tutorial* | Intermediate | <https://python.langchain.com/docs/tutorials/rag/> | End-to-end RAG pipeline with document loading, splitting, embedding, retrieval, and generation. |
| *LlamaIndex Documentation* | Intermediate | <https://docs.llamaindex.ai/> | In-depth guides on advanced data connectors, index routing, and agentic query engines. |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| *RAG from Scratch* (LangChain) | Intermediate | <https://www.youtube.com/playlist?list=PLfaIDFEXuae2LXbO1_PKyE1lLm3Dgbd2e> | Step-by-step video series building a RAG pipeline from basic chunking to advanced retrieval. |
| *Building RAG from Scratch* (Andrej Karpathy) | Advanced | <https://www.youtube.com/watch?v=kCc8FmEb1nY> | (Within the Let's Build GPT context) - Understanding how context windows interact with retrieved tokens. |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| *DeepLearning.AI — Advanced Retrieval for AI* | Advanced | <https://www.deeplearning.ai/short-courses/advanced-retrieval-for-ai-with-chroma/> | Covers query expansion, cross-encoder reranking, and embedding spaces by Andrew Ng. |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| *Arize Phoenix* | Advanced | <https://phoenix.arize.com/> | Open-source tool for visualizing RAG traces, embedding spaces (UMAP/t-SNE), and LLM evaluations. |
| *Pinecone Console* | Beginner | <https://app.pinecone.io/> | Interactive dashboard to experiment with vector indices, cosine similarity thresholds, and metadata filtering. |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks* (Lewis et al., 2020) | Intermediate | <https://arxiv.org/abs/2005.11401> | Original RAG paper proposing DPR + BART fusion-in-decoder for open-domain QA. |
| *Dense Passage Retrieval for Open-Domain Question Answering* (Karpukhin et al., 2020) | Intermediate | <https://arxiv.org/abs/2004.04906> | The mathematical foundation for training dual-encoder architectures (DPR). |
| *REALM: Retrieval-Augmented Language Model Pre-Training* (Guu et al., 2020) | Advanced | <https://arxiv.org/abs/2002.08909> | Introduces masked language modeling with a learned retriever during pretraining. |
| *CRAG — Comprehensive RAG Benchmark* (Yan et al., 2024) | Advanced | <https://arxiv.org/abs/2406.04744> | Evaluates the robustness of RAG systems against hallucination and temporal drift. |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| *LlamaIndex RAG Starter* | Intermediate | <https://github.com/run-llama/llama_index/tree/main/docs/docs/examples> | Practical notebooks covering basic RAG, advanced retrieval, and multi-document agents. |
| *RAGAS (RAG Assessment)* | Advanced | <https://github.com/explodinggradients/ragas> | Framework to mathematically evaluate RAG pipelines (Faithfulness, Context Precision/Recall). |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *Building RAG at Scale* (Databricks) | Advanced | <https://www.databricks.com/blog/rag-scale> | Production considerations: data ingestion pipelines, MLOps, chunking strategies, and latency. |
| *Hybrid Search Explained* (Weaviate) | Intermediate | <https://weaviate.io/blog/hybrid-search-explained> | The math behind combining sparse keyword search (BM25) with dense vector representations. |

---

## RAG Architecture & Mathematics

```text
User Query (q)
    │
    ▼
 ┌─────────────┐     ┌────────────────────────────────┐
 │  Embedding  │────│  Vector Database               │
 │  Model E(q) │     │  argmax_{d_i} cosine(E(q), E(d))│
 └─────────────┘     └────────┬───────────────────────┘
                              │ top-k chunks {d_1...d_k}
                              ▼
 ┌─────────────┐     ┌────────────────────────────────┐
 │  LLM        │────│  Prompt Builder                │
 │  P(y|q, D)  │     │  Context: D = [d_1, ..., d_k]  │
 └──────┬──────┘     └────────────────────────────────┘
        │
        ▼
  Grounded Answer (y)
```

---

## Vector Databases

| Database | Type | Notes |
|----------|------|-------|
| **Qdrant** | Open-source, cloud | Written in Rust; excellent for high-throughput production with payload-based filtering. |
| **Pinecone** | Managed cloud | Serverless, high availability, built-in proprietary hybrid search. |
| **Weaviate** | Open-source, cloud | Rich schema, native hybrid search (BM25 + Vector), GraphQL API. |
| **Milvus** | Open-source | Highly scalable, built for massive enterprise datasets distributed across nodes. |
| **pgvector** | PostgreSQL extension | Ideal if already relying on Postgres; provides ACID compliance alongside vector ops. |

---

## Chunking Strategies

| Strategy | Description | Best For |
|----------|-------------|----------|
| **Fixed-size** | Split by absolute token/character count with a specified overlap threshold. | Simple text streams, predictable chunk boundaries. |
| **Recursive character** | Hierarchically split on natural delimiters (`

`, `
`, `.`, ` `). | General purpose; balances structural integrity and simplicity. |
| **Semantic Chunking** | Split text at topic boundaries by measuring cosine distance drops between consecutive sentence embeddings. | High-quality retrieval, reducing noise in context windows. |
| **Document-based** | Utilize DOM/AST parsing (paragraphs, HTML tags, markdown headings) via tools like `Unstructured.io`. | Highly structured documents (PDFs, wikis, Notion pages). |
| **Agentic Chunking** | An LLM dynamically decides chunk boundaries and synthesizes metadata during ingestion. | Maximum quality for complex reasoning, but computationally expensive. |

---

## Key Concepts Checklist

- **Vector Math:** Understanding Cosine Similarity ($1 - rac{A \cdot B}{||A|| ||B||}$), Dot Product, and L2 (Euclidean) Distance.
- **Dual-Encoders vs. Cross-Encoders:** Using fast bi-encoders (e.g., `text-embedding-3-small`) for initial retrieval, and highly accurate cross-encoders (e.g., `bge-reranker`) for post-retrieval reranking.
- **Hybrid Search:** Fusing dense vector search with sparse lexical search (BM25) using reciprocal rank fusion (RRF).
- **Query Transformations:** Rewriting queries, decomposing complex questions, or using HyDE (Hypothetical Document Embeddings) to bridge the semantic gap.
- **Evaluation Metrics (RAGAS):**
  - **Faithfulness:** Does the generated answer strictly hallucinate nothing outside the retrieved context?
  - **Answer Relevancy:** How well does the answer address the original query?
  - **Context Precision / Recall:** Did we retrieve the right chunks, and did we retrieve *all* the necessary chunks?

---

## Projects / Practice

| Project | Description |
|---|---|
| **End-to-End Enterprise RAG Microservice** | Avoid simple local notebooks. Implement an asynchronous ingestion pipeline using `Unstructured.io` for semantic chunking and push to a remote `Qdrant` cluster. Serve the retrieval and generation pipeline using `FastAPI` and an open-source model running on `vLLM` to handle high concurrency. |
| **Advanced Multi-hop Agentic RAG** | Build an agentic query engine using `LangGraph` where the LLM dynamically evaluates if it needs to route the query to a vector database, execute a SQL query on a structured database, or perform a web search. Incorporate backtracking if the retrieved context is flagged as insufficient by an internal evaluator. |
| **RAG Evaluation and Tracing CI/CD** | Deploy a production RAG pipeline instrumented with `Arize Phoenix` for full telemetry. Set up an automated evaluation script that computes NDCG for the retrieval step and uses an LLM-as-a-judge to score Faithfulness. Integrate this into a CI/CD pipeline that blocks deployment if evaluation scores drop below a defined threshold. |

---

## References

- [Dense Passage Retrieval (Karpukhin et al., 2020)](https://arxiv.org/abs/2004.04906)
- [REPLUG: Retrieval-Augmented Black-Box LMs (Shi et al., 2023)](https://arxiv.org/abs/2301.12652)
- [CRAG — Comprehensive RAG Benchmark (Yan et al., 2024)](https://arxiv.org/abs/2406.04744)

---

## See also

- [Agentic AI](../06-agentic-ai/README.md) — Extending RAG by granting the LLM agency to query, filter, and summarize external databases dynamically.
- [Prompt Engineering](prompt-engineering.md) — Structuring the prompt context to maximize the LLM's adherence to retrieved chunks.
- [MLOps](../07-mlops-and-deployment/README.md) — Handling the vector database infrastructure, embedding model versioning, and pipeline tracing.