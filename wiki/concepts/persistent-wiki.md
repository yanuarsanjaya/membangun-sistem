---
title: "Persistent Wiki"
type: concept
status: evergreen
created: 2026-11-08
updated: 2026-11-08
tags:
  - knowledge-management
  - llm
sources:
  - karpathy-llm-wiki
confidence: high
---

# Persistent Wiki

> A structured, interlinked body of Markdown pages that an LLM compiles from raw sources once and then keeps current, rather than re-deriving knowledge at query time.

## What it is

A persistent wiki is the middle layer between raw documents and the person asking questions. Each source is read, summarized, and integrated into existing pages. The wiki records definitions, entities, claims, evidence, cross-references, disagreements, and an evolving synthesis. It is not a search index over chunks, and it is not a chat transcript. It is a compiled knowledge artifact that is revised as new sources arrive.

Karpathy's formulation is that the LLM "incrementally builds and maintains a persistent wiki" and that "the wiki is a persistent, compounding artifact." The important word is *persistent*: the work of understanding a source survives the conversation in which it was ingested.

## Why it matters

Most LLM-plus-documents workflows are retrieval systems. They store chunks, retrieve the most similar ones at query time, and generate an answer. This works, but every question starts from scratch. A question that requires synthesizing five documents forces the model to find and reconcile the fragments again. Nothing accumulates.

A persistent wiki changes the economics:

- **Synthesis is done once and revised**, not re-derived per query.
- **Cross-references are already present**, so related knowledge is discoverable.
- **Contradictions are recorded**, so they are not silently averaged away.
- **Answers can be filed back**, so exploration also compounds.
- **The wiki becomes an asset** that is readable, editable, diffable, and portable.

The approach also changes the human's role. The human curates sources, directs the analysis, and asks good questions. The LLM does the bookkeeping: summarizing, cross-referencing, filing, and keeping pages consistent.

## Contrast with RAG

| Dimension | RAG | Persistent wiki |
|---|---|---|
| Unit of knowledge | Retrieved chunk | Compiled page |
| When synthesis happens | At query time | At ingest time, revised over time |
| Memory across queries | None by default | The wiki itself |
| Cross-references | Implicit in embeddings or reranking | Explicit wikilinks |
| Contradictions | Usually flattened or missed | Recorded and dated |
| Human-readable | Only the generated answer | The whole knowledge base |
| Infrastructure | Vector store, embeddings, retriever | Markdown files, index, optional search |
| Main failure mode | Retrieval misses the relevant chunk | Maintenance drift and unverified claims |

The wiki does not make retrieval obsolete. It moves the expensive synthesis earlier and makes the result inspectable. A search tool can still sit on top of the wiki; the difference is that search retrieves compiled pages, not raw fragments.

## How it works

1. **Ingest.** Read a source, extract its claims and entities, write a source page, and update related pages.
2. **Integrate.** Connect new claims to existing ones. If a claim conflicts, keep both and explain the disagreement.
3. **Query.** Answer from the compiled pages with citations. File substantial answers back into the wiki.
4. **Lint.** Periodically check for contradictions, stale claims, orphans, missing pages, and gaps.

A source can touch many pages. Karpathy estimates 10–15 for a dense source. That is the point: the value is in the integration, not in the summary alone.

## What makes it persistent

- **Stable page identities.** Slugs do not change casually; links are maintained.
- **Frontmatter.** Type, status, dates, tags, sources, and confidence make pages queryable.
- **An index.** A content catalog that the agent reads before drilling in.
- **A log.** An append-only chronology of what changed and when.
- **A schema.** Explicit conventions for page structure and workflows, so the next session behaves like the last one.
- **Version control.** Git provides history, diffs, and rollback.

## Limits

- **Scale.** Index-first navigation is comfortable at roughly 100 sources and a few hundred pages. Beyond that, add search.
- **Trust.** An LLM can write a confident, well-linked, wrong page. Citations, confidence levels, and human review matter.
- **Source quality.** The wiki cannot be better than the sources it compiles, though it can make their weaknesses visible.
- **Maintenance drift.** Without periodic lint, pages go stale and links break.
- **Granularity.** Too many tiny pages create navigation overhead; too few large pages hide connections.

## Connections

- [[three-layer-architecture|Three-Layer Architecture]] — where the wiki sits relative to raw sources and the schema.
- [[ingest-query-lint|Ingest, Query, Lint]] — the loop that keeps the wiki current.
- [[index-and-log|Index and Log]] — the navigation files that make it legible.
- [[business-brain|Business Brain]] — the pattern applied to business knowledge and decisions.
- [[knowledge-management|Knowledge Management]] — the broader discipline of treating context as a reusable asset.
- [[karpathy-llm-wiki|LLM Wiki (Karpathy gist)]] — the founding source.

## Disagreements and open questions

- Is the persistent wiki a replacement for RAG, or a layer above it? The source presents it as an alternative for personal knowledge bases; in practice, hybrid retrieval over wiki pages is plausible.
- How much synthesis should the LLM do versus the human? The source leans toward LLM ownership of the wiki, but quality may depend on human review of high-stakes claims.
- Does the compounding effect actually hold at scale, or does maintenance cost grow faster than value? This is the central empirical question.

## Sources

- [[karpathy-llm-wiki|LLM Wiki (Karpathy gist)]]
