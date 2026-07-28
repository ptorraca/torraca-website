# -*- coding: utf-8 -*-
from content import *
import build
build.NAV_SERVICES = [(s['slug'], s['name']) for s in SERVICES if s['slug'] != 'level-2-asp-electrician']
build.NAV_SUBURBS = [(sb['slug'], sb['name']) for sb in SUBURBS]

def ticks(items):
    return '<ul class="ticks">'+"".join(f'<li>{I["check"]}<span>{html.escape(x)}</span></li>' for x in items)+'</ul>'

def chips():
    data=[("101 five-star Google reviews"),("Licence "+LIC),("Level 2 ASP no. "+ASP),("12-month workmanship warranty")]
    return '<div class="chips">'+"".join(f'<span class="chip">{I["check"]}{c}</span>' for c in data)+'</div>'

def cta_band(a=""):
    return f"""
<section class="section cta">
  <div class="wrap">
    <h2>Need a sparky who gets it right the first time?</h2>
    <p>Tell us about the job. We will give you a clear quote and a straight answer, no pressure.</p>
    <span class="cta-phone"><a href="tel:{TEL}">{PHONE}</a></span>
    <div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap">
      <a class="btn btn-white" href="tel:{TEL}">{I['phone']}Call now</a>
      <a class="btn btn-ghost" href="{SMSLINK}">{I['sms']}Text us</a>
      <a class="btn btn-ghost" href="{a}contact/">Get a quote</a>
    </div>
  </div>
</section>"""

# ---------------- HOME ----------------
def build_home():
    d=0
    schema=[local_business_schema(),
      {"@context":"https://schema.org","@type":"WebSite","name":"Torraca Electrical",
       "url":BASE+"/"}]
    services_cards=""
    for s in SERVICES:
        if s['slug']=='level-2-asp-electrician': continue
        services_cards+=f"""
        <a class="card reveal" href="services/{s['slug']}/">
          <div class="ic">{I[s['icon']]}</div>
          <h3>{s['name']}</h3>
          <p>{s['card']}</p>
          <span class="arrow">Learn more {I['arrow']}</span>
        </a>"""
    why=[("compass","Future-proofed, not patched","We ask what is coming next, an EV, a reno, a pool, and build for it, so the job is done once."),
     ("bolt","Level 2 ASP accredited","We do the network-side work most electricians cannot touch, in the same visit. Accreditation no. "+ASP+"."),
     ("shield","12-month workmanship warranty","If our work plays up in the first year, we come back and fix it at no cost."),
     ("check","Licensed and insured","NSW Electrical Contractor Licence "+LIC+", with public liability and professional indemnity cover."),
     ("pin","Local to the North Shore","Based in Berowra, we cover Hornsby and the Upper North Shore and respond quickly."),
     ("chat","Straight answers, upfront pricing","A clear quote before we start and no jargon. You always know what you are paying for.")]
    why_html=""
    for ic,h,p in why:
        why_html+=f'<div class="feat reveal"><div class="fic">{I[ic]}</div><div><h4>{h}</h4><p>{p}</p></div></div>'
    suburb_groups=""
    for reg in REGIONS:
        pills="".join(f'<a class="pill" href="{s["slug"]}/">{I["pin"]}{s["name"]}</a>'
                      for s in SUBURBS if s.get("region")==reg)
        suburb_groups+=f'<div class="area-group reveal"><h3 class="area-reg">{reg}</h3><div class="pills">{pills}</div></div>'
    steps=[("Call or enquire","Ring us or send the form with a quick description of the job."),
     ("We assess and quote","We look at the whole setup, not just the symptom, and give you a clear fixed quote."),
     ("Booked in and done right","We turn up when we say we will, do it to standard and leave it tidy."),
     ("Backed by our warranty","Compliance certificate supplied and 12 months on our workmanship.")]
    steps_html=""
    for i,(h,p) in enumerate(steps,1):
        steps_html+=f'<div class="step reveal"><div class="num">{i}</div><h4>{h}</h4><p>{p}</p></div>'

    body=f"""
<main>
<section class="hero-media">
  <img src="assets/img/team-hero.jpg" alt="The Torraca Electrical team on the job" width="2048" height="1362" fetchpriority="high">
</section>
<section class="hero-intro">
  <div class="wrap">
    <h1>Electrical work done once, done right.</h1>
    <p class="lead">Torraca Electrical looks after homes, builders and property managers across Sydney's North Shore, Northern Beaches and Hills District. We are licensed, Level 2 ASP accredited, and we ask the questions others miss so you are not paying to redo the same job twice.</p>
    <div class="hero-ctas">
      <a class="btn btn-red" href="tel:{TEL}">{I['phone']}Call {PHONE}</a>
      <a class="btn btn-outline" href="contact/">Get a quote</a>
    </div>
  </div>
</section>

<div class="stripbar"><div class="wrap">
  <span class="item"><span class="stars">{STARS}</span><span class="n">{RATING}</span> from {REVIEWS} Google reviews</span>
  <span class="item">{I['bolt']}Level 2 ASP accredited</span>
  <span class="item">{I['shield']}Licensed and insured</span>
  <span class="item">{I['pin']}North Shore, Northern Beaches and Hills</span>
</div></div>

<section class="section">
  <div class="wrap split">
    <div class="reveal">
      <span class="eyebrow">The difference</span>
      <h2 class="h2">Most electrical problems get fixed twice</h2>
      <p class="lead" style="margin-bottom:20px">The cheapest quote solves today's fault and ignores the board that caused it. Six months later you are booking another callout. We work differently. Before we start, we look at the whole setup and tell you what is coming, so the work holds up and you are not back here next year.</p>
      <a class="btn btn-navy" href="about/">How we work {I['arrow']}</a>
    </div>
    <div class="compare reveal">
      <div class="row">
        <div class="cell bad"><h4>The cheap way</h4><p>Fixes the symptom, leaves the cause. You pay again when it comes back.</p></div>
        <div class="cell good"><h4>Our way</h4><p>We find the cause, quote it straight, and size the fix for what you will add next.</p></div>
      </div>
      <div class="row">
        <div class="cell bad"><h4>Two trades</h4><p>Network-side work gets subbed out. More bookings, more markup.</p></div>
        <div class="cell good"><h4>One team</h4><p>Level 2 accredited, so we handle the connection and the wiring together.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="section services-sec">
  <div class="wrap">
    <div class="center"><span class="eyebrow reveal">What we do</span>
    <h2 class="h2 reveal">Electrical services across Sydney's north</h2>
    <p class="lead reveal" style="margin:0 auto 40px">From a single powerpoint to a full new-build fit-out and the network connection behind it, all backed by our Level 2 accreditation.</p></div>
    <div class="grid grid-3">{services_cards}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="center"><span class="eyebrow reveal">Why Torraca</span>
    <h2 class="h2 reveal">Built on getting it right the first time</h2></div>
    <div class="grid grid-3" style="margin-top:36px">{why_html}</div>
  </div>
</section>

<section class="section proc">
  <div class="wrap">
    <div class="center"><span class="eyebrow reveal">How it works</span>
    <h2 class="h2 reveal">From first call to job done</h2></div>
    <div class="steps">{steps_html}</div>
  </div>
</section>

{reviews_block()}

<section class="section areas-sec">
  <div class="wrap">
    <span class="eyebrow reveal">Service areas</span>
    <h2 class="h2 reveal">Electricians across the North Shore, Northern Beaches and Hills</h2>
    <p class="lead reveal">Based in Berowra and covering Sydney's North Shore, Northern Beaches and Hills District. Tap your suburb for local detail, or call us if you are not sure we reach you.</p>
    {suburb_groups}
  </div>
</section>

{cta_band()}
</main>"""
    doc=head("Electricians North Shore, Northern Beaches and Hills Sydney | Torraca Electrical",
      "Licensed electricians for homes, builders and property managers across Sydney's North Shore, Northern Beaches and Hills District. Level 2 ASP accredited, 101 five-star reviews. Call "+PHONE+".",
      BASE+"/", schema, d, body_class="home")+header(d)+body+footer(d)
    write("index.html",doc)

