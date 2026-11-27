# Known limitations and future enhancements

The current Leaver Lab is a functional, independently implemented simulation with primary provisioning scenarios reported tested. It is **not production-ready enterprise offboarding**. Original source and raw November 26 results remain unavailable; [E-005](../../docs/evidence/leaver-2026-11-26.md) separates the narrative from reconstructed code.

| Future work — not completed | Why it matters / acceptance target |
|---|---|
| Northstar Health Mover workflow | Test authorized access additions and obsolete removals when employment attributes change. |
| Final no-account regression | Run the final twelve-step workflow for Mary-style identities, with and without Business Roles; verify the skip and convergence paths. |
| Automated provisioning result validation | Inspect results of all three LCM calls; do not treat foreground return or Stop as universal success. |
| Workflow exception handling | Distinguish failed identity lookup, missing target account, unreadable connector state and failed provisioning. |
| Retry and recovery mechanisms | Reconcile partial results before retry; avoid duplicate creates and redundant revokes; test replay and concurrent changes. |
| Provisioning failure notifications | Route actionable exceptions under a reviewed escalation policy. Current lab arguments disable normal approvals/notifications. |
| Termination audit reports | Connect authoritative change, lifecycle decision, plans, results, target verification and unresolved exceptions. |
| Automatic reconciliation after provisioning | Refresh stored Links/Identity Cubes deliberately; live ResourceObject retrieval alone does not persist a reconciled account. |
| Broader multi-application offboarding | Inventory and remove access across additional targets with explicit per-target results. Current workflow targets Oracle and IIQ Business Role assignments. |
| Additional entitlement categories | Test object privileges, PUBLIC-derived/effective access and other connector-supported categories separately. Current dynamic plan covers `ROLES` and `SYSTEM_PRIVILEGES`. |
| Multiple role assignments using assignment IDs | Preserve assignment-specific semantics; name-based `assignedRoles` removal does not establish correct behavior for duplicate assignments or multiple account targets. |
| Prevent automatic role reassignment after termination | Make eligibility/assignment rules termination-aware and verify that later refresh does not restore removed access. |
| Map termination to IIQ inactive status | Explicitly configure and test `inactive`; `employmentStatus = Terminated` alone does not establish this mapping. |
| Disable IIQ login access where applicable | Verify authentication policy and any IIQ login account separately from Oracle locking. |
| Active Directory offboarding integration | Add supported AD account/group operations and independent directory verification in an isolated domain. |
| Existing application session termination | Test target-specific session/token revocation; account locking is not proof existing sessions ended. |
| Automated post-offboarding access verification | Read back each required control and reconcile discrepancies before declaring completion. Current target checks were manual DBeaver checks. |
| Separate Oracle roles and remaining system privileges where appropriate | Re-read after role revocation to account for automatic privilege changes; test behavior for the installed Oracle/connector release. |
| Jane Doe entitlement recovery | Reconcile the partially provisioned account, define the remaining authorized changes and test a separate recovery path. Completion was not supplied. |

The reconstruction iterates every discovered Oracle Link, but only the named single-account scenarios were reported. It cannot discover uncorrelated orphan accounts that have no Link. It does not delete database users, define retention, close sessions, implement cross-system rollback or establish a least-privilege connector configuration. Broad Oracle roles used in synthetic tests are not a recommended workforce access model.

Next practical lab: **retest the final no-Oracle-account branch** and capture sanitized original workflow/task/target evidence. Production-oriented error handling and result gates should follow without expanding claims about the current tests.
