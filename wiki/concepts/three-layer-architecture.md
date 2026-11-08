---
title: "Three-Layer Architecture"
type: concept
status: evergreen
created: 2026-11-08
updated: 2026-11-08
tags:
  - knowledge-management
  - architecture
sources:
  - karpathy-llm-wiki
confidence: high
---

# Three-Layer Architecture

> The LLM Wiki pattern separates immutable raw sources, an LLM-maintained wiki, and a schema that defines how the wiki is structured and maintained.

## What it is

The architecture has three layers with different owners and different rules:

| Layer | Contents | Owner | Rule |
|---|---|---|---|
| Raw sources | Articles, papers, images, data files | Human | Immutable, read-only, source of truth |
| Wiki | Summaries, concepts, entities, comparisons, synthesis | LLM | Persistent, interlinked, continuously revised |
| Schema | `AGENTS.md` or `CLAUDE.md` | Human + LLM | Conventions, workflows, quality rules |

The layers are not just folders. They are a trust hierarchy. A claim in the wiki should be traceable to a source; a source should never be silently rewritten to fit the wiki; and the schema should make that relationship explicit.

## Why the separation matters

**Auditability.** If the wiki and the sources are mixed, it becomes impossible to tell what was observed from what was inferred. Keeping raw sources immutable preserves the evidence trail.

**Recoverability.** If the wiki drifts or a page is damaged, the sources are still there. The wiki can be rebuilt. If the sources are edited to match the wiki, the original evidence is lost.

**Ownership clarity.** The human curates sources and directs the work. The LLM writes and maintains the wiki. The schema is co-owned. Ambiguity here produces either an idle agent or an agent that oversteps.

**Iteration.** The wiki can be reorganized, split, merged, and linted without touching the evidence. The schema can evolve without rewriting the sources.

## Layer 1: raw sources

Raw sources are the ground truth. They include web clippings, papers, PDFs, transcripts, meeting notes, images, and data files. They are immutable in the sense that the agent reads them but never edits them.

Practical rules:

- Preserve provenance: URL, author, publication date, capture date.
- Keep a local copy when the source is a web page; links rot.
- Store images locally so the agent can view them and so references do not break.
- Do not store secrets or sensitive data you would not want in git.
- If a source needs correction, add a new source or annotate the wiki; do not rewrite history.

Immutability is not bureaucracy. It is what makes the wiki's claims checkable later.

## Layer 2: the wiki

The wiki is the compiled layer. It contains:

- **Source pages** — one summary per raw source, with citation and key claims.
- **Concept pages** — ideas, methods, patterns, and definitions.
- **Entity pages** — people, organizations, products, places, works.
- **Comparison pages** — side-by-side analyses.
- **Question pages** — filed answers and explorations.
- **An overview** — the evolving top-level synthesis.
- **An index and a log** — navigation and chronology.

The LLM owns this layer. It creates pages, updates them when new sources arrive, maintains cross-references, and keeps everything consistent. The human reads it, reviews it, and asks for changes.

The wiki is derived, but it is not disposable. It contains synthesis that is expensive to reconstruct: connections, comparisons, and judgments about what matters. That is why it is versioned and maintained rather than regenerated.

## Layer 3: the schema

The schema is the operating manual. It tells the agent:

- What the layers are and who owns them.
- What page types exist and what frontmatter they require.
- What workflows to follow for ingest, query, and lint.
- What quality rules apply: citations, confidence, contradictions, link style, naming.
- What not to do: edit raw sources, delete pages, invent facts.

Karpathy calls the schema "the key configuration file" and says it is what makes the LLM "a disciplined wiki maintainer rather than a generic chatbot." The schema should co-evolve with the human as the domain and workflow become clearer.

A schema is not a prompt dump. It should be specific enough to constrain behavior and short enough to be read at the start of every session. When a convention changes, the schema changes and the log records why.

## Failure modes

- **Editing raw sources.** Destroys the evidence trail and makes the wiki unfalsifiable.
- **Letting the wiki become the source of truth.** The wiki is a synthesis; it can be wrong. Claims should still point back to sources.
- **Schema drift.** The agent follows an outdated schema, or the human changes conventions without updating it. Log structural changes.
- **No separation between synthesis and evidence.** Pages should distinguish "the source says" from "this implies."
- **Treating the wiki as a dump.** A pile of summaries is not a compiled knowledge base; integration and cross-references are the point.

## Connections

- [[persistent-wiki|Persistent Wiki]] — the layer's purpose and value.
- [[ingest-query-lint|Ingest, Query, Lint]] — the operations that move knowledge between layers.
- [[index-and-log|Index and Log]] — the navigation files inside the wiki layer.
- [[business-brain|Business Brain]] — a concrete instantiation of the three layers for a business.
- [[agent-memory|Agent Memory]] — a parallel memory layer that lives in the agent runtime, not the wiki.
- [[karpathy-llm-wiki|LLM Wiki (Karpathy gist)]] — the founding source.

## Disagreements and open questions

- Should the schema live in one file or be split into modular rule files as it grows?
- How much of the schema should be enforced by tooling (lint, scripts) versus written instructions?
- Should raw sources be versioned in the same repository as the wiki, or kept separately for privacy or size reasons?
- When a source is superseded, should it stay in `raw/` forever, or be archived elsewhere?

## Sources

- [[karpathy-llm-wiki|LLM Wiki (Karpathy gist)]]
