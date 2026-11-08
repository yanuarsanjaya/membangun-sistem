# LLM Wiki — Operating Schema

> This file is the schema for an LLM-maintained wiki. It is written for the agent. The human-facing guide is `README.md`.

## 1. What this vault is

This vault implements the **LLM Wiki pattern**: a persistent, interlinked Markdown wiki that sits between immutable raw sources and the human. The agent reads sources, compiles knowledge into `wiki/`, keeps pages current, cross-references them, and logs every operation.

**Division of labor**

- **Human:** curates sources, chooses the domain, directs analysis, asks questions, reviews.
- **Agent:** reads, summarizes, files, cross-references, updates, lints, and logs.
- **Obsidian:** the IDE. **The wiki:** the codebase. **The agent:** the maintainer.

The goal is not to answer from raw documents on every query. The goal is to compile knowledge once, then keep it current so every new source and every good question makes the wiki richer.

## 2. Layers and ownership

| Layer | Path | Owner | Rule |
|---|---|---|---|
| Raw sources | `raw/` | Human | Immutable. Read only. |
| Wiki | `wiki/` | Agent | Create and update freely. Never delete without permission. |
| Schema | `AGENTS.md` | Human + agent | Co-evolve deliberately. Announce structural changes. |

- `raw/inbox/` is a drop zone for unprocessed sources.
- `raw/sources/` is the curated source collection.
- `raw/assets/` holds downloaded images and attachments.
- Never edit the contents of a raw file.
- Never rename or move raw files unless the human asks.

## 3. Non-negotiable rules

1. Read `wiki/index.md` before any ingest, query, or lint. It is the map.
2. Read the last five entries of `wiki/log.md` for recent context.
3. Never modify anything under `raw/`.
4. Never invent facts, quotes, citations, or links. If the wiki lacks an answer, say so and suggest a source.
5. Cite the origin of every non-obvious claim: inline `[[source-slug]]` links plus the page's `sources:` frontmatter.
6. Search before creating. Extend existing pages instead of creating near-duplicates.
7. Never delete a wiki page. Merge duplicates into a canonical page and leave a redirect, or mark the old page `status: archived`. Ask before doing anything destructive.
8. Update `updated:` on every page you edit. Update `wiki/index.md` and `wiki/log.md` after every ingest, every query that files a page, and every lint pass.
9. Use `[[kebab-slug|Display text]]` for internal links. Do not use Markdown links to wiki pages. In Markdown tables, escape the pipe: `[[kebab-slug\|Display text]]`.
10. Keep pages focused: one source, concept, or entity per page. Split pages at roughly 2,000–2,500 words.
11. Write wiki content in the language of the source unless the human asks otherwise. Keep frontmatter keys in English.
12. Do not edit `.obsidian/` configuration or `scripts/` unless the human asks.

## 4. Directory map

```text
AGENTS.md                  schema (this file)
README.md                  human quickstart
raw/
  inbox/                   unprocessed drops
  sources/                 curated, immutable sources
  assets/                  images and attachments
wiki/
  index.md                 content catalog (read first)
  log.md                   append-only chronology
  overview.md              evolving top-level synthesis
  sources/                 one summary per raw source
  concepts/                ideas, methods, patterns
  entities/                people, orgs, products, places, works
  comparisons/             side-by-side analyses
  questions/               filed answers and explorations
  meta/                    lint reports, audits, conventions
templates/                 page templates
scripts/wiki.py            search / lint / stats / new
.opencode/commands/        /ingest, /ask, /lint
```

## 5. Page types and frontmatter

| Type | Folder | Use for | Required extra fields |
|---|---|---|---|
| `source` | `wiki/sources/` | Summary of one raw source | `source_path` |
| `concept` | `wiki/concepts/` | Idea, method, pattern, theory | `sources`, `confidence` |
| `entity` | `wiki/entities/` | Person, org, product, place, work | `sources`, `confidence` |
| `comparison` | `wiki/comparisons/` | Side-by-side analysis | `sources`, `confidence` |
| `question` | `wiki/questions/` | Filed answer or exploration | `sources`, `confidence` |
| `overview` | `wiki/overview.md` | Top-level synthesis | none |
| `meta` | `wiki/meta/` | Lint reports, audits | none |
| `index` | `wiki/index.md` | Catalog | none |
| `log` | `wiki/log.md` | Chronology | none |

**Common frontmatter**

