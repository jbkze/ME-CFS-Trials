# Routine: ME/CFS research watch

The repeatable procedure for surfacing new ME/CFS **drug-trial opportunities in
Germany** and notable new **ME/CFS research papers**. Run it on each check
(manually, or as the scheduled Routine in `SETUP-ROUTINE.md`). It reads/writes
the files described in `README.md`. Each run surfaces only what is *new* or
*changed* since `last_check`.

Two tracks, two scopes: **trials** are Germany-focused and tightly filtered;
**papers** are broader (notable ME/CFS science, not Germany-restricted). Both
prioritise **Klaus Wirth** and **Carmen Scheibenbogen**.

## Scope — trials (the relevance filter)

A trial is **in scope** only if **all** of these hold:

1. **Condition** — ME/CFS (incl. post-COVID / post-infectious ME/CFS with PEM).
2. **Intervention** — a **drug / pharmacological** (or biologic) study. Apheresis
   such as immunoadsorption is borderline — include it, set `is_drug_study`
   by judgement, and say so in `notes`. Exclude pure exercise/diet/behavioural
   trials.
3. **Germany** — at least one site in Germany. For a *planned* study without
   confirmed sites yet, a German sponsor/institution (e.g. Charité, Mitodicure)
   satisfies this.
4. **Status** — **`recruiting`** / **`enrolling_by_invitation`** (open for
   enrollment) **or `not_yet_recruiting`** (planned / announced but not yet open).
   All three are in scope.

**Two reporting tiers.** Lead with **open for enrollment**, then **planned / not
yet recruiting**. Planned studies are genuinely relevant — they let patients and
clinicians prepare and catch the opening early — so report them (clearly labelled
as planned), don't hide them. Flag the moment one flips to recruiting (`newly_open`).

**Priority = HIGH** for any trial linked to **Klaus Wirth** or **Carmen
Scheibenbogen** (set `priority: "high"`, list them in `associated_researchers`),
in either tier — e.g. **Mitodicure MDC002** is planned and not yet registered,
but is still high priority and reported.

## Scope — papers

A paper is **in scope** if **all** hold:

1. **Topic** — ME/CFS (incl. post-COVID / post-infectious ME/CFS, PEM): patho-
   mechanism, biomarkers, drug targets, treatment / clinical-trial results, or
   genetics/epidemiology that bears on mechanism or treatment.
2. **Recency** — published or preprinted in roughly the **last 3 months**, or
   since `last_check`.
3. **Credibility** — a peer-reviewed journal or a major preprint server
   (medRxiv / bioRxiv). Skip predatory/marginal venues and purely tangential work.

Papers are **not** restricted to Germany (unlike trials). **Priority = HIGH** for
**Wirth**, **Scheibenbogen** and their groups/co-authors, but include other
notable ME/CFS science (e.g. DecodeME genetics, micro-clots, mitochondrial/muscle
findings). Confirm each via its **DOI / journal / preprint page**; news/blogs are
leads only — never fabricate.

