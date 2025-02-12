# Database Management Systems

# Lab Practicals

Tested on 10.6.18-MariaDB-0ubuntu0.22.04.1 except Question 4 which will be written with MySQL 8.0.37 in mind

Question 8 onwards, we are using Oracle Databases since we need to use PL/SQL. I know, I feel the same way😿
Question 12 was answered on [Oracle's LiveSQL](https://livesql.oracle.com/)
Version: `Live SQL 24.1.3, running Oracle Database 19c EE Extreme Perf - 19.17.0.0.0`

> [!IMPORTANT]
> Question 1 to 7 is done using **MySQL 8.0 Command Line Client**. [Tested and reviewed]  
> Question 8 to 12 is done using **Run SQL Command Line**. [Tested and reviewed]

Program 10 is skipped(PL/SQL cursor)

## Program 1: Execute Single line Query and Group Functions.
###	Create a table INVENTORY with the following attributes(Item_No,Item_Name,Price).

```SQL
CREATE TABLE inventory(item_no varchar(10) PRIMARY KEY, item_name varchar(20), price decimal(10,2));
```

- ✅ MySQL returned an empty result set (i.e. zero rows). (Query took 0.0015 seconds.)

###	Insert five tuples in the table INVENTORY. 
(Doing only 2, same concept)

```SQL
INSERT INTO inventory VALUES('L101', 'Laptop', 50000);
```

- ✅  1 row inserted. (Query took 0.0003 seconds.)

```SQL
INSERT INTO inventory VALUES('L102', 'Computer', 100000);
```

- ✅ 1 row inserted. (Query took 0.0002 seconds.)

###	Display all the tuples from the INVENTORY Table.

```SQL
SELECT * FROM inventory;
```

- ✅ Showing rows 0 - 1 (2 total, Query took 0.0002 seconds.)

###	Perform single line query operations using group functions.

```SQL
SELECT COUNT(*) number_of_items from inventory;
```

| number_of_items |
|-----------------|
| 2               |

- ✅ Your SQL query has been executed successfully.

```SQL
SELECT MAX(price) maximum_price FROM inventory;
```

| maximum_price |
|---------------|
| 100000.00     |

- ✅ Showing rows 0 - 0 (1 total, Query took 0.0002 seconds.)

```SQL
SELECT MIN(price) minimum_price FROM inventory;
```

| minimum_price |
|---------------|
| 50000.00      |

- ✅ Showing rows 0 - 0 (1 total, Query took 0.0002 seconds.)

```SQL
SELECT AVG(price) avg_amount FROM inventory;
```

| avg_amount    |
|---------------|
| 75000.000000  |

- ✅ Showing rows 0 - 0 (1 total, Query took 0.0001 seconds.)

```SQL
SELECT SUM(price) total_amount FROM inventory;
```

| total_amount  |
|---------------|
| 150000.00     |

- ✅ Showing rows 0 - 0 (1 total, Query took 0.0001 seconds.)


## Program 2: Execute DDL Commands.
### Create table STUDENT with the following attributes(Register_no, Name, Mark_1,Mark_2,Mark_3).

```SQL
CREATE TABLE student(register_no varchar(10) PRIMARY KEY, name varchar(20), mark_1 int, mark_2 int, mark_3 int);
```

- ✅ MySQL returned an empty result set (i.e. zero rows). (Query took 0.0003 seconds.)

```SQL
DESC student;
```

- ✅ Your SQL query has been executed successfully.

| Field       | Type        | Null | Key | Default | Extra |
|-------------|-------------|------|-----|---------|-------|
| register_no | varchar(10) | NO   | PRI | NULL    |       |
| name        | varchar(20) | YES  |     | NULL    |       |
| mark_1      | int(11)     | YES  |     | NULL    |       |
| mark_2      | int(11)     | YES  |     | NULL    |       |
| mark_3      | int(11)     | YES  |     | NULL    |       |

### Add new columns(Total, Average) to the table STUDENT.

```SQL
ALTER TABLE student add(total int, average decimal(7,2));
```

- ✅ MySQL returned an empty result set (i.e. zero rows). (Query took 0.0003 seconds.)

```SQL
desc student;
```

- ✅ Your SQL query has been executed successfully.

| Field       | Type         | Null | Key | Default | Extra |
|-------------|--------------|------|-----|---------|-------|
| register_no | varchar(10)  | NO   | PRI | NULL    |       |
| name        | varchar(20)  | YES  |     | NULL    |       |
| mark_1      | int(11)      | YES  |     | NULL    |       |
| mark_2      | int(11)      | YES  |     | NULL    |       |
| mark_3      | int(11)      | YES  |     | NULL    |       |
| total       | int(11)      | YES  |     | NULL    |       |
| average     | decimal(7,2) | YES  |     | NULL    |       |

### Rename the table STUDENT to  STUDENT_T1.

```SQL
RENAME TABLE student to student_t1;
```

- ✅ MySQL returned an empty result set (i.e. zero rows). (Query took 0.0004 seconds.)

### Truncate the table STUDENT_T1.

```SQL
TRUNCATE TABLE student_t1;
```

- ✅ MySQL returned an empty result set (i.e. zero rows). (Query took 0.0003 seconds.)

### Drop the table STUDENT_T1.

```SQL
DROP TABLE student_t1;
```

- ✅ MySQL returned an empty result set (i.e. zero rows). (Query took 0.0003 seconds.)


## Program 3: Execute DML Commands.
### Create table STUDENT with the following attributes(Register_No, Name, Mark_1, Mark_2, Mark_3,Total,Average).

```SQL
CREATE TABLE student002(register_no varchar(10) PRIMARY KEY, name varchar(20), mark_1 int, mark_2 int, mark_3 int, total int, average decimal(7,2));
```

- ✅ MySQL returned an empty result set (i.e. zero rows). (Query took 0.0004 seconds.)

```SQL
DESC student002;
```

- ✅ Your SQL query has been executed successfully.

| Field       | Type         | Null | Key | Default | Extra |
|-------------|--------------|------|-----|---------|-------|
| register_no | varchar(10)  | NO   | PRI | NULL    |       |
| name        | varchar(20)  | YES  |     | NULL    |       |
| mark_1      | int(11)      | YES  |     | NULL    |       |
| mark_2      | int(11)      | YES  |     | NULL    |       |
| mark_3      | int(11)      | YES  |     | NULL    |       |
| total       | int(11)      | YES  |     | NULL    |       |
| average     | decimal(7,2) | YES  |     | NULL    |       |

### Insert five tuples in the table STUDENT.(Make sure average and total fields are NULL).
(Doing only 2, same concept)

```SQL
INSERT INTO student002 VALUES('S101', 'charles', 99, 100, 95, null, null);
```
(If the above code doesn't work, try this:)
```SQL
INSERT INTO student002 VALUES('S101', 'charles', 99, 100, 95);
```

- ✅ 1 row inserted. (Query took 0.0008 seconds.)

```SQL
INSERT INTO student002 VALUES('S102', 'abdul', 100, 99, 100, null, null);
```
(If the above code doesn't work, try this:)
```SQL
INSERT INTO student002 VALUES('S102', 'abdul', 100, 99, 100);
```
- ✅ 1 row inserted. (Query took 0.0001 seconds.)

### Display all the tuples from the table STUDENT.

```SQL
SELECT * FROM student002;
```

- ✅ Showing rows 0 - 1 (2 total, Query took 0.0002 seconds.)

| register_no | name    | mark_1 | mark_2 | mark_3 | total | average |
|-------------|---------|--------|--------|--------|-------|---------|
| S101        | charles | 99     | 100    | 95     | NULL  | NULL    |
| S102        | abdul   | 100    | 99     | 100    | NULL  | NULL    |

### Find the Total and AVERAGE AND UPDATE TO THE TABLE student.
- Total=(Mark_1 + Mark_2 + Mark_3)
- Average=(Mark_1+Mark_2+Mark_3)/3.

```SQL
UPDATE student002 SET total=(mark_1+mark_2+mark_3),average=(mark_1+mark_2+mark_3)/3;
```

- ✅ 2 rows affected. (Query took 0.0003 seconds.)

```SQL
SELECT * FROM student002;
```

- ✅ Showing rows 0 - 0 (1 total, Query took 0.0002 seconds.)

| register_no | name   | mark_1 | mark_2 | mark_3 | total | average |
|-------------|--------|--------|--------|--------|-------|---------|
| S101        | charles|   99   |   100  |    95  |   294 |    98.00|
| S102        | abdul  |   100  |    99  |   100  |   299 |    99.67|

### Delete a tuple from the table STUDENT.

```SQL
DELETE FROM student002 WHERE register_no='S101';
```

- ✅ 1 row deleted. (Query took 0.0003 seconds.)

```SQL
SELECT * FROM student002;
```
- ✅ Showing rows 0 - 0 (1 total, Query took 0.0002 seconds.)

| register_no | name   | mark_1 | mark_2 | mark_3 | total | average |
|-------------|--------|--------|--------|--------|-------|---------|
| S102        | abdul  |   100  |    99  |   100  |   299 |    99.67|


## Program 4: Execute DCL and TCL Commands.
### Connect the database using the command line window.

```SQL
CONNECT souhrud_practical;
```

- ✅ MySQL returned an empty result set (i.e. zero rows). (Query took 0.0001 seconds.)

### Create a table PURCHASE with the following attributes (Item_No, Item_Name,Price).

```SQL
CREATE TABLE purchase(item_no varchar(4), item_name varchar(20), price decimal(10,2));
```
- ✅ MySQL returned an empty result set (i.e. zero rows). (Query took 0.0085 seconds.)

### Insert two tuples in the PURCHASE.

```SQL
INSERT INTO purchase VALUES("L101", "laptop", 50000);
```

- ✅ 1 row inserted. (Query took 0.0011 seconds.)

```SQL
INSERT INTO purchase VALUES("L102", "desktop", 100000);
```

- ✅ 1 row inserted. (Query took 0.0011 seconds.)

### Create a user with (User name: customer,Password:sales).

```SQL
CREATE USER 'customer'@'localhost' IDENTIFIED BY 'sales';
```
(If the above code doesn't work, try this:)
```SQL
CREATE USER 'customer' IDENTIFIED BY 'sales';
```

- ✅ Query OK, 0 rows affected (0.16 sec)

### Perform DCL command operations using the table PURCHASE.

```SQL
GRANT ALL ON souhrud_practical.* TO 'customer'@'localhost';
```

- ✅ Query OK, 0 rows affected (0.12 sec)


## Program 5: Implement the Nested Queries.
### Create a table TEACHER with the following attributes(Tid,Tanme,Deptid).

```SQL
CREATE TABLE teacher(tid int(4) PRIMARY KEY, tname varchar(20), deptid varchar(3));
```

- ✅ Query OK, 0 rows affected, 1 warning (0.03 sec)

### Insert two tuples in the table TEACHER.

```SQL
INSERT INTO teacher VALUES(1001, 'charles', 'D11');
```

- ✅ Query OK, 1 row affected (0.01 sec)

```SQL
INSERT INTO teacher VALUES(1002, 'abdul', 'D12');
```

- ✅ Query OK, 1 row affected (0.01 sec)

Now, output it
```SQL
select * from teacher;
```

- ✅ 2 rows in set (0.00 sec)

| tid  | tname   | deptid |
|------|---------|--------|
| 1001 | charles | D11    |
| 1002 | abdul   | D12    |

### Create a table DEPARTMENT with the following attributes(Deptid,Dname).

```SQL
CREATE TABLE department(deptid varchar(10), dname varchar(20));
```

- ✅ Query OK, 0 rows affected (0.28 sec)

Check the attributes
```SQL
DESC department;
```

- ✅ 2 rows in set (0.17 sec)

### Insert three tuples into the DEPARTMENT Table.

```SQL
INSERT INTO department VALUES('D11','computer science'),('D15','physics'),('D13', 'maths');
```

- ✅ Query OK, 3 rows affected (0.06 sec)
  Records: 3  Duplicates: 0  Warnings: 0

Now, check the output:
```SQL
SELECT * FROM department;
```

- ✅ 3 rows in set (0.00 sec)

| deptid | dname            |
|--------|------------------|
| D11    | computer science  |
| D15    | physics          |
| D13    | maths            |

### Perform nested queries using the table TEACHER and DEPARTMENT.

```SQL
SELECT * FROM teacher WHERE deptid IN(SELECT deptid FROM department WHERE teacher.deptid=department.deptid);
```

- ✅ 1 row in set (0.04 sec)

| tid  | tname   | deptid |
|------|---------|--------|
| 1001 | charles | D11    |


## Program 6: Implement Join Operations in SQL.
### Create a table EMPLOYEE with the following attributes(Emp_id, Emp_name,Edept_id).

```SQL
CREATE TABLE employee(emp_id int PRIMARY KEY, emp_name varchar(20), edept_id int);
```

- ✅ Query OK, 0 rows affected (0.14 sec)

### Insert three tuples in the table EMPLOYEE.

```SQL
INSERT INTO employee VALUES(1001, 'charles', 10), (1002, 'abdul', 30), (1003, 'rohan', 30);
```

- ✅ Query OK, 3 rows affected (0.05 sec)
Records: 3  Duplicates: 0  Warnings: 0

### Create a table DEPARTMENT with the following attributes(Dept_id,Dept_name).

```SQL
CREATE TABLE department(dept_id int PRIMARY KEY, dept_name varchar(20));
```

- ✅ Query OK, 0 rows affected (0.17 sec)

### Enter Four tuples in the table DEPARTMENT.

```SQL
INSERT INTO department VALUES(10, 'accounts'), (20, 'design'), (40, 'testing'), (50, 'purchase');
```

- ✅ Query OK, 4 rows affected (0.04 sec)
Records: 4  Duplicates: 0  Warnings: 0

### Perform join Operations using the table EMPLOYEE and DEPARTMENT.

#### Inner Join:
```SQL
SELECT emp_id, emp_name, edept_id, dept_name FROM employee INNER JOIN department ON employee.edept_id=department.dept_id;
```

- ✅ 1 row in set (0.00 sec)

| emp_id | emp_name | edept_id | dept_name |
|--------|----------|----------|-----------|
|   1001 | charles  |       10 | accounts  |

#### Left Outer Join: 
```SQL
SELECT emp_id, emp_name, edept_id, dept_name FROM employee LEFT JOIN department ON employee.edept_id=department.dept_id;
```

- ✅ 3 rows in set (0.00 sec)

| emp_id | emp_name | edept_id | dept_name |
|--------|----------|----------|-----------|
|   1001 | charles  |       10 | accounts  |
|   1002 | abdul    |       30 | NULL      |
|   1003 | rohan    |       30 | NULL      |

#### Right Outer Join:
```SQL
SELECT emp_id, emp_name, edept_id, dept_name FROM employee RIGHT JOIN department ON employee.edept_id=department.dept_id;
```

- ✅ 4 rows in set (0.00 sec)

| emp_id | emp_name | edept_id | dept_name |
|--------|----------|----------|-----------|
|   1001 | charles  |       10 | accounts  |
|   NULL | NULL     |     NULL | design    |
|   NULL | NULL     |     NULL | testing   |
|   NULL | NULL     |     NULL | purchase  |

#### Full Join: 
```SQL
SELECT emp_id, emp_name, edept_id, dept_name FROM employee LEFT JOIN department ON employee.edept_id=department.dept_id UNION SELECT emp_id, emp_name, edept_id, dept_name FROM employee RIGHT JOIN department ON employee.edept_id=department.dept_id;
```

- ✅ 6 rows in set (0.02 sec)

| emp_id | emp_name | edept_id | dept_name |
|--------|----------|----------|-----------|
|   1001 | charles  |       10 | accounts  |
|   1002 | abdul    |       30 | NULL      |
|   1003 | rohan    |       30 | NULL      |
|   NULL | NULL     |     NULL | design    |
|   NULL | NULL     |     NULL | testing   |
|   NULL | NULL     |     NULL | purchase  |


## Program 7: Create a view for a particular table.
### Create a table TRAIN (Train_no,Train_Nmae,Source,Destination).
```SQL
CREATE TABLE train(train_no int PRIMARY KEY, train_name varchar(20), source varchar(20), destination varchar(20)); 
```

- ✅ Query OK, 0 rows affected (0.16 sec)

### Insert three tuples in the table TRAIN.
```SQL
INSERT INTO train VALUES (50001, 'malgudi exp', 'bengaluru', 'mysuru'), (50002,'karnataka exp','bengaluru','new delhi'), (50003,'shatabdi exp','bengaluru','chennai'); 
```

- ✅ Query OK, 3 rows affected (0.05 sec)
Records: 3  Duplicates: 0  Warnings: 0

### Display all the tuples from the table TRAIN.
```SQL
SELECT * FROM train; 
```

- ✅ 3 rows in set (0.00 sec)

| train_no | train_name      | source    | destination |
|----------|-----------------|-----------|-------------|
|    50001 | malgudi exp     | bengaluru | mysuru      |
|    50002 | karnataka exp   | bengaluru | new delhi   |
|    50003 | shatabdi exp    | bengaluru | chennai     |

### Perform view operations using the table TRAIN.
```SQL
CREATE VIEW display_view AS SELECT * FROM train; 
```

- ✅ Query OK, 0 rows affected (0.06 sec)

Display Train View
```SQL
 SELECT * FROM display_view;
```

- ✅ 3 rows in set (0.00 sec)

| train_no | train_name      | source    | destination |
|----------|-----------------|-----------|-------------|
|    50001 | malgudi exp     | bengaluru | mysuru      |
|    50002 | karnataka exp   | bengaluru | new delhi   |
|    50003 | shatabdi exp    | bengaluru | chennai     |

```SQL
INSERT INTO display_view VALUES(50004,'kochuveli exp', NULL, NULL); 
```

- ✅ Query OK, 1 row affected (0.05 sec)

Display Train View after Operation
```SQL
SELECT * FROM display_view; 
```

- ✅ 4 rows in set (0.00 sec)

| train_no | train_name      | source    | destination |
|----------|-----------------|-----------|-------------|
|    50001 | malgudi exp     | bengaluru | mysuru      |
|    50002 | karnataka exp   | bengaluru | new delhi   |
|    50003 | shatabdi exp    | bengaluru | chennai     |
|    50004 | kochuveli exp   | NULL      | NULL        |

Add data to 50004 train
```SQL
UPDATE train set source='bengaluru', destination='kochuveli' WHERE train_no=50004; 
```

- ✅ Query OK, 1 row affected (0.08 sec)
Rows matched: 1  Changed: 1  Warnings: 0

Output the result
```SQL
SELECT * FROM display_view;
``` 

- ✅ 4 rows in set (0.00 sec)

| train_no | train_name      | source    | destination |
|----------|-----------------|-----------|-------------|
|    50001 | malgudi exp     | bengaluru | mysuru      |
|    50002 | karnataka exp   | bengaluru | new delhi   |
|    50003 | shatabdi exp    | bengaluru | chennai     |
|    50004 | kochuveli exp   | bengaluru | kochuveli   |


## Program 8: Implement Locks for a particular table.
### Connect the database using the command line window.

```SQL
CONNECT system;
```

- ✅ Connected.

### Create table CAR with the following attributes(Model_No, Brand,Price).

```SQL
CREATE TABLE car(Model_No VARCHAR(5) PRIMARY KEY, Brand VARCHAR(20), Price DECIMAL(10,2));
```

- ✅ Table created.

### Insert five tuples in the table CAR.

```SQL
INSERT INTO car VALUES('H1001','Hyundai', 1000000);
INSERT INTO car VALUES('H1002','Maruti', 800000);
INSERT INTO car VALUES('H1003','Tata', 700000);
INSERT INTO car VALUES('H1004','Honda', 600000);
INSERT INTO car VALUES('H1005','Mahindra', 500000);
```

- ✅ 5 row created.

### Create a user with (User name: Owner, Password:car) and grant the select, update permission.

```SQL
CREATE USER owner IDENTIFIED BY car;
```

- ✅ User created.

```SQL
GRANT CONNECT TO owner;
```

- ✅ Grant succeeded.

```SQL
GRANT SELECT ON car TO owner;
```

- ✅ Grant succeeded.

```SQL
GRANT UPDATE ON car TO owner;
```

- ✅ Grant succeeded.

```SQL
UPDATE car SET Price=1000000 WHERE Model_No='H1001';
```

- ✅ 1 row updated.

```SQL
commit;
```

- ✅ Commit complete.

### Implement the Locks using the table CAR.

```SQL
LOCK TABLE car IN EXCLUSIVE MODE;
```

- ✅ Table(s) Locked.

## Program 9: Write PL/SQL Procedure for an application using exception handling.
### Create a table BANK with the following attributes(Acno, Name,Balance).

```SQL
CREATE TABLE bank(acno int primary key, name varchar(20), balance decimal(10,2));
```

### Insert two tuples in the table BANK.

```SQL
INSERT INTO bank VALUES(0001, 'Souhrud', 20);
INSERT INTO bank VALUES(0002, 'Joel', 30);
```

### Display all the tables from the table BANK.

```SQL
SELECT * FROM bank;
```

ACNO | NAME     | BALANCE |
-----|----------|---------|
1    | Souhrud  | 20      |
2    | Joel     | 30      |

### Perform exception handling using the table BANK.

```SQL
SET SERVEROUTPUT ON;
```

```SQL
DECLARE
  cacno bank.acno%TYPE;
  cname bank.name%TYPE;
  cbalance bank.balance%TYPE;	
BEGIN
  SELECT acno, name, balance INTO cacno, cname, cbalance 
  FROM bank 
  WHERE acno = 0001;
  
  DBMS_OUTPUT.PUT_LINE(REPLACE(cacno || '    ' || cname || '   ' || cbalance, CHR(10), ''));
EXCEPTION
  WHEN NO_DATA_FOUND THEN
    DBMS_OUTPUT.PUT_LINE('no such customer');
  WHEN OTHERS THEN
    DBMS_OUTPUT.PUT_LINE('Error');
END;
/
```

### Output: 

```
1   Souhrud  20
```

- ✅ PL/SQL procedure successfully completed.

## Program 10: Write PL/SQL procedure for an application using a cursor.(skip)
### Create a table BANK with the following attributes(Acno, Name,Balance).

```SQL
CREATE TABLE bank(acno int primary key, name varchar(20), balance decimal(10,2));
```
### Insert two tuples in the table BANK.

```SQL
INSERT INTO bank VALUES(0001, 'Souhrud', 20);
INSERT INTO bank VALUES(0002, 'Joel', 30);
```

### Display all the tuples from the table BANK.

```SQL
SELECT * FROM bank;
```

ACNO | NAME     | BALANCE |
-----|----------|---------|
1    | Souhrud  | 20      |
2    | Joel     | 30      |

### Display all the tuples from the table BANK using cursor.

```SQL
SET SERVEROUTPUT ON;
```

```SQL
DECLARE
cacno bank.acno%type;
cname bank.name%type;
cbalance bank.balance%type;
CURSOR cbank is
SELECT acno,name,balance FROM bank;
BEGIN
dbms_output.put_line('Account no.   '||'Name    '||'Balance');
dbms_output.put_line('==================================');
OPEN cbank;
LOOP
FETCH cbank into cacno,cname,cbalance;
EXIT WHEN cbank%notfound;
dbms_output.put_line(cacno||'  '||cname||'    '||cbalance);
END LOOP;
CLOSE cbank;
END;
/
```

### Output:

```
Account no.   Name    Balance
==================================
1           Souhrud    20
2           Joel       30
```

- ✅ PL/SQL procedure successfully completed.


## Program 11: Write a PL/SQL procedure for an application using functions.
### Create a table LAPTOP with the following attributes(Model_No,Company_Name, Price).
```SQL
CREATE TABLE laptop(model_no varchar(5), company_name varchar(20), price decimal(10,2));
```
### Insert two tuples in the table LAPTOP.
```SQL
INSERT INTO laptop VALUES('L1001', 'dell', 50000); 
INSERT INTO laptop VALUES('L1002', 'hp', 40000);
```

### Display all the tuples in the table LAPTOP.
```SQL
SELECT * FROM laptop;
```

MODEL | COMPANY_NAME  | PRICE |
------|---------------|-------|
L1001 | dell          | 50000 |
L1002 | hp            | 40000 |

### Find the maximum price in the table LAPTOP using the function.

```SQL
SET SERVEROUTPUT ON;
```

```SQL
create or replace function maximum
return decimal IS
maxprice number(10,2):=0;
begin
select max(price)into maxprice from laptop;
return maxprice;
end;
/
```

- ✅ Function created.

```SQL
declare 
n number(10,2);
begin
n:=maximum();
dbms_output.put_line('maximum price='||n);
end;
/
```

### Output:
```
maximum price=50000
```

- ✅ PL/SQL procedure successfully completed.

## Program 12: Write a PL/SQL procedure for an application using a package.
### Create a table LIBRARY with the following attributes(Book_id, Book_name, B_price).
```SQL
CREATE TABLE library(Book_Id INT PRIMARY KEY, Book_Name VARCHAR(40), B_Price DECIMAL(20,2));
```

- ✅ Table created.

### Insert three tuples in the table LIBRARY.
```SQL
INSERT INTO library VALUES (1001,'C# and Dotnet',200);
INSERT INTO library VALUES (1002,'Computer Communication and Networks',250);
INSERT INTO library VALUES (1003,'Database Management System',250);
```

- ✅ 3 row(s) inserted.


### Display all the tuples from the table LIBRARY.
```SQL
SELECT * FROM library;
```

| BOOK_ID	| BOOK_NAME |	B_PRICE |
| --- | --- | --- |
| 1001 | C# and Dotnet | 200 |
| 1002 | Computer Communication and Networks | 250 |
| 1003  | Database Management System | 250 |

### Create a package using the table LIBRARY.
```SQL
CREATE OR REPLACE PACKAGE library_package IS
PROCEDURE ADD_NEW (B_Id VARCHAR,B_Name VARCHAR2,B_Price NUMBER);
FUNCTION DISPLAY RETURN VARCHAR2;
END library_package;
/
```

- ✅ Package created.

```SQL
CREATE OR REPLACE PACKAGE BODY library_package IS
PROCEDURE ADD_NEW (B_Id VARCHAR,B_Name VARCHAR2,B_Price NUMBER) IS
BEGIN
INSERT INTO library VALUES(B_Id,B_Name,B_Price);
END;
FUNCTION display RETURN VARCHAR2 IS
BEGIN
RETURN 'Recorded Inserted';
END display;
END library_package;
/
```

- ✅ Package body created.

```SQL
BEGIN
library_package.ADD_NEW('1004','OPP With JAVA',500);
dbms_output.PUT_LINE(library_package.display);
END;
/
```
- ✅ Recorded Inserted  
      PL/SQL procedure successfully completed.

Now, Output it:
```SQL
SELECT * FROM library;
```

| BOOK_ID | BOOK_NAME                                | B_PRICE |
|---------|------------------------------------------|---------|
| 1001    | C# and Dotnet                            | 200     |
| 1002    | Computer Communication and Networks      | 250     |
| 1003    | Database Management System               | 250     |
| 1004    | OPP With JAVA                            | 500     |


## Source:
- General Questions were found in Syllabus
- Specific Questions are from a documents shared in the whatsapp group.
