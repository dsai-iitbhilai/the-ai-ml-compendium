# 02 — Data Science

> The art and science of extracting insights from data: wrangling, exploration, statistical inference, and communicating results. This module bridges raw programming skills (01 – Foundations) with downstream machine learning (03 – ML).

**Last Reviewed:** 2026-06

**Prerequisites:** [01 – Foundations](../01-foundations/README.md)

---

## Overview

Data science is the practice of turning messy, real-world data into actionable knowledge. This module covers the entire pipeline: acquiring and cleaning data, exploratory analysis, visualization, statistical inference, and working with databases.

| Sub‑page | Est. Hours | Priority |
|---|---|---|
| [Data Wrangling](data-wrangling.md) | 10–15 | Essential |
| [EDA & Visualization](eda-and-visualization.md) | 8–12 | Essential |
| [Statistics & Inference](statistics-and-inference.md) | 12–18 | Essential |
| [SQL & Databases](sql-and-databases.md) | 6–10 | Important |
| [Case Studies](case-studies.md) | 4–6 | Helpful |

---

## Prerequisite Map

```
┌─────────────────────────────────────────────┐
│               01 - Foundations              │
│     (Python, NumPy, pandas, math basics)    │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│              02 - Data Science              │
│                                             │
│  Data Wrangling ──► EDA & Visualization     │
│       │                      │              │
│       ▼                      ▼              │
│  Statistics & Inference  SQL & Databases    │
│       │                      │              │
│       └──────┬───────────────┘              │
│              ▼                              │
│         Case Studies                        │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│            03 - Machine Learning            │
└─────────────────────────────────────────────┘
```

---

## How to Use

1. Start with **Data Wrangling** — you cannot analyze what you cannot clean.
2. Move to **EDA & Visualization** to build intuition about your data.
3. Study **Statistics & Inference** to formalize your findings.
4. Learn **SQL & Databases** for real-world data access patterns.
5. Cap the module with **Case Studies** to see everything in action.

---

## Reference Textbooks

| Title | Author(s) | Used In |
|---|---|---|
| *Python Data Science Handbook* | VanderPlas | Data Wrangling, EDA |
| *Naked Statistics* | Wheelan | Statistics & Inference |
| *R for Data Science* (concepts apply to Python) | Wickham & Grolemund | Data Wrangling, EDA |
| *Learning SQL* | Beaulieu | SQL & Databases |
| *Storytelling with Data* | Knaflic | EDA & Visualization |

---

## See also

- [ Visualizers & Playgrounds](../visualizers-and-playgrounds/README.md) — interactive tools for distributions, sampling, and plotting
- [03 – Machine Learning](../03-machine-learning/README.md) — next module
- [Templates / Resource Entry Template](../templates/resource-entry-template.md)
