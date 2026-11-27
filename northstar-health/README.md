# Northstar Health business scenario

Northstar Health is a fictional healthcare organization connecting these exercises. The business requirements below are a model; Joiner is implemented/tested and Leaver primary scenarios are tested as reported in the November 26 update. Mover remains planned. [Joiner](../labs/joiner/README.md) · [Leaver](../labs/leaver/README.md) · [Evidence limits](../docs/evidence/leaver-2026-11-26.md). The lab uses synthetic workforce records only, with no patients, actual healthcare integration or compliance certification.

Employees, contractors, clinicians, IT staff, administrators and external partners need appropriate access as their relationship to the organization changes. HR owns employment facts. Governance connects business decisions to directory/application permissions; authentication is handled by directories and identity providers rather than inferred from governance approval.

## Business requirements

| ID | Requirement | Practical acceptance criterion |
|---|---|---|
| NH-01 | One workforce identity per stable employee key | Reaggregation does not create another Identity Cube; conflicting sources are reviewed |
| NH-02 | Reliable manager relationship | Bob Fields resolves to Ann Parson; missing/ambiguous managers do not cause an arbitrary approval routing choice |
| NH-03 | Pre-hire readiness without early sign-in | Sarah Miller's proposed account is disabled before start; explicit activation evidence is required |
| NH-04 | Unique organizational usernames | First initial plus surname proposal `smiller`; collision, rename, rehire and character-policy handling tested before reservation |
| NH-05 | Governed database access | Approved, least-privilege entitlement is visible on Oracle and in reconciled IIQ evidence |
| NH-06 | Conditional account handling | Existing-account Modify and absent-account Create branches tested independently; multiple accounts require explicit selection/policy |
| NH-07 | Mover access does not accumulate indefinitely | Required additions and obsolete removals are reviewed and verified, including shared-entitlement dependencies |
| NH-08 | Timely exit control | Disablement and applicable session/access revocation are independently observed with failures escalated |
| NH-09 | Explainable audit trail | One evidence record connects source event, decision, approval, request, target readback and reconciliation |
| NH-10 | Separation of duties | A synthetic toxic combination is detected and routed according to defined policy before granting access |

`DBA Business → DBA IT → DBA` records a historical educational experiment, not a recommended ordinary clinical or employee access model. Future exercises should use narrow lab roles instead of granting broad database administration.

## Modules and ownership boundaries

- [Current reported architecture](../docs/architecture/current-lab.md) and [target alternatives](../docs/architecture/target-architecture.md).
- [Joiner, mover and leaver plan](lifecycle-plan.md).
- [Access-request flow](access-request.md) and [test scenarios](test-scenarios.md).

HR supplies lifecycle dates and identifiers; the governance platform evaluates access under policy; directories and applications enforce their account state; the IdP enforces authentication policy. Name changes must not change the stable person key. Directory synchronization and downstream licensing require explicit configuration and do not follow automatically from an IIQ connector test.