```yaml
---
title: "Human-readable title"
type: concept
status: seed            # seed | developing | evergreen | stale | archived
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: []                # lowercase, no #
sources: []             # source-page slugs
confidence: medium      # low | medium | high
---
```

**Source frontmatter**

```yaml
---
title: "Source title"
type: source
status: developing
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: []
source_path: raw/sources/YYYY-MM-DD-slug.md
source_url: ""
author: ""
published: ""
ingested: YYYY-MM-DD
confidence: high
---
```

**Status values**

- `seed` — created, minimal content, needs expansion.
- `developing` — useful but incomplete.
- `evergreen` — current, well-supported, stable.
- `stale` — superseded or unverified, needs review.
- `archived` — kept for history, outside the live synthesis.

**Confidence rubric**

- `high` — multiple independent sources or direct primary evidence.
- `medium` — one credible source or strong inference.
- `low` — unverified, speculative, or contested.

## 6. Page anatomy

Every knowledge page begins with:

1. An H1 matching the title.
2. A one-sentence definition or summary in a blockquote.
3. Body sections appropriate to the type.
4. `## Connections` with links to related pages.
5. `## Disagreements and open questions` when relevant.
6. `## Sources` with links to source pages.

**Section patterns by type**

- **Source:** Citation, Key takeaways, Claims and evidence, Quotes, Connections, Open questions.
- **Concept:** What it is, Why it matters, Details, Connections, Disagreements and open questions, Sources.
- **Entity:** What it is, Role and significance, Timeline, Connections, Open questions, Sources.
- **Comparison:** Question, Options, Criteria, Verdict, Caveats, Sources.
- **Question:** Question, Short answer, Analysis, Evidence, Caveats, Follow-ups, Sources.

**Writing style**

- Direct and specific. No filler.
- Short paragraphs and bullets over long prose.
- Distinguish source claims from synthesis: "Karpathy argues…" versus "This implies… (synthesis)".
- Put exact quotes in blockquotes with a locator when possible.
- Define jargon on first use and link the concept page.

## 7. Ingest workflow

Trigger: `/ingest <path-or-url>`, "ingest", "process this source", "add this to the wiki".

1. **Locate the source.** If given a URL, fetch it and save a Markdown copy to `raw/sources/YYYY-MM-DD-slug.md` with an HTML comment recording the URL and retrieval date. If given a file, read it from `raw/` (or wherever it is). If no source is given, list `raw/inbox/` and `raw/sources/` and ask which one to ingest.
2. **Read it fully.** For PDFs and images, extract the text first; view images separately when useful. Do not skim.
3. **Orient.** Read `wiki/index.md` and the last five entries of `wiki/log.md`. Then read the source pages and concept/entity pages most likely to be affected.
4. **Extract.** Note the thesis, key claims, evidence, entities, concepts, definitions, contradictions with existing pages, open questions, and useful quotes.
5. **Plan.** Search for existing pages with `python3 scripts/wiki.py search "<terms>"`. Decide which source page to create, which concept/entity pages to update, which new pages are justified, and what contradicts what. Aim for 3–10 touched pages per source; a dense source may touch 10–15.
6. **Write the source page** at `wiki/sources/<slug>.md` using `templates/source.md`.
7. **Integrate.** Create or update concept and entity pages. Extend, do not duplicate. Add cross-links in both directions. If a new source contradicts an older claim, keep both, date them, and explain the disagreement. Never silently overwrite.
8. **Update the synthesis.** Revise `wiki/overview.md` so it reflects the new source.
9. **Update `wiki/index.md`.** Add every new page with a one-line summary. Update changed summaries. Keep alphabetical order within categories.
10. **Append to `wiki/log.md`** using the format in section 11.
11. **Report.** Give 3–5 key takeaways, pages created and updated, contradictions, gaps, and suggested next sources. Do not paste the whole source back.

Default behavior: proceed through the ingest, then report. If the source is ambiguous, conflicts with established pages, or would require deleting content, pause and ask. If the human asks to discuss first, give the takeaways before writing.

## 8. Query workflow

Trigger: `/ask <question>`, or any question about the wiki's domain.