# ---------------- SERVICE PAGES ----------------
def build_service(s):
    d=2
    url=f"{BASE}/services/{s['slug']}/"
    emg = s.get("emergency")
    related=[x for x in SERVICES if x['slug']!=s['slug']][:4]
    rel_links="".join(f'<li><a href="../{r["slug"]}/">{I["arrow"]}{r["name"]}</a></li>' for r in related)
    sub_links="".join(f'<li><a href="../../{sb["slug"]}/">{I["pin"]}{sb["name"]}</a></li>' for sb in SUBURBS[:6])
    schema=[
      {"@context":"https://schema.org","@type":"Service","name":s['name'],
       "serviceType":s.get('stype',s['name']),"provider":local_business_schema(url=url),
       "areaServed":{"@type":"AdministrativeArea","name":"North Shore Sydney"},"url":url},
      breadcrumb_schema([("Home",BASE+"/"),("Services",BASE+"/services/"),(s['name'],url)])]
    intro_html="".join(f"<p>{p}</p>" for p in s['intro'])
    groups_html=""
    for gh,items in s['groups']:
        groups_html+=f"<h3>{html.escape(gh)}</h3>{ticks(items)}"
    edu_html=(f"<h2>{html.escape(s['edu_h'])}</h2><p>{s['edu_intro']}</p>"
              f"{ticks(s['edu_list'])}<p>{s['edu_close']}</p>")
    badge = f'<span class="em-badge">{I["alert"]}Available 24 hours, 7 days</span>' if emg else ""
    hero_cls = "pagehero emergency" if emg else "pagehero"
    prose_cls = "prose emergency" if emg else "prose"
    body=f"""
<main>
<section class="{hero_cls}">
  <img class="pagehero-bg" src="../../assets/img/{s['img']}" alt="Torraca Electrical, {html.escape(s['name'].lower())}" width="1000" height="1333">
  <div class="inner">
    <div class="crumb"><a href="../../">Home</a> / <a href="../">Services</a> / {s['name']}</div>
    {badge}
    <h1>{s['h1']}</h1>
    <p class="sub">{s['hero']}</p>
    <div style="display:flex;gap:14px;flex-wrap:wrap">
      <a class="btn btn-white" href="tel:{TEL}">{I['phone']}Call {PHONE}</a>
      <a class="btn btn-ghost" href="../../contact/">Get a quote</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap layout">
    <div class="{prose_cls}">
      {intro_html}
      <h2>Our {s['name'].lower()} services</h2>
      {groups_html}
      {edu_html}
    </div>
    <aside class="aside">
      <div class="box">
        <h4>{'Emergency? Call now' if emg else 'Talk to Torraca'}</h4>
        <p>{'We answer 24/7 for urgent electrical faults across the North Shore.' if emg else 'Straight advice and a clear quote. We cover Hornsby and the North Shore.'}</p>
        <a class="btn btn-red" href="tel:{TEL}" style="width:100%;margin-bottom:10px">{I['phone']}{PHONE}</a>
        <a class="btn btn-outline" href="{SMSLINK}" style="width:100%;margin-bottom:10px">{I['sms']}Text us</a>
        <a class="btn btn-outline" href="../../contact/" style="width:100%">Request a quote</a>
      </div>
      <div class="box">
        <h4>Related services</h4>
        <ul class="linklist">{rel_links}</ul>
      </div>
      <div class="box">
        <h4>Popular areas</h4>
        <ul class="linklist">{sub_links}</ul>
      </div>
    </aside>
  </div>
</section>
{cta_band("../../")}
</main>"""
    doc=head(s['title'],s['meta'],url,schema,d)+header(d)+body+footer(d)
    write(f"services/{s['slug']}/index.html",doc)

