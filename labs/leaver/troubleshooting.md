# Leaver troubleshooting and engineering decisions

These cases combine the owner's November 26 lab narrative with explicitly labeled diagnostic guidance. **Reported observations** are not newly captured runtime evidence. Missing original errors, exports and query results have not been replaced with invented logs or Oracle error codes. [E-005](../../docs/evidence/leaver-2026-11-26.md).

## 1. Missing Oracle role and partial account provisioning

**Problem:** the custom Oracle provisioning workflow was changed to request account creation and roles in the **same Create AccountRequest**. The requested roles were `DBA`, `RESOURCE`, `ANALYST` and `CONNECT`.

**Observed behavior:** Jane Doe's Oracle account was created, but role provisioning failed because `ANALYST` did not exist. The overall request failed even though the database user existed. IIQ initially had no corresponding Link. Oracle Account Aggregation subsequently discovered and correlated that account.

**Root cause:** the missing `ANALYST` role is the owner's established cause for the grant failure. The request was partially applied; this is not evidence that every requested role was granted or that any particular transaction/rollback mechanism ran. Exact connector errors and the specific role subset left behind were not supplied.

**Investigation:** the owner checked actual Oracle account existence separately from request status and IIQ Link presence, then used aggregation to reconcile the account. For a future recovery, inspect every actual grant before deciding which approved changes remain.

**Resolution:** the missing target role was created in the isolated lab:

```sql
CREATE ROLE ANALYST;
```

The same Create-with-roles implementation then succeeded for **John Doe**, as reported. This does **not** prove Jane's entitlements were recovered. Jane's entitlement recovery remains a future exercise; no employee IDs, Oracle native identity for Jane, request IDs or original output were supplied. The SQL above records a reported remediation, not a migration to run automatically, and it is not included in the read-only verification script.

**Lesson:** provisioning operations are not necessarily atomic. A failed overall request does not guarantee rollback of target changes. Investigate connector errors against the target; aggregate/correlate partial accounts before retrying and design recovery separately. Aggregation can repair the account representation without fulfilling the failed access request. The historical [November 21 Create-plus-Modify practice](../../sailpoint-iiq/provisioning/README.md) remains unchanged; its list-ordering limitation is a separate earlier design.

## 2. Stale entitlement information after successful revocation

**Problem:** Sarah's UI/Link view initially still showed five Oracle roles after Business Role removal.

**Observed behavior:** Oracle showed all five grants revoked; IdentityIQ initially retained the old access values. Later Account Aggregation and Identity Refresh reconciled them.

**Root cause:** a difference between target state and the stored IIQ account view was confirmed in the reported test. The precise internal cache/transaction/update mechanism was not supplied; attributing it to a specific cache bug would be a hypothesis.

**Investigation:** compare the exact account's `DBA_ROLE_PRIVS` results with the Link and identity role view rather than immediately repeating a revoke.

**Resolution:** account aggregation followed by identity refresh reconciled the stored view, as reported.

**Lesson:** provisioning and reconciliation are separate. A stale entitlement display does not establish that the target revoke failed.

## 3. Discovering remaining access through the live connector

**Problem:** the initial entitlement snapshot could contain grants removed by the preceding Business Role operation.

**Observed behavior:** Sarah's stale-Link case exposed this risk. The final workflow was improved to retrieve current account data in Build Oracle Entitlement Removal Plan.

**Root cause:** relying on a pre-change snapshot for a post-change decision. The supplied narrative does not establish that a specific redundant-revoke error actually occurred.

**Investigation:** compare Link attributes with `ConnectorFactory.getConnector(app, null)` and `connector.getObject("account", link.getNativeIdentity(), null)` output, then independently verify in Oracle.

**Resolution:** build remaining `ROLES` / `SYSTEM_PRIVILEGES` removals from the returned ResourceObject after the Business Role paths converge.

**Lesson:** a live read improves plan freshness but does not persist a Link update, discover uncorrelated accounts or eliminate races. Connector failure is not an empty-entitlement result.

## 4. Avoiding empty ProvisioningPlan execution

**Problem:** identities can have no Business Roles or no remaining Oracle entitlements.

**Observed behavior:** the final design includes conditional execution guards. No specific runtime error from an empty plan was supplied.

**Root cause:** executing a plan without requested work would add unnecessary subprocess processing. Its exact behavior depends on the local workflow; it is not universally claimed to fail.

**Investigation:** inspect null plans, null request lists, empty request lists and empty AttributeRequest lists separately.

**Resolution:** add a Modify AccountRequest only if it contains AttributeRequests; execute role/entitlement plans only if their AccountRequest list is nonempty. Empty role plans go to live entitlement discovery; empty entitlement plans go to Stop.

**Lesson:** a no-op branch needs an explicit destination, especially when later cleanup still matters. [Exact guards](workflow-design.md).

## 5. Incorrect XML workflow step nesting

**Problem:** incorrect Step nesting was identified and corrected during workflow development, according to the owner.

**Observed behavior:** the malformed original file, exact affected step and error message were not supplied. No specific parser or runtime symptom is invented.

**Root cause:** misplaced Step boundaries/nesting is the reported configuration issue. The original diff is unavailable.

