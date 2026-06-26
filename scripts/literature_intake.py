#!/usr/bin/env python3
"""Literature intake for the ME/CFS papers — adapts the user's Obsidian-vault
convention to this repo (there is no `vault` CLI here, so this is the equivalent).

For every paper in data/papers.json it creates one folder:

  literature/papers/<YEAR-firstauthor-short-title>/
    ├── summary_<YEAR>_<SHORT>.md   primary note (YAML frontmatter + body)
    ├── citation.bib                BibTeX for THIS paper (key: surnameYYYY)
    ├── paper.pdf                   open-access PDF when one was found
    ├── paper.txt                   extracted full text (when a PDF was found)
    └── cover.png                   page-1 thumbnail (when a PDF was found)

PDF source chain (stop at first valid %PDF, >10 KB): Unpaywall OA locations
(repository/PMC preferred) → Europe PMC render → publisher OA patterns. Paywalled
/ headless-blocked papers (Elsevier, Wiley, Springer, medRxiv, PNAS direct …) get
a "_No PDF available_" note in the summary, keeping the DOI — exactly per the
vault convention. Re-runnable: existing PDFs are kept; notes/bib are refreshed.

Usage:  python3 scripts/literature_intake.py [--no-fetch]
"""
from __future__ import annotations
import json, os, re, subprocess, sys, unicodedata, urllib.parse, urllib.request, pathlib, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAPERS = ROOT / "data" / "papers.json"
LIBDIR = ROOT / "literature" / "papers"
EMAIL = "jonas.kunze@optimax-energy.de"   # Unpaywall requires a contact email
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
ADDED = "2026-06-26"

# Thematic tag vocabulary (inline; the local vault uses references/tag-vocabulary.md).
TAG_RULES = [
    ("autoimmunity", ["autoantib", "autoimmun", "gpcr", "adrenergic", "muscarinic", "b cell", "b-cell", "rituximab", "plasma cell", "daratumumab", "immunoadsorption"]),
    ("immunology", ["immune", "cytokine", "interleukin", "nk cell", "natural killer", "inflammat", "mast cell", "il-"]),
    ("metabolism", ["metabol", "pyruvate", "mitochond", "energy", "atp", "bioenerget", "itaconate"]),
    ("exercise-physiology", ["exercise", "cardiopulmonary", "cpet", "vo2", "exertion"]),
    ("post-exertional-malaise", ["post-exertional", "post exertional", "pem"]),
    ("neuroinflammation", ["neuroinflamm", "pet", "brain", "thalam", "neuro", "cerebrospinal", "csf"]),
    ("autonomic", ["autonomic", "pots", "orthostatic", "vasopressin", "endothel", "vascular", "microclot", "clot"]),
    ("skeletal-muscle", ["skeletal muscle", "muscle"]),
    ("genetics", ["genome", "gwas", "genetic", "decodeme"]),
    ("microbiome", ["microbiome", "gut", "tryptophan", "microbial"]),
    ("biomarker", ["biomarker", "proteom", "diagnos", "signature", "nanoelectronic", "cell-free", "rna signature"]),
    ("treatment", ["therapy", "treatment", "trial", "cyclophosphamide", "naltrexone", "oxygen", "bc007", "rovunaptabin", "mdc002"]),
    ("infection-trigger", ["herpesvirus", "hhv-6", "ebv", "epstein", "post-covid", "long covid", "post-infectious", "viral"]),
    ("diagnostic-criteria", ["criteria", "consensus", "redefining", "case definition"]),
    ("epidemiology", ["prevalence", "epidemiolog", "burden"]),
    ("review", ["review", "hypothesis", "perspectives", "framework", "insights from"]),
]
STOPWORDS = {"the", "a", "an", "of", "in", "on", "and", "for", "with", "to", "by", "from", "is",
             "patients", "study", "myalgic", "encephalomyelitis", "chronic", "fatigue", "syndrome",
             "me", "cfs", "mecfs"}


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def surname(authors: str) -> str:
    first = re.split(r"[,;]", authors.strip())[0]
    first = re.sub(r"\(.*?\)", "", first).strip()
    tok = re.sub(r"[^A-Za-zÀ-ÿ\- ]", "", first).split()
    if not tok:
        return "anon"
    # "Surname Initials" → first token; take first hyphen-segment, strip accents to ASCII
    sn = tok[0].split("-")[0].lower()
    sn = unicodedata.normalize("NFKD", sn)
    return "".join(c for c in sn if not unicodedata.combining(c))


