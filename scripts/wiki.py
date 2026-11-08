#!/usr/bin/env python3
"""Helper CLI for an LLM-maintained Markdown wiki.

Commands:
  search QUERY    Rank wiki pages by term matches and print snippets.
  lint            Check links, frontmatter, index coverage, orphans, and log format.
  stats           Print page, word, link, and source counts.
  new TYPE TITLE  Create a page from templates/ and print next steps.

Stdlib only. Works on Python 3.9+.
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
RAW = ROOT / "raw"
TEMPLATES = ROOT / "templates"

WIKILINK_RE = re.compile(r"\[\[([^\[\]]+?)\]\]")
FRONTMATTER_RE = re.compile(r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*\r?\n?", re.DOTALL)
LOG_ENTRY_RE = re.compile(r"^## \[(\d{4}-\d{2}-\d{2})\] ([a-z]+) \| (.+)$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

TYPES = {
    "source",
    "concept",
    "entity",
    "comparison",
    "question",
    "overview",
    "meta",
    "index",
    "log",
}
STATUSES = {"seed", "developing", "evergreen", "stale", "archived"}
CONFIDENCES = {"low", "medium", "high"}
COMMON_FIELDS = ["title", "type", "status", "created", "updated", "tags"]
TYPE_FIELDS = {
    "source": ["source_path"],
    "concept": ["sources", "confidence"],
    "entity": ["sources", "confidence"],
    "comparison": ["sources", "confidence"],
    "question": ["sources", "confidence"],
}
NEW_TYPES = {
    "source": ("sources", "source.md"),
    "concept": ("concepts", "concept.md"),
    "entity": ("entities", "entity.md"),
    "comparison": ("comparisons", "comparison.md"),
    "question": ("questions", "question.md"),
}
SKIP_INDEX = {"index", "log"}
SKIP_ORPHANS = {"index", "log", "overview"}


@dataclass
class Page:
    path: Path
    rel: str
    slug: str
    text: str
    body: str
    fm: dict


def strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def parse_frontmatter(text: str):
    """Parse the small YAML subset used by this vault."""
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text

    data = {}
    key = None
    for line in match.group(1).splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        list_match = re.match(r"^-\s+(.*)$", stripped)
        if list_match and key:
            if not isinstance(data.get(key), list):
                data[key] = []
            data[key].append(strip_quotes(list_match.group(1)))
            continue

        if ":" in line:
            raw_key, raw_value = line.split(":", 1)
            key = raw_key.strip()
            value = raw_value.strip()
            if value == "":
                data[key] = []
            elif value.startswith("[") and value.endswith("]"):
                inner = value[1:-1].strip()
                data[key] = (
                    [strip_quotes(item.strip()) for item in inner.split(",")]
                    if inner
                    else []
                )
            else:
                data[key] = strip_quotes(value)

    return data, text[match.end() :]


def load_pages():
    pages = []
    if not WIKI.exists():
        return pages
    for path in sorted(WIKI.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        pages.append(
            Page(
                path=path,
                rel=path.relative_to(ROOT).as_posix(),
                slug=path.stem,
                text=text,
                body=body,
                fm=fm,
            )
        )
    return pages


def wikilinks(text: str):
    for match in WIKILINK_RE.finditer(text):
        raw = match.group(1)
        target = raw.split("|", 1)[0]
        target = target.replace("\\", "")
        target = target.split("#", 1)[0].strip()
        if target.endswith(".md"):
            target = target[:-3]
        if target:
            yield target


def build_link_maps(pages):
    by_slug = defaultdict(list)
    by_rel = {}
    for page in pages:
        by_slug[page.slug].append(page)
        by_rel[page.rel[:-3]] = page  # wiki/concepts/foo
        by_rel[page.path.relative_to(WIKI).as_posix()[:-3]] = page  # concepts/foo
    return by_slug, by_rel


def resolve_link(target: str, by_slug, by_rel):
    target = target.strip().strip("/")
    if not target:
        return None
    if target in by_rel:
        return by_rel[target]
    if target.startswith("wiki/"):
        short = target[5:]
        if short in by_rel:
            return by_rel[short]
    if target in by_slug and len(by_slug[target]) == 1:
        return by_slug[target][0]
    if "/" in target:
        stem = target.rsplit("/", 1)[-1]
        if stem in by_slug and len(by_slug[stem]) == 1:
            return by_slug[stem][0]
    return None


def build_file_maps():
    rels = set()
    names = defaultdict(list)
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith(".git/") or rel.startswith(".obsidian/"):
            continue
        rels.add(rel)
        names[path.name].append(rel)
    return rels, names


def is_asset_target(target: str) -> bool:
    suffix = Path(target).suffix.lower()
    return bool(suffix) and suffix != ".md"


def resolve_asset(target: str, rels, names):
    target = target.strip().strip("/")
    if target in rels:
        return target
    if target in names:
        return names[target][0]
    if "/" in target:
        base = target.rsplit("/", 1)[-1]
        if base in names:
            return names[base][0]
    return None


def slugify(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_text.lower()).strip("-")
    return slug or "untitled"


def cmd_search(args):
    query = " ".join(args.query)
    terms = [
        term.lower()
        for term in re.findall(r"[A-Za-z0-9_][A-Za-z0-9_\-']*", query)
    ]
    if not terms:
        print("Query has no searchable terms.", file=sys.stderr)
        return 1

    results = []
    for page in load_pages():
        if page.slug in SKIP_INDEX and not args.all:
            continue

        body_lower = page.body.lower()
        title = str(page.fm.get("title", page.slug)).lower()
        tags_value = page.fm.get("tags", [])
        tags = (
            " ".join(str(tag) for tag in tags_value).lower()
            if isinstance(tags_value, list)
            else str(tags_value).lower()
        )

        score = 0
        first_index = None
        for term in terms:
            count = body_lower.count(term)
            if not count:
                continue
            score += count
            if term in title:
                score += 8
            if term in tags:
                score += 4
            index = body_lower.find(term)
            if index >= 0 and (first_index is None or index < first_index):
                first_index = index

        if not score:
            continue

        index = first_index if first_index is not None else 0
        start = max(0, index - args.context // 2)
        end = min(len(page.body), index + args.context)
        snippet = re.sub(r"\s+", " ", page.body[start:end]).strip()
        if start > 0:
            snippet = "..." + snippet
        if end < len(page.body):
            snippet = snippet + "..."
        results.append((score, page, snippet))

    results.sort(key=lambda item: (-item[0], item[1].rel))

    if not results:
        print(f"No matches for: {query}")
        return 0

    print(f"Search: {query} ({len(results)} match{'es' if len(results) != 1 else ''})")
    for position, (score, page, snippet) in enumerate(results[: args.limit], 1):
        title = page.fm.get("title", page.slug)
        print()
        print(f"{position}. {title}  [score {score}]")
        print(f"   {page.rel}")
        print(f"   {snippet}")

    if len(results) > args.limit:
        print()
        print(f"... {len(results) - args.limit} more. Use --limit to see more.")
    return 0


def cmd_lint(args):
    pages = load_pages()
    if not pages:
        print("No Markdown pages found under wiki/.")
        return 1

    errors = []
    warnings = []
    by_slug, by_rel = build_link_maps(pages)
    rels, names = build_file_maps()

    slug_groups = defaultdict(list)
    for page in pages:
        slug_groups[page.slug].append(page)
    for slug, group in slug_groups.items():
        if len(group) > 1:
            errors.append(
                f"duplicate slug '{slug}': {', '.join(page.rel for page in group)}"
            )

    title_groups = defaultdict(list)
    for page in pages:
        title = str(page.fm.get("title", "")).strip().lower()
        if title:
            title_groups[title].append(page.rel)
    for title, group in title_groups.items():
        if len(group) > 1:
            warnings.append(f"duplicate title '{title}': {', '.join(group)}")

    for page in pages:
        if not page.fm:
            errors.append(f"{page.rel}: missing YAML frontmatter")
            continue

        for field in COMMON_FIELDS:
            if field not in page.fm:
                errors.append(f"{page.rel}: missing frontmatter field '{field}'")

        page_type = str(page.fm.get("type", "")).strip()
        if page_type not in TYPES:
            errors.append(f"{page.rel}: invalid type '{page_type}'")

        status = str(page.fm.get("status", "")).strip()
        if status and status not in STATUSES:
            errors.append(f"{page.rel}: invalid status '{status}'")

        confidence = str(page.fm.get("confidence", "")).strip()
        if confidence and confidence not in CONFIDENCES:
            errors.append(f"{page.rel}: invalid confidence '{confidence}'")

        for field in ("created", "updated"):
            value = str(page.fm.get(field, "")).strip()
            if value and not DATE_RE.match(value):
                warnings.append(f"{page.rel}: {field} is not YYYY-MM-DD: {value}")

        for field in TYPE_FIELDS.get(page_type, []):
            if field not in page.fm:
                errors.append(
                    f"{page.rel}: missing frontmatter field '{field}' for type {page_type}"
                )

        if page_type == "source":
            source_path = str(page.fm.get("source_path", "")).strip()
            if source_path and not (ROOT / source_path).exists():
                errors.append(
                    f"{page.rel}: source_path does not exist: {source_path}"
                )

        for target in wikilinks(page.body):
            if is_asset_target(target):
                if not resolve_asset(target, rels, names):
                    errors.append(f"{page.rel}: broken asset link [[{target}]]")
            elif not resolve_link(target, by_slug, by_rel):
                errors.append(f"{page.rel}: broken link [[{target}]]")

        words = len(page.body.split())
        if words < 40:
            warnings.append(f"{page.rel}: stub ({words} words)")

    index = next((page for page in pages if page.slug == "index"), None)
    if index is None:
        errors.append("wiki/index.md is missing")
    else:
        indexed = set()
        for target in wikilinks(index.body):
            resolved = resolve_link(target, by_slug, by_rel)
            if resolved:
                indexed.add(resolved.slug)
        for page in pages:
            if page.slug in SKIP_INDEX:
                continue
            if page.slug not in indexed:
                errors.append(f"{page.rel}: not listed in wiki/index.md")

    inbound = defaultdict(set)
    for page in pages:
        for target in wikilinks(page.body):
            if is_asset_target(target):
                continue
            resolved = resolve_link(target, by_slug, by_rel)
            if resolved and resolved.slug != page.slug:
                inbound[resolved.slug].add(page.slug)

    for page in pages:
        if page.slug in SKIP_ORPHANS:
            continue
        if str(page.fm.get("type", "")).strip() == "meta":
            continue  # reports are index-only by design
        sources = inbound.get(page.slug, set())
        if not sources:
            warnings.append(f"{page.rel}: orphan (no inbound links)")
        elif sources == {"index"}:
            warnings.append(
                f"{page.rel}: only linked from the index; add cross-links or integrate it"
            )
        elif sources == {"overview"}:
            warnings.append(f"{page.rel}: only linked from overview")

    log = next((page for page in pages if page.slug == "log"), None)
    if log is None:
        errors.append("wiki/log.md is missing")
    else:
        entries = []
        for line in log.body.splitlines():
            if not line.startswith("## "):
                continue
            match = LOG_ENTRY_RE.match(line)
            if not match:
                warnings.append(
                    f"wiki/log.md: malformed entry heading: {line.strip()}"
                )
            else:
                entries.append(match)
        dates = [match.group(1) for match in entries]
        if dates != sorted(dates):
            warnings.append("wiki/log.md: entries are not in chronological order")
        if not entries:
            warnings.append("wiki/log.md: no entries found")

    today = date.today()
    for page in pages:
        status = str(page.fm.get("status", "")).strip()
        if status == "stale":
            warnings.append(f"{page.rel}: marked stale")
        updated = str(page.fm.get("updated", "")).strip()
        if DATE_RE.match(updated):
            try:
                age = (today - date.fromisoformat(updated)).days
            except ValueError:
                age = 0
            if age > args.stale_days and status not in ("archived", "stale"):
                warnings.append(f"{page.rel}: not updated in {age} days")

    print(f"Wiki lint — {ROOT}")
    print()
    if errors:
        print(f"Errors ({len(errors)}):")
        for error in errors:
            print(f"  ERROR  {error}")
    else:
        print("Errors: none")
    print()
    if warnings:
        print(f"Warnings ({len(warnings)}):")
        for warning in warnings:
            print(f"  WARN   {warning}")
    else:
        print("Warnings: none")
    print()
    print(
        f"Summary: {len(pages)} pages, {len(errors)} error(s), {len(warnings)} warning(s)"
    )

    if errors or (args.strict and warnings):
        return 1
    return 0


def cmd_stats(args):
    pages = load_pages()
    words = sum(len(page.body.split()) for page in pages)
    links = sum(len(list(wikilinks(page.body))) for page in pages)
    types = Counter(str(page.fm.get("type", "unknown")) for page in pages)

    raw_files = []
    if RAW.exists():
        raw_files = [
            path
            for path in RAW.rglob("*")
            if path.is_file() and not path.name.startswith(".")
        ]

    print("Wiki statistics")
    print(f"  Pages: {len(pages)}")
    print(f"  Words: {words}")
    print(f"  Wikilinks: {links}")
    print(f"  Raw files: {len(raw_files)}")
    print(
        "  By type: "
        + ", ".join(f"{name} {count}" for name, count in sorted(types.items()))
    )

    log = next((page for page in pages if page.slug == "log"), None)
    if log:
        entries = [
            line for line in log.body.splitlines() if line.startswith("## [")
        ]
        print(f"  Log entries: {len(entries)}")
        if entries:
            print(f"  Last entry: {entries[-1][3:]}")
    return 0


def cmd_new(args):
    page_type = args.type.lower()
    if page_type not in NEW_TYPES:
        print(
            f"Unknown type '{page_type}'. Choose from: "
            + ", ".join(sorted(NEW_TYPES))
            + ".",
            file=sys.stderr,
        )
        return 1

    folder, template_name = NEW_TYPES[page_type]
    template = TEMPLATES / template_name
    if not template.exists():
        print(f"Template not found: {template}", file=sys.stderr)
        return 1

    title = " ".join(args.title).strip()
    slug = slugify(title)
    destination = WIKI / folder / f"{slug}.md"
    if destination.exists():
        print(
            f"Page already exists: {destination.relative_to(ROOT)}",
            file=sys.stderr,
        )
        return 1

    today = date.today().isoformat()
    text = template.read_text(encoding="utf-8")
    text = (
        text.replace("{{title}}", title)
        .replace("{{date}}", today)
        .replace("{{slug}}", slug)
    )
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(text, encoding="utf-8")

    print(f"Created {destination.relative_to(ROOT)}")
    print("Next: fill it in, add it to wiki/index.md, and append an entry to wiki/log.md.")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Search, lint, and maintain an LLM-maintained Markdown wiki."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    search_parser = subparsers.add_parser(
        "search", help="Rank wiki pages by term matches."
    )
    search_parser.add_argument("query", nargs="+", help="Search terms.")
    search_parser.add_argument(
        "--limit", type=int, default=10, help="Maximum results (default: 10)."
    )
    search_parser.add_argument(
        "--context",
        type=int,
        default=180,
        help="Snippet length in characters (default: 180).",
    )
    search_parser.add_argument(
        "--all",
        action="store_true",
        help="Include index.md and log.md in the search.",
    )
    search_parser.set_defaults(func=cmd_search)

    lint_parser = subparsers.add_parser(
        "lint", help="Check links, frontmatter, index coverage, and log format."
    )
    lint_parser.add_argument(
        "--strict", action="store_true", help="Exit 1 when warnings are present."
    )
    lint_parser.add_argument(
        "--stale-days",
        type=int,
        default=365,
        help="Warn when a page has not been updated in this many days (default: 365).",
    )
    lint_parser.set_defaults(func=cmd_lint)

    stats_parser = subparsers.add_parser(
        "stats", help="Print page, word, link, and source counts."
    )
    stats_parser.set_defaults(func=cmd_stats)

    new_parser = subparsers.add_parser(
        "new", help="Create a page from a template."
    )
    new_parser.add_argument(
        "type", help="Page type: source, concept, entity, comparison, question."
    )
    new_parser.add_argument("title", nargs="+", help="Page title.")
    new_parser.set_defaults(func=cmd_new)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
