# Torraca Electrical — standalone site build

Built 16/07/2026. A complete, responsive, multi-page website you can deploy today. This is a from-scratch benchmark build, separate from the live Squarespace site.

## What is in the folder

23 pages, one shared design system, header and footer.

- `index.html` — home
- `services/` — services index + 7 service pages (switchboard upgrades, Level 2 ASP, EV chargers, data and comms, lighting, renovations and new builds, commercial and strata)
- 11 suburb pages — `electrician-hornsby/`, `electrician-asquith/`, `electrician-berowra/`, `electrician-mount-colah/`, `electrician-wahroonga/`, `electrician-turramurra/`, `electrician-pymble/`, `electrician-st-ives/`, `electrician-chatswood/`, `electrician-pennant-hills/`, `electrician-gordon/`
- `about/`, `contact/`, `service-areas/`
- `assets/` — one CSS file, one small JS file, optimised photos
- `sitemap.xml`, `robots.txt`
- `build.py`, `content.py`, `render.py` — the source generator. Not part of the live site. Edit `content.py` to change copy, then run `python3 render.py` to rebuild every page. Delete these three files before deploying if you want the folder spotless.

## Two things to fill before it goes live

1. **Real reviews.** The reviews section shows the real aggregate (5.0 from 101) and links to Google, but the three review cards are placeholders marked `[Paste a real Google review here]`. Drop in three real Google reviews (name, suburb, quote). Search `PLACEHOLDER` in `content.py` (the `reviews_block` function in `build.py`) or edit `index.html` directly. I did not invent reviews on purpose.
2. **Logo file.** The logo currently loads from your Squarespace CDN URL, so it needs internet to show. To make the site fully self-contained, export the logo PNG from Squarespace, save it as `assets/img/logo.png`, and swap the `LOGO` value near the top of `build.py` to `assets/img/logo.png` (the generator handles the relative paths), then rerun `render.py`. Optional, but cleaner.

## Facts locked in (corrected from the earlier draft)

Founded 2021 (the old draft wrongly said "since 2015 / 10+ years"). 101 five-star reviews (not 92). Licence 377890C and Level 2 ASP no. 5760 shown site-wide (the old draft had `[INSERT LICENCE NUMBER]`). ABN 40 654 325 694. NAP uses the registered Berowra address for schema. No emojis, no em dashes, brand voice throughout, banned phrases avoided.

## Deploy (fastest path: Netlify Drop, free)

1. Go to app.netlify.com/drop
2. Drag the whole `torraca-site` folder onto the page
3. It publishes in seconds on a temporary `*.netlify.app` address for you to review
4. To use it for real, point a domain at it in Netlify's domain settings

Any static host works the same way (Cloudflare Pages, GitHub Pages, Vercel). The folder is plain HTML, CSS, JS and images. No build step, no framework.

Note: this is a separate site from your live Squarespace one. If you migrate to it, you move the domain across and lose the Squarespace-hosted Google reviews widget (replace it with the reviews section here plus the Google link). If you would rather stay on Squarespace, tell me and I will map this copy and SEO into a Squarespace page plan instead.

## First seven days after launch

1. Point the domain and confirm every page loads on the live URL.
2. Submit `sitemap.xml` in Google Search Console and request indexing of the home, service and suburb pages.
3. Update the Google Business Profile so the name, address and phone match the footer exactly (Torraca Electrical Pty Ltd, 11 Kywong Rd Berowra NSW 2081, 0483 932 387).
4. Add the three real reviews to the reviews section.
5. Check the contact form. It opens the visitor's email app pre-filled to info@torracaelectrical.com.au. If you want form submissions to land in Outlook or simPRO automatically instead, wire it to a form service (Netlify Forms, Formspree) or an embedded Squarespace/simPRO form. Say the word and I will set it up.
6. Run the live URL through PageSpeed Insights and confirm mobile scores. Images are already sized and lazy-loaded below the fold.
7. Start the off-page work from the 15/07 diagnosis: citations (Google, Bing, Apple, True Local, Hipages) and a few local backlinks. That is the lever for ranking, not on-page.

## Accessibility and performance built in

WCAG AA contrast, 44px minimum tap targets, visible focus states, alt text on every image, labelled form fields, semantic headings (one H1 per page). One web font request (Poppins + Manrope). Images have width and height set and lazy-load below the fold. Content is visible without JavaScript; the scroll animation is a progressive enhancement only.
