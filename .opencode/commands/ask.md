---
description: Ask the wiki a question and answer with citations
---

Follow the **Query workflow** in `AGENTS.md` to answer: $ARGUMENTS

If no question is given, ask what the human wants to know.

Read `wiki/index.md` first, search the wiki with `python3 scripts/wiki.py search "<keywords>"`, and read the most relevant pages. Follow links to source pages for provenance.

Answer directly with `[[wikilink]]` citations. Distinguish what the wiki says from your own inference. If the wiki is silent or contradictory, say so.

If the answer is a substantial reusable synthesis (comparison, analysis, discovered connection), offer to file it as a `question` or `comparison` page. If the arguments begin with `--file`, file it immediately and update the index, log, and overview.
