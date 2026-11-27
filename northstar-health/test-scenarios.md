# Acceptance scenarios

**Scope: broader acceptance criteria, originally planned.** This table defines expected outcomes, not blanket successful execution claims. Later bounded evidence is in [E-004](../docs/evidence/oracle-create-modify-2026-11-20.md), and the November 26 owner-reported Leaver outcomes are in the [four-scenario test matrix](../labs/leaver/test-scenarios.md). Those narrower tests do not satisfy every control below, such as sessions, automated escalation or pre-hire activation. Record actual outcomes using the [evidence ledger](../docs/evidence/README.md).

| ID / scope | Input or precondition | Expected control and evidence |
|---|---|---|
| T-01 HR baseline | Synthetic primary HR fixture, unique employee IDs | Correct attributes and account Links; count/mappings recorded |
| T-02 replay | Aggregate unchanged T-01 again | No extra Identity Cube or duplicated account; counts and stable keys compared |
| T-03 manager | Bob's manager key refers to Ann | Resolved Identity reference; document task order and refreshed state |
| T-04 missing manager | Manager key absent/unmatched | Flag exception; no arbitrary approval recipient |
| T-05 duplicate source | Mitch 401 in both authoritative fixtures | Reproduce/investigate safely; verify configured matching; never silently choose a duplicate |
| T-06 existing Oracle account | Exactly one valid Oracle Link | Modify correct native identity; no second account; target role readback |
| T-07 no Oracle account | Eligible identity has no Oracle Link | Create with required attributes; verify account before any dependent change |
| T-08 ambiguous account | More than one matching Oracle Link | Stop or require explicit approved account selection; no arbitrary first match |
| T-09 stale Link | Link exists but target account absent | Reconcile and review; no blind Modify success claim |
| T-10 missing required attribute | Create request lacks required connector input | Validation failure before target call; useful sanitized reason |
| T-11 negative approval | Request denied | No target mutation; auditable denial |
| T-12 connector failure | Isolated target unavailable/permission denied | Failed/pending result recorded accurately; bounded retry and escalation |
| T-13 replay after partial result | Account created but entitlement step failed | Readback before retry; no duplicate Create; converge only authorized changes |
| T-14 Sarah pre-hire | Start date future, valid HR data | Disabled target account if supported; no early activation |
| T-15 Sarah activation | Effective start time reached and active HR state | Enable only approved identity; verify target account and sign-in policy separately |
| T-16 username collision | `smiller` already reserved | Collision resolved under explicit naming policy; target policy and concurrency checked |
| T-17 mover | Title/department change | New approved access plus verified obsolete removal; shared entitlement preserved if still required |
| T-18 leaver | Authorized termination event | Disablement, applicable sessions and access removal independently checked; failures escalated |
| T-19 rehire | Same stable key, retained target account | No duplicate identity; retained access reviewed before reactivation |
| T-20 SoD | Two synthetic conflicting permissions | Defined policy violation/approval route; no assertion of a configured SoD engine |

Run each test with a dedicated disposable identity and narrowly scoped entitlement. Capture pre-state, timestamps, task/request references, actual target state, post-refresh identity state, cleanup and unresolved issues. A Java exercise or repository validation pass cannot satisfy these acceptance criteria.
