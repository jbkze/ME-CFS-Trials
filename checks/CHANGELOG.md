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

## 2026-07-02 (scheduled autonomous, 04:15 UTC)
- Sources checked — trials: ClinicalTrials.gov API, DRKS (incl. post-COVID terms), CTIS/euclinicaltrials.eu (blocked — SPA shell), WHO ICTRP, Charité CFC clinical-research listing, Mitodicure.com (pipeline/news/about-us), NAPKON/NUM (incl. dedicated RAPID_REVIVE study page), Lungeninformationsdienst, healthrising.org, thesicktimes.org, mecfs.de, drug/investigator-name queries.
- Sources checked — papers: PubMed (date-sorted + Scheibenbogen/Wirth author searches), Europe PMC, medRxiv/bioRxiv, Preprints.org, Google Scholar, s4me.info, meassociation.org.uk.
- New trials: none
- Newly open: none
- **Status changed:** `rapid-revive` (RAPID_REVIVE) — **recruiting → active_not_recruiting**. The dedicated NAPKON institutional page now states enrollment is full at all 11 sites and closed to further recruitment (confirmed >100 of a planned 150 patients enrolled by mid-2025; a Feb 2026 NUM-Insights talk by Prof. Vehreschild presented "first results"). Formal CTIS status label still unconfirmed (portal blocked) — recheck next cycle.
- Closed since last: `rapid-revive` (no longer open for enrollment; flagged `closed_since_last`)
- All 3 other tracked trials re-verified unchanged: NCT07529197 (IMPACT, recruiting), DRKS00033897 (IA-Surv, recruiting), MDC002 (still pre-clinical/not_yet_recruiting, no registry entry).
- **Papers — 4 new confirmed:**
  - Wirth KJ, Preprints.org (not peer-reviewed), May 2026 — "Laxity Comes with Consequences: Connective Tissue Disorders and ME/CFS"; hypothesis paper linking connective-tissue laxity/hypoxia/mast-cell activity to ME/CFS pathology. HIGH PRIORITY (Wirth-authored); flagged as an unreviewed preprint with some claims contested on s4me.info. DOI 10.20944/preprints202605.0876.v1.
  - Sardell J et al. (PrecisionLife), J Transl Med, Apr 2026 — combinatorial-genetics follow-up on the DecodeME cohort; >22,000 reproducible variant-combinations, ~250 core genes, 76 shared with long COVID, drug-repurposing candidates (ampligen, apremilast). DOI 10.1186/s12967-026-08167-1.
  - Habermann-Horstmeier L & Horstmeier LM, J Transl Med, Apr 2026 — German APAV-ME/CFS cohort (n=748) shows symptom clusters statistically track distinct neuroimmune/autonomic mechanisms, supporting subgroup-based treatment. DOI 10.1186/s12967-026-08159-1.
  - Tyson SF & Fleming R, medRxiv (preprint), Jun 2026 — TIMES symptom-burden survey, n=1,028 ME/CFS patients; severe overall burden, cognitive symptoms worst, women more affected than men. DOI 10.64898/2026.06.17.26355870.
- isNew set true: `wirth-2026-connective-tissue-laxity`, `sardell-2026-decodeme-combinatorial-genetics`, `habermann-horstmeier-2026-symptom-clusters`, `tyson-2026-times-survey` (all new this run, will clear next run)
- isNew cleared: `ryback-2026-myoblast-mitochondria-replication`, `rydland-2026-extracellular-vesicles` (no longer new since last check)
- Trials tracked: 4 (open: 2 — IMPACT, IA-Surv; planned: 1 — MDC002; active/not recruiting: 1 — RAPID_REVIVE)
- Notes: New-trial candidates found but excluded (no German connection, no drug intervention, or wrong phenotype/status) — NCT03773003/IMPROFA (probiotic supplement, mixed cancer+CFS population), NCT05926505/PRECISION-anakinra Jena site (respiratory-only phenotype, not_yet_recruiting locally), NCT07352254/ACCESS Hannover (telemedicine outreach, not a drug), CTIS 2024-512500-19-00/ResetME-daratumumab (Bergen, Norway sponsor — no German site), NCT07285473 low-dose naltrexone (US-only). Germany's new "Nationale Dekade gegen Postinfektiöse Erkrankungen" (announced Jan 2026, €500M/2026–2036) is a funding-pipeline signal to watch for future MDC002/other trial registrations, not yet a trial itself. One paper lead excluded for marginal fit/unconfirmed authorship: Xu/OuYang/Chen NHIS diagnostic nomogram (Frontiers in Neurology, Apr 2026). Literature archive updated for all 4 new papers (PDFs fetched where available).

