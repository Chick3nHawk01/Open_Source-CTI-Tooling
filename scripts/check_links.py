#!/usr/bin/env python3
"""Lightweight link checker for cti-bookmarks.html.

Many CTI sites block automated clients (403/429). Treat those as inconclusive,
not definitely dead. Prefer fixing clear 404/DNS failures.
"""
from __future__ import annotations

import concurrent.futures
import re
import ssl
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOKMARKS = ROOT / "cti-bookmarks.html"
UA = {
    "User-Agent": (
        "Mozilla/5.0 (compatible; OpenSourceCTIBookmarks-LinkCheck/1.0; "
        "+https://github.com/Chick3nHawk01/Open_Source-CTI-Tooling)"
    )
}


def urls_from_bookmarks() -> list[str]:
    text = BOOKMARKS.read_text(encoding="utf-8", errors="replace")
    found = re.findall(r'HREF="(https?://[^"]+)"', text, flags=re.I)
    return sorted(set(found))


def check(url: str) -> tuple[str, int | str, str]:
    ctx = ssl.create_default_context()
    try:
        req = urllib.request.Request(url, method="HEAD", headers=UA)
        with urllib.request.urlopen(req, timeout=12, context=ctx) as resp:
            return url, resp.status, "ok"
    except Exception:
        try:
            req = urllib.request.Request(url, method="GET", headers=UA)
            with urllib.request.urlopen(req, timeout=12, context=ctx) as resp:
                return url, resp.status, "ok-get"
        except urllib.error.HTTPError as err:
            return url, err.code, "http-error"
        except Exception as err:
            return url, 0, str(err)[:140]


def main() -> None:
    urls = urls_from_bookmarks()
    print(f"Checking {len(urls)} unique URLs…")
    bad: list[tuple[str, int | str, str]] = []
    ok = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as pool:
        for url, code, note in pool.map(check, urls):
            if str(note).startswith("ok"):
                ok += 1
            else:
                bad.append((url, code, note))
                print(f"BAD\t{code}\t{url}\t{note}")
    print(f"Done. ok={ok} flagged={len(bad)} total={len(urls)}")
    print("Note: 403/429 often mean bot-blocking, not a dead page.")


if __name__ == "__main__":
    main()
