-- Newly authored, read-only illustrative Oracle Database verification queries.
-- Run in the intended PDB/service through an already-authorized connection.
-- Do not publish raw output with real account names or environment identifiers.
-- USER_ROLE_PRIVS: roles granted to the connected user, not arbitrary employees.
-- Source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ROLE_PRIVS.html

SELECT SYS_CONTEXT('USERENV', 'SESSION_USER') AS session_user,
       SYS_CONTEXT('USERENV', 'CON_NAME') AS container_name
FROM dual;

SELECT granted_role, admin_option, default_role
FROM user_role_privs
ORDER BY granted_role;

-- Optional DBA verification (separate authorized verifier): remove comment
-- markers only if the account already has permission to query this view.
-- Replace the synthetic example with the exact tested native account identity.
-- No broad privileges should be granted solely to run this query.
-- SELECT grantee, granted_role, admin_option, default_role
-- FROM dba_role_privs
-- WHERE grantee = 'BILL_MURRAY'
-- ORDER BY granted_role;
