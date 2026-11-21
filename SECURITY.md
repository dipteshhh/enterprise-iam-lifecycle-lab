# Security and publication policy

Use this repository only with isolated, authorized lab resources and synthetic identities. Northstar Health is fictional. No patient data, real employee records, production tenants or production administrative access belong here.

Before staging a file, inspect it for passwords, tokens, OAuth secrets, cookies, private keys, database credentials, internal identifiers and proprietary assets. Inspect XML attributes, JDBC URLs, debug output, screenshots and Git history as well as obvious credential fields. `.gitignore` helps prevent accidents; it does not inspect content or remove previously committed secrets.

Use placeholders such as `YOUR_CLIENT_ID`, `YOUR_CLIENT_SECRET` and `YOUR_DATABASE_PASSWORD`. A value invented for an example must not be a usable password. Store actual credentials outside the repository, in an appropriate local secret store. A future `.env.example` must contain placeholders only.

Do not publish IdentityIQ WARs, licensed libraries, vendor-distributed documentation or raw application exports. Minimize logging: record decisions, counts and request references rather than complete identities, tokens, passwords or full provisioning plans. Review even synthetic-looking evidence for accidental real values.

Limit database connectors, service principals and workflow launch permissions to the operations required for the isolated test. Avoid using Oracle `DBA` as ordinary birthright access. Review approval, policy and audit behavior before using a custom provisioning path; a direct executor can bypass governance built into standard request workflows.

If a secret is exposed, revoke or rotate it first, stop publication and assess every copy including history. Deleting the visible line alone is insufficient. Do not report secrets in a public issue; contact the repository owner through a private channel already known to you. No private contact endpoint is invented here.

Repository checks are heuristic and do not constitute a penetration test, full secret scanner or compliance assessment. Product and dependency security must also be reviewed against the actual versions in use.
