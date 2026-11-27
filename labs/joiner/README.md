# Northstar Health Joiner Lab

**Implemented and tested, as reported by the owner in the November 26, 2026 project update.** This is the current owner-reported lifecycle status. An original complete Joiner export and new end-to-end Joiner test evidence were not supplied with that update, so this page does not reconstruct an undocumented full Joiner workflow or invent new outcomes.

Earlier work is preserved at its original paths:

- [Authoritative HR CSV](../../sailpoint-identityiq/applications/hr-csv/README.md), [account aggregation](../../sailpoint-identityiq/identity-aggregation/README.md) and [identity correlation](../../sailpoint-identityiq/identity-correlation/README.md).
- [Original conditional Oracle provisioning design](../../sailpoint-identityiq/workflows/conditional-oracle-provisioning/README.md), with its historical form-integration limitations retained.
- [Verified scoped Oracle Create/Modify lab](../../sailpoint-identityiq/workflows/conditional-oracle-provisioning/lab-2026-11-20/README.md), including source, approval handling, duplicate guards and [actual captured runtime evidence](../../docs/evidence/oracle-create-modify-2026-11-20.md).
- [November 21 plan-construction practice](../../sailpoint-iiq/provisioning/README.md), preserving the original reconstructed Create-plus-Modify plan and its ordering limitations.
- [Pre-hire and activation design](../../northstar-health/lifecycle-plan.md): broader pre-hire/Entra/licensing steps remain planned unless separately evidenced.

The November 26 failure/recovery narrative adds a later change to the custom Oracle provisioning implementation: roles were placed on the **same Create AccountRequest**. Jane Doe's account was created before a missing `ANALYST` role caused failure; after the missing role was created, John Doe's provisioning succeeded. This is documented in the [Leaver troubleshooting case study](../leaver/troubleshooting.md). The original revised Create script was not supplied and the earlier plan-construction source has not been silently rewritten.

The earlier scoped Create test's missing `CREATE SESSION` and original form-integration gaps remain valid historical observations about that test. They are not silently resolved by the current high-level Joiner status. [Current status register](../../docs/implementation-status.md) and [November 26 provenance](../../docs/evidence/leaver-2026-11-26.md) distinguish the two evidence scopes.