def year_of(date: str) -> str:
    m = re.search(r"(19|20)\d{2}", date or "")
    return m.group(0) if m else "0000"


def short_title(title: str, n=4) -> str:
    words = re.sub(r"[^A-Za-z0-9 ]", " ", title.lower()).split()
    kept = [w for w in words if w not in STOPWORDS and len(w) > 2][:n]
    return "-".join(kept) or "untitled"


def doi_of(link: str) -> str | None:
    m = re.search(r"10\.\d{4,9}/\S+", link or "")
    return m.group(0).rstrip("/.") if m else None


def tags_for(p: dict) -> list:
    hay = (p.get("title", "") + " " + p.get("summary", "") + " " + p.get("why", "")).lower()
    out = []
    for tag, kws in TAG_RULES:
        if any(k in hay for k in kws):
            out.append(tag)
    return out[:7] or ["review"]


def unpaywall_pdf_urls(doi: str) -> list:
    url = f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi)}?email={EMAIL}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        data = json.load(urllib.request.urlopen(req, timeout=30))
    except Exception:
        return []
    locs = [l for l in (data.get("oa_locations") or []) if l.get("url_for_pdf")]
    # Prefer repository / PMC / Europe PMC hosts (they serve headless); publisher last.
    def rank(l):
        u = l["url_for_pdf"]
        if any(h in u for h in ("ncbi.nlm.nih.gov", "europepmc.org", "ebi.ac.uk")):
            return 0
        if l.get("host_type") == "repository":
            return 1
        return 2
    return [l["url_for_pdf"] for l in sorted(locs, key=rank)]


def pmcid_for_doi(doi: str) -> str | None:
    """Resolve a DOI to its PMCID via the NCBI ID Converter (authoritative, exact
    match) so we never fetch the wrong PMC record from a hand-guessed id."""
    if not doi:
        return None
    url = ("https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/"
           f"?ids={urllib.parse.quote(doi)}&format=json&tool=mecfs-watch&email={EMAIL}")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        data = json.load(urllib.request.urlopen(req, timeout=30))
        for rec in data.get("records", []):
            if rec.get("pmcid"):
                return rec["pmcid"]
    except Exception:
        pass
    return None


def candidate_urls(doi: str, p: dict) -> list:
    urls = unpaywall_pdf_urls(doi) if doi else []
    # Europe PMC serves a headless-downloadable PDF for PMC-deposited articles;
    # resolve the PMCID from the exact DOI first so the URL can't point elsewhere.
    pmcid = pmcid_for_doi(doi) if doi else None
    if pmcid:
        urls.append(f"https://europepmc.org/articles/{pmcid}?pdf=render")
        urls.append(f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextPDF")
    # Publisher OA URL patterns that are known to serve headless.
    if doi and doi.startswith("10.3389/"):           # Frontiers
        urls.append(f"https://www.frontiersin.org/articles/{doi}/pdf")
    if doi and doi.startswith("10.1186/"):           # BMC family
        urls.append(f"https://link.springer.com/content/pdf/{doi}.pdf")
    if doi and doi.startswith("10.3390/"):           # MDPI — resolve via landing
        urls.append(f"https://doi.org/{doi}")
    return list(dict.fromkeys(urls))                 # dedup, keep order


def elsevier_pdf(doi: str, dest: pathlib.Path) -> bool:
    """Full-text PDF via the Elsevier Article Retrieval API. Active only when
    ELSEVIER_API_KEY is present in the environment — the key is read from there
    and NEVER written to the repo. Rejects abstract-only "article in press" stubs
    by requiring at least 2 pages (a 1-page return is just the abstract)."""
    key = os.environ.get("ELSEVIER_API_KEY", "").strip()
    if not key or not doi or not doi.startswith("10.1016/"):
        return False
    run(["curl", "-sS", "--max-time", "90", "-o", str(dest),
         "-H", f"X-ELS-APIKey: {key}", "-H", "Accept: application/pdf",
         f"https://api.elsevier.com/content/article/doi/{doi}"])
    if not (dest.exists() and dest.stat().st_size > 10240):
        dest.exists() and dest.unlink()
        return False
    with open(dest, "rb") as fh:
        if not fh.read(5).startswith(b"%PDF"):
            dest.unlink(); return False
    try:
        import fitz
        if fitz.open(dest).page_count < 2:           # abstract-only stub
            dest.unlink(); return False
    except Exception:
        pass
    return True


def pdf_is_paper(pdf: pathlib.Path, p: dict) -> bool:
    """True if the PDF's first-page text contains the first-author surname AND at
    least 2 distinctive title words — guards a *freshly fetched* PDF against a
    wrong-record download. Existing on-disk PDFs are trusted (never re-checked)."""
    try:
        import fitz
        head = "".join(pg.get_text() for pg in fitz.open(pdf))[:8000].lower()
    except Exception:
        return True   # no fitz → can't verify; keep legacy permissive behaviour
    sn = surname(p.get("authors", "")).lower()
    if sn and sn not in head:
        return False
    stop = {"the", "and", "for", "with", "from", "this", "that", "based", "study",
            "into", "their", "have", "are", "may", "help", "associated", "disease",
            "syndrome", "chronic", "fatigue", "patients", "evidence", "insights"}
    toks = [w for w in (m.lower() for m in re.findall(r"[A-Za-z][A-Za-z\-]{4,}", p.get("title", "")))
            if w not in stop]
    return sum(1 for t in toks[:8] if t in head) >= 2


def try_download(urls: list, dest: pathlib.Path) -> bool:
    for u in urls:
        r = run(["curl", "-sSL", "--max-time", "60", "-A", UA, "-o", str(dest), u])
        if dest.exists() and dest.stat().st_size > 10240:
            with open(dest, "rb") as fh:
                if fh.read(5).startswith(b"%PDF"):
                    return True
        if dest.exists():
            dest.unlink()
    return False


def extract_text(pdf: pathlib.Path, dest: pathlib.Path) -> bool:
    try:
        import fitz
        doc = fitz.open(pdf)
        txt = "\n".join(page.get_text() for page in doc)
        if len(txt.strip()) < 200:
            return False
        dest.write_text(txt, encoding="utf-8")
        return True
    except Exception as e:
        print("  text extract failed:", e)
        return False


def make_cover(pdf: pathlib.Path, dest: pathlib.Path) -> bool:
    try:
        import fitz
        doc = fitz.open(pdf)
        page = doc[0]
        zoom = 300.0 / page.rect.width
        pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom))
        pix.save(dest)
        return True
    except Exception as e:
        print("  cover failed:", e)
        return False


