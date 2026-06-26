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

## 2026-06-26 (correction — intake-standard tightening)
- **Two trials removed:** `nksg-inebilizumab-ph2` (Inebilizumab Ph2, Charité NKSG) and `charite-semaglutide-glp1` (Semaglutide, Scheibenbogen) deleted from `data/trials.json`.
  - Reason: both were sourced solely from a general therapy-overview page (mecfs.de/therapie) and a grant-announcement page (solvecfs.org/catalyst-awards) respectively — neither has a dedicated trial-specific registry entry or a named clinical-research subpage. Under the tightened intake standard these are *leads only*, not confirmation.
  - Both trials remain scientific leads: if/when a DRKS/NCT registration or a dedicated Charité CFC trial subpage appears, they can be re-added.
- **ROUTINE.md + CLAUDE.md updated:** confirmation standard for `not_yet_recruiting` planned trials now explicitly requires either (a) a registry entry or (b) a dedicated trial-specific institutional/company page — general overview pages, grant announcements, and press releases are leads only.
- Trials tracked: 2 (open: 1 [NCT07529197], watchlist: 1 [MDC002])
- Papers: unchanged (47 total)

## 2026-06-26 (run 3 — scheduled autonomous, 14:12 UTC)
- Sources checked: ClinicalTrials.gov (Germany/ME/CFS all statuses), DRKS, CTIS, WHO ICTRP, Mitodicure.com/pipeline, Charité CFC, mecfs.de/therapie, mecfs-research.org/researchupdate, PubMed (ME/CFS 2026 + author searches), medRxiv, bioRxiv, Health Rising, The Sick Times, riffreporter.de (BC007/APTA)
- **Trials** — no new in-scope trials; all 4 existing trials verified unchanged
  - NCT07529197 (IMPACT): still recruiting (Scheibenbogen immunoadsorption, Charité) [HIGH PRIORITY]
  - MDC002 (Mitodicure): still pre-clinical/not_yet_recruiting [HIGH PRIORITY]
  - Inebilizumab Phase 2 (Scheibenbogen/NKSG): still not_yet_recruiting
  - Semaglutide GLP-1 (Scheibenbogen/Charité): still not_yet_recruiting
  - Flags cleared: new flags removed from inebilizumab and semaglutide (no longer new this run)
  - Notable: Daratumumab CTIS 2024-520094-13-00 (ResetME Phase 2, 66 pts) confirmed Norway-only — no German sites; out of scope
  - Notable: RAPID REVIVE (vidofludimus, CTIS 2024-511628-16-00, Frankfurt) — German multicenter but fully recruited (active_not_recruiting); out of scope for enrollment tracker
  - Notable: BC007/rovunaptabin ME/CFS study (APTA Therapeutics, Erlangen) planned for 2026 — news lead only (riffreporter.de), no registry ID or official institutional page yet; not added until confirmed
- **Papers** — 4 new confirmed papers added (47 total; 3 with PDF, 1 no OA PDF)
  - Eckey M et al., PNAS Jul 2025: patient-reported treatment outcomes in ME/CFS + long COVID, 3,925 patients, 150+ treatments — PMID 40627388 (missed in June 26 backfill)
  - Che X, Lipkin WI et al., npj Metab Health Dis Sep 2025: heightened innate immunity triggers PEM in ME/CFS; metformin/rapamycin suggested — DOI 10.1038/s44324-025-00079-w (missed in June 26 backfill)
  - Hunter E et al., J Transl Med Oct 2025: EpiSwitch blood test, 96% accuracy for ME/CFS diagnosis — PMID 41057909 (missed in June 26 backfill)
  - Donchev D et al., Biomedicines May 2026: comparative gut microbiome ME/CFS vs long COVID — DOI 10.3390/biomedicines14061183 (new)
  - isNew cleared on fano-illic-2026-skeletal-muscle (no longer new this run)
- Trials tracked: 4 (open: 1 [NCT07529197], watchlist: 3 [MDC002 + inebilizumab Phase 2 + semaglutide])
- Notes: Nationale Dekade gegen Postinfektiöse Erkrankungen (NDPE) first funding call opened June 1, 2026 (deadline Sep 2, 2026) — new drug trials may emerge Q4 2026/Q1 2027. Watch for BC007/APTA Therapeutics official announcement and daratumumab expansion to German sites.

