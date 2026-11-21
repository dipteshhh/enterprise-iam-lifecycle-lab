-- Newly authored illustrative MySQL 8 fixture; not an original lab export.
-- Inspect before running. Use a disposable MySQL instance and a setup account.
-- example_db must not exist. STOP ON FIRST ERROR; never use --force or continue-on-error.
-- CREATE errors alone do not prevent later INSERTs in clients that continue.
-- No DROP/TRUNCATE or credential statements are included.
-- CREATE TABLE intentionally fails if an employees table already exists.

CREATE DATABASE example_db CHARACTER SET utf8mb4;
USE example_db;

CREATE TABLE employees (
    employeeID VARCHAR(32) NOT NULL PRIMARY KEY,
    firstName VARCHAR(100) NOT NULL,
    lastName VARCHAR(100) NOT NULL,
    fullName VARCHAR(220) NOT NULL,
    email VARCHAR(254),
    phoneNumber VARCHAR(32),
    jobTitle VARCHAR(150)
);

INSERT INTO employees
    (employeeID, firstName, lastName, fullName, email, phoneNumber, jobTitle)
VALUES
    ('100', 'Ann', 'Parson', 'Ann Parson', 'ann.parson@example.org', '+1-202-555-0100', 'IT Manager'),
    ('200', 'Bob', 'Fields', 'Bob Fields', 'bob.fields@example.org', '+1-202-555-0101', 'Support Analyst'),
    ('300', 'Bill', 'Murray', 'Bill Murray', 'bill.murray@example.org', '+1-202-555-0102', 'Database Analyst'),
    ('401', 'Mitch', 'Armstrong', 'Mitch Armstrong', 'mitch.armstrong@example.org', '+1-202-555-0103', 'Reporting Analyst'),
    ('500', 'Sarah', 'Miller', 'Sarah Miller', 'sarah.miller@example.org', '+1-202-555-0104', 'Clinical Coordinator');

-- Expected count: 5 on a fresh successful run. This is an expectation, not output.
SELECT COUNT(*) AS employee_count FROM employees;
SELECT employeeID, firstName, lastName, fullName, email, phoneNumber, jobTitle
FROM employees
ORDER BY employeeID;

-- Expected empty result if fixture IDs are unique.
SELECT employeeID, COUNT(*) AS occurrences
FROM employees
GROUP BY employeeID
HAVING COUNT(*) > 1;
