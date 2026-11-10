#!/usr/bin/env python3
"""Split the portfolio into a multipage static site."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = (ROOT / "site-source" / "full.html").read_text(encoding="utf-8")

NAV = [
    ("solutions/", "Solutions"),
    ("platforms/", "Platforms"),
    ("capabilities/", "Capabilities"),
    ("work/", "Work"),
    ("process/", "Process"),
    ("about/", "About"),
]


def extract(start_marker: str, end_marker: str) -> str:
    start = SRC.index(start_marker)
    end = SRC.index(end_marker, start)
    return SRC[start:end].rstrip() + "\n"


def rewrite_paths(html: str, prefix: str) -> str:
    """Prefix root-relative asset and page links for nested pages."""
    if not prefix:
        return html

    def asset(m: re.Match) -> str:
        return f'{m.group(1)}{prefix}assets/'

    html = re.sub(r'((?:src|href)=")assets/', asset, html)

    # Solution experience links that currently look like automation/...
    for cat in ("automation", "engineering", "commerce", "systems"):
        html = html.replace(f'href="{cat}/', f'href="{prefix}{cat}/')
        html = html.replace(f"href='{cat}/", f"href='{prefix}{cat}/")

    return html


def head(title: str, description: str, prefix: str, body_class: str = "") -> str:
    bc = f' class="{body_class}"' if body_class else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Public+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet" />
  <link rel="icon" href="{prefix}assets/favicon.svg?v=2" type="image/svg+xml" />
  <link rel="icon" href="{prefix}assets/favicon.ico?v=2" sizes="any" />
  <link rel="icon" href="{prefix}assets/favicon-32.webp?v=2" type="image/webp" sizes="32x32" />
  <link rel="apple-touch-icon" href="{prefix}assets/apple-touch-icon.webp?v=2" />
  <link rel="stylesheet" href="{prefix}styles.css" />
  <link rel="stylesheet" href="{prefix}experience.css" />
</head>
<body{bc}>
  <a class="skip-link" href="#main">Skip to content</a>
  <div class="progress" aria-hidden="true"><div class="progress__fill" id="progress-fill"></div></div>
  <div class="progress-radial" aria-hidden="true">
    <svg viewBox="0 0 36 36">
      <circle class="progress-radial__track" cx="18" cy="18" r="15.5" />
      <circle class="progress-radial__value" id="progress-radial" cx="18" cy="18" r="15.5" />
    </svg>
  </div>
"""


def home_href(prefix: str) -> str:
    return prefix if prefix else "./"


def header(prefix: str, active: str | None = None) -> str:
    home = home_href(prefix)
    links = []
    mobile = []
    for href, label in NAV:
        key = href.rstrip("/")
        cls = ' class="is-active"' if active == key else ""
        links.append(f'        <a href="{prefix}{href}"{cls}>{label}</a>')
        mobile.append(f'      <a href="{prefix}{href}"{cls}>{label}</a>')
    return f"""  <header class="site-header" id="top">
    <div class="header-inner">
      <a class="logo" href="{home}" aria-label="LoveThisLife home">
        <span class="logo-word">Love<span>This</span>Life</span>
      </a>
      <nav class="nav" aria-label="Primary">
{chr(10).join(links)}
      </nav>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="mobile-nav" aria-label="Open menu">
        <span></span><span></span>
      </button>
    </div>
    <nav class="mobile-nav" id="mobile-nav" hidden>
{chr(10).join(mobile)}
    </nav>
  </header>
"""


