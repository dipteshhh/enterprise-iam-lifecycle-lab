# Troubleshooting index

## Latest lifecycle cases — November 26

The [dedicated Leaver troubleshooting guide](../labs/leaver/troubleshooting.md) covers ten reported issues/engineering decisions with problem, observations, cause certainty, investigation, resolution and lessons: missing Oracle roles/partial Create, stale Links, live retrieval, empty plans, XML nesting, no-account continuation, role versus direct cleanup, independent SQL verification, potential UNLIMITED TABLESPACE side effects and redundant revokes. Jane's entitlement recovery remains planned; hypothetical dependent-privilege errors are not presented as observed failures. [Test matrix](../labs/leaver/test-scenarios.md) and [provenance](evidence/leaver-2026-11-26.md).

## Preserved earlier diagnostic history

These symptoms come from the owner's narrative. Candidate causes and diagnostic procedures are not claims that every issue was conclusively resolved. Preserve actual errors and retests in a future evidence record.

| Symptom/history | Diagnostic sequence | Module |
|---|---|---|
| Tomcat used an unsuitable Java runtime | Identify running JVM → inspect service environment → compare supported matrix → restart only in an authorized session → verify process/logs | [Environment](lab-environment.md) |
| Identity Cube initially showed only employeeID | Compare source SQL/CSV → account schema/Link → identity mappings → targeted refresh; distinguish blank source from missing mapping | [MySQL](../sailpoint-identityiq/applications/mysql-jdbc/README.md) |
| Bob's manager did not resolve as expected | Check manager key, Ann's aggregated identity and key type; inspect manager mapping and refresh after both records exist | [Correlation](../sailpoint-identityiq/identity-correlation/README.md) |
| Mitch 401 appeared twice | Inventory authoritative settings, identity naming and correlation rules; inspect both accounts; do not delete Cubes as a first diagnostic | [Duplicate experiment](../sailpoint-identityiq/identity-correlation/README.md) |
| Business Role assignable but IT Role not offered | Inspect role type/options, requestability, required relationship and technical profile; distinguish assignment from detected access | [Roles](../sailpoint-identityiq/roles-and-entitlements/README.md) |
| Assigned role did not yield Oracle access | Inspect expansion, approvals, provisioning policy, connector result, target readback and refresh task flags | [Oracle](../sailpoint-identityiq/applications/oracle/README.md) |
| Role warning/error indicator | Capture exact message and configuration; check missing profiles/relationships/requirements before assuming refresh fixes it | [Roles](../sailpoint-identityiq/roles-and-entitlements/README.md) |
| Workflow dropdown empty or has blank choices | Inspect job-title input, persisted attribute/filter, returned value type, nulls and form variable mapping | [Workflow WIP](../sailpoint-identityiq/workflows/README.md) |
| Workflow stops unexpectedly | Trace transition conditions, step returns and workflow variables using sanitized logs | [Workflow WIP](../sailpoint-identityiq/workflows/README.md) |
| No BeanShell/named logger output | Identify active Log4j2 config; check logger level, appender references, output permissions and actual execution path | [Rules](../sailpoint-identityiq/rules/README.md) |
| Connector test passes but lifecycle does not | Connectivity is only one boundary; inspect permission, policy, identity selection, account action and target readback independently | [Entra](../sailpoint-identityiq/applications/entra-id/README.md) |

For every new failure capture: expected state, observed state, exact task/request reference, sanitized error, versions, hypothesis, one controlled change and retest. A symptom disappearing is insufficient evidence for an untested provisioning branch.
