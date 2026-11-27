-- Read-only verification for synthetic Northstar Health Leaver Lab accounts.
-- Newly authored from the supplied query examples; not captured test output.
-- Use an independently authorized dictionary-read connection to the correct PDB.
-- Quoted mixed-case usernames require the exact case in these string predicates.
-- Do not grant broad database privileges merely to run these queries.
-- No rows is not a substitute for verifying account identity and query success.

SELECT SYS_CONTEXT('USERENV', 'SESSION_USER') AS verifier,
       SYS_CONTEXT('USERENV', 'CON_NAME') AS container_name
FROM dual;

-- Alex Jones: reported account state changed OPEN -> LOCKED.
SELECT username, account_status
FROM dba_users
WHERE username = 'Alex_Jones';

SELECT grantee, granted_role
FROM dba_role_privs
WHERE grantee = 'Alex_Jones'
ORDER BY granted_role;

SELECT grantee, privilege, admin_option
FROM dba_sys_privs
WHERE grantee = 'Alex_Jones'
ORDER BY privilege;

-- Sarah Miller: reported locked account and five associated role grants revoked.
-- No broader zero-system-privilege claim was supplied for this scenario.
SELECT username, account_status
FROM dba_users
WHERE username = 'Sarah_Miller';

SELECT grantee, granted_role
FROM dba_role_privs
WHERE grantee = 'Sarah_Miller'
ORDER BY granted_role;

SELECT grantee, privilege, admin_option
FROM dba_sys_privs
WHERE grantee = 'Sarah_Miller'
ORDER BY privilege;

-- John Doe: both direct-grant queries reportedly returned zero rows.
-- Account locking is expected; separate account-status output was not supplied.
SELECT username, account_status
FROM dba_users
WHERE username = 'John_Doe';

SELECT grantee, granted_role
FROM dba_role_privs
WHERE grantee = 'John_Doe'
ORDER BY granted_role;

SELECT grantee, privilege, admin_option
FROM dba_sys_privs
WHERE grantee = 'John_Doe'
ORDER BY privilege;

-- Summary retains all three requested names, even if a database user is missing.
-- Zero direct-grant counts plus account_exists=0 is NOT a successful lock check.
-- Zero counts do not establish absence of PUBLIC/object/effective/session access.
WITH subjects (username) AS (
    SELECT 'Alex_Jones' FROM dual
    UNION ALL SELECT 'Sarah_Miller' FROM dual
    UNION ALL SELECT 'John_Doe' FROM dual
)
SELECT s.username,
       (SELECT COUNT(*) FROM dba_users u
        WHERE u.username = s.username) AS account_exists,
       (SELECT u.account_status FROM dba_users u
        WHERE u.username = s.username) AS account_status,
       (SELECT COUNT(*) FROM dba_role_privs r
        WHERE r.grantee = s.username) AS direct_role_count,
       (SELECT COUNT(*) FROM dba_sys_privs p
        WHERE p.grantee = s.username) AS direct_system_privilege_count
FROM subjects s
ORDER BY s.username;
