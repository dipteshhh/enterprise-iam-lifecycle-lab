# Interview preparation grounded in this lab

**Status: Conceptual study material.** Describe the repository as an independently developed educational lab. The author is developing IAM engineering skills; this material is not a claim of production administration, senior architecture experience, or certification.

## An honest project introduction

"I am building an enterprise identity-security lab around a fictional healthcare organization. My main hands-on platform is local SailPoint IdentityIQ. My lab history includes CSV and JDBC aggregation, identity mapping and correlation, Oracle access requests and role experiments, and an Entra connector connectivity test. The repository marks these historical results as evidence pending until I attach sanitized original artifacts. Conditional Oracle provisioning and joiner automation are in progress; AD and ISC exercises are planned."

Adapt that wording only after the [implementation tracker](../docs/implementation-status.md) changes based on inspected evidence. Do not describe illustrative code as an original exported implementation.

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
| How do you prove offboarding worked? | Disablement, entitlement removal, sessions and target reconciliation are separate | Planned positive/negative tests; no claim that one flag instantly revokes every session |
| How does IAM support healthcare security? | Least privilege, accountable approval, review and evidence | [Governance mapping](../identity-governance/README.md); no HIPAA compliance claim |

## Prepare one troubleshooting narrative

Use situation → expected behavior → observation → hypotheses → test → actual result → limitation. For example, the reported JDBC aggregation initially produced employeeID-only Identity Cubes. Explain how you would inspect raw account attributes, identity mappings and refresh behavior. State which configuration/result artifacts are available and which need to be reproduced.

Avoid invented quantitative improvements, fake terminal results and hypothetical success stories. A useful answer can end with an unresolved connector-specific question and a precise validation plan.

## Next evidence-backed portfolio story

Complete the conditional Oracle account lab with two synthetic identities: one already has an account and one does not. Include an ambiguous-account case, denied request, permission failure and successful reconciliation. Explain programming decisions, approval boundaries and connector limits. Promote the capability to Verified only when the required original test evidence has been inspected.