# ---------------- SERVICES INDEX ----------------
def build_services_index():
    d=1
    url=BASE+"/services/"
    cards=""
    for s in SERVICES:
        cards+=f"""<a class="card reveal" href="{s['slug']}/"><div class="ic">{I[s['icon']]}</div>
          <h3>{s['name']}</h3><p>{s['card']}</p><span class="arrow">Learn more {I['arrow']}</span></a>"""
    schema=[local_business_schema(url=url),
      breadcrumb_schema([("Home",BASE+"/"),("Services",url)])]
    body=f"""
<main>
<section class="pagehero">
  <div class="inner">
    <div class="crumb"><a href="../">Home</a> / Services</div>
    <h1>Electrical Services in Hornsby and the North Shore</h1>
    <p class="sub">From a single powerpoint to a full new-build fit-out and the network connection behind it. Everything backed by our Level 2 ASP accreditation and a 12-month workmanship warranty.</p>
    <div style="display:flex;gap:14px;flex-wrap:wrap">
      <a class="btn btn-white" href="tel:{TEL}">{I['phone']}Call {PHONE}</a>
      <a class="btn btn-ghost" href="../contact/">Get a quote</a>
    </div>
  </div>
</section>
<section class="section services-sec">
  <div class="wrap"><div class="grid grid-3">{cards}</div></div>
</section>
{cta_band("../")}
</main>"""
    doc=head("Electrical Services | Torraca Electrical Hornsby and North Shore",
      "Residential, commercial and Level 2 ASP electrical services across Hornsby and Sydney's North Shore. Switchboards, EV chargers, lighting, data, renovations and strata.",
      url,schema,d)+header(d)+body+footer(d)
    write("services/index.html",doc)

# ---------------- SEGMENT (customer type) PAGES ----------------
SEGMENTS=[
 {"slug":"homeowners","name":"Homeowners","img":"lighting.jpg",
  "h1":"Electricians for North Shore homeowners",
  "hero":"Clean, safe, future-proofed electrical work for homes across Hornsby and the North Shore. Done once, done right.",
  "title":"Electrician for Homeowners | Hornsby and North Shore | Torraca Electrical",
  "meta":"Licensed electricians for North Shore homeowners. Switchboards, EV chargers, lighting and Level 2, done right the first time. Call 0483 932 387.",
  "intro":"You want a sparky who turns up, does clean work, and gets it right the first time so you are not booking the same job twice. That is who we are. From an extra powerpoint to a full switchboard upgrade or an EV charger, we handle it and we future-proof it, so the work holds up for years.",
  "services":["residential-electrician","ev-charger-installation","level-2-asp-electrician","landscape-lighting","thermal-imaging","emergency-electrician"]},
 {"slug":"businesses","name":"Businesses","img":"switchboard.jpg",
  "h1":"Electricians for North Shore businesses",
  "hero":"Reliable commercial and industrial electrical that works around your trading hours. Fit-outs, maintenance and everything between.",
  "title":"Commercial Electrician for Businesses | Torraca Electrical",
  "meta":"Reliable electricians for North Shore businesses. Fit-outs, maintenance, test and tag and more, working around your trading hours. Call 0483 932 387.",
  "intro":"Downtime costs money, so you need an electrician who works around your trading hours and does not need managing. We look after offices, retail, warehouses and light industrial across the North Shore, from a single fit-out to an ongoing maintenance agreement.",
  "services":["commercial-electrician","industrial-electrician","ev-charger-installation","thermal-imaging","emergency-electrician"]},
 {"slug":"property-managers","name":"Property Managers","img":"van.jpg",
  "h1":"A reliable electrician for property managers",
  "hero":"One electrician you can call and forget about. Fast response, clear reporting, and work that holds up across your managed properties.",
  "title":"Electrician for Property Managers | Torraca Electrical",
  "meta":"A reliable electrician for property managers across the North Shore. Fast response, clear reporting, work that holds up. Call 0483 932 387.",
  "intro":"You want one electrician you can call and forget about, who turns up, sorts it, sends the paperwork and keeps it off your desk. That is the whole pitch. Reliable maintenance, fast response and clear reporting for the properties you manage.",
  "services":["strata-property-maintenance","emergency-electrician","residential-electrician","thermal-imaging"]},
 {"slug":"strata","name":"Strata","img":"van.jpg",
  "h1":"Strata electrical, handled",
  "hero":"Common areas, compliance and reactive callouts for owners corporations and strata managers across the North Shore.",
  "title":"Strata Electrician | North Shore | Torraca Electrical",
  "meta":"Strata electrical for owners corporations and strata managers. Common areas, compliance, reactive callouts and reporting. Call 0483 932 387.",
  "intro":"Common areas, car parks, compliance and the after-hours callout nobody planned for. We handle strata electrical for owners corporations and strata managers across the North Shore, with the documentation you need to stay compliant year-round.",
  "services":["strata-property-maintenance","emergency-electrician","commercial-electrician","level-2-asp-electrician"]},
]

def build_segment(seg):
    d=1
    url=f"{BASE}/{seg['slug']}/"
    cards=""
    for slug in seg['services']:
        s=SVC_BY_SLUG[slug]
        cards+=f"""<a class="card reveal" href="../services/{s['slug']}/"><div class="ic">{I[s['icon']]}</div>
          <h3>{s['name']}</h3><p>{s['card']}</p><span class="arrow">Learn more {I['arrow']}</span></a>"""
    schema=[local_business_schema(url=url),
      breadcrumb_schema([("Home",BASE+"/"),(seg['name'],url)])]
    body=f"""
<main>
<section class="pagehero">
  <img class="pagehero-bg" src="../assets/img/{seg['img']}" alt="Torraca Electrical for {html.escape(seg['name'].lower())}" width="1000" height="1333">
  <div class="inner">
    <div class="crumb"><a href="../">Home</a> / {seg['name']}</div>
    <h1>{seg['h1']}</h1>
    <p class="sub">{seg['hero']}</p>
    <div style="display:flex;gap:14px;flex-wrap:wrap">
      <a class="btn btn-red" href="tel:{TEL}">{I['phone']}Call {PHONE}</a>
      <a class="btn btn-white" href="../contact/">Get a quote</a>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap" style="max-width:820px">
    <p class="lead">{seg['intro']}</p>
  </div>
</section>
<section class="section services-sec" style="padding-top:0">
  <div class="wrap">
    <div class="center"><span class="eyebrow reveal">How we help</span>
    <h2 class="h2 reveal">What we do for {seg['name'].lower() if seg['name']!='Strata' else 'strata'}</h2></div>
    <div class="grid grid-3" style="margin-top:32px">{cards}</div>
  </div>
</section>
{cta_band("../")}
</main>"""
    doc=head(seg['title'],seg['meta'],url,schema,d)+header(d)+body+footer(d)
    write(f"{seg['slug']}/index.html",doc)

