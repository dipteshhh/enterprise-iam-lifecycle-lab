# Oracle Create/Modify runtime evidence — 2026-11-20

**Status: Verified for the bounded account/role exercise.** Independent Oracle readback, targeted IIQ Link reconciliation and the installed request-verification scanner confirm the successful Create retry and Modify request. The original custom workflow remains In Progress; automatic correlation and usable sign-in for the new account are not verified. This record preserves the failed/no-op first Create attempt. The test date is local **America/New_York, 2026-11-20**; capture timestamps use UTC explicitly.

## Scope and provenance

The user authorized the selected next lab: test Oracle Create and Modify paths with synthetic identities and a narrow role, then capture target readback and reconciliation evidence. The lab is a newly authored scoped exercise, separate from the owner's historical implementation claims and the original `Oracle Provisioning new` form/workflow.

The existing custom workflow was inspected privately: its plan-creation step and `LCM Provisioning` reference were present; a working Modify branch was not established. No original workflow is declared complete by this evidence record.

After execution, the original custom workflow compared unchanged. Application schemas, provisioning forms and correlation configuration also compared unchanged. Aggregation tracking timestamps and the stored credential representation changed during processing; a private decryption-and-equality check confirmed the effective connector credential was identical. Neither credential representation was published.

## Environment inspected

| Component | Actual observation | Limit |
|---|---|---|
| IIQ installation JAR | Version 8.3, build `f4b330b4da3-20220427-175259` | Does not establish all installed patch/configuration details |
| Running service JVM | JDK 17.0.21, observed through the running Java process | Does not establish vendor support for the combination |
| Local UI endpoint | HTTP 200 at the local IIQ application | HTTP response alone is not a functional-login test |
| Docker | Desktop started; existing `oracle-sailpoint` became running | No new Oracle container/image was deployed for this exercise |
| Oracle target | Local port 1521, PDB `FREEPDB1`, read-write | Other PDBs and targets are outside mutation scope |
| Oracle banner | Oracle AI Database 26ai Free Release 23.26.3.0.0 | Exact IIQ/JVM/database compatibility remains unconfirmed |
| Saved IIQ application | `Oracle Application`, type `Oracle Database - Direct`, `sailpoint.connector.OracleDBConnector` | Existing administrative credentials were not published |
| Connector test | `Test Succeeded.` observed through the IIQ console | Connectivity only, not provisioning or correlation |
| Account schema | `USERNAME` identity; `ROLES` multivalued group entitlement; `SYSTEM_PRIVILEGES` entitlement | Names are observed in this saved application, not universal connector assumptions |
| Create policy | Required `USERNAME` and `password` fields | Does not prove submitted request inputs or execution |
| Application hooks/correlation | No configured before/after provisioning rule or `CorrelationConfig` in inspected export | Does not establish automatic correlation behavior |

Private application/workflow exports were inspected for configuration, not included as public artifacts. No licensed binaries or raw credential-bearing exports are attached.

## Baseline and fixture preparation

Initial collision checks found no `NS_LAB` users, roles or tables and neither target IIQ subject Identity existed. Administrative fixture preparation then created the narrow role and Modify precondition; those operations must not be counted as IIQ provisioning.

Independent target baseline captured at **2026-11-21T04:20:14.660259+00:00**, equivalent to **2026-11-20 23:20:14 America/New_York**:

| Assertion | Observed state |
|---|---|
| Container | `FREEPDB1` |
| Data owner | `NS_LAB_DATA_OWNER`, `LOCKED`, authentication `NONE` |
| Modify subject | `NS_LAB_MODIFY_01`, `OPEN`, authentication `PASSWORD`; exactly one account |
| Create subject | `NS_LAB_CREATE_01` absent |
| Modify baseline system grant | `CREATE SESSION`, `ADMIN_OPTION=NO` |
| Requested role on either subject | Absent |
| Role object grant | `NS_LAB_REPORT_READER`: SELECT on `NS_LAB_DATA_OWNER.NS_LAB_PROBE`, `GRANTABLE=NO` |
| Role system privileges | Count 0 |
| Nested roles | Count 0 |
| Probe table | Exactly one synthetic row |

The Modify account password was generated in memory and not retained or published. The schema-only data owner has no login authentication. The role itself has no login privilege; account login state and role access must be checked separately.

## Execution and actual results

