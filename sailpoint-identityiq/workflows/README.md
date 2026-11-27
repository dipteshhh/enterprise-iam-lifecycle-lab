# IdentityIQ workflow experiments

## Current lifecycle implementation

The November 26 update documents the [Northstar Leaver Workflow](../../labs/leaver/README.md), with eight variables, twelve conditional top-level steps and three LCM Provisioning calls. [Current Joiner status](../../labs/joiner/README.md) is implemented/tested as reported. Original Leaver and complete Joiner exports were not supplied; new Leaver XML/BeanShell is labeled reconstructed/unexecuted. The earlier experiment history below retains its original scope.

## Earlier workflow experiments

**Status: In Progress.** The owner's historical experiments include Process Designer, Start/Stop and Script steps, forms, transitions, return values, workflow variables, `wfcontext.setVariable`, QueryOptions-based selection and named logging. Original workflow exports and execution evidence were not available for inspection.

The active [conditional Oracle provisioning project](conditional-oracle-provisioning/README.md) documents the evolved requirement: eligible identities remain selectable regardless of existing Oracle account presence. Account existence is evaluated afterward, alongside authorization and connector-specific policy.

Before adapting a form, establish whether it returns an Identity name or internal ID and use the matching retrieval method consistently. Inspect field return type, allowed-values shape, step return mapping, transition conditions and variable propagation separately. A blank dropdown or missing log line is a diagnostic symptom, not proof of an empty Identity Cube set.

See [rules](../rules/README.md) for read-only helpers, [provisioning](../provisioning/README.md) for plan anatomy, [troubleshooting](../../docs/troubleshooting.md) and [lifecycle status/design](../../northstar-health/lifecycle-plan.md). No original import-ready completed workflow export is claimed.
