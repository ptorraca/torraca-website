# One-time setup: auto-deploy via GitHub → Netlify

Do this once. After it's done, every change publishes itself: edit the files,
commit + push in GitHub Desktop, Netlify rebuilds in ~30 seconds.

The repo is already prepped — `netlify.toml`, `.gitignore` and the build
scripts are in place and the build's been tested. You're just connecting it up.

---

## Stage 1 — GitHub Desktop (get the folder onto GitHub)

1. Install GitHub Desktop from https://desktop.github.com and open it.
2. Sign in with a GitHub account (create a free one if you don't have it).
3. **File → Add local repository** → Choose this folder:
   `…/Torraca OS/website/torraca-standalone-site`
4. It'll say the folder isn't a git repository yet — click **"create a
   repository"**. Name it `torraca-website`, leave the path as-is, click
   **Create Repository**. (It'll use the existing `.gitignore` automatically.)
5. You'll see every file listed as a change. In the Summary box type
   `Initial commit — site, SMS CTAs, git deploy config`, then click
   **Commit to main**.
6. Click **Publish repository** (top bar). **Keep "Keep this code private"
   ticked.** Click Publish.

Done — your site source is now on GitHub.

## Stage 2 — Netlify (point it at the repo)

7. Log in at https://app.netlify.com and open your existing staging site
   (`candid-tarsier-5291b2`).
8. **Site configuration → Build & deploy → Continuous deployment** →
   **Link repository** (may read "Link site to Git").
9. Choose **GitHub**, authorise it, then pick the **torraca-website** repo and
   the **main** branch.
10. Build settings should auto-fill from `netlify.toml`:
    - Build command: `python3 render.py && python3 build_netlify.py`
    - Publish directory: `public`
    If either box is blank, type those in. Save.
11. Click **Deploy site**. Watch the log until it says **Published**.

## Stage 3 — check it worked

12. Open the staging URL, then add `/electrician-hornsby/` — you should see the
    new **Text us** button in the sidebar and the bottom band.
13. Staging stays hidden from Google: the `noindex` header is still in
    `netlify.toml`, so nothing's changed there.

---

## From now on

To publish any change: edit `content.py` (copy/suburbs) or `render.py`, open
GitHub Desktop, write a short summary, **Commit to main**, then **Push origin**.
Netlify does the rest.

## Two things to know

- **OneDrive:** this folder is cloud-synced. Git and OneDrive usually coexist
  fine, but if you ever get odd sync conflicts on the hidden `.git` folder,
  the fix is to move the repo out of OneDrive to a plain local folder.
- **Going live (later, separate job):** when you're ready to point
  `torracaelectrical.com.au` at Netlify, delete the `X-Robots-Tag = "noindex"`
  block in `netlify.toml`, push, then submit `sitemap.xml` in Google Search
  Console. Don't do this until you've decided to cut over from Squarespace.
