# Practical learning roadmap

The goal is evidence of a small working capability before expanding its scope. [Statuses](implementation-status.md) govern all claims; [test scenarios](../northstar-health/test-scenarios.md) define acceptance.

| Phase | Practical outcome | Prerequisite | Completion evidence |
|---|---|---|---|
| 1 — Recover baseline | Record supported IIQ build/runtime and replay HR aggregation | Licensed existing lab and synthetic fixtures | Versions, settings, task result, mapped attributes, manager and replay check |
| 2 — Conditional Oracle provisioning | One approved narrow role; both existing/absent account paths | Verified target schema and request workflow | T-06 through T-13, Oracle readback and reconciled identity |
| 3 — Joiner | One authoritative event drives one controlled target account | Stable correlation and phase 2 evidence | Successful and rejected/missing-data paths with request trace |
| 4 — Entra pre-hire | Disabled pre-hire account, collision-safe name, scheduled activation | Tenant permissions, supported connector, chosen cloud authority | T-14 through T-16; account/permission/licensing checks separately |
| 5 — Mover and leaver | Verified additions, removals, disablement and exceptions | Reliable lifecycle events and target reconciliation | T-17 through T-19, partial-failure and replay evidence |
| 6 — AD and hybrid | Isolated AD domain, delegated operations and chosen sync topology | Supported Windows infrastructure, DNS and certificates | [AD roadmap](../active-directory/README.md) acceptance records |
| 7 — ISC alternative | Source/profile/transform/access/lifecycle/governance/API exercises | Accessible licensed ISC tenant; no tenant assumed | [ISC roadmap](../sailpoint-isc/README.md) evidence per exercise |
| 8 — Authentication and governance | One OIDC/SAML lab, one SCIM lab, one review/SoD lab | Isolated IdP/SP/resources; approved scope | Token/assertion validation, provisioning readback and remediation evidence |

## Next recommended lab

Complete **conditional Oracle provisioning for one synthetic identity with an existing account and one without**, using a narrow role instead of `DBA`. First record the local versions and verify HR correlation. Keep Create/Modify decision logic separate from execution, preserve configured approvals, and verify target state before declaring either branch complete. Do not assume Create then Modify in one plan is ordered by every connector. See [workflow WIP](../sailpoint-identityiq/workflows/README.md).

## Planned information architecture

Expand only when substantive material exists. Future modules may add `lifecycle-events/`, platform-specific source/connectivity labs, AD PowerShell scripts, Entra Graph requests, ISC transforms/API examples, certification campaigns and SoD policies. Keep executable code canonical beside its platform or in shared `scripts/`; use links instead of duplicate copies. Do not create every directory in the aspirational structure now.

For each new exercise: define objective and failure cases, verify official versioned documentation, implement one scope, collect sanitized evidence, update the status register and record the next unresolved question. Use [resources](../learning/resources.md) and [interview preparation](../learning/interview-preparation.md) to connect concepts to evidence without inflating claims.