# ---------------- SUBURB PAGES ----------------
# Region-aware phrasing so the copy is honest about reach (Berowra is on the
# doorstep of the North Shore, a longer run to the Northern Beaches).
REACH={
 "North Shore":("part of our regular service area","Being local to the North Shore, we can usually get to {name} quickly."),
 "Hills District":("an area we regularly cover","We cover the Hills District regularly, so we can usually get to {name} without much wait."),
 "Northern Beaches":("an area we cover across the Northern Beaches","We cover the Northern Beaches regularly. Give us a ring and we will tell you the soonest we can be there."),
}

def build_suburb(sb):
    d=1
    url=f"{BASE}/{sb['slug']}/"
    name=sb['name']
    region=sb.get('region','North Shore')
    reach_area,reach_speed=REACH.get(region,REACH["North Shore"])
    # Per-suburb hero photo. Drop a file in assets/img/ and add "photo":"<filename>"
    # to the suburb in content.py (ideally the team on the job in that suburb).
    # Falls back to the shared van shot until a local photo is supplied.
    hero_img=sb.get('photo','hero-van.jpg')
    hero_alt=(f"Torraca Electrical on the job in {name}" if sb.get('photo')
              else f"Torraca Electrical serving {name}")
    svc_cards=""
    for s in SERVICES[:6]:
        svc_cards+=f"""<a class="card reveal" href="../services/{s['slug']}/"><div class="ic">{I[s['icon']]}</div>
          <h3>{s['name']}</h3><p>{s['card']}</p><span class="arrow">Learn more {I['arrow']}</span></a>"""
    # real nearby suburbs from the "near" list; fall back to same-region suburbs
    near=[SB_BY_SLUG[n] for n in sb.get('near',[]) if n in SB_BY_SLUG]
    if len(near)<3:
        near+=[x for x in SUBURBS if x['region']==region and x['slug']!=sb['slug'] and x not in near][:3-len(near)]
    other_links="".join(f'<a class="pill" href="../{o["slug"]}/">{I["pin"]}{o["name"]}</a>' for o in near)
    faqs=[
     (f"Do you cover {name}?",
      f"Yes. {name} is {reach_area}. Call {PHONE} and we will book you in."),
     (f"How quickly can you get to {name}?",
      f"{reach_speed} For urgent safety issues we run emergency callouts, so ring us and we will tell you the soonest we can be there."),
     (f"Do you charge extra to come out to {name}?",
      f"No. Our quote is our quote. There is no postcode premium for {name}, and you get a clear price before we start, not a surprise on the invoice."),
     ("Are you licensed and insured?",
      f"Yes. NSW Electrical Contractor Licence {LIC}, Level 2 ASP no. {ASP}, with public liability and professional indemnity cover. Every job comes with a compliance certificate and a 12-month workmanship warranty.")]
    schema=[local_business_schema(url=url,area=[name,region+" Sydney"]),
      breadcrumb_schema([("Home",BASE+"/"),("Service areas",BASE+"/service-areas/"),(f"Electrician {name}",url)]),
      faq_schema(faqs)]
    body=f"""
<main>
<section class="pagehero">
  <img class="pagehero-bg" src="../assets/img/{hero_img}" alt="{hero_alt}" width="1600" height="1000">
  <div class="inner">
    <div class="crumb"><a href="../">Home</a> / <a href="../service-areas/">Areas</a> / Electrician {name}</div>
    <h1>Electrician in {name}</h1>
    <p class="sub">Licensed, Level 2 ASP accredited electricians covering {name} and the surrounding {region}. Local, reliable, and focused on getting the job right the first time.</p>
    <div style="display:flex;gap:14px;flex-wrap:wrap">
      <a class="btn btn-white" href="tel:{TEL}">{I['phone']}Call {PHONE}</a>
      <a class="btn btn-ghost" href="../contact/">Get a quote</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap layout">
    <div class="prose">
      <p>{sb['intro']}</p>
      <p>Whether it is a switchboard that trips, a renovation that needs planning, an EV charger, or network-side work only a Level 2 provider can do, we handle the whole job. {name} is {sb['hook']}, and we know the local housing: {sb['local']}.</p>
      <h2>Electrical work we do across {name}</h2>
      {ticks(["Switchboard upgrades and safety switches","EV charger supply and installation","Level 2 connections, mains and metering","Lighting design and LED upgrades","Data and communications cabling","Renovation, extension and new-build wiring","Commercial, strata and property maintenance","Emergency callouts for genuine safety issues"])}
      <h2>Why {name} locals call Torraca</h2>
      <p>You get work that holds up, a clear quote before we start, and a team that turns up when it says it will. We plan for what you will add next, an EV charger, a reno, a pool, so the job is done once rather than twice. Most of our {name} work comes through referral, which tells you how the last job went.</p>
      <h2>Common questions</h2>
      {qa_html(faqs)}
    </div>
    <aside class="aside">
      <div class="box">
        <h4>Electrician in {name}</h4>
        <p>Local, licensed and Level 2 accredited. Call, text or send the form.</p>
        <a class="btn btn-red" href="tel:{TEL}" style="width:100%;margin-bottom:10px">{I['phone']}{PHONE}</a>
        <a class="btn btn-outline" href="{SMSLINK}" style="width:100%;margin-bottom:10px">{I['sms']}Text us</a>
        <a class="btn btn-outline" href="../contact/" style="width:100%">Request a quote</a>
      </div>
      <div class="box">
        <h4>Rated 5.0 on Google</h4>
        <p>{STARS} {REVIEWS} five-star reviews from customers across the North Shore, Northern Beaches and Hills.</p>
      </div>
    </aside>
  </div>
</section>

<section class="section services-sec">
  <div class="wrap">
    <div class="center"><span class="eyebrow reveal">Services in {name}</span><h2 class="h2 reveal">What we can do for you</h2></div>
    <div class="grid grid-3" style="margin-top:32px">{svc_cards}</div>
  </div>
</section>

<section class="section areas-sec">
  <div class="wrap center">
    <span class="eyebrow reveal">Nearby areas</span>
    <h2 class="h2 reveal">We also cover the suburbs around {name}</h2>
    <div class="pills reveal" style="justify-content:center">{other_links}</div>
  </div>
</section>
{cta_band("../")}
</main>"""
    title=f"Electrician {name} | Torraca Electrical | Local and Level 2 ASP"
    desc=f"Licensed electrician in {name}, NSW {sb['pc']}. Switchboards, EV chargers, Level 2 connections, lighting and more. 101 five-star reviews. Call {PHONE}."
    doc=head(title,desc,url,schema,d)+header(d)+body+footer(d)
    write(f"{sb['slug']}/index.html",doc)