**Investigation:** parse XML, inspect parent-child relationships, count twelve direct `Workflow/Step` elements and resolve every transition target. Well-formed XML alone can still have invalid workflow nesting.

**Resolution:** represent all twelve steps as sibling children of Workflow; keep each Script, WorkflowRef and Transition inside its owning Step. The reconstruction follows this structure.

**Lesson:** XML syntax, workflow structure and executable BeanShell are different validation layers. Repository checks do not establish an IIQ import passed.

## 6. Stopping when no Oracle account exists

**Problem:** an earlier path stopped when no Oracle account was found, preventing later Business Role cleanup.

**Observed behavior:** Mary Jane's original termination event triggered. The final full no-account execution path was **not separately retested** after the final changes.

**Root cause:** Oracle-account existence was being treated as a prerequisite for the entire workflow instead of just Oracle disabling.

**Investigation:** trace `hasOracleAccount = false` through the transition graph and inspect whether Business Role cleanup is reachable.

**Resolution:** skip Execute Disable and continue to Build Business Role Removal Plan. Both Business Role paths then reach Build Oracle Entitlement Removal Plan.

**Lesson:** design coverage and runtime regression coverage are different. Mary's final branch remains a named follow-up test.

## 7. Separating Business Role and direct entitlement removal

**Problem:** role deassignment alone does not address an employee with direct Oracle grants and no IIQ Business Role.

**Observed behavior:** Sarah's Business Role removal revoked its five associated roles. John had no Business Role but had four direct roles plus a direct system privilege; his two direct-grant views were empty after offboarding.

**Root cause:** IIQ role assignments and direct target grants are separate access paths. The actual propagation of role removal depends on role/assignment configuration.

**Investigation:** inventory assigned Bundles, required/detected IT Roles and current Oracle grants for the same subject.

**Resolution:** use separate `roleRemovalPlan` and live `entitlementRemovalPlan` stages, each with its own LCM call and empty-plan guard.

**Lesson:** Sarah establishes this particular role-based path; John establishes the reported direct-grant cleanup. Neither justifies a universal role-removal guarantee.

## 8. Independent database verification

**Problem:** plan generation, UI request success and stored IIQ access can differ from actual target state.

**Observed behavior:** Alex's lock and Sarah/John's access changes were independently checked in DBeaver, as reported. Jane's failed request nevertheless left an Oracle account.

**Root cause:** intent, processing outcome, target state and reconciled IIQ state are separate observations.

**Investigation:** use the correct PDB/service and exact native identity to query `DBA_USERS`, `DBA_ROLE_PRIVS` and `DBA_SYS_PRIVS`. Investigate missing users, SQL errors and case mismatches before interpreting zero rows.

**Resolution:** retain independent readback as the acceptance criterion, then reconcile the IIQ view. The [read-only verification SQL](../../scripts/sql/verify-oracle-offboarding.sql) supports the three supplied Oracle native identities.

**Lesson:** automated result validation and automated post-offboarding access verification remain future work. This repository update did not itself execute those queries.

## 9. Automatic UNLIMITED TABLESPACE changes

**Problem:** certain predefined-role operations can have associated system-privilege effects, complicating a plan based on a single earlier snapshot.

**Observed behavior:** John had `UNLIMITED TABLESPACE`, and both direct-grant views were empty after termination. The supplied evidence does **not** isolate whether that privilege was removed automatically by a role revoke or by an explicit system-privilege request.

**Root cause:** automatic grant/revoke side effects are a **version- and operation-dependent possibility**, not a confirmed explanation for John's result. Oracle's current GRANT reference describes a conditional associated `UNLIMITED TABLESPACE` grant when granting DBA; older Oracle guidance described automatic revoke behavior for DBA/RESOURCE. Do not treat the older rule as universal for this modern Docker target. [Oracle GRANT](https://docs.oracle.com/en/database/oracle/oracle-database/26/sqlrf/GRANT.html), [historical Oracle security guidance](https://docs.oracle.com/cd/A59447_01/nt_804ee/doc/oem.804/a57694/ch_secur.htm).

**Investigation:** in a separate isolated test, record direct system privileges before/after each specific role operation on the actual database release and inspect connector results.

**Resolution:** current cleanup dynamically includes represented system privileges; the final target result was reported empty. Separating role removal from a subsequent remaining-privilege read is a future improvement.

**Lesson:** distinguish direct grants from privileges effective through a role, and measured side effects from assumptions.

## 10. Potential redundant entitlement revocation

**Problem:** role removal may remove a dependent privilege before a later request in the same plan revokes that privilege explicitly.

**Observed behavior:** this is an identified operational possibility. No specific redundant-revoke error, exact Oracle error code or completed retry test was supplied.

**Root cause:** potentially stale state between dependent changes, even when the starting snapshot came from a live connector read. This is a hypothesis to test for the installed connector/database combination.

**Investigation:** inspect individual provisioning-item results and query the target after role removal; determine whether the remaining privilege is still directly granted.

**Resolution:** no completed automatic recovery is claimed. Future design: process roles first, validate results, re-read current system privileges, then request only remaining approved removals.

**Lesson:** a live pre-plan read does not guarantee atomicity or eliminate inter-request dependencies. Readback and partial-failure recovery need their own implementation.