**Write summaries for laypeople.** Both `summary` and `why` must be understandable
by someone with no medical background: short sentences, plain words, as many
technical terms as necessary but as few as possible — and when a term is
unavoidable, explain it in a few words right there (e.g. *"post-exertional malaise
(a crash after activity)"*, *"autoantibodies (antibodies that mistakenly attack the
body)"*). Avoid statistics, p-values, and acronyms unless essential. Aim for 1–2
short sentences each. The existing entries in `data/papers.json` are the style
reference — match their tone.

## Status vocabulary (trials)

`recruiting`, `not_yet_recruiting`, `enrolling_by_invitation`,
`active_not_recruiting`, `suspended`, `completed`, `terminated`, `withdrawn`,
`unknown`. (Aligned to ClinicalTrials.gov; map DRKS/CTIS wording onto these.)

## Procedure

1. **Read state.** Load `data/trials.json` **and** `data/papers.json`. Note
   `last_check` and the existing ids/statuses — your baseline for diffing.
2. **Search — trials.** Work through `sources/search-sources.md`: registries
   first (DRKS → ClinicalTrials.gov → CTIS → WHO ICTRP), then the Wirth and
   Scheibenbogen leads, then news sources for anything not yet registered.
3. **Search — papers.** Use the literature sources in `sources/search-sources.md`
   (PubMed / Europe PMC, medRxiv / bioRxiv, key journals) plus author searches for
   Wirth and Scheibenbogen, limited to roughly the last 3 months / since `last_check`.
   **The sources list is a floor, not a ceiling** — always also run fresh,
   open-ended web search for both tracks (new investigators, drugs, institutions,
   announcements, papers). Add durable new sources you find to the list.
4. **Confirm each candidate.** Trials: against a registry or the institution's own
   clinical-research page (for a *planned* study not yet registered, an official
   institutional/company announcement is acceptable — record it as
   `not_yet_recruiting` and link that source). Papers: against the DOI / journal /
   preprint page. Never enter anything on the basis of a blog post alone.
5. **Diff against the baseline** and compute `flags` for each in-scope trial:
   - `new` — `id` not present in the previous `data/trials.json`.
   - `newly_open` — status changed **into** `recruiting` / `enrolling_by_invitation`.
   - `status_changed` — any other status change (update `last_status_change`
     and append to `status_history`).
   - `closed_since_last` — was open last time, now closed/suspended/etc.
   - `details_changed` — material change (sites, eligibility, links) with same status.
   - (no flag) — unchanged since last check.
   For papers, mark `isNew: true` only if the `id` is new this run; set it back to
   `false` on later runs.
6. **Update files** (see below).
7. **Report** (see below).

## Updating the files

- **Trials:** add/update each record in `data/trials.json` following
  `data/schema.json` (copy `templates/trial-entry.json` for new ones). Set
  `first_seen` once (never overwrite); always refresh `last_checked` to today.
  Recompute `flags` every run (they describe change *since last check*, so a trial
  that was `new` last time and is unchanged now has its flags cleared). A trial
  that drops out of scope is **not deleted** — update its status, flag it
  `closed_since_last`, let it move to the archived section.
- **Papers:** add confirmed new papers to `data/papers.json` (copy
  `templates/paper-entry.json`): `title`, `authors`, `journal`, `date`, a one-line
  `summary`, a one-line `why` (why it matters), `link` (DOI), `first_seen`, and
  `isNew`. Write `summary` and `why` in **plain, layperson language** (see the
  style note under "Scope — papers"). Refresh its `isNew` flags as above.
- Set top-level `last_check` to today's date (YYYY-MM-DD) in both files, and set
  top-level `last_run_at` in `data/trials.json` to the current timestamp **with
  time** (UTC ISO-8601, e.g. `date -u +%FT%TZ` → `2026-06-25T14:21:48Z`). The
  dashboard localises this to the viewer's timezone and shows the time next to
  the date; `nextRun` is computed as `last_run_at + 1 day` (daily cadence).
- Regenerate the views: `python3 scripts/render_trials.py` — rebuilds both
  `TRIALS.md` and `docs/dashboard.json` (the feed for the GitHub Pages dashboard,
  `docs/index.html`; studies from `trials.json`, papers from `papers.json`).
- Append one entry to `checks/CHANGELOG.md` using the template at the top of that file.
- **Never hand-edit `TRIALS.md` or `docs/dashboard.json`** — they are generated.

## Reporting back

Lead with what changed, newest first, in two parts:

- **Trials** — two tiers: **open for enrollment** first, then **planned / not yet
  recruiting** (label which is which). For each new or changed trial give:
  **name · status · drug/intervention · patient eligibility · registration/source
  link.** Note any that **closed or changed status** since last check.
- **Papers** — **title · authors · journal · date · why it matters · DOI.**

Call out Wirth/Scheibenbogen explicitly in both parts (including planned trials).
If nothing is new or changed, say so in one line (e.g. *"No new or changed ME/CFS
drug trials in Germany and no notable new papers since 2026-06-25."*) — still bump
`last_check` and add a CHANGELOG line.

The full, self-contained prompt for both manual and scheduled runs lives in
**`SETUP-ROUTINE.md`** ("Routine prompt").

---

## Running headless (as a scheduled Routine)

When this runs unattended as a cloud **Routine** (see `SETUP-ROUTINE.md`), there
is no human in the loop, so two things differ from an interactive run:

1. **State must persist on the default branch.** Each run clones the repo fresh
   from the default branch, so the *previous* run's data is only visible if it was
   committed back to that branch. Therefore the run must **commit** the updated
   `data/trials.json`, `data/papers.json`, `TRIALS.md`, `docs/dashboard.json`, and
   `checks/CHANGELOG.md`. With *Allow unrestricted branch pushes* enabled it
   commits straight to the default branch (recommended — keeps the baseline
   current automatically). Without it, it pushes a `claude/` branch and opens a
   PR, and **you must merge that PR** before the next run or the baseline goes stale.
2. **Deliver the summary somewhere you'll see it**, since there's no chat reply
   to read. Open a GitHub issue titled `Research watch <YYYY-MM-DD>` with a Trials
   part (two tiers) and a Papers part (Wirth/Scheibenbogen first) — **only when
   something is new or changed.** When nothing changed, skip the issue: the
   committed CHANGELOG entry and the dashboard's updated "last run" date are the
   record. If issue creation isn't available, put the summary in the commit body.

Use the shell (`date +%F`) for today's date. The exact prompt to paste into the
Routine form is in `SETUP-ROUTINE.md`.
