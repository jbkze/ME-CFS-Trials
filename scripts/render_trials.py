#!/usr/bin/env python3
"""Regenerate TRIALS.md (human-readable view) from data/trials.json (source of truth).

Usage:  python3 scripts/render_trials.py
No third-party dependencies. Run after every update to data/trials.json.
"""
from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "trials.json"
OUT = ROOT / "TRIALS.md"

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


def cell(text: str) -> str:
    """Escape pipes so a value never breaks the Markdown table."""
    return str(text).replace("|", "\\|").replace("\n", " ").strip() or "—"


def link(label: str, url: str | None) -> str:
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


def main() -> int:
    if not DATA.exists():
        print(f"error: {DATA} not found", file=sys.stderr)
        return 1
    db = json.loads(DATA.read_text(encoding="utf-8"))
    trials = db.get("trials", [])

    # Sort: open enrollment first, then high priority, then name.
    trials.sort(key=lambda t: (
        not t.get("open_for_enrollment", False),
        t.get("priority") != "high",
        (t.get("acronym") or t.get("name") or t.get("id") or "").lower(),
    ))

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

    OUT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"wrote {OUT} ({len(trials)} trials)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
