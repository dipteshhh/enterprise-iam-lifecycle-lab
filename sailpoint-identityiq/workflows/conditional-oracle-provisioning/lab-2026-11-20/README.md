# Scoped Oracle Create and Modify lab

**Status: Verified for the bounded account/role exercise.** Independent Oracle readback, targeted IIQ Link reconciliation and the installed request-verification scanner confirmed Create request `0000000014` and Modify request `0000000013` as `Completed/Success`. The [evidence record](../../../../docs/evidence/oracle-create-modify-2026-11-20.md) preserves the failed/no-op first Create attempt and the remaining limitations. The original custom form/workflow remains In Progress; automatic correlation and usable sign-in for the new account were not verified.

## Objective and business requirement

Test two distinct approved Oracle account operations for synthetic Northstar Health identities: create an account that does not exist, and add a narrow role to an existing account. Connect the IIQ request outcome to independent Oracle readback and the reconciled Identity Link.

This exercise tests a scoped connector/request path. It does not establish that the existing custom selection form or every branch of the [conditional workflow design](../README.md) is complete.

## Observed environment and prerequisites

The inspected installation is IIQ **8.3**, build `f4b330b4da3-20220427-175259`, with the running service JVM **17.0.21**. The saved `Oracle Application` uses `sailpoint.connector.OracleDBConnector`, type `Oracle Database - Direct`, and connects to local `FREEPDB1`. Its account identity attribute is `USERNAME`; `ROLES` is a multivalued group entitlement; `SYSTEM_PRIVILEGES` is another entitlement attribute. The saved Create policy requires `USERNAME` and `password`. No before/after provisioning rule or `CorrelationConfig` was configured in the inspected application.

The existing Docker target reports **Oracle AI Database 26ai Free Release 23.26.3.0.0**. A successful connector test demonstrates observed connectivity only. Vendor support for this exact IIQ/JVM/Oracle combination has **not** been established. Do not interpret a working experiment as a supported production configuration.

Prerequisites for the execution stages are the authorized isolated target, exact synthetic-name collision checks, reviewed LCM workflow inputs, protected password generation, deliberate approval ownership, and permission to query the necessary Oracle dictionary views through an already authorized verifier. No new broad dictionary privilege is granted merely to collect evidence.

## Fixture and account authority

| Object | Purpose and initial state |
|---|---|
| `NS_LAB_DATA_OWNER` | Schema-only, no-authentication account, locked; owns the probe table |
| `NS_LAB_DATA_OWNER.NS_LAB_PROBE` | One synthetic row, with no patient or actual workforce information |
| `NS_LAB_REPORT_READER` | SELECT on the probe table only; no grant option, system privileges or nested roles |
| `NS_LAB_MODIFY_01` | Pre-existing target account, initially open, with separate baseline `CREATE SESSION`; requested role absent |
| `NS_LAB_CREATE_01` | Target account absent before the Create request |
| IIQ `NS_LAB_APPROVER` | Synthetic manager and catalog owner with no email; the test requests use `spadmin` as launcher |

Administrative SQL fixture setup is **not** IIQ provisioning. In particular, creating the Modify account directly prepares its precondition and does not count as a successful IIQ Create. The Create account must remain absent until IIQ executes that branch.

Three synthetic IIQ identities were seeded directly for this focused test: the Create subject, Modify subject and approver. The existing Modify account was bound manually to its exact intended identity before targeted aggregation because the inspected application had no `CorrelationConfig`. That manual fixture binding does not verify automatic HR-to-account correlation or an immutable employee-key strategy. The exact role was aggregated into the catalog, marked requestable and assigned to the synthetic approver as owner.

## Request and verification sequence

