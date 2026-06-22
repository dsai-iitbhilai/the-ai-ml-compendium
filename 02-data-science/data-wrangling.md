# Data Wrangling

> Transforming raw, messy data into a clean, analysis-ready format. Covers pandas, NumPy, and general cleaning techniques.

**Last Reviewed:** 2026-06

**Prerequisites:** [Python for AI](../01-foundations/programming/python-for-ai.md)

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| *Python Data Science Handbook* — Chapter 3 (Data Manipulation) | Beginner | [Link](https://example.com/pydata-handbook-ch3) | Pandas deep-dive with real examples |
| pandas Official API Reference | Intermediate | [Link](https://example.com/pandas-docs) | Always-up-to-date reference |
| *Data Wrangling with Python* — Jacquart | Beginner | [Link](https://example.com/wrangling-jacquart) | Step-by-step practical guide |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| Data Wrangling with pandas — Corey Schafer | Beginner | [Link](https://example.com/corey-pandas) | Clear, paced walkthrough of pandas basics |
| Pandas in 10 Minutes (YouTube) | Beginner | [Link](https://example.com/pandas-10min-vid) | Quick-start for absolute beginners |
| Advanced pandas: GroupBy & Reshaping — Data School | Intermediate | [Link](https://example.com/dataschool-groupby) | Covers pivot tables, melt, and stack/unstack |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| DataCamp — Data Manipulation with pandas | Beginner | [Link](https://example.com/datacamp-pandas) | In-browser exercises with immediate feedback |
| Coursera — Data Wrangling, Analysis & AB Testing (U. Colorado) | Intermediate | [Link](https://example.com/coursera-wrangling) | Project-based: real datasets |
| Kaggle — Data Cleaning Micro-Course | Beginner | [Link](https://example.com/kaggle-clean) | Free, 1-hour interactive notebook |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| pandas Playground (GitHub Codespaces) | Beginner | [Link](https://example.com/pandas-playground) | Pre-loaded Jupyter environment |
| NumPy Broadcasting Visualizer | Intermediate | [Link](https://example.com/broadcast-viz) | Interactive tool to understand array shapes |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| pandas Cheat Sheet (Official) | Beginner | [Link](https://example.com/pandas-cheatsheet) | One-page reference for common operations |
| NumPy Quickstart Tutorial | Beginner | [Link](https://example.com/numpy-quickstart) | Official NumPy tutorial |
| Data Cleaning Notebook — Titanic | Beginner | [Link](https://example.com/titanic-clean) | End-to-end cleaning on a classic dataset |
| Feature Engineering Notebook — Housing Prices | Intermediate | [Link](https://example.com/housing-features) | Missing value imputation, encoding, scaling |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *A Visual Intro to NumPy* (Jay Alammar) | Beginner | [Link](https://example.com/jay-numpy) | Illustrated guide to arrays and broadcasting |
| *Pandas Pipeline: Writing Clean Data Code* | Intermediate | [Link](https://example.com/pandas-pipeline) | Chaining operations with `.pipe()` |
| *12 Common Data Cleaning Mistakes* | Beginner | [Link](https://example.com/cleaning-mistakes) | Practical pitfalls and how to avoid them |

---

## Key Concepts Checklist

- [ ] DataFrame and Series basics (indexing, slicing, filtering)
- [ ] Handling missing data (`isna`, `dropna`, `fillna`, interpolation)
- [ ] Merging, joining, and concatenating DataFrames
- [ ] GroupBy operations (split-apply-combine)
- [ ] Reshaping data (pivot, melt, stack, unstack)
- [ ] Applying functions (apply, map, applymap, vectorized ops)
- [ ] NumPy broadcasting and universal functions
- [ ] String operations with `.str` accessor
- [ ] Working with datetime data
- [ ] Reading/writing CSV, Excel, JSON, Parquet
- [ ] Handling duplicates, outliers, and inconsistent formatting

---

## Projects / Practice

| Project | Description |
|---|---|
| Clean the UCI Adult Income Dataset | Handle missing values, encode categoricals, normalize numeric columns |
| Combine Multiple CSV Files | Merge 12 months of sales data into a single clean DataFrame |
| Build a Data Cleaning Pipeline | Write reusable functions for common cleaning tasks on new datasets |

---

## See also

- [EDA & Visualization](eda-and-visualization.md) — what to do after the data is clean
- [SQL & Databases](sql-and-databases.md) — acquiring data from relational sources
- [01 – Foundations / Python for AI](../01-foundations/programming/python-for-ai.md)
