# IdentityIQ workflow experiments

**Status: In Progress.** The owner's historical experiments include Process Designer, Start/Stop and Script steps, forms, transitions, return values, workflow variables, `wfcontext.setVariable`, QueryOptions-based selection and named logging. Original workflow exports and execution evidence were not available for inspection.

The active [conditional Oracle provisioning project](conditional-oracle-provisioning/README.md) documents the evolved requirement: eligible identities remain selectable regardless of existing Oracle account presence. Account existence is evaluated afterward, alongside authorization and connector-specific policy.

Before adapting a form, establish whether it returns an Identity name or internal ID and use the matching retrieval method consistently. Inspect field return type, allowed-values shape, step return mapping, transition conditions and variable propagation separately. A blank dropdown or missing log line is a diagnostic symptom, not proof of an empty Identity Cube set.

See [rules](../rules/README.md) for read-only helpers, [provisioning](../provisioning/README.md) for plan anatomy, [troubleshooting](../../docs/troubleshooting.md) for historical issues and [lifecycle plan](../../northstar-health/lifecycle-plan.md) for future event-driven work. No import-ready completed workflow is claimed.
