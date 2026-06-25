# Routine: ME/CFS trial watch

The repeatable procedure for finding new ME/CFS drug-trial opportunities in
Germany. Run it on each check (manually, or paste the prompt below to Claude).
It reads/writes the files described in `README.md`.

## Scope (the relevance filter)

A trial is **in scope** only if **all** of these hold:

1. **Condition** — ME/CFS (incl. post-COVID / post-infectious ME/CFS with PEM).
2. **Intervention** — a **drug / pharmacological** (or biologic) study. Apheresis
   such as immunoadsorption is borderline — include it, set `is_drug_study`
   by judgement, and say so in `notes`. Exclude pure exercise/diet/behavioural
   trials.
3. **Germany** — at least one recruiting **site in Germany**.
4. **Open for enrollment** — status is **`recruiting`** or
   **`enrolling_by_invitation`**. Nothing else counts as "open".

**Priority = HIGH** for any trial linked to **Klaus Wirth** or **Carmen
Scheibenbogen** (set `priority: "high"`, list them in `associated_researchers`).
These get reported first even if only on the watchlist.

**Watchlist** — trials that are relevant but `not_yet_recruiting` (e.g. a Wirth /
Mitodicure Phase 1 in planning). Keep them in `data/trials.json` so the next run
catches the moment they open. Do **not** report them as "open opportunities".

## Status vocabulary

`recruiting`, `not_yet_recruiting`, `enrolling_by_invitation`,
`active_not_recruiting`, `suspended`, `completed`, `terminated`, `withdrawn`,
`unknown`. (Aligned to ClinicalTrials.gov; map DRKS/CTIS wording onto these.)

## Procedure

1. **Read state.** Load `data/trials.json`. Note `last_check` and the existing
   trials (their `id` and `status`) — this is your baseline for diffing.
2. **Search.** Work through `sources/search-sources.md`: registries first
   (DRKS → ClinicalTrials.gov → CTIS → WHO ICTRP), then the Wirth and
   Scheibenbogen leads, then news sources for anything not yet registered.
   **That list is a floor, not a ceiling** — always also run fresh, open-ended
   web searches each time (new investigators, new drug names, new institutions,
   newer announcements). The curated sources guarantee coverage of the basics;
   they do not limit where you may look. If you discover a durable new source,
   add it to `sources/search-sources.md`.
3. **Confirm each candidate** against a registry or the institution's own
   clinical-research page before trusting it. Never enter a trial on the basis
   of a blog post alone.
4. **Diff against the baseline** and compute `flags` for each in-scope trial:
   - `new` — `id` not present in the previous `data/trials.json`.
   - `newly_open` — status changed **into** `recruiting` / `enrolling_by_invitation`.
   - `status_changed` — any other status change (update `last_status_change`
     and append to `status_history`).
   - `closed_since_last` — was open last time, now closed/suspended/etc.
   - `details_changed` — material change (sites, eligibility, links) with same status.
   - (no flag) — unchanged since last check.
5. **Update files** (see below).
6. **Report** (see below).

## Updating the files

- For each in-scope trial, add or update its record in `data/trials.json`
  following `data/schema.json`. Copy `templates/trial-entry.json` as a starting
  point for new ones. Set `first_seen` once (never overwrite it); always refresh
  `last_checked` to today.
- Set top-level `last_check` to today's date (YYYY-MM-DD).
- Recompute `flags` every run (they describe change *since last check*, so a
  trial that was `new` last time and is unchanged now should have its flags cleared).
- Regenerate the human view: `python3 scripts/render_trials.py`.
- Append one entry to `checks/CHANGELOG.md` using the template at the top of that file.
- A trial that drops out of scope (e.g. closed) is **not deleted** — update its
  status, flag it `closed_since_last`, and let it move to the archived section.

## Reporting back

Lead with what changed, newest first. For each new or changed trial give:
**trial name · enrollment status · drug/intervention · patient eligibility ·
registration link.** Call out Wirth/Scheibenbogen trials explicitly.

If nothing changed since `last_check`, say so in one line (e.g. *"No new or
changed ME/CFS drug trials in Germany since 2026-06-25; N trials still tracked,
M open for enrollment."*) — still bump `last_check` and add a CHANGELOG line.

---

## Copy-paste prompt for a check

> Run the ME/CFS trial watch in this repo. Follow `ROUTINE.md`: load
> `data/trials.json` as the baseline, search the sources in
> `sources/search-sources.md` (Germany only, ME/CFS drug studies, open for
> enrollment, prioritising Klaus Wirth and Carmen Scheibenbogen), confirm each
> candidate against a registry, then update `data/trials.json`
> (set `last_check`, recompute `flags`), run `python3 scripts/render_trials.py`,
> and append to `checks/CHANGELOG.md`. Report new/changed trials newest-first
> with name, status, intervention, eligibility, and link — or confirm briefly if
> nothing changed.
