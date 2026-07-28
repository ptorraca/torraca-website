# -*- coding: utf-8 -*-
"""Torraca Electrical static site generator. No em dashes, no emojis."""
import os, json, html

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE = "https://www.torracaelectrical.com.au"
PHONE = "0483 932 387"
TEL = "0483932387"
SMSNUM = "+61483932387"  # international format for cross-device sms: links
# Prefilled text so the customer's message lands with context. ?&body= works on iOS and Android.
SMSLINK = f"sms:{SMSNUM}?&body=Hi%20Torraca%2C%20I%27d%20like%20a%20quote%20for%3A%20"
EMAIL = "info@torracaelectrical.com.au"
LOGO = BASE + "/assets/img/logo.png"  # full colour wordmark logo (schema uses absolute URL)
REVIEWS = "101"
RATING = "5.0"
LIC = "377890C"
ASP = "5760"
ABN = "40 654 325 694"

# ---- SVG icons (stroke, currentColor) ----
I = {
 "phone":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
 "check":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
 "arrow":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>',
 "pin":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
 "clock":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><polyline points="12 7 12 12 15 14"/></svg>',
 "mail":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><polyline points="3 7 12 13 21 7"/></svg>',
 "board":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="3" width="16" height="18" rx="2"/><line x1="8" y1="7" x2="8" y2="11"/><line x1="12" y1="7" x2="12" y2="11"/><line x1="16" y1="7" x2="16" y2="11"/><line x1="8" y1="15" x2="16" y2="15"/></svg>',
 "ev":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 20V6a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v14"/><path d="M3 20h14"/><path d="M15 9h2a2 2 0 0 1 2 2v5a1.5 1.5 0 0 0 3 0v-6l-2-2"/><path d="M10 7l-2 3h3l-2 3"/></svg>',
 "bolt":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>',
 "data":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v14c0 1.7 3.6 3 8 3s8-1.3 8-3V5"/><path d="M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/></svg>',
 "bulb":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18h6"/><path d="M10 22h4"/><path d="M12 2a7 7 0 0 0-4 12.7c.6.5 1 1.3 1 2.1h6c0-.8.4-1.6 1-2.1A7 7 0 0 0 12 2z"/></svg>',
 "home":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V21h14V9.5"/><path d="M9 21v-6h6v6"/></svg>',
 "building":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="3" width="16" height="18" rx="1"/><line x1="9" y1="7" x2="9" y2="7.01"/><line x1="15" y1="7" x2="15" y2="7.01"/><line x1="9" y1="11" x2="9" y2="11.01"/><line x1="15" y1="11" x2="15" y2="11.01"/><line x1="9" y1="15" x2="9" y2="15.01"/><line x1="15" y1="15" x2="15" y2="15.01"/></svg>',
 "shield":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><polyline points="9 12 11 14 15 10"/></svg>',
 "star-svg":'<svg viewBox="0 0 24 24" fill="currentColor" stroke="none"><polygon points="12 2 15 9 22 9.3 16.5 14 18.3 21 12 17 5.7 21 7.5 14 2 9.3 9 9"/></svg>',
 "compass":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><polygon points="16 8 13 13 8 16 11 11 16 8"/></svg>',
 "chat":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.5 8.5 0 0 1-12 7.7L3 21l1.8-6A8.5 8.5 0 1 1 21 11.5z"/></svg>',
 "sms":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.5 8.5 0 0 1-12 7.7L3 21l1.8-6A8.5 8.5 0 1 1 21 11.5z"/><line x1="8" y1="11" x2="8" y2="11.01"/><line x1="12" y1="11" x2="12" y2="11.01"/><line x1="16" y1="11" x2="16" y2="11.01"/></svg>',
 "alert":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12" y2="17.01"/></svg>',
 "key":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="7.5" cy="15.5" r="4.5"/><path d="M10.5 12.5 20 3"/><path d="M16 7l3 3"/><path d="M13.5 9.5l2.5 2.5"/></svg>',
 "tree":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2 6 10h3l-4 6h5v6h4v-6h5l-4-6h3z"/></svg>',
 "scan":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7V5a2 2 0 0 1 2-2h2"/><path d="M17 3h2a2 2 0 0 1 2 2v2"/><path d="M21 17v2a2 2 0 0 1-2 2h-2"/><path d="M7 21H5a2 2 0 0 1-2-2v-2"/><circle cx="12" cy="12" r="3"/></svg>',
 "chev":'<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>',
}

# Nav dropdown data, populated by render.py (list of (slug, name))
NAV_SERVICES = []
NAV_SUBURBS = []
STARS = '<span class="stars" aria-label="5 out of 5 stars">'+I["star-svg"]*5+'</span>'

NAV = [("/", "Home"), ("/services/", "Services"), ("/about/", "About"),
       ("/service-areas/", "Areas"), ("/contact/", "Contact")]

