#!/usr/bin/env python3
"""Mirror https://tunit.dev/docs as Markdown, strip Docusaurus heading anchors, rebuild CLAUDE.md.

Run from anywhere: python3 scripts/refresh_docs.py
"""
import collections
import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

SITE = "https://tunit.dev"
ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

LINK = re.compile(r"- \[(.+?)\]\((/[^)]+\.md)\)(?::\s*(.*))?$")
# Docusaurus heading anchor: [<zero-width space>](#id "Direct link to Title"). Titles may contain ")".
ANCHOR = re.compile(r'\[​\]\(#[^\s)]*\s+"Direct link to (?:[^"\\]|\\.)*"\)')


def fetch(url: str) -> str:
    with urllib.request.urlopen(url, timeout=60) as response:
        return response.read().decode("utf-8")


def parse_index(llms: str) -> list[tuple[str, str, str]]:
    rows = []
    for line in llms.splitlines():
        match = LINK.match(line.strip())
        if not match or match.group(2) == "/search.md":
            continue
        title, path, summary = match.group(1), match.group(2).lstrip("/"), (match.group(3) or "").strip()
        rows.append((path, title, summary))
    return rows


def download(path: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(ANCHOR.sub("", fetch(f"{SITE}/{path}")), encoding="utf-8")


def first_sentence(summary: str) -> str:
    sentence = re.split(r"(?<=[.!?])\s", summary, maxsplit=1)[0].rstrip(":")
    return sentence if len(sentence) <= 160 else sentence[:157].rstrip() + "…"


def write_claude_md(rows: list[tuple[str, str, str]], version: str) -> None:
    groups: dict[str, list] = collections.OrderedDict()
    for path, title, summary in sorted(rows, key=lambda r: (r[0].count("/") > 1, r[0])):
        parts = path.split("/")
        groups.setdefault("/".join(parts[:2]) if len(parts) > 2 else "docs", []).append((path, title, summary))

    lines = [
        "# TUnit docs — local Markdown copy",
        "",
        "Every page of https://tunit.dev/docs as Markdown, one file per page, same tree as the site.",
        f"Mirrored from `https://tunit.dev/llms.txt`; latest TUnit release at refresh time: `{version}` (see `VERSION`).",
        "",
        "## How to use this folder",
        "",
        "- Find the topic below, open **one** file, read it. Don't load the whole folder.",
        "- Paths are relative to this folder. `grep -ril <term> docs/` when the index doesn't name it.",
        "- Docs are not proof: the showcase repo (`../TUnit-*/CHANGELOG.md`, *Divergences from docs*) lists places where the real behaviour differs.",
        "- `WHATSNEW.md` (when present) is the delta between the previous and the current `VERSION`.",
        "",
        "## Refresh",
        "",
        "- `python3 scripts/refresh_docs.py` — re-download every page, strip heading anchors, rebuild this file.",
        "- `scripts/whats-new.sh <old-tag> <new-tag>` — release notes, public API diff and `src/` changes between two TUnit tags.",
        "- `.github/workflows/weekly-tunit.yml` runs both every Monday and opens a PR with the result.",
        "",
        "This file is generated — edit `scripts/refresh_docs.py`, not this file.",
        "",
        "## Index",
        "",
    ]
    for group, items in groups.items():
        lines += [f"### `{group}/`", ""]
        for path, title, summary in items:
            lines.append(f"- `{path}` — **{title}**" + (f": {first_sentence(summary)}" if summary else ""))
        lines.append("")
    (ROOT / "CLAUDE.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    llms = fetch(f"{SITE}/llms.txt")
    (ROOT / "llms.txt").write_text(llms, encoding="utf-8")
    rows = parse_index(llms)

    with ThreadPoolExecutor(max_workers=8) as pool:
        list(pool.map(download, [path for path, _, _ in rows]))

    listed = {ROOT / path for path, _, _ in rows}
    for stale in DOCS.rglob("*.md"):
        if stale not in listed:
            stale.unlink()

    version_file = ROOT / "VERSION"
    version = version_file.read_text().strip() if version_file.exists() else "unknown"
    write_claude_md(rows, version)
    print(f"{len(rows)} pages")


if __name__ == "__main__":
    main()
