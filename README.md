# ME-CFS-Trials

A small tracking system for a recurring task: **finding new clinical-trial
opportunities for ME/CFS patients in Germany** — drug studies, open for
enrollment, with a focus on the research of **Klaus Wirth** (Mitodicure / MDC002)
and **Carmen Scheibenbogen** (Charité Fatigue Centrum).

The point of this repo is to make each check **fast and stateful**: it remembers
what was found last time so a run only has to surface what is *new* or *changed*.

## How a check works

1. The routine reads `data/trials.json` (what we already know).
2. It searches the registries and leads in `sources/search-sources.md`.
3. It updates the JSON, regenerates `TRIALS.md`, and logs the run.
4. It reports new/changed trials — or confirms briefly that nothing changed.

Full procedure and the copy-paste prompt: **[`ROUTINE.md`](ROUTINE.md)**.

## File structure

| Path | Role |
|---|---|
| **`ROUTINE.md`** | The playbook — scope rules, status vocabulary, step-by-step procedure, and the prompt to paste for a check. Start here. |
| **`sources/search-sources.md`** | Durable "where to look": registries (DRKS, ClinicalTrials.gov, CTIS, WHO ICTRP), the Wirth & Scheibenbogen leads, and reusable search queries. |
| **`data/trials.json`** | **Source of truth** — structured state of every known trial. Enables "new / changed since last check". Starts empty. |
| **`data/schema.json`** | JSON Schema documenting every field in a trial record. |
| **`TRIALS.md`** | Human-readable table, **auto-generated** from `data/trials.json`. Don't edit by hand. |
| **`scripts/render_trials.py`** | Regenerates `TRIALS.md` from the JSON (Python stdlib only). |
| **`templates/trial-entry.json`** | Copy-paste skeleton for a new trial record. |
| **`checks/CHANGELOG.md`** | Append-only log, one entry per check — the human-readable "since last time". |

## Quickstart

```bash
# See the current tracker
cat TRIALS.md

# After editing data/trials.json, refresh the human-readable view
python3 scripts/render_trials.py
```

To run a check, open [`ROUTINE.md`](ROUTINE.md) and follow it (or paste its
"prompt for a check" to Claude).

## Design notes

- **JSON is the source of truth; Markdown is generated.** Avoids the two copies
  drifting apart — only `data/trials.json` is edited, `TRIALS.md` is rebuilt.
- **State is never silently deleted.** A trial that closes is updated and flagged,
  not removed, so history (`status_history`, `first_seen`) survives.
- **Leads ≠ confirmed trials.** Blog/news leads live in `sources/`; a record only
  enters `data/trials.json` once confirmed against a registry or the institution.
- **Empty baseline is intentional.** The first real check legitimately discovers
  everything as `new`; nothing here is fabricated trial data.
