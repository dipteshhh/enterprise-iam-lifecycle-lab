# Practical lab template

Copy this structure into a substantive new lab; do not create blank modules merely to mirror the roadmap.

## Lab title and status

State one [status](implementation-status.md), artifact provenance, product/connector versions and last test date. Use “not recorded” for unavailable facts.

## Objective

Identify one measurable technical capability.

## Business requirement

Explain whose access need or control this capability serves.

## Prerequisites

Record permissions, licensed access, isolated infrastructure, configuration dependencies and a rollback baseline.

## Architecture

Describe the data and control boundaries. Label planned components in diagrams.

## Implementation steps

Record the actual settings and sequence. Mark proposed steps separately from steps already performed.

## Code and configuration

Link canonical sanitized source files; identify illustrative reconstructions. Explain inputs, outputs, execution context and APIs used.

## Expected behavior

Define positive, negative, duplicate, missing-data and failure outcomes before testing.

## Test procedure

Give repeatable setup, execution, target readback, identity reconciliation and cleanup steps. Include replay and partial-failure cases for provisioning.

## Actual results

Record only observed outcomes, with date, versions and sanitized evidence references. “Not run” is a valid result. An expected result is not evidence.

## Troubleshooting

For each issue: symptom, candidate causes, diagnostic evidence, change made, retest and unresolved questions.

## Security considerations

Explain credentials, scope, authorization, approvals, personal data and safe logging.

## Limitations

State missing evidence, untested branches, connector differences and environmental constraints.

## Next improvements

Choose a small next implementation and its acceptance criteria.
