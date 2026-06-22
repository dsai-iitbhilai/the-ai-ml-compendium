"""Format an approved Quick Add issue into a table row and open a PR.

Usage:
    python scripts/quick_add_to_table.py <issue-number>

Requires:
    - GITHUB_TOKEN env var (for GitHub API access)
"""

import os
import re
import sys
import urllib.request
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

TYPE_MAP = {
    "doc": "📘 Docs",
    "docs": "📘 Docs",
    "documentation": "📘 Docs",
    "video": "🎥 Video",
    "course": "🎓 Course",
    "visualizer": "🕹️ Visualizer/Playground",
    "playground": "🕹️ Visualizer/Playground",
    "paper": "📄 Paper",
    "code": "💻 Code/Notebook",
    "notebook": "💻 Code/Notebook",
    "blog": "📰 Blog",
    "article": "📰 Blog",
}


def infer_resource_type(title: str, link: str) -> str:
    """Heuristic: guess type from URL and title."""
    link_lower = link.lower()
    title_lower = title.lower()

    if any(d in link_lower for d in ["youtube", "youtu.be", "vimeo"]):
        return "🎥 Video"
    if "arxiv" in link_lower and "pdf" in link_lower:
        return "📄 Paper"
    if "arxiv" in link_lower:
        return "📄 Paper"
    if any(p in link_lower for p in ["github.com", "colab", "kaggle", "notebook"]):
        return "💻 Code/Notebook"
    if any(p in link_lower for p in ["playground", "explainer", "visualizer", "demo"]):
        return "🕹️ Visualizer/Playground"
    if any(c in link_lower for c in ["coursera", "udacity", "edx", "fast.ai", "deeplearning.ai"]):
        return "🎓 Course"
    if any(b in link_lower for b in ["blog", "medium", "towardsdatascience"]):
        return "📰 Blog"
    if any(d in link_lower for d in ["docs.", ".readthedocs", "documentation", ".org"]):
        return "📘 Docs"

    if "tutorial" in title_lower:
        return "🎓 Course"
    if "paper" in title_lower or ":" in title:
        return "📄 Paper"

    return "📘 Docs"


def guess_level(notes: str, title: str) -> str:
    combined = (notes + " " + title).lower()
    if any(w in combined for w in ["advanced", "deep dive", "expert"]):
        return "Advanced"
    if any(w in combined for w in ["intermediate"]):
        return "Intermediate"
    return "Beginner"


def generate_row(link: str, reason: str, topic: str, subtopic: str) -> str:
    title = link.rstrip("/").split("/")[-1].replace("-", " ").replace("_", " ").title()
    resource_type = infer_resource_type(title, link)
    level = guess_level(reason, title)

    from datetime import datetime

    today = datetime.utcnow().strftime("%Y-%m")

    row = f"| [{title}]({link}) | {resource_type} | {level} | {today} | {reason} |"
    return row


def build_pr_body(link: str, reason: str, topic: str, subtopic: str) -> str:
    row = generate_row(link, reason, topic, subtopic)
    file_path = f"{topic}/{subtopic}" if subtopic else f"{topic}/README.md"
    return f"""## Quick Add Resource

**Link:** {link}
**Topic:** {topic}
**File:** {file_path}

**Generated row:**
{row}

This PR was auto-generated from an approved Quick Add issue.
"""


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/quick_add_to_table.py <issue-number>")
        sys.exit(1)

    issue_number = sys.argv[1]
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("GITHUB_TOKEN env var required.")
        sys.exit(1)

    repo = os.environ.get("GITHUB_REPOSITORY", "dsai-iitbhilai/the-ai-ml-compendium")
    url = f"https://api.github.com/repos/{repo}/issues/{issue_number}"

    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req) as resp:
        issue = json.loads(resp.read())

    body = issue.get("body", "")
    link = ""
    reason = ""
    topic = ""
    subtopic = ""

    for line in body.split("\n"):
        link_match = re.match(r"### Resource Link\s*\n\s*(https?://\S+)", body)
        reason_match = re.search(r"### Why is this worth including\?\s*\n\s*(.+?)(?:\n|$)", body)
        topic_match = re.search(r"### Which topic does this belong to\?\s*\n\s*(.+)", body)
        subtopic_match = re.search(r"### Specific file \(if known\)\s*\n\s*(.+)", body)

        if link_match:
            link = link_match.group(1)
        if reason_match:
            reason = reason_match.group(1)
        if topic_match:
            topic = topic_match.group(1).strip()
        if subtopic_match and subtopic_match.group(1).strip().lower() not in (
            "",
            "_no response_",
        ):
            subtopic = subtopic_match.group(1).strip()

    pr_body = build_pr_body(link, reason, topic, subtopic)

    print(pr_body)


if __name__ == "__main__":
    main()
