# Diffusion Models

Diffusion models generate data by iteratively denoising a random signal. This file covers the mathematical foundations (forward/reverse diffusion, score matching), Stable Diffusion architecture (UNet + VAE + text encoder), text-to-image and text-to-video pipelines, and conditioning mechanisms (CFG, ControlNet).

## Resources

| Category | Title | Description | Level | Last Reviewed |
|----------|-------|-------------|-------|---------------|
| 📘 Docs | [HuggingFace Diffusers Library](https://huggingface.co/docs/diffusers/en/index) | Official library for pretrained diffusion pipelines: Stable Diffusion, Flux, DALL·E-style models, video | Intermediate | 2026-06 |
| 📄 Paper | [Denoising Diffusion Probabilistic Models (Ho et al., 2020)](https://arxiv.org/abs/2006.11239) | Foundational DDPM paper establishing the Gaussian diffusion + UNet framework | Advanced | 2026-06 |
| 📄 Paper | [High-Resolution Image Synthesis with Latent Diffusion Models (Rombach et al., 2022)](https://arxiv.org/abs/2112.10752) | Introduces Stable Diffusion — diffusion in latent space with cross-attention conditioning | Intermediate | 2026-06 |
| 🎥 Video | [Diffusion Models Explained (YouTube)](https://www.youtube.com/watch?v=fbLgFrlTnGU) | Visual walkthrough of DDPM training, sampling, and the reverse diffusion process | Beginner | 2026-06 |
| 💻 Code/Notebook | [Train a diffusion model from scratch (Colab)](https://github.com/example/diffusion-from-scratch) | Minimal PyTorch implementation of DDPM on MNIST / CIFAR-10 | Advanced | 2026-06 |
| 🕹️ Visualizer/Playground | [Stable Diffusion Web UI (AUTOMATIC1111)](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | Popular browser interface for SD with prompt editing, inpainting, ControlNet, and extensions | Intermediate | 2026-06 |
| 📰 Blog | [What are diffusion models? (Lilian Weng)](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/) | Comprehensive blog post covering DDPM, score matching, SDEs, and classifier-free guidance | Intermediate | 2026-06 |

## How Diffusion Works

```
Forward (noise addition):
x₀  →  x₁  →  x₂  →  ...  →  x_T  (pure noise)
q(xₜ | xₜ₋₁) = 𝒩(√(1-βₜ)·xₜ₋₁, βₜ·I)

Reverse (denoising — learned):
x_T  →  x_{T-1}  →  ...  →  x₀  (generated sample)
p_θ(x_{t-1} | x_t) = 𝒩(μ_θ(x_t, t), Σ_θ(x_t, t))
```

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Latent diffusion** | Diffusion performed in compressed latent space (VAE encoder) rather than pixel space — much faster |
| **UNet** | U-shaped CNN with down/up-sampling and skip connections; predicts the noise ε |
| **Text conditioning** | Cross-attention layers inject CLIP text embeddings into the UNet |
| **Classifier-Free Guidance (CFG)** | Interpolate between conditional and unconditional predictions; `cfg > 1` strengthens prompt adherence |
| **Scheduler** | Algorithm controlling noise schedule and sampling steps (DDPM, DDIM, DPM++); fewer steps = faster |
| **ControlNet** | Add spatial conditioning (edge maps, depth, pose) by copying and locking UNet weights |
| **VAE decoder** | Decodes the denoised latent back into pixel space |
| **Video diffusion** | Extends spatial UNet to 3D spatiotemporal convolutions (frames as a temporal dimension) |

## Text-to-Image Pipeline Flow

```
Text Prompt → CLIP Text Encoder → text embeddings
                                        │
Random latent z_T                      │
    │                                   │
    ▼                                   ▼
┌──────────────────────────────────────────┐
│  UNet (denoising loop, T → 0)            │
│  ┌────────────────────────────────────┐  │
│  │ Cross-Attention: text embeds ────► │  │
│  │ Self-Attention + Conv blocks      │  │
│  │ Skip connections                   │  │
│  └────────────────────────────────────┘  │
└──────────────────┬───────────────────────┘
                   │ z₀
                   ▼
              VAE Decoder → Generated Image
```

## References

- [Score-Based Generative Modeling through SDEs (Song et al., 2021)](https://arxiv.org/abs/2011.13456)
- [Imagen: Photorealistic Text-to-Image (Saharia et al., 2022)](https://arxiv.org/abs/2205.11487)
- [Adding Conditional Control to Text-to-Image (Zhang et al., 2023)](https://arxiv.org/abs/2302.05543)
- [Video Diffusion Models (Ho et al., 2022)](https://arxiv.org/abs/2204.03458)
