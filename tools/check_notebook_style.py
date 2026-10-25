"""Audit MAD 4401 notebooks and student-facing repository consistency."""

from __future__ import annotations

import ast
import json
import re
import sys
import tempfile
from pathlib import Path
from urllib.parse import unquote

import pycodestyle

MODULE_DIRECTORIES = ("module_1", "module_2", "module_3")
IGNORED_PYCODESTYLE_CODES = ("E402", "W292", "W503")
NOTEBOOK_NAME_PATTERN = re.compile(r"^\d{2}_[a-z0-9_]+\.ipynb$")
MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
HTML_ID_PATTERN = re.compile(r'\bid=["\']([^"\']+)["\']')
HTML_ANCHOR_PATTERN = re.compile(r'href=["\']#([^"\']+)["\']')


def notebook_paths(root: Path) -> list[Path]:
    """Return all course notebooks in module and filename order."""
    paths: list[Path] = []
    for directory in MODULE_DIRECTORIES:
        paths.extend(sorted((root / directory).glob("*.ipynb")))
    return paths


def source_text(cell: dict) -> str:
    """Return a notebook cell's source as one string."""
    source = cell.get("source", "")
    if isinstance(source, list):
        return "".join(source)
    return str(source)


def check_markdown(path: Path, cells: list[dict]) -> list[str]:
    """Check Markdown cells for the course math-delimiter convention."""
    issues: list[str] = []
    forbidden = (r"\(", r"\)", r"\[", r"\]")

    for cell_number, cell in enumerate(cells, start=1):
        if cell.get("cell_type") != "markdown":
            continue

        text = source_text(cell)
        for delimiter in forbidden:
            if delimiter in text:
                issues.append(
                    f"{path}: cell {cell_number}: use $...$ or $$...$$ "
                    f"instead of {delimiter}."
                )

    return issues


def check_section_title(path: Path, cells: list[dict]) -> list[str]:
    """Check that a numbered notebook starts with its matching section number."""
    issues: list[str] = []
    prefix = path.stem.split("_", maxsplit=1)[0]

    try:
        section_number = int(prefix)
    except ValueError:
        return issues

    first_markdown = next(
        (
            source_text(cell)
            for cell in cells
            if cell.get("cell_type") == "markdown"
        ),
        "",
    )
    expected = f"# Section {section_number}"

    if not first_markdown.lstrip().startswith(expected):
        issues.append(
            f"{path}: first Markdown cell should start with "
            f"'{expected}'."
        )

    return issues


def check_code_cells(path: Path, cells: list[dict]) -> list[str]:
    """Check Python syntax and PEP 8 style for every code cell."""
    issues: list[str] = []

    with tempfile.TemporaryDirectory() as temporary_directory:
        temporary_root = Path(temporary_directory)

        for cell_number, cell in enumerate(cells, start=1):
            if cell.get("cell_type") != "code":
                continue

            code = source_text(cell)
            if not code.strip():
                continue

            try:
                ast.parse(code)
            except SyntaxError as error:
                issues.append(
                    f"{path}: cell {cell_number}: Python syntax error: "
                    f"{error.msg} (line {error.lineno})."
                )
                continue

            temporary_path = temporary_root / (
                f"{path.stem}__cell_{cell_number:03d}.py"
            )
            temporary_path.write_text(code, encoding="utf-8")

            style = pycodestyle.StyleGuide(
                quiet=True,
                max_line_length=79,
                ignore=list(IGNORED_PYCODESTYLE_CODES),
            )
            report = style.check_files([str(temporary_path)])

            if report.total_errors:
                checker = pycodestyle.Checker(
                    filename=str(temporary_path),
                    max_line_length=79,
                    ignore=list(IGNORED_PYCODESTYLE_CODES),
                )
                checker.check_all()
                issues.append(
                    f"{path}: cell {cell_number}: "
                    f"{report.total_errors} PEP 8 issue(s)."
                )

    return issues


def check_notebook(path: Path, root: Path) -> list[str]:
    """Run all checks for one notebook."""
    relative_path = path.relative_to(root)

    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        return [f"{relative_path}: invalid notebook JSON: {error}."]

    cells = notebook.get("cells", [])
    issues: list[str] = []
    issues.extend(check_section_title(relative_path, cells))
    issues.extend(check_markdown(relative_path, cells))
    issues.extend(check_code_cells(relative_path, cells))
    return issues