1. Read `wiki/index.md`.
2. Search with `python3 scripts/wiki.py search "<keywords>"`. Use `grep -ri` for exact strings. Read the best 3–8 pages, not only the top hit.
3. Follow links to source pages for provenance. Read `wiki/overview.md` for the current synthesis.
4. Answer directly, with citations such as `[[persistent-wiki|Persistent Wiki]]`. Distinguish what the wiki says from your own inference. State when the wiki is silent or contradictory.
5. Offer to file the answer when it is a substantial reusable synthesis: a comparison, an analysis, a discovered connection, or a decision. If the human agrees, or the request is explicitly a filing request, create a `question` or `comparison` page, then update the index, log, and overview.
6. Do not file trivial Q&A. Filing threshold: the answer synthesizes three or more pages, resolves a real question, or would be expensive to reconstruct.

Default answer format is Markdown. Use tables for comparisons. Use Marp, Canvas, or charts only when asked or clearly useful.

## 9. Lint workflow

Trigger: `/lint`, "health check", "clean up the wiki", or periodically after several ingests.

1. Run `python3 scripts/wiki.py lint`. Fix all errors: broken links, missing index entries, missing frontmatter, duplicate titles or slugs, missing source files.
2. Review warnings: orphans, stubs, stale pages, malformed log entries.
3. Content review, which requires reading:
   - Contradictions between pages.
   - Claims superseded by newer sources.
   - Important concepts or entities mentioned but lacking a page.
   - Missing cross-references.
   - Pages with no sources or weak confidence.
   - Gaps that a web search or new source could fill.
   - Near-duplicate pages that should be merged.
4. Write a report to `wiki/meta/lint-YYYY-MM-DD.md` with: summary, errors fixed, warnings, content findings, recommended actions, suggested questions and sources.
5. Update `wiki/index.md` (add the report) and append a `lint` entry to `wiki/log.md`.
6. Report the 3–5 highest-value next actions.

## 10. Index rules

- `wiki/index.md` is the first file read for any task.
- List every content page exactly once under its category: Sources, Concepts, Entities, Comparisons, Questions, Meta.
- Each entry: `- [[slug|Title]] — one-line summary.` Optionally append `(updated YYYY-MM-DD)`.
- Keep categories alphabetical by title. Empty categories: `_None yet._`
- Link `overview` and `log` at the top under "Start here".
- Update the index on every ingest, every filed answer, every lint report, and whenever a page is created, renamed, or archived.
- A page missing from the index is a lint error.

## 11. Log rules

- Append only. Never rewrite or delete past entries.
- Entry format:

```md
## [YYYY-MM-DD] <type> | <Title>
- Summary: one or two lines.
- Touched: [[slug]], [[slug]].
- Notes: optional contradictions, gaps, follow-ups.
```

- Types: `ingest`, `query`, `lint`, `maintenance`.
- One blank line between entries. Newest at the bottom.
- Keep the log parseable: `grep "^## \[" wiki/log.md | tail -5`.

## 12. Maintenance and refactors

- **Rename** a page only when the slug is wrong or ambiguous. Run `grep -rn "\[\[old-slug" wiki/` first, update every inbound link, the index, and the log.
- **Merge** near-duplicates into the more canonical page. Leave a redirect line at the old page and mark it `archived` once no inbound links remain.
- **Split** a page when it covers multiple concepts. Link both directions.
- **Archive** pages that are obsolete but historically useful. Keep them out of the main synthesis.
- Announce structural changes in the log.

## 13. Helper commands

```bash
python3 scripts/wiki.py search "persistent wiki"   # ranked full-text search
python3 scripts/wiki.py lint                        # links, orphans, frontmatter, index coverage
python3 scripts/wiki.py stats                       # counts, words, links
python3 scripts/wiki.py new concept "Attention"     # create a page from a template
```

OpenCode commands: `/ingest <path-or-url>`, `/ask <question>`, `/lint`.

## 14. Obsidian conventions

- Internal links are wikilinks: `[[slug|Display]]`.
- In tables, escape the pipe: `[[slug\|Display]]`.
- Embeds: `![[filename]]` for images stored in `raw/assets/`.
- Frontmatter must be valid YAML. Dates are `YYYY-MM-DD`. Tags are lowercase and do not include `#`.
- Prefer native Markdown and Bases over plugin-specific syntax unless the human uses the plugin.
- Do not edit `.obsidian/`.
- Use graph view to spot hubs and orphans; use `wiki/views.base` for a live table.

## 15. When in doubt

1. Read the index.
2. Search before creating.
3. Extend before adding.
4. Cite before asserting.
5. Ask before deleting.
6. Prefer a smaller, better-linked wiki over a larger, shallow one.