1. Check for collisions across the fixed synthetic users, role, table and IIQ Identity names. Stop before mutation if an existing object has uncertain ownership.
2. Capture the independent Oracle baseline: PDB, account state, direct roles, direct system/object grants, role nesting and probe-row count. Confirm the Create account is absent and neither subject has the requested role.
3. Seed only the intended synthetic IIQ identities and any explicit fixture binding. Reconcile the existing Modify account with a narrowly targeted read; avoid a full account aggregation that could affect unrelated identities.
4. Build a single Create AccountRequest for `NS_LAB_CREATE_01` and a separate Modify AccountRequest for `NS_LAB_MODIFY_01`. Use the inspected schema and a protected generated password. Do not combine ordered Create-plus-Modify requests in one plan or call a direct provisioning executor to bypass the governed path.
5. Launch installed `LCM Provisioning` with reviewed test notification inputs and a synthetic manager with no email. Verify recipients and actual notification behavior: this run's inputs did not suppress every manager-notification attempt. Record whether a real work item remains pending; a configured approval scheme does not prove an approval occurred.
6. Inspect and explicitly approve only the scoped synthetic work items through the authorized administrative test path. On the installed IIQ 8.3 console, use the reviewed approval-set decision as well as work-item completion: `approve <WORK_ITEM_ID> "test approval comment" approve`. An omitted final `approve` closed the first Create work item without approving its items and produced no target account; preserve that failure as evidence. Record the successful decision as a **console test approval**, not an independent human manager decision or the historical Ann/Bill experiment. Confirm the console contract for another IIQ release before reusing the command.
7. Record the workflow/request processing result without printing complete plans or passwords. Pending, queued and failed states remain distinct from successful target changes.
8. Query Oracle independently after each branch. Require exactly one intended account, the narrow role on the correct account, `ADMIN_OPTION=NO`, and no unintended role/system/object grants attributable to the test.
9. Re-read each target account through the connector and aggregate only that account into IIQ. Verify native identity, intended owner and exact `ROLES` value on its Link. Record any deliberate identity refresh and its options separately. This run refreshed only the two subjects with lifecycle triggers, provisioning and attribute synchronization disabled, then used the installed request-verification scanner only on the two exact requests after checking their identity/application scope; it did not force a verified status.
10. If replay or revocation is exercised, capture its actual result and target/Link state. Reconcile before retry after a timeout or partial result; do not issue another blind Create.
11. Record cleanup explicitly, including whether the role was removed, accounts were disabled or fixtures were retained for inspection. In this run the two approved accounts and role grants were retained for inspection; no revocation or disablement test was performed. Do not claim cleanup from an unexecuted plan.

## Code and configuration

The execution source is newly authored for this exercise and canonical in this lab directory:

| Source | Purpose and execution boundary |
|---|---|
| [runner.bsh](runner.bsh) | Scoped identity fixtures, inspection, reconciliation and governed Create/Modify requests; opt-in mode contract |
| [setup.sql](setup.sql) | Administrative target-fixture preparation; not IIQ provisioning |
| [readback.sql](readback.sql) | Independent dictionary checks for the fixed synthetic scope |
| [catalog-role.bsh](catalog-role.bsh) | Aggregate the exact test role and configure its test ownership/requestability |
| [refresh-subjects.bsh](refresh-subjects.bsh) | Refresh only the two synthetic subjects with target-write/lifecycle options disabled |
| [verify-requests.bsh](verify-requests.bsh) | Scope-check and scan only the two intended request records with the installed verification API |
| [inspect-requests.bsh](inspect-requests.bsh) | Inspect scoped request state without publishing complete plans |
| [outcomes.bsh](outcomes.bsh) | Summarize observed request/workflow outcomes |
| [build_rule.py](build_rule.py) | Build console Rule XML from the new-source scripts for this installed lab |

No vendor workflow XML, licensed library, application credential, generated password or unreviewed raw export belongs in the published lab. The initial application/workflow exports used for inspection remain private authoring material. These sources are version-scoped test utilities, not production-ready provisioning or a portable IIQ installer.

Use the evidence record and repository commit to identify the tested source revision. Script existence, XML well-formedness and a successful connection test alone do not prove provisioning.

The case suffix `Create-02` and request names `0000000013`/`0000000014` belong to this evidence run. A fresh instance will allocate different request names. Inspect its actual request-to-subject/application mapping before adapting `verify-requests.bsh`; its fixed scope checks deliberately refuse mismatches. Do not substitute a broad maintenance scan or force a completion status.

From the repository root, build XML without importing or executing it:

```sh
python3 sailpoint-identityiq/workflows/conditional-oracle-provisioning/lab-2026-11-20/build_rule.py --output-dir local-evidence/oracle-private-build
```

Use a fresh output directory. The builder creates six Rule documents and six argument Maps with the console's required DOCTYPE. In an authorized IIQ console, import only the reviewed generated Rule needed for the next stage; `runner.xml` defines `NS Lab Oracle Runner 20261120`, and its argument Maps select the six explicit modes listed in the source. Follow the stage order above and inspect live work-item ownership, type and exact requested access before completing anything.

## Expected outcomes and test procedure

| Case | Expected outcome | Required independent evidence |
|---|---|---|
| Create | One new `NS_LAB_CREATE_01` account receives the approved narrow role | Before absence, request/approval result, Oracle account/role readback, reconciled Link |
| Modify | Existing `NS_LAB_MODIFY_01` receives the role without an extra account | Baseline role absence, request/approval result, target role grant and unchanged account count, reconciled Link |
| Duplicate guards | Repeated Create is refused when the account/Link already exists; repeated Modify is refused when the role is present | Both refusals observed; no new request beyond 12/13/14; final account count remained one each. This is not a concurrency guarantee |
| Revocation, if run | The role is absent after the governed removal and reconciliation | Removal result, Oracle absence and post-aggregation Link |