## 2026-06-26 (run 2 — correction, commit 52de042)
- Correction to afternoon run below: VERI-LONG (NCT05697640, active_not_recruiting) removed from trials.json — status was never in the allowed intake set (recruiting / enrolling_by_invitation / not_yet_recruiting); TRIALS.md and dashboard.json regenerated
- BibTeX key corrected: `fanò-illic2026` → `fano2026` (ASCII-safe, surnameYYYY convention); author format fixed: `Surname Initial` → `Surname, Initial`; summary frontmatter id/bibtex_key updated to match
- `scripts/literature_intake.py` `surname()` function updated to strip accents via NFKD normalisation and take only the first hyphen-segment — ensures the script produces `fano2026` deterministically on future runs
- Trials tracked: 4 (open: 1 [NCT07529197], watchlist: 3 [MDC002 + inebilizumab Phase 2 + semaglutide])

## 2026-06-26 (run 2 — afternoon, 13:42 UTC)
- Sources checked: ClinicalTrials.gov (Germany/ME/CFS, all statuses incl. active_not_recruiting), DRKS (DRKS00032963 found — pediatric IA, permanently halted), CTIS (daratumumab Phase 2 2024-520094-13-00 noted, German sites unconfirmed), Mitodicure.com/pipeline (still pre-clinical, no change), Charité CFC (trial_veri_long page), ME/CFS Research Registry (mrr.mecfs-research.org), mecfs.de/therapie, Solve ME Catalyst Awards, BMFTR, The Sick Times international conference roundup (May 2026), PubMed/medRxiv/bioRxiv, Diagnostics MDPI
- **Trials** — 3 new trials added (5 total now: open: 1, watchlist: 4)
  - New (not_yet_recruiting): nksg-inebilizumab-ph2 — Inebilizumab (Uplizna) Phase 2, Charité NKSG, Scheibenbogen PI; BMFTR-funded January 2026 (€18M); IA-responders only; not yet registered [HIGH PRIORITY]
  - New (not_yet_recruiting): charite-semaglutide-glp1 — Semaglutide GLP-1 agonist study, Scheibenbogen/Charité; Solve ME Catalyst Award February 2026; not yet registered [HIGH PRIORITY]
  - New (active_not_recruiting): nct05697640 VERI-LONG — Vericiguat Phase 2a, Charité Berlin; started June 2023; 104 patients; enrollment complete; results expected 2026; out-of-scope for enrollment but tracked for results
  - Unchanged: NCT07529197 (IMPACT) still recruiting; MDC002 still pre-clinical
  - Notable: DRKS00032963 (BIAKI pediatric IA, Flensburg) — recruitment permanently halted; out of scope (apheresis + paediatric); not added
  - Notable: daratumumab Phase 2 CTIS 2024-520094-13-00 (KTS-11-2024) mentioned as recruiting on mecfs.de; German sites unconfirmed; not added pending confirmation
- **Papers** — 1 new confirmed paper added (43 total)
  - Fanò-Illic G et al., Diagnostics Mar 2026: skeletal muscle pathophysiology, translational, and diagnostic aspects of ME/CFS — DOI 10.3390/diagnostics16071019
  - isNew cleared for 3 morning-run papers (kim-2026-hbot-mecfs, huhmar-2026-vasopressin, saleem-2026-microclots)
- Trials tracked: 5 (open: 1 [NCT07529197], watchlist: 4 [MDC002 + 2 unregistered planned + VERI-LONG])
- Notes: International ME/CFS Conference (May 2026, Berlin) reported null results for IA-PACS-CFS (sham-controlled IA RCT), PoCoVIT (methylprednisolone stopped early), LDN RCT (failed primary endpoint), Myoflame-19 (failed). Inebilizumab Phase 2 and semaglutide study are the two most important new planned trials — both Scheibenbogen/Charité, both awaiting registry. VERI-LONG (vericiguat) is the first German drug RCT in post-COVID/ME/CFS; results in 2026 will be landmark.

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