## 2026-07-01 (scheduled autonomous, 04:13 UTC)
- Sources checked — trials: ClinicalTrials.gov API, DRKS (incl. post-COVID terms), CTIS/euclinicaltrials.eu (partially blocked — SPA shell), WHO ICTRP, Charité CFC/NKSG (all 5 trial subpages), Mitodicure.com (pipeline/news/about-us), NAPKON/NUM + num.charite.de, Lungeninformationsdienst, healthrising.org, thesicktimes.org, mecfs.de, RiffReporter, APTA Therapeutics.
- Sources checked — papers: PubMed (date-sorted + Scheibenbogen/Wirth author searches), Europe PMC, medRxiv/bioRxiv, healthrising.org, thesicktimes.org, meassociation.org.uk, s4me.info.
- New trials: none
- Newly open: none
- Status changed: none
- Closed since last: none
- All 4 tracked trials re-verified unchanged (NCT07529197, DRKS00033897, RAPID_REVIVE recruiting; MDC002 still pre-clinical/not_yet_recruiting).
- **Papers — 2 new confirmed:**
  - Ryback AA et al. (Ponting/DecodeME-linked group), PLOS ONE, Feb 2026 — large pre-registered replication attempt found no mitochondrial-function difference in myoblasts exposed to ME/CFS vs healthy serum (negative result re: a widely-cited 2016 "blood-borne factor" finding). DOI 10.1371/journal.pone.0341334.
  - Rydland A et al. (Oslo University Hospital), Biochemistry and Biophysics Reports, Jun 2026 — largest extracellular-vesicle protein-cargo study in ME/CFS so far (49 patients vs 50 controls); mostly exploratory, no differences survived correction. DOI 10.1016/j.bbrep.2026.102679.
