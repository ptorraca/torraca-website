# -*- coding: utf-8 -*-
"""Combine the generated multi-page site into one self-contained, navigable preview.html."""
import os, re, base64, json

ROOT = os.path.dirname(os.path.abspath(__file__))

# ---- collect pages and their routes ----
def route_for(relpath):
    d = os.path.dirname(relpath)
    return "/" + (d + "/" if d else "")

PAGES = []  # (route, mainhtml)
files = []
for dp, _, fs in os.walk(ROOT):
    for f in fs:
        if f == "index.html":
            rel = os.path.relpath(os.path.join(dp, f), ROOT)
            if rel.startswith("_"): continue
            files.append(rel)
# order: home, services index, services, suburbs, about/contact/areas
def sortkey(r):
    if r == "index.html": return (0, r)
    if r == "services/index.html": return (1, r)
    if r.startswith("services/"): return (2, r)
    if r.startswith("electrician-"): return (3, r)
    return (4, r)
files.sort(key=sortkey)

# ---- inline images as data URIs ----
# _embed was a temporary downsized-image dir; fall back to assets/img if absent.
EMB = os.path.join(ROOT, "_embed")
if not os.path.isdir(EMB):
    EMB = os.path.join(ROOT, "assets", "img")
def datauri(path):
    with open(path, "rb") as fh:
        b = base64.b64encode(fh.read()).decode()
    return "data:image/jpeg;base64," + b
IMGMAP = {}
for name in os.listdir(EMB):
    if not name.lower().endswith((".jpg", ".jpeg")): continue
    IMGMAP["assets/img/" + name] = datauri(os.path.join(EMB, name))

def resolve_route(page_rel, link):
    d = os.path.dirname(page_rel)
    tgt = os.path.normpath(os.path.join(d, link))
    if tgt == ".": tgt = ""
    r = "/" + (tgt + "/" if tgt else "")
    return "#" + r

def strip_bg(main):
    """Convert hero/pagehero <img> backgrounds into shared CSS background classes (dedupes data)."""
    def sub(m):
        key = os.path.basename(m.group("src")).rsplit(".", 1)[0]
        return f'<section class="{m.group("cls")} bg-{key}">'
    main = re.sub(r'<section class="(?P<cls>hero[^"]*)">\s*<img class="hero-bg" src="(?P<src>[^"]+)"[^>]*>', sub, main)
    main = re.sub(r'<section class="(?P<cls>pagehero[^"]*)">\s*<img class="pagehero-bg" src="(?P<src>[^"]+)"[^>]*>', sub, main)
    return main

def rewrite(main, page_rel):
    def repl(m):
        attr, val = m.group(1), m.group(2)
        if val.startswith(("tel:", "mailto:", "#", "http", "data:")):
            return f'{attr}="{val}"'
        norm = os.path.normpath(os.path.join(os.path.dirname(page_rel), val))
        if norm in IMGMAP:
            return f'{attr}="{IMGMAP[norm]}"'
        return f'{attr}="{resolve_route(page_rel, val)}"'
    return re.sub(r'(href|src)="([^"]+)"', repl, main)

for rel in files:
    html = open(os.path.join(ROOT, rel), encoding="utf-8").read()
    m = re.search(r"<main>(.*?)</main>", html, re.S)
    main = m.group(1) if m else ""
    main = rewrite(strip_bg(main), rel)
    PAGES.append((route_for(rel), main))

# shared background CSS (each image defined once)
BGCSS = ".hero,.pagehero{background-size:cover;background-position:center}\n"
for path, uri in IMGMAP.items():
    key = os.path.basename(path).rsplit(".", 1)[0]
    BGCSS += f".bg-{key}{{background-image:url({uri})}}\n"

# ---- shared CSS + JS (inline) ----
CSS = open(os.path.join(ROOT, "assets/style.css"), encoding="utf-8").read()
LOGO = "data:image/png;base64," + base64.b64encode(open(os.path.join(ROOT,"assets/img/logo.png"),"rb").read()).decode()
PHONE="0483 932 387"; TEL="0483932387"; EMAIL="info@torracaelectrical.com.au"
LIC="377890C"; ASP="5760"; ABN="40 654 325 694"

PHONE_ICON='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
MAIL_ICON='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><polyline points="3 7 12 13 21 7"/></svg>'
PIN_ICON='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>'
CLOCK_ICON='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><polyline points="12 7 12 12 15 14"/></svg>'

from content import SERVICES, SUBURBS, HOME_SERVICES
CHEV='<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>'
# Homeowners items are live pages: (slug, name) -> #/homeowners/<slug>/ routes.
HOME_SVC=[(s['slug'], s['name']) for s in HOME_SERVICES]
BIZ_SVC=["Commercial Electrician","3-Phase Power","Office Lighting","Emergency Lighting",
  "Data Cabling","Test and Tag","Commercial EV Charging","Power Upgrades",
  "Warehouse Lighting","Thermal Imaging","24/7 Emergency"]
