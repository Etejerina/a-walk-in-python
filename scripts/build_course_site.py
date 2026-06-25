from __future__ import annotations

import html
import os
import re
import shutil
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
SITE_ROOT = ROOT / "course_site"
CONTENT_ROOT = SITE_ROOT / "content"
README = ROOT / "README.md"
GITHUB_REPO = os.environ.get("GITHUB_REPOSITORY", "Etejerina/a-walk-in-python")
GITHUB_REF = os.environ.get("GITHUB_REF_NAME", "codex-course-site-colab")
EXCLUDED_DIRS = {".git", ".venv", "__pycache__", "notebooks", "course_site"}
EXCLUDED_MARKDOWN_FILES = {ROOT / "docs" / "index.md"}
EXCLUDED_MARKDOWN_PATHS = {path.resolve() for path in EXCLUDED_MARKDOWN_FILES}
LOCAL_MD_LINK_RE = re.compile(r"(!?)\[([^\]]*)\]\(([^)]+)\)")
CODE_FENCE_RE = re.compile(r"^```([A-Za-z0-9_+.-]*)\s*$")


def slugify(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text).strip().lower()
    text = re.sub(r"[*_`]", "", text)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def title_from_markdown(path: Path, markdown: str) -> str:
    in_code = False
    fallback: str | None = None
    for line in markdown.splitlines():
        if CODE_FENCE_RE.match(line.strip()):
            in_code = not in_code
            continue
        if in_code:
            continue
        if line.startswith("## Day "):
            return line[3:].strip()
        if line.startswith("## ") and fallback is None:
            fallback = re.sub(r"[*_`]", "", line[3:]).strip()
        if line.startswith("# ") and fallback is None:
            title = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", line[2:])
            title = re.sub(r"[*_`]", "", title).strip()
            if title != "A walk in Python":
                fallback = title
    return fallback or path.stem.replace("_", " ").title()


def resolve_local_markdown_path(markdown_path: Path, raw_link: str) -> Path | None:
    parsed = urlparse(unquote(raw_link.strip()))
    if parsed.scheme or parsed.netloc or not parsed.path.lower().endswith(".md"):
        return None

    candidate = Path(parsed.path)
    if candidate.is_absolute():
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


def html_path_for_markdown(markdown_path: Path) -> Path:
    return CONTENT_ROOT / markdown_path.relative_to(ROOT).with_suffix(".html")


def notebook_url_for_markdown(markdown_path: Path) -> str:
    notebook_path = markdown_path.relative_to(ROOT).with_suffix(".ipynb")
    return (
        "https://colab.research.google.com/github/"
        f"{GITHUB_REPO}/blob/{GITHUB_REF}/notebooks/{notebook_path.as_posix()}"
    )


def rewrite_inline(text: str, markdown_path: Path) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*\*([^*]+)\*\*\*", r"<strong><em>\1</em></strong>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", escaped)

    def link_replacement(match: re.Match[str]) -> str:
        is_image, label, raw_link = match.groups()
        target = resolve_local_markdown_path(markdown_path, html.unescape(raw_link))
        parsed = urlparse(html.unescape(raw_link.strip()))
        href = html.escape(raw_link)
        if target is not None:
            href = html.escape(
                html_path_for_markdown(target)
                .relative_to(html_path_for_markdown(markdown_path).parent)
                .as_posix()
            )
            if parsed.fragment:
                href += f"#{html.escape(parsed.fragment)}"
        if is_image:
            return f'<img src="{href}" alt="{label}">'
        return f'<a href="{href}">{label}</a>'

    return LOCAL_MD_LINK_RE.sub(link_replacement, escaped)