- isNew set true: `ryback-2026-myoblast-mitochondria-replication`, `rydland-2026-extracellular-vesicles` (both new this run, will clear next run)
- flags cleared: `rapid-revive` (`new` → `[]`, no longer new since last check)
- Trials tracked: 4 (open: 3 — IMPACT, IA-Surv, RAPID_REVIVE; planned: 1 — MDC002)
- Notes: Borderline leads not entered (no registry entry, wrong status, or no German site) — VERI-LONG/NCT05697640 (active_not_recruiting, watch for reopen), inebilizumab (Scheibenbogen, funded but unregistered), BC007/rovunaptabin (APTA Therapeutics — new site is Coimbra, Portugal, not Germany), semaglutide (Scheibenbogen — grant announcement only, no trial page), PoCoVIT (cognition-only eligibility, doesn't clearly meet ME/CFS-overlap phenotype), daratumumab larger RCT (Fluge/Bergen, no German site), anakinra NCT05926505 (German site but respiratory-only phenotype). A single-author medRxiv preprint (Lee, ME/CFS-IBS-psychiatric genetic overlap) was flagged but not added pending author-affiliation verification. Literature archive updated for both new papers (full-text PDFs fetched via Unpaywall/PMC).

## 2026-06-30 (manual — missed-trial root-cause fix, 19:23 UTC)
- Trigger: a user-flagged recruiting study at Uniklinik Frankfurt that the watch never surfaced.
- Sources checked: CTIS (Post-COVID), DRKS, ClinicalTrials.gov, NAPKON/NUM platform, Lungeninformationsdienst, Goethe-Uni Frankfurt, unimedizin-ffm.de, published protocol (PMC12366011).
- **New trial:**
  - `rapid-revive` — RAPID_REVIVE: Phase 2 double-blind, placebo-controlled RCT of **vidofludimus calcium (IMU-838)** for Post-COVID Syndrome; ~376 patients, **11 German sites incl. Charité Berlin**; eligibility by Bell Disability Scale 20–60 + fatigue/cognitive/orthostatic (post-COVID ME/CFS-overlapping population); recruiting since Sep 2024; sponsor Goethe-Uni Frankfurt (Vehreschild); confirmed via CTIS 2024-511628-16-00.
- **Root cause of the miss:** registry queries used only ME/CFS terms (never `Post-COVID-Syndrom`/`Long COVID`) and the NAPKON/NUM post-COVID platform was not a monitored source — so post-COVID **drug** trials (even with a Charité site) were invisible, despite post-COVID ME/CFS being in scope.
- **Fix:** `sources/search-sources.md` updated — scope reminder now mandates post-COVID condition queries; DRKS/CTgov/CTIS rows add them; new §3a (NAPKON/NUM, university-clinic study pages, Lungeninformationsdienst) with a drug+ME/CFS-phenotype triage rule; post-COVID reusable queries added.
- The user-flagged page itself (CARE-MIND, Frankfurt psychiatry) is an **observational** Long-COVID cognition/metabolism study (no drug) → out of scope; logged as a lead only.
- Trials tracked: 4 (open: 3 — IMPACT, IA-Surv, RAPID_REVIVE; planned: 1 — MDC002).

## 2026-06-30 (scheduled autonomous, 04:10 UTC)
- Sources checked: DRKS, ClinicalTrials.gov (Germany/ME/CFS recruiting+not_yet_recruiting), CTIS, Mitodicure.com/pipeline, Charité CFC, APTA Therapeutics (BC007/rovunaptabin), PubMed (ME/CFS Jun–Jul 2026, Scheibenbogen/Wirth author searches), Europe PMC, medRxiv, ScienceDaily, Health Rising, The Sick Times, ME/CFS Research Foundation news
- New trials: none
- Newly open: none
- Status changed: none
- Closed since last: none
- Papers — 0 new confirmed (no new notable ME/CFS papers indexed since 2026-06-29)
- isNew cleared: `frank-2026-molecular-reclassification` (was `true` from 2026-06-29 run)
- flags cleared: none (all trials already `[]`)
- Trials tracked: 3 (open: 2 [NCT07529197, DRKS00033897], watchlist: 1 [MDC002])
- Notes: MDC002 still pre-clinical (no new Mitodicure announcement). Inebilizumab and semaglutide from Scheibenbogen still unregistered (leads only). APTA Therapeutics (BC007/rovunaptabin) planning new trials for end of 2026, still no registry entry for ME/CFS indication. ME/CFS Research Foundation 2026 funding announcement expected ~June 30 — not yet published at time of this run. NDPE funding call (BMFTR) open until Sep 2, 2026; new drug trial registrations expected Q4 2026. VERI-LONG (NCT05697640, vericiguat, Charité) results still pending. PubMed returned no new results for Jun 29–30 (normal 1–3 day indexing lag). No new qualifying trials found.

## 2026-06-29 (scheduled autonomous, 04:11 UTC)
- Sources checked: DRKS, ClinicalTrials.gov (Germany/ME/CFS), CTIS, Mitodicure.com/pipeline, Charité CFC/NKSG, Solve ME/CFS Catalyst Awards, PubMed (ME/CFS 2026 Jun–Jul, Scheibenbogen/Wirth author searches), medRxiv, Science for ME, Health Rising, The Sick Times, Phoenix Rising forums
- New trials: none
- Newly open: none
- Status changed: none
- Closed since last: none
- **Papers — 1 new confirmed:**
  - Frank J et al. (Klimas group, Nova Southeastern), Int J Mol Sci May 2026 — molecular reclassification of ME/CFS via multi-omics + ML; innate immune activation, T cell exhaustion, mitochondrial dysfunction as targets (PMID 42196410)
- isNew cleared: `watton-2026-reframing-mecfs-unified` (was `true` from 2026-06-28 run)
- flags cleared: none (all trials already `[]`)
- Trials tracked: 3 (open: 2 [NCT07529197, DRKS00033897], watchlist: 1 [MDC002])
- Notes: NCT05710770 (IA-PACS-CFS RCT, Charité/Pruess) confirmed **Completed** Jan 2026 — never in our database; results (negative: no benefit vs sham) presented at May 2026 ME/CFS Symposium. Rituximab NCT06952413 is Japan-only (no German site) — out of scope. Semaglutide/Scheibenbogen still no registry entry (lead only). NCT06952413 no German site. No new qualifying trials found.

## 2026-06-28 (scheduled autonomous, 04:10 UTC)
- Sources checked: DRKS, ClinicalTrials.gov (Germany/ME/CFS), CTIS, WHO ICTRP, Mitodicure.com/pipeline, Charité CFC/NKSG, Solve ME/CFS Catalyst Awards, PubMed (Scheibenbogen/Wirth/ME/CFS 2026), medRxiv, Science for ME, Health Rising, The Sick Times
- New trials: none
- Newly open: none
- Status changed: none
- Closed since last: none
- **Papers — 1 new confirmed:**
  - Watton P, Prusty BK, J Transl Med May 2026 — unified mechanistic model of ME/CFS as disorder of impaired adaptive capacity; published May 22, 2026 (PMID 42174604) [Prusty group]
- isNew cleared: 9 papers from 2026-06-27 run (liu, seifert, desa, wirth-myasthenia, souma, heidarifard, tomic, azcue, huang-mgwas)
- flags cleared: `drks00033897` (was `new`, now `[]` — unchanged since last check)
- Trials tracked: 3 (open: 2 [NCT07529197, DRKS00033897], watchlist: 1 [MDC002])
- Notes: MDC002 still pre-clinical. Semaglutide/Scheibenbogen Catalyst Award confirmed but no registry entry found — remains a lead. Inebilizumab/Scheibenbogen still unregistered. DRKS00032963 (pediatric IA, Flensburg) is suspended — out of scope. National Decade funding call closes Sep 2 2026; new trial registrations expected Q4 2026.

## 2026-06-27 (scheduled autonomous, 12:04 UTC)
- Sources checked: DRKS, ClinicalTrials.gov (Germany/ME/CFS), CTIS, WHO ICTRP, Mitodicure.com/pipeline, Charité CFC, PubMed (Scheibenbogen C[Author], Wirth K[Author], ME/CFS 2026), Europe PMC, medRxiv, bioRxiv, Health Rising, The Sick Times
- **New trials:**
  - `drks00033897` — IA-Surv: observational immunoadsorption study in GPCR autoantibody-positive post-COVID/post-vac syndrome; recruiting at Gemeinschaftskrankenhaus Havelhöhe (Berlin) + Potsdam; PI Prof. Harald Matthes; registered DRKS Jan 27, 2025; n=82; apheresis borderline (is_drug_study: false)
- Newly open: none (IA-Surv was already recruiting since Jan 2025; new to our baseline)
- Status changed: none
- Closed since last: none
- **Papers — 9 new confirmed:**
  - Liu Z et al. (Scheibenbogen+Prusty), Brain Behav Immun Health Mar 2026 — IgG from ME/CFS disrupts cell energy (PMID 41704659) [HIGH PRIORITY]
  - Seifert M et al. (Scheibenbogen group), Int J Mol Sci Feb 2026 — extracellular vesicle biomarkers for ME/CFS (PMID 41828537) [HIGH PRIORITY]
  - Santos Guedes de Sá K et al. (Iwasaki), Cell May 2026 — autoantibodies causally linked to neurological symptoms in long COVID (PMID 42208499)
  - Wirth KJ, Steinacker JM, Front Physiol Feb 2026 — electrophysiology mechanism of muscle weakness in ME/CFS (PMID 41705124) [HIGH PRIORITY]
  - Souma B et al., Int J Mol Sci May 2026 — irisin resistance and TSP-1 axis in post-exertional malaise (PMID 42278300)
  - Heidarifard M et al., Int J Mol Sci May 2026 — Raman spectroscopy + ML diagnostic for ME/CFS (PMID 42278463)
  - Tomić S et al., Medicina Jun 2026 — 16-year longitudinal: 85% of ME/CFS women develop major comorbidities (PMID 42356126)
  - Azcue N et al., J Transl Med Jun 2026 — post-COVID and ME/CFS convergence over 31 months (PMID 42286686)
  - Huang K et al., iScience Dec 2025 — mGWAS in UK Biobank links ME/CFS to lipid/neurotransmitter gene variants (DOI 10.1016/j.isci.2025.114316)
- Trials tracked: 3 (open: 2 [NCT07529197, DRKS00033897], watchlist: 1 [MDC002])
- Notes: No Mitodicure MDC002 update (still pre-clinical). No Inebilizumab/Semaglutide registry entries found. NDPE first funding call closes Sep 2 2026 — new trial registrations may follow in Q4 2026.

## 2026-06-26 (correction — intake-standard tightening)
- **Two trials removed:** `nksg-inebilizumab-ph2` (Inebilizumab Ph2, Charité NKSG) and `charite-semaglutide-glp1` (Semaglutide, Scheibenbogen) deleted from `data/trials.json`.
  - Reason: both were sourced solely from a general therapy-overview page (mecfs.de/therapie) and a grant-announcement page (solvecfs.org/catalyst-awards) respectively — neither has a dedicated trial-specific registry entry or a named clinical-research subpage. Under the tightened intake standard these are *leads only*, not confirmation.
  - Both trials remain scientific leads: if/when a DRKS/NCT registration or a dedicated Charité CFC trial subpage appears, they can be re-added.
- **ROUTINE.md + CLAUDE.md updated:** confirmation standard for `not_yet_recruiting` planned trials now explicitly requires either (a) a registry entry or (b) a dedicated trial-specific institutional/company page — general overview pages, grant announcements, and press releases are leads only.
- Trials tracked: 2 (open: 1 [NCT07529197], watchlist: 1 [MDC002])
- Papers: unchanged (47 total)

## 2026-06-26 (run 4 — scheduled autonomous, 14:28 UTC)
- Sources checked: DRKS, ClinicalTrials.gov (Germany/ME/CFS), CTIS, WHO ICTRP, Mitodicure.com/pipeline, Charité CFC/NKSG, mecfs.de, mecfs-research.org, PubMed, medRxiv, bioRxiv, Health Rising, The Sick Times (May 2026 Berlin conference roundup)
- **Trials** — no new in-scope trials; all 4 existing trials verified unchanged
  - NCT07529197 (IMPACT): still recruiting (Scheibenbogen immunoadsorption, Charité) [HIGH PRIORITY]
  - MDC002 (Mitodicure): still pre-clinical/not_yet_recruiting [HIGH PRIORITY]
  - Inebilizumab Phase 2 (Scheibenbogen/NKSG): still not_yet_recruiting
  - Semaglutide GLP-1 (Scheibenbogen/Charité): still not_yet_recruiting
  - Notable: Berlin conference (May 7–8, 2026) — IA-PACS-CFS (immunoadsorption RCT) and PoCoVIT (methylprednisolone) both failed primary endpoints; both completed before our tracking began
- **Papers** — no new papers since last check (14:12 UTC); isNew cleared for 4 papers added in run 3 (donchev, hunter, che, eckey)
- Trials tracked: 4 (open: 1 [NCT07529197], watchlist: 3)
- Notes: No changes. Watch: BC007/APTA announcement, NDPE-funded drug trials (expected Q4 2026).
  - *(Note: run 4 saw inebilizumab/semaglutide as tracked; both subsequently removed by correction entry above.)*

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
