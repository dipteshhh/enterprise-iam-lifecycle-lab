# MySQL JDBC aggregation and identity mapping

**Status: Previously Completed, Evidence Pending.** The maintainer describes a working connection, aggregation, and mapping corrections. No original SQL, application XML, task results, or runtime evidence was inspected. The supplied SQL is newly authored illustrative source.

## Objective and business requirement

Read five synthetic employees from `example_db.employees` into IIQ and populate useful identity attributes. This demonstrates a custom relational source without claiming that a successful connection proves mapping or provisioning.

## Prerequisites and architecture

Use an isolated MySQL 8 database, a compatible JDBC driver acquired through its legitimate distribution, an IIQ JDBC connector, and credentials with SELECT access to the test table. Use a separate setup account for DDL; the aggregation account should not require account-management privileges.

```mermaid
flowchart LR
  DB["example_db.employees"] --> J["JDBC query and driver"]
  J --> S["IIQ account schema"]
  S --> L["Account Link"]
  L --> M["Identity attribute mappings and correlation"]
  M --> I["Identity Cube after selected refresh"]
```

## Code and configuration

Canonical setup: [mysql-employees.sql](../../../scripts/sql/mysql-employees.sql). It creates the described seven columns and inserts five entirely fictional records. Run only on a disposable MySQL instance where `example_db` does not exist, using a client configured to stop on the first error; never use `--force` or a GUI continue-on-error option. A CREATE error is not a universal write guard: later INSERTs can run if the client continues. The SQL does not create database users or embed passwords. [MySQL batch behavior](https://dev.mysql.com/doc/refman/8.4/en/batch-mode.html).

Illustrative connector settings:

| Setting | Example / decision |
|---|---|
| Driver class | `com.mysql.cj.jdbc.Driver`; confirm installed Connector/J release |
| URL | `jdbc:mysql://localhost:3306/example_db`; localhost means the IIQ runtime's host |
| Username/password | Supply privately; no values tracked in Git |
| Connection test query | `SELECT 1` |
| Account identity attribute | `employeeID` |
| Display attribute | `fullName` |
| Authority | Decide explicitly; do not add a second HR authority unintentionally |

Connector query (omit the trailing semicolon in the IIQ query field):

```sql
SELECT employeeID, firstName, lastName, fullName,
       email, phoneNumber, jobTitle
FROM example_db.employees
ORDER BY employeeID
```

The setup `.sql` file uses normal SQL statement terminators. SailPoint's JDBC query-field guidance differs and cautions against ending those field entries with semicolons. [JDBC query settings](https://documentation.sailpoint.com/connectors/identityiq8_3/jdbc/help/integrating_jdbc/account_query_settings.html). Connector/J connection URL syntax is documented by [MySQL](https://dev.mysql.com/doc/connector-j/en/connector-j-reference-jdbc-url-format.html).

## Implementation steps

1. Inspect the SQL and use a disposable MySQL instance with no existing `example_db`. The script creates that database. Run with a setup account through an interactive password prompt, not a password in shell arguments, and stop on the first error.
2. Run the verification SELECT statements at the bottom. Confirm five rows, unique employee IDs, and expected column names.
3. Test the same query with the intended read-only connector credential.
4. Create the JDBC application and configure connection/query settings. Do not commit its raw exported XML.
5. Discover account schema and inspect exact field names/case/types. Set identity/display attributes.
6. Define person correlation and identity attribute mappings. An account schema does not automatically populate all person-level attributes.
7. Aggregate the application and inspect every Link. Run only required identity-refresh options and inspect the Identity's name, display name, email, and job title.
8. Repeat unchanged, then update one synthetic attribute in a separate controlled experiment. Confirm same identity ownership and capture sanitized before/after evidence.

## Expected behavior and test procedure

Expect five source rows and five aggregated accounts when no filters omit records. Identity counts depend on authoritative/correlation settings; do not promise five new identities in an existing lab. Test whether names and emails are present first on the Link and then on the Identity. Repeating aggregation should not create additional people under correct stable matching.

## Actual results and troubleshooting

The maintainer reports initially seeing Identity Cubes containing only employeeID values, then adjusting mappings and aggregating again to populate other fields. That history does not establish the exact final mapping or precedence configuration.

- If the query returns missing columns, correct SQL/schema before identity mappings.
- If the Link is populated but the Identity is not, inspect mapping source/precedence and refresh settings.
- If JDBC schema names differ from aliases, compare driver behavior with SailPoint's version-specific guidance; do not apply URL workarounds without reproducing the issue. [JDBC troubleshooting](https://documentation.sailpoint.com/connectors/identityiq/jdbc/help/integrating_jdbc/troubleshooting.html).
- Connection success does not prove the aggregation query, correlation, or provisioning works. JDBC provisioning requires separate supported configuration/rules; none is claimed here.

## Security, limitations, and next improvement

Prefer TLS when crossing hosts, constrain database network access, use SELECT-only aggregation access, and keep credentials outside source control. The local URL is illustrative, not a portable network topology. MySQL/IIQ execution of the new script remains unverified. Next, record a complete source row → Link → Identity mapping test with no extra authority or provisioning options enabled.
