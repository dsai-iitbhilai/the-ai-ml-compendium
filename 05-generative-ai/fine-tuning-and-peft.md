# Fine-Tuning & PEFT

>Fine-tuning adapts a pretrained LLM to a specific domain or task by updating its weights. Parameter-Efficient Fine-Tuning (PEFT) methods like LoRA and QLoRA make this feasible on consumer hardware by updating only a small set of trainable parameters. This file also covers instruction tuning, adapter architectures, and the mathematical mechanics of weight decomposition.

**Last Reviewed:** 2026-06

**Prerequisites:** [LLM Fundamentals](llm-fundamentals.md) · Linear Algebra

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| *HuggingFace PEFT Documentation* | Intermediate | <https://huggingface.co/docs/peft/en/index> | Official library docs for LoRA, IA3, AdaLoRA, Prompt Tuning, and more with code examples |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *LoRA: Low-Rank Adaptation* (Hu et al., 2021) | Intermediate | <https://arxiv.org/abs/2106.09685> | Introduces low-rank weight updates (${\Delta}W = BA$) that can be merged at inference time with zero added latency |
| *QLoRA: Efficient Finetuning of Quantized LLMs* (Dettmers et al., 2023) | Advanced | <https://arxiv.org/abs/2305.14314> | Combines 4-bit NormalFloat quantization with LoRA to fine-tune 65B models on a single 48GB GPU |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| *QLoRA Reference Implementation* | Advanced | <https://github.com/artidoro/qlora> | The official end-to-end repository for fine-tuning LLMs with QLoRA on custom datasets |
| *Axolotl* | Advanced | <https://github.com/axolotl-ai-cloud/axolotl> | Open-source framework for simplified fine-tuning with support for multiple PEFT methods and distributed training pipelines |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| *HuggingFace — Fine-tuning LLMs* | Intermediate | <https://huggingface.co/learn/nlp-course/chapter3/1> | Course module covering tokenizer training, dataset preparation, and trainer API for SFT |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *Practical Tips for Finetuning LLMs* (Sebastian Raschka) | Intermediate | <https://magazine.sebastianraschka.com/p/practical-tips-for-finetuning-llms> | Practical deep-dive on LoRA rank selection, where to apply adapters, and merging strategies |

---

## PEFT Methods Comparison

| Method | Trainable Params | Inference Overhead | Key Idea |
|--------|-----------------|-------------------|----------|
| **Full Fine-Tuning** | 100% | None | Update all weights (expensive, prone to catastrophic forgetting) |
| **LoRA** | 0.1–1% | None (merged) | Low-rank matrices ($B \in \mathbb{R}^{d \times r}, A \in \mathbb{R}^{r \times k}$) injected into attention layers |
| **QLoRA** | 0.1–1% | None (merged) | LoRA on top of 4-bit quantized base model utilizing double quantization |
| **AdaLoRA** | 0.1–1% | None (merged) | Budget-aware rank allocation dynamically adjusting singular values (SVD) across layers |
| **IA3** | ~0.01% | None (merged) | Learns element-wise scaling vectors (fewest params) |
| **Prompt Tuning** | ~0.01% | Increased context | Learns soft prompt embeddings prepended to input sequence |

---

## Key Concepts Checklist

- **Weight Decomposition Logic:** Formulating weight updates as ${\Delta}W = B \cdot A$, where $B$ and $A$ are low-rank matrices, ensuring $W_{out} = W_{in} + {\Delta}W$.
- **Quantization Constants:** The mathematics of mapping high-precision floating points into 4-bit NormalFloat (NF4) bins for QLoRA to ensure theoretically optimal storage.
- **Catastrophic Forgetting:** Measuring the degradation of the original pretraining probability distribution $P(y|x)$ after fine-tuning on a highly specific target domain.
- **Instruction Tuning:** Supervised Fine-Tuning (SFT) mapping cross-entropy loss over structured instruction-response pairs rather than standard autoregressive text completion.
- **Merge & Unload Constraints:** Matrix addition mechanics to permanently apply the adapter ${\Delta}W$ to the base model weights to eliminate latency bottlenecks in production inference.
- **Rank ($r$) and Alpha ($\alpha$) Scaling:** Understanding the theoretical capacity of the adapter ($r$) and the scaling factor ($\frac{\alpha}{r}$) on the learning rate.

---

## Projects / Practice

| Project | Description |
|---|---|
| **Mathematical LoRA Derivation** | Bypass the HuggingFace `peft` library to implement the LoRA forward and backward passes completely from scratch in PyTorch or NumPy. Derive the gradients for matrices $A$ and $B$, mathematically proving that initializing $B$ to zero guarantees no initial deviation from the base model's state. |
| **Scalable Agentic SFT Pipeline** | Construct a scalable, CI/CD-integrated fine-tuning pipeline utilizing `Axolotl` on a cloud GPU instance. Train a domain-specific agentic model on a synthetically generated tool-calling dataset, employing QLoRA with FlashAttention. Package the merged model weights into a Dockerized endpoint for high-throughput production inference. |

---

## References

- [T-Few: Fine-Tuning T0 with Adapters (Liu et al., 2022)](https://arxiv.org/abs/2205.05638)
- [Scaling Down to Scale Up: A Guide to PEFT (Lialin et al., 2023)](https://arxiv.org/abs/2304.01852)
- [LLaMA-Adapter (Zhang et al., 2023)](https://arxiv.org/abs/2303.06865)

---

## See also

- [LLM Fundamentals](llm-fundamentals.md) — Architectural basis for adapter targeting (e.g., $q\_proj$, $v\_proj$).
- [Prompt Engineering](prompt-engineering.md) — Comparing zero-shot prompt optimization against parameter updates for domain adaptation.
- [MLOps](../visualizers-and-playgrounds/README.md) — Deployment engineering practices for testing, versioning, and hosting fine-tuned checkpoints.
"""