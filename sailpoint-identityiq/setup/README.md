# Re-establishing the IdentityIQ lab baseline

**Status: Previously Completed, Evidence Pending.** This is a verification runbook for the [reported environment](../../docs/lab-environment.md), not a fresh installation recipe.

## Objective and business requirement

Establish which isolated platform and connector versions produced a result so Northstar Health experiments can be explained and repeated without assuming machine-specific paths.

## Prerequisites and architecture

Licensed IIQ installation access, matching vendor support documentation, local administrator access, and a recoverable lab backup are required. The reported flow is browser → Tomcat/IIQ → IIQ MySQL database and separate practice targets. Do not confuse IIQ's persistence database with the `example_db` JDBC source.

## Verification procedure

1. Record macOS/CPU, IIQ build and patch, Tomcat, actual service JVM and MySQL versions without exporting secrets.
2. Check the installed IIQ release's supported platform matrix; document any unsupported experiment explicitly.
3. Review service launch environment and active log configuration. Validate the historical `JAVA_HOME`/`JRE_HOME` changes against the running process.
4. Confirm an isolated login and appropriate IIQ rights. Inventory applications by connector type/version, authoritative setting and permitted operations; redact host/tenant identifiers as needed.
5. Record the initial identity/account counts and back up disposable test configuration privately.
6. Execute one small target-read aggregation lab before attempting provisioning. Aggregation updates IIQ; review provisioning, lifecycle and refresh options to prevent unintended target actions. Add sanitized evidence and exact task options.

## Code, expected behavior and actual results

No original installation configuration is included. Expected: the service version and JVM can be identified and a scoped task can be traced through logs and UI. Actual: no runtime check was performed during repository authoring. Use the [lab template](../../docs/lab-template.md) to record results.

## Troubleshooting, security and limitations

If the shell and service Java versions differ, inspect service configuration rather than changing every Java installation. If logs are missing, confirm the active configuration, level, appender and write permissions. Do not expose the local admin UI publicly or log credentials. IIQ installation procedures and API compatibility remain dependent on the licensed installed release. Next: collect baseline evidence, then replay the synthetic HR aggregation exercise.