| Stage | Actual result |
|---|---|
| Synthetic IIQ identity seeding | Created `NS_LAB_CREATE_01`, `NS_LAB_MODIFY_01` and `NS_LAB_APPROVER`; no email configured on the synthetic identities |
| Entitlement catalog | Aggregated exact `NS_LAB_REPORT_READER` under `ROLES`, marked it requestable and set its owner to the synthetic approver |
| Existing Modify account binding/targeted aggregation | Manually bound the exact account to the synthetic identity, then targeted aggregation passed: target account present/open; one correctly owned Link; requested role absent on target and Link |
| Create baseline reconciliation | Target account absent; zero Links; no role grant |
| First Create request | Case `NSLAB-Oracle-Create-01`, request `0000000012`: initially paused on policy Form owned by `spadmin`; later closed `Completed/Success` with empty items and a no-email Warning task result, but **no account was created** |
| First Create failure cause | The console command finished the work item without approving its item set because the optional final `approvalSetStatus=approve` argument was omitted; target readback, not the request label, established the no-op |
| Corrected Create request/approval | Fresh retry `NSLAB-Oracle-Create-02`, request `0000000014`, after confirming target absence; policy Form reviewed and synthetic-manager work-item items explicitly approved |
| Create processing result | Four items initially reported provisioning state `Commited` (installed spelling), errors 0; workflow TaskResult `Warning` with one no-email message. After scoped verification, IdentityRequest `Completed/Success`; all item provisioning states `Finished`, error count 0 |
| Create independent target readback | Exactly one `NS_LAB_CREATE_01`, `OPEN`, authentication `PASSWORD`; intended role present, `ADMIN_OPTION=NO`, `DEFAULT_ROLE=YES`; **no `CREATE SESSION` grant observed** |
| Create post-provision Link reconciliation | Target present/open; exactly one Link; owner matched intended synthetic subject; exact test role present on target and Link |
| Modify request and approval | Case `NSLAB-Oracle-Modify-01`, request `0000000013`; synthetic-manager Approval items explicitly approved through the console test path |
| Modify processing result | TaskResult `Success`, 0 messages; Add item ApprovalState `Finished`, initially provisioning state `Commited` (installed spelling), error count 0. After scoped verification, IdentityRequest `Completed/Success`; item provisioning state `Finished`, error count 0 |
| Modify independent target readback | Exactly one existing account remained `OPEN`, gained only the requested role with `ADMIN_OPTION=NO`, `DEFAULT_ROLE=YES`; baseline `CREATE SESSION` unchanged |
| Modify post-provision Link reconciliation | Target present/open; exactly one Link; owner matched intended synthetic subject; exact test role present on target and Link |
| Runtime duplicate guards | Create refused an existing target/Link; Modify refused a regrant when the role was already present; no new requests beyond 12/13/14 and target counts stayed one per subject |
| Role revocation | Not tested in this scope |
| Cleanup/final retained state | Approved synthetic accounts and role grants retained for inspection; no account disablement, object deletion or revocation test was performed |

Independent Oracle readback at **2026-11-21T04:29:08.076876+00:00** (**2026-11-20 23:29:08 America/New_York**) confirmed the target was unchanged by the pending requests: Create account absent; Modify account open with baseline `CREATE SESSION`; no `NS_LAB_REPORT_READER` grant on either subject. The narrow role still had its single SELECT privilege, no system privileges and no nested role.

Automatic approval review initially rejected the attempted console block containing `approve` because completing the work items could create the account or grant access. The user subsequently explicitly approved both exact changes, resolving that execution gate. The completed synthetic work-item item decisions are administrative console test approvals, not independent human manager review or historical Ann/Bill evidence.

Independent post-Modify readback at **2026-11-21T04:31:38.776269+00:00** (**2026-11-20 23:31:38 America/New_York**) established the role grant on the existing Modify account. Independent post-Create-retry readback at **2026-11-21T04:32:58.584286+00:00** (**2026-11-20 23:32:58 America/New_York**) established exactly one account per subject and the intended role on both. The role remained SELECT-only on the one probe table, with `GRANTABLE=NO`, zero system privileges and zero nested roles.

These checks establish target account creation and the exact role assignments. The Create account's missing `CREATE SESSION` is a documented scope limitation; the operator did not add an unapproved system privilege or claim successful user authentication.

## Reconciliation and final request verification

Targeted connector readback and aggregation returned, for both subjects: target exists, account status `OPEN`, Link count 1, Link owner equals the intended synthetic identity, test role present on target and test role present on Link. This is post-write reconciliation evidence; the initial manual Modify binding remains a separate fixture step and does not become automatic correlation evidence.

Only the two synthetic identities were then refreshed with `processTriggers=false`, `provision=false`, `synchronizeAttributes=false` and `refreshProvisioningRequests=true`. The requests initially remained `Verifying`. After validating each request's target identity and application scope, the operator invoked the installed `IdentityRequestProvisioningScanner(context, new Attributes()).scan(request)` **only** for `0000000013` and `0000000014`. No `markVerifiedAndFinalize` or forced-status method was called.

Both scanned requests subsequently reported execution status `Completed`, completion status `Success`, all item provisioning states `Finished`, and zero item errors. Create's aggregate account item had no approval state; its username, password and role items had ApprovalState `Finished`. These are the observed installed API results, not a promise that another release or unattended scanner schedule behaves identically.

Both Create workflow cases had only the Warning message `Warn:notification_failed_no_email`, from attempted notification to the synthetic manager with no email address. No message was sent. Test notification inputs did not suppress those manager-notification attempts. The warning is separate from the first Create no-op caused by an unapproved item set. It is retained even though target readback and verification succeeded for the retry; the Modify workflow TaskResult had Success and zero messages.

## Duplicate guards and final target state

