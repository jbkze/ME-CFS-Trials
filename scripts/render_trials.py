#!/usr/bin/env python3
"""Regenerate the human-readable views from the JSON sources of truth.

Outputs:
  - TRIALS.md            (Markdown table, from data/trials.json)
  - STATE-OF-THE-ART.md  (Markdown view of data/state_of_the_art.json)
  - docs/dashboard.json  (feed for the GitHub Pages dashboard, docs/index.html)
  - docs/feed.xml        (Atom feed: newest papers + trial changes, for feed readers)

Reads:
  - data/trials.json            (studies; source of truth)
  - data/papers.json            (papers; optional)
  - data/state_of_the_art.json  (plain-language research overview; optional)

Usage:  python3 scripts/render_trials.py
No third-party dependencies. Run after every update to the data files.
"""
from __future__ import annotations

import json
import pathlib
import re
import sys
from datetime import datetime, timedelta

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "trials.json"
PAPERS = ROOT / "data" / "papers.json"
SOTA = ROOT / "data" / "state_of_the_art.json"
OUT_MD = ROOT / "TRIALS.md"
OUT_SOTA_MD = ROOT / "STATE-OF-THE-ART.md"
OUT_DASH = ROOT / "docs" / "dashboard.json"
OUT_FEED = ROOT / "docs" / "feed.xml"
SITE_URL = "https://jbkze.github.io/ME-CFS-Trials/"
FEED_LIMIT = 60

STATUS_LABEL = {
    "recruiting": "🟢 Recruiting",
    "enrolling_by_invitation": "🟢 Enrolling (invite)",
    "not_yet_recruiting": "🟡 Not yet recruiting",
    "active_not_recruiting": "🟠 Active, not recruiting",
    "suspended": "🔴 Suspended",
    "completed": "⚪ Completed",
    "terminated": "🔴 Terminated",
    "withdrawn": "🔴 Withdrawn",
    "unknown": "❔ Unknown",
}

# Map the trial lifecycle status onto the dashboard's visual buckets and tiers.
# Statuses not listed here (completed / terminated / withdrawn / suspended /
# unknown) go to the collapsed "archived" tier.
DASH_BUCKET = {
    "recruiting": ("recruiting", "Recruiting"),
    "enrolling_by_invitation": ("recruiting", "Enrolling (invite)"),
    "not_yet_recruiting": ("soon", "Planned"),
    "active_not_recruiting": ("planned", "Active, not recruiting"),
}
BUCKET_ORDER = {"recruiting": 0, "soon": 1, "planned": 2, "closed": 3}
TIER = {"recruiting": "open", "soon": "planned", "planned": "planned", "closed": "archived"}

# Change flags (see ROUTINE.md step 5) → short badge shown on the study card.
CHANGE_LABEL = {
    "newly_open": "Now open",
    "status_changed": "Status changed",
    "closed_since_last": "Closed",
    "details_changed": "Updated",
}

# Confidence scale for state-of-the-art sections (label shown on the dashboard).
CONFIDENCE = {
    "established": "Well established",
    "strong": "Strong evidence",
    "emerging": "Emerging evidence",
    "contested": "Mixed / contested",
    "early": "Early ideas",
}

PRIORITY_RESEARCHERS = (("Scheibenbogen", re.compile(r"Scheibenbogen")),
                        ("Wirth", re.compile(r"\bWirth K")))


# --------------------------------------------------------------------------- #
# TRIALS.md
# --------------------------------------------------------------------------- #
def cell(text) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ").strip() or "—"


def link(label: str, url) -> str:
    return f"[{cell(label)}]({url})" if url else cell(label)


def fmt_sites(germany: dict) -> str:
    sites = germany.get("sites") or []
    if not sites:
        return "✓ DE" if germany.get("has_german_site") else "—"
    return ", ".join(cell(f"{s.get('city', '')} ({s.get('institution', '')})".strip()) for s in sites)


def render_row(t: dict) -> str:
    reg = t.get("registry") or {}
    intervention = t.get("intervention") or {}
    flags = t.get("flags") or []
    flag_str = " ".join(f"`{f}`" for f in flags) if flags else "—"
    researchers = ", ".join(t.get("associated_researchers") or []) or "—"
    star = "⭐ " if t.get("priority") == "high" else ""
    name = link(t.get("acronym") or t.get("name", t.get("id", "?")), reg.get("url") or (t.get("links") or [None])[0])
    return "| {prio}{name} | {status} | {drug} | {researchers} | {sites} | {reg} | {checked} | {flags} |".format(
        prio=star,
        name=name,
        status=STATUS_LABEL.get(t.get("status", "unknown"), cell(t.get("status", "?"))),
        drug=cell(intervention.get("name", "?")),
        researchers=cell(researchers),
        sites=fmt_sites(t.get("germany") or {}),
        reg=cell(f"{reg.get('name', '')} {reg.get('id', '')}".strip()),
        checked=cell(t.get("last_checked", "—")),
        flags=flag_str,
    )


