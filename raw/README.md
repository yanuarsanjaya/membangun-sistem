# Raw Sources

This folder is the **source of truth**. The agent reads from it and never edits it.

## What goes here

Articles, papers, reports, transcripts, book notes, meeting notes, screenshots, data files — anything you want the wiki to be built from.

## Folders

- **`inbox/`** — drop new, unprocessed sources here. Anything is fine; the agent will identify and read it.
- **`sources/`** — the curated collection. Use `YYYY-MM-DD-slug.md` for clipped articles and web pages. Original filenames are fine for PDFs and other files.
- **`assets/`** — images and attachments referenced by sources or wiki pages. Obsidian stores downloaded images here automatically.

## How to add a source

1. **Web article:** use Obsidian Web Clipper, save into `raw/inbox/`, then optionally run “Download attachments for current file” to pull images into `raw/assets/`.
2. **Paper or PDF:** drop the file into `raw/inbox/` or `raw/sources/`.
3. **Manual notes:** create a Markdown file in `raw/inbox/` with your notes and the original URL.
4. **URL only:** tell the agent to ingest the URL. It will save a Markdown copy under `raw/sources/` with provenance before processing.

## Rules

- Do not edit a source after it has been captured. If you need to correct or annotate it, add a new source or a note in the wiki.
- Do not store secrets, credentials, or personal data you would not want in the wiki or a git repository.
- Keep provenance: for web pages, include the URL and capture date at the top (an HTML comment is enough).
- The agent may read images separately from the text. Local images are more reliable than remote URLs.

## Naming

- Markdown clippings: `YYYY-MM-DD-short-slug.md`
- PDFs and other files: original name is fine; prefix with the date if the name is generic.
- Keep names stable after ingest so the wiki's `source_path` links keep working.