def markdown_to_html(markdown_path: Path, markdown: str) -> str:
    html_lines: list[str] = []
    list_stack: list[int] = []
    in_code = False
    code_language = ""
    code_buffer: list[str] = []
    in_blockquote = False

    def close_lists() -> None:
        while list_stack:
            html_lines.append("</ul>")
            list_stack.pop()

    def close_blockquote() -> None:
        nonlocal in_blockquote
        if in_blockquote:
            html_lines.append("</blockquote>")
            in_blockquote = False

    for raw_line in markdown.splitlines():
        line = raw_line.rstrip()
        fence_match = CODE_FENCE_RE.match(line)
        if fence_match:
            if not in_code:
                close_lists()
                close_blockquote()
                in_code = True
                code_language = fence_match.group(1).lower()
                code_buffer = []
            else:
                code = html.escape("\n".join(code_buffer))
                html_lines.append(
                    f'<pre><code class="language-{code_language}">{code}</code></pre>'
                )
                in_code = False
            continue

        if in_code:
            code_buffer.append(raw_line)
            continue

        if not line.strip():
            close_lists()
            close_blockquote()
            continue

        heading = re.match(r"^(#{1,6})\s+(.+)$", line)
        if heading:
            close_lists()
            close_blockquote()
            level = len(heading.group(1))
            text = rewrite_inline(heading.group(2), markdown_path)
            anchor = slugify(heading.group(2))
            html_lines.append(f'<h{level} id="{anchor}">{text}</h{level}>')
            continue

        if line.strip("_") == "":
            close_lists()
            close_blockquote()
            html_lines.append("<hr>")
            continue

        if line.startswith(">"):
            close_lists()
            if not in_blockquote:
                html_lines.append("<blockquote>")
                in_blockquote = True
            quote = line.lstrip("> ")
            html_lines.append(f"<p>{rewrite_inline(quote, markdown_path)}</p>")
            continue

        bullet = re.match(r"^(\s*)[*-]\s+(.+)$", raw_line)
        if bullet:
            close_blockquote()
            level = len(bullet.group(1)) // 2
            while len(list_stack) <= level:
                html_lines.append("<ul>")
                list_stack.append(level)
            while len(list_stack) > level + 1:
                html_lines.append("</ul>")
                list_stack.pop()
            html_lines.append(f"<li>{rewrite_inline(bullet.group(2), markdown_path)}</li>")
            continue

        close_lists()
        close_blockquote()
        html_lines.append(f"<p>{rewrite_inline(line, markdown_path)}</p>")

    close_lists()
    close_blockquote()
    return "\n".join(html_lines)


def discover_markdown_files() -> list[Path]:
    files: list[Path] = []
    seen: set[Path] = set()
    queue = [README.resolve()]

    while queue:
        path = queue.pop(0)
        if path in seen:
            continue
        seen.add(path)
        files.append(path)
        markdown = path.read_text(encoding="utf-8")
        for raw_link in LOCAL_MD_LINK_RE.findall(markdown):
            target = resolve_local_markdown_path(path, raw_link[2])
            if target and target not in seen and target not in queue:
                queue.append(target)

    for path in sorted(ROOT.rglob("*.md")):
        if EXCLUDED_DIRS.intersection(path.parts):
            continue
        resolved = path.resolve()
        if resolved in EXCLUDED_MARKDOWN_PATHS:
            continue
        if resolved not in seen:
            files.append(resolved)
            seen.add(resolved)

    return files


def navigation_for_page(output_path: Path, files: list[Path], titles: dict[Path, str]) -> str:
    nav_items = []
    for path in files:
        href = os.path.relpath(html_path_for_markdown(path), output_path.parent)
        href = href.replace(os.sep, "/")
        nav_items.append(f'<a href="{href}">{html.escape(titles[path])}</a>')
    return "<nav>" + "\n".join(nav_items) + "</nav>"


def write_page(
    markdown_path: Path,
    title: str,
    body: str,
    files: list[Path],
    titles: dict[Path, str],
) -> None:
    output_path = html_path_for_markdown(markdown_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    prefix = os.path.relpath(SITE_ROOT, output_path.parent).replace(os.sep, "/")
    if prefix == ".":
        prefix = "."
    prefix = f"{prefix}/"
    colab_url = notebook_url_for_markdown(markdown_path)
    navigation = navigation_for_page(output_path, files, titles)
    page = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)} | A walk in Python</title>
  <script src="{prefix}assets/theme-toggle.js"></script>
  <link rel="stylesheet" href="{prefix}assets/styles.css">
</head>
<body>
  <header class="topbar">
    <a class="brand" href="{prefix}index.html">A walk in Python</a>
    <nav>
      <a href="{prefix}index.html#lessons">Lessons</a>
      <a href="{prefix}index.html#how-to-use">How to use</a>
      <a class="nav-action" href="{colab_url}">Open in Colab</a>
      <button class="theme-toggle" type="button" data-theme-toggle aria-label="Toggle dark mode" aria-pressed="false">
        <span class="theme-toggle-indicator" aria-hidden="true"></span>
        <span>Theme</span>
      </button>
    </nav>
  </header>
  <main class="layout">
    <aside class="sidebar">
      <strong>Course</strong>
      {navigation}
    </aside>
    <article class="content">
      <div class="page-actions">
        <span>{html.escape(markdown_path.relative_to(ROOT).as_posix())}</span>
        <a class="button" href="{colab_url}">Open notebook in Colab</a>
      </div>
      {body}
    </article>
  </main>
