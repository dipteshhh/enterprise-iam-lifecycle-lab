# Interview preparation grounded in this lab

**Status: Conceptual study material.** Describe the repository as an independently developed educational lab. The author is developing IAM engineering skills; this material is not a claim of production administration, senior architecture experience, or certification.

## An honest project introduction

"I independently built a SailPoint IdentityIQ lifecycle lab for fictional Northstar Health using synthetic employee data. My Joiner work covers Oracle provisioning, and my Leaver workflow responds to an authoritative HR status change to lock Oracle accounts, remove Business Roles and revoke remaining database roles and system privileges. I investigated partial provisioning and stale account information, used the connector API for current account reads and checked target changes through DBeaver. Mover, broader application offboarding and automated failure/recovery controls are future work."

This introduction reflects the owner's [November 26 reported outcomes](../docs/evidence/leaver-2026-11-26.md). Distinguish them from the earlier [captured scoped Create/Modify evidence](../docs/evidence/oracle-create-modify-2026-11-20.md). Explain Mary's outstanding final no-account regression and that the published Leaver XML/BeanShell is reconstructed, not an original export. Keep claims aligned with the [implementation tracker](../docs/implementation-status.md).

## Questions to answer with concrete evidence

| Question | Explain | Evidence to collect or reference |
|---|---|---|
| How does HR become an identity? | Schema → aggregation → mapping/correlation → Identity Cube/refresh | Synthetic source row, schema/mapping and task result |
| Why did duplicate identities appear? | Multiple authorities, correlation key and exact tested behavior | Employee 401 fixture plus sanitized before/after identities; no claim of universal duplicate resolution |
| How is a manager related to an identity? | Manager source value, lookup/correlation and missing-manager handling | Ann/Bob relationship and resulting identity reference |
| What does a successful connection test prove? | Reachability/authentication for tested operation, not full provisioning | Separate test-connection result from target-side create/grant checks |
| What is the RBAC hierarchy? | Business role, IT role, technical entitlement and assignment versus detection | Reported DBA hierarchy with privileges and limitations explicitly discussed |
| What happens after approval? | Plan evaluation, connector execution, possible failure, reconciliation | Approval record, result and independent target readback |
| What does an IIQ Link represent? | An application account associated with an identity | Sanitized link attributes and account native identity |
| How do you choose Create versus Modify? | Zero/one/multiple matching links; required create attributes; ambiguity handling | WIP design and tests, not an unsupported claim of ordered same-plan operations |
| Why are identity attributes empty? | Source schema, account values, mapping and refresh are separate stages | The MySQL employeeID-only symptom and recorded mapping diagnosis |
| Why choose a rule? | Evaluate out-of-box options first; customize only justified gaps | Rule purpose, inputs, null handling, version assumptions and test results |
| How do OAuth, OIDC and SCIM differ? | API authorization, authentication and provisioning | [Protocol flows](../iam-fundamentals/protocols.md); future tests labelled Planned |
| How do you prove offboarding worked? | Disablement, entitlement removal, sessions and target reconciliation are separate | [Alex, Sarah and John outcomes and Mary's coverage gap](../labs/leaver/test-scenarios.md); no claim that locking ends all sessions |
| Why read the connector after removing a Business Role? | A stored Link may still contain revoked values; live ResourceObject retrieval and persisted reconciliation differ | Sarah's stale five-role view and the [remaining-access builder](../labs/leaver/implementation.md) |
| Can a failed request still create an account? | Account Create and entitlement changes can be partially applied | [Jane/John case study](../labs/leaver/troubleshooting.md); Jane's entitlement recovery remains future work |
| How does IAM support healthcare security? | Least privilege, accountable approval, review and evidence | [Governance mapping](../identity-governance/README.md); no HIPAA compliance claim |

## Prepare one troubleshooting narrative

Use situation → expected behavior → observation → hypotheses → test → actual result → limitation. For example, the reported JDBC aggregation initially produced employeeID-only Identity Cubes. Explain how you would inspect raw account attributes, identity mappings and refresh behavior. State which configuration/result artifacts are available and which need to be reproduced.

Avoid invented quantitative improvements, fake terminal results and hypothetical success stories. A useful answer can end with an unresolved connector-specific question and a precise validation plan.

## Next evidence-backed portfolio story

Use the Leaver's conditional workflow, Sarah's role-based removal and John's direct-grant cleanup as the current reported engineering story. Retain original sanitized source and target readback when available, then retest the final no-account branch. Continue ambiguous-account, denied-request, permission-failure and recovery exercises separately. Explain which outcomes have captured evidence and which are currently owner-reported; repository syntax checks do not establish runtime success.
