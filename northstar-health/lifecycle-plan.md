# Joiner, mover and leaver implementation plan

**Status: In Progress for joiner study/design; Planned for practical mover/leaver automation.** All flows below are proposed. No complete lifecycle has been executed or verified for this repository.

## Objective, business requirement and prerequisites

Implement NH-01 through NH-09 from the [business scenario](README.md), beginning with one synthetic person and one target. Required: a verified authoritative HR mapping, unique stable key, resolved manager, target connector permissions, defined approval policy and an isolated rollback baseline. AD/hybrid steps additionally need supported domain and synchronization infrastructure; they are not prerequisites for a first direct Oracle experiment.

## Joiner and pre-hire

```mermaid
flowchart TD
    HR["HR records synthetic hire"] --> AGG["Aggregate and correlate unique employee key"]
    AGG --> VALID{"Required attributes and manager valid?"}
    VALID -->|"no"| HOLD["Hold for review"]
    VALID -->|"yes"| ROLE["Evaluate approved birthright access"]
    ROLE --> ID["Reserve collision-checked username"]
    ID --> PRE["Create disabled pre-hire account where supported"]
    PRE --> DATE{"Authoritative active status and start date reached?"}
    DATE -->|"no"| WAIT["Remain disabled and monitor changes"]
    DATE -->|"yes"| ENABLE["Activate through validated connector operation"]
    ENABLE --> ACCESS["Assign approved groups, applications and optional licensing"]
    ACCESS --> VERIFY["Verify target state and reconcile identity"]
```

Sarah Miller's `smiller` is a proposed base name, not a unique reservation or confirmed provisioned account. Define the timezone, start-of-day activation policy, future HR corrections and cancellation behavior before scheduling. Creating a disabled account does not prove all application/session paths are blocked; test applicable enforcement. Licensing needs product eligibility, required usage-location data and a chosen assignment method, not a presumed universal group operation.

## Mover

```mermaid
flowchart TD
    HR["HR changes department, title or manager"] --> DIFF["Compare authoritative before and after state"]
    DIFF --> EVAL["Evaluate new roles, SoD and shared access dependencies"]
    EVAL --> APPROVE["Route approval where policy requires"]
    APPROVE --> ADD["Provision approved new access"]
    ADD --> REMOVE["Remove obsolete access according to policy"]
    REMOVE --> VERIFY["Verify additions and removals in each target"]
    VERIFY --> RECON["Refresh identity and record exceptions"]
```

Order additions and removals according to risk and continuity requirements; the depicted sequence is an example, not a guaranteed transactional change. A role no longer matching a title does not by itself prove all obsolete direct grants were revoked. Check competing roles and manually assigned access before removal.

## Leaver

```mermaid
flowchart TD
    HR["Authoritative termination or emergency event"] --> VALIDATE["Validate subject, effective time and authorized trigger"]
    VALIDATE --> DISABLE["Disable relevant accounts with priority policy"]
    DISABLE --> REVOKE["Revoke applicable sessions and tokens where supported"]
    REVOKE --> ACCESS["Remove access, groups and reclaim eligible licenses"]
    ACCESS --> RETAIN["Apply retention or deletion policy"]
    RETAIN --> VERIFY["Read back target state and reconcile"]
    VERIFY --> EXCEPTION{"Any target failed or remained accessible?"}
    EXCEPTION -->|"yes"| ESCALATE["Escalate and track remediation"]
    EXCEPTION -->|"no"| CLOSE["Close with evidence"]
```

Disablement, session revocation, entitlement removal and deletion are different operations. Token/session behavior is target-dependent; do not claim immediate universal logout. Emergency termination requires a defined authorized escalation path independent of routine HR batch latency. Retention and deletion require an approved policy; a teaching diagram does not define one.

## Implementation sequence and verification

1. Baseline the installed platform and capture an HR aggregation/correlation replay.
2. Test the conditional Oracle workflow with a narrow synthetic role before using broad entitlements.
3. Implement one joiner path with documented preconditions; capture source event, decisions, request, target readback and reconciliation.
4. Add pre-hire activation and cancellation, missing manager, duplicate key and username collision tests.
5. Implement mover additions/removals and verify shared-role dependencies.
6. Implement leaver disablement first, then target-specific session/access removal and retention, including failure escalation.

Expected behavior is defined in [test scenarios](test-scenarios.md). Actual results: not run. There is no importable lifecycle configuration here. Avoid duplicate event handling with persistent request keys and readback before retry; serialize conflicting changes for a person and record partial target failures rather than pretending cross-system rollback is atomic.

## Additional planned scenarios

| Scenario | Control to design before testing |
|---|---|
| Rehire | Match stable key, inspect retained accounts and reapprove access rather than restoring everything |
| Contractor onboarding and extension | Sponsor, end date, renewal approval and automatic expiry |
| Temporary access | Explicit purpose, approver, expiry and verified removal |
| Leave of absence | Suspend/reactivate policy distinct from termination |
| Internal promotion/department transfer/manager change | Attribute ownership, role recalculation and approval rerouting |
| Employee-to-contractor conversion | Relationship transition, authoritative-source precedence and access reset |
| Orphan account remediation | Owner investigation and authorization before disable/delete |
| Dormant accounts | Reliable activity evidence, exclusions and approved remediation |
| Service accounts | Named owner, purpose, credential rotation, noninteractive use and retirement criteria |

Security: use synthetic identities, least-privilege connectors and reviewed logs. Limitations: exact IIQ version, connector schema, lifecycle event configuration and downstream permissions are unverified. Next improvement: complete the two conditional Oracle branches and collect evidence before expanding to AD or cloud activation.
