# Authoritative learning resources

Reference links reviewed for this documentation foundation on **2026-11-20**. Product documentation changes; recheck the installed version, connector, subscription and API support before running a lab. A source establishes documented behavior, not evidence that this lab implemented it.

| Study area | Primary source | How to use it |
|---|---|---|
| IIQ aggregation | [Account aggregation, IIQ 8.4](https://documentation.sailpoint.com/identityiq_84/help/tasks/account_aggregation.html) | Compare task behavior with the locally installed IIQ release |
| IIQ refresh | [Identity refresh, IIQ 8.4](https://documentation.sailpoint.com/identityiq_84/help/tasks/identity_refresh.html) | Distinguish role evaluation from external provisioning options |
| IIQ provisioning state | [Updating Identity Cube, IIQ 8.5](https://documentation.sailpoint.com/identityiq/8.5/help/provisioning/update_identity_cube.html) | Understand why plan execution and role detection require separate checks |
| ISC identity model | [Identity profiles](https://documentation.sailpoint.com/saas/help/setup/identity_profiles.html) | Map authoritative source values and understand profile priority |
| ISC access model | [Access overview](https://documentation.sailpoint.com/saas/help/access/index.html) | Separate entitlements, access profiles and roles |
| ISC lifecycle | [Lifecycle states](https://documentation.sailpoint.com/saas/help/provisioning/lifecycle.html) | Review configured access effects before applying processing changes |
| SailPoint APIs | [API specifications](https://developer.sailpoint.com/docs/api/) | Select the product and a supported endpoint/version; review authentication and scopes |
| AD DS | [AD DS overview](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/active-directory-domain-services) | Follow official concepts for forests, domains, replication and security |
| AD automation | [ActiveDirectory PowerShell module](https://learn.microsoft.com/en-us/powershell/module/activedirectory/) | Check exact cmdlet parameters and prerequisites before a scoped exercise |
| Entra app model | [Applications in the Entra ecosystem](https://learn.microsoft.com/en-us/entra/architecture/establish-applications) | Distinguish application objects from tenant service principals |
| Graph users | [Create user](https://learn.microsoft.com/en-us/graph/api/user-post-users?view=graph-rest-1.0) | Check required properties and permissions; do not copy example passwords |
| Hybrid identity | [Sync tools](https://learn.microsoft.com/en-us/entra/identity/hybrid/sync-tools), [current comparison](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/connect-to-cloud-sync-decision-guide) | Validate topology and feature requirements without relying on old comparison tables |
| Entra governance | [Governance overview](https://learn.microsoft.com/en-us/entra/id-governance/identity-governance-overview), [licensing](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals) | Check entitlement management, reviews and PIM availability before selecting labs |
| Digital identity | [NIST SP 800-63-4](https://pages.nist.gov/800-63-4/) | Read proofing, authentication and federation as distinct assurance subjects |
| Control catalog | [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) | Map controls to evidence; no certification claim |
| Zero Trust | [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final) | Relate resource-focused architecture to identity policy |
| Protocol specifications | [Protocol guide](../iam-fundamentals/protocols.md) | Follow the individual RFC, OASIS, OpenID and W3C links |
| Frameworks and regulations | [Governance study map](../identity-governance/README.md) | Use official ISO, AICPA, HHS, SEC and EUR-Lex sources in context |

Do not upload licensed product documentation, binaries or libraries to this repository. If an API method or connector behavior cannot be confirmed in accessible official documentation, record the question and validate it in the authorized local environment instead of inventing a supported behavior.
