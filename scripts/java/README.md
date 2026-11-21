# Standalone Java username exercise

**Provenance:** newly authored illustrative code. This is separate from the owner's historical Java/BeanShell exercises. It contains no SailPoint, Entra, or Oracle dependencies and performs no provisioning. Its local tests establish algorithm behavior only.

## Objective and business requirement

Model Northstar Health's proposed first-initial-plus-surname username policy: Sarah Miller becomes `smiller`. Before writing a custom IIQ rule, assess the connector's supported out-of-the-box policy/configuration. This exercise makes naming-policy decisions visible without assuming a universal account-name specification.

## Inputs, output, and policy

`UsernameGenerator.generate(firstName, lastName, occupiedNames, maxLength)` returns a proposed string. It requires both names, a non-null snapshot of occupied names, and a length from 2 through 64. It lowercases with `Locale.ROOT`, strips ASCII spaces/apostrophes/hyphens from names, and matches occupied usernames case-insensitively. A collision receives the first available numeric suffix starting at 2.

It rejects digits, non-ASCII letters, missing values, and names/suffixes that exceed the limit without truncation. These rejections are an explicitly limited teaching policy; real naming must accommodate international names through an approved normalization/manual-review policy. The maximum is a function parameter, not a claim about AD, Entra, email, or Oracle limits. A candidate is not a reserved account name.

## Prerequisites and procedure

Use a JDK with Java 17 source support. No licensed vendor libraries are required. From the repository root:

```sh
mkdir -p /tmp/northstar-username-classes
javac --release 17 -d /tmp/northstar-username-classes scripts/java/UsernameGenerator.java scripts/java/UsernameGeneratorTest.java
java -cp /tmp/northstar-username-classes UsernameGeneratorTest
```

The temporary directory is outside the repository so compiled files cannot be mistaken for source deliverables. Do not commit `.class` files. Inspect the source before running; neither file reads environment variables or credentials.

## Test procedure and actual result

The dependency-free test program covers normal naming, case/whitespace collisions, numeric suffixes, punctuation, compound surnames, null/blank/unsupported inputs, length failures, nonmutation of the supplied set, and locale-independent lowercasing. A failing check raises `AssertionError` or an unexpected exception and exits unsuccessfully.

Local validation on 2026-11-20 used the available JDK 23 compiler with `--release 17` and JDK 23 runtime: **19 checks passed**. This establishes Java 17-targeted compilation and local algorithm checks; it is not a test on a JDK 17 runtime, a BeanShell parser, IIQ, or a live directory. No SailPoint installation was accessed.

## Security, limitations, and next improvements

The caller must obtain a fresh authorized directory snapshot. Simultaneous requests can choose the same name: uniqueness needs an atomic reservation or authoritative target check, neither implemented here. Do not turn a snapshot algorithm into a concurrency guarantee. Rehire rules, renamed employees, multiple account types, reserved words, UPN suffixes, domain validation, connector-specific character limits, and international naming remain unresolved.

Next: agree a written naming policy and collision/rehire rules; verify native target constraints; then validate built-in configuration in an isolated lab. If a custom rule is justified, port and test it using the installed IIQ rule signature. See the [rule collection](../../sailpoint-identityiq/rules/README.md).
