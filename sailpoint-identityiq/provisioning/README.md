# IdentityIQ provisioning: plan to target verification

**Status:** conceptual reference based on official IIQ documentation. Historical Oracle access provisioning remains **Previously Completed, Evidence Pending**; the [conditional workflow](../workflows/conditional-oracle-provisioning/README.md) remains **In Progress**. An XML plan shape is not an executed provisioning request.

## Objective and business requirement

Represent an approved Northstar Health access change, track its execution, and prove that Oracle reflects the intended result. An approval records authorization; a plan records requested changes; a connector result records processing; a target query records target state. Keep all four forms of evidence distinct.

## Architecture and vocabulary

```mermaid
flowchart LR
    A[Requested access] --> B[Eligibility and approval]
    B --> C[ProvisioningPlan]
    C --> D[Compile and resolve policies]
    D --> E[Application handler or manual action]
    E --> F[Provisioning result]
    F --> G[Target state verification]
    G --> H[Reaggregation and Identity Refresh]
```

This diagram describes a proposed controlled flow, not a trace from the lab. IIQ partitions plans for processing by the configured application handlers. It can use direct connectors, integration configurations, or manual work items; a generic `execute()` call does not replace that configuration. [SailPoint provisioning overview](https://documentation.sailpoint.com/identityiq_83/help/provisioning/provisioningoverview.htm)

| Object or concept | Why it matters |
|---|---|
| `ProvisioningPlan` | Container for the identity's requested changes; composing one is distinct from submitting it through a governed workflow. |
| `AccountRequest` | Identifies the application, account operation such as Create or Modify, and target account identity where required. |
| `AttributeRequest` | Requests one attribute/entitlement change using an operation appropriate to the schema, such as Set, Add, or Remove. |
| Native identity | Connector-specific account key. For an existing account obtain it from its correlated Link; do not substitute the IIQ Identity name or display name. |
| Provisioning policy | Supplies or collects required account-creation attributes and validation. Confirm requirements for the installed connector. |
| Result / transaction / request | Evidence about processing and errors. Accepted, pending, retried, failed, and confirmed outcomes need separate handling. |

## Prerequisites and implementation sequence

Prerequisites: licensed IIQ and known patch level; an isolated Oracle application; confirmed schema; verified correlation; approved least-privilege test entitlement; a requester allowed to request it; an approval route; and a target-side read-only verification account. No prerequisite is established by this repository alone.

1. Resolve the requested identity unambiguously and authorize the requester for that identity and access.
2. Validate application ownership, requestability, SoD, approval requirements, and account-selection policy. Reject unknown entitlement names rather than accepting arbitrary form input.
3. Refresh the account view and check target state. Classify zero/one/multiple matching accounts before choosing Create or Modify.
4. Construct a plan using the exact local application name and schema attributes. For Modify use the existing native identity. For Create resolve all required attributes using the installed provisioning policy.
5. Use the installation's approved workflow and provisioning path. The plan compiler resolves roles, dependencies, policies, and application partitions; do not assume compiling a plan commits target changes. [Compiling the plan](https://documentation.sailpoint.com/identityiq_84/help/provisioning/compiling_the_plan.html)
6. Track the request and connector outcome, including asynchronous/pending work, retries, and manual work items. Do not mark a request complete because a script returned a plan. [Implementing the plan](https://documentation.sailpoint.com/identityiq_84/help/provisioning/implementing_the_plan.html)
7. Independently query the target account and granted role, then reconcile account data and refresh the identity as appropriate. Refresh options can generate additional provisioning, so select them deliberately. Provisioning does not itself recalculate all role detection. [Updating Identity Cube](https://documentation.sailpoint.com/identityiq/8.5/help/provisioning/update_identity_cube.html)

## Code and configuration example

[Illustrative Modify plan](illustrative-modify-plan.xml) shows containment only. `YOUR_...` values must remain placeholders in Git. The entitlement attribute must be discovered from the actual application schema; this example deliberately does not assert that the correct field is `roles` for every Oracle connector/version. There is no Identity reference, approval metadata, request ID, credential, or executor in this fragment.

`plan.add(accountRequest)` adds a request to the plan's request collection; `plan.setAccountRequests(accountRequestList)` replaces that collection with a supplied list. Treat them as different composition choices and check the installed API signatures before use. Neither proves execution, enforces approval, or establishes ordering between requests. Prefer clear construction with one explicit collection rather than mixing both operations and accidentally discarding requests.

## Test procedure and actual results

Expected behavior: one approved operation changes the intended account and entitlement exactly once; rejected/ambiguous input performs no write. A retry after partial success must inspect current target state rather than blindly create a second account.

Tests to perform in the isolated lab:

- Inspect the plan before submission; verify identity, application, native identity, operation, and entitlement against the approval.
- Reject missing identity, stale correlation, two matching accounts, blank native identity, missing required Create attributes, an unapproved role, and approval denial.
- Exercise success, target rejection, temporary connectivity failure, pending work, and partial completion. Record request IDs and sanitized errors.
- Query Oracle for account existence and the exact granted role, reaggregate, refresh selected identity data, and compare the requested and detected state.
- Repeat the same request and confirm the documented idempotency/reconciliation behavior.

Actual results: the XML is a newly authored illustration. No IIQ import, plan compilation, execution, approval, or Oracle query has been performed for it. Local XML parsing, when recorded in repository QA, establishes only well-formedness.

## Security, limitations, and next improvements

Never log full plans that may contain passwords. Avoid DBA as birthright access; use a narrow fictional test role. Keep write permissions confined to the connector service account and isolate destructive experiments. Manual work-item completion is not independent evidence of a changed target.

Exact Java signatures, account-creation fields, role attribute names, retry behavior, transaction boundaries, and supported Oracle Free release remain unverified for the user's installation. This reference is IIQ-specific; ISC APIs and workflows are separate.

Next: capture a sanitized successful standard LCM request before developing custom execution logic; then complete the workflow's zero/one/multiple-account test matrix.
