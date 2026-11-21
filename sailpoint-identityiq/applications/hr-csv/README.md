# Simulated authoritative HR CSV

**Status: Previously Completed, Evidence Pending.** Historical sources were ACMEE HR, Practice CSV, NorthStar HR CSV, Friends CSV, and Northstar Workday HR. All are lab names; Northstar Workday HR was simulated with CSV. No Workday API integration is claimed.

## Objective and business requirement

Provide a reproducible source for identity creation, attributes, manager relationships, and later lifecycle exercises at fictional Northstar Health.

## Prerequisites and architecture

A local licensed IIQ installation, a delimited-file connector supported by its release, and a runtime-readable synthetic CSV are needed. Flow: CSV → account aggregation → mapping/correlation → Identity Cube → selected refresh behavior. Follow the full [aggregation lab](../../identity-aggregation/README.md).

## Code and configuration

Canonical fixtures and provenance are in [sample-data/synthetic](../../../sample-data/synthetic/README.md). These are newly authored, not exported historical files.

| CSV attribute | Intended use in this example | Validation |
|---|---|---|
| employeeID | Account identity; candidate stable person correlation key | Nonempty, unique within source, string |
| firstName / lastName | Identity name mappings | Preserve characters; no username derivation here |
| fullName | Account display attribute; candidate Identity displayName | Display only, not unique matching |
| email | Candidate Identity email | Synthetic `example.org` address |
| phoneNumber | Optional phone mapping | Fictional reserved-style value |
| jobTitle / department | Future role/lifecycle inputs | Validate controlled vocabulary first |
| managerEmployeeID | Manager matching to employee ID | Blank or one known manager |
| employmentStatus | Future lifecycle design input | No automatic enable/disable supplied |
| startDate | Future pre-hire activation date | ISO date; date alone does not trigger automation |

## Implementation steps

1. Copy the fixture to a private lab runtime location; do not embed machine-specific paths in shared exports.
2. Inspect the header and row count before importing.
3. Configure string attributes and `employeeID`/`fullName` identity/display settings.
4. Choose one source as authoritative and define attribute mappings before aggregation.
5. Configure manager matching and account correlation explicitly.
6. Aggregate, inspect task results/Links/Identities, then run only needed refresh options.

## Expected behavior and test procedure

Expect five accounts in this fixture, Bob's manager to resolve to Ann under the documented mapping, and an unchanged repeat run to preserve person ownership. Compare every row to the resulting identity and save sanitized evidence. Do not use the secondary duplicate fixture as an ordinary production-style HR feed.

## Actual results and troubleshooting

The maintainer describes historical successful schema discovery, aggregation, mappings, and Identity Cube updates. No original evidence was inspected and this new fixture has not been run in IIQ. If fields are missing, distinguish source parse/schema failures from Link-to-Identity mapping failures. If duplicate people appear, inspect authoritative settings and [correlation](../../identity-correlation/README.md) before another import.

## Security, limitations, and next improvement

Use fictional data only; omit real HR exports and private runtime paths. This file does not supply a licensed connector or deployment-specific XML. Next, capture one clean aggregation/refresh run with the fixture and promote only the demonstrated capability's status.
