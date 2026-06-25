from __future__ import annotations

import json
import os
import re
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
NOTEBOOK_ROOT = ROOT / "notebooks"
CODE_FENCE_RE = re.compile(r"^(\s*)```([A-Za-z0-9_+.-]*)\s*$")
OUTPUT_RE = re.compile(r"^\s*#\s*output\b", re.IGNORECASE)
LOCAL_MD_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
NEXT_LESSON_LINK_RE = re.compile(r"\[(Go to Day \d+)\]\(([^)]+\.ipynb)\)")
EXCLUDED_DIRS = {".git", ".venv", "__pycache__", "notebooks", "course_site"}
EXCLUDED_MARKDOWN_FILES = {ROOT / "docs" / "index.md"}
EXCLUDED_MARKDOWN_PATHS = {path.resolve() for path in EXCLUDED_MARKDOWN_FILES}


def normalize_source(text: str) -> list[str]:
    if not text:
        return []
    return text.splitlines(keepends=True)


def resolve_local_markdown_path(markdown_path: Path, raw_link: str) -> Path | None:
    parsed = urlparse(unquote(raw_link.strip()))
    if parsed.scheme or parsed.netloc or not parsed.path.lower().endswith(".md"):
        return None

    link_path = parsed.path
    candidate = Path(link_path)
    if link_path.startswith(("/", "\\")) or candidate.is_absolute():
        candidate = ROOT / str(candidate).lstrip("\\/")
    else:
        candidate = markdown_path.parent / candidate
    try:
        resolved = candidate.resolve()
    except OSError:
        return None
    if resolved.is_file() and resolved.suffix.lower() == ".md":
        return resolved
    return None


def notebook_path_for_markdown(markdown_path: Path) -> Path:
    return NOTEBOOK_ROOT / markdown_path.relative_to(ROOT).with_suffix(".ipynb")


def relative_notebook_link(source_notebook: Path, target_markdown: Path) -> str:
    target_notebook = notebook_path_for_markdown(target_markdown)
    relative = os.path.relpath(target_notebook, source_notebook.parent)
    return relative.replace(os.sep, "/")


def rewrite_local_markdown_links(
    text: str,
    markdown_path: Path,
    notebook_path: Path,
) -> str:
    def replacement(match: re.Match[str]) -> str:
        label = match.group(0).split("](", 1)[0]
        raw_link = match.group(1)
        parsed = urlparse(raw_link.strip())
        target_markdown = resolve_local_markdown_path(markdown_path, raw_link)
        if target_markdown is None:
            return match.group(0)

        target_link = relative_notebook_link(notebook_path, target_markdown)
        fragment = f"#{parsed.fragment}" if parsed.fragment else ""
        query = f"?{parsed.query}" if parsed.query else ""
        return f"{label}]({target_link}{query}{fragment})"

    text = LOCAL_MD_LINK_RE.sub(replacement, text)

    def next_lesson_replacement(match: re.Match[str]) -> str:
        label, href = match.groups()
        return f'<a href="{href}" target="_self">{label}</a>'

    return NEXT_LESSON_LINK_RE.sub(next_lesson_replacement, text)


def new_markdown_cell(
    text: str,
    markdown_path: Path,
    notebook_path: Path,
) -> dict[str, object] | None:
    if not text.strip():
        return None
    text = rewrite_local_markdown_links(text, markdown_path, notebook_path)
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": normalize_source(text),
    }


def new_code_cell(text: str) -> dict[str, object] | None:
    code_lines: list[str] = []
    for line in text.splitlines(keepends=True):
        if OUTPUT_RE.match(line):
            break
        code_lines.append(line)

    code = "".join(code_lines).strip("\n")
    if not code.strip():
        return None

    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": normalize_source(code + "\n"),
    }


def markdown_to_notebook(
    markdown: str,
    markdown_path: Path,
    notebook_path: Path,
) -> dict[str, object]:
    cells: list[dict[str, object]] = []
    markdown_buffer: list[str] = []
    code_buffer: list[str] = []
    in_fence = False
    fence_language = ""

    for line in markdown.splitlines(keepends=True):
        fence_match = CODE_FENCE_RE.match(line.rstrip("\n"))
        if fence_match:
            if not in_fence:
                in_fence = True
                fence_language = fence_match.group(2).lower()
                if fence_language == "python":
                    cell = new_markdown_cell(
                        "".join(markdown_buffer),
                        markdown_path,
                        notebook_path,
                    )
                    if cell:
                        cells.append(cell)
                    markdown_buffer = []
                    code_buffer = []
                else:
                    markdown_buffer.append(line)
                continue

            in_fence = False
            if fence_language == "python":
                cell = new_code_cell("".join(code_buffer))
                if cell:
                    cells.append(cell)
            else:
                markdown_buffer.append(line)
            fence_language = ""
            code_buffer = []
            continue

        if in_fence and fence_language == "python":
            code_buffer.append(line)
        else:
            markdown_buffer.append(line)

    if in_fence and fence_language == "python":
        cell = new_code_cell("".join(code_buffer))
        if cell:
            cells.append(cell)
    else:
        cell = new_markdown_cell("".join(markdown_buffer), markdown_path, notebook_path)
        if cell:
            cells.append(cell)

    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def local_markdown_links(markdown_path: Path, markdown: str) -> list[Path]:
    links: list[Path] = []
    for raw_link in LOCAL_MD_LINK_RE.findall(markdown):
        resolved = resolve_local_markdown_path(markdown_path, raw_link)
        if resolved:
            links.append(resolved)
    return links


def markdown_files_in_navigation_order() -> list[Path]:
    discovered: list[Path] = []
    seen: set[Path] = set()
    queue = [README.resolve()] if README.exists() else []

    while queue:
        path = queue.pop(0)
        if path in seen:
            continue
        seen.add(path)
        discovered.append(path)
        markdown = path.read_text(encoding="utf-8")
        for linked_path in local_markdown_links(path, markdown):
            if linked_path not in seen and linked_path not in queue:
                queue.append(linked_path)

    for path in sorted(ROOT.rglob("*.md")):
        if EXCLUDED_DIRS.intersection(path.parts):
            continue
        resolved = path.resolve()
        if resolved in EXCLUDED_MARKDOWN_PATHS:
            continue
        if resolved not in seen:
            discovered.append(resolved)
            seen.add(resolved)

    return discovered


def main() -> None:
    for markdown_path in markdown_files_in_navigation_order():
        notebook_path = notebook_path_for_markdown(markdown_path)
        notebook_path.parent.mkdir(parents=True, exist_ok=True)
        notebook = markdown_to_notebook(
            markdown_path.read_text(encoding="utf-8"),
            markdown_path,
            notebook_path,
        )
        notebook_path.write_text(
            json.dumps(notebook, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        relative_md = markdown_path.relative_to(ROOT)
        relative_ipynb = notebook_path.relative_to(ROOT)
        print(f"{relative_md} -> {relative_ipynb}")


if __name__ == "__main__":
    main()