def footer(prefix: str) -> str:
    home = home_href(prefix)
    return f"""  <footer class="site-footer">
    <div class="container footer-main">
      <div class="footer-col footer-col--brand">
        <a class="footer-logo" href="{home}" aria-label="LoveThisLife home">
          <span class="logo-word logo-word--footer">Love<span>This</span>Life</span>
        </a>
        <p class="footer-desc">A Los Angeles IT studio for AI, full-stack engineering, ecommerce, and business systems—built with agency polish and engineering depth.</p>
        <p class="footer-location">Los Angeles, California</p>
      </div>
      <div class="footer-col">
        <h4 class="footer-heading">Explore</h4>
        <nav class="footer-links" aria-label="Site pages">
          <a href="{home}">Home</a>
          <a href="{prefix}solutions/">Solutions</a>
          <a href="{prefix}platforms/">Platforms</a>
          <a href="{prefix}capabilities/">Capabilities</a>
          <a href="{prefix}work/">Work</a>
          <a href="{prefix}process/">Process</a>
          <a href="{prefix}about/">About</a>
        </nav>
      </div>
      <div class="footer-col">
        <h4 class="footer-heading">Capabilities</h4>
        <ul class="footer-list">
          <li>AI Agents &amp; Automation</li>
          <li>Full Stack &amp; Mobile</li>
          <li>Shopify &amp; Ecommerce</li>
          <li>Odoo &amp; ERP Systems</li>
          <li>Python &amp; Integrations</li>
        </ul>
      </div>
      <div class="footer-col">
        <h4 class="footer-heading">Studio</h4>
        <p class="footer-founder"><strong>Christina Jaramillo</strong><span>Founder &amp; Lead Engineer</span></p>
        <ul class="footer-list footer-list--compact">
          <li>Production systems, not demos</li>
          <li>End-to-end delivery &amp; handoff</li>
          <li>Startups &amp; established teams</li>
        </ul>
      </div>
    </div>
    <div class="footer-bar">
      <div class="container footer-bar__inner">
        <p>© <span id="year"></span> Christina Jaramillo · LoveThisLife</p>
        <a class="footer-top-link" href="#top">Back to top ↑</a>
      </div>
    </div>
  </footer>

  <script src="{prefix}script.js"></script>
</body>
</html>
"""


def page_banner(kicker: str, title: str, lede: str) -> str:
    return f"""    <header class="page-banner">
      <div class="container">
        <p class="eyebrow">{kicker}</p>
        <h1 class="page-banner__title">{title}</h1>
        <p class="page-banner__lede">{lede}</p>
      </div>
    </header>
"""


def write_page(relpath: str, content: str) -> None:
    out = ROOT / relpath
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content, encoding="utf-8")
    print(f"wrote {relpath}")


