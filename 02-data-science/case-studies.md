# Case Studies

> End-to-end examples of data science applied to real-world problems. Each case ties together wrangling, EDA, statistics, and communication.

**Last Reviewed:** 2026-06

**Prerequisites:** [Data Wrangling](data-wrangling.md) · [EDA & Visualization](eda-and-visualization.md) · [Statistics & Inference](statistics-and-inference.md) · [SQL & Databases](sql-and-databases.md)

---

> 💡 **Tip:** After studying each case, try to reproduce the analysis yourself using the linked dataset. The learning comes from doing.

---

## Resources

### 📘 Case Collection Docs

| Title | Level | Link | Notes |
|---|---|---|---|
| *Data Science from Scratch* (Joel Grus) — Case Chapters | Beginner | [Link](https://example.com/ds-from-scratch) | Implement every algorithm from scratch on small datasets |
| Kaggle — Getting Started Competitions | Beginner | [Link](https://example.com/kaggle-getting-started) | Titanic, Housing Prices, Spaceship Titanic |
| *Feature Engineering for Machine Learning* (Alice Zheng) | Intermediate | [Link](https://example.com/feature-engineering-book) | Case-driven feature creation techniques |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| Data Science Project from Scratch — Ken Jee | Beginner | [Link](https://example.com/ken-jee-project) | Full walkthrough: scraped data to deployed model |
| A/B Testing Case: E-Commerce Experiment | Intermediate | [Link](https://example.com/ab-testing-case) | Real experiment design and analysis walkthrough |
| Building a Recommendation Engine — MovieLens | Intermediate | [Link](https://example.com/movielens-case) | Collaborative filtering on 25M ratings |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| Coursera — Data Science Capstone (Johns Hopkins) | Intermediate | [Link](https://example.com/jhu-capstone) | Peer-reviewed capstone with real data |
| fast.ai — Practical Deep Learning (lesson case studies) | Intermediate | [Link](https://example.com/fastai-cases) | Production-oriented ML case studies |
| Udacity — Data Scientist Nanodegree Projects | Intermediate | [Link](https://example.com/udacity-ds) | 5 real-world portfolio projects |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| TMDB Box Office Prediction (Kaggle) | Beginner | [Link](https://example.com/tmdb-case) | EDA + feature engineering on 7K movies |
| Customer Churn Analysis — Telco Dataset | Intermediate | [Link](https://example.com/churn-case) | Classification with shap explanations |
| Uber Pickups Analysis (NYC) | Intermediate | [Link](https://example.com/uber-case) | Geospatial EDA + time series patterns |
| Credit Card Fraud Detection | Intermediate | [Link](https://example.com/fraud-case) | Imbalanced classification, precision-recall tradeoffs |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *How Booking.com Runs 1000 A/B Tests a Week* | Intermediate | [Link](https://example.com/booking-ab) | Infrastructure and culture of experimentation |
| *Netflix Prize: What Actually Worked?* | Intermediate | [Link](https://example.com/netflix-prize) | Retrospective on the famous 2006–2009 competition |
| *A Data Science Post-Mortem: Predicting FIFA World Cup 2022* | Beginner | [Link](https://example.com/fifa-postmortem) | Honest reflection on what went wrong in a prediction project |

---

## Case Study Walkthroughs

### Titanic Survival Prediction

| Step | Technique | Est. Time |
|---|---|---|
| Load & inspect data | pandas `info()`, `describe()`, `head()` | 5 min |
| Handle missing values | Impute Age, drop Cabin, encode Sex & Embarked | 15 min |
| Feature engineering | FamilySize, Title extraction from Name | 10 min |
| EDA | Survival rates by Sex, Class, Age group (seaborn) | 15 min |
| Model baseline | LogisticRegression, cross-validation | 10 min |
| Interpret | SHAP summary plot, permutation importance | 10 min |

### Marketing Campaign ROI Analysis

| Step | Technique | Est. Time |
|---|---|---|
| SQL query to aggregate campaign data | CTEs, window functions, cohort joins | 20 min |
| Click-through rate analysis | Binomial proportion confidence intervals | 15 min |
| A/B test across creative variants | Chi-squared test, effect size | 15 min |
| Segmentation analysis | RFM scoring, k-means clustering | 20 min |
| Dashboard | Plotly Dash or Streamlit summary | 30 min |

---

## Projects / Practice

| Project | Description |
|---|---|
| Full EDA + Prediction on a Kaggle Tabular Dataset | Choose a dataset, produce a clean notebook with visuals and a tuned model |
| Replicate a Published Data Journalism Article | Find a FiveThirtyEight or NYT Upshot piece and reproduce the analysis |
| End-to-End Data Pipeline | SQL → Python wrangling → EDA → statistical test → dashboard |

---

## See also

- [All 02 – Data Science pages](README.md) — every technique in this module feeds into these case studies
- [03 – Machine Learning](../03-machine-learning/README.md) — the next step after exploratory analysis
- [08 – Projects & Examples](../08-projects-and-examples/README.md) — more project ideas
