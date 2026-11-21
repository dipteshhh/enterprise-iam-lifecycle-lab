# Identity engineering flows

**Status: Conceptual.** Each flow is a model for an isolated lab; exact fields, task options and execution APIs depend on the installed products.

## Aggregation and correlation

```mermaid
flowchart LR
    SRC["Source account row"] --> SCHEMA["Parse account schema"]
    SCHEMA --> KEY["Normalize stable key"]
    KEY --> MATCH{"Unique identity match?"}
    MATCH -->|"one"| LINK["Associate account Link"]
    MATCH -->|"none"| AUTH{"Authoritative creation allowed?"}
    AUTH -->|"yes"| CREATE["Create identity under configured rules"]
    AUTH -->|"no"| HOLD["Uncorrelated account review"]
    MATCH -->|"multiple"| HOLD
    CREATE --> LINK
    LINK --> REFRESH["Refresh mapped identity attributes and manager"]
    REFRESH --> VERIFY["Compare source, Link and Identity Cube"]
```

This is a design for handling ambiguity, not a statement that all connectors automatically quarantine duplicates. Configure and test the actual correlation rules. Aggregation reads accounts; correlation associates them with a person; refresh updates selected identity/role data. SailPoint documents configurable [account aggregation](https://documentation.sailpoint.com/identityiq_84/help/tasks/account_aggregation.html) and [identity refresh](https://documentation.sailpoint.com/identityiq_84/help/tasks/identity_refresh.html) options. Avoid enabling provisioning as an incidental diagnostic step.

## ProvisioningPlan lifecycle

```mermaid
flowchart LR
    REQUEST["Authorized access intent"] --> PLAN["ProvisioningPlan"]
    PLAN --> COMPILE["Compile and expand roles; resolve policy fields"]
    COMPILE --> GOVERN["Configured approvals and policy checks"]
    GOVERN -->|"approved"| TARGET["Application-specific account and attribute requests"]
    GOVERN -->|"denied or invalid"| STOP["Stop and record reason"]
    TARGET --> RESULT["Connector or manual execution result"]
    RESULT --> READBACK["Independent target readback"]
    READBACK --> RECON["Reaggregate and refresh as needed"]
    RECON --> CLOSE["Record verified outcome or remediation"]
```

This summarizes the proposed standard access-request path; form/approval ordering is workflow-dependent and not universal. An AccountRequest identifies application, operation and native account identity; AttributeRequests describe intended field/entitlement operations. A plan expresses intent, not successful execution. [IIQ provisioning processing](https://documentation.sailpoint.com/identityiq/8.5/help/provisioning/process_provisioning.html) explains compilation and handlers; release 8.5 is a reference, not the unconfirmed local version. See the [conditional workflow](../../sailpoint-identityiq/workflows/README.md) for account-existence decisions.

## Authentication and federation

```mermaid
sequenceDiagram
    actor User
    participant App as Relying application
    participant IdP as Identity provider
    participant API as Resource API
    User->>App: Open protected application
    App->>IdP: OIDC authorization request with state, nonce and PKCE
    IdP->>User: Authenticate and apply required MFA/policy
    IdP-->>App: Authorization code through browser redirect
    App->>IdP: Redeem code using verifier and appropriate client authentication
    IdP-->>App: ID token and access token
    App->>App: Validate ID token and establish application session
    App->>API: Access token for intended resource
    API->>API: Validate token and enforce authorization
```

This is a conceptual OIDC authorization-code flow, not an implemented Entra SSO integration. The ID token is for the client; the access token is for its resource API. SAML uses assertions and a different protocol flow; SCIM provisions resources and does not authenticate interactive sessions. See the [protocol guide](../../iam-fundamentals/protocols.md) for official specifications and validation requirements.
