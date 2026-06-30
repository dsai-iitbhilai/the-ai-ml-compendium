# RNN & Sequence Models

> Learn how neural networks process sequential data using Recurrent Neural Networks (RNNs), LSTMs, GRUs, Seq2Seq models, and Attention—the foundation that eventually evolved into Transformers and modern LLMs.

**Last Reviewed:** 2026-06

**Prerequisites:** [04 – Deep Learning / README](README.md) · [Neural Network Fundamentals](neural-network-fundamentals.md) · [Probability & Statistics](../01-foundations/mathematics/probability-statistics.md)

---

>  **Tip:** RNNs are no longer state-of-the-art for NLP, but understanding them makes Transformers, Attention, and LLMs much easier to grasp.

---

# Learning Roadmap

```text
Sequential Data
      ↓
Simple RNN
      ↓
Backpropagation Through Time
      ↓
Vanishing Gradients
      ↓
LSTM
      ↓
GRU
      ↓
Bidirectional RNN
      ↓
Encoder–Decoder
      ↓
Attention Mechanism
      ↓
Transformers
```

---

# Resources

## 📘 Documentation & Books

| Title | Level | Link | Notes |
|---|---|---|---|
| Dive into Deep Learning — RNNs | Beginner | <https://d2l.ai/chapter_recurrent-neural-networks/index.html> | Best free hands-on introduction with code |
| Deep Learning (Goodfellow, Bengio & Courville) – Chapter 10 | Intermediate | <https://www.deeplearningbook.org> | Complete theory of sequence models |
| Understanding Deep Learning (Simon Prince) | Intermediate | <https://udlbook.github.io/udlbook/> | Modern explanation of gated RNNs |
| Speech and Language Processing (Jurafsky & Martin) | Intermediate | <https://web.stanford.edu/~jurafsky/slp3/> | NLP textbook covering RNNs, LSTMs, Seq2Seq and Attention |

---

## 🎥 Videos

| Title | Level | Link | Notes |
|---|---|---|---|
| StatQuest — Recurrent Neural Networks | Beginner | <https://www.youtube.com/@statquest> | Excellent intuition for RNNs |
| Christopher Olah — Understanding LSTMs (Video Companion) | Beginner | <https://www.youtube.com/results?search_query=understanding+lstm+christopher+olah> | Visual explanation of LSTM cells |
| Stanford CS231n — RNNs & Image Captioning | Intermediate | <https://www.youtube.com/watch?v=yCC09vCHzF8> | Sequence modeling from Stanford |
| Stanford CS224N (2023 Playlist) | Intermediate | <https://www.youtube.com/playlist?list=PLoROMvodv4rPt5D0zs3YhbWSZA8Q_DyiJ> | Modern NLP course covering RNNs through Transformers |
| Andrej Karpathy — The Unreasonable Effectiveness of RNNs | Intermediate | <https://www.youtube.com/results?search_query=andrej+karpathy+recurrent+neural+networks> | Classic talk on sequence generation |

---

## 🎓 Courses

| Title | Level | Link | Notes |
|---|---|---|---|
| DeepLearning.AI — Sequence Models | Beginner | <https://www.coursera.org/learn/nlp-sequence-models> | Andrew Ng's course on RNNs, LSTMs and Attention |
| Stanford CS224N | Intermediate | <https://web.stanford.edu/class/cs224n/> | Best university NLP course |
| fast.ai Practical Deep Learning | Beginner | <https://course.fast.ai> | Includes NLP using AWD-LSTM |
| Dive into Deep Learning | Beginner | <https://d2l.ai> | Interactive notebooks for RNNs and sequence models |

---

## 🕹 Interactive Visualizers

| Title | Level | Link | Notes |
|---|---|---|---|
| LSTM Explorer (TensorFlow Playground-inspired) | Beginner | <https://lstm-demo.github.io/> | Interactive LSTM visualization |
| Christopher Olah — Understanding LSTM Networks | Beginner | <https://colah.github.io/posts/2015-08-Understanding-LSTMs/> | The best visual explanation of LSTMs |
| Distill — Attention and Sequence Visualization | Intermediate | <https://distill.pub> | Interactive deep learning visualizations |
| TensorFlow Embedding Projector | Intermediate | <https://projector.tensorflow.org> | Explore learned word embeddings |

---

## 📄 Must Read Papers

| Title | Level | Link | Notes |
|---|---|---|---|
| Long Short-Term Memory (1997) | Advanced | <https://www.bioinf.jku.at/publications/older/2604.pdf> | Original LSTM paper |
| Learning Phrase Representations using RNN Encoder–Decoder | Advanced | <https://arxiv.org/abs/1406.1078> | Introduced GRU and Encoder–Decoder |
| Sequence to Sequence Learning with Neural Networks | Intermediate | <https://arxiv.org/abs/1409.3215> | Foundation of neural machine translation |
| Neural Machine Translation by Jointly Learning to Align and Translate | Intermediate | <https://arxiv.org/abs/1409.0473> | Introduced Attention |

