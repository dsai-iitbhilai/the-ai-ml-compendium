# Resource Entry Template

Use this format when adding resources to any topic `.md` file.

## Standard Table Format

We group resources by their category (e.g., Docs, Videos) using `###` headers. The table columns should strictly be: `| Title | Level | Link | Notes |`.

```markdown
## Topic Name
*Prerequisites: [Prerequisite Topic](../01-foundations/mathematics/calculus.md)*

### 🎥 Video

| Title | Level | Link | Notes |
|---|---|---|---|
| *StatQuest: Linear Regression* | Beginner | https://www.youtube.com/ | Best first intuition-builder |

### 📘 Docs & Textbooks

| Title | Level | Link | Notes |
|---|---|---|---|
| *Scikit-learn Docs: Linear Models* | Beginner | https://scikit-learn.org/ | Reference implementation |
```

## Category Taxonomy

When creating new headers, use these standard emojis:
- `📘 Docs & Textbooks`
- `🎥 Video`
- `🎓 Course`
- `🕹️ Visualizer & Playground`
- `📄 Paper`
- `💻 Code & Notebook`
- `📰 Blog`

## Level Taxonomy

- `Beginner`
- `Intermediate`
- `Advanced`

## Ordering Convention

Rows should be ordered by learning sequence, not alphabetically:

1. **Intuition-builders** (visualizers, beginner videos, blog posts)
2. **Depth** (courses, detailed docs, papers)
3. **Reference** (official docs, API references, frameworks)

## See Also

Use `**See also:** [Topic Name](../01-foundations/mathematics/calculus.md)` instead of duplicating tables when a topic belongs in multiple places.
