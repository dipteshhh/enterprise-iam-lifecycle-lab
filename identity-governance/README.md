# Identity governance and control evidence

**Status: Conceptual foundation; practical controls below are Planned.** The author's reported Oracle request, approval and role experiments remain **Previously Completed, Evidence Pending** until original evidence is inspected. Northstar Health is fictional. No compliance, certification, audit opinion or production deployment is claimed.

## Access governance lifecycle

A useful governance record answers who requested which access, why it was justified, who decided, which policy was evaluated, what the target actually changed, and when access should end. An approved request and a successful provisioning result are different events. Reaggregation and a target-side check reconcile intent with observed access.

| Control area | Northstar design | Planned acceptance evidence |
|---|---|---|
| Access requests | Request a named, owned entitlement with business justification and expiry | Request ID, requester, beneficiary, item, decision and target outcome |
| Approvals | Manager assesses business need; owner assesses application risk where required | Authorized approver, decision, timestamp, rejection path and delegation behavior |
| Entitlement ownership | Every catalog item has an accountable owner and risk classification | Missing/inactive-owner report; ownership reassignment review |
| RBAC / ABAC | Roles bundle job access; attributes/context constrain eligibility and actions | Positive/negative membership cases, attribute quality checks and explicit policy scope |
| Access reviews | Manager reviews people; application owner reviews technical access | Defined population, reviewer, deadline, decisions and unresolved exceptions |
| Certifications | Periodic attestation with verified remediation | Revoked test access removed on target, reaggregated and reviewed for closure |
| Separation of Duties | Define incompatible actions, not just arbitrary role pairs | Conflict detection, blocked request or documented exception and compensating control |
| Privileged access | Separate ordinary and elevated access; time-bound grants where supported | Activation/approval evidence, expiry, least-privilege scope and emergency procedure |
| Orphan accounts | Reconcile accounts to valid identities and owners | Uncorrelated candidate investigation; no automatic deletion from a single unmatched record |
| Dormant accounts | Evaluate qualifying activity over a defined period | Timestamp source, exclusions, owner decision and staged remediation |
| Identity risk | Prioritize review using supported signals and documented rationale | Signal provenance, false-positive review and accountable action |
| Reporting | Summarize approvals, failures, overdue reviews and remediation | Reproducible report query/scope, counts and evidence references |

Governance platforms can support these processes, but target systems enforce many final permissions. Provisioning services, IdPs, directories and PAM tools have distinct responsibilities. Where multiple governance products exist, designate the approval and access-remediation owner to prevent competing writers.

## Northstar toxic-access example

**Illustrative policy:** the same identity must not both create supplier payment details and approve payments. This is separate from the historical Oracle `DBA` role experiment. A production policy requires business-owner validation of actual transactions and effective permissions.

1. Define entitlements that confer each incompatible capability, including nested roles/groups.
2. Test both single access grants and the combined effective-access state.
3. Evaluate the request before fulfillment; document whether the platform supports the desired preventive check.
4. If an exception is allowed, record accountable approval, duration, compensating review and expiry.
5. After remediation, verify the dangerous capability is no longer effective on the target.

Role mining is a future analysis exercise: cluster synthetic access, propose role candidates, and have an owner remove accidental or excessive grants. Frequent historical access is evidence of a pattern, not proof that the pattern should become birthright access.

## Evidence and audit trail design

Keep a lab test record with a unique case ID, date/timezone, platform version, synthetic identity ID, source event, expected access, request/correlation references, decisions, sanitized result, target readback, refresh/aggregation result, negative test and cleanup. Record partial failures and manual interventions explicitly.

Use minimal synthetic data. Review every screenshot, log, XML export and request body for secrets, personal information and proprietary material before committing. Evidence can be summarized rather than publishing a full raw export. Define a retention policy and access controls for any future private evidence store; Git history makes accidental secret disclosure persistent.

Suggested future metrics are request fulfillment time, failed/partial provisioning count, unmatched accounts, inactive entitlement owners, overdue reviews, and unclosed revocations. A metric needs its source, denominator and time window; no values are fabricated here.

## Framework and regulation study map

These are introductions and proposed educational mappings, not a legal applicability determination or an assessment that Northstar meets a standard.

| Reference | What it addresses | IAM study exercise and evidence |
|---|---|---|
| NIST | US National Institute of Standards and Technology publishes standards/guidance; it is not a lab certification | Distinguish a control catalog, architecture publication and assurance guideline |
| NIST SP 800-53 Rev. 5 | Security/privacy control catalog; current releases include updates to the catalog | Map account management (AC-2), separation of duties (AC-5), least privilege (AC-6), and selected audit/identification controls to actual lab tests. [Official catalog](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) |
| NIST SP 800-63-4 | Digital identity proofing, authentication and federation guidance; final Revision 4 was issued July 2025 | Explain IAL/AAL/FAL selection before claiming an assurance level. [Official suite](https://pages.nist.gov/800-63-4/) |
| NIST SP 800-207 | Zero Trust architecture concepts | Trace resource access through identity/device evaluation and policy enforcement; do not claim Zero Trust from MFA alone. [Official publication](https://csrc.nist.gov/pubs/sp/800/207/final) |
| ISO/IEC 27001:2022 | Information security management system requirements | Build a risk-linked access-control/evidence register within an identified scope. Full standard text requires authorized access. [ISO overview](https://www.iso.org/standard/27001) |
| SOC 2 | CPA examination/reporting concerning a service organization's controls under applicable criteria | Define system boundaries, control owners and evidence; a configured control is not a SOC 2 report. [AICPA description criteria](https://www.aicpa-cima.com/resources/download/get-description-criteria-for-your-organizations-soc-2-r-report) |
| HIPAA | US health-information requirements; Security Rule safeguards apply to regulated ePHI contexts | Relate authorized access, unique accountability, audit controls and authentication to a fictional healthcare scenario. No real patient records belong in the lab. [HHS Security Rule summary](https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/index.html) |
| SOX | Sarbanes-Oxley obligations include internal control over financial reporting in applicable organizations | Model approval separation and access changes affecting a fictional finance system. [SEC Section 404 guide](https://www.sec.gov/info/smallbus/404guide.pdf) |
| GDPR | EU personal-data protection requirements; Article 32 addresses appropriate security measures | Minimize identity data, constrain access and document security testing. IAM addresses only part of the obligations. [Official regulation](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=celex%3A32016R0679) |

IAM controls can supply supporting evidence for broader security and compliance programs. Organizational scope, risk assessment, policies, operating effectiveness, retention, training, incident response and external assessment requirements remain beyond any single configuration exercise.

## First practical governance lab

Use a harmless Oracle test role rather than `DBA`: request it for a synthetic identity, deny once, approve once, verify grant, certify removal, and verify revocation. Capture each distinct stage and one connector-failure case. This establishes a small auditable access lifecycle before expanding to role mining or enterprise SoD rules.

**Actual results:** no certification campaign, SoD engine, risk model or governance report was executed for this module. Next attach sanitized historical request/approval evidence and then run the scoped grant-and-revoke exercise.
