# CLAUDE.md

Standing orders for this repo. Auto-loaded every session. The detailed procedure
lives in `ROUTINE.md` — **this file is the gist + the instruction to read it.**

## What this repo is

A stateful tracker for **new ME/CFS clinical-trial opportunities in Germany**:
drug studies, open for enrollment, prioritising the research of **Klaus Wirth**
(Mitodicure / MDC002) and **Carmen Scheibenbogen** (Charité Fatigue Centrum).
Each run should surface only what is *new* or *changed* since `last_check`.

## When asked to "run a check" / "Studien-Check" / "trial watch"

**Read `ROUTINE.md` first and follow it exactly.** It is authoritative if anything
below is ambiguous. In short:

1. Load `data/trials.json` as the baseline (existing ids + statuses).
2. Search the sources in `sources/search-sources.md` **and** do fresh open-ended
   web search beyond that list (it is a checklist, not a limit).
3. Confirm every candidate against a registry (DRKS, ClinicalTrials.gov, CTIS,
   WHO ICTRP) or the institution's own page before recording it.
4. Update `data/trials.json` (set `first_seen` once, refresh `last_checked`, set
   top-level `last_check`, recompute `flags`), then run
   `python3 scripts/render_trials.py`, then append to `checks/CHANGELOG.md`.
5. Report new/changed trials newest-first (name · status · intervention ·
   eligibility · link), Wirth/Scheibenbogen first. If nothing changed, confirm in
   one line.

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
- **Never hand-edit `TRIALS.md`** — it is generated; edit the JSON and re-run the script.
- **Never delete** a trial that drops out of scope — update its status + flag it.
- Sources list is a **floor, not a ceiling**; add durable new sources you find.

## File map

`ROUTINE.md` procedure · `sources/search-sources.md` where to look ·
`data/trials.json` source of truth · `data/schema.json` field docs ·
`TRIALS.md` generated view · `scripts/render_trials.py` renderer ·
`templates/trial-entry.json` skeleton · `checks/CHANGELOG.md` run log.
