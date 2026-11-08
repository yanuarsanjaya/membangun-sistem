---
title: "LLM Wiki (Karpathy gist)"
type: source
status: evergreen
created: 2026-11-08
updated: 2026-11-08
tags:
  - knowledge-management
  - llm
  - wiki
source_path: raw/sources/2026-04-04-karpathy-llm-wiki.md
source_url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
author: Andrej Karpathy
published: 2026-04-04
ingested: 2026-11-08
confidence: high
---

# LLM Wiki (Karpathy gist)

> An idea file proposing that an LLM incrementally build and maintain a persistent, interlinked wiki between raw sources and the user, instead of re-deriving answers from raw documents on every query.

## Citation

- **Author:** Andrej Karpathy
- **Published:** 2026-04-04
- **URL:** <https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>
- **Local copy:** `raw/sources/2026-04-04-karpathy-llm-wiki.md`

## Key takeaways

- **Compile, don't re-derive.** RAG rediscovers knowledge on every question. A persistent wiki extracts and integrates knowledge once, then keeps it current. The wiki is a compounding artifact, not an index.
- **Three layers, clear ownership.** Raw sources are immutable and human-curated. The wiki is LLM-owned and continuously revised. The schema (`AGENTS.md` or `CLAUDE.md`) defines structure and workflows.
- **Three operations form the loop.** Ingest a source, query the wiki, lint the wiki. A single source can touch 10–15 pages.
- **Answers can become knowledge.** A good query answer can be filed back as a new page, so explorations compound instead of disappearing into chat history.
- **Two navigation files.** `index.md` is a content-oriented catalog; `log.md` is a chronological, append-only record with a parseable prefix.
- **The schema is the control surface.** It is what turns a generic chatbot into a disciplined maintainer. It should co-evolve with the human.
- **Tooling is optional and modular.** Index-first navigation works at moderate scale. Search engines, slide decks, charts, Dataview, and other tools are add-ons, not requirements.
- **Maintenance is the real bottleneck.** Humans abandon wikis because bookkeeping grows faster than value. LLMs are good at the bookkeeping: cross-references, stale claims, contradictions, consistency.

## Claims and evidence

| Claim | Evidence or location | Confidence |
|---|---|---|
| RAG re-derives knowledge per query; a persistent wiki accumulates it. | "The core idea" section | High (author's central argument) |
| A single source may touch 10–15 wiki pages. | "Operations → Ingest" | Medium (practitioner estimate) |
| `index.md` works at roughly 100 sources and hundreds of pages. | "Indexing and logging" | Medium (author's experience) |
| The schema is the key file that makes the LLM a disciplined maintainer. | "Architecture → The schema" | High |
| Good query answers should be filed back as wiki pages. | "Operations → Query" | High |
| Lint should find contradictions, stale claims, orphans, missing pages, missing cross-references, and data gaps. | "Operations → Lint" | High |
| The wiki can be a git repo, giving version history and collaboration for free. | "Tips and tricks" | High |
| Local search tooling (e.g. qmd) becomes useful as the wiki grows. | "Optional: CLI tools" | Medium |

## Architecture in brief

| Layer | Contents | Owner | Property |
|---|---|---|---|
| Raw sources | Articles, papers, images, data | Human | Immutable, source of truth |
| Wiki | Summaries, entities, concepts, comparisons, synthesis | LLM | Persistent, interlinked, always current |
| Schema | `AGENTS.md` / `CLAUDE.md` | Human + LLM | Conventions, workflows, quality rules |

The wiki sits between the user and the sources. It is not a cache of chunks; it is a compiled representation that gets revised as new evidence arrives.

## Operations in brief

| Operation | Input | Output |
|---|---|---|
| Ingest | A new raw source | Source summary, updated concept/entity pages, index entry, log entry |
| Query | A question | Cited synthesis; optionally a new filed page |
| Lint | The whole wiki | Fixed structural issues, content review, report, suggested next questions/sources |

The loop is intentionally simple. The complexity lives in the schema and in the quality of the sources, not in a retrieval pipeline.

## Practical tips recorded by the source

- Use Obsidian Web Clipper to get web articles into the raw collection quickly.
- Set Obsidian's attachment folder to a fixed directory such as `raw/assets/`, then bind a hotkey to "Download attachments for current file" so images are local.
- Use Obsidian's graph view to see hubs, clusters, and orphans.
- Marp can turn wiki content into slide decks; Dataview can query frontmatter.
- Treat the wiki as a git repository for history, branching, and collaboration.

## Caveats and limitations

- The document is **intentionally abstract**. It describes a pattern, not an implementation. Directory structure, page formats, and tooling are left to the human and the agent.
- The scale claim for index-first navigation is approximate. Beyond a few hundred pages, search is likely necessary.
- The pattern's quality depends on **human source curation and review**. An LLM can maintain cross-references, but it can also propagate errors confidently.
- "LLMs don't get bored" is a claim about maintenance reliability, not about factual accuracy or judgment.
- The gist is a practitioner's idea file, not a peer-reviewed study. The claims about maintenance cost and compounding value are plausible and widely reported, but not measured here.
- The gist mentions related implementations and tools only as options. Nothing in the pattern requires Obsidian, qmd, Marp, or Dataview.

## Quotes

> "This is the key difference: **the wiki is a persistent, compounding artifact.**"

> "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."

> "The human's job is to curate sources, direct the analysis, ask good questions, and think about what it all means. The LLM's job is everything else."

> "The wiki stays maintained because the cost of maintenance is near zero."

## Connections

- [[persistent-wiki|Persistent Wiki]] — the core concept in depth.
- [[three-layer-architecture|Three-Layer Architecture]] — the structural model.
- [[ingest-query-lint|Ingest, Query, Lint]] — the operating loop.
- [[index-and-log|Index and Log]] — the navigation files.

## Open questions

- What page granularity works best in practice: one page per concept, or broader topic pages with sections?
- How should the wiki represent contradictions when both sources are credible and recent?
- At what scale does index-first navigation actually break down, and what is the cheapest effective search layer?
- How much human review is needed to keep an LLM-written wiki trustworthy?
- Can the pattern handle multiple domains in one vault, or does it work better as one vault per domain?
- How should the wiki handle sources that are themselves LLM-generated?
