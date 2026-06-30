# How to Read Research Papers

> Strategies, templates, and tools for effectively reading and understanding ML research papers.

**Last Reviewed:** 2026-06

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| *Papers with Code — Reading Guide* | Beginner | https://paperswithcode.com/about | Connecting mathematical equations in papers to their open-source code implementations. |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| *How to Read a Machine Learning Paper* (Yannic Kilcher) | Beginner | https://www.youtube.com/watch?v=733m6qBH-jI | Practical, step-by-step advice on skimming abstracts and deconstructing results tables. |
| *How to Read Research Papers* (Andrew Ng) | Beginner | https://www.youtube.com/watch?v=733m6qBH-jI | Andrew Ng's personal methodology for compiling and understanding research. |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| *Stanford CS230 — Deep Learning: Reading Papers* | Beginner | https://cs230.stanford.edu/files/CS230_Reading_Papers.pdf | Structured, academic approach from the Stanford DL course on dissecting literature. |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| *Zotero + Obsidian Paper Workflow* | Intermediate | https://github.com/alexandresanlim/Badges4-README.md-Profile | Tool setup templates for managing massive libraries of paper notes via Markdown linking. |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *How to Read a Paper* (S. Keshav) | Beginner | https://blizzard.cs.uwaterloo.ca/keshav/home/Papers/data/07/paper-reading.pdf | The definitive, classic three-pass approach to reading academic literature. |
| *How to Read a Paper in ML* (Yale CS) | Beginner | https://cpsc486.github.io/ | Template outlining the exact questions you should ask while reading each section. |

---

## The Three-Pass Method (Keshav)

| Pass | Time | Goal |
|---|---|---|
| **1st Pass** | ~5-10 min | Get a high-level understanding. Read the title, abstract, Introduction, section headings, and Conclusion. Ignore the math. |
| **2nd Pass** | ~1 hr | Understand the method and key results. Read the core architecture sections, examine the Figures/Tables, and understand the objective function. (Ignore proofs and appendices). |
| **3rd Pass** | ~3-4 hrs | Deep understanding. Attempt to virtually re-implement the paper. Identify hidden assumptions, critique the dataset, and understand every mathematical derivation. |

---

## Note-Taking Template

When completing the 2nd pass, answer these questions in your notes (Obsidian/Notion):

```markdown
## Title + Year + Venue (e.g., NeurIPS)
**Problem:** What specific bottleneck or mathematical limitation are they trying to solve?
**Method:** What is the core architectural change or novel algorithm?
**Results:** What metrics improved? By how much? Against what baseline?
**Strengths:** Why is this a good idea?
**Limitations:** What are the computational costs? Did they test it on noisy real-world data?
**Follow-up Questions:** What didn't I understand that I need to Google?
**Related Papers to Read:** Which paper from the citations seems like a necessary prerequisite?
```

---

## Tools for Paper Management

| Tool | Purpose |
|---|---|
| **Zotero** | Open-source reference manager. Excellent browser extension for saving PDFs directly from arXiv. |
| **Mendeley** | Reference manager backed by Elsevier, featuring strong social sharing features for research groups. |
| **Paperpile** | Highly ergonomic, Google Docs/Chrome integrated reference manager. |
| **Notion / Obsidian** | Note-taking tools. Obsidian is preferred for research due to its local, bidirectional linking (Zettelkasten method). |
| **TLDR This / Elicit.org** | AI-powered research assistants that summarize papers and find related literature based on semantic search. |

---

## Staying Current

- Subscribe to **arXiv RSS feeds** for specific categories: `cs.LG` (Machine Learning), `cs.CL` (Computation and Language), `cs.CV` (Computer Vision).
- Follow the **Papers with Code** weekly newsletter for trending repositories.
- Use **Twitter/X** to follow the primary authors of papers you like; ML Twitter is highly active for pre-print announcements.
- Join an online **journal club** (e.g., through Discord communities) to force yourself to read and discuss one paper a week.