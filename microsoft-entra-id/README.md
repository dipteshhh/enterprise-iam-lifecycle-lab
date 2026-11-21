# Microsoft Entra ID learning and implementation map

**This module: Conceptual documentation and Planned exercises.** The previously reported IIQ connector connectivity test remains **Previously Completed, Evidence Pending** in the [status tracker](../docs/implementation-status.md). A connector test proves neither account provisioning nor end-to-end onboarding.

## Platform model

A tenant is the organizational directory boundary for users, groups, applications, and policies. An app registration defines an application object; a service principal represents the application's local presence in a tenant and is managed through Enterprise applications. Treat client/application ID, object ID, tenant ID, and an employee ID as different identifiers. [Microsoft application model](https://learn.microsoft.com/en-us/entra/architecture/establish-applications)

The Northstar cloud-only joiner design is HR → IIQ → Entra account → approved access. The separate [AD hybrid design](../active-directory/README.md) introduces AD provisioning and a selected sync service. Choose account authority before implementation to avoid creating competing cloud-only and synchronized identities.

## Exercise sequence

| Area | Planned exercise | What must be demonstrated |
|---|---|---|
| Tenants and administration | Inventory lab tenant, roles, and administrative units | Scoped administrative boundary; no implied tenant ownership from connector access |
| Users and groups | Create one disabled synthetic user and a harmless security group | Unique employee ID, controlled group membership, cleanup and duplicate detection |
| Dynamic groups | Model a department rule after attribute validation | Membership processing observed; lifecycle timing and license requirements recorded |
| App registrations | Register a lab client; compare delegated and application permissions | Consent and effective permissions understood; secret/certificate stored outside Git |
| Enterprise applications | Configure one test app assignment | Assignment is separate from app registration and from the app's own authorization |
| Microsoft Graph | Read selected synthetic user fields; then test a reviewed write | Correct tenant, scopes/roles, HTTP handling, pagination, audit trail and target state |
| Authentication | Compare SAML with OIDC authorization-code flow | Issuer/audience/redirect/signature validation; no captured tokens published |
| MFA and Conditional Access | Stage a scoped policy using report-only/testing where supported | Intended user/device impact plus emergency administrator access verified |
| Identity Protection | Study risk signals and remediation | Available license and supported risk controls identified; no fake risky-sign-in evidence |
| PIM | Configure time-limited eligible test-role activation if licensed | Justification, approval/MFA as configured, activation expiry, audit record |
| Governance | Request access package, review it, expire or revoke assignment | Approval separated from fulfillment and remediation |
| Microsoft 365 licensing | Assign an available test license only when required | Usage location, SKU availability, service plans, assignment errors and reclamation |
| Provisioning and synchronization | Compare app provisioning with directory synchronization | Object authority, source anchor, mappings, scope and conflict behavior documented |
| Workload identities | Inventory a service principal and compare managed identity | Owner, purpose, permissions and credential lifecycle recorded |
| Hybrid identity | Evaluate Connect Sync versus Cloud Sync for actual lab requirements | Supported topology and attribute ownership chosen using current documentation |

Microsoft Graph user creation requires attributes beyond a display name; a UPN must use an appropriate tenant-verified domain. `accountEnabled` explicitly controls the account's enabled flag. A successful create response is only the start of provisioning verification. [Graph create user](https://learn.microsoft.com/en-us/graph/api/user-post-users?view=graph-rest-1.0)

Entitlement management supports governed resource bundles called access packages. PIM addresses privileged activation, while access reviews reassess continued need. These features have subscription and scenario requirements; check licensing before choosing an exercise. [Entitlement management](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-overview), [governance licensing](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals)

Managed identities remove the need for an application to manage a credential for that identity in supported Azure scenarios; they do not remove permission review or replace every service principal scenario. [Managed identities overview](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview)

## Sarah Miller pre-hire acceptance plan

**Status: Planned end-to-end validation; related joiner development is In Progress.** Use synthetic Sarah Miller and a configurable start date. Generate the candidate `smiller`, then check uniqueness and supported characters before reserving the actual UPN. Name collisions must not be silently merged.

1. Aggregate employee ID and verify a single IIQ identity, manager, and lifecycle dates.
2. Confirm whether this is a cloud-only or AD-authoritative account path.
3. Create the approved account disabled; query the target and verify `employeeId`, UPN, and `accountEnabled = false`.
4. Record request and connector result; reaggregate to check correlation. Denial, missing manager, duplicate ID, and permission failure must have visible outcomes.
5. At the authorized start-date boundary, enable the account only after eligibility checks. Document the business timezone and scheduler behavior.
6. Provision approved group/app access and any required license; verify each outcome independently. A group membership is not proof of application authorization or license success.
7. Test rollback and offboarding in the disposable lab. Document session/token behavior separately from disabling an account.

## Actual results and limitations

No Graph calls, policy changes, user creation, license assignment, or authentication experiments were executed for this module. The original connector export, test timestamp, tenant settings, permissions and IIQ connector version are unavailable. Next reproduce the read-only connector test with sanitized evidence before enabling writes.