def render_markdown(db: dict, trials: list) -> None:
    open_now = [t for t in trials if t.get("open_for_enrollment")]
    watch = [t for t in trials if not t.get("open_for_enrollment")
             and t.get("status") in ("not_yet_recruiting", "active_not_recruiting")]
    archived = [t for t in trials if t not in open_now and t not in watch]

    header = (
        "| Trial | Status | Drug / intervention | Researcher(s) | German site(s) | Registry | Last checked | Flags |\n"
        "|---|---|---|---|---|---|---|---|\n"
    )
    lines = [
        "# ME/CFS drug trials in Germany — tracker",
        "",
        "> Auto-generated from `data/trials.json` by `scripts/render_trials.py`. "
        "**Do not edit by hand** — edit the JSON and re-run the script.",
        "",
        f"- Last check: **{db.get('last_check') or 'never'}**",
        f"- Trials tracked: **{len(trials)}** (open for enrollment: **{len(open_now)}**, "
        f"watchlist: **{len(watch)}**, archived: **{len(archived)}**)",
        "- ⭐ = linked to Klaus Wirth or Carmen Scheibenbogen.",
        "",
    ]
    if not trials:
        lines += ["_No trials recorded yet. Run the routine in `ROUTINE.md` to populate this._", ""]
    else:
        lines += ["## Open for enrollment", ""]
        lines += [header + "\n".join(render_row(t) for t in open_now)] if open_now else ["_None currently._"]
        lines += ["", "## Planned / not yet recruiting (also relevant)", ""]
        lines += [header + "\n".join(render_row(t) for t in watch)] if watch else ["_None._"]
        if archived:
            lines += ["", "## Archived (closed / completed / withdrawn)", ""]
            lines += [header + "\n".join(render_row(t) for t in archived)]
    OUT_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


# --------------------------------------------------------------------------- #
# docs/dashboard.json  (feed for docs/index.html)
# --------------------------------------------------------------------------- #
def study_location(germany: dict) -> str:
    sites = [s for s in (germany.get("sites") or []) if s.get("institution") or s.get("city")]
    if not sites:
        return "Germany" if germany.get("has_german_site") else "—"
    first = ", ".join(p for p in [sites[0].get("institution"), sites[0].get("city")] if p)
    return first + (f" +{len(sites) - 1} more" if len(sites) > 1 else "")


def to_study(t: dict) -> dict:
    status = t.get("status")
    bucket = DASH_BUCKET.get(status) or ("closed", STATUS_LABEL.get(status, "Closed").split(" ", 1)[-1])
    flags = t.get("flags") or []
    title = t.get("name") or t.get("id") or "Untitled study"
    if t.get("acronym"):
        title = f"{t['acronym']} — {title}"
    reg = t.get("registry") or {}
    iv = t.get("intervention") or {}
    elig = t.get("eligibility") or {}
    sites = [
        {"name": ", ".join(p for p in [s.get("institution"), s.get("city")] if p),
         "recruiting": s.get("recruiting")}
        for s in (t.get("germany") or {}).get("sites") or []
        if s.get("institution") or s.get("city")
    ]
    change = next((CHANGE_LABEL[f] for f in flags if f in CHANGE_LABEL), None)
    cities = []
    for s in (t.get("germany") or {}).get("sites") or []:
        c = (s.get("city") or "").strip()
        if c and c not in cities:
            cities.append(c)
    return {
        "id": t.get("id"),
        "title": title,
        "shortTitle": t.get("acronym") or iv.get("name") or title,
        "officialTitle": t.get("name") or "",
        "plainSummary": t.get("plain_summary") or "",
        "keyRequirement": t.get("key_requirement") or "",
        "cities": cities,
        "status": bucket[0],
        "statusLabel": bucket[1],
        "tier": TIER[bucket[0]],
        "location": study_location(t.get("germany") or {}),
        "link": reg.get("url") or (t.get("links") or ["#"])[0] or "#",
        "registry": f"{reg.get('name', '')} {reg.get('id', '')}".strip(),
        "isNew": ("new" in flags) or ("newly_open" in flags),
        "change": change,
        "priority": t.get("priority", "normal"),
        "researchers": t.get("associated_researchers") or [],
        "intervention": iv.get("name", ""),
        "interventionType": iv.get("type", ""),
        "mechanism": iv.get("mechanism", ""),
        "phase": t.get("phase") or "",
        "condition": t.get("condition") or "",
        "pi": t.get("principal_investigator") or "",
        "sponsor": t.get("sponsor") or "",
        "eligibility": {
            "summary": elig.get("summary", ""),
            "age": elig.get("age", ""),
            "inclusion": elig.get("key_inclusion") or [],
            "exclusion": elig.get("key_exclusion") or [],
        },
        "sites": sites,
        "firstSeen": t.get("first_seen") or "",
        "lastChecked": t.get("last_checked") or "",
        "lastStatusChange": t.get("last_status_change") or "",
    }