def main() -> None:
    hero = extract('<section class="hero"', '<div class="part-divider" aria-hidden="true">\n      <span class="part-divider__num">01</span>')
    intro = extract(
        '<div class="part-divider" aria-hidden="true">\n      <span class="part-divider__num">01</span>',
        '<div class="part-divider" aria-hidden="true">\n      <span class="part-divider__num">02</span>',
    )
    pillars = extract(
        '<div class="part-divider" aria-hidden="true">\n      <span class="part-divider__num">02</span>',
        '<div class="part-divider part-divider--dark" aria-hidden="true">\n      <span class="part-divider__num">03</span>',
    )
    solutions = extract(
        '<div class="part-divider part-divider--dark" aria-hidden="true">\n      <span class="part-divider__num">03</span>',
        '<div class="part-divider part-divider--ink" aria-hidden="true">\n      <span class="part-divider__num">04</span>',
    )
    platforms = extract(
        '<div class="part-divider part-divider--ink" aria-hidden="true">\n      <span class="part-divider__num">04</span>',
        '<div class="part-divider" aria-hidden="true">\n      <span class="part-divider__num">05</span>',
    )
    skills = extract(
        '<div class="part-divider" aria-hidden="true">\n      <span class="part-divider__num">05</span>',
        '<div class="part-divider" aria-hidden="true">\n      <span class="part-divider__num">06</span>',
    )
    work = extract(
        '<div class="part-divider" aria-hidden="true">\n      <span class="part-divider__num">06</span>',
        '<div class="part-divider part-divider--dark" aria-hidden="true">\n      <span class="part-divider__num">07</span>',
    )
    process = extract(
        '<div class="part-divider part-divider--dark" aria-hidden="true">\n      <span class="part-divider__num">07</span>',
        '<div class="part-divider" aria-hidden="true">\n      <span class="part-divider__num">08</span>',
    )
    about = extract(
        '<div class="part-divider" aria-hidden="true">\n      <span class="part-divider__num">08</span>',
        "  </main>",
    )

    home_cta = """
    <section class="home-gate section">
      <div class="container home-gate__grid">
        <a class="home-gate__card reveal" href="solutions/">
          <span class="home-gate__num">01</span>
          <h2>Solutions</h2>
          <p>Twelve offerings—AI, engineering, commerce, and business systems.</p>
          <span class="home-gate__go">Explore →</span>
        </a>
        <a class="home-gate__card reveal" href="work/">
          <span class="home-gate__num">02</span>
          <h2>Selected work</h2>
          <p>Case studies with outcomes, stacks, and product surfaces.</p>
          <span class="home-gate__go">View work →</span>
        </a>
        <a class="home-gate__card reveal" href="about/">
          <span class="home-gate__num">03</span>
          <h2>About</h2>
          <p>Christina Jaramillo · LoveThisLife · Los Angeles.</p>
          <span class="home-gate__go">Meet Christina →</span>
        </a>
      </div>
    </section>
"""

    # HOME
    write_page(
        "index.html",
        head(
            "Christina Jaramillo — LoveThisLife | AI, Full Stack & Business Systems · Los Angeles",
            "Christina Jaramillo of LoveThisLife builds AI automation, full-stack web and mobile apps, ecommerce, Odoo ERP, Bubble, and Python business systems in Los Angeles.",
            "",
            "page-home",
        )
        + header("", None)
        + "  <main id=\"main\">\n"
        + hero
        + intro
        + pillars
        + home_cta
        + "  </main>\n\n"
        + footer(""),
    )

    pages = [
        (
            "solutions/index.html",
            "solutions",
            "Solutions — LoveThisLife",
            "Twelve offerings across AI, engineering, commerce, and business systems from LoveThisLife.",
            "Solutions &amp; services",
            "What I build for teams",
            "Click any offering to open its experience gallery with product samples.",
            solutions,
            True,
        ),
        (
            "platforms/index.html",
            "platforms",
            "Platforms — LoveThisLife",
            "Technology platforms LoveThisLife works in every week—Shopify, Odoo, React, Power BI, and more.",
            "Technology stack",
            "Platforms I work in every week",
            "The tools behind production systems—commerce, AI, ERP, and engineering.",
            platforms,
            False,
        ),
        (
            "capabilities/index.html",
            "capabilities",
            "Capabilities — LoveThisLife",
            "Skills organized by domain: intelligence, engineering, commerce, and business systems.",
            "Capabilities",
            "Skills organized by domain",
            "Four clear practice areas—each with the skills that belong together.",
            skills,
            False,
        ),
        (
            "work/index.html",
            "work",
            "Work — LoveThisLife",
            "Selected case studies from LoveThisLife—AI, full stack, ecommerce, and business systems.",
            "Selected work",
            "What I've shipped",
            "Compact case studies—real product UIs, outcome first, stack second.",
            work,
            False,
        ),
        (
            "process/index.html",
            "process",
            "Process — LoveThisLife",
            "How LoveThisLife delivers—from discover and design to build and handoff.",
            "How I work",
            "From brief to production",
            "A refined delivery rhythm—four stages, zero guesswork.",
            process,
            False,
        ),
        (
            "about/index.html",
            "about",
            "About — Christina Jaramillo · LoveThisLife",
            "Christina Jaramillo, founder of LoveThisLife in Los Angeles—AI, full stack, ecommerce, and business systems.",
            "About",
            "Christina Jaramillo",
            "Founder, LoveThisLife · Los Angeles",
            about,
            False,
        ),
    ]

    for rel, active, title, desc, kicker, banner_title, lede, body, strip_intro in pages:
        prefix = "../"
        body_html = rewrite_paths(body, prefix)
        if strip_intro:
            # Drop the dark part-divider + section intro eyebrow/title that page-banner replaces for solutions,
            # but keep the solutions flow. For solutions we keep the section but remove duplicate heading block.
            body_html = re.sub(
                r'<div class="part-divider[^"]*"[^>]*>.*?</div>\s*',
                "",
                body_html,
                count=1,
                flags=re.S,
            )
            body_html = re.sub(
                r'<div class="solutions-intro reveal">.*?</div>\s*',
                "",
                body_html,
                count=1,
                flags=re.S,
            )
        else:
            body_html = re.sub(
                r'<div class="part-divider[^"]*"[^>]*>.*?</div>\s*',
                "",
                body_html,
                count=1,
                flags=re.S,
            )
            # Soften duplicate page titles inside sections (keep section content)
            body_html = re.sub(
                r'<p class="eyebrow[^"]*"[^>]*>.*?</p>\s*<h2[^>]*>.*?</h2>\s*(?:<p class="section-lede[^"]*"[^>]*>.*?</p>\s*)?',
                "",
                body_html,
                count=1,
                flags=re.S,
            )
            body_html = re.sub(
                r'<div class="container platforms-head reveal">\s*</div>\s*',
                "",
                body_html,
                flags=re.S,
            )

        content = (
            head(title, desc, prefix, f"page-inner page-{active}")
            + header(prefix, active)
            + '  <main id="main" class="page-main">\n'
            + page_banner(kicker, banner_title, lede)
            + body_html
            + "  </main>\n\n"
            + footer(prefix)
        )
        write_page(rel, content)

    import build_experience_pages as xp

    xp.main()


if __name__ == "__main__":
    main()
