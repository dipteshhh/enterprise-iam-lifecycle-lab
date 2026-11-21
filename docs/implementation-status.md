# Implementation status

Last reviewed: **2026-11-20**. Scope: repository artifacts and the owner's supplied narrative; no running identity systems were inspected. [Evidence ledger](evidence/README.md).

| Status | Meaning |
|---|---|
| Verified | Inspected original implementation or test evidence confirms the stated scope worked. A local example test verifies only that example. |
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
| Ann Parson approval for Bill Murray access | Previously Completed, Evidence Pending | E-002; inspect approval, request and target evidence separately |
| Oracle Business/IT Role modeling | Previously Completed, Evidence Pending | E-002; inspect required-role relationship and entitlement profile |
| Job-title automatic role assignment | In Progress | Investigated only; capture assignment, provisioning and removal behavior |
| MySQL JDBC connectivity, aggregation and mapping | Previously Completed, Evidence Pending | E-002; inspect schema/query, task result and mapped identity |
| Entra connector connectivity/schema | Previously Completed, Evidence Pending | E-002; inspect sanitized connection test and connector version |
| Entra employeeId correlation | In Progress | Studied; prove unique match and ambiguity handling |
| BeanShell identity count/name/email queries | Previously Completed, Evidence Pending | E-002; reconstructed snippets require IIQ execution evidence |
| QueryOptions, logging and workflow form experiments | Previously Completed, Evidence Pending | E-002; inspect original rule signatures and workflow variables |
| Conditional Oracle Create/Modify workflow | In Progress | No working end-to-end artifact inspected; test both branches and replay |
| Joiner lifecycle automation | In Progress | Design/early study; no complete workflow verified |
| Pre-hire disable/activation, username uniqueness and M365 licensing | Planned | Connectivity alone does not establish provisioning |
| Mover, leaver and additional lifecycle automation | Planned | Defined acceptance scenarios; not executed |
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

The [quality record](quality-assurance.md) records checks performed on the new documentation, fixtures and standalone examples. Passing these checks cannot verify the IIQ, Oracle, MySQL, Entra or AD integrations above. E-001 confirms repository history, not practical implementation.

To advance a row, attach a runtime evidence record with versions, inputs, actual results, target readback, failure/replay tests and reviewer observations. Narrow the row if only one branch or operation has been tested. If an environment becomes confirmed unavailable, record the actual blocker rather than assuming all planned topics are Blocked.
