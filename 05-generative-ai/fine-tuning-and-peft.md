# Fine-Tuning & PEFT

Fine-tuning adapts a pretrained LLM to a specific domain or task by updating its weights. Parameter-Efficient Fine-Tuning (PEFT) methods like LoRA and QLoRA make this feasible on consumer hardware by updating only a small set of trainable parameters. This file also covers instruction tuning, adapter architectures, and catastrophic forgetting.

## Resources

| Category | Title | Description | Level | Last Reviewed |
|----------|-------|-------------|-------|---------------|
| 📘 Docs | [HuggingFace PEFT Documentation](https://huggingface.co/docs/peft/en/index) | Official library docs for LoRA, IA3, AdaLoRA, Prompt Tuning, and more with code examples | Intermediate | 2026-06 |
| 📄 Paper | [LoRA: Low-Rank Adaptation (Hu et al., 2021)](https://arxiv.org/abs/2106.09685) | Introduces low-rank weight updates that can be merged at inference time with zero added latency | Intermediate | 2026-06 |
| 📄 Paper | [QLoRA: Efficient Finetuning of Quantized LLMs (Dettmers et al., 2023)](https://arxiv.org/abs/2305.14314) | Combines 4-bit NormalFloat quantization with LoRA to fine-tune 65B models on a single 48GB GPU | Advanced | 2026-06 |
| 💻 Code/Notebook | [QLoRA fine-tuning tutorial (Colab)](https://github.com/example/qlora-finetune) | End-to-end notebook for fine-tuning Llama 2 / Mistral with QLoRA on custom datasets | Intermediate | 2026-06 |
| 🎓 Course | [HuggingFace — Fine-tuning LLMs](https://huggingface.co/learn/nlp-course/chapter3/1) | Course module covering tokenizer training, dataset preparation, and trainer API for SFT | Intermediate | 2026-06 |
| 📰 Blog | [LoRA explained (Sebastian Raschka)](https://magazine.sebastianraschka.com/p/practical-tips-for-finetuning-llms) | Practical deep-dive on LoRA rank selection, where to apply adapters, and merging strategies | Intermediate | 2026-06 |
| 📰 Blog | [Axolotl — fine-tuning framework overview](https://github.com/example/axolotl) | Open-source library for simplified fine-tuning with support for multiple PEFT methods and distributed training | Advanced | 2026-06 |

## PEFT Methods Comparison

| Method | Trainable Params | Inference Overhead | Key Idea |
|--------|-----------------|-------------------|----------|
| **Full Fine-Tuning** | 100% | None | Update all weights (expensive, prone to forgetting) |
| **LoRA** | 0.1–1% | None (merged) | Low-rank matrices injected into attention layers |
| **QLoRA** | 0.1–1% | None (merged) | LoRA on top of 4-bit quantized base model |
| **AdaLoRA** | 0.1–1% | None (merged) | Budget-aware rank allocation across layers |
| **IA3** | ~0.01% | None (merged) | Learns element-wise scaling vectors (fewest params) |
| **Prompt Tuning** | ~0.01% | Increased context | Learns soft prompt embeddings prepended to input |
| **(IA)³** | ~0.01% | None (merged) | Infused Adapter by Inhibiting and Amplifying Inner Activations |

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Catastrophic forgetting** | Loss of previously learned knowledge when fine-tuning on narrow distributions |
| **Instruction tuning** | Fine-tuning on (instruction, response) pairs to improve general instruction following |
| **Adapter layers** | Small bottleneck networks inserted between transformer layers (Houlsby et al., 2019) |
| **Quantization** | Reducing model precision (FP16 → int4) to decrease memory; NF4 used in QLoRA |
| **Merge & unload** | Applying LoRA weights into the base model so inference runs at full speed |
| **Multi-task fine-tuning** | Training a single model on multiple tasks simultaneously with shared parameters |

## Training Tips

- **Rank (r) selection**: Start with r=8–16 for LoRA; increase for more complex tasks
- **Target modules**: Fine-tune `q_proj` and `v_proj` first; add `o_proj`, `k_proj` for higher capacity
- **Learning rate**: 1e-4 to 5e-4 is typical for LoRA; lower for full fine-tuning (1e-5)
- **Dataset quality**: 500–2000 high-quality examples often outperform 50k noisy examples
- **Evaluation**: Always hold out a validation set; watch for overfitting on small PEFT runs

## References

- [T-Few: Fine-Tuning T0 with Adapters (Liu et al., 2022)](https://arxiv.org/abs/2205.05638)
- [Scaling Down to Scale Up: A Guide to PEFT (Lialin et al., 2023)](https://arxiv.org/abs/2304.01852)
- [LLaMA-Adapter (Zhang et al., 2023)](https://arxiv.org/abs/2303.06865)
