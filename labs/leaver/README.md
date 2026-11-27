# Northstar Health automated Leaver Lab

**Implemented, with primary provisioning scenarios tested on November 26, 2026.** This independent SailPoint IdentityIQ lab automates offboarding when a synthetic employee's `employmentStatus` changes from `Active` to `Terminated` in **Northstar Workday HR**, an authoritative CSV application. Northstar Health is a fictional healthcare enterprise; this is not a Workday API integration or a deployed healthcare system.

The workflow locks existing Oracle accounts, removes assigned IIQ Business Roles, and revokes remaining directly granted Oracle roles and system privileges. It continues through role cleanup when an identity has no Oracle account. A live connector read after Business Role removal avoids building the next plan from an earlier, potentially stale entitlement snapshot.

## Implementation and evidence boundary

The completion date and scenario outcomes are the **owner's reported lab results** supplied for this update. Original Leaver workflow XML, BeanShell files, screenshots, task/request records, Log4j2 configuration and DBeaver exports were not supplied or found in the existing repository. No new IdentityIQ or Oracle runtime test was performed while preparing this documentation. [Provenance record E-005](../../docs/evidence/leaver-2026-11-26.md).

The [example workflow XML](../../workflows/leaver/northstar-leaver-workflow.example.xml) and [canonical BeanShell examples](implementation.md) are **reconstructed, unexecuted examples**, not the original exported source or captured evidence. The connector retrieval fragment, AttributeRequest fragment and sample plan shapes supplied by the owner are identified in the implementation guide. Repository checks cannot establish runtime provisioning success.

## Environment

| Component | Responsibility in this lab |
|---|---|
| SailPoint IdentityIQ on Apache Tomcat | Identity Cubes, lifecycle event processing, workflow execution and provisioning |
| MySQL | IdentityIQ backend persistence; separate from the historical MySQL JDBC practice source |
| Java / BeanShell / XML | SailPoint API calls, step scripts, variable bindings and conditional transitions |
| Northstar Workday HR | Synthetic CSV authoritative source for identity attributes and employment state |
| Oracle Application | Connected Oracle Database target in Docker; account provisioning/disablement, role and system-privilege management |
| LCM Provisioning | Subprocess used separately for Disable, Business Role removal and remaining entitlement removal |
| Connector API | Current account retrieval as a `ResourceObject` before remaining entitlement removal |
| Log4j2 / `loggerDex` | Custom diagnostic logging; original logger configuration not available |
| DBeaver | Independent Oracle verification of account state and grants |

Earlier inspected runtime versions are preserved in the [environment record](../../docs/lab-environment.md). They do not establish the exact versions or configuration used for this November 26 run. A licensed IIQ installation and separately configured applications are prerequisites; this repository cannot install or reproduce licensed software by itself.

## Lifecycle trigger and execution

| Setting | Reported lab value |
|---|---|
| Authoritative application | `Northstar Workday HR` |
| Identity attribute | `employmentStatus` |
| Previous value → new value | `Active` → `Terminated` |
| Launched workflow | `Northstar Leaver Workflow` |
| Workflow type | `IdentityLifecycle` |

1. Change the selected synthetic employee's authoritative CSV record from `Active` to `Terminated`.
2. Run **Northstar Account Aggregation** to read and correlate that source record.
3. Run **Identity Refresh with Process Events enabled** using the configured identity attribute mappings and lifecycle event.
4. IdentityIQ evaluates the configured attribute-change event against the identity change.
5. The event launches **Northstar Leaver Workflow** automatically for that identity.

The CSV owns the employment fact. Aggregation brings source-account data into IIQ and associates it with an identity. Identity Refresh applies configured identity processing and evaluates lifecycle events when Process Events is selected. The event selects the business process; the workflow constructs and submits provisioning changes. Editing a CSV alone does not contact Oracle, and an already terminated record is not a new `Active` → `Terminated` change. [SailPoint lifecycle events](https://documentation.sailpoint.com/identityiq/8.5/help/lifecycle_manager/lifecycle_events.html) and [Identity Refresh](https://documentation.sailpoint.com/identityiq_83/help/tasks/identity_refresh.htm) describe these configurable responsibilities; verify the installed release and event configuration.

## Results at a glance

| Scenario | Reported result | Verification boundary |
|---|---|---|
| Mary Jane, `NH-0101`, no Oracle account | Original termination event triggered | Complete final no-account path has **not** been separately retested after the final workflow changes |
| Alex Jones, `NH-1010`, `Alex_Jones` | Account changed from `OPEN` to `LOCKED` | Disable plan, LCM execution and independent DBeaver check reported |
| Sarah Miller, `NH-1001`, `Sarah_Miller` | Account locked; `dba - Business` removed; five associated Oracle roles revoked | Role-based deprovisioning and subsequent aggregation/refresh reconciliation reported |
| John Doe, `John_Doe` | No directly granted Oracle roles or system privileges remained | Zero rows in both `DBA_ROLE_PRIVS` and `DBA_SYS_PRIVS` independently checked through DBeaver, as reported |

See the [test matrix](test-scenarios.md) for expected versus actual results. John's employee ID and an independent account-status readback were not supplied. Zero grant rows do not prove removal of PUBLIC access, object privileges, every effective permission or existing database sessions.

## Documentation and source

- [Workflow design](workflow-design.md): eight variables, twelve top-level steps, branch diagram and three LCM subprocess invocations.
- [Implementation](implementation.md): Identity/Link/Bundle discovery, plan anatomy, live connector reads, source provenance and adaptation instructions.
- [Tests and SQL verification](test-scenarios.md): four scenarios, evidence limits and reusable read-only queries.
- [Troubleshooting](troubleshooting.md): Jane/John partial provisioning, stale Links, XML structure and entitlement dependencies.
- [Future enhancements](future-enhancements.md): explicit gaps between the functional lab and production offboarding.
- [Technical concepts](../../docs/technical-concepts.md) and [current architecture](../../docs/architecture/current-lab.md).

The [Joiner index](../joiner/README.md), historical Oracle exercises and their source/evidence remain available. The **Mover workflow is planned**.
