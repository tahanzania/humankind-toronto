#!/usr/bin/env python3
"""Generates the static humanKIND toronto pages into the repo root (plain HTML output).

Usage:  python3 tools/build.py      (Python 3, standard library only)

Every .html page, sitemap.xml, robots.txt and _redirects in the repo root is written by this
script, so edit the copy and shared header/footer here, not in the generated files.
CSS, JS and images in assets/ are NOT generated; edit those directly.
"""
import json, os, html as _html

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)  # the repo root is the published site
BASE = "https://www.humankindtoronto.org"
META = json.load(open(os.path.join(HERE, "imgmeta.json")))  # {image name: [width, height]}
EMAIL = "helpforhumankind@gmail.com"
IG = "https://www.instagram.com/humankind_toronto"
FB = "https://www.facebook.com/humankindTO"
DONATE_FORM = "https://glassregister.societ.com/humankindtoronto/form?id=a23be75d-485c-4596-a85a-f2bd7a215c3a"
CHARITY_NO = "70047 3002 RC001"
LASTMOD = "2026-10-01"  # update when content changes
EVENT_ISO = "2026-11-20"
EVENT_HUMAN = "November 20, 2026"

def esc(s): return _html.escape(s, quote=True)

# ---------------------------------------------------------------- icons
ICONS = {
 "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 "heart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 20s-7-4.4-9.2-9A5 5 0 0 1 12 6a5 5 0 0 1 9.2 5C19 15.6 12 20 12 20Z"/></svg>',
 "box": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7.5 12 3l9 4.5v9L12 21l-9-4.5v-9Z"/><path d="M3 7.5 12 12l9-4.5M12 12v9"/></svg>',
 "people": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="9" cy="8" r="3.2"/><path d="M3 20a6 6 0 0 1 12 0"/><circle cx="17.5" cy="9" r="2.5"/><path d="M16 14.2A5 5 0 0 1 21 19"/></svg>',
 "hands": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 11V6.5a1.5 1.5 0 0 1 3 0V11M10 10V5a1.5 1.5 0 0 1 3 0v5M13 10V6a1.5 1.5 0 0 1 3 0v6"/><path d="M16 9.5a1.5 1.5 0 0 1 3 0V14a7 7 0 0 1-7 7h-.5A6.5 6.5 0 0 1 5 16.5L3.6 13a1.6 1.6 0 0 1 2.8-1.5L7 13"/></svg>',
 "spark": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v4M12 17v4M3 12h4M17 12h4M5.6 5.6l2.8 2.8M15.6 15.6l2.8 2.8M18.4 5.6l-2.8 2.8M8.4 15.6l-2.8 2.8"/></svg>',
 "gift": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="8" width="18" height="4" rx="1"/><path d="M5 12v8h14v-8M12 8v12M12 8S10.5 4 8 4a2 2 0 0 0 0 4M12 8s1.5-4 4-4a2 2 0 0 1 0 4"/></svg>',
 "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
 "instagram": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg>',
 "facebook": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13.5 21v-7.5h2.6l.4-3h-3V8.6c0-.9.3-1.5 1.5-1.5h1.6V4.4c-.3 0-1.2-.1-2.3-.1-2.3 0-3.8 1.4-3.8 3.9v2.3H8v3h2.5V21h3Z"/></svg>',
 "lock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>',
 "check": '<svg viewBox="0 0 26 26" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="13" cy="13" r="11.5" stroke-width="1" opacity=".35"/><path d="M8 13.5l3.4 3.4L18.5 9.5"/></svg>',
 "chev": '<svg viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M1.5 3.5 5 7l3.5-3.5"/></svg>',
 "sock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 3h7v9l-5.5 6.5a3.2 3.2 0 0 1-4.9-4.1L9 11V3Z"/><path d="M9 6h7"/></svg>',
 "calendar": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>',
}
def icon(n): return ICONS[n]

def ripples(cls="", n=3, animate=False):
    circles = "".join(f'<circle cx="300" cy="300" r="{r}"/>' for r in ([290, 290, 290] if animate else [90, 150, 210, 270][:n+1]))
    return f'<svg class="ripples{" ripples--animate" if animate else ""} {cls}" viewBox="0 0 600 600" aria-hidden="true" focusable="false">{circles}</svg>'

def underline(word):
    return (f'<span class="script-underline">{word}<svg viewBox="0 0 200 20" preserveAspectRatio="none" aria-hidden="true">'
            f'<path d="M3 14 C 50 4, 120 4, 197 11"/></svg></span>')

def img(name, alt, eager=False, sizes="(min-width: 900px) 50vw, 100vw"):
    w, h = META[name]
    load = 'fetchpriority="high" decoding="async"' if eager else 'loading="lazy" decoding="async"'
    return f'<img src="assets/img/{name}.webp" alt="{esc(alt)}" width="{w}" height="{h}" {load} sizes="{sizes}">'

def btn(href, label, kind="", arrow=True, extra=""):
    cls = "btn" + (f" btn--{kind}" if kind else "")
    return f'<a class="{cls}" href="{href}"{extra}>{label}{icon("arrow") if arrow else ""}</a>'

# ---------------------------------------------------------------- navigation
NAV = [
    ("About", None, [
        ("about.html", "Who We Are", "Values, mission &amp; our team"),
        ("our-story.html", "Our Story", "From 2017 to today"),
        ("faq.html", "FAQs", "Answers to common questions"),
    ]),
    ("Programs", "programs.html", None),
    ("Annual Drives", None, [
        ("annual-drives.html", "All Annual Drives", "Essentials, all year long"),
        ("sock-drive.html", "Sock Drive", "No more cold feet"),
        ("project-lunchbox.html", "Project Lunchbox", "A meal is more than food"),
        ("gift-of-hope.html", "Gift of Hope", "For a fresh start"),
    ]),
    ("Create for a Cause", None, [
        ("create-for-a-cause.html", "Create for a Cause 2026", "Save the date: Nov 20"),
        ("past-events.html", "Past Events", "2019 to 2025"),
    ]),
    ("Get Involved", None, [
        ("volunteer.html", "Volunteer", "Join our circle"),
        ("host-a-fundraiser.html", "Host a Fundraiser", "Bake sales, classes &amp; more"),
        ("partner-with-us.html", "Partner With Us", "For local businesses"),
    ]),
    ("Contact", "contact.html", None),
]

def wordmark(tag="a", href="index.html"):
    return (f'<a class="wordmark" href="{href}" aria-label="humanKIND toronto — home">'
            '<span class="wordmark__ring" aria-hidden="true">hK</span>'
            '<span class="wordmark__text" aria-hidden="true"><span class="wordmark__name">human<b>KIND</b></span>'
            '<span class="wordmark__city">toronto</span></span></a>')

def header(slug):
    def cur(h): return ' aria-current="page"' if h == slug else ""
    items = []
    for label, href, sub in NAV:
        if sub:
            current = any(s[0] == slug for s in sub)
            subs = "".join(f'<li><a href="{h}"{cur(h)}>{t}<small>{d}</small></a></li>' for h, t, d in sub)
            items.append(
                f'<li class="nav__item"><button class="nav__toggle{" is-current" if current else ""}" type="button" aria-expanded="false">'
                f'{label}{icon("chev")}</button><ul class="nav__sub">{subs}</ul></li>')
        else:
            items.append(f'<li class="nav__item"><a class="nav__link" href="{href}"{cur(href)}>{label}</a></li>')
    mob = []
    for label, href, sub in NAV:
        if sub:
            mob.append(f'<li><p class="mobile-group">{label}</p><ul class="sub">' + "".join(
                f'<li><a href="{h}"{cur(h)}>{t}</a></li>' for h, t, d in sub) + "</ul></li>")
        else:
            mob.append(f'<li><a href="{href}"{cur(href)}>{label}</a></li>')
    return f'''<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="container header-inner">
    {wordmark()}
    <nav class="nav" aria-label="Primary">
      <ul class="nav__list">{"".join(items)}</ul>
    </nav>
    <a class="btn header-cta" href="donate.html">Donate</a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="mobile-menu" data-menu-open><span class="menu-btn__bars" aria-hidden="true"></span>Menu</button>
  </div>
</header>
<div class="mobile-menu" id="mobile-menu" role="dialog" aria-modal="true" aria-label="Site menu" aria-hidden="true" inert>
  <div class="mobile-menu__top">{wordmark()}<button class="menu-btn" type="button" aria-expanded="true" data-menu-close><span class="menu-btn__bars" aria-hidden="true"></span>Close</button></div>
  <nav aria-label="Mobile">
    <ul>
      <li><a href="index.html"{' aria-current="page"' if slug == "index.html" else ""}>Home</a></li>
      {"".join(mob)}
    </ul>
  </nav>
  <div class="mobile-menu__foot">
    {btn("donate.html", "Donate", "sand")}
    {btn("volunteer.html", "Join Our Circle", "ghost-light")}
  </div>
</div>'''

def footer():
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="footer-top">
      <div>
        <img class="footer-logo" src="assets/img/humankind-toronto-logo-light.png" alt="humanKIND toronto logo" width="600" height="600" loading="lazy">
        <p class="footer-tagline">A female established organization creating awareness while empowering and uplifting women and children in local shelters.</p>
        <div class="socials">
          <a href="{IG}" target="_blank" rel="noopener" aria-label="humanKIND toronto on Instagram (opens in a new tab)">{icon("instagram")}</a>
          <a href="{FB}" target="_blank" rel="noopener" aria-label="humanKIND toronto on Facebook (opens in a new tab)">{icon("facebook")}</a>
          <a href="mailto:{EMAIL}" aria-label="Email humanKIND toronto">{icon("mail")}</a>
        </div>
      </div>
      <div>
        <h2>About</h2>
        <ul>
          <li><a href="about.html">Who We Are</a></li>
          <li><a href="our-story.html">Our Story</a></li>
          <li><a href="programs.html">Programs</a></li>
          <li><a href="faq.html">FAQs</a></li>
        </ul>
      </div>
      <div>
        <h2>Give back</h2>
        <ul>
          <li><a href="annual-drives.html">Annual Drives</a></li>
          <li><a href="create-for-a-cause.html">Create for a Cause</a></li>
          <li><a href="past-events.html">Past Events</a></li>
          <li><a href="volunteer.html">Volunteer</a></li>
          <li><a href="host-a-fundraiser.html">Host a Fundraiser</a></li>
          <li><a href="partner-with-us.html">Partner With Us</a></li>
          <li><a href="donate.html">Donate</a></li>
        </ul>
      </div>
      <div>
        <h2>Say hello</h2>
        <ul>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="{IG}" target="_blank" rel="noopener">@humankind_toronto</a></li>
          <li><a href="contact.html">Contact form</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 humanKIND toronto &middot; Greater Toronto Area, Ontario</span>
      <span>Charitable Registration Number: {CHARITY_NO}</span>
      <span><a href="privacy.html">Privacy</a> &middot; <a href="accessibility.html">Accessibility</a></span>
    </div>
  </div>
  <p class="footer-giant" aria-hidden="true">because the need never stops</p>
</footer>'''

ORG_LD = {
    "@context": "https://schema.org",
    "@type": "NGO",
    "@id": BASE + "/#organization",
    "name": "humanKIND toronto",
    "alternateName": "humanKIND",
    "url": BASE + "/",
    "logo": BASE + "/assets/img/humankind-toronto-logo.png",
    "image": BASE + "/assets/img/og-image.jpg",
    "email": EMAIL,
    "slogan": "Because the need never stops",
    "description": "A volunteer-led nonprofit supporting women, children, and youth living in shelters across the Greater Toronto Area through monthly programs, annual drives, and community giving.",
    "foundingDate": "2017",
    "founder": {"@type": "Person", "name": "Ashifa Champsi"},
    "taxID": CHARITY_NO,
    "areaServed": {"@type": "Place", "name": "Greater Toronto Area, Ontario, Canada"},
    "address": {"@type": "PostalAddress", "addressLocality": "Toronto", "addressRegion": "ON", "addressCountry": "CA"},
    "sameAs": [IG, FB],
}

def breadcrumbs_ld(crumbs):
    return {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name, "item": BASE + "/" + (href[:-5] if href != "index.html" else "")}
            for i, (name, href) in enumerate(crumbs)
        ],
    }

def breadcrumb_html(crumbs):
    lis = []
    for i, (name, href) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            lis.append(f'<li><span aria-current="page">{name}</span></li>')
        else:
            lis.append(f'<li><a href="{href}">{name}</a></li>')
    return f'<nav class="breadcrumb" aria-label="Breadcrumb"><ol>{"".join(lis)}</ol></nav>'

def page_hero(crumbs, eyebrow, title, lead, image=None, alt="", chip=None):
    media = ""
    if image:
        chip_html = f'<span class="float-chip">{chip}</span>' if chip else ""
        media = f'<div class="page-hero__media reveal reveal-delay-2"><div class="arch">{img(image, alt, eager=True, sizes="(min-width: 940px) 440px, 90vw")}</div>{chip_html}</div>'
    return f'''<section class="page-hero">
  {ripples(animate=True)}
  <div class="container">
    {breadcrumb_html(crumbs)}
    <div class="page-hero__grid">
      <div class="reveal">
        <p class="eyebrow">{eyebrow}</p>
        <h1>{title}</h1>
        <p class="lead">{lead}</p>
      </div>
      {media}
    </div>
  </div>