Additional missing-data, multiple-account, stale-Link, denied-request, concurrent-request and connector-failure tests remain unverified unless separately recorded. Dictionary privilege checks establish the requested role's grant scope; they do not prove every effective permission available through PUBLIC or the entire database configuration has been audited.

## Actual results and troubleshooting

Observed preflight and subsequent results belong in the [evidence record](../../../../docs/evidence/oracle-create-modify-2026-11-20.md). The initial Create case `NSLAB-Oracle-Create-01` closed with no account created after the work item was finished without an approved item set. The corrected Modify case completed its provisioning item, and a fresh Create retry passed the required policy-form review and synthetic-manager item approval. Independent readback then found exactly one account per subject and the intended role on both accounts, with no admin option.

Targeted post-write reconciliation confirmed both accounts were open, each subject had one correctly owned Link, and the exact test role was present on the target and Link. Requests initially remained `Verifying/Pending` after refresh. A scope-checked call to the installed `IdentityRequestProvisioningScanner.scan(request)` for requests `0000000013` and `0000000014` then yielded `Completed/Success`, with item provisioning state `Finished` and zero item errors. No forced finalization/status method was used.

The Create workflows' Warning results were limited to `Warn:notification_failed_no_email`: the synthetic manager had no email address, and the manager-notification attempts could not dispatch. No email was sent. The Modify workflow TaskResult was Success with no messages. The first Create no-op was caused by the missing item approval, not this notification warning. A workflow warning, a request-verification result, target grants and login ability are distinct observations.

Both runtime duplicate guards were then exercised: Create refused an already existing target/Link, and Modify refused a regrant when the role was already present. No new request was created; the observed requests remained 12, 13 and 14. Final independent readback at `2026-11-21T04:36:05.835484+00:00` still showed exactly one target account per subject, both approved role grants with no admin option, the unchanged narrow role and the one synthetic probe row. These sequential guard tests do not establish race-free or concurrent execution.

The new Create account had **no `CREATE SESSION` grant** in the observed dictionary readback. Account creation and role assignment are established; usable database login is not. This exercise does not add an unapproved system privilege to make sign-in work. The pre-existing Modify account retained its separately prepared baseline `CREATE SESSION` grant.

| Issue observed | Correction and verified boundary |
|---|---|
| Console variable-map parsing | Mode-input XML Maps needed `DOCTYPE Map`; corrected files reached the runner |
| Missing Oracle account lookup | The connector throws `ObjectNotFoundException`; catch that exact absent-object result only, allowing other connector failures to propagate |
| Workflow reference initially produced undefined launch with no case | Using `WorkflowLaunch.setWorkflow(workflow)` rather than the attempted ID reference produced the named LCM cases; readback showed no target writes from the failed launch |
| Create flow pauses before manager approval | The installed provisioning-policy form requires review even when required values are populated; do not skip this review or claim a provisioning failure/success |
| First Create request closed without creating an account | Console work-item completion without the final approval-set decision resulted in an empty item set; use the installed `approve` contract and verify the target independently |
| Create account exists but has no login privilege | The role-based Create path did not yield `CREATE SESSION` in this run; do not claim a usable sign-in or add a new privilege outside the approved test scope |
| Requests remain Verifying after targeted refresh | After confirming target and Link state, the installed verification scanner naturally completed only the two exact requests; no direct forced status/finalization was used |
| Create workflow emits a no-email Warning | The synthetic manager had no email; a manager-notification attempt failed without dispatch. Test notification settings did not suppress that attempt, so record the warning rather than presenting the workflow as message-free |

An absent Link is not proof of an absent target account; query Oracle before deciding Create. A role-grant result is separate from login permission: inspect `CREATE SESSION` rather than assuming all connector Create paths add it automatically. If an approval is skipped or automatically satisfied, document that behavior instead of claiming a work-item decision.

## Security, limitations and next improvements

Limit mutations to the fixed synthetic objects. Generate passwords without publishing plaintext values, use reviewed notification inputs and verify no-email synthetic recipients, and keep full plans and sensitive logs private. Do not assume those inputs prevent every notification attempt. The connector service account's existing broad privileges are not validated as a least-privilege configuration by this test; the **requested role** is deliberately narrow.

The original custom workflow compared unchanged. Application schemas, provisioning forms and correlation settings also compared unchanged; aggregation updated tracking timestamps and the stored credential representation. A private comparison confirmed the effective connector credential remained identical, without publishing either representation. Nine console Rules created in this session, including the cleanup helper, were removed; an exact-prefix listing confirmed none remained. The approved accounts, role, table, identities and request/audit records were retained.

The original custom form, automatic correlation, original historical requests, supported-version matrix, concurrency, revocation and broader failure branches remain outside this test's proven scope. The next implementation is to connect the validated account decisions to the existing custom workflow and add denied/missing-data/ambiguous-account cases. A login-readiness exercise requires its own approved privilege scope and authentication test.
