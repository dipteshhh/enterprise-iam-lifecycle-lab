# IAM glossary

**Status: Conceptual.** This glossary is a study reference; definitions do not imply implementation.

| Term | Meaning and boundary |
|---|---|
| IAM | Identity and Access Management: identity administration, authentication, authorization and related access operations. |
| IGA | Identity Governance and Administration: access policy, identity lifecycle administration, requests, reviews and accountability. |
| IdP | Identity Provider: authenticates subjects and issues assertions/tokens under a trust arrangement. |
| SP | Service Provider: application consuming federation assertions; OIDC commonly calls the client a relying party. |
| SSO | Single Sign-On: access multiple applications using an established authentication session. |
| MFA | Multi-Factor Authentication: authenticate using more than one distinct factor type. |
| 2FA | Two-Factor Authentication: MFA using two distinct factor types. |
| RBAC | Role-Based Access Control: associate permissions with roles and subjects with roles. |
| ABAC | Attribute-Based Access Control: evaluate attributes of subject, resource, action and environment. |
| PBAC | Policy-Based Access Control: explicit policy determines access; define the specific engine/model used. |
| DAC | Discretionary Access Control: an authorized resource owner can grant access under system constraints. |
| MAC | Mandatory Access Control: centrally enforced classification/label policy governs access. |
| PAM | Privileged Access Management: discipline and tooling to limit, monitor and govern powerful access. |
| PIM | Privileged Identity Management: management of privileged identity rights; Microsoft PIM provides eligible/time-bound activation controls for supported resources. |
| CIEM | Cloud Infrastructure Entitlement Management: analyze and manage effective permissions across cloud infrastructure. No CIEM product deployment is claimed here. |
| JIT | Just-in-Time Access: grant/activate access for the required interval rather than standing assignment. |
| JEA | Just Enough Administration: constrain administrative capabilities; Microsoft also uses JEA for its PowerShell delegated-administration technology. |
| Least privilege | Grant only the access needed for an approved purpose and duration. |
| Birthright access | Baseline access driven by approved employment/identity policy, not unlimited automatic access. |
| Separation of Duties (SoD) | Divide incompatible responsibilities to reduce fraud/error; conflicts require policy and accountable review. |
| Toxic access combination | A defined combination enabling a prohibited or high-risk action, such as approving one's own payment. |
| Access review | Decision about whether existing access remains justified. |
| Certification / recertification | Formal access attestation campaign or repeated review; remediation still needs verification. |
| Role mining | Analyze existing access patterns to propose role candidates; historical access is not automatically legitimate. |
| Orphan account | Account without a valid accountable identity/owner under the defined correlation and ownership policy. |
| Dormant account | Account showing no qualifying activity for a defined interval; timestamp quality matters. |
| Service account | Account used by a service or application; requires an owner, purpose, scoped permissions and lifecycle controls. |
| Non-human identity (NHI) | Identity for software, workloads, services, devices or automation rather than a human user. Scope varies by platform. |
| Workload identity | Identity used by software to authenticate and obtain access. |
| Managed identity | Platform-managed workload identity in supported scenarios; permission governance remains necessary. |
| Correlation | Associate an account with its correct identity using configured evidence/rules. |
| Aggregation | Read accounts/entitlements from a source into a governance platform. |
| Provisioning | Apply an intended account/access change to a target, then verify its outcome. |
| Native identity | Connector-specific account identifier used to address a target account; not necessarily a person's display name. |
| Federation | Trust an external issuer's authentication statements rather than maintaining a separate authentication process at every application. |
| Delegated authorization | Allow a client limited resource access on behalf of a user under an authorization grant. |
| Identity proofing | Establish confidence in a person's claimed real-world identity before/while enrollment. |
| Passkey | Public-key credential used in supported passwordless authentication; deployment and recovery properties determine assurance. |
| Zero Trust | Resource-focused architecture without implicit trust solely from network location/ownership. |

For assurance terminology see [NIST SP 800-63-4](https://pages.nist.gov/800-63-4/). For access models see [NIST ABAC guidance](https://csrc.nist.gov/pubs/sp/800/162/upd2/final). Product terms should be confirmed against the [platform modules](README.md).
