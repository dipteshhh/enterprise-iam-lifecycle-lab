# Evidence ledger

Reviewed on 2026-11-20 using the project owner's supplied lab narrative and the existing Git repository.

| Evidence ID | Artifact inspected | What it establishes | What it does not establish |
|---|---|---|---|
| E-001 | Original commit `45ca03a`, one `README.md` | Repository existed with an IIQ/Entra lifecycle description | Connector configuration, code execution or target changes |
| E-002 | Owner's master project prompt, supplied in this chat | Reported environment, previous experiments, challenges and current intent | Independently verified configuration or successful runtime tests |
| E-003 | Newly authored repository examples | Reviewable illustrative code, documentation and fixtures | Original IIQ exports or execution inside the owner's environment |

The original README contained the title `enterprise-iam-lifecycle-lab` and described a hands-on lifecycle project using SailPoint IdentityIQ and Microsoft Entra ID. It contained no configuration, code or test evidence. The initial working tree was clean; `main` tracked `origin/main` at the original HTTPS remote.

No original SailPoint installation, task results, application exports, database readbacks or tenant screenshots were inspected. The repository work does not promote those historical capabilities to Verified.

## Add a runtime record

For each completed exercise, add a small sanitized Markdown record here containing:

- Capability and previous status; test date and operator.
- IIQ build/patch, connector version, Java runtime and target version.
- Fixture path/commit, synthetic identity key, relevant settings and pre-test state.
- Test steps, actual task/request status, independent target readback and post-aggregation identity state.
- Negative/replay cases, cleanup, failures and remaining limitations.
- Links to reviewed evidence artifacts; state any deliberate redactions.

Keep raw logs and exports outside Git, for example in ignored `local-evidence/`. Do not treat a green connector test, an approval, a queued request or a Java unit test as proof of end-to-end provisioning. Only change the relevant capability's status after reviewing evidence for its full stated scope.
