#!/usr/bin/env python3
"""Build local console XML from original lab source; never imports or runs it.

Run from the repository root with an explicitly chosen private output directory.
Existing output files cause an error. Review the runbook and current lab state
before any import: these are fixed-scope, version-specific administrative tests.
"""
from pathlib import Path
import argparse
import xml.etree.ElementTree as ET

SOURCES = {
    "runner.bsh": "NS Lab Oracle Runner 20261120",
    "catalog-role.bsh": "NS Lab Oracle Catalog 20261120",
    "refresh-subjects.bsh": "NS Lab Oracle Refresh 20261120",
    "verify-requests.bsh": "NS Lab Oracle Verification 20261120",
    "inspect-requests.bsh": "NS Lab Oracle Evidence 20261120",
    "outcomes.bsh": "NS Lab Oracle Outcomes 20261120",
}
MODES = ("preflight", "seed-identities", "inspect", "reconcile",
         "request-create", "request-modify")


def document(root: ET.Element, doctype_root: str) -> str:
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<!DOCTYPE {doctype_root} PUBLIC "sailpoint.dtd" "sailpoint.dtd">\n'
            + ET.tostring(root, encoding="unicode") + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    source_dir = Path(__file__).resolve().parent
    output = args.output_dir.resolve()
    rendered: dict[str, str] = {}
    for filename, name in SOURCES.items():
        root = ET.Element("sailpoint")
        rule = ET.SubElement(root, "Rule", language="beanshell", name=name)
        ET.SubElement(rule, "Source").text = (source_dir / filename).read_text()
        rendered[Path(filename).stem + ".xml"] = document(root, "sailpoint")
    for mode in MODES:
        root = ET.Element("Map")
        ET.SubElement(root, "entry", key="mode", value=mode)
        rendered[mode + ".xml"] = document(root, "Map")
    collisions = [name for name in rendered if (output / name).exists()]
    if collisions:
        parser.error("Output collision; choose a fresh directory: " + ", ".join(collisions))
    output.mkdir(parents=True, exist_ok=True, mode=0o700)
    for name, text in rendered.items():
        target = output / name
        with target.open("x", encoding="utf-8") as stream:
            stream.write(text)
        target.chmod(0o600)
    print(f"Built {len(rendered)} XML files; no IIQ import or execution performed.")


if __name__ == "__main__":
    main()
