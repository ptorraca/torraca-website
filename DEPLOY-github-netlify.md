# Website — GitHub + Netlify auto-deploy

**Set up:** 28/07/2026. Replaces the old "zip and drop into Netlify" method.

## How it works now
The site source lives in a **private GitHub repo**: `github.com/ptorraca/torraca-website`.
Netlify (`candid-tarsier-5291b2.netlify.app`) is **linked to that repo**. Any commit
pushed to `main` triggers a build and publishes automatically in ~30 seconds.

    edit source  ->  git commit  ->  git push (main)  ->  Netlify builds & publishes

Netlify runs the build itself: `python3 render.py && python3 build_netlify.py`,
then publishes the `public/` folder. Config is in `netlify.toml`. Standard library
only — no packages to install.

## The everyday workflow
Just ask in a session: *"make this change to the website and push it."*
Claude edits the source, commits, pushes to `main`, and Netlify takes it live.
GitHub is the source of truth; this OneDrive folder is the working copy Claude
edits and keeps in sync.

## The deploy token
Claude pushes using a GitHub fine-grained token in `gh-deploy-token.txt` (this folder).
- Scope: this one repo only, Contents read/write. No expiry.
- Password-equivalent: it's git-ignored so it never lands in the repo. Don't share
  the file, don't paste it in chat.
- To rotate/revoke: GitHub -> Settings -> Developer settings -> Personal access
  tokens -> Fine-grained -> `torraca-website deploy`. Generate a new one and
  replace the contents of `gh-deploy-token.txt`.

## Rolling back
**A. Fast, live site only (Netlify one-click):** Netlify -> site
`candid-tarsier-5291b2` -> Deploys -> click the older deploy -> **Publish deploy**.
Reverts the live site instantly without touching GitHub.

**B. Proper rollback of the source:** ask Claude to *"roll back the website to the
previous version"* — reverts the commit and pushes, so GitHub and the live site
both go back cleanly, recorded in history.

## Staging vs live
The `netlify.app` URL is **staging** and is kept out of Google by the
`X-Robots-Tag = "noindex"` header block in `netlify.toml` (and the `_headers` file).
When you point the real domain (`torracaelectrical.com.au`) at Netlify, delete that
header block, push, then submit `sitemap.xml` in Google Search Console.