MONTHS = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}
_FULL = re.compile(r"\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.? (\d{1,2}), (\d{4})")
_MONTH = re.compile(r"\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.? (\d{4})")
_YEAR = re.compile(r"\b(19|20)\d{2}\b")


def paper_published(p: dict) -> str:
    """ISO date (YYYY-MM-DD, YYYY-MM or YYYY) a paper first became available.

    Uses an explicit `published` field when present; otherwise parses the
    free-text `date` (e.g. "Oct 2026 (posted online Aug 10, 2026)") and takes
    the EARLIEST date mentioned — the online/preprint date, not the print issue.
    """
    if p.get("published"):
        return str(p["published"])
    text = p.get("date") or ""
    cands = [(int(y), MONTHS[m.lower()[:3]], int(d)) for m, d, y in _FULL.findall(text)]
    cands += [(int(y), MONTHS[m.lower()[:3]], 0) for m, y in _MONTH.findall(text)]
    if not cands:
        years = [int(m.group(0)) for m in _YEAR.finditer(text)]
        return str(min(years)) if years else ""
    y, mo = min((c[0], c[1]) for c in cands)
    day = max(c[2] for c in cands if (c[0], c[1]) == (y, mo))
    return f"{y:04d}-{mo:02d}-{day:02d}" if day else f"{y:04d}-{mo:02d}"


def paper_researchers(p: dict) -> list:
    if p.get("associated_researchers"):
        return list(p["associated_researchers"])
    authors = p.get("authors", "")
    return [name for name, rx in PRIORITY_RESEARCHERS if rx.search(authors)]


def load_papers() -> list:
    if not PAPERS.exists():
        return []
    pdb = json.loads(PAPERS.read_text(encoding="utf-8"))
    papers = []
    for p in pdb.get("papers", []):
        flags = p.get("flags") or []
        papers.append({
            "id": p.get("id", ""),
            "title": p.get("title", ""),
            "authors": p.get("authors", ""),
            "journal": p.get("journal", ""),
            "date": p.get("date", ""),
            "published": paper_published(p),
            "summary": p.get("summary", ""),
            "why": p.get("why", ""),
            "link": p.get("link") or "#",
            "researchers": paper_researchers(p),
            "topics": [],
            "firstSeen": p.get("first_seen", ""),
            "isNew": p.get("isNew", ("new" in flags)),
        })
    # New first, then newest publication date first.
    papers.sort(key=lambda p: (not p["isNew"], _neg_date(p["published"])))
    return papers


def _neg_date(iso: str) -> tuple:
    parts = [int(x) for x in iso.split("-")] if iso else [0]
    parts += [0] * (3 - len(parts))
    return tuple(-x for x in parts)


# --------------------------------------------------------------------------- #
# State of the art  (data/state_of_the_art.json → dashboard + STATE-OF-THE-ART.md)
# --------------------------------------------------------------------------- #
def cite_label(p: dict) -> str:
    authors = re.sub(r"\s*\([^)]*\)", "", p.get("authors") or "")  # drop "(formerly …)" notes
    first = authors.split(",")[0].strip()
    surname = first.rsplit(" ", 1)[0] if " " in first else first
    if not surname or surname.lower().startswith(("institute", "the ")):
        surname = (p.get("journal") or p.get("id") or "?").split(" (")[0]
    year = (p.get("published") or "")[:4]
    return f"{surname} {year}".strip()