def _sub_nav(label,items):
    cells=[]
    for x in items:
        if isinstance(x,tuple):
            slug,name=x
            cells.append(f'<a href="#/homeowners/{slug}/">{name}</a>')
        else:
            cells.append(f'<span class="soon">{x}</span>')
    lis="".join(cells)
    return (f'<div class="subitem"><button class="subtoggle" aria-expanded="false" aria-haspopup="true">{label}'
            f'<span class="subchev">{CHEV}</span></button><div class="submenu">{lis}</div></div>')
seg_menu_nav=(_sub_nav("Homeowners",HOME_SVC)+_sub_nav("Businesses",BIZ_SVC)
  +'<a class="navsingle" href="#/property-managers/">Property Managers</a>'
  +'<a class="navsingle" href="#/strata/">Strata</a>')
areas_menu_nav="".join(f'<a href="#/{s}/">{n}</a>' for s,n in [
  ("residential-electrician-areas","Residential Electrician"),
  ("commercial-electrician-areas","Commercial Electrician"),
  ("level-2-electrician-areas","Level 2 Electrician")])
navlinks=(
 f'<div class="navitem"><button class="navtoggle" aria-expanded="false" aria-haspopup="true">Services {CHEV}</button>'
 f'<div class="menu submenus">{seg_menu_nav}</div></div>'
 f'<div class="navitem"><button class="navtoggle" aria-expanded="false" aria-haspopup="true">Areas {CHEV}</button>'
 f'<div class="menu">{areas_menu_nav}<a class="menu-all" href="#/service-areas/">All areas</a></div></div>'
 '<a class="navlink" href="#/services/level-2-asp-electrician/">Level 2 Electrician</a>'
 '<a class="navlink" href="#/about/">About</a>'
 '<a class="navlink" href="#/contact/">Contact</a>'
)

svc=[("level-2-asp-electrician","Level 2 ASP"),("residential-electrician","Residential"),
     ("commercial-electrician","Commercial"),("ev-charger-installation","EV charger installation"),
     ("emergency-electrician","Emergency 24/7"),("strata-property-maintenance","Strata and property")]
svc_links="".join(f'<li><a href="#/services/{s}/">{n}</a></li>' for s,n in svc)
areas=[("electrician-hornsby","Hornsby"),("electrician-wahroonga","Wahroonga"),("electrician-chatswood","Chatswood"),
       ("electrician-manly","Manly"),("electrician-dee-why","Dee Why"),("electrician-castle-hill","Castle Hill")]
area_links="".join(f'<li><a href="#/{s}/">{n}</a></li>' for s,n in areas)

HEADER=f"""
<div class="top-note">101 five-star Google reviews. Licensed and Level 2 ASP accredited. <a href="tel:{TEL}">Call {PHONE}</a></div>
<header class="site">
  <div class="hd">
    <a class="brand" href="#/" aria-label="Torraca Electrical home"><img src="{LOGO}" alt="Torraca Electrical" width="180" height="46"></a>
    <nav class="nav" id="nav" aria-label="Main">{navlinks}</nav>
    <div class="hd-actions">
      <a class="hd-phone" href="tel:{TEL}">{PHONE_ICON}<span>{PHONE}</span></a>
      <a class="btn btn-red" href="#/contact/">Get a quote</a>
      <button class="burger" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<div class="callbar">
  <a class="btn btn-navy" href="tel:{TEL}">{PHONE_ICON}Call now</a>
  <a class="btn btn-red" href="#/contact/">Get a quote</a>
</div>"""

FOOTER=f"""
<footer class="site">
  <div class="wrap">
    <div class="foot">
      <div class="fb">
        <img src="{LOGO}" alt="Torraca Electrical" width="180" height="42" loading="lazy">
        <p>Licensed electricians for homes, builders and property managers across Sydney's North Shore, Northern Beaches and Hills District. We get the job right the first time.</p>
        <div class="cred">Torraca Electrical Pty Ltd<br>NSW Electrical Contractor Licence {LIC}<br>Level 2 ASP no. {ASP} &nbsp;|&nbsp; ABN {ABN}</div>
      </div>
      <div><h4>Services</h4><ul>{svc_links}</ul></div>
      <div><h4>Service areas</h4><ul>{area_links}<li><a href="#/service-areas/">All areas</a></li></ul></div>
      <div><h4>Contact</h4>
        <div class="ci">{PHONE_ICON}<a href="tel:{TEL}">{PHONE}</a></div>
        <div class="ci">{MAIL_ICON}<a href="mailto:{EMAIL}">{EMAIL}</a></div>
        <div class="ci">{PIN_ICON}<span>11 Kywong Rd, Berowra NSW 2081</span></div>
        <div class="ci">{CLOCK_ICON}<span>Mon to Fri 7:00 to 17:00<br>Emergency callouts available</span></div>
      </div>
    </div>
    <div class="foot-bot"><span>Copyright 2026 Torraca Electrical Pty Ltd. All rights reserved.</span><span>Electricians across Sydney's North Shore, Northern Beaches and Hills District</span></div>
  </div>
</footer>"""