</section>'''

def cta_band(title="Kindness is <em>contagious.</em>", text="Join a growing circle of volunteers, donors, partners and small businesses who show up, consistently and compassionately.", buttons=None):
    buttons = buttons or [btn("volunteer.html", "Join Our Circle", "sand"), btn("donate.html", "Donate", "ghost-light")]
    return f'''<section class="cta-band">
  {ripples(animate=True)}
  <div class="container container--narrow reveal">
    <p class="eyebrow" style="color:var(--sage)">Because the need never stops</p>
    <h2>{title}</h2>
    <p class="lead" style="margin-inline:auto;color:rgba(231,217,203,.9)">{text}</p>
    <div class="btn-row">{"".join(buttons)}</div>
  </div>
</section>'''

def render(slug, title, description, body, crumbs=None, extra_ld=None, og_image="og-image.jpg", robots="index, follow"):
    canonical = BASE + "/" + ("" if slug == "index.html" else slug[:-5])
    ld = [ORG_LD] if slug == "index.html" else [ {"@context": "https://schema.org", "@type": "WebPage", "name": title, "url": canonical, "description": description, "isPartOf": {"@type": "WebSite", "name": "humanKIND toronto", "url": BASE + "/"}, "publisher": {"@id": BASE + "/#organization"}} ]
    if slug == "index.html":
        ld.append({"@context": "https://schema.org", "@type": "WebSite", "name": "humanKIND toronto", "url": BASE + "/", "publisher": {"@id": BASE + "/#organization"}, "inLanguage": "en-CA"})
    if crumbs: ld.append(breadcrumbs_ld(crumbs))
    if extra_ld: ld.extend(extra_ld)
    ld_html = "\n".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    doc = f'''<!doctype html>
