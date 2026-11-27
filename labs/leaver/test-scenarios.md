# Leaver scenarios and independent verification

**Primary implementation/testing date: November 26, 2026, as reported by the owner.** These are synthetic employees in a fictional organization. The actual-results column records the supplied narrative; no original screenshots, request IDs, logs or SQL exports were provided. No new runtime execution was performed for this repository update. [E-005 provenance](../../docs/evidence/leaver-2026-11-26.md).

## Test matrix

| Scenario / identifiers | Initial conditions | Expected final workflow behavior | Actual reported results | Verification status |
|---|---|---|---|---|
| Mary Jane — `NH-0101`; no Oracle native identity | Active HR account; no Oracle account | Termination event launches workflow; skip Oracle Disable; process Business Role cleanup if needed; build no Oracle entitlement requests and stop | Initial `Active` → `Terminated` lifecycle event triggered successfully | **Initial trigger confirmed by owner; final no-account path not separately retested** after final changes. Role assignments and final cleanup outcomes were not supplied. |
| Alex Jones — `NH-1010`; `Alex_Jones` | Active; existing Oracle account; no Oracle roles, direct system privileges or Business Roles | Generate and execute Disable; skip empty role/entitlement plans; retain locked database user | Event triggered; Oracle account discovered; Disable plan generated; LCM executed; `OPEN` → `LOCKED` | **Account disabling independently verified using DBeaver, as reported.** No original database output supplied. |
| Sarah Miller — `NH-1001`; `Sarah_Miller` | Active; `dba - Business` assigned; required/detected `dba - IT`; five Oracle role entitlements | Lock account; remove Business Role; revoke associated access under this role configuration; reconcile stored access view | Account locked; Business Role removed; IT Role no longer displayed; all five Oracle roles revoked; stale IIQ entitlements found; Account Aggregation and Identity Refresh reconciled the view | **Successful role-based deprovisioning and reconciliation, as reported.** Exact role export and original query captures unavailable. |
| John Doe — employee ID not supplied; `John_Doe` | Active; Oracle account; no assigned IIQ Business Role; four direct Oracle roles and one direct system privilege | Lock account; skip empty Business Role plan; dynamically revoke current `ROLES` and `SYSTEM_PRIVILEGES` | Automated offboarding reported successful; `DBA_ROLE_PRIVS` and `DBA_SYS_PRIVS` each returned zero rows for the account | **Successful direct entitlement deprovisioning independently verified through DBeaver, as reported.** A separate account-status result and employee ID were not supplied. |

Do not turn Mary's initial trigger check into a claim that the final no-account branch passed. Do not infer a specific John account-status readback from the overall successful-offboarding report. The expected behavior is a test criterion, not additional test evidence.

## Sarah Miller: role-based access

Tested hierarchy: **`dba - Business` → required `dba - IT` → five Oracle role entitlements**:

- `ACCHK_READ`
- `ADM_PARALLEL_EXECUTE_TASK`
- `APPLICATION_TRACE_VIEWER`
- `AQ_ADMINISTRATOR_ROLE`
- `AQ_USER_ROLE`

Removing Sarah's Business Role revoked all five role grants in **this lab configuration**. The IT Role no longer appeared in IIQ. This does not prove that removing any Business Role in another environment revokes every shared, independently assigned or retained entitlement. No conclusion about other direct system privileges or all effective database access follows from the five-role result.

Oracle reflected successful revocation before IIQ's stored entitlement view did. Subsequent Oracle Account Aggregation and Identity Refresh reconciled those five values. This observation motivated the live connector read in step 10; that read and a persisted Link update are different operations.

## John Doe: direct access

Before termination, John's directly granted Oracle roles were **`DBA`, `RESOURCE`, `ANALYST`, `CONNECT`**. His additional system privilege was **`UNLIMITED TABLESPACE`**. IdentityIQ's system-privilege entitlement value included its ADMIN_OPTION information; the exact serialized value was not supplied and is not invented here. Removal must preserve the connector-returned value rather than substituting a guessed encoding.

After offboarding, both direct-grant queries returned zero rows. This establishes the absence of directly granted roles and system privileges for that exact account in the queried database container, as reported. It does not establish the absence of PUBLIC grants, object privileges, other accounts, existing sessions or every possible effective access path.

## Reusable Oracle verification

Use [verify-oracle-offboarding.sql](../../scripts/sql/verify-oracle-offboarding.sql) in DBeaver or another SQL client with an independently authorized dictionary-read connection to the intended Oracle service/PDB. It contains separate account/role/system-privilege queries for Alex, Sarah and John, plus an account-preserving count summary. It is read-only and does not grant verifier permissions.

| View | What the check establishes | Interpretation boundary |
|---|---|---|
| `DBA_USERS` | Whether the database user exists and its `ACCOUNT_STATUS` | A retained `LOCKED` user is disabled, not deleted. A missing row must be investigated rather than labeled a successful lock. |
| `DBA_ROLE_PRIVS` filtered by exact `GRANTEE` | Role grants directly attached to that account | Does not enumerate every privilege through role hierarchies or PUBLIC. |
| `DBA_SYS_PRIVS` filtered by exact `GRANTEE` | Direct system-privilege grants and `ADMIN_OPTION` | Does not enumerate object privileges or prove session termination. |

Sources: [Oracle DBA_USERS](https://docs.oracle.com/en/database/oracle/oracle-database/26/refrn/DBA_USERS.html), [DBA_ROLE_PRIVS](https://docs.oracle.com/en/database/oracle/oracle-database/26/refrn/DBA_ROLE_PRIVS.html), [DBA_SYS_PRIVS](https://docs.oracle.com/en/database/oracle/oracle-database/26/refrn/DBA_SYS_PRIVS.html).

Quoted mixed-case Oracle usernames preserve case. For a user created as `"John_Doe"`, use the string literal `'John_Doe'` in a dictionary predicate. An unquoted `John_Doe` identifier is normalized to `JOHN_DOE`. Do not uppercase a Link's native identity or remove case distinctions to make a query match. Diagnostic case-insensitive searches can identify candidates but cannot establish which account was governed. [Oracle identifier rules](https://docs.oracle.com/en/database/oracle/oracle-database/26/sqlrf/Database-Object-Names-and-Qualifiers.html).

## Verification procedure for a future controlled rerun

1. Record the exact synthetic Identity name, correlated Oracle native identity, current employment status and target baseline. Keep missing employee IDs missing until recovered from real lab records.
2. Capture account status and both direct-grant queries before the HR change. Record the correct PDB/service privately.
3. Change the authoritative status, aggregate Northstar Workday HR, and refresh the scoped identity with Process Events enabled and the intended mappings.
4. Inspect lifecycle launch, each generated plan and each LCM provisioning result separately. A generated plan proves requested intent; a successful request screen alone is insufficient target evidence.
5. Independently query Oracle. Confirm account existence/locking and the specific role/privilege outcomes appropriate to that test. Treat SQL errors, wrong case, missing users and wrong containers as unresolved checks.
6. Aggregate Oracle account data and refresh selected identity/role information. Compare target access to the stored Link and Identity Cube. Choose refresh options deliberately to avoid unintended reassignment.
7. Save sanitized original artifacts and update the evidence ledger only for what they establish. Preserve failures, pending results and incomplete regression coverage.

A future Mary's-path regression should cover no Oracle Link with no Business Roles, and no Oracle Link with a removable Business Role. Neither variant was supplied as a completed final regression. Multiple accounts, multiple role assignments, automatic assignment, connector failures and replay safety also remain outside the demonstrated coverage.
