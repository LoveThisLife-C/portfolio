#!/usr/bin/env python3
"""Generate experience sample pages for each solution."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent

PAGES = [
    {
        "path": "automation/experience",
        "category": "Automation",
        "category_slug": "automation",
        "title": "AI Agents & Assistants",
        "slug": "ai-agents",
        "tag": "AI & Automation",
        "lede": "Custom agents for research, support, and multi-step tasks—with guardrails and human handoff. Product surfaces from live agent consoles to approval queues.",
        "stack": ["OpenAI", "Claude", "GHL AI", "RAG", "Voice AI"],
        "samples": [
            ("Agent console", "Skill focus: LLM tool-calling, streaming chat UI, citation grounding."),
            ("Orchestration board", "Skill focus: multi-agent routing, task queues, status telemetry."),
            ("Research results", "Skill focus: RAG retrieval, confidence scoring, source attribution."),
            ("Support workspace", "Skill focus: helpdesk copilots, GHL inbox sync, knowledge retrieval."),
            ("Agent analytics", "Skill focus: eval metrics, token cost controls, latency dashboards."),
            ("Approval queue", "Skill focus: human-in-the-loop gates, risk scoring, audit trails."),
            ("Guardrails settings", "Skill focus: policy engines, allowlists, rate-limit configuration."),
        ],
    },
    {
        "path": "automation/workflow",
        "category": "Automation",
        "category_slug": "automation",
        "title": "Workflow Automation",
        "slug": "workflow",
        "tag": "AI & Automation",
        "lede": "Orchestration across CRM, ERP, email, and ops—approvals without chasing. Visual builders, sync monitors, and retry observability.",
        "stack": ["Make.com", "n8n", "Zapier", "GoHighLevel", "Monday.com"],
        "samples": [
            ("Workflow canvas", "Skill focus: Make/n8n/GHL orchestration, CRM triggers, action graphs."),
            ("Sync monitor", "Skill focus: GHL ↔ Monday/CRM sync health, latency, failed-record recovery."),
            ("Approval inbox", "Skill focus: Monday.com approvals, SLA timers, decision audit logs."),
            ("Node editor", "Skill focus: branching logic, HTTP steps, filter/transform nodes."),
            ("Job calendar", "Skill focus: GHL calendars + cron scheduling, cadence, run windows."),
            ("Retry observability", "Skill focus: error taxonomy, exponential retry, incident recovery."),
            ("Webhook log", "Skill focus: endpoint observability, payload inspection, status codes."),
        ],
    },
    {
        "path": "engineering/web-apps",
        "category": "Engineering",
        "category_slug": "engineering",
        "title": "Full Stack Web Applications",
        "slug": "web-apps",
        "tag": "Engineering",
        "lede": "React, Next.js, Node, and APIs—deployed and monitored for production. Dashboards, RBAC, billing, and API surfaces teams actually run.",
        "stack": ["React", "Next.js", "Node", "PostgreSQL", "Supabase"],
        "samples": [
            ("SaaS home on desktop", "Skill focus: Next.js app shell, KPI composition, production UX."),
            ("Analytics on ultrawide PC", "Skill focus: chart systems, retention cohorts, React data viz."),
            ("Team RBAC settings", "Skill focus: role matrices, invites, permission-aware UI."),
            ("API developer portal", "Skill focus: REST/GraphQL docs, auth scopes, try-it panels."),
            ("Customer CRM table", "Skill focus: server-driven filters, Postgres-backed lists, saved views."),
            ("Billing & subscriptions", "Skill focus: Stripe-ready plans, invoices, entitlement states."),
            ("Delivery board desktop", "Skill focus: Monday-style boards, state machines, realtime product UI."),
        ],
    },
    {
        "path": "engineering/mobile",
        "category": "Engineering",
        "category_slug": "engineering",
        "title": "Mobile Apps",
        "slug": "mobile",
        "tag": "Engineering",
        "lede": "Cross-platform mobile with push notifications, offline sync, and polished UX—field apps, loyalty, and support in the pocket.",
        "stack": ["React Native", "Expo", "Firebase", "Flutter", "Push"],
        "samples": [
            ("Field home on iPhone", "Skill focus: React Native navigation, job queues, status chips."),
            ("Job detail phone UI", "Skill focus: camera capture, checklists, offline-capable forms."),
            ("Push notification center", "Skill focus: FCM/APNs, deep links, assignment alerts."),
            ("Offline sync screen", "Skill focus: queued mutations, conflict handling, reconnect UX."),
            ("GPS check-in map", "Skill focus: geolocation, geofencing, map SDK integration."),
            ("In-app support chat", "Skill focus: realtime messaging, technician/customer threads."),
            ("Loyalty app home", "Skill focus: Storefront API, rewards state, polished consumer UX."),
        ],
    },
    {
        "path": "commerce/shopify",
        "category": "Commerce",
        "category_slug": "commerce",
        "title": "Ecommerce & Shopify",
        "slug": "shopify",
        "tag": "Commerce",
        "lede": "Store builds, theme development, checkout flows, and marketing automation for DTC brands that need conversion and ops in sync.",
        "stack": ["Shopify Plus", "Klaviyo", "Stripe", "GHL", "Triple Whale"],
        "samples": [
            ("Storefront home", "Skill focus: Liquid theme systems, conversion heroes, DTC merchandising."),
            ("Product detail", "Skill focus: variant UX, gallery performance, trust/SEO signals."),
            ("Checkout flow", "Skill focus: cart upsells, shipping logic, payment readiness."),
            ("Orders admin", "Skill focus: fulfillment queues, order ops, inventory sync."),
            ("Subscriptions", "Skill focus: recurring billing portals, pause/skip flows."),
            ("Collection grid", "Skill focus: merchandising rules, filterable catalogs."),
            ("Campaign preview", "Skill focus: Klaviyo-ready email creative wired to catalog data."),
        ],
    },
    {
        "path": "commerce/cms",
        "category": "Commerce",
        "category_slug": "commerce",
        "title": "WordPress, Wix & CMS",
        "slug": "cms",
        "tag": "Commerce",
        "lede": "Custom themes, SEO-ready sites, and headless CMS for content teams who need speed without giving up structure.",
        "stack": ["WordPress", "Wix", "Webflow", "Sanity", "SEO"],
        "samples": [
            ("Block editor", "Skill focus: composable CMS blocks, editor UX, content modeling."),
            ("Marketing home", "Skill focus: performance-minded themes, IA, conversion sections."),
            ("Blog listing", "Skill focus: editorial systems, taxonomy, search/SEO structure."),
            ("Content calendar", "Skill focus: publish workflows, multi-location scheduling."),
            ("Entry editor", "Skill focus: headless CMS fields, preview, structured content."),
            ("SEO panel", "Skill focus: schema, meta, index controls, technical SEO."),
            ("Services page", "Skill focus: location pages, CTAs, local business UX."),
        ],
    },
    {
        "path": "systems/odoo",
        "category": "Business Systems",
        "category_slug": "systems",
        "title": "Odoo ERP & Business Systems",
        "slug": "odoo",
        "tag": "Business Systems",
        "lede": "Sales, inventory, accounting—configured, integrated, and adopted by teams who need one operational source of truth.",
        "stack": ["Odoo", "NetSuite", "QuickBooks", "Python", "Barcode"],
        "samples": [
            ("Sales pipeline", "Skill focus: ERP opportunity stages, forecast, sales ops."),
            ("Stock levels", "Skill focus: warehouse quantities, reorder points, inventory hygiene."),
            ("Invoice list", "Skill focus: AR workflows, payment status, accounting views."),
            ("MRP board", "Skill focus: manufacturing orders, work centers, production status."),
            ("Purchase orders", "Skill focus: vendor POs, receiving, procurement controls."),
            ("ERP dashboard", "Skill focus: cross-module KPIs, ops visibility, executive views."),
            ("Receiving desk", "Skill focus: barcode intake, putaway, warehouse execution."),
        ],
    },
    {
        "path": "systems/bubble",
        "category": "Business Systems",
        "category_slug": "systems",
        "title": "Bubble No-Code Apps",
        "slug": "bubble",
        "tag": "Business Systems",
        "lede": "Rapid MVPs and internal tools—workflows, permissions, and API connections that ship before custom code is justified.",
        "stack": ["Bubble", "Airtable", "Stripe", "Xano", "Softr"],
        "samples": [
            ("Ops portal", "Skill focus: no-code app architecture, internal dashboards."),
            ("Permissions", "Skill focus: role matrices, privacy rules, access control."),
            ("Dispatch board", "Skill focus: assignment workflows, realtime status boards."),
            ("Client portal", "Skill focus: external user UX, status timelines, messaging."),
            ("Workflow builder", "Skill focus: Bubble logic, conditions, backend workflows."),
            ("Payments list", "Skill focus: Stripe connector patterns, invoice states."),
            ("Responsive tool", "Skill focus: responsive no-code layouts across devices."),
        ],
    },
    {
        "path": "automation/python",
        "category": "Automation",
        "category_slug": "automation",
        "title": "Python Business Automation",
        "slug": "python",
        "tag": "AI & Automation",
        "lede": "Scripts, schedulers, and data pipelines—ETL, reporting, and API glue that keep ops moving without spreadsheet babysitting.",
        "stack": ["Python", "FastAPI", "Pandas", "Airflow", "Cron"],
        "samples": [
            ("Pipeline monitor", "Skill focus: ETL orchestration, row counts, latency SLOs."),
            ("Run history", "Skill focus: job observability, Flask/FastAPI ops dashboards."),
            ("Schema browser", "Skill focus: warehouse modeling, lineage, data contracts."),
            ("Alert panel", "Skill focus: Slack/ops alerts, threshold monitors, incident UX."),
            ("Cron board", "Skill focus: schedulers, environment promotion, run windows."),
            ("Report preview", "Skill focus: Pandas reporting, tabular QA before distribute."),
            ("API map", "Skill focus: middleware health, service topology, integration ops."),
        ],
    },
    {
        "path": "systems/crm-erp",
        "category": "Business Systems",
        "category_slug": "systems",
        "title": "CRM & ERP Integration",
        "slug": "crm-erp",
        "tag": "Business Systems",
        "lede": "Salesforce, HubSpot, NetSuite, Dynamics—one story across systems with conflict rules and idempotent sync.",
        "stack": ["GoHighLevel", "HubSpot", "Salesforce", "Monday.com", "NetSuite"],
        "samples": [
            ("Opportunity pipeline", "Skill focus: GHL/HubSpot pipelines, stages, forecast UX."),
            ("Sync status", "Skill focus: GHL ↔ Monday/Salesforce sync, lag metrics, idempotency."),
            ("Quote-to-cash", "Skill focus: opportunity→order timelines, RevOps handoffs."),
            ("Contact timeline", "Skill focus: GHL conversations + CRM activity unification."),
            ("Fulfillment view", "Skill focus: ERP order ops tied to CRM accounts."),
            ("Conflict resolver", "Skill focus: field-level merge rules, data stewardship."),
            ("Integration map", "Skill focus: system topology, webhook ownership, health."),
        ],
    },
    {
        "path": "systems/power-platform",
        "category": "Business Systems",
        "category_slug": "systems",
        "title": "Power BI & Power Apps",
        "slug": "power-platform",
        "tag": "Business Systems",
        "lede": "Dashboards and low-code apps wired to CRM, ERP, and Dataverse—so operators see and act in the same loop.",
        "stack": ["Power BI", "Power Apps", "Power Automate", "Dataverse", "Teams"],
        "samples": [
            ("Executive BI", "Skill focus: semantic models, DAX-ready visuals, executive KPIs."),
            ("Canvas app", "Skill focus: Power Apps forms, Dataverse writeback, mobile ops."),
            ("Flow designer", "Skill focus: Power Automate approvals, connectors, branching."),
            ("Dataverse browser", "Skill focus: table design, relationships, security roles."),
            ("Embedded analytics", "Skill focus: BI embedded in CRM workspaces."),
            ("Mobile approvals", "Skill focus: phone-first approval UX for operators."),
            ("SLA scorecards", "Skill focus: service health, trend sparklines, team targets."),
        ],
    },
    {
        "path": "automation/documents",
        "category": "Automation",
        "category_slug": "automation",
        "title": "Intelligent Documents",
        "slug": "documents",
        "tag": "AI & Automation",
        "lede": "Extract, classify, and route invoices and contracts into your systems—with exceptions and audit trails operators trust.",
        "stack": ["Document AI", "OCR", "QuickBooks", "DocuSign", "Python"],
        "samples": [
            ("Invoice OCR", "Skill focus: document AI extraction, line-item structuring."),
            ("Classification inbox", "Skill focus: doc typing, triage queues, routing prep."),
            ("Contract review", "Skill focus: clause detection, risk tags, legal ops UX."),
            ("PO matching", "Skill focus: 3-way match exceptions, finance controls."),
            ("Routing rules", "Skill focus: conditional routing engines, queue assignment."),
            ("Audit trail", "Skill focus: approval provenance, compliance timelines."),
            ("Batch queue", "Skill focus: bulk processing, progress, retry failed packs."),
        ],
    },
]


def rel_prefix(path: str) -> str:
    depth = path.count("/") + 1
    return "../" * depth


def other_links(current: dict) -> list[dict]:
    same = [p for p in PAGES if p["category_slug"] == current["category_slug"] and p["path"] != current["path"]]
    others = [p for p in PAGES if p["category_slug"] != current["category_slug"]]
    picks = (same + others)[:3]
    return picks


def render(page: dict) -> str:
    prefix = rel_prefix(page["path"])
    samples_html = []
    for i, (name, blurb) in enumerate(page["samples"], start=1):
        src = f"{prefix}assets/samples/{page['slug']}/{i:02d}.jpg"
        skill = ""
        detail = blurb
        if blurb.startswith("Skill focus:"):
            skill = blurb.replace("Skill focus:", "", 1).strip()
            detail = f"Skill focus: {skill}"
        skill_html = f'<em class="xp-skill">{skill}</em>' if skill else ""
        samples_html.append(
            f"""          <figure class="xp-gallery__item">
            <img src="{src}" alt="{name} — {page['title']}" loading="lazy" width="1280" height="800" />
            <figcaption>
              <strong>{name}</strong>
              {skill_html}
              <span>{detail}</span>
            </figcaption>
          </figure>"""
        )

    meta = "\n".join(f"          <span>{s}</span>" for s in page["stack"])
    more = []
    for o in other_links(page):
        href = f"{prefix}{o['path']}/"
        more.append(
            f"""        <a class="xp-more__link" href="{href}">
          <small>{o['tag']}</small>
          <strong>{o['title']}</strong>
        </a>"""
        )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{page['title']} — LoveThisLife Experience</title>
  <meta name="description" content="{page['lede']}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Public+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet" />
  <link rel="icon" href="{prefix}assets/favicon.svg?v=2" type="image/svg+xml" />
  <link rel="stylesheet" href="{prefix}styles.css" />
  <link rel="stylesheet" href="{prefix}experience.css" />
</head>
<body class="xp-body">
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header xp-header" id="top">
    <div class="header-inner">
      <a class="logo" href="{prefix}" aria-label="LoveThisLife home">
        <span class="logo-word">Love<span>This</span>Life</span>
      </a>
      <nav class="nav" aria-label="Primary">
        <a href="{prefix}solutions/" class="is-active">Solutions</a>
        <a href="{prefix}platforms/">Platforms</a>
        <a href="{prefix}capabilities/">Capabilities</a>
        <a href="{prefix}work/">Work</a>
        <a href="{prefix}process/">Process</a>
        <a href="{prefix}about/">About</a>
      </nav>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="mobile-nav" aria-label="Open menu">
        <span></span><span></span>
      </button>
    </div>
    <nav class="mobile-nav" id="mobile-nav" hidden>
      <a href="{prefix}solutions/" class="is-active">Solutions</a>
      <a href="{prefix}platforms/">Platforms</a>
      <a href="{prefix}capabilities/">Capabilities</a>
      <a href="{prefix}work/">Work</a>
      <a href="{prefix}process/">Process</a>
      <a href="{prefix}about/">About</a>
    </nav>
  </header>

  <main id="main" class="xp-main">
    <div class="container">
      <header class="xp-hero">
        <nav class="xp-crumb" aria-label="Breadcrumb">
          <a href="{prefix}">Home</a>
          <span class="xp-crumb__sep">/</span>
          <a href="{prefix}solutions/">Solutions</a>
          <span class="xp-crumb__sep">/</span>
          <span>{page['category']}</span>
          <span class="xp-crumb__sep">/</span>
          <span>{page['path'].split('/')[-1]}</span>
        </nav>
        <p class="xp-kicker">{page['tag']} · Experience</p>
        <h1 class="xp-title">{page['title']}</h1>
        <p class="xp-lede">{page['lede']}</p>
        <div class="xp-meta">
{meta}
        </div>
      </header>

      <section class="xp-gallery" aria-label="Product samples">
{chr(10).join(samples_html)}
      </section>

      <aside class="xp-cta">
        <h2>Need this in production?</h2>
        <p>LoveThisLife ships the full stack—from agents and automation to storefronts and ERP—with clear handoff.</p>
        <div class="xp-cta__row">
          <a class="xp-btn xp-btn--primary" href="{prefix}about/">Talk with Christina</a>
          <a class="xp-btn xp-btn--ghost" href="{prefix}solutions/">All solutions</a>
        </div>
      </aside>

      <section class="xp-more">
        <h2>More experience</h2>
        <div class="xp-more__grid">
{chr(10).join(more)}
        </div>
      </section>
    </div>
  </main>
  <script src="{prefix}script.js"></script>
</body>
</html>
"""


def main() -> None:
    for page in PAGES:
        out = ROOT / page["path"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(page), encoding="utf-8")
        print(f"wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