# ---------- shared partials ----------
def head(title, desc, canon, schema, depth, body_class=""):
    a = "../"*depth if depth else ""
    og = LOGO
    js = "\n".join('<script type="application/ld+json">%s</script>' %
                   json.dumps(s, ensure_ascii=False) for s in schema)
    return f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script>document.documentElement.className+=' js';</script>
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canon}">
<meta name="robots" content="index, follow">
<meta property="og:type" content="website">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{og}">
<meta property="og:locale" content="en_AU">
<meta name="theme-color" content="#1f3d6e">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{a}assets/style.css">
{js}
</head>
<body class="{body_class}">"""

def header(depth):
    a = "../"*depth if depth else ""
    # Services dropdown. Homeowners + Businesses fly out to service labels
    # (placeholder text for now, individual pages to be linked later).
    # Property Managers + Strata are direct links to their landing pages.
    HOME_SVC = ["Electrical Repairs","Switchboard Upgrades","LED Lighting","Safety Switches",
        "Smoke Alarms","EV Chargers","Ceiling Fans","Power Points","Outdoor Lighting",
        "Rewiring","Surge Protection","24/7 Emergency"]
    BIZ_SVC = ["Commercial Electrician","3-Phase Power","Office Lighting","Emergency Lighting",
        "Data Cabling","Test and Tag","Commercial EV Charging","Power Upgrades",
        "Warehouse Lighting","Thermal Imaging","24/7 Emergency"]
    def _sub(label, items):
        lis = "".join(f'<span class="soon">{x}</span>' for x in items)
        return (f'<div class="subitem"><button class="subtoggle" aria-expanded="false" aria-haspopup="true">{label}'
                f'<span class="subchev">{I["chev"]}</span></button>'
                f'<div class="submenu">{lis}</div></div>')
    seg_menu = (_sub("Homeowners", HOME_SVC) + _sub("Businesses", BIZ_SVC)
        + f'<a class="navsingle" href="{a}property-managers/">Property Managers</a>'
        + f'<a class="navsingle" href="{a}strata/">Strata</a>')
    # Areas dropdown (was "Our Services"): same service options, each pointing to a
    # service-based area hub page that lists all the suburb links.
    areas_menu = "".join(f'<a href="{a}{s}/">{n}</a>' for s, n in [
        ("residential-electrician-areas","Residential Electrician"),
        ("commercial-electrician-areas","Commercial Electrician"),
        ("level-2-electrician-areas","Level 2 Electrician")])
    links = (
        f'<div class="navitem"><button class="navtoggle" aria-expanded="false" aria-haspopup="true">Services {I["chev"]}</button>'
        f'<div class="menu submenus">{seg_menu}</div></div>'
        f'<div class="navitem"><button class="navtoggle" aria-expanded="false" aria-haspopup="true">Areas {I["chev"]}</button>'
        f'<div class="menu">{areas_menu}<a class="menu-all" href="{a}service-areas/">All areas</a></div></div>'
        f'<a class="navlink" href="{a}services/level-2-asp-electrician/">Level 2 Electrician</a>'
        f'<a class="navlink" href="{a}about/">About</a>'
        f'<a class="navlink" href="{a}contact/">Contact</a>'
    )
    return f"""
<div class="top-note">101 five-star Google reviews. Licensed and Level 2 ASP accredited. <a href="tel:{TEL}">Call {PHONE}</a></div>
<header class="site">
  <div class="hd">
    <a class="brand" href="{a or './'}" aria-label="Torraca Electrical home">
      <img src="{a}assets/img/logo.png" alt="Torraca Electrical Pty Ltd" width="200" height="81">
    </a>
    <nav class="nav" id="nav" aria-label="Main">{links}</nav>
    <div class="hd-actions">
      <a class="hd-phone" href="tel:{TEL}">{I['phone']}<span>{PHONE}</span></a>
      <a class="btn btn-red" href="{a}contact/">Get a quote</a>
      <button class="burger" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<div class="callbar">
  <a class="btn btn-navy" href="tel:{TEL}">{I['phone']}Call now</a>
  <a class="btn btn-red" href="{a}contact/">Get a quote</a>
</div>"""

def footer(depth):
    a = "../"*depth if depth else ""
    svc = ["level-2-asp-electrician","residential-electrician","commercial-electrician",
           "ev-charger-installation","emergency-electrician","strata-property-maintenance"]
    svc_names = {"level-2-asp-electrician":"Level 2 ASP","residential-electrician":"Residential",
        "commercial-electrician":"Commercial","ev-charger-installation":"EV charger installation",
        "emergency-electrician":"Emergency 24/7","strata-property-maintenance":"Strata and property"}
    svc_links = "".join(f'<li><a href="{a}services/{s}/">{svc_names[s]}</a></li>' for s in svc)
    area_slugs = [("electrician-hornsby","Hornsby"),("electrician-wahroonga","Wahroonga"),
        ("electrician-chatswood","Chatswood"),("electrician-manly","Manly"),
        ("electrician-dee-why","Dee Why"),("electrician-castle-hill","Castle Hill")]
    area_links = "".join(f'<li><a href="{a}{s}/">{n}</a></li>' for s,n in area_slugs)
    return f"""
