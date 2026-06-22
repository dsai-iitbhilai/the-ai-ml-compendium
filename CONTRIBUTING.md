# Contributing to AI/ML Compendium

Thanks for helping make this resource better! There are two paths to contribute:

## Path A: Quick Add (No Git Required)

Use the [Quick Add](https://github.com/dsai-iitbhilai/the-ai-ml-compendium/issues/new?template=quick-add-resource.yml) issue template. You only need:
1. The resource link
2. A one-line explanation of why it's worth including
3. Which topic folder it belongs to

A maintainer will review and format it. This is the best way to suggest a single link.

## Path B: Full PR (For Structural Changes)

For new topic files, folders, or edits spanning multiple entries:

### Resource Entry Format

Every resource entry in topic `.md` files uses this table format:

```markdown
| Resource | Type | Level | Last Reviewed | Notes |
|---|---|---|---|---|
| [Title](https://...) | Type | Level | YYYY-MM | Why it's good |
```

**Type taxonomy:** `📘 Docs` · `🎥 Video` · `🎓 Course` · `🕹️ Visualizer/Playground` · `📄 Paper` · `💻 Code/Notebook` · `📰 Blog`

**Level taxonomy:** `Beginner` · `Intermediate` · `Advanced`

See the full template in [templates/resource-entry-template.md](./templates/resource-entry-template.md).

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
