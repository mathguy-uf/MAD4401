"""Check MAD 4401 notebooks for basic consistency and PEP 8 style."""

from __future__ import annotations

import ast
import json
import sys
import tempfile
from pathlib import Path

import pycodestyle

MODULE_DIRECTORIES = ("module_1", "module_2", "module_3")
IGNORED_PYCODESTYLE_CODES = ("E402", "W292", "W503")


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


def check_notebook(path: Path) -> list[str]:
    """Run all checks for one notebook."""
    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        return [f"{path}: invalid notebook JSON: {error}."]

    cells = notebook.get("cells", [])
    issues: list[str] = []
    issues.extend(check_section_title(path, cells))
    issues.extend(check_markdown(path, cells))
    issues.extend(check_code_cells(path, cells))
    return issues


def main() -> int:
    """Check all course notebooks and return a shell-friendly status code."""
    root = Path(__file__).resolve().parents[1]
    paths = notebook_paths(root)

    if not paths:
        print("No course notebooks found.")
        return 1

    all_issues: list[str] = []
    for path in paths:
        relative_path = path.relative_to(root)
        print(f"Checking {relative_path}")
        all_issues.extend(check_notebook(relative_path))

    if all_issues:
        print("\nNotebook style audit found issues:\n")
        for issue in all_issues:
            print(f"- {issue}")
        return 1

    print(f"\nAll {len(paths)} notebooks passed the style audit.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