def load_sota(papers: list, trials: list):
    """Resolve the state-of-the-art file into render-ready sections.

    Every cited id must exist in papers.json or trials.json; unknown ids are
    reported as warnings and dropped, so nothing uncited reaches the page.
    """
    if not SOTA.exists():
        return None, []
    sota = json.loads(SOTA.read_text(encoding="utf-8"))
    by_paper = {p["id"]: p for p in papers}
    by_trial = {t.get("id"): t for t in trials}
    warnings = []

    def cite(ref: str):
        if ref in by_paper:
            p = by_paper[ref]
            return {"kind": "paper", "id": ref, "label": cite_label(p), "title": p["title"], "link": p["link"]}
        if ref in by_trial:
            t = by_trial[ref]
            reg = t.get("registry") or {}
            label = t.get("acronym") or (t.get("intervention") or {}).get("name") or ref
            return {"kind": "trial", "id": ref, "label": label, "title": t.get("name", ""),
                    "link": reg.get("url") or (t.get("links") or ["#"])[0]}
        warnings.append(ref)
        return None

    # Topic tagging: a paper belongs to a section if it is cited there or if one
    # of the section's `keywords` starts a word in its title or summary.
    for sec in sota.get("sections", []):
        kws = [k.lower() for k in sec.get("keywords") or []]
        rx = re.compile(r"\b(" + "|".join(re.escape(k) for k in kws) + ")") if kws else None
        cited = {r for pt in sec.get("points", []) for r in pt.get("refs", [])}
        for p in papers:
            hay = (p["title"] + " " + p["summary"]).lower()
            if p["id"] in cited or (rx and rx.search(hay)):
                p["topics"].append(sec.get("id", ""))

    sections = []
    for sec in sota.get("sections", []):
        points = []
        for pt in sec.get("points", []):
            refs = [c for c in (cite(r) for r in pt.get("refs", [])) if c]
            points.append({"text": pt.get("text", ""), "refs": refs})
        sections.append({
            "id": sec.get("id", ""),
            "title": sec.get("title", ""),
            "takeaway": sec.get("takeaway", ""),
            "confidence": sec.get("confidence", ""),
            "confidenceLabel": CONFIDENCE.get(sec.get("confidence", ""), ""),
            "updated": sec.get("updated", ""),
            "paperCount": sum(1 for p in papers if sec.get("id") in p["topics"]),
            "points": points,
        })
    out = {
        "updated": sota.get("updated", ""),
        "reviewed": sota.get("reviewed", ""),
        "intro": sota.get("intro", ""),
        "sections": sections,
    }
    return out, warnings


def render_sota_markdown(sota: dict) -> None:
    lines = [
        "# ME/CFS research — state of the art",
        "",
        "> Auto-generated from `data/state_of_the_art.json` by `scripts/render_trials.py`. "
        "**Do not edit by hand** — edit the JSON and re-run the script.",
        "",
        f"- Last content change: **{sota.get('updated') or '—'}** · last reviewed: **{sota.get('reviewed') or '—'}**",
        "",
    ]
    if sota.get("intro"):
        lines += [sota["intro"], ""]
    for sec in sota["sections"]:
        conf = f" · _{sec['confidenceLabel']}_" if sec["confidenceLabel"] else ""
        lines += [f"## {sec['title']}", "", f"**{sec['takeaway']}**{conf}", ""]
        for pt in sec["points"]:
            refs = "; ".join(f"[{r['label']}]({r['link']})" for r in pt["refs"])
            lines.append(f"- {pt['text']}" + (f" ({refs})" if refs else ""))
        lines += ["", f"<sub>Section updated {sec['updated'] or '—'}</sub>", ""]
    OUT_SOTA_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def format_run(db: dict):
    """Return (last_run_at_iso, lastRun_date_str, nextRun_str).

    last_run_at is an ISO-8601 timestamp (with time) when available — the HTML
    localises it to the viewer's timezone and shows the time next to the date.
    The date/next-run strings are plain fallbacks. Cadence is daily (+1 day).
    """
    at = db.get("last_run_at")  # ISO with time, e.g. "2026-06-25T14:21:48Z"
    last = db.get("last_check")  # date only, e.g. "2026-06-25"
    if not at and not last:
        return None, "Not run yet", "First scheduled run pending"
    d = None
    for candidate in (at[:10] if at else None, last):
        if candidate:
            try:
                d = datetime.strptime(candidate, "%Y-%m-%d")
                break
            except ValueError:
                continue
    if d is None:
        return at, (last or "—"), ""
    return at, d.strftime("%d %b %Y"), "Next run ~" + (d + timedelta(days=1)).strftime("%d %b %Y")


