# RAG Systems

Retrieval-Augmented Generation (RAG) combines a retrieval step (searching a knowledge base) with a generation step (an LLM producing an answer grounded in the retrieved context). This file covers vector databases, embedding models, document chunking, hybrid search (dense + sparse), and RAG evaluation.

## Resources

| Category | Title | Description | Level | Last Reviewed |
|----------|-------|-------------|-------|---------------|
| 📘 Docs | [LangChain RAG Tutorial](https://python.langchain.com/docs/tutorials/rag/) | End-to-end RAG pipeline with document loading, splitting, embedding, retrieval, and generation | Intermediate | 2026-06 |
| 📄 Paper | [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (Lewis et al., 2020)](https://arxiv.org/abs/2005.11401) | Original RAG paper proposing DPR + BART fusion-in-decoder for open-domain QA | Intermediate | 2026-06 |
| 📄 Paper | [REALM: Retrieval-Augmented Language Model Pre-Training (Guu et al., 2020)](https://arxiv.org/abs/2002.08909) | Introduces masked language modeling with a learned retriever during pretraining | Advanced | 2026-06 |
| 💻 Code/Notebook | [LlamaIndex — RAG Starter Notebook](https://docs.llamaindex.ai/en/stable/examples/) | Practical notebooks covering basic RAG, advanced retrieval, and agentic RAG patterns | Intermediate | 2026-06 |
| 🎥 Video | [RAG from Scratch (YouTube playlist)](https://www.youtube.com/playlist?list=PLfaIDFEXuae2LXbO1_PKyE1lLm3Dgbd2e) | Step-by-step video series building a RAG pipeline: chunking, embeddings, vector search, generation | Intermediate | 2026-06 |
| 🕹️ Visualizer/Playground | [ChromaDB interactive demo](https://example.com/chromadb-demo) | Browser-based playground to experiment with collections, embedding functions, and query filters | Beginner | 2026-06 |
| 📰 Blog | [Building RAG at Scale (Databricks)](https://www.databricks.com/blog/rag-scale) | Production considerations for RAG: data ingestion pipelines, chunking strategies, and latency optimization | Advanced | 2026-06 |

## RAG Architecture

```
User Query
    │
    ▼
 ┌─────────────┐     ┌──────────────────┐
 │  Embedding   │────▶│  Vector Database  │
 │  Model       │     │  (cosine search)  │
 └─────────────┘     └────────┬─────────┘
                              │ top-k chunks
                              ▼
 ┌─────────────┐     ┌──────────────────┐
 │  LLM         │◀────│  Prompt Builder  │
 │  (generator) │     │  query + context  │
 └──────┬──────┘     └──────────────────┘
        │
        ▼
  Grounded Answer
```

## Vector Databases

| Database | Type | Notes |
|----------|------|-------|
| **ChromaDB** | Open-source, embedded | Great for prototyping; runs in-process or as a server |
| **Pinecone** | Managed cloud | Serverless, high availability, built-in hybrid search |
| **Weaviate** | Open-source, cloud | Rich schema, hybrid search (vector + keyword), GraphQL API |
| **Qdrant** | Open-source, cloud | Written in Rust; filtering and payload indexing |
| **pgvector** | PostgreSQL extension | Ideal if already on Postgres; ACID compliance |

## Chunking Strategies

| Strategy | Description | Best For |
|----------|-------------|----------|
| **Fixed-size** | Split by character count with overlap | Simple, predictable chunk boundaries |
| **Recursive character** | Split on natural delimiters (`\n\n`, `\n`, `.`, ` `) | Balanced quality and simplicity |
| **Semantic** | Split at topic boundaries using embedding similarity | High-quality chunks, slower |
| **Document-based** | Use existing structure (paragraphs, sections, markdown headings) | Structured documents (PDFs, wikis) |
| **Agentic** | LLM decides chunk boundaries during ingestion | Maximum quality, costly |

## Evaluation Metrics

- **Hit rate** — fraction of queries where relevant context is in retrieved top-k
- **MRR** — Mean Reciprocal Rank of the first relevant result
- **NDCG** — Normalized Discounted Cumulative Gain (rank-aware)
- **Faithfulness** — does the LLM answer stay grounded in retrieved context?
- **Answer relevancy** — is the generated answer useful for the query?

## References

- [Dense Passage Retrieval (Karpukhin et al., 2020)](https://arxiv.org/abs/2004.04906)
- [REPLUG: Retrieval-Augmented Black-Box LMs (Shi et al., 2023)](https://arxiv.org/abs/2301.12652)
- [CRAG — Comprehensive RAG Benchmark (Yan et al., 2024)](https://arxiv.org/abs/2406.04744)
