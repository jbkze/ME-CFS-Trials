#!/usr/bin/env python3
"""Regenerate the human-readable views from the JSON sources of truth.

Outputs:
  - TRIALS.md            (Markdown table, from data/trials.json)
  - docs/dashboard.json  (feed for the GitHub Pages dashboard, docs/index.html)

Reads:
  - data/trials.json     (studies; source of truth)
  - data/papers.json     (papers; optional)

Usage:  python3 scripts/render_trials.py
No third-party dependencies. Run after every update to the data files.
"""
from __future__ import annotations

import json
import pathlib
import sys
from datetime import datetime, timedelta

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "trials.json"
PAPERS = ROOT / "data" / "papers.json"
OUT_MD = ROOT / "TRIALS.md"
OUT_DASH = ROOT / "docs" / "dashboard.json"

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

# Map the trial lifecycle status onto the dashboard's three visual buckets.
# Statuses not listed here (completed / terminated / withdrawn / suspended /
# unknown) are treated as archived and omitted from the dashboard.
DASH_BUCKET = {
    "recruiting": ("recruiting", "Recruiting"),
    "enrolling_by_invitation": ("recruiting", "Enrolling (invite)"),
    "not_yet_recruiting": ("soon", "Starts soon"),
    "active_not_recruiting": ("planned", "Active, not recruiting"),
}
BUCKET_ORDER = {"recruiting": 0, "soon": 1, "planned": 2}


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
        lines += ["", "## Watchlist (not yet open / not recruiting)", ""]
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


def to_study(t: dict):
    bucket = DASH_BUCKET.get(t.get("status"))
    if bucket is None:
        return None  # archived / closed → not shown on the dashboard
    flags = t.get("flags") or []
    title = t.get("name") or t.get("id") or "Untitled study"
    if t.get("acronym"):
        title = f"{t['acronym']} — {title}"
    reg = t.get("registry") or {}
    return {
        "title": title,
        "status": bucket[0],
        "statusLabel": bucket[1],
        "location": study_location(t.get("germany") or {}),
        "link": reg.get("url") or (t.get("links") or ["#"])[0] or "#",
        "isNew": ("new" in flags) or ("newly_open" in flags),
        "_priority": t.get("priority", "normal"),
    }


def load_papers() -> list:
    if not PAPERS.exists():
        return []
    pdb = json.loads(PAPERS.read_text(encoding="utf-8"))
    papers = []
    for p in pdb.get("papers", []):
        flags = p.get("flags") or []
        papers.append({
            "title": p.get("title", ""),
            "authors": p.get("authors", ""),
            "journal": p.get("journal", ""),
            "date": p.get("date", ""),
            "summary": p.get("summary", ""),
            "why": p.get("why", ""),
            "link": p.get("link") or "#",
            "isNew": p.get("isNew", ("new" in flags)),
        })
    papers.sort(key=lambda p: not p["isNew"])  # new first, otherwise input order
    return papers


def format_run(last):
    if not last:
        return "Not run yet", "First scheduled run pending"
    try:
        d = datetime.strptime(last, "%Y-%m-%d")
        return d.strftime("%d %b %Y"), "Next run ~" + (d + timedelta(days=7)).strftime("%d %b %Y")
    except ValueError:
        return str(last), ""


def build_dashboard(db: dict, trials: list) -> int:
    studies = [s for s in (to_study(t) for t in trials) if s]
    studies.sort(key=lambda s: (not s["isNew"], BUCKET_ORDER.get(s["status"], 9),
                                s["_priority"] != "high", s["title"].lower()))
    for s in studies:
        s.pop("_priority", None)
    papers = load_papers()
    last_run, next_run = format_run(db.get("last_check"))
    out = {
        "generated": db.get("last_check"),
        "lastRun": last_run,
        "nextRun": next_run,
        "studies": studies,
        "papers": papers,
    }
    OUT_DASH.parent.mkdir(parents=True, exist_ok=True)
    OUT_DASH.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return len(studies), len(papers)


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
    n_studies, n_papers = build_dashboard(db, trials)
    print(f"wrote {OUT_MD} ({len(trials)} trials)")
    print(f"wrote {OUT_DASH} ({n_studies} studies, {n_papers} papers)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
