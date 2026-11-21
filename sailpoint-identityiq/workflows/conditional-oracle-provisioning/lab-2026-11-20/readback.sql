-- Independent dictionary readback for this exact isolated synthetic fixture.
whenever oserror exit failure
whenever sqlerror exit failure rollback
set echo off verify off feedback off heading off pagesize 0 linesize 240 trimspool on
alter session set container=FREEPDB1;
select 'CONTAINER|'||sys_context('USERENV','CON_NAME') from dual;
select 'ACCOUNT|'||username||'|'||account_status||'|'||authentication_type from dba_users
 where username in ('NS_LAB_CREATE_01','NS_LAB_MODIFY_01','NS_LAB_DATA_OWNER') order by username;
select 'ACCOUNT_COUNT|'||username||'|'||count(*) from dba_users
 where username in ('NS_LAB_CREATE_01','NS_LAB_MODIFY_01') group by username order by username;
select 'ROLE_GRANT|'||grantee||'|'||granted_role||'|ADMIN='||admin_option||'|DEFAULT='||default_role
 from dba_role_privs where grantee in ('NS_LAB_CREATE_01','NS_LAB_MODIFY_01','NS_LAB_REPORT_READER')
 order by grantee,granted_role;
select 'SYSTEM_GRANT|'||grantee||'|'||privilege||'|ADMIN='||admin_option from dba_sys_privs
 where grantee in ('NS_LAB_CREATE_01','NS_LAB_MODIFY_01','NS_LAB_REPORT_READER') order by grantee,privilege;
select 'OBJECT_GRANT|'||grantee||'|'||owner||'.'||table_name||'|'||privilege||'|GRANTABLE='||grantable
 from dba_tab_privs where grantee in ('NS_LAB_CREATE_01','NS_LAB_MODIFY_01','NS_LAB_REPORT_READER')
 order by grantee,owner,table_name,privilege;
select 'ROLE_SYSTEM_COUNT|'||count(*) from role_sys_privs where role='NS_LAB_REPORT_READER';
select 'ROLE_NESTED_COUNT|'||count(*) from role_role_privs where role='NS_LAB_REPORT_READER';
select 'PROBE_ROW_COUNT|'||count(*) from NS_LAB_DATA_OWNER.NS_LAB_PROBE;
exit
