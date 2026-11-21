# Synthetic fixtures

All records here were newly authored for this repository. They are illustrative fixtures, not original HR exports or proof of completed integrations. Northstar Health and these identities are fictional. The names Ann Parson, Bob Fields, Bill Murray, Mitch Armstrong, and Sarah Miller reproduce the prompt's fictional lab scenarios only.

| File | Purpose | Safeguard |
|---|---|---|
| [northstar-hr.csv](northstar-hr.csv) | Five people, manager matching, lifecycle discussion | Intended isolated baseline |
| [secondary-authoritative.csv](secondary-authoritative.csv) | Repeats Mitch employee ID 401 for duplicate-authority testing | Negative test; do not enable casually |
| [MySQL setup](../../scripts/sql/mysql-employees.sql) | Seven-column, five-row JDBC source | Separate canonical SQL, no credentials |

`employeeID` is a string. The Ann/Bob identifiers `100`/`200`, Bill `300`, and Sarah `500` are illustrative choices; only Mitch's `401` was supplied in the lab narrative. `managerEmployeeID=100` points to Ann. Blank manager denotes a top-level manager. Dates and employment statuses are test data, not historical observations or working lifecycle triggers. `example.org` email addresses and fictional phone values prevent accidental use of actual employee information.

Before import, validate required headers, row counts, nonempty/unique IDs within a source, consistent normalization, and manager references. The same `401` across the two CSVs is intentional. Cross-source duplicates are not automatically errors: whether they should correlate depends on the authoritative-source design. Follow the [correlation lab](../../sailpoint-identityiq/identity-correlation/README.md) and [aggregation lab](../../sailpoint-identityiq/identity-aggregation/README.md).
