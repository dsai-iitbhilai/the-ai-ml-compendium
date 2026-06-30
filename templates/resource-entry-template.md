# Resource Entry Template

Use this format when adding resources to any topic `.md` file.

## Standard Table Format

```markdown
## Topic Name
*Prerequisites: [Prerequisite Topic](../01-foundations/mathematics/calculus.md)*

| Resource | Type | Level | Last Reviewed | Notes |
|---|---|---|---|---|
| [Title](https://www.youtube.com/) | Type | Level | YYYY-MM | Brief note on why this resource |
```

## Type Taxonomy

| Type | Tag |
|---|---|
| Documentation | ` Docs` |
| Video | ` Video` |
| Course | ` Course` |
| Visualizer / Playground | ` Visualizer/Playground` |
| Research Paper | ` Paper` |
| Code / Notebook | ` Code/Notebook` |
| Blog Post | ` Blog` |

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

## Example

```markdown
## Linear Regression
*Prerequisites: [Calculus](../01-foundations/mathematics/calculus.md), [Probability & Statistics](../01-foundations/mathematics/probability-statistics.md)*

| Resource | Type | Level | Last Reviewed | Notes |
|---|---|---|---|---|
| [StatQuest: Linear Regression](https://youtube.com/) |  Video | Beginner | 2026-06 | Best first intuition-builder |
| [Scikit-learn Docs: Linear Models](https://scikit-learn.org/) |  Docs | Beginner | 2026-06 | Reference implementation |
| [Andrew Ng — ML Specialization](https://coursera.org/) |  Course | Beginner | 2026-06 | Full module on regression |

**See also:** [Logistic Regression](../01-foundations/mathematics/calculus.md) for the classification analogue
```
