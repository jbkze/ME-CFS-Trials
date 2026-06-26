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
fetches the open-access PDF (Unpaywall → Europe PMC → publisher OA patterns;
verifies `%PDF`, >10 KB), and — when a PDF is found and **PyMuPDF** is installed
(`pip install pymupdf`) — extracts `paper.txt` and renders `cover.png`. Existing
PDFs are kept. The routine runs this after each papers update (see `../ROUTINE.md`).

> First backfill (2026-06-26): 42 papers, 17 with open-access PDFs, 25 noted as
> `_No PDF available_` (paywalled / headless-blocked).

This is the cloud equivalent of the user's local `vault` CLI; there is no
`python -m vault add` here. PDFs live in-repo, so the repo (and each routine clone)
grows over time — if that becomes heavy, move PDFs to git-LFS or a separate vault repo.
