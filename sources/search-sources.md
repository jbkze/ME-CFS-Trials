# Search sources & leads

Durable "where to look" knowledge for the routine. This file rarely changes;
trial *state* lives in `data/trials.json`, not here. Work through the registries
top-to-bottom each run, then chase the named leads.

Scope reminder: **ME/CFS · drug/pharmacological · at least one site in Germany ·
open for enrollment.** Prioritise anything linked to **Klaus Wirth** or
**Carmen Scheibenbogen**.

---

## 1. Trial registries (check every run)

| Priority | Registry | Why | Search entry point |
|---|---|---|---|
| ★★★ | **DRKS — Deutsches Register Klinischer Studien** | The German national register. Best coverage of Germany-only trials. | https://drks.de/search/de — search `ME/CFS`, `chronisches Fatigue-Syndrom`, `myalgische Enzephalomyelitis`, `post-exertional`, plus drug names below. Filter recruitment status = *recruiting*. |
| ★★★ | **ClinicalTrials.gov** | Largest register; many German sites list here. | https://clinicaltrials.gov/search?cond=ME%2FCFS&country=Germany&aggFilters=status:rec — also query by intervention (e.g. `MDC002`) and by investigator (`Scheibenbogen`). |
| ★★ | **CTIS — EU Clinical Trials Information System** (EMA) | Mandatory portal for new EU drug trials since 2022; replaced EudraCT/EU-CTR. | https://euclinicaltrials.eu/ (public search). Filter country = Germany, condition = ME/CFS / post-COVID. |
| ★★ | **WHO ICTRP** | Meta-search across national registries; catches anything missed above. | https://trialsearch.who.int/ — query condition + `Germany`. |

Status vocabulary to record is defined in `../ROUTINE.md`. "Open for enrollment"
= **recruiting** or **enrolling by invitation** only.

---

## 2. Named leads — Klaus Wirth (priority: HIGH)

- **Mitodicure GmbH** — Wirth is CSO / Managing Director (since 2022; ex-Sanofi).
  - Lead candidate **MDC002**: orally applicable small molecule that stimulates
    the Na⁺/K⁺-pump and the Na⁺/Ca²⁺ exchanger (NCX) in skeletal muscle; target
    indication ME/CFS and post-acute infection syndromes / PEM.
  - Status as of early 2026: **clinical trials in planning** — not yet recruiting.
    This is the key trigger to watch: flag the moment a Phase 1 opens, especially
    a German site.
  - Sources to recheck: https://mitodicure.com/ and https://mitodicure.com/about-us/
- Wirth publishes the ME/CFS skeletal-muscle / vascular pathomechanism work
  jointly with Scheibenbogen — a new paper often precedes trial news. Check
  PubMed: `Wirth K AND (ME/CFS OR chronic fatigue)`.

---

## 3. Named leads — Carmen Scheibenbogen (priority: HIGH)

- **Charité Fatigue Centrum (CFC), Berlin** — Institute of Medical Immunology.
  - Clinical-research listing (trials + recruitment): https://cfc.charite.de/en/clinical_research/
  - Known / recent trial programmes to verify each run:
    - **Immunoadsorption (IA)** in autoantibody-positive post-infectious ME/CFS —
      e.g. observational study **NCT07529197**; "Trial RIA" (repeat IA):
      https://cfc.charite.de/en/clinical_research/nksg/trial_ria/
    - **BC007 / rovunaptabin** (Berlin Cures) — aptamer neutralising GPCR
      autoantibodies.
    - Watch also for low-dose naltrexone, daratumumab, efgartigimod or other
      autoantibody-targeting agents her group discusses.
  - Munich Chronic Fatigue Center for Young People (paediatric ME/CFS) often
    co-recruits — relevant if a trial includes adolescents.

---

## 4. Secondary / news sources (catch announcements before registration)

- **#MEAction / Deutsche Gesellschaft für ME/CFS** — https://www.mecfs.de/ (news, studies)
- **Health Rising** — https://www.healthrising.org/ (covers Wirth/Scheibenbogen trials in depth)
- **The Sick Times** — https://thesicktimes.org/
- PubMed new-publication alerts for both investigators (often precede trials).

> News sources are *leads only*. Never enter a trial into `data/trials.json` on
> the strength of a blog post — confirm it against a registry or the
> institution's own clinical-research page first, and cite that as `registry`/`links`.

---

## 5. Reusable search queries

Drug / intervention names worth querying directly each run:
`MDC002`, `Mitodicure`, `BC007`, `rovunaptabin`, `immunoadsorption ME/CFS`,
`low-dose naltrexone ME/CFS`, `daratumumab ME/CFS`, `efgartigimod fatigue`.

General queries:
`ME/CFS clinical trial Germany recruiting`,
`chronisches Fatigue-Syndrom Studie Teilnehmer gesucht`,
`myalgische Enzephalomyelitis Arzneimittelstudie`,
`Scheibenbogen Studie rekrutiert`, `Wirth MDC002 Phase 1`.
