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

## 2026-06-26
- Sources checked: ClinicalTrials.gov (Germany/ME/CFS, recruiting + not_yet_recruiting), DRKS, CTIS, WHO ICTRP, Mitodicure.com (accessible — no new announcement), Charité CFC, PubMed (Wirth/Scheibenbogen author searches + ME/CFS topic, Jun 2026), Europe PMC, medRxiv (403 blocked), Health Rising, The Sick Times, mecfs.de
- **Trials** — no new trials; both confirmed unchanged
  - New: none | Newly open: none | Status changed: none | Closed: none
  - MDC002 (Mitodicure): mitodicure.com accessible this run — still "advancing towards clinical trials," no new funding or registration announcement
  - Inebilizumab ME/CFS trial (Scheibenbogen/Charité): still unregistered — no DRKS or ClinicalTrials.gov entry found
  - NCT05710770 / NCT05629988: both completed predecessors to IMPACT; not added (superseded by NCT07529197)
- **Papers** — 3 new confirmed papers added (16 total)
  - Kim L, Scheibenbogen C et al., J Transl Med Jun 2026: hyperbaric oxygen therapy — symptoms + thalamic connectivity (PMID 42249466) — HIGH PRIORITY (Scheibenbogen co-author)
  - Huhmar HM et al., Endocr Pract Jun 2026: low vasopressin in ME/CFS (PMID 41475665)
  - Saleem S et al., Blood Coagul Fibrinolysis Jun 2026: dynamic microclot profiling in long COVID/ME/CFS (PMID 42274123)
- **One-time deep-research backfill (same day):** +26 verified landmark/notable ME/CFS papers (2011–2025) added as a historical library (isNew=false) — incl. Wirth/Scheibenbogen unifying-hypothesis (2020) & skeletal-muscle (2021), Loebel 2016 & Sotzny 2018 (Scheibenbogen), Haffke 2022 endothelial, Schreiner/Prusty HHV-6, DecodeME GWAS, NIH deep-phenotyping (Walitt 2024), Hornig/Lipkin 2015, Montoya 2017, Naviaux 2016, Fluge PDH/RituxME/cyclophosphamide, Systrom & Keller CPET, Giloteaux/Xiong microbiome, Esfandyarpour nanoneedle, Nakatomi PET, BioMapAI & cell-free-RNA (2025), Komaroff/Lipkin 2021, ICC (2011) & IOM/SEID (2015), Lim 2020 prevalence.
- Trials tracked: 2 (open: 1, watchlist: 1) | Papers tracked: 42 (3 new today + 39 library)
- Notes: All existing papers' isNew reset to false; only today's 3 new finds are flagged. ClinicalTrials.gov confirmed only NCT07529197 recruiting in Germany for ME/CFS drug studies. Landmark trial *results* (RituxME, BC007, cyclophosphamide) are recorded as papers, not in trials.json (which stays scoped to recruiting/planned German drug trials).

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
