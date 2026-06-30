# Multimodal Models

> Multimodal models process and generate representations across divergent sensory modalities — text, images, audio, and video. This file covers vision-language models (VLMs), contrastive pretraining mathematics, spatial reasoning topologies, visual grounding, and unified cross-attention architectures.

**Last Reviewed:** 2026-06

**Prerequisites:** [LLM Fundamentals](llm-fundamentals.md) · [Diffusion Models](diffusion-models.md) · Matrix Calculus

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| *HuggingFace Multimodal Generation Documentation* | Intermediate | <https://huggingface.co/docs/transformers/tasks/any_to_any> | Official guides for omni-modal inference, covering `AutoModelForMultimodalLM` and multimodal pipelines. |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| *Stanford CME296: Diffusion & Large Vision Models* | Advanced | <https://www.youtube.com/watch?v=oyLUvz9nR6E> | Lecture covering latent spaces, state-of-the-art vision architectures, and image editing. |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| *DeepLearning.AI — Understanding and Applying Text Embeddings* | Beginner | <https://www.deeplearning.ai/short-courses/> | Foundational concepts in building vector spaces that translate across text and image modalities. |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| *CLIP Interrogator* | Beginner | <https://github.com/pharmapsychotic/clip-interrogator> | Tool that generates the optimal text prompt describing an image by mathematically aligning CLIP embeddings. |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *Learning Transferable Visual Models (CLIP)* (Radford et al., 2021) | Intermediate | <https://arxiv.org/abs/2103.00020> | Contrastive image-text pretraining enabling zero-shot classification and semantic retrieval. |
| *LLaVA: Large Language and Vision Assistant* (Liu et al., 2023) | Intermediate | <https://arxiv.org/abs/2304.08485> | Connects a CLIP vision encoder to a Vicuna LLM via a linear projection layer. |
| *Flamingo: A Visual Language Model for Few-Shot Learning* (Alayrac et al., 2022) | Advanced | <https://arxiv.org/abs/2204.14198> | Pioneers interleaved text-image few-shot learning with gated cross-attention mechanisms. |
| *GPT-4V System Card* (OpenAI) | Intermediate | <https://cdn.openai.com/papers/GPTV_System_Card.pdf> | Analysis of multimodal OCR, chart reading, spatial reasoning, and constraint boundaries. |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| *Qwen-VL Open Source Pipeline* | Advanced | <https://github.com/QwenLM/Qwen-VL> | End-to-end repository for setting up and fine-tuning an advanced VLM capable of bounding box predictions. |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *ImageBind: One Embedding Space to Bind Them All* (Meta AI) | Intermediate | <https://ai.meta.com/blog/imagebind-six-modalities-single-shared-representation/> | Overview of emergent zero-shot binding across six distinct modalities (audio, IMU, depth, thermal, text, image). |

---

## Architecture Patterns

| Pattern | Examples | Description |
|---------|----------|-------------|
| **Contrastive Dual-Encoder** | CLIP, SigLIP | Separate encoders (ViT + Transformer) trained with InfoNCE loss to maximize the cosine similarity of paired embeddings. |
| **Frozen Encoder + Connector + LLM** | LLaVA, BLIP-2 | Vision encoder is frozen; a lightweight learnable connector (MLP or Q-Former) maps visual embeddings into the LLM's token space. |
| **Unified Transformer** | Flamingo, Gemini | A single transformer explicitly models interleaved multimodal tokens, dynamically switching context via cross-attention. |
| **Multimodal Diffusion** | Stable Diffusion, Sora | Text/audio conditioning mathematically injected via cross-attention into a denoising UNet for generative outputs. |

---

## Key Concepts Checklist

- **Contrastive Pretraining Mathematics:** Minimizing the distance between positive $(I_i, T_i)$ pairs while maximizing distance from negative pairs $(I_i, T_j)$ across a massive batch matrix.
- **Visual Grounding:** Emitting numerical bounding box coordinates from natural language phrases (e.g., predicting $[y_{min}, x_{min}, y_{max}, x_{max}]$).
- **Q-Former:** A lightweight transformer bridging a frozen vision encoder and an LLM by querying visual features to extract the most semantically dense tokens.
- **Multimodal Chain-of-Thought (CoT):** Integrating step-by-step logical deduction while simultaneously referencing intermediate spatial or visual evidence.
- **Interleaved Sequences:** Managing sequence lengths and causal masks when an input array consists of $[Text, Image, Text, Text, Image]$.

---

## Selected Models

| Model | Modalities | Open-Source | Key Innovation |
|-------|-----------|-------------|----------------|
| **CLIP** | Image + Text |  | Contrastive dual-encoder with 400M image-text pairs |
| **BLIP-2** | Image + Text |  | Q-Former bridging frozen vision encoder and LLM |
| **LLaVA** | Image + Text |  | Simple linear projection; strong instruction following |
| **Flamingo** | Image + Video + Text |  (weights) | Gated cross-attention for few-shot multimodal |
| **GPT-4V** | Image + Text |  | Advanced OCR, chart, and spatial reasoning |
| **Gemini** | Image + Audio + Video + Text |  | Natively multimodal from pretraining |
| **ImageBind** | 6 modalities |  | Emergent zero-shot binding across modalities |

## Projects / Practice

| Project | Description |
|---|---|
| **Mathematical CLIP Derivation** | Write the forward pass and InfoNCE contrastive loss function from scratch using pure `NumPy` and `PyTorch` primitives. Demonstrate how the temperature parameter scales the logits matrix mathematically before applying the softmax. |
| **End-to-End VLM Web Scraper** | Build a robust extraction tool using `Selenium` and a deployed local `Qwen-VL` instance. Feed DOM screenshots to the model to spatially reason and extract specific HTML element bounding boxes that defeat dynamic class-name obfuscation. |
| **Deployed OCR & Analytics Microservice** | Utilize `FastAPI` and `llama.cpp` to host a multimodal endpoint capable of ingesting charts and diagrams. Implement a rigorous schema constraint using structured outputs to ensure the VLM returns parsed chart data as validated JSON for data analysis pipelines. |

---

## References

- [BLIP-2: Bootstrapping Language-Image Pre-training (Li et al., 2023)](https://arxiv.org/abs/2301.12597)
- [ImageBind: One Embedding Space To Bind Them All (Girdhar et al., 2023)](https://arxiv.org/abs/2305.05665)
- [PaLI-X: Scaling Language-Image Models (Chen et al., 2023)](https://arxiv.org/abs/2305.18565)
- [Any-to-Any Generation via Composable Diffusion (Tang et al., 2023)](https://arxiv.org/abs/2305.11846)

---

## See also

- [LLM Fundamentals](llm-fundamentals.md) — The core autoregressive architecture underlying unified multimodal models.
- [Diffusion Models](diffusion-models.md) — Understanding the generation side of multimodal systems.
- [Agentic AI](../06-agentic-ai/README.md) — Giving VLMs tools to execute actions based on spatial reasoning.