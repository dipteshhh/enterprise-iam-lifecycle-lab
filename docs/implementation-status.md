# Implementation status

Last reviewed: **2026-11-26**. Scope: repository artifacts, owner-reported lifecycle implementation/results in E-005, and the separately captured bounded Oracle runtime exercise in E-004. Current owner-reported completion is distinct from independently inspected execution evidence. [Evidence ledger](evidence/README.md).

| Status | Meaning |
|---|---|
| Verified | Inspected original implementation or test evidence confirms the stated scope worked. A local example test verifies only that example. |
| Implemented / tested (owner-reported) | The owner reports implementation and the specified tests; original runtime evidence/source was not supplied for independent inspection. This is not automatically promoted to Verified. |
| Previously Completed, Evidence Pending | Described in prior lab history; original source or verification evidence has not been inspected. |
| In Progress | Actively being developed; successful completion is not claimed. |
| Planned | Intended future practical exercise. |
| Conceptual | Documentation, model or architecture only. |
| Blocked | A confirmed access, licensing, infrastructure or unresolved dependency prevents execution. |

## Platform capabilities

| Capability | Status | Evidence and next verification |
|---|---|---|
| Local IIQ/Tomcat/JDK/MySQL environment | Previously Completed, Evidence Pending | E-002; record actual IIQ build and supported runtime matrix |
| Log4j2, IIQ debug pages and console | Previously Completed, Evidence Pending | E-002; show a sanitized named-logger event and active config |
| Authoritative CSV application/schema/account aggregation | Previously Completed, Evidence Pending | E-002; inspect task result, Link and Identity Cube |
| Identity attribute mapping and refresh | Previously Completed, Evidence Pending | E-002; compare source, Link and refreshed identity attributes |
| Identity Cube creation and account correlation | Previously Completed, Evidence Pending | E-002; prove stable key and replay outcome |
| Manager correlation: Bob Fields → Ann Parson | Previously Completed, Evidence Pending | E-002; inspect resolved manager reference and missing-manager case |
| Duplicate Mitch Armstrong / Employee ID 401 experiment | Previously Completed, Evidence Pending | E-002; reproduce safely; no complete remediation framework |
| Oracle account/entitlement aggregation and provisioning | Previously Completed, Evidence Pending | E-002; inspect actual connector and Oracle target readback |
| New scoped Oracle connector connectivity | Verified | E-004; saved Oracle Application test succeeded against local FREEPDB1 |
| New Oracle Create account plus narrow role / existing-account Modify | Verified | E-004; requests 14/13 Completed/Success; independent target and exact owned Links agree; no login or complete custom-form claim |
| Sequential duplicate guards for that scoped harness | Verified | E-004; existing-account Create and repeated-role Modify refused before another request; concurrency not tested |
| Ann Parson approval for Bill Murray access | Previously Completed, Evidence Pending | E-002; inspect approval, request and target evidence separately |
| Oracle Business/IT Role modeling | Previously Completed, Evidence Pending | E-002; inspect required-role relationship and entitlement profile |
| Job-title automatic role assignment | In Progress | Investigated only; capture assignment, provisioning and removal behavior |
| MySQL JDBC connectivity, aggregation and mapping | Previously Completed, Evidence Pending | E-002; inspect schema/query, task result and mapped identity |
| Entra connector connectivity/schema | Previously Completed, Evidence Pending | E-002; inspect sanitized connection test and connector version |
| Entra employeeId correlation | In Progress | Studied; prove unique match and ambiguity handling |
| BeanShell identity count/name/email queries | Previously Completed, Evidence Pending | E-002; reconstructed snippets require IIQ execution evidence |
| QueryOptions, logging and workflow form experiments | Previously Completed, Evidence Pending | E-002; inspect original rule signatures and workflow variables |
| Original conditional Oracle selection-form workflow | Broader coverage unverified | Earlier custom-form gaps retained; E-005 reports later same-Create role assignment success for John after Jane's partial failure, without revised source or full form regression |
| Joiner lifecycle automation | Implemented and tested (owner-reported) | E-005; [Joiner index](../labs/joiner/README.md) preserves earlier work and separates current status from missing full Joiner source/evidence |
| Pre-hire disable/activation, username uniqueness and M365 licensing | Planned | Connectivity alone does not establish provisioning |
| Mover lifecycle automation | Planned | No Mover workflow or execution supplied |
| Leaver lifecycle automation | Implemented; primary provisioning scenarios tested (owner-reported) | E-005; [Leaver Lab](../labs/leaver/README.md). Alex locking, Sarah role-based removal/reconciliation, John direct-grant cleanup. Mary's final no-account regression outstanding |
| Leaver role-based Oracle deprovisioning | Tested in this configuration (owner-reported) | Sarah: dba - Business → dba - IT → five roles removed; not a universal role-removal guarantee |
| Leaver dynamic direct-entitlement removal | Tested (owner-reported) | John: zero direct role/system-privilege rows; live connector retrieval documented. PUBLIC/object/session access untested |
| Revised Create AccountRequest with role attributes | Successful later test (owner-reported) | Jane account created but missing ANALYST role caused grant failure; target role created; subsequent John provisioning succeeded. Original revised source unavailable |
| Jane Doe entitlement recovery | Planned | Aggregation/correlation reported; entitlement recovery completion not supplied |
| Leaver XML / BeanShell source in this update | Reconstructed, unexecuted example | Offline artifact checks only; no original Leaver export, schema import or IIQ execution |
| On-premises AD domain, PowerShell and IIQ integration | Planned | No domain controller or local integration verified |
| AD → Entra hybrid sync | Planned | Choose ownership/topology before building |
| SailPoint ISC tenant/source/profile/transforms/access/governance/API | Planned | Tenant access unconfirmed; practical execution gated on access |
| SAML, OAuth/OIDC, SCIM and modern MFA hands-on exercises | Planned | Conceptual foundation only |
| Access reviews/certifications, SoD and role mining | Planned | No campaign, policy or mining result inspected |
| Entra CA, MFA, PIM, Identity Protection, access packages | Planned | Tenant features/licensing and exercises not verified |
| Workload identities, managed identities and NHI governance | Planned | Define product/feature scope before implementation |
| PAM, JIT/JEA and CIEM practical integrations | Planned | Conceptual distinctions documented; no tools integrated |
| Target architectures, control mapping and protocol knowledge base | Conceptual | Design artifacts; no compliance or production claim |

## Repository verification is separate

The [quality record](quality-assurance.md) records repository checks. Those checks alone cannot verify integrations. E-004 separately supplies actual scoped IIQ/Oracle runtime evidence; it does not verify the other historical/platform rows. E-005 records current owner-reported outcomes and their source/evidence gaps. E-001 confirms repository history, not practical implementation.

To advance a row, attach a runtime evidence record with versions, inputs, actual results, target readback, failure/replay tests and reviewer observations. Narrow the row if only one branch or operation has been tested. If an environment becomes confirmed unavailable, record the actual blocker rather than assuming all planned topics are Blocked.
