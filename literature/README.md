# Literature archive

A local literature store for the papers tracked in `../data/papers.json`, adapting
the user's Obsidian-vault convention to this repo. **The folder is the record** —
one folder per paper under `papers/<slug>/`:

```
literature/papers/<YEAR-firstauthor-short-title>/
├── summary_<YEAR>_<SHORT-TITLE>.md   primary note: YAML frontmatter + body
├── citation.bib                      BibTeX for THIS paper (key: surnameYYYY)
├── paper.pdf                         open-access PDF (when one was found)
├── paper.txt                         extracted full text (when a PDF was found)
└── cover.png                         page-1 thumbnail (when a PDF was found)
```

- **Slug:** `YEAR-firstauthor-short-title`, lowercase + hyphens. **BibTeX key:**
  `surnameYYYY` (lowercase, no separator), collision suffix `a`, `b`, …
- **Summary frontmatter:** `type, id, title, authors[], year, venue, doi, url,
  pdf, text, tags, status: to-read, added, source, bibtex_key` (+ `cover` only if
  `cover.png` exists). Body: `## Related files`, `## Summary`, `## Why this matters`,
  `## Notes`.
- **No PDF?** The note carries a `_No PDF available_` line stating the blocker; the
  DOI stays in `pdf:`/`url:`. Many papers are paywalled (Elsevier, Wiley, Springer,
  PNAS-direct, Nature subscription, Wolters Kluwer) and **cannot be fetched headless
  here** — retrieve those via institutional access (Shibboleth) or interlibrary loan.

## Maintenance

`python3 ../scripts/literature_intake.py` (re-runnable) rebuilds every folder from
`data/papers.json`: derives slug/key, writes `citation.bib` + the summary note,
fetches the PDF, and — when a PDF is found and **PyMuPDF** is installed
(`pip install pymupdf`) — extracts `paper.txt` and renders `cover.png`. Existing
PDFs are kept. The routine runs this after each papers update (see `../ROUTINE.md`).

**PDF source chain** (first valid `%PDF`, >10 KB wins): Unpaywall OA locations →
the DOI's PMC copy via the **NCBI ID Converter → Europe PMC** render route (the
PMCID is resolved from the exact DOI, so a wrong record can't slip in) → publisher
OA patterns → **Elsevier Article API** for `10.1016/…` DOIs *iff* the
`ELSEVIER_API_KEY` environment variable is set. A freshly fetched PDF is
**identity-checked** (first-author surname + ≥2 distinctive title words must appear
in the text) and Elsevier returns must be ≥2 pages, so abstract-only "article in
press" stubs and mismatched records are discarded rather than filed.

> **Elsevier key (optional but recommended).** Set `ELSEVIER_API_KEY` as an
> environment variable / secret in the routine environment (never commit it). With
> it, paywalled ScienceDirect papers (Brain Behav Immun, Autoimmunity Reviews, Cell
> Host & Microbe, Endocrine Practice, …) are fetched as full text automatically.
> The key is read only from the environment and is never written into this repo.

> First backfill (2026-06-26): 42 papers, 17 open-access PDFs. Follow-ups the same
> day brought it to **37 with full-text PDFs** (legal OA/PMC + Elsevier API,
> identity-verified); the remaining 5 are non-Elsevier paywalls (Wolters Kluwer,
> Annals), one article not deposited in PMC, an article-in-press (abstract only so
> far), and the NAP-login-gated IOM report.

This is the cloud equivalent of the user's local `vault` CLI; there is no
`python -m vault add` here. PDFs live in-repo, so the repo (and each routine clone)
grows over time — if that becomes heavy, move PDFs to git-LFS or a separate vault repo.
