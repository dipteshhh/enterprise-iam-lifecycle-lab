# Oracle provisioning plan practice

**Date: 2026-11-21.** A focused BeanShell learning exercise: inspect an identity's Oracle account Links and construct the appropriate requests. [The script](oracle-create-modify-plan.bsh) is a sanitized reconstruction of the exercise, not an original IIQ export or an executing workflow.

| Completion label | Exact scope |
|---|---|
| **Completed: ProvisioningPlan Construction** | This exercise builds one Modify request for an existing account, or separate Create and Modify requests for a missing-account candidate. |
| **Completed: Provisioning Execution and Workflow Integration** | The **earlier, separate standard-LCM exercise** verified scoped Create/Modify execution and reconciliation on 2026-11-20. [Actual evidence](../../docs/evidence/oracle-create-modify-2026-11-20.md). It does not verify execution of this new combined-request script; the original custom-form integration remains In Progress. |

## Inputs and execution context

Use a licensed, isolated IdentityIQ lab and an authorized script/rule context that supplies `context`. Supply `identityName`, `applicationName`, `requestedRoles` (a Java List of approved synthetic role names), and `newAccountName` for the missing-account branch. Names must match the lab objects. The script returns a `ProvisioningPlan` and performs only IIQ object reads.

This example uses the previously inspected Oracle schema's `USERNAME` identity attribute and `ROLES` entitlement attribute. Check the actual connector/version/schema before adapting it. It rejects missing objects, empty role lists, malformed role values, multiple matching Links and a blank existing native identity. Repeated role names are included only once.

## Scenario 1 — Existing Oracle account

Loop through the identity's Links and find exactly one for the Oracle application. Read its `nativeIdentity` and account instance. Construct **Modify only**, adding one `ROLES` Add AttributeRequest for each requested role. The existing account key comes from the Link, rather than the employee's display name or IIQ internal ID.

## Scenario 2 — Missing Oracle account

When no Oracle Link matches, construct a **Create** AccountRequest containing the proposed `USERNAME`, followed by a separate **Modify** AccountRequest for role additions. Both requests refer to the proposed new account name and are added to the same plan. This models the learning requirement; it does not establish that the target account is actually absent.

## Concepts learned

| Concept | Role in the exercise |
|---|---|
| `ProvisioningPlan` | Holds the identity and requested account changes. |
| `AccountRequest` | Describes an application's Create or Modify operation. |
| `AttributeRequest` | Describes a field/entitlement change: Set `USERNAME` or Add `ROLES`. |
| `Link` | IIQ's account representation used to inspect existing ownership. |
| `nativeIdentity` | Connector account key used to address the existing or proposed account. |
| Java loops | Inspect Links and build role AttributeRequests from a list. |

## Current limitation and verification boundary

The script **constructs requests only**. It does not call an executor, compile a plan, launch a workflow, contact Oracle, obtain approvals or update account Links. List insertion order **does not guarantee CREATE before MODIFY**, an atomic transaction or safe retries. A generated/changed username could also make the proposed Modify target incorrect.

The Create request intentionally contains no password. Its required protected password and any other connector-specific inputs still need a reviewed provisioning policy. Before any future execution, independently check account existence, naming collisions, eligibility, approvals and supported connector behavior. A single Create with supported role attributes, or a separately verified Create followed by Modify, may be more appropriate; neither alternative is implemented here.

Construction checks must inspect request count, operations, native identities and role attributes for both scenarios, plus ambiguous/missing-input cases. Such checks establish the returned plan's shape, not target changes. The earlier execution evidence used a separate governed path and does not prove ordering for this combined plan.

**Verification:** 28 offline construction checks passed using installed IIQ 8.3/BeanShell model classes on JDK 17 with an in-memory context proxy: 16 object lookups and zero forbidden context calls. No console, database, connector or workflow was contacted by these checks.

Use fictional identities and narrow lab roles. No Oracle passwords, credentials, secret-bearing connection strings or real employee records are included. Never add a complete credential-bearing plan or unreviewed application export to this folder.
