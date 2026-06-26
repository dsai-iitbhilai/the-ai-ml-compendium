"""Find resources whose Last Reviewed date is older than N months.

Usage:
    python scripts/find_stale_resources.py --months 12 [--format markdown|json]

Note: Only resources using the canonical 5-column table format with a
Last Reviewed date (YYYY-MM) will be checked. Legacy 4-column entries
without dates are silently skipped.
"""

import argparse
import json
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Canonical 5-column format: | [Title](url) | Type | Level | YYYY-MM | Notes |
CANONICAL_RE = re.compile(
    r"^\|\s*\[(.+?)\]\((.+?)\)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(\d{4}-\d{2})\s*\|\s*(.*?)\s*\|$",
    re.MULTILINE,
)


def parse_date(date_str: str) -> datetime:
    return datetime.strptime(date_str, "%Y-%m")


def find_stale(months: int) -> list[dict]:
    cutoff = datetime.utcnow() - timedelta(days=months * 30)
    stale = []

    for md_file in sorted(REPO_ROOT.rglob("*.md")):
        if ".github" in md_file.parts:
            continue
        text = md_file.read_text(encoding="utf-8")
        for match in CANONICAL_RE.finditer(text):
            reviewed = parse_date(match.group(5))
            if reviewed < cutoff:
                stale.append(
                    {
                        "title": match.group(1).strip(),
                        "url": match.group(2).strip(),
                        "type": match.group(3).strip(),
                        "level": match.group(4).strip(),
                        "last_reviewed": match.group(5).strip(),
                        "notes": match.group(6).strip(),
                        "file": str(md_file.relative_to(REPO_ROOT)),
                    }
                )

    return stale


def output_markdown(stale: list[dict]) -> None:
    if not stale:
        return
    print(f"# Stale Resource Report ({len(stale)} resources)\n")
    print("Resources with `Last Reviewed` dates older than 12 months:\n")
    for r in stale:
        print(f"- [{r['title']}]({r['url']}) — `{r['file']}` — last reviewed {r['last_reviewed']}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--months", type=int, default=12)
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    args = parser.parse_args()

    stale = find_stale(args.months)

    if args.format == "json":
        print(json.dumps(stale, indent=2))
    else:
        output_markdown(stale)

    sys.exit(0 if not stale else 1)


if __name__ == "__main__":
    main()
