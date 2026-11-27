# Evidence ledger

Updated on 2026-11-26 using the owner's latest lifecycle narrative, the existing repository and previously captured scoped Oracle runtime evidence. E-005 is an owner-report record, not newly collected runtime evidence.

| Evidence ID | Artifact inspected | What it establishes | What it does not establish |
|---|---|---|---|
| E-001 | Original commit `45ca03a`, one `README.md` | Repository existed with an IIQ/Entra lifecycle description | Connector configuration, code execution or target changes |
| E-002 | Owner's master project prompt, supplied in this chat | Reported environment, previous experiments, challenges and current intent | Independently verified configuration or successful runtime tests |
| E-003 | Newly authored repository examples | Reviewable illustrative code, documentation and fixtures | Original IIQ exports or execution inside the owner's environment |
| E-004 | [Oracle Create/Modify runtime record](oracle-create-modify-2026-11-20.md) and sanitized captures | Actual scoped requests 13/14, target grants, exact Link reconciliation, verification and sequential duplicate guards | Original custom-form completion, automatic correlation, login usability, broad compatibility or historical Ann/Bill evidence |
| E-005 | [November 26 lifecycle implementation narrative](leaver-2026-11-26.md) | Owner-reported Joiner completion, primary Leaver test outcomes, final workflow contract, connector improvement and partial-provisioning lessons | Original Leaver/Joiner exports, new captured logs/SQL/screenshots, Mary's final regression, every Oracle access category or production readiness |

The original README contained the title `enterprise-iam-lifecycle-lab` and described a hands-on lifecycle project using SailPoint IdentityIQ and Microsoft Entra ID. It contained no configuration, code or test evidence. The initial working tree was clean; `main` tracked `origin/main` at the original HTTPS remote.

During the initial foundation no runtime artifacts were inspected. E-004 later inspected the local IIQ installation, private application/workflow exports and actual synthetic request/database results. Only its bounded capabilities are independently Verified. E-005 adds the owner's later implemented/tested lifecycle status while retaining the missing-source and evidence boundary. Other historical configurations and platforms remain evidence pending.

## Add a runtime record

For each completed exercise, add a small sanitized Markdown record here containing:

- Capability and previous status; test date and operator.
- IIQ build/patch, connector version, Java runtime and target version.
- Fixture path/commit, synthetic identity key, relevant settings and pre-test state.
- Test steps, actual task/request status, independent target readback and post-aggregation identity state.
- Negative/replay cases, cleanup, failures and remaining limitations.
- Links to reviewed evidence artifacts; state any deliberate redactions.

Keep raw logs and exports outside Git, for example in ignored `local-evidence/`. Do not treat a green connector test, an approval, a queued request or a Java unit test as proof of end-to-end provisioning. Only change the relevant capability's status after reviewing evidence for its full stated scope.
