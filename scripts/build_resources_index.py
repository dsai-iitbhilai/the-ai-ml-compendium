"""Scrape all resource tables in the repo and build a resources.json index."""

import json
import re
import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

RESOURCE_RE = re.compile(
    r"^\|\s*\[(.+?)\]\((.+?)\)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(\d{4}-\d{2})\s*\|\s*(.*?)\s*\|$",
    re.MULTILINE,
)


def extract_topic_from_path(filepath: Path) -> str:
    relative = filepath.relative_to(REPO_ROOT)
    parts = relative.parts
    if len(parts) >= 2:
        return f"{parts[0]}/{parts[1]}"
    return parts[0]


def scrape_file(filepath: Path) -> list[dict]:
    text = filepath.read_text(encoding="utf-8")
    resources = []
    for match in RESOURCE_RE.finditer(text):
        resources.append(
            {
                "title": match.group(1).strip(),
                "url": match.group(2).strip(),
                "type": match.group(3).strip(),
                "level": match.group(4).strip(),
                "last_reviewed": match.group(5).strip(),
                "notes": match.group(6).strip(),
                "file": str(filepath.relative_to(REPO_ROOT)),
                "topic": extract_topic_from_path(filepath),
            }
        )
    return resources


def main():
    all_resources = []
    for md_file in sorted(REPO_ROOT.rglob("*.md")):
        if ".github" in md_file.parts:
            continue
        all_resources.extend(scrape_file(md_file))

    output_path = REPO_ROOT / "resources.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(
            {"count": len(all_resources), "resources": all_resources},
            f,
            indent=2,
            ensure_ascii=False,
        )
    print(f"Built resources.json with {len(all_resources)} entries.")


if __name__ == "__main__":
    main()
