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

## 2026-06-25 (trial watch — first search)
- Sources checked: ClinicalTrials.gov API (ME/CFS + Germany, all open statuses), DRKS (search), CTIS, WHO ICTRP, Mitodicure.com, Charité CFC clinical research page, PubMed/Health Rising/The Sick Times (4th International ME/CFS Conference, Berlin, May 2026), mecfs-research.org, Science for ME forum
- New: **IMPACT** (NCT07529197) — Scheibenbogen immunoadsorption observational study, recruiting since March 2026
- New: **MDC002 Phase 1** (mitodicure-mdc002-ph1) — Klaus Wirth / Mitodicure GmbH, pre-clinical / advancing to trials
- Newly open: none beyond what's listed above
- Status changed: n/a (first real run, no baseline)
- Closed since last: n/a
- Trials tracked: 2 (open: 1, watchlist: 1, archived: 0)
- Notes: Several recent completions noted as context (not tracked — out of scope): IA-PACS-CFS (NCT05710770, completed Oct 2025, no significant IA benefit vs sham), Trial RIA (NCT05629988, completed Mar 2025), BIAKI/DRKS00032963 (pediatric IA, Flensburg, discontinued), reCOVer/BC007 (Erlangen, completed Sep 2024, some positive signal). VERI-LONG (NCT05697640, vericiguat, Charité, active not recruiting — enrolled, awaiting results). No German rituximab, daratumumab, LDN, or efgartigimod ME/CFS drug trials currently recruiting. **Unconfirmed lead (not entered):** Scheibenbogen announced an inebilizumab (anti-CD19) pilot (~15 ME/CFS patients, IA-responders only, federal funding) at the 4th ME/CFS Conference Berlin May 2026 — source is a news article (The Sick Times), not a registry or institutional trial page; will enter once a DRKS/NCT ID or official CFC page is found.

## 2026-06-25
- **Repository / routine set up.** No trial search performed yet — `data/trials.json`
  intentionally starts empty so the first real check flags every in-scope trial as `new`.
- Leads pre-loaded into `sources/search-sources.md`: Mitodicure **MDC002** (Klaus Wirth;
  trials in planning), Charité immunoadsorption / **NCT07529197** & Trial RIA and
  **BC007** (Carmen Scheibenbogen).
- Trials tracked: 0 (open: 0, watchlist: 0)
- Next: run the routine to perform the first real check.
