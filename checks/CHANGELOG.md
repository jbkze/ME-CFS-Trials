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

## 2026-06-26 (one-time deep-research backfill — papers)
- One-time comprehensive backfill of the ME/CFS research literature via deep web research; **every paper verified via DOI/PubMed/journal**. Not a routine trial check.
- **Papers: +26 landmark/notable papers (2011–2025)** added → **39 total**. All set `isNew: false` (historical library baseline; the "New" badge is reserved for genuine new finds in future daily runs, so the counter reads 0).
- Added (selection): Wirth/Scheibenbogen *Unifying Hypothesis* (2020) & skeletal-muscle (2021); Loebel 2016 & Sotzny 2018 autoimmunity (Scheibenbogen); Haffke 2022 endothelial; Schreiner/Prusty 2020 HHV-6; DecodeME GWAS (2025); NIH deep-phenotyping (Walitt 2024); Hornig/Lipkin 2015; Montoya 2017; Naviaux 2016; Fluge PDH 2016, RituxME 2019, cyclophosphamide 2020; Systrom 2021 & Keller 2014 CPET; Giloteaux 2016 & Xiong 2023 microbiome; Esfandyarpour 2019 nanoneedle; Nakatomi 2014 PET; BioMapAI (Xiong 2025); cell-free RNA (Gardella 2025); Komaroff/Lipkin 2021; ICC (Carruthers 2011); IOM/SEID (2015); Lim 2020 prevalence.
- **Trials: unchanged** (2 tracked — IMPACT recruiting, MDC002 planned). Scope stays per ROUTINE.md (Germany drug trials); landmark trial *results* (RituxME, BC007, etc.) are recorded as papers, not in trials.json.
- Papers tracked: 39 | Trials tracked: 2 (open: 1, watchlist: 1)
- Notes: top-level `last_check`/`last_run_at` bumped to 2026-06-26 to reflect today's data refresh. Future daily runs resume normal "new since last check" flagging.

## 2026-06-25 (second run — papers track)
- Sources checked: ClinicalTrials.gov API (ME/CFS + Germany), DRKS, CTIS, WHO ICTRP, Mitodicure.com (unreachable — site down), Charité CFC, PubMed (Wirth/Scheibenbogen author + ME/CFS topic queries), Europe PMC, medRxiv
- **Trials** — no new trials; both confirmed unchanged (flags cleared)
  - New: none | Newly open: none | Status changed: none | Closed: none
- **Papers** — 4 new confirmed papers added to existing 9 (13 total)
  - Fehrer A et al., Autoimmun Rev May 2026: CFC 3rd Conference expert perspectives (PMID 41895458)
  - Esteban DJ et al., Microbiologyopen Jun 2026: gut tryptophan/AhR metabolism (PMID 42325052)
  - Thomas N et al., Front Neuroendocrinol Jun 2026: chronobiological neuroendocrinology framework (PMID 42320559)
  - Brown M et al., J Transl Med Jun 2026: GI symptoms and systemic inflammation (PMID 42321833)
- Trials tracked: 2 (open: 1, watchlist: 1) | Papers tracked: 13
- Notes: Mitodicure.com timed out — MDC002 status presumed unchanged. Inebilizumab pilot (Scheibenbogen, announced May 2026) still unregistered — watching. No new German drug trials in any registry.

## 2026-06-25 (Research watch — first real check)
- Sources checked: ClinicalTrials.gov API (Germany/ME/CFS filter), DRKS search, Mitodicure website, Charité CFC clinical research pages, The Sick Times ME/CFS Conference roundup (May 2026), PubMed, Europe PMC, Health Rising, mecfs-research.org
- New trials: **NCT07529197 (IMPACT)** — Scheibenbogen immunoadsorption at Charité, recruiting | **mitodicure-mdc002-ph1** — MDC002 (Klaus Wirth), planned/not yet registered
- Newly open: NCT07529197 (first check; flagged `new`)
- Status changed: none (first check)
- Closed since last: none (first check)
- Trials tracked: 2 (open: 1, watchlist: 1)
- New papers: 9 — including Wirth/Scheibenbogen 2026 neurotransmitter review (IJMS Apr 2026); Cell Reports Medicine serum proteomics (Hoel et al. Mar 2026); daratumumab pilot (Fluge et al. Jul 2025); BC007/reCOVer RCT (Hohberger et al. Jul 2025); CSF proteomics (Bragée et al. Sci Rep 2026); PEM pathophysiology (Jin et al. Apr 2026); TRPM3 (Sasso et al. Jan 2026); IL-11/MMP-9 (Chinnappan et al. Jun 2026); Wirth/Scheibenbogen skeletal muscle review (J Cachexia Feb 2025)
- Notes: VERI-LONG (NCT05697640, vericiguat, Charité) is active_not_recruiting as of Jan 2026 — out of scope (completed enrollment); results pending. IA-PACS-CFS sham-controlled immunoadsorption trial at Charité completed with negative result (May 2026 conference). PoCoVIT (methylprednisolone, NCT05986422) terminated Mar 2025 due to serious adverse events. Rituximab trial NCT06952413 is Japan-only. Inebilizumab ME/CFS trial at Charité mentioned at May 2026 conference but no registry entry found yet.

## 2026-06-25 (setup)
- **Repository / routine set up.** No trial search performed yet — `data/trials.json`
  intentionally starts empty so the first real check flags every in-scope trial as `new`.
- Leads pre-loaded into `sources/search-sources.md`: Mitodicure **MDC002** (Klaus Wirth;
  trials in planning), Charité immunoadsorption / **NCT07529197** & Trial RIA and
  **BC007** (Carmen Scheibenbogen).
- Trials tracked: 0 (open: 0, watchlist: 0)
- Next: run the routine to perform the first real check.
