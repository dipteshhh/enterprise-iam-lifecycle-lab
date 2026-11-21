# Maintaining this lab

This is an independently developed portfolio by Diptesh Shahi Thakuri. New examples, including assisted examples, require review and local validation before being described as tested lab implementations.

1. Start from the [status register](docs/implementation-status.md). State whether a change is an original artifact, a reconstruction from lab history, or a newly authored illustrative example.
2. Use the [lab template](docs/lab-template.md). Keep observed results separate from expected behavior. Link evidence when advancing a capability to Verified.
3. Store executable examples once, beside their platform documentation. Shared standalone Java, SQL and Python belong in `scripts/`; platform pages link to those canonical files. Do not copy the same rule into several directories.
4. Use fictional data and reserved example email domains such as `example.org` or `.example`. Review exports and screenshots before staging; follow [SECURITY.md](SECURITY.md). Never commit vendor software, licensed JARs, WARs or full unreviewed application exports.
5. Record product version, connector version, task options, relevant configuration and source-document version. Documentation for another release is a reference, not compatibility evidence.
6. Run `python3 scripts/python/validate_repository.py` from the repository root. Run the Java exercise instructions if Java changes. Review `git diff --check` and the staged diff, including additions.
7. Update [CHANGELOG.md](CHANGELOG.md), the status register and the relevant evidence record. Keep a single next practical exercise in the [roadmap](docs/learning-roadmap.md).

Use a branch for each experiment. Preserve failed outcomes and their diagnosis without exposing credentials or private identity data. Do not force-push shared history or import experimental workflows into connected systems without a separate operational decision.

The MIT license covers original material contributed here; it grants no rights to SailPoint or other vendors' software and documentation.
