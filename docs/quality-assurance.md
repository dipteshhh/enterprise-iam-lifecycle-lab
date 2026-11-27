# Repository quality assurance

## November 26, 2026 lifecycle documentation update

The existing GitHub `main` head matched the inspected local baseline `faef5f78225b26590edd7cea2da89c44b55173a7`. Documentation and examples were prepared in a separate local checkout/branch; original source and captured evidence were retained. There were no baseline Actions or deployable lifecycle/application exports to modify.

| Check | Actual result and scope |
|---|---|
| Repository validator | Passed for all Git-tracked and nonignored publication candidates: relative file links, Markdown fences, two standalone XML documents, synthetic CSV invariants and heuristic credential/prohibited-artifact checks. |
| Mermaid | All **26** Markdown diagrams parsed with Mermaid **11.12.2** and JSDOM **26.1.0** from temporary tooling outside the repository. No render/screenshot quality claim. |
| Leaver XML/source consistency | `python3 scripts/python/build_leaver_workflow.py --check` passed; embedded source matches seven canonical reconstructed `.bsh` files. No original export is claimed. |
| XML structure / branches | Offline inspection confirmed **8 variables, 12 sibling top-level Steps, valid transition targets and 3 distinct LCM argument sets**. Eight modeled Boolean decision combinations reached Stop with the specified skip/convergence behavior; this did not execute BeanShell conditions or IIQ. |
| XML documentation snippets | All **3** fenced XML fragments in Markdown parsed as well formed. Standalone example XML also parsed; no vendor DTD/schema validation or import was performed. |
| BeanShell syntax | **16 source blocks** parsed without evaluation using locally available BeanShell **2.1.8** on JDK **23**: seven canonical files and nine XML Source blocks, including two plan guards. Syntax parsing does not establish API resolution or runtime compatibility. No proprietary library was copied into the repository. |
| SQL | Manually reviewed the new verifier as read-only SELECT/CTE statements using exact supplied account names; it preserves missing-account visibility and avoids role/user writes. No Oracle execution was performed. |
| Preservation / diff | All pre-existing paths retained; **31 existing non-Markdown source/data/XML/capture/policy artifacts** compared byte-identical to baseline. Earlier Joiner/Oracle source and four sanitized captures remain unchanged. Changed documentation updates current status or adds clearly scoped links. |
| Publication hygiene | Reviewed changed text, reconstructed XML/BeanShell, SQL and all publication candidates for credentials, secret-like literals, connection secrets, personal data and proprietary artifacts. Heuristic checks passed; no new screenshots/logs or original runtime evidence were fabricated. |
| Git whitespace | `git diff --check` passed; the complete staged diff and new-file inventory were reviewed before publication. |

No IdentityIQ import, workflow execution, connector call, Oracle SQL execution, aggregation or identity refresh was performed during this repository update. The reported Leaver outcomes remain attributed to the owner in [E-005](evidence/leaver-2026-11-26.md); [E-004](evidence/oracle-create-modify-2026-11-20.md) preserves separately captured earlier runtime evidence. Mary's complete final no-account regression and Jane's entitlement recovery remain outstanding.

## Preserved foundation quality record

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

## Not executed during the initial foundation

- No IIQ application import, BeanShell execution, workflow launch, aggregation or refresh was run.
- No MySQL or Oracle setup/provisioning SQL was executed. SQL examples remain unverified against the actual lab engine/connector.
- No Entra Graph mutation, user creation, tenant policy, license change or SSO test was performed.
- No AD domain, hybrid synchronization, ISC tenant, review campaign or SoD policy was deployed.
- Official reference pages were researched; external links were not exhaustively crawl-tested. Product/API/schema compatibility must be confirmed for the actual installed version.
- Heuristic secret checks are not a complete secret-scanning/security audit. Ignored private local files are outside the publication candidate set.

The validator operates on Git-tracked and nonignored candidate files and does not contact network services. It intentionally does not claim full Markdown parsing, fragment validation, Mermaid rendering, SQL execution or SailPoint schema validation. Passing repository checks must not promote historical integration rows to Verified.

## Subsequent authorized runtime exercise

[E-004](evidence/oracle-create-modify-2026-11-20.md) records actual Oracle fixture setup, installed IIQ 8.3 execution, scoped LCM approvals, independent target readback, targeted Link aggregation, request scanning and duplicate guards. This later work supersedes the initial no-runtime boundary only for that precise scope. Its XML builder also produced 12 well-formed documents with exact source round-trip checks. Original historical claims, other platforms and full custom-form completion remain outside that verification.
