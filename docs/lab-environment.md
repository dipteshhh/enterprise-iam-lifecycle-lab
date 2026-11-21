# Reported lab environment

**Status: Previously Completed, Evidence Pending.** Source: owner's lab history (E-002). This document records that environment; it is not a portable installation guide or compatibility certification.

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

## Operational boundary

This repository task has not edited the installation, restarted Tomcat, run Docker, contacted localhost or changed a connected identity system. All runtime procedures are instructions for a separately authorized lab session. Vendor binaries, licensed JARs/WARs and confidential documentation are excluded from this repository.

Use the [setup checklist](../sailpoint-identityiq/setup/README.md) and [evidence ledger](evidence/README.md) before attempting reproducibility.
