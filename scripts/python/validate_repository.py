#!/usr/bin/env python3
"""Offline publication checks; no target systems, credentials or network access.

Checks Git's tracked and nonignored candidate files. Markdown parsing is scoped
to this repository's inline links/fences. This is not a complete Markdown parser,
secret scanner, SQL validator, Mermaid parser or SailPoint schema validator.
"""
from __future__ import annotations

import csv
import io
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]


def main() -> int:
    paths = subprocess.check_output(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=ROOT,
    ).decode().split("\0")
    files = sorted({ROOT / name for name in paths if name and (ROOT / name).is_file()})
    errors: list[str] = []
    counts = {"files": len(files), "markdown": 0, "relative_links": 0,
              "mermaid_blocks": 0, "xml": 0, "csv_rows": 0}
    forbidden = {".jar", ".war", ".class", ".pem", ".key", ".p12", ".pfx",
                 ".jks", ".log", ".zip", ".hprof", ".dmp"}
    token_patterns = [r"gh[pousr]_[A-Za-z0-9]{20,}", r"github_pat_[A-Za-z0-9_]{20,}",
                      r"AKIA[0-9A-Z]{16}", r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"]
    required = ["README.md", "LICENSE", "SECURITY.md", "CONTRIBUTING.md",
                "docs/implementation-status.md", "docs/evidence/README.md"]
    for name in required:
        if not (ROOT / name).is_file():
            errors.append(f"Missing required file: {name}")

    for path in files:
        label = path.relative_to(ROOT).as_posix()
        if path.suffix.lower() in forbidden or (path.name.startswith(".env") and path.name != ".env.example"):
            errors.append(f"Forbidden publication artifact: {label}")
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except (UnicodeError, OSError):
            errors.append(f"Non-UTF-8 or unreadable artifact needs manual review: {label}")
            continue
        # Report only locations/categories, never the potential secret itself.
        for pattern in token_patterns:
            if re.search(pattern, content):
                errors.append(f"Potential credential/private key: {label}")
        assignment = r'''(?i)(?:password|client_secret|api_key|access_token)\s*[:=]\s*["']([^"'\n]+)["']'''
        for match in re.finditer(assignment, content):
            if not re.fullmatch(r"YOUR_[A-Z0-9_]+", match.group(1)):
                errors.append(f"Review credential-like literal: {label}")
        if path.suffix == ".xml":
            counts["xml"] += 1
            try:
                ET.fromstring(content)
            except ET.ParseError as exc:
                errors.append(f"Malformed XML {label}: {exc}")
        if path.suffix != ".md":
            continue
        counts["markdown"] += 1
        prose: list[str] = []
        fence_char = ""
        fence_length = 0
        for line in content.splitlines():
            fence = re.match(r"^\s{0,3}(`{3,}|~{3,})(.*)$", line)
            if fence:
                marker, info = fence.groups()
                if not fence_char:
                    fence_char, fence_length = marker[0], len(marker)
                    if info.strip() == "mermaid":
                        counts["mermaid_blocks"] += 1
                elif marker[0] == fence_char and len(marker) >= fence_length and not info.strip():
                    fence_char = ""
                continue
            if not fence_char:
                prose.append(line)
        if fence_char:
            errors.append(f"Unclosed Markdown fence: {label}")
        # All authored internal links currently target files, without fragments.
        for match in re.finditer(r"!?\[[^\]\n]*\]\(([^)\n]+)\)", "\n".join(prose)):
            target = match.group(1).strip().strip("<>")
            if target.startswith("#") or urlsplit(target).scheme:
                continue
            parsed = urlsplit(target)
            counts["relative_links"] += 1
            resolved = (path.parent / unquote(parsed.path)).resolve()
            if not resolved.is_relative_to(ROOT):
                errors.append(f"Link escapes repository: {label} -> {target}")
            elif not resolved.exists():
                errors.append(f"Broken relative link: {label} -> {target}")

    fixture = ROOT / "sample-data/synthetic/northstar-hr.csv"
    secondary = ROOT / "sample-data/synthetic/secondary-authoritative.csv"
    if fixture.is_file() and secondary.is_file():
        rows = list(csv.DictReader(io.StringIO(fixture.read_text())))
        other = list(csv.DictReader(io.StringIO(secondary.read_text())))
        counts["csv_rows"] = len(rows) + len(other)
        identifiers = [row["employeeID"] for row in rows]
        if len(rows) != 5 or len(set(identifiers)) != 5:
            errors.append("Primary HR fixture must contain five distinct employee IDs")
        by_id = {row["employeeID"]: row for row in rows}
        for row in rows:
            manager = row["managerEmployeeID"]
            if manager and (manager not in by_id or manager == row["employeeID"]):
                errors.append("Primary HR fixture has invalid manager relationship")
            if not row["email"].endswith("@example.org"):
                errors.append("Primary HR fixture has a non-example email domain")
        if by_id.get("200", {}).get("managerEmployeeID") != "100":
            errors.append("Expected Bob to Ann illustrative manager relationship")
        if "401" not in {row["employeeID"] for row in other} & set(identifiers):
            errors.append("Secondary fixture must preserve intentional duplicate key 401")
    else:
        errors.append("Missing synthetic HR fixtures")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("PASS: " + ", ".join(f"{key}={value}" for key, value in counts.items()))
    print("Scope: relative file links, fences, XML well-formedness, fixture invariants,")
    print("and heuristic credential/artifact checks. No external URLs or integrations tested.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