def bibtex(key, p, doi):
    fields = {
        "title": p.get("title", ""),
        "author": " and ".join(a.strip() for a in re.split(r",(?![^()]*\))", p.get("authors", "")) if a.strip()),
        "journal": p.get("journal", ""),
        "year": year_of(p.get("date", "")),
        "doi": doi or "",
        "url": p.get("link", ""),
    }
    lines = [f"@article{{{key},"]
    for k, v in fields.items():
        if v:
            lines.append(f"  {k} = {{{v}}},")
    lines.append("}\n")
    return "\n".join(lines)


def authors_yaml(authors: str) -> str:
    items = [a.strip().replace('"', "'") for a in re.split(r",(?![^()]*\))", authors) if a.strip()]
    return "[" + ", ".join(f'"{a}"' for a in items) + "]"


def write_summary(folder, slug, key, p, doi, has_pdf, has_txt, has_cover, blocker):
    year = year_of(p.get("date", ""))
    short = short_title(p.get("title", "")).upper().replace("-", "-")
    md = folder / f"summary_{year}_{short}.md"
    pdf_field = f"literature/papers/{slug}/paper.pdf" if has_pdf else p.get("link")
    fm = [
        "---", "type: paper", f"id: {key}",
        f'title: "{p.get("title","").replace(chr(34), chr(39))}"',
        f"authors: {authors_yaml(p.get('authors',''))}",
        f"year: {year}", f'venue: "{p.get("journal","")}"',
        f"doi: {doi or 'null'}", f"url: {p.get('link') or 'null'}",
        f"pdf: {pdf_field or 'null'}",
        f"text: {'literature/papers/%s/paper.txt' % slug if has_txt else 'null'}",
        f"tags: [{', '.join(tags_for(p))}]",
        "status: to-read", f"added: {ADDED}", "source: doi",
        f"bibtex_key: {key}",
    ]
    if has_cover:
        fm.append(f'cover: "[[literature/papers/{slug}/cover.png]]"')
    fm.append("---")
    body = ["", f"# {p.get('title','')}", "", "## Related files"]
    if has_pdf:
        body.append(f"![[literature/papers/{slug}/paper.pdf]]")
    body.append(f"- [[literature/papers/{slug}/citation.bib]]")
    if has_txt:
        body.append(f"- [[literature/papers/{slug}/paper.txt]]")
    body += ["", "## Summary", "", p.get("summary", "").strip()]
    if not has_pdf:
        body += ["", f"> _No PDF available_ — {blocker} Retrieve via institutional access (Shibboleth) or interlibrary loan; DOI kept in `pdf:`/`url:`."]
    elif has_txt:
        body += ["", "_(Full text in `paper.txt`; the summary above is the curated plain-language abstract — deepen from the full text when reading.)_"]
    body += ["", "## Why this matters", "", p.get("why", "").strip()]
    if p.get("notes"):
        body += ["", "## Notes", "", p["notes"].strip()]
    md.write_text("\n".join(fm + body) + "\n", encoding="utf-8")


