# Contributing

Thanks for helping keep this CTI bookmark set useful for hunters and analysts.

## Where to edit

| File | Purpose |
|------|---------|
| `cti-bookmarks.html` | Source of truth for Netscape-format browser import |
| `cti-bookmarks-console.html` | Browser console UI (embeds a JSON copy of the same links) |
| `README.md` | Folder overview for GitHub readers |

When you add, rename, or remove a link, update **both** HTML files so import and console stay in sync.

## Adding a bookmark

1. Pick the right pillar folder: **Operational**, **Tactical**, **Strategic**, or **Tools**.
2. Place it in the closest existing subcategory (create a new subcategory only if nothing fits).
3. Use a short display name, a stable HTTPS URL when possible, and a one-line description of *why* a hunter would open it.
4. Mirror the same entry in `cti-bookmarks-console.html` inside the embedded `DATA` array (`pillar` → `categories` → `links` with `name`, `url`, `host`, `blurb`).
5. Open the console locally and confirm search / **Use for** still make sense.

## Console extras (no sync needed)

Stars live in the browser (`localStorage`). Hunters can **Export** / **Import** JSON from the toolbar to move stars between machines. Keyboard shortcuts are listed under **?** in the console.

## Link health

Prefer fixing a moved page over deleting a useful resource. Automated HTTP checks often false-flag bot-protected sites (403/429); treat those as live unless a human browser also fails.

A lightweight checker used for this repo:

```bash
python scripts/check_links.py
```

## Pull requests

- One concern per PR when practical (links, console UX, or docs).
- Describe what changed and how you verified it (browser import and/or console open).
- Suggested license for contributions is MIT (see `LICENSE`).
