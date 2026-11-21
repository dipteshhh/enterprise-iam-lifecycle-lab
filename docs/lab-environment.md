# Reported lab environment

**Status: Historical environment evidence pending, with scoped runtime observations in E-004.** The table preserves the original reported baseline; the later observations below resolve selected facts, not vendor compatibility or every component.

| Component | Reported environment | Missing verification |
|---|---|---|
| Host | macOS, Apple Silicon | OS and architecture details not inspected |
| IGA | SailPoint IdentityIQ, locally deployed WAR | Exact IIQ version/build/patch unknown |
| Servlet container | Apache Tomcat 9 via Homebrew | Exact release, service configuration and support matrix unknown |
| Java | JDK 17 configured for Tomcat | Actual running service JVM not inspected |
| IIQ database | MySQL 8 | Exact release, driver and supported configuration unknown |
| UI | `http://localhost:8080/identityiq` | Not accessed during this repository task |
| Oracle practice target | Docker image `gvenzl/oracle-free:23-slim` | Actual image digest, CPU emulation and DB banner not inspected |
| DB clients | SQL*Plus and DBeaver | Versions not recorded |
| Cloud target | Microsoft Entra ID | Tenant/config/permissions not inspected |

The owner reported an Oracle AI Database Free release banner. Preserve the exact banner when evidence is collected; an image tag alone is not a complete version record. The third-party image is not an official Oracle support commitment, and an instructional Oracle 11g lab should not be assumed equivalent to this target.

## Service runtime troubleshooting history

Java compatibility issues led to setting `JAVA_HOME` and `JRE_HOME` and configuring the Homebrew `tomcat@9` service environment, then restarting and checking the service. No original service environment file is available. A shell's `java -version` does not establish which JVM an already running service uses.

For a future verification, record the IIQ build, consult that release's vendor installation/support documentation, inspect the actual Tomcat process JVM, and compare it with the intended service environment. Record changes and a sanitized startup log. Do not infer vendor support for JDK 17 from the fact it was used locally. Avoid broad upgrades until the IIQ release is known.

## Environment-specific logging locations

Historical paths, specific to this Homebrew setup:

```text
/opt/homebrew/opt/tomcat@9/libexec/webapps/identityiq/WEB-INF/classes/log4j2.properties
/opt/homebrew/var/log/sailpoint.log
```

The owner experimented with file appenders, root/named loggers, `loggerDex`, BeanShell/workflow logging and missing output. Check which configuration the service actually loaded, logger level and appender references, file permissions and service user before changing configuration. Restrict debug logging to a short isolated test and restore normal levels afterward. Full identity objects and plans may contain secrets or personal information.

## Later runtime observations

The [Oracle exercise](evidence/oracle-create-modify-2026-11-20.md) inspected installed IIQ **8.3 build f4b330b4da3-20220427-175259**, confirmed the running service JVM **17.0.21**, received HTTP 200 from the local endpoint and successfully tested the saved Oracle connector. The existing Docker target reported **Oracle AI Database 26ai Free Release 23.26.3.0.0**, with `FREEPDB1` read-write. The exact vendor-supported combination remains unconfirmed. HTTP 200 alone does not verify a UI login.

## Operational boundary

The initial foundation did not operate identity systems. The user subsequently authorized the bounded Oracle test, including the concrete account and narrow-role changes. That session started Docker Desktop, inspected the local installation, used the IIQ console and operated only the documented synthetic fixture/request scope. No Tomcat restart or installation-file edit was performed. See E-004 for retained objects, actual effects and cleanup. Vendor binaries, licensed JARs/WARs and confidential documentation remain excluded.

Use the [setup checklist](../sailpoint-identityiq/setup/README.md) and [evidence ledger](evidence/README.md) before attempting reproducibility.
