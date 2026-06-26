# CLAUDE.md

Standing orders for this repo. Auto-loaded every session. The detailed procedure
lives in `ROUTINE.md` — **this file is the gist + the instruction to read it.**

## What this repo is

A stateful tracker with two tracks, prioritising **Klaus Wirth** (Mitodicure /
MDC002) and **Carmen Scheibenbogen** (Charité Fatigue Centrum):

- **Trials** — new ME/CFS **drug-trial opportunities in Germany** (open for
  enrollment *or* planned / not yet recruiting). → `data/trials.json`
- **Papers** — notable new ME/CFS **research papers** (pathomechanism, biomarkers,
  drug targets, treatment, genetics), *not* Germany-restricted. → `data/papers.json`

Each run surfaces only what is *new* or *changed* since `last_check`.

## When asked to "run a check" / "Studien-Check" / "research watch"

**Read `ROUTINE.md` first and follow it exactly.** It is authoritative if anything
below is ambiguous. In short:

1. Load `data/trials.json` **and** `data/papers.json` as baselines.
2. Search the sources in `sources/search-sources.md` **and** do fresh open-ended
   web search beyond that list (it is a checklist, not a limit) — for both trials
   and recent papers.
3. Confirm every candidate before recording it: trials against a registry (DRKS,
   ClinicalTrials.gov, CTIS, WHO ICTRP) or the institution's page; papers against
   the DOI / journal / preprint page.
4. Update the JSON (set `first_seen`/`isNew` once, refresh `last_checked`, set
   top-level `last_check` + `last_run_at` (UTC timestamp with time), recompute
   trial `flags`), then run
   `python3 scripts/render_trials.py`, then append to `checks/CHANGELOG.md`.
5. Report newest-first: trials in two tiers (open, then planned), then papers —
   Wirth/Scheibenbogen first. If nothing changed, confirm in one line.

## Hard rules (always)

- **Scope filter — all must hold:** condition = ME/CFS · intervention =
  drug/pharmacological (immunoadsorption is borderline → include + note) ·
  German connection (≥1 site in Germany, or — for a planned study without
  confirmed sites — a German sponsor/institution) · status **`recruiting`**,
  **`enrolling_by_invitation`**, **or `not_yet_recruiting`** (planned/announced
  but not yet open). **All three statuses are relevant.**
- **Report in two tiers:** *open for enrollment* (recruiting / enrolling_by_invitation)
  first, then *planned / not yet recruiting* — both are surfaced, clearly labelled.
- **Prioritise** anything linked to **Klaus Wirth** or **Carmen Scheibenbogen**
  (`priority: "high"`), in either tier — e.g. **Mitodicure MDC002** is planned,
  not yet registered, and is still high priority and reported.
- **Never fabricate.** A trial enters `data/trials.json` only after confirmation
  from a registry **or** an official institutional/company page — the latter is
  often the only source for a *planned* study (e.g. Mitodicure's site for MDC002).
  News/blogs are leads, not evidence.
- **Papers track:** notable new ME/CFS research, prioritising Wirth/Scheibenbogen
  but **not** Germany-restricted; recent (~last 3 months / since `last_check`);
  confirmed via DOI/journal/preprint; `summary` + `why` written in **plain,
  layperson language** (minimal jargon, explained inline). → `data/papers.json`.
- **Never hand-edit `TRIALS.md` or `docs/dashboard.json`** — they are generated;
  edit the JSON and re-run the script.
- **Never delete** a trial that drops out of scope — update its status + flag it.
- Sources list is a **floor, not a ceiling**; add durable new sources you find.

## File map

`ROUTINE.md` procedure · `SETUP-ROUTINE.md` scheduled-run setup + canonical prompt ·
`sources/search-sources.md` where to look · `data/trials.json` + `data/papers.json`
sources of truth · `data/schema.json` field docs · `TRIALS.md` generated view ·
`docs/` GitHub Pages dashboard (`index.html` + generated `dashboard.json`) ·
`scripts/render_trials.py` renderer · `literature/papers/` per-paper PDF + summary +
BibTeX archive (`scripts/literature_intake.py`) · `templates/` entry skeletons ·
`checks/CHANGELOG.md` run log.
