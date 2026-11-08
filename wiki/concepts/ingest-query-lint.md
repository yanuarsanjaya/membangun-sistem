---
title: "Ingest, Query, Lint"
type: concept
status: evergreen
created: 2026-11-08
updated: 2026-11-08
tags:
  - knowledge-management
  - workflow
sources:
  - karpathy-llm-wiki
confidence: high
---

# Ingest, Query, Lint

> The three core operations of an LLM Wiki: compile a new source into the wiki, answer questions from the wiki, and health-check the wiki.

## What it is

The pattern has a small operating loop. Each operation has a distinct input, output, and quality bar.

| Operation | Input | Output | Frequency |
|---|---|---|---|
| Ingest | A new raw source | Source page, updated related pages, index entry, log entry | Per source |
| Query | A question | Cited answer, optionally a filed page | As needed |
| Lint | The whole wiki | Fixed issues, content review, report, next actions | Periodically |

The loop is deliberately simple. The intelligence lives in the reading, synthesis, and judgment, not in a complex pipeline.

## Ingest

Ingest is where knowledge enters the wiki. A good ingest is not a summary pasted into a new file; it is an integration pass.

1. **Read the source fully.** Do not skim. For PDFs and images, extract text first and view images separately when useful.
2. **Orient.** Read the index and the recent log. Read the pages most likely to be affected.
3. **Extract.** Identify the thesis, key claims, evidence, entities, concepts, definitions, contradictions, quotes, and open questions.
4. **Plan.** Search for existing pages. Decide what to create, what to extend, and what conflicts. A dense source may touch 10–15 pages.
5. **Write the source page.** Citation, key takeaways, claims and evidence, quotes, connections, open questions.
6. **Integrate.** Update concept and entity pages. Add cross-links in both directions. Record contradictions rather than erasing them.
7. **Update the synthesis.** Revise the overview so it reflects the new source.
8. **Index and log.** Add every new page to the index; append a log entry.
9. **Report.** Key takeaways, pages touched, contradictions, gaps, suggested next sources.

The most common failure is creating near-duplicate pages instead of extending existing ones. Search first. The second most common failure is writing a summary that is not connected to anything; a source page with no inbound or outbound links is a dead end.

## Query

Query is where the wiki earns its keep. The agent answers from compiled pages, not raw chunks, and cites what it used.

1. Read the index.
2. Search the wiki and read the best pages, not just the top hit.
3. Follow links to source pages for provenance.
4. Answer directly, with citations. Distinguish source claims from inference.
5. State when the wiki is silent or contradictory.
6. File the answer if it is a substantial reusable synthesis.

Filing is the compounding mechanism. A comparison, an analysis, or a discovered connection should not disappear into chat history. But not every answer deserves a page; filing everything turns the wiki into a transcript archive. A reasonable threshold: the answer synthesizes three or more pages, resolves a real question, or would be expensive to reconstruct.

## Lint

Lint is maintenance. It has two parts: deterministic checks and judgment.

**Deterministic checks** (automatable):

- Broken wikilinks and missing assets.
- Pages missing from the index.
- Missing or invalid frontmatter.
- Duplicate titles or slugs.
- Source pages whose raw file is missing.
- Orphan pages with no inbound links.
- Malformed log entries.

**Content review** (requires reading):

- Contradictions between pages.
- Claims superseded by newer sources.
- Important concepts or entities mentioned but lacking a page.
- Missing cross-references.
- Pages with no sources or weak confidence.
- Gaps that a web search or new source could fill.
- Near-duplicate pages that should be merged.

Lint produces a report and a short list of next actions. It is also the moment to suggest new questions and sources. A wiki that is never linted slowly becomes a pile of stale summaries.

## Why the loop works

- **Ingest** turns reading into structure.
- **Query** turns structure into answers, and answers back into structure.
- **Lint** keeps the structure honest.

The loop is a flywheel: each pass makes the next one cheaper. The wiki gets richer, the index gets more useful, and the agent spends less time rediscovering context.

## Failure modes

- **Ingest without integration.** Source pages accumulate; concepts do not improve.
- **Query without citations.** Answers sound authoritative but cannot be checked.
- **Filing everything.** The wiki becomes a chat archive with no editorial judgment.
- **Lint without content review.** The links are clean, but the claims are stale or contradictory.
- **No lint at all.** Orphans, broken links, and duplicate pages accumulate until the wiki is hard to navigate.

## Connections

- [[persistent-wiki|Persistent Wiki]] — why the loop exists.
- [[three-layer-architecture|Three-Layer Architecture]] — where each operation moves knowledge.
- [[index-and-log|Index and Log]] — the files updated by every operation.
- [[business-brain|Business Brain]] — a domain application of the same loop.
- [[agent-skills|Agent Skills]] — how the procedures behind ingest and lint become repeatable.
- [[karpathy-llm-wiki|LLM Wiki (Karpathy gist)]] — the founding source.

## Disagreements and open questions

- Should ingest always discuss takeaways with the human first, or proceed and report? The source prefers staying involved; an agent workflow often favors proceeding.
- When should a query answer be filed? The source says good answers can be filed; it does not define a threshold.
- How much of lint can be automated without missing the important content problems?
- Should lint run on a schedule, after every N ingests, or only when the human asks?

## Sources

- [[karpathy-llm-wiki|LLM Wiki (Karpathy gist)]]