def _xml(text) -> str:
    return (str(text or "").replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def render_feed(db: dict, studies: list, papers: list) -> int:
    """Atom feed of the newest papers and trial additions/status changes."""
    entries = []
    for p in papers:
        if not p.get("firstSeen"):
            continue
        authors = p["authors"].split(",")
        authors = ",".join(authors[:3]) + (", et al." if len(authors) > 3 else "")
        source = p["link"] if p["link"].startswith("http") else ""
        entries.append((p["firstSeen"], "paper-" + p["id"], "Paper: " + p["title"],
                        SITE_URL + "#paper/" + p["id"],
                        f"{p['summary']}\n\nWhy it matters: {p['why']}\n\n{p['journal']} · {authors}"
                        + (f"\n{source}" if source else "")))
    for s in studies:
        when = max(s.get("firstSeen") or "", s.get("lastStatusChange") or "")
        if not when:
            continue
        what = "New study" if when == s.get("firstSeen") else "Status change"
        entries.append((when, f"study-{s['id']}-{when}", f"{what}: {s['shortTitle']} — {s['statusLabel']}",
                        SITE_URL + "#study/" + s["id"],
                        f"{s['plainSummary']}\n\n{s['title']}\nStatus: {s['statusLabel']} · {s['location']}"))
    entries.sort(key=lambda e: e[0], reverse=True)
    entries = entries[:FEED_LIMIT]
    updated = (db.get("last_run_at") or (db.get("last_check") or "1970-01-01") + "T00:00:00Z")
    out = [
        '<?xml version="1.0" encoding="utf-8"?>',
        '<feed xmlns="http://www.w3.org/2005/Atom">',
        "  <title>ME/CFS Research Watch</title>",
        "  <subtitle>New ME/CFS drug trials in Germany and notable new research papers.</subtitle>",
        f'  <link rel="alternate" href="{SITE_URL}"/>',
        f'  <link rel="self" href="{SITE_URL}feed.xml"/>',
        f"  <id>{SITE_URL}</id>",
        f"  <updated>{_xml(updated)}</updated>",
    ]
    for when, eid, title, link_url, summary in entries:
        out += [
            "  <entry>",
            f"    <title>{_xml(title)}</title>",
            f'    <link href="{_xml(link_url)}"/>',
            f"    <id>{_xml(SITE_URL + '#' + eid)}</id>",
            f"    <updated>{_xml(when)}T00:00:00Z</updated>",
            f"    <summary>{_xml(summary)}</summary>",
            "  </entry>",
        ]
    out.append("</feed>")
    OUT_FEED.write_text("\n".join(out) + "\n", encoding="utf-8")
    return len(entries)


def build_dashboard(db: dict, trials: list):
    studies = [to_study(t) for t in trials]
    studies.sort(key=lambda s: (BUCKET_ORDER.get(s["status"], 9), not s["isNew"],
                                s["priority"] != "high", s["title"].lower()))
    papers = load_papers()
    sota, warnings = load_sota(papers, trials)
    if sota:
        render_sota_markdown(sota)
    last_run_at, last_run, next_run = format_run(db)
    out = {
        "generated": db.get("last_check"),
        "lastRunAt": last_run_at,
        "lastRun": last_run,
        "nextRun": next_run,
        "studies": studies,
        "papers": papers,
        "overview": sota,
    }
    OUT_DASH.parent.mkdir(parents=True, exist_ok=True)
    OUT_DASH.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    render_feed(db, studies, papers)
    return len(studies), len(papers), sota, warnings


# --------------------------------------------------------------------------- #
def main() -> int:
    if not DATA.exists():
        print(f"error: {DATA} not found", file=sys.stderr)
        return 1
    db = json.loads(DATA.read_text(encoding="utf-8"))
    trials = db.get("trials", [])
    trials.sort(key=lambda t: (
        not t.get("open_for_enrollment", False),
        t.get("priority") != "high",
        (t.get("acronym") or t.get("name") or t.get("id") or "").lower(),
    ))
    render_markdown(db, trials)
    n_studies, n_papers, sota, warnings = build_dashboard(db, trials)
    print(f"wrote {OUT_MD} ({len(trials)} trials)")
    if sota:
        print(f"wrote {OUT_SOTA_MD} ({len(sota['sections'])} sections)")
    print(f"wrote {OUT_DASH} ({n_studies} studies, {n_papers} papers)")
    print(f"wrote {OUT_FEED}")
    for ref in warnings:
        print(f"WARNING: state_of_the_art.json cites unknown id '{ref}' (not in papers.json "
              f"or trials.json) — dropped from the output; fix the id.", file=sys.stderr)
    return 1 if warnings else 0


if __name__ == "__main__":
    raise SystemExit(main())