def blocker_for(doi, journal):
    pref = (doi or "").split("/")[0]
    j = (journal or "").lower()
    if pref == "10.1016" or "lancet" in j or "cell" in j or "elsevier" in j:
        return ("Elsevier/ScienceDirect — paywalled; set ELSEVIER_API_KEY in the "
                "environment to fetch full text via the Elsevier Article API.")
    if pref in ("10.1002", "10.1111") or "wiley" in j:
        return "Wiley — paywalled, blocks headless download."
    if pref == "10.1007" or "springer" in j:
        return "Springer — not open access / blocks headless download."
    if pref == "10.1038" and "commun" not in j and "scientific reports" not in j:
        return "Nature (subscription) — paywalled."
    if pref == "10.1097":
        return "Wolters Kluwer — paywalled."
    if pref == "10.1101":
        return "medRxiv preprint — host blocks headless download (open via the medRxiv site)."
    if "pnas" in j or pref == "10.1073":
        return "PNAS — open access but blocks headless download; use the PMC copy."
    return "publisher does not serve a headless-downloadable open-access PDF."


def main():
    no_fetch = "--no-fetch" in sys.argv
    db = json.loads(PAPERS.read_text(encoding="utf-8"))
    papers = db.get("papers", [])
    LIBDIR.mkdir(parents=True, exist_ok=True)
    seen_slug, seen_key = {}, {}
    got = nopdf = 0
    report = []
    for p in papers:
        doi = doi_of(p.get("link", ""))
        yr = year_of(p.get("date", ""))
        sn = surname(p.get("authors", ""))
        slug = f"{yr}-{sn}-{short_title(p.get('title',''))}"
        while slug in seen_slug and seen_slug[slug] != p["id"]:
            slug += "-b"
        seen_slug[slug] = p["id"]
        key = f"{sn}{yr}"
        n = seen_key.get(key, 0)
        seen_key[key] = n + 1
        if n:
            key += chr(ord("a") + n - 1)
        folder = LIBDIR / slug
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "citation.bib").write_text(bibtex(key, p, doi), encoding="utf-8")

        pdf = folder / "paper.pdf"
        has_pdf = pdf.exists() and pdf.stat().st_size > 10240
        newly = False
        if not has_pdf and not no_fetch and doi:
            # open-access routes first, then the Elsevier API (if a key is set)
            if try_download(candidate_urls(doi, p), pdf) or elsevier_pdf(doi, pdf):
                has_pdf = newly = True
        # A freshly fetched PDF must actually be THIS paper — else discard it so a
        # wrong PMCID / mismatched record can never be filed. Existing PDFs trusted.
        if newly and not pdf_is_paper(pdf, p):
            print(f"  identity mismatch, discarding fetched PDF for {slug}")
            pdf.unlink(missing_ok=True)
            has_pdf = False
        has_txt = (folder / "paper.txt").exists()
        has_cov = (folder / "cover.png").exists()
        if has_pdf and not has_txt:
            has_txt = extract_text(pdf, folder / "paper.txt")
        if has_pdf and not has_cov:
            has_cov = make_cover(pdf, folder / "cover.png")
        blocker = "" if has_pdf else blocker_for(doi, p.get("journal"))
        write_summary(folder, slug, key, p, doi, has_pdf, has_txt, has_cov, blocker)
        if has_pdf:
            got += 1; report.append(f"  PDF  {slug}")
        else:
            nopdf += 1; report.append(f"  ---  {slug}  ({blocker.split(' — ')[0]})")
    print("\n".join(report))
    print(f"\nDONE: {len(papers)} papers | {got} with PDF | {nopdf} no-PDF (noted)")


if __name__ == "__main__":
    raise SystemExit(main())
