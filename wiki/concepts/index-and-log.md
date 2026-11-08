---
title: "Index and Log"
type: concept
status: evergreen
created: 2026-11-08
updated: 2026-11-08
tags:
  - knowledge-management
  - navigation
sources:
  - karpathy-llm-wiki
confidence: high
---

# Index and Log

> The two navigation files that make an LLM Wiki legible: `index.md` is a content-oriented catalog, and `log.md` is an append-only chronology.

## What it is

As a wiki grows, the agent needs a way to find the right pages without loading everything into context. Two files solve different problems:

- **`index.md`** answers "what is in the wiki, and where should I look?"
- **`log.md`** answers "what happened recently, and in what order?"

They are complementary. The index is organized by category and optimized for retrieval. The log is organized by time and optimized for continuity.

## `index.md`: the content catalog

The index lists every page with a link, a one-line summary, and optional metadata. It is organized by category: sources, concepts, entities, comparisons, questions, meta.

A typical entry:

```md
- [[persistent-wiki|Persistent Wiki]] — why compiled knowledge beats query-time re-derivation.
```

The agent reads the index first, identifies the relevant pages, and drills into them. This is a surprisingly effective retrieval strategy at moderate scale. Karpathy puts the comfortable range at roughly 100 sources and a few hundred pages. It avoids the need for embeddings and a vector store.

Index rules:

- Every content page appears exactly once.
- Summaries are one line and present tense.
- Categories are alphabetical by title.
- The index is updated on every ingest, filed answer, and lint report.
- A page missing from the index is a lint error.

The index is not a substitute for search. It is a map. At larger scale, a search engine can supplement it, but the index remains the human-readable overview.

## `log.md`: the chronology

The log is append-only. It records ingests, queries, lint passes, and maintenance. Each entry starts with a consistent prefix so the log is parseable with simple tools:

```md
## [2026-11-08] ingest | LLM Wiki (Karpathy gist)
- Summary: Ingested the founding source and created four concept pages.
- Touched: [[karpathy-llm-wiki]], [[persistent-wiki]], [[overview]].
- Notes: Implementation choices are this vault's, not the source's.
```

Types: `ingest`, `query`, `lint`, `maintenance`.

The consistent prefix enables commands such as:

```bash
grep "^## \[" wiki/log.md | tail -5
```

That gives the last five entries: a quick timeline of what the wiki has been doing. The log also helps the agent understand recent context without rereading every page.

## Why both

The index would be enough to find content, but it would not show history. The log would be enough to see history, but it would not help you find a page. Together they give the wiki two dimensions:

| File | Dimension | Optimized for | Updated |
|---|---|---|---|
| `index.md` | Content | Finding the right page | On every structural change |
| `log.md` | Time | Understanding recent activity | On every operation |

The log is also an audit trail. If a page changed in a surprising way, the log says when and why. If a lint pass fixed broken links, the log records it. If a query produced a filed answer, the log links it.

## Scale and limits

The index-first approach works because the index is small relative to the wiki. At some point, the index itself becomes too large to read at the start of every session. That is the signal to add search.

Options:

- A local search tool over Markdown files, such as qmd.
- A simple term-frequency search script, like `scripts/wiki.py search`.
- A hybrid: read the index for orientation, then search for specific terms.

The log scales better than the index because it is append-only and can be tailed. Keep it parseable and do not rewrite history.

## Failure modes

- **Index drift.** Pages are created but not indexed. Lint catches it.
- **Index duplication.** A page is listed in two categories. Keep one canonical entry.
- **Log rewriting.** Editing past entries destroys the audit trail.
- **Unparseable log.** Inconsistent prefixes make the log hard to query.
- **Index as a substitute for links.** The index is a map, not a replacement for cross-references inside pages.
- **Log as a diary.** Keep entries short and structured; the log is not the place for full analyses.

## Connections

- [[persistent-wiki|Persistent Wiki]] — the artifact these files navigate.
- [[three-layer-architecture|Three-Layer Architecture]] — where the files sit.
- [[ingest-query-lint|Ingest, Query, Lint]] — the operations that update them.
- [[business-brain|Business Brain]] — a working wiki that depends on both files.
- [[agent-memory|Agent Memory]] — a different memory layer, with its own files and review cycle.
- [[karpathy-llm-wiki|LLM Wiki (Karpathy gist)]] — the founding source.

## Disagreements and open questions

- Should the index include every page, including meta reports, or only knowledge pages?
- Should the log record queries that did not file a page? Recording everything is more complete; recording only changes keeps it focused.
- When the index grows too large, should it be split by category or replaced by search?
- Should the log have a machine-readable companion, such as JSONL, or is Markdown enough?

## Sources

- [[karpathy-llm-wiki|LLM Wiki (Karpathy gist)]]
