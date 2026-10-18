#!/usr/bin/env python3
"""Validate the portable skill shape and, optionally, a ZIP distribution.

This intentionally uses only the Python standard library so it can run in a
fresh checkout without installing a package manager or YAML dependency.
"""

from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path


NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("SKILL.md must start with YAML frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError("SKILL.md frontmatter has no closing '---'") from exc

    values: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith(" "):
            continue
        key, separator, value = line.partition(":")
        if not separator:
            raise ValueError(f"unsupported frontmatter line: {line}")
        values[key.strip()] = value.strip().strip('"')
    return values, "\n".join(lines[end + 1 :])


def validate_directory(root: Path) -> list[str]:
    errors: list[str] = []
    skill = root / "SKILL.md"
    if not skill.is_file():
        return ["missing SKILL.md"]

    try:
        metadata, body = frontmatter(skill)
    except ValueError as exc:
        return [str(exc)]

    name = metadata.get("name", "")
    description = metadata.get("description", "")
    if not NAME_RE.fullmatch(name):
        errors.append("frontmatter name must be lowercase hyphenated text")
    if len(name) > 64:
        errors.append("frontmatter name exceeds 64 characters")
    if len(description) == 0 or len(description) > 1024:
        errors.append("frontmatter description must be 1-1024 characters")
    if root.name != name:
        errors.append(f"frontmatter name '{name}' does not match directory '{root.name}'")

    for reference in re.findall(r"\]\((references/[^)]+)\)", body):
        if not (root / reference).is_file():
            errors.append(f"missing linked reference: {reference}")

    skill_files = list(root.rglob("SKILL.md"))
    if len(skill_files) != 1:
        errors.append("package must contain exactly one SKILL.md")

    apm = root / "apm.yml"
    if apm.is_file():
        apm_text = apm.read_text(encoding="utf-8")
        for required in ("name:", "version:", "type: skill"):
            if required not in apm_text:
                errors.append(f"apm.yml is missing '{required}'")

    return errors


def validate_zip(archive: Path) -> list[str]:
    errors: list[str] = []
    with zipfile.ZipFile(archive) as bundle:
        names = bundle.namelist()
        if any(Path(name).is_absolute() or ".." in Path(name).parts for name in names):
            errors.append("ZIP contains an absolute or parent-traversal path")
        skill_names = [name for name in names if name.endswith("/SKILL.md") or name == "SKILL.md"]
        if len(skill_names) != 1:
            errors.append("ZIP must contain exactly one SKILL.md")
    return errors


def main(argv: list[str]) -> int:
    root = Path(argv[1] if len(argv) > 1 else ".").resolve()
    errors = validate_directory(root)
    if len(argv) > 2:
        errors.extend(validate_zip(Path(argv[2]).resolve()))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"OK: {root}")
    if len(argv) > 2:
        print(f"OK: {Path(argv[2]).resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