# ---------------- ABOUT ----------------
def build_about():
    d=1;url=BASE+"/about/"
    schema=[local_business_schema(url=url),breadcrumb_schema([("Home",BASE+"/"),("About",url)])]
    vals=[("compass","We future-proof, we don't patch","The reason work gets done twice is that the first person only fixed what was in front of them. We look at the whole setup and plan for what you will add next."),
      ("bolt","We do the work others can't","As a Level 2 ASP provider we handle the network side of the meter ourselves, so your job is not held up waiting on a second trade."),
      ("chat","We give you a straight answer","A clear quote before we start, in plain language, so you always know the scope, the price and what happens next.")]
    vals_html="".join(f'<div class="feat reveal"><div class="fic">{I[ic]}</div><div><h4>{h}</h4><p>{p}</p></div></div>' for ic,h,p in vals)
    body=f"""
<main>
<section class="pagehero">
  <img class="pagehero-bg" src="../assets/img/van.jpg" alt="Torraca Electrical" width="900" height="1200">
  <div class="inner">
    <div class="crumb"><a href="../">Home</a> / About</div>
    <h1>About Torraca Electrical</h1>
    <p class="sub">A local electrical contractor on the North Shore, built around one idea: do the job once, do it right, and stand behind it.</p>
  </div>
</section>
<section class="section">
  <div class="wrap prose">
    <p>Torraca Electrical was founded in 2021 and is run by director Patrick La Torraca. We are a small team of electricians covering Hornsby and Sydney's North Shore, working across residential, commercial and light industrial jobs for homeowners, high-end builders and property managers.</p>
    <p>We built the business on a simple frustration: too much electrical work gets done cheaply and then done again. The switchboard that was swapped like for like and now cannot take the reno. The EV charger wired into a board that trips. The quote that solved the symptom and ignored the cause. We do the opposite. We ask the questions you have not thought of yet, plan for what you will add later, and get it right the first time. It costs a little more up front and saves you the second job.</p>
    <p>We are also an accredited Level 2 Authorised Service Provider, no. {ASP}. That means we can work on the network side of the meter, the consumer mains, the service line and the metering, which most electricians are not licensed to touch. For you it means one team from the street to the last powerpoint, not two trades and a wait.</p>
    <h2>What we stand for</h2>
  </div>
  <div class="wrap"><div class="grid grid-3" style="margin-top:20px">{vals_html}</div></div>
</section>
<div class="stripbar"><div class="wrap">
  <span class="item"><span class="stars">{STARS}</span><span class="n">{RATING}</span> from {REVIEWS} reviews</span>
  <span class="item">{I['shield']}Licence {LIC}</span>
  <span class="item">{I['bolt']}Level 2 ASP no. {ASP}</span>
  <span class="item">{I['check']}ABN {ABN}</span>
</div></div>
{cta_band("../")}
</main>"""
    doc=head("About Torraca Electrical | North Shore Electricians",
      "Torraca Electrical is a licensed, Level 2 ASP accredited electrical contractor on Sydney's North Shore. Founded 2021. We future-proof the job so it is done once.",
      url,schema,d)+header(d)+body+footer(d)
    write("about/index.html",doc)

# ---------------- CONTACT ----------------
def build_contact():
    d=1;url=BASE+"/contact/"
    schema=[local_business_schema(url=url),breadcrumb_schema([("Home",BASE+"/"),("Contact",url)])]
    opts=["Residential electrical","Commercial electrical","Industrial electrical","EV charger installation","Thermal imaging","Emergency (24/7)","Strata or property maintenance","Sports field lighting","Landscape lighting","Something else"]
    opt_html="".join(f"<option>{o}</option>" for o in opts)
    body=f"""
<main>
<section class="pagehero">
  <div class="inner">
    <div class="crumb"><a href="../">Home</a> / Contact</div>
    <h1>Get a quote</h1>
    <p class="sub">Tell us about the job and we will get back to you with a clear, no-obligation quote. For anything urgent, call and we will talk it through.</p>
  </div>
</section>
<section class="section">
  <div class="wrap split" style="align-items:start">
    <div class="reveal">
      <h2 class="h2">Talk to us</h2>
      <p class="lead" style="margin-bottom:24px">We cover Hornsby and Sydney's North Shore. Straight advice, upfront pricing and work that holds up.</p>
      <div class="foot" style="display:block;border:0;padding:0">
        <div class="ci" style="color:var(--ink);margin-bottom:16px">{I['phone']}<a href="tel:{TEL}" style="font-weight:700;color:var(--navy)">{PHONE}</a></div>
        <div class="ci" style="color:var(--ink);margin-bottom:16px">{I['mail']}<a href="mailto:{EMAIL}" style="font-weight:700;color:var(--navy)">{EMAIL}</a></div>
        <div class="ci" style="color:var(--ink);margin-bottom:16px">{I['pin']}<span>11 Kywong Rd, Berowra NSW 2081</span></div>
        <div class="ci" style="color:var(--ink)">{I['clock']}<span>Mon to Fri 7:00 to 17:00. Emergency callouts available.</span></div>
      </div>
      <p style="margin-top:22px;font-size:.92rem;color:var(--muted)">Licensed NSW Electrical Contractor {LIC}. Level 2 ASP no. {ASP}. ABN {ABN}.</p>
    </div>
    <div class="formwrap reveal">
      <form id="quoteform">
        <div class="fgrid">
          <div class="fg full"><label for="name">Name</label><input id="name" name="name" type="text" autocomplete="name" required></div>
          <div class="fg"><label for="phone">Phone</label><input id="phone" name="phone" type="tel" autocomplete="tel" required></div>
          <div class="fg"><label for="suburb">Suburb</label><input id="suburb" name="suburb" type="text"></div>
          <div class="fg full"><label for="service">What do you need?</label><select id="service" name="service"><option value="">Select a service</option>{opt_html}</select></div>
          <div class="fg full"><label for="message">Tell us about the job</label><textarea id="message" name="message" placeholder="A quick description. The more detail, the sharper the quote."></textarea></div>
          <div class="fg full"><button class="btn btn-red" type="submit" style="width:100%">Send my quote request</button>
          <p style="font-size:.82rem;color:var(--muted);margin-top:10px">This opens your email app with the details filled in. Prefer to talk? Call {PHONE}.</p></div>
        </div>
      </form>
    </div>
  </div>
</section>
</main>"""
    doc=head("Contact Torraca Electrical | Get a Quote | Hornsby and North Shore",
      "Get a no-obligation quote from Torraca Electrical. Call "+PHONE+" or send the form. Licensed, Level 2 ASP accredited electricians on Sydney's North Shore.",
      url,schema,d)+header(d)+body+footer(d)
    write("contact/index.html",doc)

