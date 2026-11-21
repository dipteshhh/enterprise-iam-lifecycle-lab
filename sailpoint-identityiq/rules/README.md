# IdentityIQ rule learning collection

**Status:** historical query exercises are **Previously Completed, Evidence Pending**; the added helpers are **Conceptual**, newly authored examples awaiting IIQ execution. None is an original exported rule. See the [central tracker](../../docs/implementation-status.md).

## Purpose and execution boundary

Northstar Health needs to retrieve identities, diagnose missing attributes, and determine whether an account request needs more investigation. These examples progress from list operations to filtered queries and account classification. They do not provision access.

An authorized administrator must supply a licensed, isolated IIQ lab, the installed version's API documentation, test identities, and an execution mechanism that injects `context`. A `.bsh` file is a script body, not a complete importable Rule XML object. Rule types define different input and return contracts; a helper returning a `Map` cannot simply be pasted into a Correlation rule that expects another contract. Check the installed rule signature before adapting one. [SailPoint rules and scripts](https://documentation.sailpoint.com/identityiq/8.5/help/system_administration/rules_scripts.html)

The referenced public manual is a documentation reference, not evidence that the lab runs IIQ 8.5. The user's exact IIQ version and patch remain unknown. Confirm `Identity.isInactive`, `Link.getApplicationName`, `getObjectByName`, queryable attributes, and signatures against the locally licensed API before execution. No SailPoint libraries are redistributed here.

## Example catalog

| Example and provenance | Inputs and context | Expected return | Verification and limits |
|---|---|---|---|
| [Count](identity-queries/count-identities.bsh), reconstructed historical pattern | IIQ `context`; small isolated identity set | Integer list size, including any non-person Identity objects returned | Compare to a separately enumerated test set; this loads all matches into memory, so it is a beginner exercise rather than a production counting strategy. |
| [Names](identity-queries/list-identity-names.bsh), reconstructed historical pattern | Same | List of `Identity.getName()` values; order unspecified | Compare by set, not ordering. Names are not display names or internal IDs. No employee-only filter is applied. |
| [Emails](identity-queries/list-identity-emails.bsh), reconstructed historical pattern | Same | List containing strings and possibly nulls | Use one populated and one missing email; verify null remains present. Historical null observations are narrative only. Do not publish real output. |
| [Job title selection](identity-queries/select-by-job-title.bsh), illustrative | `context`, nonblank String `jobTitle` | List of matching identity names | Verify matching, nonmatching, blank, and unmapped title cases. Confirm `jobTitle` exists as a searchable Identity attribute; display or source schema configuration alone does not guarantee querying works. No account-Link filter, so no-account identities remain eligible for later policy checks. |
| [Selected identity validation](identity-queries/validate-selected-identity.bsh), illustrative | `context`, exact String `identityName` | Map with name and Boolean email presence, or exception | Test active, inactive, missing identity, and missing email. Missing email is reported, not silently treated as a valid mailbox. This is not a full eligibility, identity-correlation, or authorization rule. |
| [Oracle Link classification](account-inspection/classify-oracle-links.bsh), illustrative | `context`, exact `identityName`, exact `applicationName` | Map with `CREATE_CANDIDATE` or `MODIFY_CANDIDATE`; Modify includes native identity | Test zero, one, and two matching Links; missing application; blank native identity; inactive identity. Multiple accounts stop for review. Reconcile against Oracle before any write: zero Links can reflect stale data. |
| [Logger marker](logging/workflow-marker.bsh), illustrative adaptation | IIQ runtime with Log4j2 available | Fixed marker string; debug event if routing and level permit | Execute once with a named logger in the isolated lab; check runtime config, level, appender, file permissions, and destination. No secrets, identity attributes, or whole plans are logged. |

Every row's expected behavior is a proposed test oracle, not recorded IIQ output. Actual results: no BeanShell execution, rule import, or connector execution was performed while preparing this collection.

## Implementation and learning sequence

1. Inventory the IIQ version, rule signature, injected variables, and test identity set. Start with read-only examples under a limited administrator account.
2. Run count, names, and emails. Record whether workgroups or service identities are included and how missing values appear.
3. Validate the source-to-Identity `jobTitle` mapping, then run the filtered query. Do not substitute concatenated query strings for `Filter.eq`.
4. Decide whether a form persists an Identity ID or name. Resolve that value once and consistently pass it between steps. For an ID use an API documented for ID retrieval, rather than a name lookup.
5. Add input validation and Link inspection. Treat every returned action as a candidate until authorization, approval, account freshness, and connector-specific requirements are checked.
6. Capture sanitized results and the exact source revision in an evidence record before promoting any example's status.

`SailPointContext` retrieves persistent IIQ objects. `Identity` represents the Identity Cube; `Application` identifies the managed source; `Link` represents an aggregated application account. `QueryOptions` groups query criteria and `Filter.eq` expresses equality. None is an ISC API. The Link helper intentionally compares application names exactly; deployments with several account instances need an explicit instance-selection policy as well.

## Java and BeanShell compatibility

Raw collections in the reconstructed files preserve the supplied teaching patterns. New helpers cast each element explicitly so the checks are visible. In compiled Java prefer `List<Identity>` and `Map<String, Object>` where supported, but do not assume the installed BeanShell parser supports all Java language syntax or generics. Java platform compatibility does not establish BeanShell compatibility. Exception handling should route a validation failure to review; catching every exception and returning success would conceal failed work.

The independent [Java username exercise](../../scripts/java/README.md) demonstrates typed collections and deterministic collision handling without SailPoint libraries. It is a new local exercise, not a deployed BeanShell username rule. Investigate the target connector's supported configuration before introducing a custom naming rule.

## Troubleshooting and next improvements

An empty dropdown can mean no matching identities, an unmapped/nonsearchable attribute, a wrong form return type, or missing variable propagation. Inspect the exact query and expected value type before changing data. A missing log line can mean debug is disabled even when execution succeeded. Resolve these separately from provisioning failures.

Future work: bounded queries/iterator cleanup using the installed API, a correctly typed correlation rule with zero/one/multiple-match tests, application queries, entitlement/role evaluation with version-specific semantics, provisioning-policy validation, workflow helper libraries, and structured error reporting. None of those advanced rules is claimed implemented here. See the [workflow project](../workflows/conditional-oracle-provisioning/README.md) and [plan anatomy](../provisioning/README.md).
