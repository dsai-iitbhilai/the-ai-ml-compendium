# Diffusion Models

> Diffusion models generate data by iteratively denoising a random signal. This file covers the mathematical foundations, latent diffusion architectures (Stable Diffusion), text-to-image/video pipelines, and conditioning mechanisms (CFG, ControlNet).

**Last Reviewed:** 2026-06

**Prerequisites:** [Deep Learning](../04-deep-learning/README.md) · Probability Theory · Calculus

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| *HuggingFace Diffusers Library* | Intermediate | <https://huggingface.co/docs/diffusers/index> | Official library for pretrained diffusion pipelines (SD, Flux, video). |
| *NVIDIA: Generative AI with Diffusion* | Advanced | <https://developer.nvidia.com/blog/improving-diffusion-models-as-an-alternative-to-gans-part-1/> | Deep dive into the math and scaling of enterprise diffusion models. |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| *fast.ai: Deep Learning Part 2 (Diffusion)* | Intermediate | <https://course.fast.ai/Lessons/part2.html> | Code-first video lectures building Stable Diffusion completely from scratch. |
| *Diffusion Models Explained* | Beginner | <https://www.youtube.com/watch?v=HoKDTa5jHvg> | Visual walkthrough of DDPM training and the reverse diffusion process. |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| *DeepLearning.AI — How Diffusion Models Work* | Beginner | <https://www.deeplearning.ai/short-courses/how-diffusion-models-work/> | Short course by Sharon Zhou covering the intuition and sampling methods. |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| *AUTOMATIC1111 Web UI* | Intermediate | <https://github.com/AUTOMATIC1111/stable-diffusion-webui> | Popular browser interface for SD with prompt editing, inpainting, and ControlNet. |
| *ComfyUI* | Advanced | <https://github.com/comfyanonymous/ComfyUI> | Powerful node-based GUI for building complex diffusion pipelines visually. |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *Denoising Diffusion Probabilistic Models* (Ho et al., 2020) | Advanced | <https://arxiv.org/abs/2006.11239> | Foundational DDPM paper establishing the Gaussian diffusion framework. |
| *Latent Diffusion Models* (Rombach et al., 2022) | Intermediate | <https://arxiv.org/abs/2112.10752> | Introduces Stable Diffusion — running diffusion in a compressed latent space. |
| *Denoising Diffusion Implicit Models* (Song et al., 2020) | Advanced | <https://arxiv.org/abs/2010.02502> | DDIM: Introduces deterministic, non-Markovian sampling to speed up generation. |
| *Classifier-Free Diffusion Guidance* (Ho & Salimans, 2022) | Advanced | <https://arxiv.org/abs/2207.12598> | The mathematical basis for prompt adherence without needing a separate classifier. |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| *The Annotated Diffusion Model* | Advanced | <https://huggingface.co/blog/annotated-diffusion> | Minimal, line-by-line PyTorch implementation of DDPM based on the original paper. |
| *Keras DDIM Tutorial* | Intermediate | <https://keras.io/examples/generative/ddim/> | End-to-end TensorFlow/Keras tutorial for building and training a DDIM model. |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *What are diffusion models?* (Lilian Weng) | Advanced | <https://lilianweng.github.io/posts/2021-07-11-diffusion-models/> | Comprehensive post covering DDPM, score matching, and SDEs. |
| *Diffusion models are autoencoders* (Sander Dieleman) | Advanced | <https://benanne.github.io/2022/01/31/diffusion.html> | Offers a unique perspective linking diffusion math to hierarchical VAEs. |

---

## How Diffusion Works

```text
Forward (noise addition):
x₀  →  x₁  →  x₂  →  ...  →  x_T  (pure noise)
q(xₜ | xₜ₋₁) = 𝒩(√(1-βₜ)·xₜ₋₁, βₜ·I)

Reverse (denoising — learned):
x_T  →  x_{T-1}  →  ...  →  x₀  (generated sample)
p_θ(x_{t-1} | x_t) = 𝒩(μ_θ(x_t, t), Σ_θ(x_t, t))
```

---

## Key Concepts Checklist

- **Latent Diffusion:** Diffusion in compressed latent space (via VAE) rather than pixel space.
- **UNet:** U-shaped CNN with cross-attention that predicts the noise $\epsilon$ added at step $t$.
- **Text Conditioning:** Injecting CLIP text embeddings into the UNet via cross-attention layers.
- **Classifier-Free Guidance (CFG):** Interpolating conditional and unconditional predictions to strengthen prompt adherence.
- **Scheduler:** Algorithms (DDPM, DDIM, DPM++) controlling noise schedules and step sizes.
- **ControlNet:** Spatial conditioning (edge maps, depth, pose) by copying and locking UNet weights.

---

## Text-to-Image Pipeline Flow

```text
Text Prompt → CLIP Text Encoder → text embeddings
                                        │
Random latent z_T                       │
    │                                   │
    ▼                                   ▼
┌──────────────────────────────────────────┐
│  UNet (denoising loop, T → 0)            │
│  ┌────────────────────────────────────┐  │
│  │ Cross-Attention: text embeds ────► │  │
│  │ Self-Attention + Conv blocks       │  │
│  │ Skip connections                   │  │
│  └────────────────────────────────────┘  │
└──────────────────┬───────────────────────┘
                   │ z₀
                   ▼
              VAE Decoder → Generated Image
```

---

## Projects / Practice

| Project | Description |
|---|---|
| **Build a Custom Scheduler** | Implement a custom DDIM scheduler from scratch in PyTorch to plug into a HuggingFace Diffusers pipeline, optimizing inference speed. |
| **Train a Domain-Specific LoRA** | Use `diffusers` to train a Low-Rank Adaptation (LoRA) on a specific art style, merging it with a base SD 1.5 or SDXL model. |
| **Node-Based API Backend** | Create a backend microservice that triggers a headless `ComfyUI` generation workflow via API, dynamically swapping out ControlNet inputs. |

---

## References

- [Score-Based Generative Modeling through SDEs (Song et al., 2021)](https://arxiv.org/abs/2011.13456)
- [Imagen: Photorealistic Text-to-Image (Saharia et al., 2022)](https://arxiv.org/abs/2205.11487)
- [Adding Conditional Control to Text-to-Image (Zhang et al., 2023)](https://arxiv.org/abs/2302.05543)
- [Video Diffusion Models (Ho et al., 2022)](https://arxiv.org/abs/2204.03458)

---

## See also

- [Deep Learning](../04-deep-learning/README.md) — Fundamental neural network and CNN architectures underlying the UNet.
- [Fine-Tuning & PEFT](fine-tuning-and-peft.md) — techniques for adapting diffusion models (e.g., DreamBooth, LoRA) to diffusion models.
- [MLOps](../07-mlops-and-deployment/README.md) — Hosting heavy image/video generation endpoints in production.