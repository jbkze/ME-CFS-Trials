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
Run the recurring ME/CFS clinical-trial watch for this repository. You are an
autonomous cloud session with no human to reply to — finish the whole job and
leave the results in the repo and a GitHub issue.

1. Read CLAUDE.md and ROUTINE.md in the repo root and follow ROUTINE.md exactly,
   including its "Running headless" section. data/trials.json on the default
   branch is your baseline of previously-known trials.
2. Scope (all must hold): ME/CFS; drug/pharmacological intervention; at least one
   recruiting site in Germany; status recruiting or enrolling-by-invitation.
   Prioritise trials linked to Klaus Wirth (Mitodicure / MDC002) or Carmen
   Scheibenbogen (Charité Fatigue Centrum). Search sources/search-sources.md AND
   do fresh open-ended web search. Confirm every candidate against a registry
   (DRKS, ClinicalTrials.gov, CTIS, WHO ICTRP) or the institution's own page
   before recording it. Never fabricate a trial.
3. Update data/trials.json per data/schema.json: set first_seen once, refresh
   last_checked to today (use `date +%F`), set top-level last_check to today,
   and recompute each trial's flags (new / newly_open / status_changed /
   closed_since_last) versus the baseline. Then run
   `python3 scripts/render_trials.py` (this rebuilds both TRIALS.md and
   docs/dashboard.json, the feed for the GitHub Pages dashboard) and prepend a
   dated entry to checks/CHANGELOG.md. Optionally also record notable new papers
   in data/papers.json (same confirm-first rule) — they show on the dashboard's
   Papers tab.
4. Persist state: commit data/trials.json, data/papers.json, TRIALS.md,
   docs/dashboard.json and checks/CHANGELOG.md to the default branch with
   message "Trial watch <YYYY-MM-DD>: N new, M changed".
   (If you cannot push to the default branch, push a claude/ branch and open a PR
   with the same summary.) This is essential — the next run reads the baseline
   from the default branch.
5. Deliver the summary: open a GitHub issue titled "Trial watch <YYYY-MM-DD>"
   listing new and changed trials newest-first — name, enrollment status,
   drug/intervention, key eligibility, and registration link — with
   Wirth/Scheibenbogen trials first. If nothing is new or changed, still do steps
   3–4 and post a one-line issue comment / note saying no new or changed ME/CFS
   drug trials in Germany since the last check.
```

## Network allowlist (if you choose Custom instead of Full)

```
drks.de, clinicaltrials.gov, euclinicaltrials.eu, trialsearch.who.int,
charite.de, cfc.charite.de, mitodicure.com, ncbi.nlm.nih.gov,
pubmed.ncbi.nlm.nih.gov, mecfs.de, healthrising.org, thesicktimes.org
```

Custom is tighter but will miss any source not on the list; **Full** is
recommended for open-ended web research. (Either way, leave "include default
package managers" checked.)

## State persistence — why it matters

A Routine clones the **default branch** on every run, so it only "remembers"
what previous runs committed there. That's why step 4 commits the updated
`data/trials.json`. With *Allow unrestricted branch pushes* on, this is automatic.
With it off, the run opens a PR instead and **you must merge it** before the next
run, or the "new / changed since last check" detection silently resets.

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
