"""Format an approved Quick Add issue into a table row and open a PR.

Usage (standalone):
    python scripts/quick_add_to_table.py <issue-number>

Usage (via GitHub Actions):
    Called by .github/workflows/quick-add-approved.yml when an issue
    gets the 'approved' label. The workflow sets GITHUB_TOKEN and
    ISSUE_NUMBER environment variables.

Requires:
    - GITHUB_TOKEN env var (for GitHub API access)
"""

import os
import re
import sys
import urllib.request
import json
from datetime import datetime
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


def parse_issue_body(body: str) -> dict:
    """Parse the structured YAML form fields from a GitHub issue body."""
    result = {"link": "", "reason": "", "topic": "", "subtopic": ""}

    # GitHub YAML forms render as:
    # ### Field Label
    #
    # Value
    sections = re.split(r"^### ", body, flags=re.MULTILINE)

    for section in sections:
        lines = section.strip().split("\n")
        if not lines:
            continue
        header = lines[0].strip().lower()
        # Get the value (skip blank lines after header)
        value_lines = [l.strip() for l in lines[1:] if l.strip()]
        value = value_lines[0] if value_lines else ""

        if "resource link" in header:
            result["link"] = value
        elif "why" in header or "worth including" in header:
            result["reason"] = value
        elif "which topic" in header:
            result["topic"] = value
        elif "specific file" in header:
            if value.lower() not in ("", "_no response_"):
                result["subtopic"] = value

    return result


def generate_row(link: str, reason: str) -> tuple[str, str]:
    """Generate a canonical table row from a link and reason, and return its inferred category."""
    # Extract a readable title from the URL
    title = link.rstrip("/").split("/")[-1].replace("-", " ").replace("_", " ").title()
    resource_type = infer_resource_type(title, link)
    level = guess_level(reason, title)
    
    # New format: | Title | Level | Link | Notes |
    row = f"| *{title}* | {level} | {link} | {reason} |"
    return row, resource_type


def fetch_issue(issue_number: str, repo: str, token: str) -> dict:
    """Fetch issue data from the GitHub API."""
    url = f"https://api.github.com/repos/{repo}/issues/{issue_number}"
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github.v3+json",
        },
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


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

    # Fetch and parse issue
    issue = fetch_issue(issue_number, repo, token)
    body = issue.get("body", "")
    parsed = parse_issue_body(body)

    link = parsed["link"]
    reason = parsed["reason"]
    topic = parsed["topic"]
    subtopic = parsed["subtopic"]

    if not link:
        print("ERROR: Could not extract resource link from issue body.")
        sys.exit(1)

    # Generate the table row
    row, resource_category = generate_row(link, reason)

    # Determine target file
    file_path = f"{topic}/{subtopic}" if subtopic else f"{topic}/README.md"

    # Output for the workflow to use
    output = {
        "row": row,
        "file": file_path,
        "link": link,
        "reason": reason,
        "topic": topic,
        "category": resource_category,
    }

    print(json.dumps(output, indent=2))

    # Write outputs to GITHUB_OUTPUT if running in Actions
    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a") as f:
            f.write(f"row={row}\n")
            f.write(f"file={file_path}\n")
            f.write(f"link={link}\n")
            f.write(f"topic={topic}\n")
            f.write(f"category={resource_category}\n")


if __name__ == "__main__":
    main()