<footer class="site">
  <div class="wrap">
    <div class="foot">
      <div class="fb">
        <img src="{a}assets/img/logo.png" alt="Torraca Electrical Pty Ltd" width="200" height="81" loading="lazy">
        <p>Licensed electricians for homes, builders and property managers across Sydney's North Shore, Northern Beaches and Hills District. We get the job right the first time.</p>
        <div class="cred">Torraca Electrical Pty Ltd<br>NSW Electrical Contractor Licence {LIC}<br>Level 2 ASP no. {ASP} &nbsp;|&nbsp; ABN {ABN}</div>
      </div>
      <div>
        <h4>Services</h4>
        <ul>{svc_links}</ul>
      </div>
      <div>
        <h4>Service areas</h4>
        <ul>{area_links}<li><a href="{a}service-areas/">All areas</a></li></ul>
      </div>
      <div>
        <h4>Contact</h4>
        <div class="ci">{I['phone']}<a href="tel:{TEL}">{PHONE}</a></div>
        <div class="ci">{I['mail']}<a href="mailto:{EMAIL}">{EMAIL}</a></div>
        <div class="ci">{I['pin']}<span>11 Kywong Rd, Berowra NSW 2081</span></div>
        <div class="ci">{I['clock']}<span>Mon to Fri 7:00 to 17:00<br>Emergency callouts available</span></div>
      </div>
    </div>
    <div class="foot-bot">
      <span>Copyright {2026} Torraca Electrical Pty Ltd. All rights reserved.</span>
      <span>Electricians across Sydney's North Shore, Northern Beaches and Hills District</span>
    </div>
  </div>
</footer>
<script src="{a}assets/app.js" defer></script>
</body>
</html>"""

def local_business_schema(name=None, url=None, area=None):
    s = {
      "@context":"https://schema.org","@type":"Electrician",
      "name":"Torraca Electrical Pty Ltd",
      "image":LOGO,"logo":LOGO,"url":url or BASE+"/",
      "telephone":TEL,"email":EMAIL,"priceRange":"$$",
      "address":{"@type":"PostalAddress","streetAddress":"11 Kywong Rd",
        "addressLocality":"Berowra","addressRegion":"NSW","postalCode":"2081","addressCountry":"AU"},
      "geo":{"@type":"GeoCoordinates","latitude":-33.6236,"longitude":151.1503},
      "areaServed":area or ["Hornsby","Wahroonga","Turramurra","Pymble","St Ives","Gordon",
        "Killara","Lindfield","Roseville","Chatswood","Willoughby","Lane Cove","Berowra",
        "Manly","Balgowlah","Seaforth","Freshwater","Dee Why","Brookvale","Frenchs Forest",
        "Belrose","Narrabeen","Mona Vale","Newport","Avalon","Cherrybrook","West Pennant Hills",
        "Castle Hill","Dural","North Shore Sydney","Northern Beaches Sydney","Hills District Sydney"],
      "openingHoursSpecification":{"@type":"OpeningHoursSpecification",
        "dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],
        "opens":"07:00","closes":"17:00"},
      "sameAs":["https://www.facebook.com/torracaelectrical","https://www.instagram.com/torracaelectrical"],
      "aggregateRating":{"@type":"AggregateRating","ratingValue":RATING,"reviewCount":REVIEWS,
        "bestRating":"5","worstRating":"1"}
    }
    if name: s["name"]=name
    return s

def breadcrumb_schema(items):
    return {"@context":"https://schema.org","@type":"BreadcrumbList",
      "itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":u}
        for i,(n,u) in enumerate(items)]}

def faq_schema(qas):
    return {"@context":"https://schema.org","@type":"FAQPage",
      "mainEntity":[{"@type":"Question","name":q,
        "acceptedAnswer":{"@type":"Answer","text":a}} for q,a in qas]}

def qa_html(qas):
    out='<div class="faq">'
    for q,a in qas:
        out+=f'<details class="qa"><summary>{html.escape(q)}<span class="pm"></span></summary><div class="a">{a}</div></details>'
    out+='</div>'
    return out

def write(path, content):
    full=os.path.join(ROOT,path)
    os.makedirs(os.path.dirname(full),exist_ok=True)
    with open(full,"w",encoding="utf-8") as f: f.write(content)
    print("wrote",path)

# reusable review block (real aggregate + clearly-marked placeholders)
def reviews_block():
    return f"""
<section class="section" id="reviews">
  <div class="wrap center">
    <span class="eyebrow reveal">Reviews</span>
    <h2 class="h2 reveal">Rated 5.0 by 101 North Shore customers</h2>
    <div class="rev-head reveal">
      <div class="rev-badge">
        <span class="big">{RATING}</span>
        <span>{STARS}<br><span class="g">{REVIEWS} Google reviews</span></span>
      </div>
      <a class="btn btn-outline" href="https://www.google.com/search?q=Torraca+Electrical+reviews" rel="noopener" target="_blank">Read our reviews on Google</a>
    </div>
    <!-- Review quote cards hidden until 3 real Google reviews are supplied. Re-add via reviews_block in build.py. -->
  </div>
</section>"""

print("partials loaded")
