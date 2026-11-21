-- Isolated Oracle test fixture. Administrative preparation, not IIQ provisioning.
-- Fixed synthetic names; abort on collisions and errors. No reusable passwords.
whenever oserror exit failure
whenever sqlerror exit failure rollback
set echo off verify off feedback off heading off pagesize 0 linesize 220
alter session set container=FREEPDB1;
declare
  collisions number;
begin
  select count(*) into collisions from dba_users
   where username in ('NS_LAB_DATA_OWNER','NS_LAB_CREATE_01','NS_LAB_MODIFY_01');
  if collisions <> 0 then raise_application_error(-20001,'Synthetic account collision; stop'); end if;
  select count(*) into collisions from dba_roles where role='NS_LAB_REPORT_READER';
  if collisions <> 0 then raise_application_error(-20002,'Synthetic role collision; stop'); end if;
end;
/
create user NS_LAB_DATA_OWNER no authentication default tablespace USERS quota 1M on USERS;
alter user NS_LAB_DATA_OWNER account lock;
create table NS_LAB_DATA_OWNER.NS_LAB_PROBE
  (probe_id number primary key, sample_label varchar2(60) not null);
insert into NS_LAB_DATA_OWNER.NS_LAB_PROBE values (1,'SYNTHETIC NORTHSTAR LAB ROW');
commit;
create role NS_LAB_REPORT_READER;
grant select on NS_LAB_DATA_OWNER.NS_LAB_PROBE to NS_LAB_REPORT_READER;
declare
  generated_password varchar2(128);
begin
  generated_password := rawtohex(dbms_crypto.randombytes(24)) || 'aA9!';
  execute immediate 'create user NS_LAB_MODIFY_01 identified by "' || generated_password || '"';
  generated_password := null;
end;
/
grant create session to NS_LAB_MODIFY_01;
select 'SETUP_ACCOUNT='||username||';STATUS='||account_status from dba_users
 where username in ('NS_LAB_DATA_OWNER','NS_LAB_MODIFY_01');
select 'ROLE_OBJECT_PRIV='||role||';'||owner||'.'||table_name||';'||privilege||';GRANTABLE='||grantable
 from role_tab_privs where role='NS_LAB_REPORT_READER';
select 'ROLE_SYSTEM_PRIV_COUNT='||count(*) from role_sys_privs where role='NS_LAB_REPORT_READER';
select 'ROLE_NESTED_COUNT='||count(*) from role_role_privs where role='NS_LAB_REPORT_READER';
select 'CREATE_ACCOUNT_BEFORE='||count(*) from dba_users where username='NS_LAB_CREATE_01';
select 'TARGET_ROLE_GRANTS_BEFORE='||count(*) from dba_role_privs
 where grantee in ('NS_LAB_CREATE_01','NS_LAB_MODIFY_01') and granted_role='NS_LAB_REPORT_READER';
exit
