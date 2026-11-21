# IAM foundations

**Status: Conceptual.** These notes explain the lab's design vocabulary. They are not evidence that each control has been configured. Use the [protocol guide](protocols.md), [glossary](glossary.md), and [governance module](../identity-governance/README.md) for the next level of detail.

## Responsibilities in an identity system

| Component | Responsibility | Northstar example |
|---|---|---|
| HR authority | Workforce facts and employment dates | Synthetic CSV standing in for an HR system, not a real Workday integration |
| Governance platform | Correlate identities, model access, approve/review changes, retain evidence | Current IIQ lab; ISC as a future alternative |
| Directory | Store and administer accounts and groups | Future AD DS domain; Entra cloud directory |
| Identity provider (IdP) | Authenticate the person and issue trusted assertions/tokens | Future Entra SSO exercise |
| Service provider (SP)/relying party | Consume authentication and enforce application access | Fictional Northstar application |
| Provisioning connector/service | Change accounts and access on a target | Reported Oracle provisioning experiment |
| Privileged access tooling | Constrain powerful credentials, sessions and activation | Future PAM/PIM exercises |

IAM spans identity administration and access. IGA concentrates on who should have access, who approved it, and whether it remains appropriate. An IdP sign-in succeeds only as an authentication event; the application still needs authorization rules. A governance platform can approve access without acting as the user's sign-in IdP.

## Lifecycle and identifiers

An identity models a person or non-human subject; an account is its representation on a particular system. One person can have several accounts. Employee ID, IIQ object ID, IIQ identity name, account native identity, UPN, and display name have different purposes. Choose stable correlation identifiers and explicitly handle missing or duplicate values.

Account aggregation reads target accounts into the governance system. Identity aggregation is often used informally for building/updating the consolidated identity view; in IIQ, document the actual account aggregation and identity refresh tasks rather than implying a universal task named "identity aggregation." Provisioning writes a requested change to a target. Account creation and entitlement assignment can succeed or fail independently.

Joiner, mover and leaver controls should each define trigger, eligibility, approvals, target actions, retries, reconciliation, and evidence. Do not infer completed deprovisioning from an HR status change or from an approved request. A target read and, where relevant, a denied-login test establish different parts of the result.

## Authentication, proofing, and credentials

Identity proofing establishes confidence in who a person is. Authentication demonstrates control of an authenticator bound to an account. Authorization decides what a subject may do in a context. NIST SP 800-63 Revision 4, finalized in July 2025, separates proofing, authentication, and federation assurance. [NIST SP 800-63-4](https://pages.nist.gov/800-63-4/)

- Passwords need protected enrollment, storage, reset and recovery paths. A password reset can become an account takeover path if recovery is weak.
- MFA uses distinct factor types; entering two passwords is not two-factor authentication. A specific passkey deployment's assurance depends on authenticator properties, user verification, recovery and policy, not the label "passwordless."
- FIDO2 combines WebAuthn with authenticator communication standards. Passkeys are public-key credentials; phishing resistance depends on the protocol's relying-party binding and correct implementation.
- Adaptive authentication changes requirements based on context or risk. Entra Conditional Access is a policy capability, not a protocol and not proof that every sign-in requires MFA.
- Credential lifecycle includes enrollment, binding, use, rotation where appropriate, revocation, recovery, and destruction. Non-human credentials need owners and expiry review too.

Use the normative [NIST authentication guidance](https://pages.nist.gov/800-63-4/sp800-63b.html) and [WebAuthn specification](https://www.w3.org/TR/webauthn-2/) when designing actual tests. No authentication assurance level is claimed for this lab.

## Access-control models

| Model | Decision basis | Example and implementation caution |
|---|---|---|
| RBAC: Role-Based Access Control | Job/technical roles | A reviewed Northstar DBA role bundles access; prevent broad automatic privilege based solely on a job-title string |
| ABAC: Attribute-Based Access Control | Subject, resource, action, environment attributes | A clinician may view a record only under an approved care relationship; attribute quality and policy evaluation are required |
| PBAC: Policy-Based Access Control | Explicit policy evaluation | An umbrella design term whose exact meaning varies; record the actual policy engine and inputs |
| DAC: Discretionary Access Control | Resource owner discretion | A file owner grants access, within platform constraints |
| MAC: Mandatory Access Control | Centrally enforced labels/classifications | A label/clearance policy constrains access beyond ordinary owner discretion |

RBAC and ABAC can coexist: a role establishes eligibility while an attribute/context policy constrains a particular action. A role assignment rule evaluated during identity processing is not automatically a live application authorization decision. [NIST ABAC guide](https://csrc.nist.gov/pubs/sp/800/162/upd2/final)

## Frequently confused pairs

| Pair | Practical distinction |
|---|---|
| SSO / MFA | SSO reuses a sign-in across applications; MFA strengthens authentication. They can be used together. |
| OAuth / OIDC | OAuth delegates API access; OIDC adds authentication semantics and ID tokens. |
| SAML / OIDC | Both support federation; SAML commonly uses XML assertions, OIDC uses OAuth-based flows and ID tokens. |
| OAuth / SCIM | OAuth can authorize a client's API access; SCIM defines identity-resource provisioning operations. |
| JWT / access token | JWT is a representation format. Not every access token is JWT; an ID token is not an API access token. |
| PAM / PIM | PAM is the broader privileged access discipline; Microsoft PIM is a product capability for privileged eligibility/activation and governance. |
| IIQ / ISC | Different deployment models and customization APIs; do not transplant IIQ Java/BeanShell code into cloud APIs. |
| AD DS / Entra ID | Domain services and cloud identity service; connecting one does not automatically configure the other. |
| Account / entitlement provisioning | Create or update an account versus grant/revoke access on that account; verify both. |

Protocol details and authoritative sources appear in the [protocol guide](protocols.md). Platform distinctions are expanded in the [ISC](../sailpoint-isc/README.md), [AD](../active-directory/README.md), and [Entra](../microsoft-entra-id/README.md) modules.

## Session and token validation

An application must validate tokens/assertions using the chosen protocol and trusted issuer configuration. Check signature, allowed algorithm, audience, issuer, time constraints and flow-specific bindings such as nonce or request correlation. Decoding a JWT is not validation. Never log bearer tokens or publish browser captures containing session cookies.

Disabling an account, revoking a refresh token, and terminating an application's session have different effects. Test the relevant resource and token/session lifetime rather than promising instant universal logout. [OIDC validation rules](https://openid.net/specs/openid-connect-core-1_0.html), [JWT security guidance](https://www.rfc-editor.org/rfc/rfc8725.html)

## Zero Trust study scope

Zero Trust removes implicit trust based only on network location or ownership and uses resource-focused access decisions. It is an architectural approach rather than a badge acquired by deploying MFA. A future Northstar exercise should connect authoritative identity, least privilege, device/context policy, monitoring, and revocation evidence. [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final)

**Next study exercise:** trace one synthetic employee from HR record to account to entitlement to sign-in, and identify which component owns each decision. Keep conceptual explanations separate from actual test outcomes.