# ---------------- SERVICE AREAS ----------------
def build_areas():
    d=1;url=BASE+"/service-areas/"
    schema=[local_business_schema(url=url),breadcrumb_schema([("Home",BASE+"/"),("Service areas",url)])]
    blurbs={"North Shore":"Home ground. From Hornsby and the Upper North Shore down to Chatswood and the Lower North Shore.",
            "Northern Beaches":"From Manly up the peninsula to Avalon, plus the Forest and the commercial pocket around Brookvale.",
            "Hills District":"Cherrybrook, Castle Hill and the acreage around Dural, where bigger blocks often need Level 2 supply work."}
    sections=""
    for reg in REGIONS:
        cards=""
        for sb in SUBURBS:
            if sb.get("region")!=reg: continue
            cards+=f"""<a class="card reveal" href="../{sb['slug']}/"><div class="ic">{I['pin']}</div>
              <h3>{sb['name']}</h3><p>Electrician in {sb['name']} {sb['pc']}. {sb['hook'].capitalize()}.</p>
              <span class="arrow">View {sb['name']} {I['arrow']}</span></a>"""
        sections+=f"""
<section class="section services-sec">
  <div class="wrap">
    <div class="center"><span class="eyebrow reveal">{reg}</span>
    <h2 class="h2 reveal">Electricians across the {reg}</h2>
    <p class="lead reveal" style="margin:0 auto 34px">{blurbs.get(reg,'')}</p></div>
    <div class="grid grid-3">{cards}</div>
  </div>
</section>"""
    body=f"""
<main>
<section class="pagehero">
  <div class="inner">
    <div class="crumb"><a href="../">Home</a> / Service areas</div>
    <h1>Where We Work</h1>
    <p class="sub">Based in Berowra and covering Sydney's North Shore, Northern Beaches and Hills District. If your suburb is not listed, call us. We will travel for the right job.</p>
    <div style="display:flex;gap:14px;flex-wrap:wrap">
      <a class="btn btn-white" href="tel:{TEL}">{I['phone']}Call {PHONE}</a>
      <a class="btn btn-ghost" href="../contact/">Get a quote</a>
    </div>
  </div>
</section>
{sections}
{cta_band("../")}
</main>"""
    doc=head("Service Areas | Torraca Electrical | North Shore, Northern Beaches and Hills",
      "Torraca Electrical covers Sydney's North Shore, Northern Beaches and Hills District. From Hornsby and Chatswood to Manly, Dee Why and Castle Hill. Find your suburb and call "+PHONE+".",
      url,schema,d)+header(d)+body+footer(d)
    write("service-areas/index.html",doc)

