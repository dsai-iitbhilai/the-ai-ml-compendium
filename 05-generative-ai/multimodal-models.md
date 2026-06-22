# Multimodal Models

Multimodal models process and generate across multiple modalities — text, images, audio, and video. This file covers vision-language models (VLMs) like CLIP, GPT-4V, and LLaVA, contrastive pretraining, image- and audio-generation conditioning, and unified multimodal architectures.

## Resources

| Category | Title | Description | Level | Last Reviewed |
|----------|-------|-------------|-------|---------------|
| 📄 Paper | [Learning Transferable Visual Models from Natural Language Supervision (CLIP, Radford et al., 2021)](https://arxiv.org/abs/2103.00020) | Contrastive image-text pretraining enabling zero-shot classification and multimodal retrieval | Intermediate | 2026-06 |
| 📄 Paper | [LLaVA: Large Language and Vision Assistant (Liu et al., 2023)](https://arxiv.org/abs/2304.08485) | Connects a CLIP vision encoder to a Vicuna LLM via a simple projection layer; strong instruction following | Intermediate | 2026-06 |
| 📄 Paper | [Flamingo: A Visual Language Model for Few-Shot Learning (Alayrac et al., 2022)](https://arxiv.org/abs/2204.14198) | Pioneers interleaved text-image few-shot learning with gated cross-attention | Advanced | 2026-06 |
| 💻 Code/Notebook | [HuggingFace — Multimodal Transformers](https://huggingface.co/docs/transformers/en/multimodal) | Official notebooks for CLIP, BLIP2, Llava, and ImageBind inference and fine-tuning | Intermediate | 2026-06 |
| 🕹️ Visualizer/Playground | [CLIP Interrogator](https://replicate.com/example/clip-interrogator) | Given an image, generates the text prompt that best describes it using CLIP embeddings | Beginner | 2026-06 |
| 🎥 Video | [Vision-Language Models explained (Stanford MLSys)](https://www.youtube.com/watch?v=example) | Seminar covering contrastive learning, visual grounding, and recent VLM architectures | Advanced | 2026-06 |
| 📰 Blog | [GPT-4V System Card (OpenAI)](https://cdn.openai.com/papers/GPTV_System_Card.pdf) | Analysis of GPT-4V's visual capabilities: OCR, chart reading, spatial reasoning, and safety | Intermediate | 2026-06 |

## Architecture Patterns

| Pattern | Examples | Description |
|---------|----------|-------------|
| **Contrastive dual-encoder** | CLIP, SigLIP, ImageBind | Separate encoders for each modality; trained with contrastive loss to align embeddings |
| **Frozen encoder + connector + LLM** | LLaVA, BLIP-2, Qwen-VL | Vision encoder frozen; lightweight connector (Q-Former, MLP) maps to text LLM |
| **Unified transformer** | Flamingo, GPT-4V, Gemini | Single transformer processes interleaved multimodal tokens via cross-attention |
| **Multimodal diffusion** | Stable Diffusion, Sora | Text/audio/video conditioning via cross-attention in a denoising UNet |
| **Audio-language models** | Whisper + LLM, AudioLDM | Speech-to-text, audio captioning, or text-to-audio generation |

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Contrastive pretraining** | Maximize cosine similarity between paired (image, text) embeddings; minimize for unpaired pairs |
| **Q-Former** | Lightweight BERT-sized transformer that queries frozen vision features and feeds them to frozen LLM (BLIP-2) |
| **Visual grounding** | Locating objects in an image from natural language (phrase → bounding box) |
| **Interleaved inputs** | Mixed sequences of images and text within a single prompt (Flamingo, GPT-4V) |
| **ImageBind** | Learns shared embedding space across 6 modalities: image, text, audio, depth, thermal, IMU |
| **Multimodal chain-of-thought** | Step-by-step reasoning that integrates visual evidence alongside textual reasoning |

## Selected Models

| Model | Modalities | Open-Source | Key Innovation |
|-------|-----------|-------------|----------------|
| **CLIP** | Image + Text | ✅ | Contrastive dual-encoder with 400M image-text pairs |
| **BLIP-2** | Image + Text | ✅ | Q-Former bridging frozen vision encoder and LLM |
| **LLaVA** | Image + Text | ✅ | Simple linear projection; strong instruction following |
| **Flamingo** | Image + Video + Text | ❌ (weights) | Gated cross-attention for few-shot multimodal |
| **GPT-4V** | Image + Text | ❌ | Advanced OCR, chart, and spatial reasoning |
| **Gemini** | Image + Audio + Video + Text | ❌ | Natively multimodal from pretraining |
| **ImageBind** | 6 modalities | ✅ | Emergent zero-shot binding across modalities |

## References

- [BLIP-2: Bootstrapping Language-Image Pre-training (Li et al., 2023)](https://arxiv.org/abs/2301.12597)
- [ImageBind: One Embedding Space To Bind Them All (Girdhar et al., 2023)](https://arxiv.org/abs/2305.05665)
- [PaLI-X: Scaling Language-Image Models (Chen et al., 2023)](https://arxiv.org/abs/2305.18565)
- [Any-to-Any Generation via Composable Diffusion (Tang et al., 2023)](https://arxiv.org/abs/2305.11846)
