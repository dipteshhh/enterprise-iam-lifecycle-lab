# Access request and manager approval

**Historical status: Previously Completed, Evidence Pending.** The owner reported Ann Parson approving an access request involving Bill Murray and subsequent Oracle provisioning experiments. The exact original request, approval log and target readback are unavailable. The flow below is an illustrative reconstruction and proposed verification path.

## Objective and requirement

Grant a synthetic workforce identity the approved technical access represented by a business request, with NH-05/NH-09 evidence linking the decision to target enforcement.

```mermaid
sequenceDiagram
    actor Requester
    participant IIQ as IdentityIQ request workflow
    actor Manager as Ann Parson - illustrative approver
    participant Oracle as Oracle lab target
    Requester->>IIQ: Request approved lab access for Bill Murray
    IIQ->>IIQ: Resolve identity, manager, role and policy
    IIQ->>Manager: Approval work item where configured
    alt Manager rejects or required context is invalid
        Manager-->>IIQ: Reject or route for review
        IIQ-->>Requester: No access grant, record outcome
    else Approved
        Manager-->>IIQ: Approve scoped request
        IIQ->>IIQ: Resolve account action and compile required changes
        IIQ->>Oracle: Provision through configured supported path
        Oracle-->>IIQ: Execution result
        IIQ->>Oracle: Independent target readback or reaggregation
        Oracle-->>IIQ: Observed account and role state
        IIQ-->>Requester: Record completion or unresolved failure
    end
```

## Prerequisites, steps and expected behavior

An isolated Oracle target, reviewed connector permissions, stable identity correlation, resolved manager, a narrow synthetic entitlement and an appropriate IIQ request workflow are prerequisites. Inspect whether the role requires or merely permits its associated IT Role; permission to request an optional role is not an automatic grant.

Request one scoped entitlement, record the request reference, inspect approver resolution, then approve or reject through the intended configured workflow. Inspect the compiled account/attribute operations and final connector outcome. Query the database independently and reconcile the resulting account. An approval or a queued request alone must not be recorded as completed provisioning.

## Actual results, troubleshooting and limitations

No runtime test was conducted here. Verify manager resolution, work-item ownership, entitlement requestability, provisioning policy fields, connector status, Oracle account/native identity and identity refresh if expected access is missing. The historical `DBA Business → DBA IT → DBA` experiment is documented in [role modeling](../sailpoint-identityiq/roles-and-entitlements/README.md); use a narrow custom lab role for future tests.

## Security and next improvement

Do not bypass approvals with a direct executor solely to make a demonstration succeed. Log decisions without full credential-bearing plans. Test a rejected request, unresolved manager and failed connector operation alongside the approved request; see [test scenarios](test-scenarios.md).