---

## 💻 Code & Implementations

| Title | Level | Link | Notes |
|---|---|---|---|
| PyTorch Sequence Models Tutorial | Beginner | <https://pytorch.org/tutorials/beginner/nlp/sequence_models_tutorial.html> | Official RNN/LSTM tutorial |
| Dive into Deep Learning Notebooks | Beginner | <https://github.com/d2l-ai/d2l-en> | Hands-on notebooks |
| char-rnn (Karpathy) | Intermediate | <https://github.com/karpathy/char-rnn> | Classic character-level text generation |
| Seq2Seq Translation Tutorial (PyTorch) | Intermediate | <https://pytorch.org/tutorials/intermediate/seq2seq_translation_tutorial.html> | Attention-based translation model |

---

## 📰 Articles & Blogs

| Title | Level | Link | Notes |
|---|---|---|---|
| The Unreasonable Effectiveness of Recurrent Neural Networks | Intermediate | <https://karpathy.github.io/2015/05/21/rnn-effectiveness/> | Classic RNN blog |
| Understanding LSTM Networks | Beginner | <https://colah.github.io/posts/2015-08-Understanding-LSTMs/> | Must-read article for LSTMs |
| Lil'Log — Attention and Sequence Models | Intermediate | <https://lilianweng.github.io> | High-quality deep learning explanations |
| Distill | Intermediate | <https://distill.pub> | Interactive visual explanations of sequence models |

---

# Key Concepts Checklist

## Foundations

- [ ] Sequential data
- [ ] Time steps
- [ ] Hidden state
- [ ] Recurrent connections

---

## Simple RNN

- [ ] Forward propagation
- [ ] Hidden state update
- [ ] Parameter sharing
- [ ] Sequence prediction

---

## Backpropagation Through Time (BPTT)

- [ ] Computational graph over time
- [ ] Gradient accumulation
- [ ] Truncated BPTT

---

## Training Challenges

- [ ] Vanishing gradients
- [ ] Exploding gradients
- [ ] Gradient clipping

---

## LSTM

- [ ] Cell state
- [ ] Forget gate
- [ ] Input gate
- [ ] Output gate
- [ ] Memory mechanism

---

## GRU

- [ ] Update gate
- [ ] Reset gate
- [ ] Differences from LSTM
- [ ] Computational efficiency

---

## Advanced Architectures

- [ ] Bidirectional RNN
- [ ] Stacked RNN
- [ ] Encoder–Decoder
- [ ] Seq2Seq

---

## Attention

- [ ] Bahdanau Attention
- [ ] Luong Attention
- [ ] Context Vector
- [ ] Alignment Scores

---

## Applications

- [ ] Language Modeling
- [ ] Machine Translation
- [ ] Sentiment Analysis
- [ ] Speech Recognition
- [ ] Time Series Forecasting
- [ ] Text Generation

---

## Transition to Transformers

- [ ] Why RNNs struggle with long sequences
- [ ] Parallelization limitations
- [ ] Attention replaces recurrence
- [ ] Birth of Transformers

---

# Practice Projects

| Project | Skills |
|----------|--------|
| Character-Level Text Generator | Vanilla RNN, text generation |
| Shakespeare Text Generator | LSTM, sequence prediction |
| IMDb Sentiment Classifier | Bidirectional LSTM |
| Time Series Forecasting | LSTM regression |
| English → French Translator | Seq2Seq + Attention |
| Next Word Prediction | Language modeling |
| Speech Command Classification | GRU sequence classification |
| Compare RNN vs LSTM vs GRU | Performance benchmarking |

---

# Suggested Learning Order

```text
Sequential Data
      ↓
Simple RNN
      ↓
Hidden State
      ↓
Backpropagation Through Time
      ↓
Vanishing Gradient Problem
      ↓
LSTM
      ↓
GRU
      ↓
Bidirectional Networks
      ↓
Encoder–Decoder
      ↓
Attention
      ↓
Transformers
      ↓
Large Language Models
```

---

# See also

- [Neural Network Fundamentals](neural-network-fundamentals.md) — Backpropagation and optimization basics
- [Transformers](transformers.md) — Evolution from recurrence to attention
- [Frameworks](frameworks.md) — Implement RNNs, LSTMs, and GRUs using PyTorch and TensorFlow
- [NLP](../05-generative-ai/README.md) — Applications of sequence models
- [Visualizers & Playgrounds](../visualizers-and-playgrounds/README.md) — Interactive tools for understanding sequence models