# Check log

Append-only record of each run of the routine, newest first. One entry per check.
This is the "since last check" memory in human-readable form (the machine version
is `last_check` + `flags` in `data/trials.json`).

<!-- TEMPLATE — copy this block to the top for each new check:
## YYYY-MM-DD
- Sources checked: DRKS, ClinicalTrials.gov, CTIS, WHO ICTRP, Mitodicure, Charité CFC, …
- New: <trial name + id> — <one line> | none
- Newly open: <…> | none
- Status changed: <trial — old → new> | none
- Closed since last: <…> | none
- Trials tracked: N (open: M, watchlist: W)
- Notes: <anything notable, dead ends, things to revisit>
-->

## 2026-06-25
- **Repository / routine set up.** No trial search performed yet — `data/trials.json`
  intentionally starts empty so the first real check flags every in-scope trial as `new`.
- Leads pre-loaded into `sources/search-sources.md`: Mitodicure **MDC002** (Klaus Wirth;
  trials in planning), Charité immunoadsorption / **NCT07529197** & Trial RIA and
  **BC007** (Carmen Scheibenbogen).
- Trials tracked: 0 (open: 0, watchlist: 0)
- Next: run the routine to perform the first real check.
