# SQL & Databases

> Querying, joining, and managing data in relational databases and data warehouses. Essential for accessing production data and working with large-scale datasets.

**Last Reviewed:** 2026-06

**Prerequisites:** [01 – Foundations / README](../01-foundations/README.md) (basic programming)

---

## Resources

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| *Learning SQL* (Beaulieu) — O'Reilly | Beginner | [Link](https://example.com/learning-sql) | Gentle, example-driven introduction |
| PostgreSQL Official Documentation | Intermediate | [Link](https://example.com/postgres-docs) | Comprehensive reference for one of the most popular RDBMS |
| *SQL Performance Explained* (Winand) | Advanced | [Link](https://example.com/sql-performance) | Indexing and query optimization |

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| SQL Tutorial for Beginners — Mosh Hamedani | Beginner | [Link](https://example.com/mosh-sql) | 3-hour crash course covering SELECT, JOIN, GROUP BY |
| Advanced SQL — Window Functions & CTEs | Intermediate | [Link](https://example.com/advanced-sql) | Practical examples of ROW_NUMBER, LAG, recursive CTEs |
| Data Engineering — Warehousing & ETL | Intermediate | [Link](https://example.com/data-eng-vid) | Overview of BigQuery, Snowflake, and modern data stacks |

### 🎓 Course

| Title | Level | Link | Notes |
|---|---|---|---|
| DataCamp — Introduction to SQL | Beginner | [Link](https://example.com/datacamp-sql) | Interactive SQL exercises in browser |
| Coursera — SQL for Data Science (UC Davis) | Beginner | [Link](https://example.com/coursera-sql) | Real-world data scenarios |
| Mode Analytics — SQL School | Beginner | [Link](https://example.com/mode-sql) | Free, narrative tutorials with a built-in query editor |

### 🕹️ Visualizer / Playground

| Title | Level | Link | Notes |
|---|---|---|---|
| SQL Fiddle | Beginner | [Link](https://example.com/sql-fiddle) | Test SQL queries online without installing anything |
| DB Fiddle | Beginner | [Link](https://example.com/db-fiddle) | Supports PostgreSQL, MySQL, SQLite |
| SQL Query Visualizer (explain.depesz.com) | Intermediate | [Link](https://example.com/depesz) | Visualizes query plans for optimization learning |

### 💻 Code / Notebook

| Title | Level | Link | Notes |
|---|---|---|---|
| SQL Murder Mystery (Knight Lab) | Beginner | [Link](https://example.com/sql-mystery) | Solve a crime using SQL queries |
| SQL for Data Analysis (Jupyter + SQLite) | Beginner | [Link](https://example.com/jupyter-sql) | Running SQL directly in notebooks with `%%sql` magic |
| Python + PostgreSQL Connection Examples | Intermediate | [Link](https://example.com/python-postgres) | psycopg2, SQLAlchemy, and async patterns |
| BigQuery Public Datasets Explorations | Intermediate | [Link](https://example.com/bigquery-public) | Querying terabytes of public data with standard SQL |

### 📰 Blog

| Title | Level | Link | Notes |
|---|---|---|---|
| *SQL Window Functions Explained Simply* | Beginner | [Link](https://example.com/window-functions) | Illustrated guide to OVER, PARTITION BY, ORDER BY |
| *Indexing Strategies for Data Scientists* | Intermediate | [Link](https://example.com/indexing-strategies) | When and how to create indexes for analytical queries |
| *Data Warehousing vs Data Lakes vs Lakehouses* | Beginner | [Link](https://example.com/warehouse-vs-lake) | Modern data architecture overview |

---

## Key Concepts Checklist

- [ ] SELECT, FROM, WHERE, ORDER BY, LIMIT
- [ ] JOIN operations (INNER, LEFT, RIGHT, FULL OUTER, CROSS)
- [ ] Aggregation and GROUP BY with HAVING
- [ ] Subqueries (correlated and uncorrelated)
- [ ] Common Table Expressions (WITH clause, recursive CTEs)
- [ ] Window functions (ROW_NUMBER, RANK, LAG, LEAD, SUM OVER)
- [ ] String functions, date functions, and type casting
- [ ] Set operations (UNION, INTERSECT, EXCEPT)
- [ ] Indexes and query performance basics
- [ ] Connecting Python to SQL databases (SQLAlchemy, psycopg2, duckdb)
- [ ] Database design: normalization, primary/foreign keys
- [ ] BigQuery, Snowflake, Redshift: cloud data warehouse concepts

---

## Projects / Practice

| Project | Description |
|---|---|
| Build a Chinook Database Query Set | Write queries to answer business questions on a sample music store DB |
| Migrate CSV Data into SQLite | Import a messy CSV, write SQL to clean and aggregate it |
| Performance Optimization Lab | Take a slow query, add indexes, rewrite joins, and measure improvements |

---

## See also

- [Data Wrangling](data-wrangling.md) — combines SQL results with pandas for further cleaning
- [EDA & Visualization](eda-and-visualization.md) — visualizing query results
- [Case Studies](case-studies.md) — end-to-end examples using SQL + Python