# ---------------- SERVICE-BASED AREA HUBS ----------------
# One hub per service option in the Areas menu. Each lists every suburb link,
# so suburbs live on the page rather than in the header. Suburb links point to
# the general suburb pages for now (service-specific suburb pages to come later).
AREA_HUBS=[
 {"slug":"residential-electrician-areas","svc":"Residential Electrician",
  "h1":"Residential Electrician Areas We Cover",
  "hero":"Local residential electricians across Sydney's North Shore, Northern Beaches and Hills District. Find your suburb below.",
  "intro":"We look after homes right across the North Shore, Northern Beaches and Hills. Pick your suburb for local detail, or call us if you are not sure we reach you.",
  "lead":[
    "We cover homes across three regions, and the electrical work changes with each one. The North Shore runs to older brick and weatherboard homes on ageing switchboards. The Northern Beaches cop the weather. The Hills mix newer estates with established acreage. We know what turns up in each, and we plan the job around it.",
    "Whatever the suburb, the approach is the same: a clear quote before we start, work that holds up, and a team that plans for what you will add next so the job is done once."],
  "does_h":"Residential work we do across every suburb",
  "does":["Switchboard upgrades and safety switches","Added power points, lighting and LED upgrades","Full and partial home rewires","EV charger supply and installation","Renovation, extension and new-build wiring","Fault finding and repairs","Smoke alarm installation and testing","Data and communications cabling"],
  "regions":{
    "North Shore":"The North Shore runs heavily to older brick and weatherboard homes, and plenty are still on switchboards and wiring from decades back. Most of our residential work here is switchboard and safety-switch upgrades, added circuits for renovations, and lighting. In the Federation homes around Wahroonga, Turramurra and Killara we plan the work around the character of the place, and near the stations there is steady unit and townhouse work as well.",
    "Northern Beaches":"Homes on the Northern Beaches cop the weather. Salt air is hard on outdoor wiring, lighting and anything exposed, so we spec fittings that stand up to it rather than replace them every few years. A lot of the older beach homes are being renovated or rebuilt, and the split-level houses on the slopes bring their own wiring quirks. We handle the lot, from a single power point to a full rewire.",
    "Hills District":"The Hills mixes newer estate homes with established acreage. On the bigger blocks we deal with longer service runs and often three-phase supply for larger homes, pools and sheds. Knock-down rebuilds and extensions are common, so we plan the electrical early and leave room for what you will add later, an EV charger, a pool, a granny flat, rather than redoing it down the track."},
  "why":"You get a clear quote before we start, work that holds up, and a team that turns up when it says it will. We plan for what you will add next so the job is done once, not twice. Most of our residential work comes through referral, which tells you how the last job went.",
  "faqs":[
    ("Which suburbs do you cover for residential work?","We cover homes right across the North Shore, Northern Beaches and Hills District. Pick your suburb above for local detail, or call "+PHONE+" and we will tell you straight if we reach you."),
    ("Do you charge more to travel to my suburb?","No. Our quote is our quote, with no postcode premium. You get a clear price before we start, not a surprise on the invoice."),
    ("Can you handle a full renovation or new build?","Yes. We wire renovations, extensions and new builds start to finish, and plan the job around what you will add later so it is done once."),
    ("Are you licensed and insured?","Yes. NSW Electrical Contractor Licence "+LIC+", Level 2 ASP no. "+ASP+", with public liability and professional indemnity cover. Every job comes with a compliance certificate and a 12-month workmanship warranty.")],
  "title":"Residential Electrician Areas | North Shore, Northern Beaches and Hills | Torraca Electrical",
  "meta":"Residential electricians across Sydney's North Shore, Northern Beaches and Hills District. Find your suburb and call "+PHONE+"."},
 {"slug":"commercial-electrician-areas","svc":"Commercial Electrician",
  "h1":"Commercial Electrician Areas We Cover",
  "hero":"Commercial and light-industrial electricians across Sydney's North Shore, Northern Beaches and Hills District. Find your suburb below.",
  "intro":"We work with businesses, offices, retail and light industrial across the North Shore, Northern Beaches and Hills. Pick your suburb, or call us to talk through the job.",
  "lead":[
    "The commercial work shifts by region. The North Shore is offices, retail strips and medical suites. The Northern Beaches run to retail, hospitality and a light-industrial pocket. The Hills carry the heavier fit-outs and warehousing. We work all three, and we schedule around your trading so the doors stay open.",
    "One team handles the fit-out, the ongoing maintenance and the after-hours callout, with the certificates and records to keep you compliant. You are not juggling separate contractors."],
  "does_h":"Commercial work we do across every suburb",
  "does":["Office, retail and tenancy fit-outs","Test and tag, RCD testing and compliance","Scheduled and preventative maintenance","Commercial LED and lighting upgrades","Emergency and exit lighting","Power distribution and three-phase","Strata and common-area electrical","After-hours callouts to keep you trading"],
  "regions":{
    "North Shore":"The North Shore business base is offices, retail strips and medical suites through Chatswood, Hornsby, Gordon and St Ives, plus the strata common areas that come with all the unit blocks. We handle tenancy fit-outs, maintenance, test and tag, and the after-hours callouts that keep a business trading. We work around your hours so the shopfront or office is not shut when it should be open.",
    "Northern Beaches":"Retail and hospitality drive a lot of the Northern Beaches work, cafes, restaurants and shops through Manly, Dee Why and Mona Vale, alongside the light-industrial pocket around Brookvale. Kitchens, cool rooms, lighting and three-phase equipment are regular jobs. We schedule around trading so the doors stay open, including after hours when the job needs it.",
    "Hills District":"The Hills carry the heavier commercial and light-industrial work, business parks and warehouses through the Norwest and Castle Hill area. Larger fit-outs, three-phase, high-bay lighting and machinery connections are day-to-day here. Whether it is a new tenancy or an ongoing maintenance run across a site, we scope it clearly and keep it compliant."},
  "why":"Businesses call us because we show up, work around their hours, and leave the paperwork sorted, certificates, test-and-tag records and reports. One team for the fit-out, the maintenance and the callout, so you are not juggling contractors.",
  "faqs":[
    ("Which areas do you cover for commercial work?","We work with businesses across the North Shore, Northern Beaches and Hills District. Pick your suburb above, or call "+PHONE+" to talk through the job."),
    ("Can you work outside our trading hours?","Yes. For shops, offices and anywhere downtime costs money, we run planned work after hours, on weekends or public holidays. The after-hours rate is agreed in writing before we start."),
    ("Do you do ongoing maintenance and test and tag?","Yes. We run scheduled maintenance, test and tag, RCD testing and compliance across sites, with the records and reports you need to stay compliant."),
    ("Are you licensed and insured?","Yes. NSW Electrical Contractor Licence "+LIC+", Level 2 ASP no. "+ASP+", with public liability and professional indemnity cover. Every job comes with a compliance certificate and a 12-month workmanship warranty.")],
  "title":"Commercial Electrician Areas | North Shore, Northern Beaches and Hills | Torraca Electrical",
  "meta":"Commercial electricians across Sydney's North Shore, Northern Beaches and Hills District. Find your suburb and call "+PHONE+"."},
 {"slug":"level-2-electrician-areas","svc":"Level 2 Electrician",
  "h1":"Level 2 ASP Electrician Areas We Cover",
  "hero":"Accredited Level 2 ASP work, connections, consumer mains and metering, across Sydney's North Shore, Northern Beaches and Hills District. Find your suburb below.",
  "intro":"As an accredited Level 2 Authorised Service Provider we handle the network-side work across the North Shore, Northern Beaches and Hills. Pick your suburb, or call us to check your job.",
  "lead":[
    "A Level 2 ASP is accredited to work on the network side of the meter, the consumer mains, service connections and metering that standard electricians cannot touch. We are accredited Level 2, and the work varies by region: ageing overhead supply on the North Shore, coastal weather on the Beaches, new connections out in the Hills.",
    "The advantage is one team for both sides of the meter. A supply upgrade and the switchboard behind it become a single job, so you are not chasing a separate provider for the network-side work."],
  "does_h":"Level 2 work we do across every suburb",
  "does":["Consumer mains repairs and upgrades","Overhead and underground service connections","New connections for builds and subdivisions","Metering installation and relocation","Service and supply fault repairs","Point of attachment and defect rectification","Temporary builders' supply","Network-side work standard electricians cannot do"],
  "regions":{
    "North Shore":"Much of the North Shore is on ageing overhead supply, so consumer-mains upgrades, service repairs and reconnections are steady Level 2 work. When an older home gets a switchboard or supply upgrade, the network-side work usually comes with it, and we do both, so you deal with one team instead of chasing a separate provider.",
    "Northern Beaches":"Coastal weather is hard on service lines, and storms bring down supply along the beaches more than most areas. We handle overhead and underground service work, consumer mains and metering, and we turn up for the storm-damage callouts that cannot wait. Being accredited Level 2, we do the network-side work standard electricians cannot.",
    "Hills District":"New builds and acreage drive Level 2 work in the Hills, new service connections, underground mains on the estates, and longer runs out to the bigger blocks. We coordinate the connection with the build so power is on when you need it, and handle metering and consumer mains as part of the same job."},
  "why":"As an accredited Level 2 ASP we handle both sides of the meter, so a supply upgrade and the switchboard behind it are one job with one team. Clear quote up front, compliance certificate on completion, and we turn up for the callouts that cannot wait.",
  "faqs":[
    ("What is a Level 2 electrician?","A Level 2 Authorised Service Provider is accredited to work on the network side of the meter, consumer mains, service connections and metering. Standard electricians cannot do this work. We are accredited Level 2, ASP no. "+ASP+"."),
    ("Which areas do you cover for Level 2 work?","We cover the North Shore, Northern Beaches and Hills District. Pick your suburb above, or call "+PHONE+" to check your job."),
    ("Can you do the connection and the switchboard together?","Yes. That is the advantage of Level 2, we handle both sides of the meter as one job, so you are not chasing a separate provider for the network-side work."),
    ("Are you licensed and insured?","Yes. NSW Electrical Contractor Licence "+LIC+", Level 2 ASP no. "+ASP+", with public liability and professional indemnity cover. Every job comes with a compliance certificate and a 12-month workmanship warranty.")],
  "title":"Level 2 ASP Electrician Areas | North Shore, Northern Beaches and Hills | Torraca Electrical",
  "meta":"Accredited Level 2 ASP electricians across Sydney's North Shore, Northern Beaches and Hills District. Find your suburb and call "+PHONE+"."},
]

