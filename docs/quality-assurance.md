# Foundation quality assurance

Review date: **2026-11-20**. This record covers repository artifacts, not a running IAM deployment. [Capability status](implementation-status.md) and [evidence scope](evidence/README.md) remain authoritative.

## Checks performed

| Check | Actual result and scope |
|---|---|
| Baseline inspection | One initial commit, clean `main`, original HTTPS remote, only the original README; history retained |
| Markdown/navigation | Offline validator passed across **60 files**, including **43 Markdown files** and **157 relative links**; fences balanced and no local fragment links used |
| Mermaid syntax | **22 diagrams parsed successfully** with Mermaid **11.12.2** and JSDOM **26.1.0** in temporary tooling outside the repository; no screenshot/render-quality claim |
| Java | `javac --release 17` with available JDK 23; **19 behavioral checks passed** on JDK 23; not execution on JDK 17, BeanShell or IIQ |
| XML | Illustrative ProvisioningPlan parsed as well-formed XML; no IIQ schema validation or import |
| Synthetic CSV | Five distinct baseline employee IDs, valid manager references, Bob `200` → Ann `100`, and intentional secondary duplicate `401` |
| Security | Reviewed text/code/fixtures for credentials, private keys, sensitive records and proprietary assets; heuristic scanner included in validator |
| Technical review | Separate reviews of lab, workflow, platform and architecture claims; corrected MySQL client error-handling wording and clarified aggregation side effects |
| Git whitespace | Staged changes reviewed with `git diff --cached --check` before delivery |

Run the maintained offline check from the repository root:

```sh
python3 scripts/python/validate_repository.py
git diff --check
```

See [Java instructions](../scripts/java/README.md) for its independent test command. Mermaid validation used temporary npm packages solely as authoring tools; no dependencies, licensed vendor libraries or generated classes were added to the repository. The first parser attempt needed a DOM environment; the corrected environment parsed all diagrams. A sequence-label semicolon that caused a real syntax error was corrected before the successful run.

## Not executed or established

- No IIQ application import, BeanShell execution, workflow launch, aggregation or refresh was run.
- No MySQL or Oracle setup/provisioning SQL was executed. SQL examples remain unverified against the actual lab engine/connector.
- No Entra Graph mutation, user creation, tenant policy, license change or SSO test was performed.
- No AD domain, hybrid synchronization, ISC tenant, review campaign or SoD policy was deployed.
- Official reference pages were researched; external links were not exhaustively crawl-tested. Product/API/schema compatibility must be confirmed for the actual installed version.
- Heuristic secret checks are not a complete secret-scanning/security audit. Ignored private local files are outside the publication candidate set.

The validator operates on Git-tracked and nonignored candidate files and does not contact network services. It intentionally does not claim full Markdown parsing, fragment validation, Mermaid rendering, SQL execution or SailPoint schema validation. Passing repository checks must not promote historical integration rows to Verified.
