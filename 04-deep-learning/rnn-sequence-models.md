# RNN & Sequence Models

> Recurrent neural networks, LSTMs, GRUs, and the foundations of sequence modeling. Covers language modeling, time series, machine translation, and the principles that led to the attention mechanism.

**Last Reviewed:** 2026-06

**Prerequisites:** [04 – Deep Learning / README](README.md), [Neural Network Fundamentals](neural-network-fundamentals.md), [Probability & Statistics](../01-foundations/mathematics/probability-statistics.md)

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| *Deep Learning* — Chapter 10 (Goodfellow et al.) | Intermediate | [Link](https://example.com/deeplearningbook-ch10) | RNN theory, BPTT, and sequence modeling |
| *Understanding Deep Learning* — Chapter 10 (Prince) | Intermediate | [Link](https://example.com/udl-ch10) | Modern treatment of RNNs and gated architectures |
| *Dive into Deep Learning* — Chapter 9 (RNNs, LSTMs, GRUs) | Beginner | [Link](https://example.com/d2l-rnn) | Code-first RNN implementation with GPU training |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| StatQuest — *Recurrent Neural Networks (RNNs) Clearly Explained* | Beginner | [Link](https://example.com/statquest-rnn) | Clear, accessible RNN intuition |
| Stanford CS231n — *Recurrent Neural Networks, Image Captioning* | Intermediate | [Link](https://example.com/cs231n-rnn) | RNNs for vision-language tasks |
| DeepMind — *The Unreasonable Effectiveness of Recurrent Neural Networks* (Karpathy) | Intermediate | [Link](https://example.com/karpathy-rnn-talk) | Classic talk on RNNs for character-level language modeling |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| Coursera — *Sequence Models* (DeepLearning.AI) | Beginner | [Link](https://example.com/coursera-seq) | Andrew Ng's fifth DL course; RNNs, LSTMs, attention, seq2seq |
| Stanford CS224n — *Natural Language Processing with Deep Learning* | Intermediate | [Link](https://example.com/cs224n-rnn) | Comprehensive NLP course covering RNNs, transformers |
| Fast.ai — *NLP with RNNs and LSTMs* | Beginner | [Link](https://example.com/fastai-nlp-rnn) | Practical NLP with ULMFiT and AWD-LSTM |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| RNN / LSTM Rollout Visualizer | Intermediate | [Link](https://example.com/rnn-rollout) | Step through time; see hidden states and cell states |
| Weights & Biases — *LSTM Gradient Flow* | Advanced | [Link](https://example.com/wandb-lstm-gradients) | Visualize vanishing/exploding gradients in RNNs |
| Distill.pub — *Visualizing the LSTM Cell* | Intermediate | [Link](https://example.com/distill-lstm) | Interactive breakdown of the LSTM gating mechanism |

### 📄 Paper

| Title | Level | Link | Notes |
|---|---|---|---|
| *Long Short-Term Memory* (Hochreiter & Schmidhuber, 1997) | Advanced | [Link](https://example.com/lstm-original) | Original LSTM paper — the gating mechanism that solved vanishing gradients |
| *Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation* (Cho et al., 2014) | Advanced | [Link](https://example.com/gru-paper) | Introduced the GRU and the encoder-decoder framework |
| *Sequence to Sequence Learning with Neural Networks* (Sutskever et al., 2014) | Intermediate | [Link](https://example.com/seq2seq) | Seq2Seq with LSTMs; foundation of modern machine translation |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| Character-level RNN in PyTorch | Beginner | [Link](https://example.com/char-rnn) | Train an RNN to generate text character by character |
| LSTM for Time Series Forecasting | Intermediate | [Link](https://example.com/lstm-timeseries) | Stock price / weather forecasting with LSTMs |
| Seq2Seq with Attention (PyTorch) | Intermediate | [Link](https://example.com/seq2seq-attention) | Full neural machine translation example |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *The Unreasonable Effectiveness of Recurrent Neural Networks* (Andrej Karpathy) | Intermediate | [Link](https://example.com/karpathy-rnn-blog) | Inspiring blog post that popularized char-level RNNs |
| *Understanding LSTM Networks* (Christopher Olah) | Intermediate | [Link](https://example.com/colah-lstm) | The most widely-read explanation of LSTMs |

---

## Key Concepts Checklist

- [ ] Recurrent neural network architecture and unrolling
- [ ] Backpropagation through time (BPTT)
- [ ] Vanishing and exploding gradients in RNNs
- [ ] LSTM (input, forget, output gates; cell state)
- [ ] GRU (update and reset gates)
- [ ] Bidirectional RNNs
- [ ] Encoder-decoder (seq2seq) architecture
- [ ] Attention mechanism (Bahdanau / Luong)
- [ ] Applications: language modeling, machine translation, time series, speech
- [ ] Teacher forcing and scheduled sampling

---

## Projects / Practice

| Project | Description |
|---|---|
| Text Generator | Train a character-level LSTM on Shakespeare or Wikipedia text |
| Sentiment Classifier | Build an LSTM-based sentiment analyzer on IMDb reviews |
| Time Series Forecaster | Predict temperature, stock prices, or energy consumption with LSTMs |

---

## See also

- [Transformers](transformers.md) — the evolution from RNNs to attention-only models
- [Neural Network Fundamentals](neural-network-fundamentals.md) — backpropagation and gradient descent basics
- [Frameworks](frameworks.md) — PyTorch RNN/LSTM modules and training utilities