<html lang="en-CA" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{esc(description)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#3d4435">
<meta property="og:type" content="website">
<meta property="og:site_name" content="humanKIND toronto">
<meta property="og:locale" content="en_CA">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{BASE}/assets/img/{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Members of the humanKIND toronto community at Create for a Cause">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(description)}">
<meta name="twitter:image" content="{BASE}/assets/img/{og_image}">
<link rel="icon" type="image/png" href="favicon.png">
<link rel="apple-touch-icon" href="favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&amp;family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&amp;family=Open+Sans:wght@300;400;600;700&amp;display=swap">
<link rel="stylesheet" href="assets/css/styles.css">
<script src="assets/js/main.js" defer></script>
{ld_html}
</head>
<body>
{header(slug)}
<main id="main">
{body}
</main>
{footer()}
</body>
</html>
'''
    with open(os.path.join(SITE, slug), "w", encoding="utf-8") as f:
        f.write(doc)
    return canonical

PAGES = []
def page(slug, title, desc, body, crumbs=None, extra_ld=None, priority="0.7", robots="index, follow", in_sitemap=True):
    url = render(slug, title, desc, body, crumbs, extra_ld, robots=robots)
    if in_sitemap: PAGES.append((url, priority))

def marquee(words):
    group = "".join(f"<span>{w}</span><i>✦</i>" for w in words)
    return (f'<div class="marquee" role="presentation"><div class="marquee__track">'
            f'<div class="marquee__group">{group}</div><div class="marquee__group" aria-hidden="true">{group}</div>'
            f'<div class="marquee__group" aria-hidden="true">{group}</div><div class="marquee__group" aria-hidden="true">{group}</div></div></div>')

def help_list(items):
    return '<ul class="help-list">' + "".join(
        f'<li><span class="help-list__icon">{icon(ic)}</span><span>{t}</span></li>' for ic, t in items) + "</ul>"

def packing(title, kicker, items):
    lis = "".join(f'<li><span>{t}</span>{icon("check")}</li>' for t in items)
    return f'<div class="packing"><p class="packing__title">{kicker}</p><h3>{title}</h3><ol>{lis}</ol></div>'

def gallery(items, cls=""):
    figs = "".join(f'<figure class="reveal">{img(n, a, sizes="(min-width: 900px) 25vw, 50vw")}</figure>' for n, a in items)
    return f'<div class="gallery {cls}">{figs}</div>'

HOME = [("Home", "index.html")]

# ================================================================= HOME
home = f'''
<section class="hero">
  {ripples(animate=True, cls="")}
  <div class="container hero__grid">
    <div class="reveal">
      <p class="eyebrow">Hope &middot; Empowerment &middot; Joy</p>
      <h1><span class="line">Because the need</span> <span class="line"><em>never stops.</em></span></h1>
      <p class="hero__intro">It started with a simple intention: <strong>Let’s give back.</strong></p>
      <p class="hero__intro">Today, humanKIND toronto is a growing circle of women committed to walking alongside women, children, and youth living in shelters across the Greater Toronto Area.</p>
      <div class="btn-row">
        {btn("volunteer.html", "Join Our Circle")}
        {btn("donate.html", "Support a Program", "ghost")}
      </div>
      <p style="margin-top:1.4rem"><a class="text-link" href="programs.html">Learn More About Our Work {icon("arrow")}</a></p>
    </div>
    <div class="hero__collage reveal reveal-delay-2" aria-label="Moments from humanKIND toronto programs and events">
      <div class="arch">{img("cfac-team-banner", "Four women from the humanKIND toronto community smiling together in front of the organization’s banner", eager=True, sizes="(min-width: 980px) 330px, 56vw")}</div>
      <div class="arch">{img("art-roses", "A bright acrylic painting of pink roses in a blue vase, made during an art session", eager=True, sizes="(min-width: 980px) 250px, 42vw")}</div>
      <div class="arch">{img("sock-team-boxes", "Volunteers surrounded by Sox Box collection boxes filled with new socks", eager=True, sizes="(min-width: 980px) 250px, 42vw")}</div>
      <div class="hero__badge" aria-hidden="true">
        <svg class="spin" viewBox="0 0 200 200"><defs><path id="badge-circle" d="M100,100 m-78,0 a78,78 0 1,1 156,0 a78,78 0 1,1 -156,0"/></defs>
          <text><textPath href="#badge-circle">kindness in action ✦ dignity matters ✦ since 2017 ✦</textPath></text></svg>
        <span class="heart">{icon("heart")}</span>
      </div>
    </div>
  </div>
</section>

<section class="section section--tight" aria-labelledby="we-support">
  <div class="container">
    <h2 id="we-support" class="visually-hidden">Who we support</h2>
    <div class="manifesto">
      <div class="manifesto__row reveal"><span class="manifesto__label">We support</span><p class="manifesto__text">those fleeing <em>domestic abuse.</em></p></div>
      <div class="manifesto__row reveal"><span class="manifesto__label">We support</span><p class="manifesto__text">those facing <em>homelessness.</em></p></div>
      <div class="manifesto__row reveal"><span class="manifesto__label">We support</span><p class="manifesto__text">those rebuilding after <em>trauma and isolation.</em></p></div>
    </div>
    <p class="big-serif reveal" style="margin-top:2.2rem;max-width:30ch">And we do it with {underline("compassion")}, creativity, and community.</p>
  </div>
</section>

{marquee(["Healing", "Self-care", "Creativity", "Confidence", "Connection"])}

<section class="section" aria-labelledby="what-we-do">
  <div class="container">
    <div class="split split--wide-left split--top">
      <div class="reveal">
        <p class="eyebrow">What we do</p>
        <h2 id="what-we-do">Every month, we step into shelters.</h2>
      </div>
      <div class="reveal reveal-delay-1">
        <p class="lead">We offer programs that create space for healing, self-care, creativity, confidence and connection.</p>
        <p class="muted">We provide essential items throughout the year so that no woman or child feels forgotten in their time of need.</p>
      </div>
    </div>
    <ul class="space-for" aria-label="Every program creates space for">
      <li class="reveal" tabindex="0">{img("selfcare-affirmations", "Affirmation cards from a humanKIND self-care session", sizes="200px")}<div><b>01</b><span>Healing</span></div></li>
      <li class="reveal reveal-delay-1" tabindex="0">{img("selfcare-kit", "A self-care kit with makeup and skincare items in a kraft gift bag", sizes="200px")}<div><b>02</b><span>Self-care</span></div></li>
      <li class="reveal reveal-delay-2" tabindex="0">{img("art-mandala", "A hand-painted dot mandala on a terracotta dish", sizes="200px")}<div><b>03</b><span>Creativity</span></div></li>
      <li class="reveal reveal-delay-3" tabindex="0">{img("lifeskills-strengths", "A life skills workshop handout titled Identifying Individual Strengths", sizes="200px")}<div><b>04</b><span>Confidence</span></div></li>
      <li class="reveal reveal-delay-3" tabindex="0">{img("cfac-tables", "Women chatting and laughing around a decorated table at a community event", sizes="200px")}<div><b>05</b><span>Connection</span></div></li>
    </ul>
  </div>
</section>

<section class="section section--olive affirm on-dark" aria-labelledby="seen">
  {ripples(animate=True)}
  <div class="container reveal">
    <p class="eyebrow" style="justify-content:center">More than anything</p>
    <h2 id="seen" class="affirm__lead">But more than anything, we remind them</h2>
    <ul class="affirm__words"><li>they are seen.</li><li>they matter.</li><li>they are not alone.</li></ul>
  </div>
</section>

<section class="section section--tight" aria-label="humanKIND toronto at a glance">
  <div class="container">
    <div class="stats">
      <div class="stat reveal"><span class="stat__num">2017</span><span class="stat__label">Founded in Toronto</span></div>
      <div class="stat reveal reveal-delay-1"><span class="stat__num">6</span><span class="stat__label">Partner shelters</span></div>
      <div class="stat reveal reveal-delay-2"><span class="stat__num">6</span><span class="stat__label">Monthly programs</span></div>
      <div class="stat reveal reveal-delay-3"><span class="stat__num">3</span><span class="stat__label">Annual drives</span></div>
    </div>
  </div>
</section>

<section class="section section--sand" aria-labelledby="programs-teaser">
  <div class="container">
    <div class="split split--top" style="margin-bottom:3rem">
      <div class="reveal"><p class="eyebrow">Our programs</p><h2 id="programs-teaser">Moments of healing, connection, <em>and joy.</em></h2></div>
      <div class="reveal reveal-delay-1"><p class="lead">On-site and virtual programs for women and children, each one thoughtfully designed to foster self-expression, build confidence, and create a sense of community.</p>{btn("programs.html", "Explore Programs", "ghost")}</div>
    </div>
    <div class="cards cards--4">
      <a class="card-program reveal" href="programs.html#life-skills"><div class="arch">{img("lifeskills-papers", "Workshop handouts spread across a table during a life skills session", sizes="(min-width: 1000px) 25vw, 50vw")}</div><span class="card-program__num">01</span><h3>Life Skills</h3><p>Practical tools that support confidence, independence, and personal growth.</p></a>
      <a class="card-program reveal reveal-delay-1" href="programs.html#yoga-cooking"><div class="arch">{img("cook-pizzas", "Homemade mini pizzas topped with colourful vegetables, ready for the oven", sizes="(min-width: 1000px) 25vw, 50vw")}</div><span class="card-program__num">02</span><h3>Yoga &amp; Cooking</h3><p>Relaxation, nourishment, and self-care through gentle yoga and cooking demos.</p></a>
      <a class="card-program reveal reveal-delay-2" href="programs.html#art"><div class="arch">{img("art-wreath-painting", "A humanKIND volunteer holding up floral wreath paintings from an art session", sizes="(min-width: 1000px) 25vw, 50vw")}</div><span class="card-program__num">03</span><h3>Art Sessions</h3><p>A powerful outlet where the process matters more than the outcome.</p></a>
      <a class="card-program reveal reveal-delay-3" href="programs.html#shared-meals"><div class="arch">{img("meals-spread", "Trays of grilled chicken, chopped tomatoes, onions and cucumbers prepared for a shared meal", sizes="(min-width: 1000px) 25vw, 50vw")}</div><span class="card-program__num">04</span><h3>Shared Meals</h3><p>Gathering around food for nourishment, conversation, and belonging.</p></a>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="drives-teaser">
  <div class="container">
    <div class="center reveal" style="margin-bottom:3rem">
      <p class="eyebrow">Annual drives</p>
      <h2 id="drives-teaser">Small things, <em>delivered with care.</em></h2>
      <p class="lead">Throughout the year, our community comes together to collect the essentials that are needed most.</p>
    </div>
    <div class="cards cards--3">
      <a class="drive-card reveal" href="sock-drive.html"><span class="tag">Sock Drive</span><div class="drive-card__img">{img("sock-boy-boxes", "A young donor and a volunteer with two Sox Boxes overflowing with new socks", sizes="(min-width: 1000px) 33vw, 100vw")}</div><div class="drive-card__body"><h3>No more cold feet</h3><p>One of the most requested, and most overlooked, essentials: new socks for children and adults.</p><span class="text-link">Sock Drive {icon("arrow")}</span></div></a>
      <a class="drive-card reveal reveal-delay-1" href="project-lunchbox.html"><span class="tag">Project Lunchbox</span><div class="drive-card__img">{img("lunchbox-kit", "A lunch kit with an insulated lunch bag, water bottle, food containers and granola bars", sizes="(min-width: 1000px) 33vw, 100vw")}</div><div class="drive-card__body"><h3>A meal is more than food</h3><p>Thoughtfully packed lunchboxes that bring routine, stability, and comfort.</p><span class="text-link">Project Lunchbox {icon("arrow")}</span></div></a>
      <a class="drive-card reveal reveal-delay-2" href="gift-of-hope.html"><span class="tag">Gift of Hope</span><div class="drive-card__img">{img("hope-packing", "Volunteers packing large bags of bedding and household items for Gift of Hope", sizes="(min-width: 1000px) 33vw, 100vw")}</div><div class="drive-card__body"><h3>Something to call their own</h3><p>Bedding and comfort items for women and children as they leave a shelter and begin again.</p><span class="text-link">Gift of Hope {icon("arrow")}</span></div></a>
    </div>
  </div>
</section>

<section class="section section--sand-soft" aria-labelledby="community">
  <div class="container split">
    <div class="reveal" style="position:relative">
      <div class="arch" style="aspect-ratio:4/5;max-width:520px">{img("volunteers-group", "A large group of humanKIND toronto volunteers and supporters posing together", sizes="(min-width: 900px) 45vw, 100vw")}</div>
    </div>
    <div class="reveal reveal-delay-1">
      <p class="eyebrow">A community that shows up</p>
      <h2 id="community">Volunteers. Donors. Partners. <em>Small businesses.</em></h2>
      <p class="lead">humanKIND toronto is powered by women who care deeply.</p>
      <p>From yoga classes and art workshops to bake sales and handcrafted goods, our community continues to find beautiful, creative ways to give back.</p>
      <p class="big-serif" style="font-size:clamp(1.5rem,1.2rem + 1.2vw,2.2rem)">Because kindness is contagious. Because dignity matters. Because the need never stops.</p>
      <div class="btn-row">{btn("volunteer.html", "Join Our Circle")}{btn("our-story.html", "Read Our Story", "ghost")}</div>
    </div>
  </div>
</section>

<section class="section section--tight" aria-labelledby="shelters">
  <div class="container center">
    <p class="eyebrow reveal">Walking alongside</p>
    <h2 id="shelters" class="reveal">Some of the shelters we <em>support</em></h2>
    <ul class="partners">
      <li class="reveal"><img src="assets/img/partner-nisa.webp" alt="NISA Homes" width="360" height="360" loading="lazy"></li>
      <li class="reveal reveal-delay-1"><img src="assets/img/partner-sakeenah.webp" alt="Sakeenah Homes" width="360" height="360" loading="lazy"></li>
      <li class="reveal reveal-delay-2"><img src="assets/img/partner-ybh.webp" alt="Yellow Brick House" width="360" height="360" loading="lazy"></li>
      <li class="reveal reveal-delay-3"><img src="assets/img/partner-360kids.webp" alt="360°kids" width="360" height="360" loading="lazy"></li>
      <li class="reveal reveal-delay-3"><img src="assets/img/partner-sandgate.webp" alt="Sandgate Women’s Shelter of York Region" width="360" height="360" loading="lazy"></li>
    </ul>
  </div>
</section>

<section class="section section--tight" aria-labelledby="save-the-date">
  <div class="container">
    <div class="std reveal">
      <div class="std__date" aria-hidden="true"><span class="std__month">Nov</span><span class="std__day">20</span><span class="std__year">2026</span></div>
      <div>
        <p class="eyebrow">Save the date &middot; {EVENT_HUMAN}</p>
        <h2 id="save-the-date">Create for a Cause</h2>
        <p style="margin:0">Our annual fundraising event: a creative workshop that brings community together in support of women and children living in shelters.</p>
      </div>
      {btn("create-for-a-cause.html", "Event Details")}
    </div>
  </div>
</section>

<section class="section" aria-labelledby="instagram">
  <div class="container insta">
    <div class="reveal">
      <p class="eyebrow">Follow our journey</p>
      <h2 id="instagram">On Instagram</h2>
      <a class="insta__handle" href="{IG}" target="_blank" rel="noopener">@humankind_toronto</a>
    </div>
    <div class="insta__grid reveal reveal-delay-1">
      <a href="{IG}" target="_blank" rel="noopener" aria-label="View on Instagram: painted flower art">{img("art-flowers", "Painted flowers in a glass vase", sizes="200px")}</a>
      <a href="{IG}" target="_blank" rel="noopener" aria-label="View on Instagram: Create for a Cause">{img("cfac-herb-bowls", "Bowls of dried herbs and flowers at a Create for a Cause workshop", sizes="200px")}</a>
      <a href="{IG}" target="_blank" rel="noopener" aria-label="View on Instagram: sock drive notes">{img("sock-notes", "Hand-decorated notes reading I hope these socks keep you warm", sizes="200px")}</a>
      <a href="{IG}" target="_blank" rel="noopener" aria-label="View on Instagram: cooking workshop">{img("cook-parfaits", "Yogurt parfaits with berries and granola from a cooking workshop", sizes="200px")}</a>
      <a href="{IG}" target="_blank" rel="noopener" aria-label="View on Instagram: Gift of Hope">{img("hope-envelopes", "Handwritten notes of encouragement in colourful envelopes", sizes="200px")}</a>
      <a href="{IG}" target="_blank" rel="noopener" aria-label="View on Instagram: humanKIND tote">{img("selfcare-tote", "A humanKIND tote printed with Because the need never stops, surrounded by self-care items", sizes="200px")}</a>
    </div>
  </div>
</section>

{cta_band()}
'''
page("index.html", "humanKIND toronto | Supporting Women & Children in GTA Shelters",
     "humanKIND toronto is a volunteer-led nonprofit supporting women, children, and youth living in shelters across the Greater Toronto Area with monthly programs, annual drives, and community care.",
     home, priority="1.0")

# ================================================================= ABOUT
TEAM = [
    ("Ashifa Champsi", "Founder", "AC",
     "What 3 things would you take if you were deserted on an island?",
     "My family, my paint supplies and of course a flint (learned that from watching Survivor).",
     "To recognize that the difficulties we face in life, allow us to grow from that experience and that we can strengthen ourselves from that growth."),
    ("Salma Valimohamed", "Sr. Board Member", "SV",
     "What’s your favourite food?",
     "The edible kind - I love food, all food, I don’t discriminate.",
     "Be good, do good, have faith - do only these 3 things everyday and you are pretty much guaranteed a life well-lived."),
    ("Fatimah Alibhai", "Board Member", "FA",
     "What 3 things would you take if you were deserted on an island?",
     "A book that never ends, white board and pen (can that count as 1?), and the Qur’an (my holy book) with exegesis - maybe then I will finally have enough time to read the entire book!",
     "Love thyself and be kind to thyself. Live in the moment - the past is done, we cannot bring it back but we can take lessons from it, and worrying about the future will not change it."),
    ("Fatima Kamalia", "Board Member", "FK",
     "If you could live anywhere, where would it be?",
     "I would choose between two very different places; one would be an Islamic state such as Mecca, Medina or Iraq and the other would be Italy due to its culture, food and the people. I always joke that I should have been born as an Italian Muslim.",
     "Always try to help others (whether it be that little old lady crossing the street or a wounded animal) because no matter how hard life may be for you at this moment; and it will eventually get better with time, hope and faith, there is always someone who is struggling even more… so a helping hand or two will go a long way."),
]
TEAM_PHOTOS = {  # full name -> filename in assets/img/ (square, 600px)
    "Ashifa Champsi": "team-ashifa.webp",
    "Salma Valimohamed": "team-salma.webp",
    "Fatimah Alibhai": "team-fatimah.webp",
    "Fatima Kamalia": "team-fatima-k.webp",
}
team_html = ""
for i, (name, role, mono, q, a, advice) in enumerate(TEAM):
    if name in TEAM_PHOTOS:
        mono_html = f'<div class="team-card__mono"><img src="assets/img/{TEAM_PHOTOS[name]}" alt="Portrait of {esc(name)}" width="300" height="300" loading="lazy"></div>'
    else:
        mono_html = f'<div class="team-card__mono" aria-hidden="true">{mono}</div>'
    team_html += f'''<article class="team-card reveal{" reveal-delay-" + str(i) if i else ""}">
  <div class="team-card__inner">
    <div class="team-card__face team-card__front">
      {mono_html}
      <h3>{name}</h3>
      <p class="team-card__role">{role}</p>
      <button class="team-card__btn" type="button">Get to know {name.split()[0]} {icon("arrow")}</button>
    </div>
    <div class="team-card__face team-card__back" aria-hidden="true" inert>
      <h4>Fun fact</h4>
      <p><span class="q">{q}</span>{a}</p>
      <h4>Piece of advice</h4>
      <p>{advice}</p>
      <button class="team-card__btn" type="button">Back to {name.split()[0]}</button>
    </div>
  </div>
</article>'''

about_crumbs = HOME + [("Who We Are", "about.html")]
about = f'''
{page_hero(about_crumbs, "About humanKIND toronto", "Who <em>we are</em>",
  "humanKIND toronto was founded in 2017 by a small group of women who believed kindness should be active — not passive.",
  "board-team", "Members of the humanKIND toronto team standing together in front of the organization’s banner", chip="est. 2017")}

<section class="section">
  <div class="container split split--wide-right split--top">
    <div class="reveal">
      <p class="eyebrow">Volunteer-led &middot; GTA</p>
      <h2>Not to <em>fix</em> their journey, but to walk beside them in it.</h2>
    </div>
    <div class="reveal reveal-delay-1">
      <p class="lead">We are a volunteer-led nonprofit working across the Greater Toronto Area to support women, children, and youth living in shelters.</p>
      <p>Many of the individuals we serve are navigating through domestic abuse, homelessness, trauma, and profound isolation. Our role is not to “fix” their journey — but to walk beside them in it.</p>
      <p>We partner with six shelters and currently deliver six monthly programs designed to foster healing, empowerment, and personal growth.</p>
      <div class="btn-row">{btn("our-story.html", "Read Our Story")}{btn("programs.html", "Our Programs", "ghost")}</div>
    </div>
  </div>
</section>

<section class="section section--sand" aria-labelledby="values">
  <div class="container center">
    <p class="eyebrow reveal">What grounds us</p>
    <h2 id="values" class="reveal">Four core <em>values</em></h2>
    <p class="lead reveal">Everything we do is grounded in four core values.</p>
    <div class="values">
      <div class="value reveal"><span class="value__num">01</span><h3>Compassion</h3><p>We lead with heart.</p></div>
      <div class="value reveal reveal-delay-1"><span class="value__num">02</span><h3>Kindness</h3><p>We act with intention.</p></div>
      <div class="value reveal reveal-delay-2"><span class="value__num">03</span><h3>Empathy</h3><p>We listen first.</p></div>
      <div class="value reveal reveal-delay-3"><span class="value__num">04</span><h3>Community</h3><p>We grow together.</p></div>
    </div>
    <p class="big-serif reveal" style="margin:3.5rem auto 0;max-width:28ch">We believe real change happens when people come together, consistently, humbly, and {underline("wholeheartedly.")}</p>
  </div>
</section>

<section class="section" aria-label="Mission and vision">
  <div class="container mv">
    <div class="mv__panel mv__panel--mission on-dark reveal">
      {ripples()}
      <p class="eyebrow">Our mission</p>
      <h2>Kindness in action.</h2>
      <p class="big">To support and empower women, children, and youth living in shelters by providing meaningful programs, essential resources, and opportunities for the wider community to give back.</p>
      <p>We exist to promote kindness in action.</p>
    </div>
    <div class="mv__panel mv__panel--vision reveal reveal-delay-1">
      {ripples()}
      <p class="eyebrow">Our vision</p>
      <h2>No one invisible.</h2>
      <p class="big">A community where every woman and child facing hardship feels supported, dignified, and surrounded by care.</p>
      <p>We envision a world where no one rebuilding their life feels invisible and where giving back becomes second nature.</p>
    </div>
  </div>
</section>

<section class="section section--sand-soft" aria-labelledby="team">
  <div class="container">
    <div class="split split--top" style="margin-bottom:3rem">
      <div class="reveal"><p class="eyebrow">Meet the team</p><h2 id="team">The hearts <em>behind</em> humanKIND</h2></div>
      <div class="reveal reveal-delay-1"><p class="lead">We asked our team a few questions to get to know them better. Flip a card to see what they had to say.</p></div>
    </div>
    <div class="team">{team_html}</div>
  </div>
</section>

<section class="section" aria-labelledby="reasons">
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">Our reasons why</p>
      <h2 id="reasons">A simple act of kindness can have a <em>profound</em> impact.</h2>
      <p>We at humanKIND toronto are passionate about helping others in need. We know that a simple act of kindness can have a profound impact on individuals, especially those who are dealing with trauma and feeling isolated. Through our various initiatives, we create opportunities to help bring people together, connect, learn and have fun.</p>
    </div>
    <div class="reveal reveal-delay-1" style="display:grid;grid-template-columns:1fr 1fr;gap:16px;align-items:end">
      <div class="arch" style="aspect-ratio:3/4">{img("cfac-friends", "Three smiling women taking a selfie together at a humanKIND event", sizes="(min-width: 900px) 25vw, 50vw")}</div>
      <div class="arch arch--down" style="aspect-ratio:3/4;margin-bottom:-30px">{img("volunteers-tiedye", "A smiling volunteer holding up a hand-dyed pouch she made", sizes="(min-width: 900px) 25vw, 50vw")}</div>
    </div>
  </div>
</section>

{cta_band("Together we can make <em>an impact.</em>")}
'''
page("about.html", "Who We Are | humanKIND toronto",
     "Meet humanKIND toronto: a volunteer-led nonprofit founded in 2017 that partners with six GTA shelters to support women, children, and youth. Our values, mission, vision and team.",
     about, about_crumbs, priority="0.9")

# ================================================================= OUR STORY
story_crumbs = HOME + [("Who We Are", "about.html"), ("Our Story", "our-story.html")]
story = f'''
{page_hero(story_crumbs, "Our history", "A story rooted in <em>gratitude</em>",
  "What began in 2017 as one woman’s expression of gratitude has grown into a dedicated network of volunteers, partners, donors, and community members.",
  "team-logo-sign", "humanKIND toronto team members holding a framed humanKIND logo", chip="2017 — today")}

<section class="section">
  <div class="container">
    <div class="timeline">
      <div class="timeline__line" aria-hidden="true"><span class="timeline__progress"></span></div>

      <article class="tl-item">
        <span class="tl-item__dot" aria-hidden="true"></span>
        <div class="tl-item__head"><span class="tl-item__year">2017</span><h2>A beginning rooted in gratitude</h2></div>
        <div class="tl-item__body">
          <div>
            <p>humanKIND toronto was founded in 2017 by Ashifa Champsi with a simple but deeply personal intention: to give back.</p>
            <p>After losing her parents at a young age, Ashifa returned to volunteering as a way of expressing gratitude for the support she had received during her own difficult seasons. What began as a quiet act of service soon grew into something more. She reached out to friends and trusted community members, women who shared a desire to serve, and together they formed a small circle committed to making a meaningful difference in their community.</p>
            <p>Throughout that year, they met with local organizations and community committees across the Greater Toronto Area to understand where support was most needed. In those conversations, they discovered a gap within women’s shelters. Many women and children were arriving from situations of domestic abuse, trauma, and isolation. While essential needs were being addressed, there was also a need for consistent, heart-centered programming that fostered healing, creativity, and connection.</p>
          </div>
        </div>
      </article>

      <article class="tl-item">
        <span class="tl-item__dot" aria-hidden="true"></span>
        <div class="tl-item__head"><span class="tl-item__year">2018</span><h2>The first monthly program</h2></div>
        <div class="tl-item__body">
          <p>In 2018, humanKIND toronto launched its first monthly program at one local shelter.</p>
          <div class="frame">{img("art-hello-love-peace", "Floral wreath paintings reading hello, love and peace from an early art workshop", sizes="(min-width: 900px) 45vw, 90vw")}</div>
        </div>
      </article>

      <article class="tl-item">
        <span class="tl-item__dot" aria-hidden="true"></span>
        <div class="tl-item__head"><span class="tl-item__year">2019</span><h2>Growing with purpose</h2></div>
        <div class="tl-item__body">
          <p>As relationships deepened and trust was built, the work began to expand. What started as one monthly program gradually grew into several. Additional shelters welcomed programming, and the circle of volunteers and supporters widened.</p>
          <div class="frame">{img("meals-team-kitchen", "Volunteers gathered together in a kitchen after preparing a shared meal", sizes="(min-width: 900px) 45vw, 90vw")}</div>
        </div>
      </article>

      <article class="tl-item">
        <span class="tl-item__dot" aria-hidden="true"></span>
        <div class="tl-item__head"><span class="tl-item__year">2020</span><h2>Creativity through crisis</h2></div>
        <div class="tl-item__body">
          <div>
            <p>When the COVID-19 pandemic disrupted in-person programming in 2020, humanKIND toronto faced one of its most defining moments. Rather than pause, the team chose to adapt.</p>
            <p>Virtual workshops were introduced, including online art sessions and creative programming designed to continue supporting women and children remotely. This shift not only allowed the organization to maintain its commitment locally, but also expanded its reach across Ontario. Through virtual delivery, humanKIND toronto was able to offer workshops to shelters outside of Toronto, including all Ontario locations of Sakeenah Canada — something that had not previously been possible.</p>
            <p>During this same period, community support grew significantly. Individuals and small businesses hosted fundraisers, donated proceeds from yoga classes and baked goods, and created handmade items in support of the mission. Social media became a powerful tool for connection and awareness, leading to invitations to share the organization’s story through live online conversations and participation in a documentary feature.</p>
            <p>In place of our annual drives, we launched new initiatives and kept families engaged with kits delivered to shelters:</p>
            <ul class="kits"><li>Feed A Woman. Feed A Child.</li><li>Virtual programs</li><li>Give the Gift of Hope</li><li>Project Lunchbox</li><li>Holiday cookie kits</li><li>Activity kits</li><li>Care kits</li><li>Donating essentials</li></ul>
            <p style="margin-top:1rem"><em>What could have been a season of pause instead became a season of resilience and expansion.</em></p>
          </div>
          <div class="frame">{img("art-eid-virtual", "Eid Mubarak crafts from an art session with Sakeenah Canada", sizes="(min-width: 900px) 45vw, 90vw")}</div>
        </div>
      </article>

      <article class="tl-item">
        <span class="tl-item__dot" aria-hidden="true"></span>
        <div class="tl-item__head"><span class="tl-item__year">2023<small>–present</small></span><h2>A growing circle</h2></div>
        <div class="tl-item__body">
          <div>
            <p>By the end of 2023, humanKIND toronto was delivering multiple programs across shelters in the Greater Toronto Area, creating consistent spaces where women and children could gather, create, reflect, and feel supported. The foundation of the organization was no longer just an idea; it was a growing community.</p>
            <p>In the years that followed, humanKIND toronto continued to grow steadily and intentionally. Today, the organization offers six monthly programs across six shelters in the Greater Toronto Area, while also leading annual drives that provide essential resources to women, children, and youth in need.</p>
            <p>What began in 2017 as one woman’s expression of gratitude has grown into a dedicated network of volunteers, partners, donors, and community members who believe deeply in showing up, consistently and compassionately.</p>
          </div>
          <div class="frame">{img("volunteers-new-circles", "humanKIND toronto volunteers outside a partner organization’s donation centre", sizes="(min-width: 900px) 45vw, 90vw")}</div>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="section section--olive ending on-dark">
  {ripples(animate=True)}
  <div class="container reveal">
    <p>Through every season of growth and challenge, one belief has remained unchanged: the need never stops.</p>
    <p class="final">And neither do we.</p>
    <div class="btn-row" style="justify-content:center">{btn("volunteer.html", "Join Our Circle", "sand")}{btn("donate.html", "Donate", "ghost-light")}</div>
  </div>
</section>
'''
page("our-story.html", "Our Story | humanKIND toronto",
     "From one monthly program in 2018 to six programs across six GTA shelters today: the history of humanKIND toronto, founded in 2017 by Ashifa Champsi.",
     story, story_crumbs, priority="0.8")

# ================================================================= PROGRAMS
prog_crumbs = HOME + [("Programs", "programs.html")]
def program_row(anchor, num, title, text, big, big_alt, small, small_alt, tags=("On-site", "Virtual")):
    pills = "".join(f"<li>{t}</li>" for t in tags)
    return f'''<article class="program-row" id="{anchor}">
  <div class="program-row__media reveal">
    <div class="arch">{img(big, big_alt, sizes="(min-width: 900px) 30vw, 60vw")}</div>
    <div class="circle-img">{img(small, small_alt, sizes="(min-width: 900px) 20vw, 40vw")}</div>
  </div>
  <div class="reveal reveal-delay-1">
    <span class="program-row__num" aria-hidden="true">{num}</span>
    <h2>{title}</h2>
    <p class="lead">{text}</p>
  </div>
</article>'''

programs = f'''
{page_hero(prog_crumbs, "Our programs", "More than <em>activities.</em>",
  "At humanKIND toronto, our programs are created to offer more than just activities. They create moments of healing, connection, and joy.",
  "art-penguins", "Two penguin crafts made from paper rolls during a children’s art session", chip="on-site &amp; virtual")}

<section class="section section--tight">
  <div class="container split split--top">
    <div class="reveal"><p class="eyebrow">How it works</p><h2>Welcoming spaces, <em>month after month.</em></h2></div>
    <div class="reveal reveal-delay-1">
      <p>We partner with shelters across the Greater Toronto Area to provide regular on-site and virtual programs for women and children. Each session is thoughtfully designed to foster self-expression, build confidence, and create a sense of community for those navigating difficult circumstances.</p>
      <p>Whether through creativity, conversation, or shared experiences, our goal is to create welcoming spaces where participants feel supported, valued, and empowered.</p>
      <ul class="program-index" style="--x:0" aria-label="Jump to a program">
        <li><a href="#life-skills" style="border-color:var(--line)">Life Skills</a></li>
        <li><a href="#yoga-cooking" style="border-color:var(--line)">Yoga &amp; Cooking</a></li>
        <li><a href="#art" style="border-color:var(--line)">Art Sessions</a></li>
        <li><a href="#shared-meals" style="border-color:var(--line)">Shared Meals</a></li>
      </ul>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="container">
    {program_row("life-skills", "01", "Life Skills", "Our life skills workshops are designed to provide practical tools that support confidence, independence, and personal growth. These sessions may focus on everyday strategies, goal setting, wellness habits, and meaningful conversations that encourage participants as they rebuild.",
       "lifeskills-workshop", "A facilitator leading a life skills workshop in front of a presentation screen", "lifeskills-strengths", "A workshop handout on identifying individual strengths")}
    {program_row("yoga-cooking", "02", "Yoga &amp; Cooking Workshops", "These sessions offer opportunities for relaxation, nourishment, and self-care. Through gentle yoga classes and interactive cooking demonstrations, participants are invited to slow down, learn new skills, and experience moments of calm and care.",
       "volunteers-yoga", "A woman in a headscarf stretching in a seated yoga pose", "cook-pepper", "A red pepper, fresh herbs and shredded cheese ready for a cooking demo")}
    {program_row("art", "03", "Art Sessions", "Art provides a powerful outlet for healing and self-expression. Our creative workshops give women and children the opportunity to explore, create, and connect in a supportive environment where the process matters more than the outcome.",
       "art-roses", "An acrylic painting of pink roses in a blue vase", "art-bracelets", "Colourful handmade loom band bracelets")}
    {program_row("shared-meals", "04", "Shared Meals", "There is something deeply meaningful about gathering around food. Our shared meal programs bring women and children together in community, offering not just nourishment but connection, conversation, and belonging.",
       "meals-salad", "A large bowl of fresh salad with oranges, tomatoes and red onion", "meals-cookies", "Freshly baked sugar cookies cooling on a rack", tags=("On-site",))}
  </div>
</section>

<section class="section section--sand" aria-labelledby="also">
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">Also in the rotation</p>
      <h2 id="also">Aimed at enhancing well-being <em>in all its forms.</em></h2>
      <p class="lead">Our programming includes yoga &amp; meditation, healthy food demos, social events, artistic expression as well as self-care sessions and life skills training.</p>
    </div>
    <div class="reveal reveal-delay-1" style="display:grid;grid-template-columns:1fr 1fr;gap:16px">
      <div class="arch" style="aspect-ratio:3/4">{img("selfcare-kit", "A self-care kit with bronzer, lip gloss and brushes", sizes="(min-width: 900px) 22vw, 45vw")}</div>
      <div class="arch arch--down" style="aspect-ratio:3/4;margin-top:40px">{img("selfcare-affirmations", "Affirmation cards with messages like Anything is possible", sizes="(min-width: 900px) 22vw, 45vw")}</div>
    </div>
  </div>
</section>

<section class="section section--olive on-dark" aria-labelledby="why-matters">
  {ripples(animate=True)}
  <div class="container container--narrow center reveal">
    <p class="eyebrow">Why it matters</p>
    <h2 id="why-matters">Dignity, encouragement, and <em>moments of hope.</em></h2>
    <p class="lead">Many of the women and children we support are navigating trauma, uncertainty, and isolation.</p>
    <p class="lead">These programs offer more than a service — they offer dignity, encouragement, and moments of hope.</p>
    <div class="btn-row" style="justify-content:center">{btn("donate.html", "Support a Program", "sand")}{btn("volunteer.html", "Volunteer", "ghost-light")}</div>
  </div>
</section>
'''
page("programs.html", "Programs for Women & Children in Shelters | humanKIND toronto",
     "Life skills, yoga and cooking workshops, art sessions and shared meals: humanKIND toronto’s on-site and virtual programs for women and children in GTA shelters.",
     programs, prog_crumbs, priority="0.9")

# ================================================================= ANNUAL DRIVES
drives_crumbs = HOME + [("Annual Drives", "annual-drives.html")]
drives = f'''
{page_hero(drives_crumbs, "Annual drives", "Essentials, <em>all year long.</em>",
  "Thank you to the amazing community for your support. Together, we have been able to organize annual drives in an effort to collect essential items needed most by vulnerable populations in local shelters.",
  "sock-sorting", "Volunteers sitting on the floor sorting hundreds of pairs of donated socks", chip="3 annual drives")}

<section class="section section--tight">
  <div class="container">
    <figure class="quote reveal">
      <span class="quote__mark" aria-hidden="true">“</span>
      <blockquote><p>Individually we are one drop, together we are an ocean.</p></blockquote>
      <figcaption>R. Satoro</figcaption>
    </figure>
  </div>
</section>

<section class="section" style="padding-top:0" aria-label="Our drives">
  <div class="container">
    <div class="cards cards--3">
      <a class="drive-card reveal" href="sock-drive.html"><span class="tag">No more cold feet</span><div class="drive-card__img">{img("sock-kids-box", "Two children dropping donations into a Sox Box", sizes="(min-width: 1000px) 33vw, 100vw")}</div><div class="drive-card__body"><h2 style="font-size:2rem">Sock Drive</h2><p>New socks for children and adults: warmth, comfort, and a small but powerful sense of dignity.</p><span class="text-link">Learn more {icon("arrow")}</span></div></a>
      <a class="drive-card reveal reveal-delay-1" href="project-lunchbox.html"><span class="tag">Project Lunchbox</span><div class="drive-card__img">{img("lunchbox-team", "Three volunteers holding lunch bags, water bottles and snacks for Project Lunchbox", sizes="(min-width: 1000px) 33vw, 100vw")}</div><div class="drive-card__body"><h2 style="font-size:2rem">Project Lunchbox</h2><p>A lunch box, a reusable water bottle, a food container and healthy snacks, packed with care.</p><span class="text-link">Learn more {icon("arrow")}</span></div></a>
      <a class="drive-card reveal reveal-delay-2" href="gift-of-hope.html"><span class="tag">Gift of Hope</span><div class="drive-card__img">{img("hope-carts", "Shopping carts full of new towels and bedding for Gift of Hope boxes", sizes="(min-width: 1000px) 33vw, 100vw")}</div><div class="drive-card__body"><h2 style="font-size:2rem">Gift of Hope</h2><p>Bedding and comfort items to help turn a new space into something that feels like home.</p><span class="text-link">Learn more {icon("arrow")}</span></div></a>
    </div>
  </div>
</section>

<section class="section section--sand" aria-labelledby="partners">
  <div class="container split">
    <div class="reveal" style="display:grid;grid-template-columns:1fr 1fr;gap:16px;align-items:start">
      <div class="arch" style="aspect-ratio:3/4">{img("sock-partner-clinic", "Two women at a local clinic holding a sign for the sock drive collection box", sizes="(min-width: 900px) 22vw, 45vw")}</div>
      <div class="arch arch--down" style="aspect-ratio:3/4;margin-top:50px">{img("sock-partner-office", "People posing beside a Sox Box collection box at a local business", sizes="(min-width: 900px) 22vw, 45vw")}</div>
    </div>
    <div class="reveal reveal-delay-1">
      <p class="eyebrow">Our partners</p>
      <h2 id="partners">Local businesses, <em>giving back.</em></h2>
      <p>Our Community Partners have been an essential part of the success we’ve achieved in collecting items to donate to our local shelters. By partnering with local businesses who have housed collection boxes onsite, not only are we able to encourage more community members to contribute to our seasonal drives, but we are also able to afford local businesses more ways to give back.</p>
      <p>If you would like to get involved by hosting a collection drive on behalf of humanKIND toronto, or participate in an upcoming collection drive as a local business, we’d love to hear from you.</p>
      <div class="btn-row">{btn("contact.html?topic=drive", "Host a Collection Drive")}</div>
    </div>
  </div>
</section>

{cta_band("Turn something small into something <em>meaningful.</em>", "Every pair of socks, every lunchbox, every Gift of Hope box reminds someone that they are seen, supported, and not forgotten.", [btn("contact.html?topic=drive", "Get Involved", "sand"), btn("donate.html", "Donate", "ghost-light")])}
'''
page("annual-drives.html", "Annual Drives: Sock Drive, Project Lunchbox & Gift of Hope | humanKIND toronto",
     "humanKIND toronto’s annual drives collect essentials for women and children in GTA shelters: the Sock Drive, Project Lunchbox and Gift of Hope. Donate, host a drive or partner with us.",
     drives, drives_crumbs, priority="0.8")

# ================================================================= SOCK DRIVE
sock_crumbs = drives_crumbs + [("Sock Drive", "sock-drive.html")]
sock = f'''
{page_hero(sock_crumbs, "Annual drive &middot; No more cold feet", "Sock <em>Drive</em>",
  "It’s one of the most requested and most overlooked essentials.",
  "sock-boy-boxes", "A young donor and a volunteer with two Sox Boxes overflowing with new socks", chip="new socks only")}

<section class="section">
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">Why socks</p>
      <h2>Warmth, comfort, and <em>dignity.</em></h2>
      <p class="lead">For women and children living in shelters, a new pair of socks can mean warmth, comfort, and a small but powerful sense of dignity. Something that is often taken for granted becomes something deeply needed.</p>
      <p>At humanKIND toronto, our annual Sock Drive is rooted in a simple idea: no one should have to go without the basics.</p>
      <p>Each year, our community comes together to collect <strong>new socks for both children and adults</strong>, helping ensure that individuals of all ages have access to something as simple and essential as clean, comfortable socks.</p>
      <p>These small items are delivered with care, reminding every recipient that they are seen, supported, and not forgotten.</p>
    </div>
    <div class="reveal reveal-delay-1">
      <div class="arch" style="aspect-ratio:4/5;max-width:480px;margin-inline:auto">{img("sock-notes", "Handmade notes decorated by children that read I hope these socks keep you warm", sizes="(min-width: 900px) 40vw, 100vw")}</div>
    </div>
  </div>
</section>

<section class="section section--sand" aria-labelledby="sock-help">
  <div class="container split split--top">
    <div class="reveal">
      <p class="eyebrow">How you can help</p>
      <h2 id="sock-help">Individuals, families, <em>and groups.</em></h2>
      <p>Whether you’re an individual, a family, or part of a larger group, there are so many ways to get involved:</p>
      {help_list([("sock", "Donate new socks (children’s and adult sizes)"), ("box", "Organize a collection drive in your school, workplace, or community"), ("hands", "Partner with us to expand our reach")])}
      <div class="btn-row">{btn("contact.html?topic=drive", "Get Involved")}{btn("donate.html", "Donate", "ghost")}</div>
    </div>
    <div class="reveal reveal-delay-1">{packing("What we collect", "The Sox Box", ["New children’s socks", "New adult socks"])}</div>
  </div>
</section>

<section class="section" aria-labelledby="sock-community">
  <div class="container">
    <div class="center reveal" style="margin-bottom:3rem">
      <p class="eyebrow">Our community of support</p>
      <h2 id="sock-community">Showing up <em>year after year.</em></h2>
      <p class="lead">This drive is made possible by the generosity of our partners and supporters who show up year after year.</p>
    </div>
    {gallery([("sock-team-boxes", "Volunteers surrounded by full Sox Box collection boxes"), ("sock-kids-box", "Two children with a Sox Box collection box"), ("sock-foodbank", "Bags of donated socks loaded into a cart beside a community food bank van"), ("sock-partner-clinic", "Partners at a local clinic hosting a sock collection box"), ("sock-sorting", "Volunteers sorting donated socks on the floor"), ("sock-boxes-stack", "A volunteer smiling beside stacked Sox Box collection boxes"), ("sock-partner-office", "People posing beside a Sox Box at a local business"), ("sock-boy-boxes", "A young donor with two boxes of new socks")])}
    <p class="big-serif center reveal" style="margin:3rem auto 0;max-width:26ch">Together, we turn something small into something meaningful. Because comfort matters. Because dignity matters.</p>
  </div>
</section>

{cta_band("Help us keep <em>every foot warm.</em>", "Host a Sox Box at your school, workplace, or business, or donate new socks for children and adults.", [btn("contact.html?topic=drive", "Host a Sox Box", "sand"), btn("annual-drives.html", "All Drives", "ghost-light")])}
'''
page("sock-drive.html", "Sock Drive: New Socks for GTA Shelters | humanKIND toronto",
     "Donate new socks for children and adults living in shelters across the Greater Toronto Area, or host a Sox Box collection drive at your school, workplace or business.",
     sock, sock_crumbs, priority="0.7")

# ================================================================= PROJECT LUNCHBOX
lunch_crumbs = drives_crumbs + [("Project Lunchbox", "project-lunchbox.html")]
lunch = f'''
{page_hero(lunch_crumbs, "Annual drive", "Project <em>Lunchbox</em>",
  "A meal is more than food. It is comfort. It is care. It is consistency in uncertain times.",
  "lunchbox-kit", "A lunch kit with an insulated lunch bag, water bottle, food containers and snacks", chip="packed with care")}

<section class="section">
  <div class="container split split--top">
    <div class="reveal">
      <p class="eyebrow">About the drive</p>
      <h2>Someone thinking of you. <em>Someone showing up for you.</em></h2>
      <p class="lead">Project Lunchbox was created to support women and children in shelters with thoughtfully prepared meal kits and essential food items.</p>
      <p>For many families navigating transition and hardship, access to reliable, nourishing food can make a meaningful difference in their day-to-day lives.</p>
      <p>These are not just items, they are tools that help create routine, stability, and a sense of normalcy, especially for children.</p>
      <p>Each box represents more than nourishment. It represents someone thinking of you. Someone showing up for you.</p>
    </div>
    <div class="reveal reveal-delay-1">{packing("Every lunchbox includes", "Carefully put together with intention and care", ["A lunch box", "A reusable water bottle", "A food container", "A selection of healthy snacks"])}</div>
  </div>
</section>

<section class="section section--sand" aria-labelledby="lunch-help">
  <div class="container split">
    <div class="reveal" style="display:grid;grid-template-columns:1fr 1fr;gap:16px;align-items:end">
      <div class="arch" style="aspect-ratio:3/4">{img("lunchbox-supplies", "Boxes of snacks, lunch bags and water bottles stacked for Project Lunchbox", sizes="(min-width: 900px) 22vw, 45vw")}</div>
      <div class="arch arch--down" style="aspect-ratio:3/4;margin-bottom:-30px">{img("lunchbox-packed", "Packed lunch bags, water bottles and snacks inside a delivery box", sizes="(min-width: 900px) 22vw, 45vw")}</div>
    </div>
    <div class="reveal reveal-delay-1">
      <p class="eyebrow">How you can help</p>
      <h2 id="lunch-help">Pack a little <em>stability.</em></h2>
      {help_list([("gift", "Sponsor a lunchbox"), ("heart", "Support financially to help us expand the program")])}
      <div class="btn-row">{btn("contact.html?topic=sponsor", "Sponsor a Lunchbox")}{btn("donate.html", "Donate", "ghost")}</div>
    </div>
  </div>
</section>

<section class="section section--olive on-dark" aria-labelledby="lunch-why">
  {ripples(animate=True)}
  <div class="container container--narrow center reveal">
    <p class="eyebrow">Why it matters</p>
    <h2 id="lunch-why">In moments of uncertainty, even one dependable meal can bring <em>a sense of stability.</em></h2>
    <p class="lead">Through Project Lunchbox, we are not just providing food — we are offering comfort, dignity, and a reminder that no one is alone.</p>
  </div>
</section>

<section class="section section--tight">
  <div class="container">
    {gallery([("lunchbox-delivery", "Volunteers delivering a cart full of lunch supplies to a shelter"), ("lunchbox-snacks", "A tower of snack boxes donated for Project Lunchbox"), ("lunchbox-team", "Volunteers holding lunch bags and water bottles"), ("lunchbox-kit", "A complete lunch kit with containers and a water bottle")])}
  </div>
</section>
'''
page("project-lunchbox.html", "Project Lunchbox: Meal Kits for Families in Shelters | humanKIND toronto",
     "Project Lunchbox gives women and children in GTA shelters a lunch box, reusable water bottle, food container and healthy snacks. Sponsor a lunchbox or donate to expand the program.",
     lunch, lunch_crumbs, priority="0.7")

# ================================================================= GIFT OF HOPE
hope_crumbs = drives_crumbs + [("Gift of Hope", "gift-of-hope.html")]
hope = f'''
{page_hero(hope_crumbs, "Annual drive", "Gift of <em>Hope</em>",
  "Leaving a shelter is a powerful step, but it can also be uncertain.",
  "hope-because-you-matter", "A Gift of Hope card reading Because you matter, tucked into a colourful envelope", chip="for a fresh start")}

<section class="section">
  <div class="container split split--top">
    <div class="reveal">
      <p class="eyebrow">About the drive</p>
      <h2>So no one leaves <em>empty-handed.</em></h2>
      <p class="lead">For many women and children, transitioning out of a shelter means starting over with very little of their own. Gift of Hope was created to support that moment — to ensure that as they move forward, they don’t leave empty-handed.</p>
      <p>This initiative provides essential bedding and comfort items that individuals can take with them as they begin their next chapter. Items that are theirs to keep. Items that help turn a new space into something that feels like home.</p>
    </div>
    <div class="reveal reveal-delay-1">{packing("Each Gift of Hope box includes", "Theirs to keep", ["A duvet", "A duvet cover", "A pillow", "Pillowcases", "A bath towel", "A bedsheet"])}</div>
  </div>
</section>

<section class="section section--sand-soft" aria-label="More than household items">
  <div class="container center reveal">
    <p class="big-serif" style="max-width:24ch;margin-inline:auto">These are more than household items.</p>
    <p class="lead" style="margin:1.2rem auto 0">They are</p>
    <ul class="affirm__words affirm__words--light" style="margin-top:1rem">
      <li>a sense of ownership.</li>
      <li>a sense of stability.</li>
    </ul>
    <p class="lead" style="margin:2rem auto 0">A small but meaningful foundation for a fresh start.</p>
  </div>
</section>

<section class="section" aria-labelledby="hope-why">
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">Why it matters</p>
      <h2 id="hope-why">Dignity in that <em>moment of change.</em></h2>
      <p>Starting over is not easy. Having something of your own; something new, something chosen with care, can make that transition feel just a little more supported.</p>
      <p>Gift of Hope is about dignity in that moment of change. It’s about sending someone forward with comfort, care, and the reminder that they are not alone.</p>
      <p class="eyebrow" style="margin-top:2rem">How you can help</p>
      {help_list([("gift", "Sponsor a Gift of Hope box"), ("heart", "Contribute financially to support purchasing and distribution")])}
      <div class="btn-row">{btn("contact.html?topic=sponsor", "Sponsor a Box")}{btn("donate.html", "Donate", "ghost")}</div>
    </div>
    <div class="reveal reveal-delay-1" style="display:grid;grid-template-columns:1fr 1fr;gap:16px">
      <div class="arch" style="aspect-ratio:3/4">{img("hope-envelopes", "Handwritten notes reading Hope lives here in coloured envelopes", sizes="(min-width: 900px) 22vw, 45vw")}</div>
      <div class="arch arch--down" style="aspect-ratio:3/4;margin-top:50px">{img("hope-ybh-delivery", "humanKIND volunteers with packed Gift of Hope bags at Yellow Brick House", sizes="(min-width: 900px) 22vw, 45vw")}</div>
    </div>
  </div>
</section>

{cta_band("New beginnings deserve <em>support.</em>", "This initiative is made possible by a community that believes in showing up not just in moments of crisis, but in moments of transition. Because everyone deserves something to call their own.", [btn("contact.html?topic=sponsor", "Sponsor a Box", "sand"), btn("donate.html", "Donate", "ghost-light")])}
'''
page("gift-of-hope.html", "Gift of Hope: Bedding for a Fresh Start | humanKIND toronto",
     "Gift of Hope gives women and children leaving GTA shelters a duvet, duvet cover, pillow, pillowcases, bath towel and bedsheet to keep. Sponsor a box or donate today.",
     hope, hope_crumbs, priority="0.7")

# ================================================================= CREATE FOR A CAUSE
cfac_crumbs = HOME + [("Create for a Cause", "create-for-a-cause.html")]
event_ld = {
    "@context": "https://schema.org", "@type": "Event",
    "name": "Create for a Cause 2026",
    "description": "humanKIND toronto’s annual fundraising event: a creative workshop supporting women and children living in shelters. Venue and ticket details to be announced.",
    "startDate": EVENT_ISO,
    "eventStatus": "https://schema.org/EventScheduled",
    "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
    "location": {"@type": "Place", "name": "Greater Toronto Area (venue to be announced)", "address": {"@type": "PostalAddress", "addressLocality": "Toronto", "addressRegion": "ON", "addressCountry": "CA"}},
    "image": [BASE + "/assets/img/cfac-herb-bowls.webp"],
    "organizer": {"@type": "Organization", "name": "humanKIND toronto", "url": BASE + "/"},
    "url": BASE + "/create-for-a-cause",
}
cfac = f'''
{page_hero(cfac_crumbs, "Annual fundraising event", "Create for <em>a Cause</em>",
  "Create for a Cause is humanKIND toronto’s annual fundraising event — a special opportunity to come together in support of women and children living in shelters while connecting with others through creativity and community.",
  "cfac-candle-workshop", "A candle-making workshop table set with herbs, a candle and a welcome card", chip="Nov 20, 2026")}

<section class="section section--tight" aria-labelledby="std">
  <div class="container">
    <div class="std reveal">
      <div class="std__date" aria-hidden="true"><span class="std__month">Nov</span><span class="std__day">20</span><span class="std__year">2026</span></div>
      <div>
        <p class="eyebrow">Save the date</p>
        <h2 id="std">Our next Create for a Cause event will take place on <em>{EVENT_HUMAN}.</em></h2>
        <p>✨ Stay tuned for more details — we can’t wait to share what’s in store this year.</p>
        <div data-countdown-wrap>
          <ul class="countdown" data-countdown="{EVENT_ISO}T00:00:00-05:00" aria-label="Countdown to Create for a Cause">
            <li><b data-days>–</b><span>Days</span></li>
            <li><b data-hours>–</b><span>Hours</span></li>
            <li><b data-mins>–</b><span>Minutes</span></li>
          </ul>
        </div>
      </div>
      <div class="btn-row" style="margin:0;flex-direction:column">
        {btn(IG, "Stay Updated", extra=' target="_blank" rel="noopener"')}
        {btn("contact.html?topic=event", "Ask a Question", "ghost")}
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split split--top">
    <div class="reveal">
      <p class="eyebrow">What to expect</p>
      <h2>Create, give back, and be part of <em>something bigger.</em></h2>
    </div>
    <div class="reveal reveal-delay-1">
      <p class="lead">Each year, participants gather for an engaging and creative workshop designed to inspire connection, spark generosity, and make a meaningful impact. It is a space where like-minded individuals can create, give back, and be part of something bigger.</p>
      <p>More than a fundraiser, <strong>Create for a Cause</strong> is a celebration of compassion in action — bringing community members together to support healing, dignity, and hope.</p>
      <p>Our annual Create for a Cause fundraiser gives us the opportunity, not only to connect with all of you but also to raise much-needed funding to sustain our programming and do what we do to help those who need it.</p>
      <ul class="years" aria-label="Past and upcoming Create for a Cause events">
        <li><a href="past-events.html#y2019">2019</a></li><li><a href="past-events.html#y2020">2020</a></li><li><a href="past-events.html#y2021">2021</a></li><li><a href="past-events.html#y2022">2022</a></li><li><a href="past-events.html#y2024">2024</a></li><li><a href="past-events.html#y2025">2025</a></li><li class="next">2026</li>
      </ul>
      <div class="btn-row">{btn("past-events.html", "See Past Events", "ghost")}</div>
    </div>
  </div>
</section>

<section class="section section--sand" aria-labelledby="past">
  <div class="container">
    <div class="center reveal" style="margin-bottom:3rem">
      <p class="eyebrow">From past events</p>
      <h2 id="past">Compassion <em>in action</em></h2>
    </div>
    {gallery([("cfac-flatlay", "Craft supplies laid out for a Create for a Cause workshop"), ("cfac-herb-bowls", "Bowls of dried flowers and herbs for blending"), ("cfac-room", "Guests creating together around round tables"), ("cfac-friends", "Three friends taking a selfie at Create for a Cause"), ("cfac-oils", "Guests choosing scents at a table of essential oils"), ("cfac-candle-jar", "A finished hand-poured candle with a handwritten label"), ("cfac-grazing-table", "A grazing table with dips, vegetables and cheese"), ("cfac-create-script", "The word create written in calligraphy")])}
  </div>
</section>

{cta_band("Can’t wait until <em>November?</em>", "Every act of kindness creates a ripple. Support women and children in shelters today.", [btn("donate.html", "Donate", "sand"), btn("volunteer.html", "Volunteer", "ghost-light")])}
'''
page("create-for-a-cause.html", "Create for a Cause 2026 Fundraiser (Nov 20) | humanKIND toronto",
     "Save the date: Create for a Cause, humanKIND toronto’s annual creative workshop fundraiser, returns November 20, 2026, in support of women and children living in GTA shelters.",
     cfac, cfac_crumbs, extra_ld=[event_ld], priority="0.8")

# ================================================================= VOLUNTEER
vol_crumbs = HOME + [("Volunteer", "volunteer.html")]
vol = f'''
{page_hero(vol_crumbs, "Volunteer with us", "Join our <em>circle</em>",
  "humanKIND toronto is powered by volunteers. Whether you have a few hours to give or want to be more deeply involved, there is a place for you here.",
  "volunteers-kitchen", "A group of volunteers smiling in a commercial kitchen while preparing food", chip="all hands welcome")}

<section class="section" aria-labelledby="opps">
  <div class="container">
    <div class="split split--top">
      <div class="reveal"><p class="eyebrow">Volunteer opportunities</p><h2 id="opps">Find your <em>place.</em></h2></div>
      <div class="reveal reveal-delay-1"><p class="lead">From supporting a program to packing a Gift of Hope box, every role helps someone feel seen.</p></div>
    </div>
    <ul class="opps">
      <li class="opp reveal"><span class="opp__num" aria-hidden="true">01</span><h3>Program support</h3><p class="muted" style="margin:6px 0 0">On-site or virtual</p></li>
      <li class="opp reveal reveal-delay-1"><span class="opp__num" aria-hidden="true">02</span><h3>Event and drive coordination</h3></li>
      <li class="opp reveal reveal-delay-2"><span class="opp__num" aria-hidden="true">03</span><h3>Donation sorting and packing</h3></li>
      <li class="opp reveal reveal-delay-3"><span class="opp__num" aria-hidden="true">04</span><h3>Community outreach and fundraising</h3></li>
    </ul>
  </div>
</section>

<section class="section section--olive on-dark" aria-labelledby="why-vol">
  {ripples(animate=True)}
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">Why volunteer?</p>
      <h2 id="why-vol">Real impact, <em>one act of kindness at a time.</em></h2>
      <p class="lead">You’ll be part of a compassionate, driven community working to create real impact — one act of kindness at a time.</p>
      <p>Need volunteer hours? We are happy to provide volunteer hours for eligible opportunities. Please confirm requirements with our team in advance.</p>
      <div class="btn-row">{btn("contact.html?topic=volunteer", "Apply to Volunteer", "sand")}{btn("faq.html", "Read the FAQs", "ghost-light")}</div>
    </div>
    <div class="reveal reveal-delay-1" style="display:grid;grid-template-columns:1fr 1fr;gap:16px;align-items:end">
      <div class="arch" style="aspect-ratio:3/4">{img("volunteers-park", "Volunteers gathered outdoors in a park", sizes="(min-width: 900px) 22vw, 45vw")}</div>
      <div class="arch arch--down" style="aspect-ratio:3/4;margin-bottom:-30px">{img("volunteers-glow", "Volunteers posing in front of a colourful mural at a partner thrift shop", sizes="(min-width: 900px) 22vw, 45vw")}</div>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="container">
    {gallery([("volunteers-mwc", "Volunteers in aprons and matching shirts at a community kitchen"), ("hope-packing", "Volunteers packing Gift of Hope bags"), ("sock-sorting", "Volunteers sorting donated socks"), ("cook-friends", "Two volunteers hugging in a kitchen")])}
  </div>
</section>
'''
page("volunteer.html", "Volunteer in Toronto | humanKIND toronto",
     "Volunteer with humanKIND toronto: program support (on-site or virtual), event and drive coordination, donation sorting and packing, and community outreach across the GTA. Volunteer hours available.",
     vol, vol_crumbs, priority="0.8")

# ================================================================= DONATE
don_crumbs = HOME + [("Donate", "donate.html")]
don = f'''
{page_hero(don_crumbs, "Make a donation", "Give with <em>intention</em>",
  "Every act of kindness creates a ripple.")}

<section class="section">
  <div class="container donate-grid">
    <div class="donate-grid__aside reveal">
      <div class="ripple-stage" aria-hidden="true">{ripples(animate=True)}<div class="ripple-stage__core">every gift creates a ripple</div></div>
      <p class="lead" style="margin-top:1.5rem">When you donate to humanKIND toronto, you are directly supporting women, children, and youth living in shelters across the Greater Toronto Area — individuals who are rebuilding their lives after experiencing abuse, homelessness, and hardship.</p>
      <p class="eyebrow" style="margin-top:1rem">Your support helps us</p>
      {help_list([("spark", "Deliver monthly healing-centered programs"), ("box", "Provide essential items through our annual drives"), ("heart", "Create safe, creative spaces for connection and growth"), ("people", "Expand our reach to more shelters and communities")])}
      <p class="big-serif" style="margin-top:2rem;font-size:clamp(1.6rem,1.3rem + 1vw,2.2rem)">No donation is too small. <em>Every contribution matters.</em></p>
    </div>
    <div class="reveal reveal-delay-1" id="donate-form">
      <div class="donate-frame">
        <div class="donate-frame__bar"><span>{icon("lock")}Secure donation form</span><a class="text-link" href="{DONATE_FORM}" target="_blank" rel="noopener">Open in a new tab {icon("arrow")}</a></div>
        <iframe src="{DONATE_FORM}" title="humanKIND toronto donation form" loading="lazy" allow="payment"></iframe>
      </div>
      <p class="muted" style="font-size:.92rem;margin-top:14px">humanKIND toronto is a registered charity. Charitable Registration Number: {CHARITY_NO}. Having trouble with the form? <a href="{DONATE_FORM}" target="_blank" rel="noopener">Donate on our secure donation page</a> or <a href="contact.html?topic=general">contact us</a>.</p>
    </div>
  </div>
</section>

<section class="section section--sand" aria-labelledby="other-ways">
  <div class="container">
    <div class="center reveal" style="margin-bottom:3rem"><p class="eyebrow">Other ways to give</p><h2 id="other-ways">Give in <em>kind.</em></h2></div>
    <div class="cards cards--3">
      <a class="drive-card reveal" href="project-lunchbox.html"><span class="tag">Sponsor</span><div class="drive-card__img">{img("lunchbox-kit", "A Project Lunchbox kit", sizes="(min-width: 1000px) 33vw, 100vw")}</div><div class="drive-card__body"><h3>Sponsor a lunchbox</h3><p>A lunch box, water bottle, food container and healthy snacks.</p><span class="text-link">Project Lunchbox {icon("arrow")}</span></div></a>
      <a class="drive-card reveal reveal-delay-1" href="gift-of-hope.html"><span class="tag">Sponsor</span><div class="drive-card__img">{img("hope-kitchen-items", "New household items gathered for a Gift of Hope box", sizes="(min-width: 1000px) 33vw, 100vw")}</div><div class="drive-card__body"><h3>Sponsor a Gift of Hope box</h3><p>Bedding and comfort items for someone beginning their next chapter.</p><span class="text-link">Gift of Hope {icon("arrow")}</span></div></a>
      <a class="drive-card reveal reveal-delay-2" href="sock-drive.html"><span class="tag">Collect</span><div class="drive-card__img">{img("sock-boxes-stack", "Stacked Sox Box collection boxes", sizes="(min-width: 1000px) 33vw, 100vw")}</div><div class="drive-card__body"><h3>Host a collection drive</h3><p>Bring a Sox Box to your school, workplace, or community.</p><span class="text-link">Sock Drive {icon("arrow")}</span></div></a>
    </div>
  </div>
</section>
'''
page("donate.html", "Donate | humanKIND toronto",
     "Donate to humanKIND toronto and directly support women, children, and youth living in shelters across the Greater Toronto Area. Registered charity 70047 3002 RC001.",
     don, don_crumbs, priority="0.9")

# ================================================================= FAQ
faq_crumbs = HOME + [("FAQs", "faq.html")]
FAQS = [
    ("Can I receive volunteer hours?", "Yes, we are happy to provide volunteer hours for eligible opportunities. Please confirm requirements with our team in advance."),
    ("Do you accept used clothing?", "At this time, we primarily accept new items to ensure dignity and safety for shelter residents. Occasionally, we may accept gently used items depending on current needs — please contact us before donating."),
    ("Do you accept furniture donations?", "We are unable to accept furniture at this time. However, we can direct you to partner organizations that do."),
    ("What volunteer opportunities are available?", 'We offer a range of opportunities including program support, event coordination, donation drives, and fundraising initiatives. Visit our <a href="volunteer.html">Volunteer page</a> to learn more.'),
    ("How can I get involved?", "You can donate, volunteer, host a fundraiser, or participate in one of our annual drives. Every contribution — big or small — makes a difference."),
    ("Do you work directly with shelters?", "Yes, we partner with shelters across the Greater Toronto Area to deliver programs and provide essential items directly to those in need."),
    ("When is the next fundraiser?", f'Our annual fundraiser, <a href="create-for-a-cause.html">Create for a Cause</a>, takes place on {EVENT_HUMAN}. Stay tuned for more details.'),
]
import re
faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}} for q, a in FAQS]}
faq_items = "".join(
    f'<details class="reveal"{" open" if i == 0 else ""}><summary>{q}<span class="plus" aria-hidden="true"></span></summary><div class="faq__answer"><p>{a}</p></div></details>'
    for i, (q, a) in enumerate(FAQS))
faq = f'''
{page_hero(faq_crumbs, "FAQs", "Frequently asked <em>questions</em>",
  "Everything you need to know about volunteering, donating, and how we work with shelters across the Greater Toronto Area.")}
<section class="section">
  <div class="container container--narrow">
    <div class="faq">{faq_items}</div>
    <div class="center reveal" style="margin-top:3.5rem">
      <p class="big-serif">Still have a question?</p>
      <div class="btn-row" style="justify-content:center">{btn("contact.html", "Contact Us")}{btn("mailto:" + EMAIL, EMAIL, "ghost", arrow=False)}</div>
    </div>
  </div>
</section>
'''
page("faq.html", "FAQs | humanKIND toronto",
     "Answers to common questions about volunteering with humanKIND toronto, volunteer hours, donating new items, furniture and clothing donations, and how we work with GTA shelters.",
     faq, faq_crumbs, extra_ld=[faq_ld], priority="0.6")

# ================================================================= CONTACT
con_crumbs = HOME + [("Contact", "contact.html")]
con = f'''
{page_hero(con_crumbs, "Contact us", "We’d love to <em>hear from you</em>",
  "Whether you’re looking to get involved, partner with us, or simply learn more about our work — we’re here to connect.")}
<section class="section">
  <div class="container contact-grid">
    <div class="reveal">
      <p class="eyebrow">Reach out</p>
      <h2>Let’s connect.</h2>
      <p>For feedback, enquiries, to volunteer your services, or to partner with us, please feel free to reach out here. We endeavour to get back to you within 24 hours.</p>
      <div class="contact-cards">
        <a class="contact-card" href="mailto:{EMAIL}"><span class="help-list__icon">{icon("mail")}</span><span><small>Email</small>{EMAIL}</span></a>
        <a class="contact-card" href="{IG}" target="_blank" rel="noopener"><span class="help-list__icon">{icon("instagram")}</span><span><small>Instagram</small>@humankind_toronto</span></a>
        <a class="contact-card" href="{FB}" target="_blank" rel="noopener"><span class="help-list__icon">{icon("facebook")}</span><span><small>Facebook</small>humankindTO</span></a>
      </div>
    </div>
    <div class="reveal reveal-delay-1">
      <form class="form" id="contact-form" data-to="{EMAIL}" action="mailto:{EMAIL}" method="post" enctype="text/plain" novalidate>
        <div class="form__grid">
          <div class="field"><label for="name">Name</label><input id="name" name="name" type="text" autocomplete="name" required></div>
          <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" required></div>
          <div class="field"><label for="phone">Phone <span style="text-transform:none;letter-spacing:0;font-weight:400">(optional)</span></label><input id="phone" name="phone" type="tel" autocomplete="tel"></div>
          <div class="field"><label for="topic">I’m reaching out about</label>
            <select id="topic" name="topic">
              <option value="general">A general enquiry</option>
              <option value="volunteer">Volunteering</option>
              <option value="partner">Partnering with humanKIND</option>
              <option value="fundraiser">Hosting a fundraiser</option>
              <option value="drive">Hosting a collection drive</option>
              <option value="sponsor">Sponsoring a lunchbox or Gift of Hope box</option>
              <option value="event">Create for a Cause</option>
              <option value="items">Donating items</option>
            </select></div>
          <div class="field form__full"><label for="message">Message</label><textarea id="message" name="message" required></textarea></div>
        </div>
        <div class="btn-row"><button class="btn" type="submit">Send Message {icon("arrow")}</button></div>
        <p class="form__status" role="status" aria-live="polite"></p>
        <p class="form__note">Sending opens your email app with your message ready to go. Prefer to write directly? Email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
      </form>
    </div>
  </div>
</section>
'''
page("contact.html", "Contact | humanKIND toronto",
     "Get in touch with humanKIND toronto to volunteer, partner, host a collection drive, sponsor a lunchbox or Gift of Hope box, or learn more about our work with GTA shelters.",
     con, con_crumbs, priority="0.7")

# ================================================================= PAST EVENTS
past_crumbs = HOME + [("Create for a Cause", "create-for-a-cause.html"), ("Past Events", "past-events.html")]

def year_block(year, title, facts, text, photos):
    facts_html = f'<p class="year__facts">{facts}</p>' if facts else ""
    return f'''<article class="year" id="y{year}">
  <div class="year__head reveal"><span class="year__num">{year}</span><h2>{title}</h2>{facts_html}</div>
  <div class="year__body reveal reveal-delay-1">{text}{gallery(photos, "gallery--year")}</div>
</article>'''

past = f'''
{page_hero(past_crumbs, "Create for a Cause", "Years of <em>creating together</em>",
  "Our annual Create for a Cause fundraiser gives us the opportunity, not only to connect with all of you but also to raise much-needed funding to sustain our programming and do what we do to help those who need it.",
  "past-2024-11", "Four women smiling in front of the humanKIND banner at a Create for a Cause event", chip="2019 to 2025")}

<section class="section section--tight">
  <div class="container">
    <p class="eyebrow">Jump to a year</p>
    <ul class="year-nav" aria-label="Jump to a year">
      <li><a href="#y2025">2025</a></li><li><a href="#y2024">2024</a></li><li><a href="#y2022">2022</a></li><li><a href="#y2021">2021</a></li><li><a href="#y2020">2020</a></li><li><a href="#y2019">2019</a></li>
    </ul>

    {year_block(2025, "Candle-making with Atma Things",
      "Friday, May 30, 2025 &middot; 6:30 to 9:30 pm &middot; Oak Ridges Community Centre",
      "<p class=lead>An evening of compassion, community, and commitment.</p><p>More than just candle-making, this workshop blended mindfulness, creativity, and community. Led by Jessie Arora of Atma Things, guests were invited to set their intentions, pour their own soy candle, and customize it with essential oils, herbs, and crystals.</p><p>Proceeds from the fundraiser allow us to continue the work we do to provide programs and support to vulnerable women and children residing in local shelters.</p>",
      [("past-2025-00", "Poster for the 2025 Create for a Cause fundraiser: a handmade candle workshop with Jessie Arora of Atma Things on Friday, May 30, 6:30 to 9:30 pm")])}

    {year_block(2024, "Clay coasters by Lake Wilcox",
      "Oak Ridges Community Centre, overlooking Lake Wilcox",
      "<p>The 2024 Create for a Cause fundraiser was held at the stunning Oak Ridges Community Centre overlooking the serene Lake Wilcox. This picturesque setting provided the perfect backdrop for an evening dedicated to creativity, connection, and community.</p><p>The event featured a hands-on workshop led by team member Salma, where participants crafted beautiful sets of clay coasters. Following the workshop, guests enjoyed a delicious dinner, dessert, and time to socialize in a warm and welcoming atmosphere.</p><p>We extend our heartfelt gratitude to everyone who participated. It was a wonderful evening of bringing together like-minded women while supporting a meaningful cause!</p>",
      [("past-2024-01", "Four women smiling together outdoors at the 2024 event"), ("past-2024-02", "Guests seated at tables beside large windows with a view of trees"), ("past-2024-03", "Women working on crafts around a decorated table"), ("past-2024-07", "A handmade marbled clay coaster"), ("past-2024-09", "Guests serving themselves dinner from trays of food"), ("past-2024-11", "Four women in front of the humanKIND banner")])}

    {year_block(2022, "Moon Magic Candle workshop",
      "With Jessie Arora of Atma Things",
      "<p>For our Create for a Cause fundraiser, we enlisted the help of Jessie Arora of Atma Things to conduct her Moon Magic Candle workshop, and it was a magical night indeed!</p><p>It was a truly beautiful evening, with an amazing group of women coming together with creativity and intention.</p><p>Not only did we have the chance to reconnect with all of you, but we raised awareness and the funding needed to continue offering our programs and initiatives.</p>",
      [("past-2022-00", "A candle workshop room set with long tables and string lights"), ("past-2022-03", "A grazing table with dips, vegetables and cheese"), ("past-2022-05", "Bowls of dried herbs and flowers for candle blending"), ("past-2022-08", "Guests gathered around a table of essential oils"), ("past-2022-10", "Four women smiling together in front of the humanKIND banner"), ("past-2022-11", "A finished hand-poured candle in a glass jar with a handwritten label")])}

    {year_block(2021, "A second year, virtually",
      "Virtual workshops",
      "<p>It was virtual programming for a second year, and while we wanted more than anything to get back to our in-person events, we still managed to put together a wonderfully informative and entertaining series of workshops, hosted by some incredibly talented instructors. We had a blast working alongside you all to quite literally &ldquo;Create for a Cause&rdquo;!</p><p>This year&rsquo;s programming included a heart-pumping workout and meditative cool down, a calligraphy workshop, a hands-on cooking class, as well as a crafting class for kids as a special treat for Mother&rsquo;s Day.</p>",
      [("past-2021-02", "A woman in a deep lunge on a yoga mat holding a kettlebell"), ("past-2021-03", "A faux calligraphy worksheet with a pen"), ("past-2021-04", "Small homemade pizzas with colourful toppings"), ("past-2021-05", "A candle beside a handmade paper flower craft")])}

    {year_block(2020, "Create for a Cause, online edition",
      "A 4-week series of virtual workshops",
      "<p>2020. The year of the Zoom call. The birth of Create for a Cause, Online Edition!</p><p>COVID couldn&rsquo;t stop us from putting on our annual fundraiser. Not only did we get creative, but we got the help of some talented creatives to put on a 4-week series of workshops to get you doodling, cooking, moving, and making!</p><p>While we certainly missed meeting our friends and supporters at our event, we couldn&rsquo;t have been happier with the incredible round-up of talent and enthusiastic participants in attendance for our series of virtual workshops in 2020.</p>",
      [("past-2020-02", "A hand-drawn floral design around the humanKIND logo"), ("past-2020-03", "Home-cooked dishes on plates and in a skillet"), ("past-2020-04", "A floor cushion and candle on a patterned rug"), ("past-2020-05", "Yarn, paper cutouts and craft supplies laid out on a table")])}

    {year_block(2019, "Our first fundraiser",
      "Joined by Motives Art Co. and Sandgate Women&rsquo;s Shelter",
      "<p>Our first ever fundraiser, an engaging night of great art, food and company, all for a worthy cause!</p><p>Joined by Motives Art Co., Sandgate Women&rsquo;s Shelter and a full house of amazing women, we had a fabulous time creating unique abstract pieces, connecting with friends, old and new, and raising awareness about issues affecting women in our communities.</p>",
      [("past-2019-02", "Five women smiling together at the first Create for a Cause"), ("past-2019-04", "Paint palettes and colourful abstract paintings in progress"), ("past-2019-05", "Women seated around a long table during the painting workshop"), ("past-2019-03", "The word create written in calligraphy")])}
  </div>
</section>

{cta_band("The next one is <em>November 20.</em>", "Join us for Create for a Cause 2026, or support women and children in shelters today.", [btn("create-for-a-cause.html", "Event Details", "sand"), btn("donate.html", "Donate", "ghost-light")])}
'''
page("past-events.html", "Past Create for a Cause Events, 2019 to 2025 | humanKIND toronto",
     "A look back at humanKIND toronto’s annual Create for a Cause fundraiser from the first art night in 2019 to the 2025 candle workshop, including our virtual years.",
     past, past_crumbs, priority="0.6")

# ================================================================= HOST A FUNDRAISER
host_crumbs = HOME + [("Get Involved", "volunteer.html"), ("Host a Fundraiser", "host-a-fundraiser.html")]
host = f'''
{page_hero(host_crumbs, "Get involved", "Host a <em>fundraiser</em>",
  "From yoga classes and art workshops to bake sales and handcrafted goods, our community continues to find beautiful, creative ways to give back.",
  "volunteers-tiedye", "A smiling volunteer holding up a hand-dyed pouch she made", chip="your idea, your way")}

<section class="section" aria-labelledby="ideas">
  <div class="container">
    <div class="split split--top">
      <div class="reveal"><p class="eyebrow">Ideas from our community</p><h2 id="ideas">Kindness is <em>contagious.</em></h2></div>
      <div class="reveal reveal-delay-1"><p class="lead">Individuals and small businesses have hosted fundraisers, donated proceeds from yoga classes and baked goods, and created handmade items in support of our mission.</p></div>
    </div>
    <ul class="opps">
      <li class="opp reveal"><span class="opp__num" aria-hidden="true">01</span><h3>Yoga &amp; fitness classes</h3><p class="muted" style="margin:6px 0 0">Donate the proceeds from a class.</p></li>
      <li class="opp reveal reveal-delay-1"><span class="opp__num" aria-hidden="true">02</span><h3>Bake sales</h3><p class="muted" style="margin:6px 0 0">Share baked goods and donate what you raise.</p></li>
      <li class="opp reveal reveal-delay-2"><span class="opp__num" aria-hidden="true">03</span><h3>Handmade goods</h3><p class="muted" style="margin:6px 0 0">Create handmade items in support of the mission.</p></li>
      <li class="opp reveal reveal-delay-3"><span class="opp__num" aria-hidden="true">04</span><h3>Art workshops</h3><p class="muted" style="margin:6px 0 0">Bring people together to create for a cause.</p></li>
    </ul>
  </div>
</section>

<section class="section section--sand" aria-labelledby="host-collect">
  <div class="container split">
    <div class="reveal" style="display:grid;grid-template-columns:1fr 1fr;gap:16px;align-items:end">
      <div class="arch" style="aspect-ratio:3/4">{img("volunteers-yoga", "A woman in a headscarf stretching in a seated yoga pose", sizes="(min-width: 900px) 22vw, 45vw")}</div>
      <div class="arch arch--down" style="aspect-ratio:3/4;margin-bottom:-30px">{img("sock-boxes-stack", "A volunteer smiling beside stacked Sox Box collection boxes", sizes="(min-width: 900px) 22vw, 45vw")}</div>
    </div>
    <div class="reveal reveal-delay-1">
      <p class="eyebrow">Prefer to collect?</p>
      <h2 id="host-collect">Host a <em>collection drive.</em></h2>
      <p>You can also organize a collection drive in your school, workplace, or community for our <a href="sock-drive.html">Sock Drive</a>.</p>
      {btn("annual-drives.html", "See the Annual Drives", "ghost")}
    </div>
  </div>
</section>

{cta_band("Tell us what you have <em>in mind.</em>", "We endeavour to get back to you within 24 hours.", [btn("contact.html?topic=fundraiser", "Plan a Fundraiser", "sand"), btn("donate.html", "Donate Instead", "ghost-light")])}
'''
page("host-a-fundraiser.html", "Host a Fundraiser for Women & Children in Shelters | humanKIND toronto",
     "Host your own fundraiser for humanKIND toronto: a yoga class, bake sale, handmade goods, art workshop or a collection drive at your school, workplace or community.",
     host, host_crumbs, priority="0.7")

# ================================================================= PARTNER WITH US
partner_crumbs = HOME + [("Get Involved", "volunteer.html"), ("Partner With Us", "partner-with-us.html")]
partner = f'''
{page_hero(partner_crumbs, "For local businesses", "Partner <em>with us</em>",
  "Our community partners have been an essential part of the success we’ve achieved in collecting items to donate to our local shelters.",
  "sock-partner-office", "People posing beside a Sox Box collection box at a local business", chip="giving back, together")}

<section class="section" aria-labelledby="partner-ways">
  <div class="container">
    <div class="split split--top">
      <div class="reveal"><p class="eyebrow">Ways to partner</p><h2 id="partner-ways">More ways for your business to <em>give back.</em></h2></div>
      <div class="reveal reveal-delay-1"><p class="lead">By partnering with local businesses who house collection boxes onsite, we encourage more community members to contribute to our seasonal drives, and give local businesses more ways to give back.</p></div>
    </div>
    <ul class="opps">
      <li class="opp reveal"><span class="opp__num" aria-hidden="true">01</span><h3>House a collection box</h3><p class="muted" style="margin:6px 0 0">Host a Sox Box or drive box at your business.</p></li>
      <li class="opp reveal reveal-delay-1"><span class="opp__num" aria-hidden="true">02</span><h3>Sponsor a box</h3><p class="muted" style="margin:6px 0 0">Sponsor a lunchbox or a Gift of Hope box.</p></li>
    </ul>
  </div>
</section>

<section class="section section--sand" aria-labelledby="partner-seen">
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">What it looks like</p>
      <h2 id="partner-seen">Small boxes, <em>big community.</em></h2>
      <p>This is a collection box at a local business, one of the places in our community where neighbours drop off new socks for women and children in shelters.</p>
      <div class="btn-row">{btn("sock-drive.html", "About the Sock Drive", "ghost")}{btn("contact.html?topic=partner", "Get in Touch")}</div>
    </div>
    <div class="reveal reveal-delay-1" style="display:grid;grid-template-columns:1fr 1fr;gap:16px;align-items:start">
      <div class="arch" style="aspect-ratio:3/4">{img("sock-partner-clinic", "Two women at a local clinic holding a sign for the sock drive collection box", sizes="(min-width: 900px) 22vw, 45vw")}</div>
      <div class="arch arch--down" style="aspect-ratio:3/4;margin-top:50px">{img("sock-boxes-stack", "A volunteer smiling beside stacked Sox Box collection boxes", sizes="(min-width: 900px) 22vw, 45vw")}</div>
    </div>
  </div>
</section>

{cta_band("Let’s do something <em>good together.</em>", "If you would like to participate in an upcoming collection drive as a local business, reach out.", [btn("contact.html?topic=partner", "Partner With Us", "sand"), btn("annual-drives.html", "Annual Drives", "ghost-light")])}
'''
page("partner-with-us.html", "Partner With Us: Local Businesses | humanKIND toronto",
     "Local businesses can partner with humanKIND toronto by housing a collection box onsite or sponsoring a lunchbox or Gift of Hope box, giving the community more ways to give back.",
     partner, partner_crumbs, priority="0.6")

# ================================================================= PRIVACY
UPDATED = "October 1, 2026"
priv_crumbs = HOME + [("Privacy", "privacy.html")]
priv = f'''
{page_hero(priv_crumbs, "Legal", "Privacy <em>policy</em>", "How this website handles your information. Last updated: " + UPDATED + ".")}
<section class="section">
  <div class="container container--narrow prose">
    <h2>Who we are</h2>
    <p>humanKIND toronto is a volunteer-led nonprofit and registered charity serving the Greater Toronto Area (Charitable Registration Number {CHARITY_NO}). You can reach us at <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

    <h2>What this website collects</h2>
    <p>This website does not use analytics, advertising trackers, or tracking cookies of its own, and it doesn&rsquo;t ask you to create an account.</p>

    <h2>Contact form and email</h2>
    <p>The contact form on this website doesn&rsquo;t send your message to a server. It opens your own email app with the message filled in. When you press send, your email reaches our inbox at {EMAIL}. We use the details you give us only to respond to your enquiry or follow up on your offer to help.</p>

    <h2>Donations</h2>
    <p>Donations are made through a secure donation form provided by a third-party platform. It is embedded on our <a href="donate.html">Donate page</a> and also available at its own web address. When you donate, you enter your payment and contact details directly with that provider. This website does not see or store your payment details, and the provider&rsquo;s own privacy practices apply to that form.</p>

    <h2>Hosting and other services</h2>
    <p>This site is hosted by Cloudflare, which processes technical information such as your IP address in order to deliver pages and keep the site secure. Fonts are loaded from Google Fonts, so your browser contacts Google to download them. Our links to Instagram and Facebook take you to those services, which have their own privacy policies.</p>

    <h2>Your choices</h2>
    <p>You can ask us what information we hold about you, or ask us to correct or delete it, by emailing <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

    <h2>Changes to this policy</h2>
    <p>If how this website works changes, for example if we add a newsletter or analytics, we will update this page and the date above.</p>
  </div>
</section>
'''
page("privacy.html", "Privacy Policy | humanKIND toronto",
     "How the humanKIND toronto website handles your information: the site itself uses no analytics or tracking cookies, how the contact form and donation form work, and who to ask about your information.",
     priv, priv_crumbs, priority="0.3")

# ================================================================= ACCESSIBILITY
acc_crumbs = HOME + [("Accessibility", "accessibility.html")]
acc = f'''
{page_hero(acc_crumbs, "Legal", "Accessibility <em>statement</em>", "We want everyone to be able to use this website. Last updated: " + UPDATED + ".")}
<section class="section">
  <div class="container container--narrow prose">
    <h2>Our aim</h2>
    <p>We want this website to work for people who use screen readers, keyboards, voice control or screen magnifiers. We are working toward meeting the Web Content Accessibility Guidelines (WCAG) 2.1 Level AA.</p>

    <h2>What we&rsquo;ve built in</h2>
    <ul>
      <li>A &ldquo;Skip to content&rdquo; link at the top of every page.</li>
      <li>Menus, accordions and flip cards you can operate with a keyboard, with a visible focus outline.</li>
      <li>Descriptive alternative text on photos.</li>
      <li>A layout that adapts from phones to large screens.</li>
      <li>Animation that switches off if your device is set to reduce motion.</li>
    </ul>

    <h2>Where we may fall short</h2>
    <p>We haven&rsquo;t yet had an independent accessibility audit, so there may be problems we haven&rsquo;t found. The donation form on our Donate page is provided by a third party and we can&rsquo;t change how it works. If you have trouble using it, email us and we&rsquo;ll do our best to help.</p>

    <h2>Tell us what&rsquo;s not working</h2>
    <p>If you run into a barrier on this website, please email <a href="mailto:{EMAIL}">{EMAIL}</a> and tell us the page and what happened. We endeavour to get back to you within 24 hours.</p>
  </div>
</section>
'''
page("accessibility.html", "Accessibility Statement | humanKIND toronto",
     "Our commitment to an accessible humanKIND toronto website: what we’ve built in, where we may fall short, and how to report a problem.",
     acc, acc_crumbs, priority="0.3")

# ================================================================= 404
nf = f'''
<section class="section notfound">
  <div class="container center">
    <p class="notfound__num">404</p>
    <h1 style="font-size:clamp(2.2rem,1.6rem + 3vw,4rem)">This page has wandered off.</h1>
    <p class="lead">But kindness is never far away.</p>
    <div class="btn-row" style="justify-content:center">{btn("index.html", "Back Home")}{btn("contact.html", "Contact Us", "ghost")}</div>
  </div>
</section>'''
page("404.html", "Page Not Found | humanKIND toronto", "The page you were looking for could not be found.", nf, robots="noindex, follow", in_sitemap=False)

# ================================================================= sitemap / robots / redirects
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for url, pr in PAGES:
    sm.append(f"  <url><loc>{url}</loc><lastmod>{LASTMOD}</lastmod><priority>{pr}</priority></url>")
sm.append("</urlset>")
open(os.path.join(SITE, "sitemap.xml"), "w").write("\n".join(sm) + "\n")
open(os.path.join(SITE, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
open(os.path.join(SITE, "_redirects"), "w").write("""# 301s from old Squarespace URLs that were renamed (Netlify / Cloudflare Pages format).
# /about, /annual-drives, /contact and /donate keep the same path, so they need no rule.
# The old per-year pages (/fundraising/create-for-a-cause-2025 etc.) all land on the Past Events page.
/on-site                   /programs             301
/fundraising               /past-events          301
/fundraising/*             /past-events          301
/create-for-a-cause-2026   /create-for-a-cause   301
/covid19-1                 /our-story            301
/annual-drives/no-more-cold-feet-sock-drive   /sock-drive         301
/annual-drives/give-the-gift-of-hope           /gift-of-hope       301
/annual-drives/project-backpack-summer         /project-lunchbox   301
/recipes                   /programs             301
""")
print("built", len(PAGES) + 1, "pages")
