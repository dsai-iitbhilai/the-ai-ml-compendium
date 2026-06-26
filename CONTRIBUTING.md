# Contributing to AI/ML Compendium

Thanks for helping make this resource better! There are three paths to contribute:

## Path A: Quick Add Resource (No Git Required)

Use the [Quick Add](https://github.com/dsai-iitbhilai/the-ai-ml-compendium/issues/new?template=quick-add-resource.yml) issue template. You only need:

1. The resource link
2. A one-line explanation of why it's worth including
3. Which topic folder it belongs to

A maintainer will review, approve, and a PR will be auto-generated. This is the best way to suggest a single link.

## Path B: Remove or Replace a Resource (No Git Required)

Think a resource is outdated, paywalled, or you know a better alternative? Use the [Update Resource](https://github.com/dsai-iitbhilai/the-ai-ml-compendium/issues/new?template=remove-replace-resource.yml) template to suggest removing or replacing it.

## Path C: Full PR (For Structural Changes)

For new topic files, folders, or edits spanning multiple entries:

> **Important:** Edit files in the **root folders** (`01-foundations/`, `02-data-science/`, etc.), NOT in the `docs/` directory. The `docs/` folder uses snippet includes (`--8<--`) to mirror content from root — your changes will be reflected automatically.

### Resource Entry Format

Every resource entry in topic `.md` files uses this table format:

```markdown
| Resource | Type | Level | Last Reviewed | Notes |
|---|---|---|---|---|
| [Title](https://...) | Type | Level | YYYY-MM | Why it's good |
```

**Type taxonomy:** `📘 Docs` · `🎥 Video` · `🎓 Course` · `🕹️ Visualizer/Playground` · `📄 Paper` · `💻 Code/Notebook` · `📰 Blog`

**Level taxonomy:** `Beginner` · `Intermediate` · `Advanced`

See the full template in [templates/resource-entry-template.md](./templates/resource-entry-template.md), and a fully populated example in [01-foundations/mathematics/linear-algebra.md](./01-foundations/mathematics/linear-algebra.md).

### Quality Bar

- No dead links (verify before submitting)
- No paywalled-only resources without a free alternative noted
- Prefer primary sources (official docs, original papers) when possible
- Every topic should include at least one interactive/visual resource where one genuinely exists
- Preserve deliberate ordering: intuition → depth → reference

### PR Checklist

- [ ] Links verified (no dead links)
- [ ] Table format matches the template
- [ ] `Last Reviewed` date is current
- [ ] Deliberate ordering preserved (not alphabetical)
- [ ] `See also` lines used instead of duplicating content

### Proposing a New Topic/Folder

Open a [New Topic issue](https://github.com/dsai-iitbhilai/the-ai-ml-compendium/issues/new?template=new-topic.yml) first to discuss structure before writing content.

## Local Development

```bash
git clone https://github.com/dsai-iitbhilai/the-ai-ml-compendium.git
cd the-ai-ml-compendium
pip install -r requirements.txt
mkdocs serve
```

The site will be available at `http://127.0.0.1:8000` with hot-reload.