def build_area_hub(hub):
    d=1;url=f"{BASE}/{hub['slug']}/"
    faqs=hub.get("faqs",[])
    schema=[local_business_schema(url=url),
      breadcrumb_schema([("Home",BASE+"/"),("Areas",BASE+"/service-areas/"),(hub['svc'],url)])]
    if faqs: schema.append(faq_schema(faqs))
    # per-region blocks: local note + suburb pills
    sections=""
    for reg in REGIONS:
        pills="".join(f'<a class="pill" href="../{s["slug"]}/">{I["pin"]}{s["name"]}</a>'
                      for s in SUBURBS if s.get("region")==reg)
        note=hub.get("regions",{}).get(reg,"")
        note_html=f'<p class="reveal" style="margin:6px 0 14px">{note}</p>' if note else ""
        sections+=f'<div class="area-group reveal"><h3 class="area-reg">{reg}</h3>{note_html}<div class="pills">{pills}</div></div>'
    lead_html="".join(f"<p>{p}</p>" for p in hub.get("lead",[hub['intro']]))
    faq_block=f"""
      <h2>Common questions</h2>
      {qa_html(faqs)}""" if faqs else ""
    body=f"""
<main>
<section class="pagehero">
  <div class="inner">
    <div class="crumb"><a href="../">Home</a> / <a href="../service-areas/">Areas</a> / {hub['svc']}</div>
    <h1>{hub['h1']}</h1>
    <p class="sub">{hub['hero']}</p>
    <div style="display:flex;gap:14px;flex-wrap:wrap">
      <a class="btn btn-white" href="tel:{TEL}">{I['phone']}Call {PHONE}</a>
      <a class="btn btn-ghost" href="../contact/">Get a quote</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap layout">
    <div class="prose">
      {lead_html}
      <h2>{hub.get('does_h','What we do')}</h2>
      {ticks(hub.get('does',[]))}
      <h2>Why locals call Torraca</h2>
      <p>{hub.get('why','')}</p>{faq_block}
    </div>
    <aside class="aside">
      <div class="box">
        <h4>{hub['svc']}</h4>
        <p>Local, licensed and Level 2 accredited. Call, text or send the form.</p>
        <a class="btn btn-red" href="tel:{TEL}" style="width:100%;margin-bottom:10px">{I['phone']}{PHONE}</a>
        <a class="btn btn-outline" href="{SMSLINK}" style="width:100%;margin-bottom:10px">{I['sms']}Text us</a>
        <a class="btn btn-outline" href="../contact/" style="width:100%">Request a quote</a>
      </div>
      <div class="box">
        <h4>Rated 5.0 on Google</h4>
        <p>{STARS} {REVIEWS} five-star reviews from customers across the North Shore, Northern Beaches and Hills.</p>
      </div>
    </aside>
  </div>
</section>

<section class="section areas-sec">
  <div class="wrap">
    <div class="center"><span class="eyebrow reveal">Suburbs we cover</span><h2 class="h2 reveal">Find your area</h2></div>
    <p class="lead reveal" style="margin:16px 0 6px">{hub['intro']}</p>
    {sections}
  </div>
</section>
{cta_band("../")}
</main>"""
    doc=head(hub['title'],hub['meta'],url,schema,d)+header(d)+body+footer(d)
    write(f"{hub['slug']}/index.html",doc)
# ---------------- SITEMAP + ROBOTS ----------------
def build_sitemap():
    urls=[BASE+"/",BASE+"/services/",BASE+"/about/",BASE+"/contact/",BASE+"/service-areas/"]
    urls+=[f"{BASE}/{seg['slug']}/" for seg in SEGMENTS]
    urls+=[f"{BASE}/services/{s['slug']}/" for s in SERVICES]
    urls+=[f"{BASE}/{h['slug']}/" for h in AREA_HUBS]
    urls+=[f"{BASE}/{sb['slug']}/" for sb in SUBURBS]
    items="".join(f"  <url><loc>{u}</loc><changefreq>monthly</changefreq><priority>{'1.0' if u==BASE+'/' else '0.8'}</priority></url>\n" for u in urls)
    write("sitemap.xml",'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+items+'</urlset>\n')
    write("robots.txt",f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")

if __name__=="__main__":
    build_home()
    build_services_index()
    for seg in SEGMENTS: build_segment(seg)
    for s in SERVICES: build_service(s)
    for sb in SUBURBS: build_suburb(sb)
    for hub in AREA_HUBS: build_area_hub(hub)
    build_about(); build_contact(); build_areas()
    build_sitemap()
    print("DONE")
