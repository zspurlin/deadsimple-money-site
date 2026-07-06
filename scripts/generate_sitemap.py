#!/usr/bin/env python3
"""Generate sitemap.xml from cards/index.json.

The sitemap contains the static public routes plus one URL per published
card. cards/index.json is the source of truth for what is public: only
cards published from the research repo appear in it, so drafts and
unpublished work are excluded by construction.
"""

import json
from pathlib import Path

BASE_URL = "https://deadsimple.money"
STATIC_ROUTES = [
    f"{BASE_URL}/",
    f"{BASE_URL}/about.html",
]

REPO_ROOT = Path(__file__).resolve().parent.parent


def card_urls() -> list[str]:
    index = json.loads((REPO_ROOT / "cards" / "index.json").read_text(encoding="utf-8"))
    urls = set()
    for section in ("open", "closed", "watchlist"):
        for card in index.get(section, []):
            card_html = card.get("card_html")
            if card_html:
                urls.add(f"{BASE_URL}/cards/{card_html}")
    return sorted(urls)


def main() -> None:
    urls = STATIC_ROUTES + card_urls()
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    lines += [f"  <url><loc>{url}</loc></url>" for url in urls]
    lines.append("</urlset>")
    (REPO_ROOT / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote sitemap.xml with {len(urls)} URLs")


if __name__ == "__main__":
    main()