def check_notebook_names(paths: list[Path], root: Path) -> list[str]:
    """Check the numbered lowercase notebook filename convention."""
    issues: list[str] = []

    for path in paths:
        if not NOTEBOOK_NAME_PATTERN.fullmatch(path.name):
            relative_path = path.relative_to(root)
            issues.append(
                f"{relative_path}: notebook filename should use the "
                "NN_lowercase_snake_case.ipynb convention."
            )

    return issues


def markdown_files(root: Path) -> list[Path]:
    """Return student-facing Markdown files whose local links should work."""
    paths = [
        root / "README.md",
        root / "START_HERE.md",
        root / "GITHUB_GUIDE.md",
    ]
    paths.extend(root / directory / "README.md" for directory in MODULE_DIRECTORIES)
    return [path for path in paths if path.exists()]


def check_local_markdown_links(root: Path) -> list[str]:
    """Check that relative links in student-facing Markdown files resolve."""
    issues: list[str] = []

    for path in markdown_files(root):
        text = path.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK_PATTERN.findall(text):
            target = target.strip().strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue

            local_target = unquote(target.split("#", maxsplit=1)[0])
            local_target = local_target.split("?", maxsplit=1)[0]
            if not local_target:
                continue

            resolved = (path.parent / local_target).resolve()
            if not resolved.exists():
                relative_path = path.relative_to(root)
                issues.append(
                    f"{relative_path}: local link does not resolve: {target}"
                )

    return issues


def check_notebook_coverage(
    root: Path,
    paths: list[Path],
) -> list[str]:
    """Check notebook-level navigation in module guides and the Pages site."""
    issues: list[str] = []
    script = (root / "script.js").read_text(encoding="utf-8")

    module_readmes = {
        directory: (root / directory / "README.md").read_text(
            encoding="utf-8"
        )
        for directory in MODULE_DIRECTORIES
    }

    for path in paths:
        relative_path = path.relative_to(root).as_posix()
        directory = path.parent.name

        if relative_path not in script:
            issues.append(
                f"script.js: missing Pages card for {relative_path}."
            )

        if path.name not in module_readmes[directory]:
            issues.append(
                f"{directory}/README.md: missing notebook {path.name}."
            )

    return issues


def check_root_module_navigation(root: Path) -> list[str]:
    """Check that the root README links to each module landing page."""
    issues: list[str] = []
    readme = (root / "README.md").read_text(encoding="utf-8")

    for directory in MODULE_DIRECTORIES:
        target = f"{directory}/README.md"
        if target not in readme:
            issues.append(f"README.md: missing module guide link {target}.")

    return issues


def check_html_anchors(root: Path) -> list[str]:
    """Check that same-page links in the Pages welcome page have targets."""
    html_path = root / "index.html"
    html = html_path.read_text(encoding="utf-8")
    identifiers = set(HTML_ID_PATTERN.findall(html))
    issues: list[str] = []

    for anchor in sorted(set(HTML_ANCHOR_PATTERN.findall(html))):
        if anchor not in identifiers:
            issues.append(
                f"index.html: internal link '#{anchor}' has no matching id."
            )

    return issues


def main() -> int:
    """Check course notebooks and repository navigation consistency."""
    root = Path(__file__).resolve().parents[1]
    paths = notebook_paths(root)

    if not paths:
        print("No course notebooks found.")
        return 1

    all_issues: list[str] = []
    for path in paths:
        print(f"Checking {path.relative_to(root)}")
        all_issues.extend(check_notebook(path, root))

    all_issues.extend(check_notebook_names(paths, root))
    all_issues.extend(check_local_markdown_links(root))
    all_issues.extend(check_notebook_coverage(root, paths))
    all_issues.extend(check_root_module_navigation(root))
    all_issues.extend(check_html_anchors(root))

    if all_issues:
        print("\nRepository audit found issues:\n")
        for issue in all_issues:
            print(f"- {issue}")
        return 1

    print(
        f"\nAll {len(paths)} notebooks and student navigation surfaces "
        "passed the audit."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
