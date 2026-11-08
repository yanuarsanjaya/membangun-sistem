---
description: Health-check the wiki and file a lint report
---

Follow the **Lint workflow** in `AGENTS.md`.

1. Run `python3 scripts/wiki.py lint`.
2. Fix every deterministic error: broken links, missing index entries, missing frontmatter, duplicate titles or slugs, missing source files.
3. Review the warnings and the content: contradictions, stale claims, orphans, missing concept pages, missing cross-references, weak confidence, and gaps worth new sources.
4. Write a report to `wiki/meta/lint-YYYY-MM-DD.md`.
5. Add the report to `wiki/index.md` and append a `lint` entry to `wiki/log.md`.

Finish with the 3–5 highest-value next actions.