pages_html=""
for route, main in PAGES:
    pages_html+=f'<div class="page" data-route="{route}" hidden>{main}</div>\n'

JS=r"""
(function(){
  var d=document, root=d.documentElement; root.className+=' js';
  var burger=d.querySelector('.burger'), nav=d.querySelector('.nav');
  function closeNav(){ if(nav){nav.classList.remove('open'); if(burger)burger.setAttribute('aria-expanded','false'); d.body.style.overflow='';} }
  if(burger&&nav){ burger.addEventListener('click',function(){var o=nav.classList.toggle('open'); burger.setAttribute('aria-expanded',o?'true':'false'); d.body.style.overflow=o?'hidden':'';}); }
  function closeSubs(scope){ (scope||d).querySelectorAll('.subitem.open').forEach(function(s){s.classList.remove('open'); var t=s.querySelector('.subtoggle'); if(t)t.setAttribute('aria-expanded','false');}); }
  function closeMenus(){ d.querySelectorAll('.navitem.open').forEach(function(i){i.classList.remove('open'); var t=i.querySelector('.navtoggle'); if(t)t.setAttribute('aria-expanded','false');}); closeSubs(); }
  d.querySelectorAll('.navtoggle').forEach(function(btn){
    btn.addEventListener('click',function(e){ e.preventDefault();
      var item=btn.closest('.navitem'), open=item.classList.contains('open'); closeMenus();
      if(!open){ item.classList.add('open'); btn.setAttribute('aria-expanded','true'); } });
  });
  d.querySelectorAll('.subtoggle').forEach(function(btn){
    btn.addEventListener('click',function(e){ e.preventDefault(); e.stopPropagation();
      var item=btn.closest('.subitem'), open=item.classList.contains('open'); closeSubs(item.parentNode);
      if(!open){ item.classList.add('open'); btn.setAttribute('aria-expanded','true'); } });
  });
  d.addEventListener('click',function(e){ if(!e.target.closest('.navitem')) closeMenus(); });
  var hdr=d.querySelector('header.site');
  window.addEventListener('scroll',function(){ if(hdr&&d.body.classList.contains('home')) hdr.classList.toggle('scrolled', window.scrollY>30); },{passive:true});
  function go(){
    var h=(location.hash||'#/').replace(/^#/,''); if(!h) h='/';
    var pages=d.querySelectorAll('.page'), active=null;
    pages.forEach(function(p){ var on=(p.getAttribute('data-route')===h); p.hidden=!on; if(on)active=p; });
    if(!active){ h='/'; pages.forEach(function(p){var on=p.getAttribute('data-route')==='/'; p.hidden=!on; if(on)active=p;}); }
    if(active){ active.querySelectorAll('.reveal').forEach(function(e){e.classList.add('in');}); }
    d.querySelectorAll('.navlink').forEach(function(a){ a.removeAttribute('aria-current'); if(a.getAttribute('href')==='#'+h)a.setAttribute('aria-current','page'); });
    d.body.classList.toggle('home', h==='/'); if(hdr) hdr.classList.remove('scrolled');
    closeNav(); closeMenus(); window.scrollTo(0,0);
    var f=d.getElementById('quoteform'); if(f&&!f._wired){ f._wired=true; f.addEventListener('submit',function(e){e.preventDefault(); var g=new FormData(f); var b='Name: '+(g.get('name')||'')+'\nPhone: '+(g.get('phone')||'')+'\nSuburb: '+(g.get('suburb')||'')+'\nService: '+(g.get('service')||'')+'\n\n'+(g.get('message')||''); location.href='mailto:info@torracaelectrical.com.au?subject='+encodeURIComponent('Website quote request')+'&body='+encodeURIComponent(b);}); }
  }
  window.addEventListener('hashchange',go); go();
})();
"""

DOC=f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Torraca Electrical — preview</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet">
<style>
{CSS}
.page[hidden]{{display:none}}
{BGCSS}
</style>
</head>
<body>
{HEADER}
<div id="app">
{pages_html}
</div>
{FOOTER}
<script>{JS}</script>
</body>
</html>"""

with open(os.path.join(ROOT,"preview.html"),"w",encoding="utf-8") as f:
    f.write(DOC)
print("preview.html written:", len(DOC)//1024, "KB,", len(PAGES), "pages")

# also emit a fragment (no doctype/head/body) for inline widget rendering
FRAG=f"""<style>
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Poppins:wght@600;700;800&display=swap');
{CSS}
.page[hidden]{{display:none}}
{BGCSS}
#twrap{{font-family:var(--font-b)}}
</style>
<div id="twrap">
{HEADER}
<div id="app">
{pages_html}
</div>
{FOOTER}
</div>
<script>{JS}</script>"""
with open(os.path.join(ROOT,"_preview_fragment.html"),"w",encoding="utf-8") as f:
    f.write(FRAG)
print("fragment written:", len(FRAG)//1024, "KB")
