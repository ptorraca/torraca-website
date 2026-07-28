# Torraca Electrical — website

Static, multi-page site for Torraca Electrical, generated from Python. Auto-deploys to Netlify on every push to `main`.

## How it deploys
Netlify runs `python3 render.py && python3 build_netlify.py` and publishes the `public/` folder. Config is in `netlify.toml`. No external Python packages — standard library only.

## Making edits
1. Edit `content.py` (all copy, services, suburbs) or `render.py` / `build.py` (layout, nav).
2. Rebuild locally to preview: `python3 render.py && python3 build_preview.py` then open `preview.html`.
3. Commit and push. Netlify rebuilds and publishes in ~30 seconds.

## Structure
- `build.py` — shared partials (head, header/nav, footer, schema helpers) + constants.
- `content.py` — the data: services and suburbs.
- `render.py` — builds every page (home, services, suburbs, area hubs, about, contact).
- `build_preview.py` — bundles the whole site into a single `preview.html` for review.
- `build_netlify.py` — assembles the clean `public/` deploy folder.
- `assets/` — CSS, JS, images.

## Before pointing the real domain
Delete the `X-Robots-Tag = "noindex"` block in `netlify.toml` (it keeps the staging URL out of Google). Then submit `sitemap.xml` in Google Search Console.
