# -*- coding: utf-8 -*-
"""Assemble a clean deploy folder (public/) from the generated site.
Netlify runs: python3 render.py && python3 build_netlify.py  (publish dir = public/)
Excludes the Python tooling, preview artifacts and anything non-web."""
import os, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
PUB = os.path.join(ROOT, "public")

SKIP_DIRS = {"public", ".git", "__pycache__", "_embed", "node_modules"}
SKIP_FILES = {"preview.html", "_preview_fragment.html", "LAUNCH.md",
              "netlify.toml", ".gitignore", "README.md", ".DS_Store",
              "gh-deploy-token.txt", "SETUP-github-deploy.md",
              "DEPLOY-github-netlify.md"}
SKIP_EXT = {".py", ".pyc", ".bak"}

def keep(rel):
    parts = rel.split(os.sep)
    if parts[0] in SKIP_DIRS: return False
    base = os.path.basename(rel)
    if base in SKIP_FILES: return False
    if os.path.splitext(base)[1] in SKIP_EXT: return False
    if "__pycache__" in parts: return False
    return True

count = 0
for dp, dirs, files in os.walk(ROOT):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    for f in files:
        full = os.path.join(dp, f)
        rel = os.path.relpath(full, ROOT)
        if not keep(rel):
            continue
        dest = os.path.join(PUB, rel)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copy2(full, dest)
        count += 1

print(f"public/ assembled: {count} files")
