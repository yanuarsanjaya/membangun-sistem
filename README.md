# LLM Wiki

A persistent, LLM-maintained knowledge base in Obsidian, based on [Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

Three layers:

- **`raw/`** — your immutable sources. You curate these; the agent never edits them.
- **`wiki/`** — the agent writes and maintains this. You read it.
- **`AGENTS.md`** — the schema and workflows that turn the agent into a disciplined wiki maintainer.

Obsidian is the IDE, the agent is the programmer, and the wiki is the codebase.

## Quick start

1. Open this folder as an Obsidian vault. It already has the right settings.
2. Add a source: drop a file into `raw/inbox/`, or use Obsidian Web Clipper.
3. In OpenCode, run:

   ```text
   /ingest raw/inbox/your-source.md
   ```

   You can also just say: “Ingest `raw/inbox/your-source.md` into the wiki.”

4. Browse the result in Obsidian. Start at `wiki/overview.md`, then `wiki/index.md`.
5. Ask questions:

   ```text
   /ask How does this pattern differ from RAG?
   ```

6. Periodically run `/lint` to health-check the wiki.

The vault is seeded with Karpathy's gist as its first source and four concept pages, so you can see the conventions in action. To make it yours, edit the domain in `wiki/overview.md` and start adding sources.

## What is already set up

- `AGENTS.md` — ingest, query, and lint workflows, page conventions, frontmatter schema, quality rules.
- Directory scaffold for sources, concepts, entities, comparisons, questions, and lint reports.
- Page templates in `templates/`.
- `scripts/wiki.py` — a stdlib-only helper for search, lint, stats, and creating pages.
- OpenCode commands: `/ingest`, `/ask`, `/lint`.
- Obsidian settings: attachments go to `raw/assets/`, templates come from `templates/`, and new links are wikilinks.
- `wiki/views.base` — a live Obsidian Base with views for all pages, sources, concepts, and pages needing attention.
- Git repository initialized for version history.

## Directory map

```text
AGENTS.md                  schema the agent follows
README.md                  this guide
raw/
  inbox/                   drop new sources here
  sources/                 curated, immutable sources
  assets/                  downloaded images and attachments
wiki/
  index.md                 catalog of every page (read this first)
  log.md                   append-only record of ingests, queries, lint passes
  overview.md              evolving top-level synthesis
  sources/                 one summary per raw source
  concepts/                ideas, methods, patterns
  entities/                people, organizations, products, places, works
  comparisons/             side-by-side analyses
  questions/               filed answers and explorations
  meta/                    lint reports and audits
templates/                 page templates
scripts/wiki.py            search, lint, stats, new page
.opencode/commands/        /ingest, /ask, /lint
```

## Daily workflows

### Add knowledge

1. Put the source in `raw/inbox/` (or anywhere under `raw/`).
2. Run `/ingest <path>`.
3. Review the changed pages in Obsidian. The agent reports every page it touched, any contradictions it found, and suggested next sources.
4. If you want more control, say “discuss the takeaways first” before the ingest. The agent will summarize before writing.

You can also ingest a URL directly. The agent saves a Markdown copy under `raw/sources/` with provenance, then processes it.

### Ask questions

Run `/ask <question>`. The agent reads the index, searches the wiki, follows links to sources, and answers with citations.

Substantial answers can be filed back into the wiki as question or comparison pages. This is how explorations compound instead of disappearing into chat history.

### Health-check

Run `/lint`. The script checks deterministic issues first:

- broken wikilinks and missing assets
- pages missing from the index
- missing or invalid frontmatter
- duplicate titles or slugs
- source pages whose raw file is gone
- orphan pages and malformed log entries

Then the agent reviews content for contradictions, stale claims, missing concept pages, missing cross-references, and gaps worth filling with new sources. It writes a report to `wiki/meta/` and logs the pass.

## Helper CLI

```bash
python3 scripts/wiki.py search "persistent wiki"   # ranked search with snippets
python3 scripts/wiki.py lint                        # health check; exit 1 on errors
python3 scripts/wiki.py stats                       # page, word, link, and source counts
python3 scripts/wiki.py new concept "Attention"     # create wiki/concepts/attention.md from a template
```

Run `python3 scripts/wiki.py --help` or `<command> --help` for options.

The search is deliberately simple: term frequency with title and tag boosts. It works well at the scale where the index file still fits in context. If the wiki grows past that, add a local search engine such as [qmd](https://github.com/tobi/qmd) and keep the same interface.

## Obsidian notes

- **Web Clipper** is the fastest way to get articles into `raw/inbox/`.
- **Download images locally:** the attachment folder is already set to `raw/assets/`. Bind a hotkey to “Download attachments for current file” in Settings → Hotkeys, then run it after clipping an article.
- **Graph view** shows the shape of the wiki: hubs, clusters, and orphans. To focus on the wiki layer, type `path:wiki` in the graph's search filter; otherwise the graph also shows `raw/`, `templates/`, and docs.
- **`wiki/views.base`** is a native Base. Use it to sort by `updated`, filter by `type` or `status`, and find `seed` and `stale` pages.
- **Templates** are configured. Insert one with the Templates core plugin, or let the agent use them.
- **Links** are wikilinks. When editing a table manually, escape the pipe: `[[slug\|Display]]`.
- **Optional output formats:** Marp for slide decks, Canvas for visual maps, Dataview for frontmatter queries. Markdown is the default; add these only if you use them.

If Obsidian was open while this vault was configured, it may not have picked up the settings. Check Settings → Files and links → Attachment folder path, and Settings → Templates → Template folder. If needed, restart Obsidian.

## Git

The repository is initialized. To make the first commit, set your identity once and commit:

```bash
git config user.name "Your Name"
git config user.email "you@example.com"
git commit -m "Initialize LLM Wiki"
```

After that, commit after significant ingests or lint passes. The wiki is just Markdown, so you get history, diffs, branching, and backup for free.

## Customizing

- **Domain:** edit the “Domain and scope” section of `wiki/overview.md`. Everything else is domain-agnostic.
- **Page types:** add a folder and a template, then update sections 4 and 5 of `AGENTS.md`.
- **Language:** sources and wiki pages can be in any language. Keep frontmatter keys in English.
- **Workflows:** `AGENTS.md` is meant to co-evolve. When you find a better ingest or lint routine, update the schema and note the change in `wiki/log.md`.
- **Reset the demo:** delete the seeded pages under `wiki/sources/` and `wiki/concepts/`, then reset `wiki/index.md`, `wiki/log.md`, and `wiki/overview.md`. Keep the templates and scripts.

## Scaling

- **Index-first navigation** works surprisingly well to roughly 100 sources and a few hundred pages.
- **Add search** when the index gets too large for context. A local hybrid search tool is the natural next step.
- **Split pages** at about 2,000–2,500 words. Keep one concept per page.
- **Lint regularly.** The wiki stays healthy because maintenance is cheap, not because it is maintenance-free.

## Troubleshooting

- **The agent ignores the schema.** Confirm `AGENTS.md` is at the vault root and start a new OpenCode session so it is loaded.
- **A link is broken.** Run `python3 scripts/wiki.py lint`; it names the page and target.
- **A page is missing from the index.** The lint check reports it; add a `- [[slug|Title]] — summary.` line to the right category.
- **The wiki feels shallow.** Ingest more sources, not more pages. A page with one source is a seed; a page with three independent sources is knowledge.