</body>
</html>
"""
    output_path.write_text(page, encoding="utf-8")


def main() -> None:
    if SITE_ROOT.exists():
        shutil.rmtree(SITE_ROOT)
    (SITE_ROOT / "assets").mkdir(parents=True)

    files = discover_markdown_files()
    titles = {path: title_from_markdown(path, path.read_text(encoding="utf-8")) for path in files}

    lesson_cards = []
    for path in files:
        if path == README:
            continue
        href = html_path_for_markdown(path).relative_to(SITE_ROOT).as_posix()
        lesson_cards.append(
            f"""
            <article class="lesson-card">
              <h3>{html.escape(titles[path])}</h3>
              <p>{html.escape(path.relative_to(ROOT).as_posix())}</p>
              <div>
                <a href="{href}">Read lesson</a>
                <a href="{notebook_url_for_markdown(path)}">Open in Colab</a>
              </div>
            </article>
            """
        )

    index = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>A walk in Python</title>
  <script src="assets/theme-toggle.js"></script>
  <link rel="stylesheet" href="assets/styles.css">
</head>
<body>
  <header class="topbar">
    <a class="brand" href="index.html">A walk in Python</a>
    <nav>
      <a href="#lessons">Lessons</a>
      <a href="#how-to-use">How to use</a>
      <a class="nav-action" href="https://github.com/{GITHUB_REPO}">GitHub</a>
      <button class="theme-toggle" type="button" data-theme-toggle aria-label="Toggle dark mode" aria-pressed="false">
        <span class="theme-toggle-indicator" aria-hidden="true"></span>
        <span>Theme</span>
      </button>
    </nav>
  </header>
  <main>
    <section class="hero">
      <div>
        <p class="eyebrow">Beginner Python course</p>
        <h1>A readable course with runnable notebooks when learners are ready.</h1>
        <p>
          Start by reading the lessons in the browser. When a learner wants to
          experiment, each page opens a matching notebook in Google Colab.
        </p>
        <div class="hero-actions">
          <a class="button" href="content/README.html">Start reading</a>
          <a class="button secondary" href="{notebook_url_for_markdown(README)}">Open index notebook</a>
        </div>
      </div>
      <div class="terminal-panel" aria-label="Python example">
        <span>Python</span>
        <pre><code>name = "learner"
print(f"Hello, {{name}}!")

# Change the value and run it again.</code></pre>
      </div>
    </section>

    <section id="how-to-use" class="band">
      <h2>How learners should use it</h2>
      <div class="steps">
        <div><strong>1</strong><p>Read the lesson page first.</p></div>
        <div><strong>2</strong><p>Open the notebook in Colab.</p></div>
        <div><strong>3</strong><p>Run one cell at a time and change small values.</p></div>
      </div>
      <p class="note">
        Do not use Run all yet. Some lessons intentionally show Python errors so
        learners can see what those errors look like.
      </p>
    </section>

    <section id="lessons" class="lessons">
      <h2>Lessons</h2>
      <div class="lesson-grid">
        {''.join(lesson_cards)}
      </div>
    </section>
  </main>
</body>
</html>
"""
    (SITE_ROOT / "index.html").write_text(index, encoding="utf-8")

    theme_toggle = """(function () {
  var storageKey = "a-walk-in-python-theme";
  var root = document.documentElement;
  var mediaQuery = window.matchMedia
    ? window.matchMedia("(prefers-color-scheme: dark)")
    : null;

  function getStoredTheme() {
    try {
      return localStorage.getItem(storageKey);
    } catch (error) {
      return null;
    }
  }

  function storeTheme(theme) {
    try {
      localStorage.setItem(storageKey, theme);
    } catch (error) {
      // Theme changes still work for the current page when storage is unavailable.
    }
  }

  function normalizeTheme(theme) {
    return theme === "dark" || theme === "light" ? theme : null;
  }

  function systemTheme() {
    return mediaQuery && mediaQuery.matches ? "dark" : "light";
  }

  function updateToggle(theme) {
    var toggles = document.querySelectorAll("[data-theme-toggle]");

    toggles.forEach(function (toggle) {
      toggle.setAttribute("aria-pressed", theme === "dark" ? "true" : "false");
    });
  }

  function setTheme(theme, persist) {
    root.setAttribute("data-theme", theme);
    root.style.colorScheme = theme;
    if (persist) {
      storeTheme(theme);
    }
    updateToggle(theme);
  }

  function currentTheme() {
    return normalizeTheme(root.getAttribute("data-theme")) || systemTheme();
  }

  setTheme(normalizeTheme(getStoredTheme()) || systemTheme(), false);

  document.addEventListener("DOMContentLoaded", function () {
    updateToggle(currentTheme());

    document.addEventListener("click", function (event) {
      var target = event.target;
      if (!target || !target.closest) {
        return;
      }

      var toggle = target.closest("[data-theme-toggle]");
      if (!toggle) {
        return;
      }

      setTheme(currentTheme() === "dark" ? "light" : "dark", true);
    });
  });

  if (mediaQuery) {
    var handleSystemThemeChange = function () {
      if (!normalizeTheme(getStoredTheme())) {
        setTheme(systemTheme(), false);
      }
    };

    if (mediaQuery.addEventListener) {
      mediaQuery.addEventListener("change", handleSystemThemeChange);
    } else if (mediaQuery.addListener) {
      mediaQuery.addListener(handleSystemThemeChange);
    }
  }
})();
"""
    (SITE_ROOT / "assets" / "theme-toggle.js").write_text(theme_toggle, encoding="utf-8")

    styles = """
:root {
  color-scheme: light;
  --ink: #1d252c;
  --muted: #52616b;
  --line: #d8dee4;
  --paper: #fbfcfd;
  --panel: #ffffff;
  --accent: #0f7b8c;
  --accent-strong: #075c69;
  --warm: #f4b942;
  --button-ink: #ffffff;
  --topbar-bg: rgba(251, 252, 253, 0.94);
  --code-bg: #111920;
  --code-ink: #e8f2f4;
  --quote-bg: #fff8e6;
}

:root[data-theme="dark"] {
  color-scheme: dark;
  --ink: #edf4f7;
  --muted: #adc0ca;
  --line: #2f3b42;
  --paper: #101416;
  --panel: #181f22;
  --accent: #58c4d4;
  --accent-strong: #8ddfed;
  --warm: #f6c661;
  --button-ink: #0d1518;
  --topbar-bg: rgba(16, 20, 22, 0.94);
  --code-bg: #0b1114;
  --code-ink: #eef8fb;
  --quote-bg: #221f15;
}

* { box-sizing: border-box; }

body {
  margin: 0;
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  color: var(--ink);
  background: var(--paper);
  line-height: 1.6;
}

a { color: var(--accent-strong); }

.topbar {
  position: sticky;
  top: 0;
  z-index: 10;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  padding: 14px 28px;
  border-bottom: 1px solid var(--line);
  background: var(--topbar-bg);
  backdrop-filter: blur(12px);
}

.brand {
  color: var(--ink);
  font-weight: 760;
  text-decoration: none;
}

.topbar nav {
  display: flex;
  align-items: center;
  gap: 16px;
  font-size: 14px;
}

.topbar a { text-decoration: none; }

.nav-action,
.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 38px;
  padding: 0 14px;
  border: 1px solid var(--accent);
  background: var(--accent);
  color: var(--button-ink);
  text-decoration: none;
  font-weight: 650;
}

.button.secondary {
  background: transparent;
  color: var(--accent-strong);
}

.theme-toggle {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  min-width: 92px;
  min-height: 38px;
  padding: 0 12px;
  border: 1px solid var(--line);
  background: var(--panel);
  color: var(--ink);
  cursor: pointer;
  font: inherit;
  font-weight: 650;
}

.theme-toggle-indicator {
  position: relative;
  width: 34px;
  height: 18px;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: var(--paper);
  flex: 0 0 auto;
}

.theme-toggle-indicator::after {
  position: absolute;
  top: 3px;
  left: 3px;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--accent);
  content: "";
  transition: transform 160ms ease;
}

:root[data-theme="dark"] .theme-toggle-indicator::after {
  transform: translateX(16px);
}

.hero {
  display: grid;
  grid-template-columns: minmax(0, 1.1fr) minmax(320px, 0.9fr);
  align-items: center;
  gap: 40px;
  max-width: 1160px;
  min-height: calc(100vh - 68px);
  margin: 0 auto;
  padding: 64px 28px;
}

.eyebrow {
  margin: 0 0 16px;
  color: var(--accent-strong);
  font-weight: 760;
  text-transform: uppercase;
  font-size: 13px;
}

h1 {
  max-width: 760px;
  margin: 0;
  font-size: clamp(42px, 7vw, 80px);
  line-height: 0.98;
}

.hero p {
  max-width: 680px;
  color: var(--muted);
  font-size: 18px;
}

.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 28px;
}

.terminal-panel {
  border: 1px solid #26343d;
  background: #111920;
  color: #e8f2f4;
  min-height: 320px;
  padding: 18px;
}

.terminal-panel span {
  display: block;
  margin-bottom: 24px;
  color: var(--warm);
  font-weight: 700;
}

pre {
  overflow: auto;
  padding: 16px;
  background: var(--code-bg);
  color: var(--code-ink);
}

code {
  font-family: "Cascadia Code", Consolas, monospace;
  font-size: 0.94em;
}

.band,
.lessons {
  max-width: 1160px;
  margin: 0 auto;
  padding: 42px 28px;
}

.steps {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 16px;
}

.steps div,
.lesson-card {
  border: 1px solid var(--line);
  background: var(--panel);
  padding: 18px;
}

.steps strong {
  display: inline-grid;
  place-items: center;
  width: 32px;
  height: 32px;
  margin-bottom: 10px;
  background: var(--warm);
}

.note {
  margin-top: 18px;
  color: var(--muted);
}

.lesson-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
  gap: 16px;
}

.lesson-card h3 {
  margin: 0 0 8px;
}

.lesson-card p {
  min-height: 44px;
  color: var(--muted);
  font-size: 14px;
}

.lesson-card div {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.layout {
  display: grid;
  grid-template-columns: 260px minmax(0, 1fr);
  max-width: 1240px;
  margin: 0 auto;
}

.sidebar {
  position: sticky;
  top: 67px;
  height: calc(100vh - 67px);
  overflow: auto;
  padding: 28px 18px;
  border-right: 1px solid var(--line);
}

.sidebar nav {
  display: grid;
  gap: 8px;
  margin-top: 12px;
}

.sidebar a {
  text-decoration: none;
}

.content {
  max-width: 860px;
  padding: 36px 32px 80px;
}

.page-actions {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 24px;
  color: var(--muted);
  font-size: 14px;
}

.content h1,
.content h2,
.content h3 {
  line-height: 1.18;
}

.content h1 {
  font-size: 42px;
}

.content h2 {
  margin-top: 36px;
}

.content table {
  width: 100%;
  border-collapse: collapse;
}

.content th,
.content td {
  border: 1px solid var(--line);
  padding: 8px;
  text-align: left;
}

blockquote {
  margin: 18px 0;
  padding: 1px 18px;
  border-left: 4px solid var(--warm);
  background: var(--quote-bg);
}

@media (max-width: 820px) {
  .topbar,
  .topbar nav,
  .page-actions {
    align-items: flex-start;
    flex-direction: column;
  }

  .hero,
  .layout,
  .steps {
    grid-template-columns: 1fr;
  }

  .hero {
    min-height: auto;
  }

  .sidebar {
    position: static;
    height: auto;
    border-right: 0;
    border-bottom: 1px solid var(--line);
  }
}
"""
    (SITE_ROOT / "assets" / "styles.css").write_text(styles, encoding="utf-8")

    site_readme = """# Course Site

This folder contains a static website for **A walk in Python**.

The intended learner experience is:

1. Read the lesson in the browser.
2. Click **Open in Colab** when they want to run or change code.
3. Run notebook cells one at a time instead of using **Run all**.

The site is generated from the Markdown files in the repository root by:

```bash
python scripts/build_course_site.py
```

The interactive notebooks live in `notebooks/` and are generated by:

```bash
python scripts/convert_md_to_ipynb.py
```

## Why this format

A website is a better default entry point for non-technical learners than raw
notebooks. It gives them a readable course first, while Colab links keep the
code interactive without requiring local setup.

The notebooks are still useful, but they should not be the only public surface:
some cells intentionally raise errors as part of the lesson, so a learner who
clicks **Run all** may think the material is broken.

## Publishing options

- GitHub Pages can host this folder as a static site.
- The Colab links assume notebooks are available in the public GitHub repo under
  `notebooks/`.
- If the repo default branch changes, update `GITHUB_REF` in
  `scripts/build_course_site.py`.
"""
    (SITE_ROOT / "README.md").write_text(site_readme, encoding="utf-8")

    for path in files:
        markdown = path.read_text(encoding="utf-8")
        write_page(path, titles[path], markdown_to_html(path, markdown), files, titles)
        print(f"{path.relative_to(ROOT)} -> {html_path_for_markdown(path).relative_to(ROOT)}")

    print(f"site -> {SITE_ROOT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