The operator exercised both runtime precondition guards after successful provisioning. The Create mode refused to submit because the account/Link already existed. The Modify mode refused to submit because the role was already present. No new request appeared: the scoped request set remained `0000000012`, `0000000013` and `0000000014`. The runner also checks the completed Create case's TaskResult before allowing resubmission. These are sequential refusal tests, not proof of concurrency safety or an atomic distributed uniqueness guarantee.

Final independent target readback at **2026-11-21T04:36:05.835484+00:00** (**2026-11-20 23:36:05 America/New_York**) confirmed:

- Exactly one `NS_LAB_CREATE_01` and one `NS_LAB_MODIFY_01`, each `OPEN`, authentication `PASSWORD`.
- `NS_LAB_REPORT_READER` on both subjects, `ADMIN_OPTION=NO`, `DEFAULT_ROLE=YES`.
- `CREATE SESSION` remained a baseline grant on the Modify subject only; no such grant was observed for Create.
- Data owner `NS_LAB_DATA_OWNER` remained locked with authentication `NONE`.
- The requested role retained exactly the single probe-table SELECT grant with `GRANTABLE=NO`, zero system privileges and zero nested roles.
- The probe table still had one synthetic row.

The approved accounts, role/table fixture and synthetic IIQ identities were retained for inspection. No real workforce identity or original application/workflow was modified. No generated plaintext password was retained in authoring files or published captures; normal target password storage and IIQ protected secret processing are separate product behavior. Revocation, account disablement and deletion were not tested.

## Troubleshooting observed during execution

| Issue | Actual correction or boundary |
|---|---|
| Mode XML Map did not parse as intended | Added `DOCTYPE Map`; subsequent mode inputs reached the runner |
| Connector lookup for absent account threw an exception | Handle only exact `ObjectNotFoundException` as absence; propagate other connector errors rather than selecting Create blindly |
| Initial workflow ID reference returned undefined with no case | Changed to `WorkflowLaunch.setWorkflow(workflow)`; named LCM cases then launched. Independent readback showed no target writes from the earlier launch |
| Create stopped at policy Form before manager review | Required inputs were populated, including the secret-typed password, but the installed fields required explicit review before the workflow could reach manager approval; this review was completed on the successful retry |
| First Create work item completed without approved items | Initial command omitted the optional approval-set status. Corrected installed syntax was `approve <id> "comment" approve`; the fresh Create retry then produced the target account. The first closed request remains a no-op failure for the intended outcome |
| Create account lacks `CREATE SESSION` | Observed after the role-based Create; sign-in usability was not established and no additional system privilege was added |
| Requests remained Verifying after refresh | Scope-checked installed scanner calls for only requests 13 and 14 naturally yielded `Completed/Success`; no forced verification/status update |
| Create retry workflow Warning | `Warn:notification_failed_no_email`; the synthetic approver had no email, so a notification attempt did not dispatch. This warning did not negate independently observed target and request-verification results |

## Private capture inventory

The operator retained private captures outside the repository, including `01-baseline.private.txt`, `03-reconcile-before.private.txt`, `04-create-pending-approval.private.txt`, `05-both-pending.private.txt`, `07-after-modify.private.txt`, `08-after-create-retry.private.txt` and `09-reconciled.private.txt`. Only sanitized observations are transcribed here. Full workflow/application exports, secret-typed field values and complete credential-bearing plans are not published.

## Published sanitized captures

- [Independent target baseline](oracle-create-modify-2026-11-20/baseline.txt).
- [Independent final target readback](oracle-create-modify-2026-11-20/final-target.txt).
- [IIQ request/workflow outcomes](oracle-create-modify-2026-11-20/iiq-outcomes.txt).
- [Reconciled target/Link observations](oracle-create-modify-2026-11-20/reconciled-links.txt).

These excerpts are limited to the exact synthetic scope. They do not include raw vendor exports, full stack logs, secret-typed values or complete plans.

## Reproduction and evidence boundary

Follow the [scoped runbook](../../sailpoint-identityiq/workflows/conditional-oracle-provisioning/lab-2026-11-20/README.md). Keep canonical new-source scripts with that lab and preserve private raw material outside Git. No generated password, full credential-bearing plan or private tenant/account export should be published.

Directly seeded synthetic IIQ identities and any manual binding are fixture setup, not successful automatic HR aggregation or correlation. A standard LCM request test does not complete the custom workflow's form, transitions, authorization checks or error paths. The evidence can support only the exact operations and cases actually executed.

## Remaining verification

Nine console Rules created during this session were removed after the test, including the cleanup helper. An exact-prefix listing returned no remaining lab console Rules. The approved target fixture, three synthetic identities, entitlement catalog item and request/audit records remain available for inspection. No revocation or account-disablement test is claimed.

Post-write target/Link reconciliation, final verification of requests 13 and 14 and sequential duplicate-guard refusals are established for this exact bounded exercise. Supported-version compatibility, concurrency, full effective-access auditing, revocation, broader negative/failure cases and the original historical Ann/Bill request remain outside the evidence currently recorded here. Any login-readiness exercise needs its own approved privilege scope and authentication test; completing the original custom form/workflow remains a separate implementation task.
