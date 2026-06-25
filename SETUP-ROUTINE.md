# Set up the recurring run (cloud Routine)

The durable, unattended way to run this watch is a **Claude Code Routine** — it
runs on Anthropic's cloud on a schedule, with no machine or open session needed,
and clones this repo fresh each time. (The in-session `/loop` and `CronCreate`
tools are *not* durable: they expire after 7 days and die when the session ends.)

> **This last step is done in the web UI** — `claude.ai/code/routines`. Routines
> cannot be created from inside a Claude Code web session, so the steps below are
> for you to click through. Everything else is already prepared in this repo.

## Create it (≈2 minutes)

1. Go to **[claude.ai/code/routines](https://claude.ai/code/routines)** → **New routine**.
2. **Name:** `ME/CFS trial watch (Germany)`.
3. **Prompt:** paste the block under *"Routine prompt"* below.
4. **Repository:** select **`jbkze/me-cfs-trials`**.
5. **Environment / Network access — important:** the **Default** environment only
   allows package registries and blocks arbitrary sites, so trial registries
   (drks.de, clinicaltrials.gov, euclinicaltrials.eu, charite.de, mitodicure.com…)
   would return `403`. Edit the environment and set **Network access = Full**
   (simplest for open web research), or **Custom** with at least the domains
   listed in *"Network allowlist"* below.
6. **Trigger:** choose **Schedule → Weekly** (clinical registries move slowly;
   weekly is plenty. Minimum interval is 1 hour). Pick any weekday/time.
7. **Permissions:** enable **Allow unrestricted branch pushes** for this repo so
   the run can commit updated state to the default branch (see *State* below).
   If you'd rather review every change, leave it off and merge the PR it opens
   each week instead.
8. **Create.** Use **Run now** on the routine's page to test it immediately.

To change cadence later to something without a preset (e.g. every two weeks),
create it as Weekly, then run `/schedule update` in the Desktop/CLI app.

## Routine prompt

```text
Run the recurring ME/CFS research watch for this repository. You are an
autonomous cloud session with no human to reply to during the run — finish the
whole job and leave the results committed in the repo and summarised in a GitHub
issue. It covers two tracks: clinical trials (Germany-focused) and notable new
research papers (broader).

1. Read CLAUDE.md and ROUTINE.md in the repo root and follow ROUTINE.md exactly,
   including its "Running headless" section. data/trials.json and data/papers.json
   on the default branch are your baselines; data/schema.json defines the trial
   record format.

2. TRIALS — a trial qualifies only if ALL hold: condition is ME/CFS (incl.
   post-COVID/post-infectious ME/CFS); intervention is drug/pharmacological
   (immunoadsorption is borderline — include and note it); a German connection
   (a site in Germany, or — for a planned study without confirmed sites — a German
   sponsor/institution); status is "recruiting", "enrolling by invitation", OR
   "not_yet_recruiting" (planned/announced but not yet open). All three statuses
   are relevant. Prioritise Klaus Wirth (Mitodicure / MDC002 — planned, not yet
   registered, still report it) and Carmen Scheibenbogen (Charité Fatigue Centrum).
   Work through sources/search-sources.md AND do fresh open-ended web search.
   Confirm each candidate against a registry (DRKS, ClinicalTrials.gov, CTIS,
   WHO ICTRP) or an official institutional/company page (the only source for a
   planned study — record it as not_yet_recruiting and link it). Never fabricate.

3. PAPERS — also search for notable new ME/CFS research papers (pathomechanism,
   biomarkers, drug targets, treatment / clinical-trial results, genetics) from
   roughly the last 3 months or since the last check. Prioritise Wirth,
   Scheibenbogen and their groups, but papers are NOT restricted to Germany. Use
   PubMed / Europe PMC, medRxiv / bioRxiv, and the journals/leads in
   sources/search-sources.md. Confirm each via its DOI / journal / preprint page;
   news/blogs are leads only. Never fabricate. Write every paper's summary and
   "why it matters" in plain, layperson language: short sentences, minimal jargon,
   and explain any unavoidable technical term in a few words right there.

4. Update the data: in data/trials.json set first_seen once, refresh last_checked
   and top-level last_check to today (use `date +%F`), and recompute each trial's
   flags (new / newly_open / status_changed / closed_since_last / details_changed)
   vs the baseline. In data/papers.json add confirmed new papers (title, authors,
   journal, date, one-line summary, one-line "why it matters", DOI link, first_seen,
   isNew) and refresh last_check. Then run `python3 scripts/render_trials.py` — this
   rebuilds TRIALS.md AND docs/dashboard.json (the GitHub Pages dashboard feed).
   Prepend a dated entry to checks/CHANGELOG.md.

5. Persist state — essential, because the next run re-clones the default branch:
   commit data/trials.json, data/papers.json, TRIALS.md, docs/dashboard.json and
   checks/CHANGELOG.md to the default branch with message
   "Research watch <YYYY-MM-DD>: T new/changed trials, P new papers". If you
   cannot push to the default branch, push a claude/ branch and open a PR with the
   same summary.

6. Deliver: if anything is new or changed, open a GitHub issue titled
   "Research watch <YYYY-MM-DD>" with two parts — TRIALS (two tiers: OPEN FOR
   ENROLLMENT first, then PLANNED / NOT YET RECRUITING, labelled; each with name,
   status, drug/intervention, key eligibility, registration/source link; note any
   that closed or changed status) and PAPERS (title · authors · journal · date ·
   why-it-matters · DOI) — Wirth/Scheibenbogen first in both. If issue creation
   isn't available to you, put the same summary in the commit body. If nothing is
   new or changed, do NOT open an issue — the committed CHANGELOG entry and the
   dashboard's updated "last run" date are the record.
```

## Network allowlist (if you choose Custom instead of Full)

```
drks.de, clinicaltrials.gov, euclinicaltrials.eu, trialsearch.who.int,
charite.de, cfc.charite.de, mitodicure.com, ncbi.nlm.nih.gov,
pubmed.ncbi.nlm.nih.gov, europepmc.org, medrxiv.org, biorxiv.org,
scholar.google.com, doi.org, mecfs.de, healthrising.org, thesicktimes.org
```

Custom is tighter but will miss any source not on the list; **Full** is
recommended for open-ended web research. (Either way, leave "include default
package managers" checked.)

## State persistence — why it matters

A Routine clones the **default branch** on every run, so it only "remembers"
what previous runs committed there. That's why step 5 commits the updated data.
With *Allow unrestricted branch pushes* on, the run commits to `main` directly.
With it off, the run opens a PR instead — and an **auto-merge workflow**
(`.github/workflows/auto-merge-routine.yml`) merges that PR into `main`
automatically, so the dashboard still updates and the baseline stays current with
no manual step. The workflow only touches the routine's own PRs (same-repo
`claude/*` branch, "Trial watch"/"Research watch" title) and leaves any PR with a
real merge conflict open for you to resolve. Enabling the setting is still
slightly cleaner (no PR churn at all), but is no longer required for the dashboard
to keep working.

## Publish the dashboard (GitHub Pages) — one-time

The dashboard lives in `docs/` (`index.html` + the generated `dashboard.json`).
To put it online, enable Pages once:

1. Repo → **Settings → Pages**.
2. **Source:** *Deploy from a branch* → **Branch:** your default branch →
   **Folder:** **`/docs`** → **Save**.
3. After a minute it's live at **`https://jbkze.github.io/ME-CFS-Trials/`**
   (the repo-name path is **case-sensitive** — keep `ME-CFS-Trials` exactly).

From then on it updates itself: each routine run regenerates and commits
`docs/dashboard.json`, and Pages redeploys automatically. (`docs/.nojekyll` is
included so GitHub serves the files as-is without Jekyll processing.)

## Notes & limits

- Routines need a Pro / Max / Team / Enterprise plan with Claude Code on the web.
- They draw on your normal subscription usage and have a daily run cap.
- Each run appears as a session under claude.ai/code — open it to see exactly
  what Claude did (a green status only means it ran, not that it found something).
- To pause: toggle **Repeats** off on the routine's page. To stop: delete it
  (past run sessions are kept).

## Alternative: GitHub Actions

If you'd prefer the schedule to live entirely in this repo (version-controlled,
no web-UI step), it can instead run as a `schedule`-triggered GitHub Actions
workflow. That needs an `ANTHROPIC_API_KEY` secret (API billing, separate from
your subscription) and Actions enabled. Ask and this can be added as
`.github/workflows/`.
