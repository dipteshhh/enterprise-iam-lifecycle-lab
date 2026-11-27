#!/usr/bin/env python3
"""Render reconstructed Leaver XML from canonical BeanShell; never import/run it.

No SailPoint runtime, connector, database or proprietary library is contacted.
Use --check to verify the committed example matches its canonical source.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
SOURCE_DIR = ROOT / "scripts/beanshell/leaver"
OUTPUT = ROOT / "workflows/leaver/northstar-leaver-workflow.example.xml"

VARIABLES = (
    ("identityName", "string", "Lifecycle input: exact IIQ Identity name."),
    ("hasOracleAccount", "boolean", "Matching Oracle Link was discovered."),
    ("assignedBusinessRoles", "List", "Assigned business Bundle names."),
    ("oracleRoles", "Map", "Early stored-Link ROLES snapshots by native identity."),
    ("oracleSystemPrivileges", "Map", "Early SYSTEM_PRIVILEGES snapshots by native identity."),
    ("disablePlan", "sailpoint.object.ProvisioningPlan", "Oracle Disable requests."),
    ("roleRemovalPlan", "sailpoint.object.ProvisioningPlan", "Internal IIQ role removals."),
    ("entitlementRemovalPlan", "sailpoint.object.ProvisioningPlan", "Remaining live Oracle entitlements."),
)
STEPS = (
    ("Start", None, None),
    ("Log Terminated Employee", "log-terminated-employee.bsh", None),
    ("Check Oracle Account", "check-oracle-account.bsh", "hasOracleAccount"),
    ("Discover Assigned Business Roles", "discover-business-roles.bsh", "assignedBusinessRoles"),
    ("Discover Oracle Entitlements", "discover-oracle-entitlements.bsh", None),
    ("Build Disable Provisioning Plan", "build-disable-plan.bsh", "disablePlan"),
    ("Execute Disable Provisioning Plan", None, None),
    ("Build Business Role Removal Plan", "build-business-role-removal-plan.bsh", "roleRemovalPlan"),
    ("Execute Business Role Removal Plan", None, None),
    ("Build Oracle Entitlement Removal Plan", "build-entitlement-removal-plan.bsh", "entitlementRemovalPlan"),
    ("Execute Oracle Entitlement Removal Plan", None, None),
    ("Stop", None, None),
)
EXECUTIONS = {
    "Execute Disable Provisioning Plan": "disablePlan",
    "Execute Business Role Removal Plan": "roleRemovalPlan",
    "Execute Oracle Entitlement Removal Plan": "entitlementRemovalPlan",
}


def nonempty_transition(step: ET.Element, target: str, plan: str) -> None:
    transition = ET.SubElement(step, "Transition", to=target)
    source = ET.SubElement(ET.SubElement(transition, "Script"), "Source")
    source.text = (
        f"return {plan} != null\n"
        f"    && {plan}.getAccountRequests() != null\n"
        f"    && !{plan}.getAccountRequests().isEmpty();"
    )


def render() -> str:
    workflow = ET.Element(
        "Workflow", name="Northstar Leaver Workflow - Reconstructed Example",
        type="IdentityLifecycle", explicitTransitions="true",
    )
    ET.SubElement(workflow, "Description").text = (
        "RECONSTRUCTED, UNEXECUTED documentation example from the owner's "
        "November 26, 2026 narrative. Not original exported source or test evidence. "
        "Review local schema, references, LCM arguments and event configuration "
        "before any isolated import. No automated result gate or reconciliation."
    )
    for name, kind, description in VARIABLES:
        attributes = {"name": name, "type": kind}
        if name == "identityName":
            attributes["input"] = "true"
        if name == "hasOracleAccount":
            attributes["initializer"] = "false"
        variable = ET.SubElement(workflow, "Variable", attributes)
        ET.SubElement(variable, "Description").text = description

    for index, (name, filename, result) in enumerate(STEPS):
        icon = name if name in {"Start", "Stop"} else "Task"
        if name in EXECUTIONS:
            icon = "Provision"
        attributes = {
            "name": name, "icon": icon,
            "posX": str(80 + (index % 4) * 260),
            "posY": str(80 + (index // 4) * 160),
        }
        if result:
            attributes["resultVariable"] = result
        step = ET.SubElement(workflow, "Step", attributes)
        if filename:
            ET.SubElement(step, "Arg", name="identityName", value="ref:identityName")
            if name == "Build Business Role Removal Plan":
                ET.SubElement(step, "Arg", name="assignedBusinessRoles", value="ref:assignedBusinessRoles")
        if name in EXECUTIONS:
            for arg_name, value in (
                ("plan", "ref:" + EXECUTIONS[name]),
                ("identityName", "ref:identityName"),
                ("approvalScheme", "none"),
                ("foregroundProvisioning", "true"),
                ("notificationScheme", "none"),
            ):
                ET.SubElement(step, "Arg", name=arg_name, value=value)
        ET.SubElement(step, "Description").text = (
            f"Reconstructed step {index + 1}: {name}. See labs/leaver/workflow-design.md."
        )
        if filename:
            ET.SubElement(ET.SubElement(step, "Script"), "Source").text = (
                (SOURCE_DIR / filename).read_text(encoding="utf-8")
            )
        if name in EXECUTIONS:
            reference = ET.SubElement(step, "WorkflowRef")
            ET.SubElement(reference, "Reference", {
                "class": "sailpoint.object.Workflow", "name": "LCM Provisioning",
            })

        if name == "Build Disable Provisioning Plan":
            ET.SubElement(step, "Transition", {
                "to": "Execute Disable Provisioning Plan", "when": "ref:hasOracleAccount",
            })
            ET.SubElement(step, "Transition", to="Build Business Role Removal Plan")
        elif name == "Build Business Role Removal Plan":
            nonempty_transition(step, "Execute Business Role Removal Plan", "roleRemovalPlan")
            ET.SubElement(step, "Transition", to="Build Oracle Entitlement Removal Plan")
        elif name == "Build Oracle Entitlement Removal Plan":
            nonempty_transition(step, "Execute Oracle Entitlement Removal Plan", "entitlementRemovalPlan")
            ET.SubElement(step, "Transition", to="Stop")
        elif name != "Stop":
            ET.SubElement(step, "Transition", to=STEPS[index + 1][0])

    ET.indent(workflow, space="  ")
    # ElementTree escapes XML text (including BeanShell &&) without altering the
    # parsed Source text. No copied vendor DTD or licensed objects are included.
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<!-- Generated reconstruction; NOT an original IIQ export. -->\n'
            + ET.tostring(workflow, encoding="unicode") + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Compare without writing")
    args = parser.parse_args()
    content = render()
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != content:
            parser.exit(1, "Leaver XML is out of date; run this builder without --check.\n")
        print("PASS: reconstructed XML matches canonical BeanShell and builder.")
    else:
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT.write_text(content, encoding="utf-8")
        print("Wrote reconstructed Leaver XML; no IIQ import or execution performed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
