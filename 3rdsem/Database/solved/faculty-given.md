---
order: 1
title: Database Faculty Questions
---
# Database Management Systems 
# Important Questions and Topics
# Unit 1:
## Q1. Database architecture
A DBMS (Database Management System) architecture refers to the overall design and organization of a DBMS, including the components, interfaces, and interactions between them. It provides a framework for managing and accessing data in a database.

[Javatpoint](https://www.javatpoint.com/dbms-architecture)

## Q2. Database Schema and Models

Database schema:
- The Skeleton of the database is created by the attributes and this skeleton is named Schema.
- Schema mentions the logical constraints like table, primary key, etc.
- The schema does not represent the data type of the attributes.

[GeeksForGeeks](https://www.geeksforgeeks.org/database-schemas/)

![Database schema Example](https://media.geeksforgeeks.org/wp-content/uploads/20230511011217/schema1drawio.png)

A Data Model in Database Management System (DBMS)  is the concept of tools that are developed to summarize the description of the database. Data Models provide us with a transparent picture of data which helps us in creating an actual database. It shows us from the design of the data to its proper implementation of data.

[GeeksForGeeks](https://www.geeksforgeeks.org/data-models-in-dbms/)
## Q3. Data Independence
Data independence is a property of a database management system by which we can change the database schema at one level of the database system without changing the database schema at the next higher level. 

It has two types:
- Physical Data Independence 
- Logical Data Independence

**Logical Data Independence**:
- Refers to the capacity to change the logical schema without altering the external schema or application programs.
- Changes may include adding new fields or tables.
- Allows users to interact with data without needing to modify their applications when the logical structure changes.

**Physical Data Independence**:
- Refers to the ability to change the physical schema without affecting the logical schema.
- Changes may involve altering storage devices, file formats, or indexing methods.
- Ensures that the logical structure remains stable even if the physical storage changes.

***Summary***:
- **Logical Independence**: Changes in the logical structure don't affect user applications.
- **Physical Independence**: Changes in physical storage don't affect the logical structure.

[GeeksForGeeks](https://www.geeksforgeeks.org/what-is-data-independence-in-dbms/)

## Q4. Database Languages
Database languages are special-purpose languages that help with tasks like data definition, manipulation, and control: 

- ***Data Definition Language (DDL)***: Used to define data types, create tables, and define relationships between them. DDL commands include CREATE, ALTER, DROP, TRUNCATE, and RENAME. 
- ***Data Manipulation Language (DML)***: Used to perform tasks like inserting, updating, or deleting data. DML commands include INSERT and UPDATE. 
- ***Data Control Language (DCL)***: Used to control access to data. DCL commands include GRANT and REVOKE. 
- ***Data Query Language (DQL)***: Used to search for information and compute derived information. 
Transaction Control Language (TCL): Used to run the changes made by the DML statement. TCL commands include COMMIT. 

![Types of DB Languages](https://files.codingninjas.in/article_images/database-languages-0-1650484671.webp)

[Naukri](https://www.naukri.com/code360/library/database-languages-in-dbms)
## Q5. Classification of DBMS
Types of DBMS
- ***Relational Database Management System (RDBMS)***: Data is organized into tables (relations) with rows and columns, and the relationships between the data are managed through primary and foreign keys. 
    - SQL (Structured Query Language) is used to query and manipulate the data.
- ***NoSQL DBMS***: Designed for high-performance scenarios and large-scale data
    - NoSQL databases store data in various non-relational formats such as key-value pairs, documents, graphs, or columns.
- ***Object-Oriented DBMS (OODBMS)***: Stores data as objects, similar to those used in object-oriented programming
    - It allows for complex data representations and relationships

[GeeksForGeeks](https://www.geeksforgeeks.org/introduction-of-dbms-database-management-system-set-1/)


# Unit 2:
## Q1. Construct a ER diagram for Company database,Student database.
- **Company Database**:
    ![Company ER](https://media.geeksforgeeks.org/wp-content/uploads/20200621171512/company.png)

- **Student Database**
    ![Student ER](https://www.simplilearn.com/ice9/free_resources_article_thumb/ERDiagramsInDBMS_1.png)

## Q2. Define Entity, Relationship and types of cardinality
An Entity is a real-world object, person, place or thing that we are representing in the database. 
- Eg. A car exists in the real world, and we can represent it in our database
- We can store data about such entities

A relationship in DBMS refers to the logical association between different entities that are stored in separate tables.
- Eg. Customers, products, and orders

Types of Cardinality/Relationship:
- ***One To One Relationship***
    - Consider two entities "Person" and "Aadhar card". Each person can have only one Aadhar card and each Aadhar card is assigned to only one person.
    -  ![One To One Relationship](https://media.geeksforgeeks.org/wp-content/uploads/20240607225720/pha.png)
- ***One-to-Many or Many-to-One Relationship***
    - Consider two entities "customer" and "order". Each customer can place multiple orders but each order is placed by only one customer.
    - ![One To N Relationship](https://media.geeksforgeeks.org/wp-content/uploads/20240607225819/cpo.png)
- ***Many-to-Many Relationship***
    - Consider two entities "Student" and "Course" where each student can enroll in multiple courses and each course can have multiple students enrolled in it. 
    - This relationship is mainly implemented using junction table. 
    - ![N to N Relationship](https://media.geeksforgeeks.org/wp-content/uploads/20240607225932/sec.png)
[GeeksForGeeks](https://www.geeksforgeeks.org/what-is-relationship-type-in-dbms/)
## Q3. Explain ER notations used in database Schema design.
ER Notations are used to represent various components of the ER Model, using different symbols.

![ER Notations](https://binaryterms.com/wp-content/uploads/2021/10/Entity-Relationship-Diagram-Symbols.jpg)


- Rectangles illustrate the entity set.
    - A Strong Entity Set only has a single border.
        - It is defined by its own set of attributes
    - A Weak Entity Set has two borders 
        - It is always associated with another Entity Set(which is called the Identifier Entity Set)
- Diamond illustrates the relationship between the entity set.
    - A Strong Relationship has a single border
        - Here, the Child Entity is completely dependent on the Parent Entity.
    - A Weak Relationship has two borders
        - A weak Relationship is where a child Entity can exist without the Parent Entity.
- Ellipse illustrates the attributes of an entity set.
    - A simple Attribute has a single outer border
        - It cannot be further divided into sub-parts. Example, *id* attribute
        - It is also known as a Single-Valued Attribute
    - A Multi-Valued Attribute has 2 outer borders
        - This means it has more than one value for a given entity.
            - Eg. *phone_number* may have multiple numbers stored
    - A Composite Attribute has subparts derived from it.
        - It can be broken down into subparts. Example, *name* can be broken down into *first_name* and *last_name* 
    - A Derived Attribute has a dotted border
        - It means the data in this attribute was derived from another attribute
            - For Example, *age* was Derived from *date_of_birth*
- Lines illustrate the association of attributes to the entity set and the association of entity set to the relationship set.

[BinaryTerms](https://binaryterms.com/entity-relationship-diagram.html)
## Q4. What is an attribute? What are the types of attributes.
[Already Answered in Q3](#q3-explain-er-notations-used-in-database-schema-design)
## Q5. What is a relationship? Give an example of all types of relationships.
A Relationship in a Database refers to a connection between properties of tables. 
- It is a logical association between different entities stored in seperate tables
- Eg. Customers, Products, and Orders are linked to each other using relations  

The example for all the types of relationships are:
- [***One-to-One relationship***](q2-define-entity-relationship-and-types-of-cardinality)  
- [***One-to-Many or Many-to-One relationship***](#q2-define-entity-relationship-and-types-of-cardinality)  
- [***Many-to-Many relationship***](#q2-define-entity-relationship-and-types-of-cardinality)

[GeeksforGeeks](https://www.geeksforgeeks.org/what-is-relationship-type-in-dbms/)

# Unit 3:
## Q1. What is a Domain, Attribute and Tuple?
Domain:
- In a database, a domain is a column that contains a data type. Data types can be built-in (such as integers or strings) or custom types that define constraints on the data themselves.
- Example:
    - In a table, a domain is a set of values that can be used to attribute an attribute. The domain of a month can accept January, February, etc. 
    - A domain of integers can accept whole numbers that are negative, positive, and zero.

Attribute:
- Any real-world object is considered to be an entity that has self-existence
    - These entities in DBMS have their own characteristics and properties known as attributes.  - Attributes give us additional information about entities and help us to study their relationship within the specified system.

Tuple:
- A Tuple in a DBMS is just a row having inter-related data about a particular entity(it can be any object).
    - Tuples are mostly seen in Relational Databases Management Systems(RDBMS) as RDBMS works on the relational model (Tabular format).
    - In DBMS, we call rows “Tuples” and a row “Tuple”.


[Gaurav Tiwari(Medium)](https://medium.com/@gauravtiwari20162/explain-1-domain-2-tuple-3-attributes-4-degree-5-cardinality-of-relation-cf31d94f1d5b)
## Q2. Explain Relational Model constraints: Domain Constraints, Referential Constraints,Integrity constraints, Null constraints.
Constraints are rules imposed on database contents to validate quality and ensure data integrity during operations like insertion and updates. They protect against threats and damages to the database.  
The main types of constraints in a relational database are four.
- ***Domain constraints***:
    - Every domain must contain atomic values(smallest indivisible units) which means composite and multi-valued attributes are not allowed.
    - We perform a datatype check here, which means when we assign a data type to a column we limit the values that it can contain. Eg. If we assign the datatype of attribute age as int, we can’t give it values other than int datatype. [[1](https://www.geeksforgeeks.org/constraints-on-relational-database-model/#main)]
- ***Referential constraints***:
    - The referential constraint is specified between two relations and is used to maintain the consistency among tuples in the two relations. 
    - the referential constraint states that a tuple in one relation that refers to another relation must refer to an existing tuple in that relation. [[2](https://www.pvpsiddhartha.ac.in/dep_it/lecture%20notes/2-2-23/DBMS/PVP20%20DBMS%20UNIT-2.pdf)]
- ***Integrity constraints***:  
    - The entity integrity constraint states that primary key value can't be null.
    - This is because the primary key value is used to identify individual rows in relation and if the primary key has a null value, then we can't identify those rows.
    - A table can contain a null value other than the primary key field [[3](https://www.javatpoint.com/dbms-integrity-constraints)]
- ***Null constraints***:  
    - Use the NULL keyword to specify that a column can store the NULL value for its data type.
    - This implies that the column need not receive any value during insert or update operations. 
    - The NULL constraint is logically equivalent to omitting the NOT NULL constraint from the column definition. [[4]](https://www.ibm.com/docs/en/informix-servers/12.10?topic=format-using-null-constraint)


## Q3. Explain operators in Relational algebra? Specifically Unary, Projection, binary 
Relational algebra is a procedural query language, which takes instances of relations as input and yields instances of relations as output. It uses operators to perform queries. 

An operator can be either unary or binary. They accept relations as their input and yield relations as their output. 

Types:
- **Unary**
    - The operations that operate on only one relation are called unary operations in relational algebra. The three unary operations in relational algebra are:
        - ***Selection***
            - The selection operation is a unary operation that is performed on one relation. 
            - The selection operation is used to retrieve tuples from the relation that satisfies the given condition. 
            - It is denoted by σ (sigma) 
        - ***Projection***
            -  Project operation selects (or chooses) certain attributes discarding other attributes.
            - The Project operation is also known as vertical partitioning since it partitions the relation or table vertically discarding other columns or attributes.
            - It is denoted by π (pi)
        - ***Rename***
            - The rename operation is operation applied on one relation. 
            - Rename operation (as the name suggests) is used to rename the relation, attributes or both. 
            - It is denoted by ρ (rho)
- ***Binary***
    - The operations that operate on two relations are called binary operations in relational algebra. The three binary operations in relational algebra are:
        - ***Union***
            - It performs binary union between two given relations
            - It is denoted by ∪ (union)
        - ***Set Difference***
            - The result of set difference operation is tuples, which are present in one relation but are not in the second relation.
            - It is denoted by − (Minus Symbol) 
        - ***Cartesian Product***
            - Combines information of two different relations into one. 
            - It is denoted by X (Multiplication X) 

- [GeeksForGeeks(Unary)](https://www.geeksforgeeks.org/what-are-the-unary-operations-in-relational-algebra/?ref=asr10)
- [TutorialsPoint](https://www.tutorialspoint.com/dbms/relational_algebra.htm) 

## Q4. What is join operation? Explain its types with an example.
SQL JOIN clause is used to query and access data from multiple tables by establishing logical relationships between them. 
- It can access data from multiple tables simultaneously using common key values shared across different tables. 

I will explain the types with various examples.
Consider two tables: `employees` and `departments`.

**employees**

| id  | name    | dept_id |
| --- | ------- | ------- |
| 1   | Alice   | 1       |
| 2   | Bob     | 2       |
| 3   | Charlie | NULL    |
| 4   | David   | 1       |

**departments**

| id  | dept_name     |
| --- | ------------- |
| 1   | HR            |
| 2   | IT            |
| 3   | Marketing     |

1. **Natural Join (⨝)**: This join automatically matches columns with the same name and data type in both tables. You don't need to specify any condition. In this example, it would automatically join on the `dept_id` column, as it's present in both tables.

Notation:
R ⨝ S 


Example:
```sql
SELECT employees.name, departments.dept_name FROM employees NATURAL JOIN departments;
```

Result:

| id  | name    | dept_name |
| --- | ------- | --------- |
| 1   | Alice   | HR        |
| 2   | Bob     | IT        |
| 4   | David   | HR        |

2. **Left Join (Left Outer Join)**  (⟕): This join returns all rows from the left table (employees), and the matching rows from the right table (departments). If there’s no match, `NULL` is returned for columns from the right table.

Notation:
R ⟕ S

Example:
```sql
SELECT employees.name, departments.dept_name FROM employees LEFT JOIN departments ON employees.dept_id = departments.id;
```

Result:

| name    | dept_name |
| ------- | --------- |
| Alice   | HR        |
| Bob     | IT        |
| Charlie | NULL      |
| David   | HR        |

3. **Right Join (Right Outer Join)** (⟖): This join returns all rows from the right table (departments), and the matching rows from the left table (employees). If there’s no match, `NULL` is returned for columns from the left table.

Notation:
R  ⟖ S

Example:
```sql
SELECT employees.name, departments.dept_name FROM employees RIGHT JOIN departments ON employees.dept_id = departments.id;
```

Result:

| name    | dept_name |
| ------- | --------- |
| Alice   | HR        |
| Bob     | IT        |
| NULL    | Marketing |

4. **Full Join (Full Outer Join)** (⟗): This join returns all rows when there is a match in either the left or right table. If there’s no match, `NULL` is returned for the unmatched rows.

Notation:
R ⟗ S

MySQL does not directly support full outer join, but you can achieve it using a combination of left join and right join with a `UNION`.

Example:
```sql
SELECT employees.name, departments.dept_name FROM employees LEFT JOIN departments ON employees.dept_id = departments.id 
UNION 
SELECT employees.name, departments.dept_name FROM employees RIGHT JOIN departments ON employees.dept_id = departments.id;
```

Result:

| name    | dept_name |
| ------- | --------- |
| Alice   | HR        |
| Bob     | IT        |
| Charlie | NULL      |
| David   | HR        |
| NULL    | Marketing |

5. **Inner Join**: This join returns rows that have matching values in both tables.  

Example: 
```sql
SELECT employees.name, departments.dept_name FROM employees INNER JOIN departments ON employees.dept_id = departments.id;
```

Result:

| name    | dept_name |
| ------- | --------- |
| Alice   | HR        |
| Bob     | IT        |
| David   | HR        |

## Q5. Explain nested Queries with example
Nested queries are a way to perform complex queries by embedding one query within another. The outer query can apply some conditions on the results of the inner query. Let us use Students, Grades tables for understanding nested queries.

Input:
Students table
| StudentID | StudentName | Age | Major         |
|-----------|-------------|-----|---------------|
| 1         | Alice       | 20  | Mathematics   |
| 2         | Bob         | 21  | Computer Sci  |
| 3         | Charlie     | 22  | Mathematics   |
| 4         | David       | 19  | Physics       |

Grades table:
| StudentID | Subject      | Score |
|-----------|--------------|-------|
| 1         | Mathematics  | 95    |
| 1         | Physics      | 88    |
| 2         | Computer Sci | 85    |
| 3         | Mathematics  | 92    |
| 4         | Physics      | 78    |

```SQL
SELECT StudentName
FROM Students
WHERE StudentID IN (
    SELECT StudentID
    FROM Grades
    WHERE Subject = ‘Mathematics’ AND Score > 90
);
```

Output:
| StudentName |
|-------------|
| Alice       |
| Charlie     |

[GeeksForGeeks](https://www.geeksforgeeks.org/nested-queries-in-sql/)
## Q6. Describe the PL/SQL block
PL/SQL Queries are more or less blocks of code.
- Declare Block
    - Declare section starts with DECLARE keyword in which variables, constants, records as cursors can be declared which stores data temporarily. 
    - It basically consists definition of PL/SQL identifiers. 
    - This part of the code is optional.
- Begin Block
    - Execution section starts with BEGIN and ends with END keyword.
    - Here, the program logic is written to perform any task like loops and conditional statements. 
    - This is a mandatory section.
- Exception Block
    - Exception section starts with EXCEPTION keyword
    - Any exceptions can be handled in this section 
    - It contains statements that are executed when a run-time error occurs.
    - This section is optional 
- End
    - Indicates the end of the PL/SQL Begin Block.
    - This is a mandatory section
- Seperator(;)
    - Marks the End of the PL/SQL query sequence
    - Helps seperate one PL/SQL sequence from another one

Syntax:
```plsql
DECLARE
    declaration statements;

BEGIN
    executable statements;

EXCEPTIONS
    exception handling statements;

END;
```

[(GeeksForGeeks)](https://www.geeksforgeeks.org/plsql-introduction/)
## Q7. Features of PL/SQL
Features of PL/SQL:
- PL/SQL is basically a procedural language
    - It provides the functionality of decision-making, iteration, and many more features of procedural programming languages.
- PL/SQL can execute a number of queries in one block using single command.
- One can create a PL/SQL unit such as procedures, functions, packages, triggers, and types
    - They are stored in the database for reuse by applications.
- PL/SQL provides a feature to handle the exception which occurs in PL/SQL block known as exception handling block.
- Applications written in PL/SQL are portable to computer hardware or operating system where Oracle is operational.
    PL/SQL Offers extensive error checking.

[GeeksForGeeks](https://www.geeksforgeeks.org/plsql-introduction/)
## Q8. What is cursor and its types
The cursor is used to retrieve data one row at a time from the results set, unlike other SQL commands that operate on all rows at once.
- Cursors update table records in a singleton or row-by-row manner.


Cursors are classified depending on how they are opened:
- ***Implicit Cursor***: If the Oracle engine opened a cursor for its internal processing it is known as an Implicit Cursor. 
    - It is created “automatically” for the user by Oracle when a query is executed and is simpler to code.
- ***Explicit Cursor***: A Cursor can also be opened for processing data through a PL/SQL block, on demand. 
    - A user-defined cursor is known as an Explicit Cursor.
    - Syntax for creating a Cursor
        - `CURSOR cursor_name IS select_statement;`


## Q9. Explain exception with an example?
An exception is an error which disrupts the normal flow of program instructions. PL/SQL provides us the exception block which raises the exception thus helping the programmer to find out the fault and resolve it.

There are two types of exceptions defined in PL/SQL:
- **User defined exception**.
- **System defined exceptions**.

[GeeksForGeeks](https://www.geeksforgeeks.org/exception-handling-plsql/) TODO: Finish
# Unit 4:
## Q1. Anomalies in relational Database design
Anomalies in the relational model refer to inconsistencies or errors that can arise when working with relational databases, specifically in the context of data insertion, deletion, and modification.
- Database anomalies are the faults in the database caused due to poor management of storing everything in the flat database. 
- It can be removed with the process of **Normalization**, which generally splits the database which results in reducing the anomalies in the database.

These anomalies can be categorized into three types:
- **Insertion Anomalies**
- **Deletion Anomalies**
- **Update Anomalies**.

[GeeksForGeeks](https://www.geeksforgeeks.org/anomalies-in-relational-model/)
## Q2. Decomposition 
When we divide a table into multiple tables or divide a relation into multiple relations, then this process is called Decomposition. 
- We perform decomposition in DBMS when we want to process a particular data set. 
- It is performed in a database management system when we need to ensure consistency and remove anomalies and duplicate data present in the database. 
    - When we perform decomposition in DBMS, we must try to ensure that no information or data is lost.

There are two types of Decomposition:
- **Lossless Decomposition**
    - We can regain the original relation R with the help of joins from the multiple relations formed after decomposition
        - While regaining the original relation, no information should be lost.
        - If we perform join operation on the sub-divided relations, we must get the original relation.
- **Lossy Decomposition**
    - When we perform join operation on the sub-relations, it doesn't result to the same relation which was decomposed

![Decomposition in DBMS](https://media.geeksforgeeks.org/wp-content/uploads/20240225103236/Screenshot-2024-02-25-103224.png)

[GeeksForGeeks](https://www.geeksforgeeks.org/decomposition-in-dbms/)
## Q3. Functional Dependencies
In relational database management, functional dependency is a concept that specifies the relationship between two sets of attributes where one attribute determines the value of another attribute. 
- It is denoted as X → Y
    - The attribute set on the left side of the arrow, X is called Determinant, and Y is called the Dependent.
    - Basically, the value of Y depends on the Value of X

There are Two Types of Functional Dependencies:
- ***Trivial functional dependency***
    - In Trivial Functional Dependency, a dependent is always a subset of the determinant. 
    - i.e. If X → Y and Y is the subset of X, then it is called trivial functional dependency
- ***Non-Trivial functional dependency***
    - In Non-trivial functional dependency, the dependent is strictly not a subset of the determinant. 
    - i.e. If X → Y and Y is not a subset of X, then it is called Non-trivial functional dependency.

[GeeksForGeeks](https://www.geeksforgeeks.org/types-of-functional-dependencies-in-dbms/)
## Q4. 1st normal Form, 2nd normal Form, 3rd normal form, BCNF
Normalization is the process of minimizing redundancy from a relation or set of relations. 
- Redundancy in relation may cause insertion, deletion, and update anomalies. 
    - So, it helps to minimize the redundancy in relations. 
    - Normal forms are used to eliminate or reduce redundancy in database tables. 
- What normalization basically does is ensure that your data is free of data redundancy or duplicate data and does not have data anomalies that would otherwise compromise its integrity.

Levels of Normalization:
- ***First Normal Form*** (1NF)
- ***Second Normal Form*** (2NF)
- ***Third Normal Form*** (3NF)
- ***Boyce-Codd Normal Form*** (BCNF)

Explanation:
- First Normal Form (1NF):
    - This is the most basic level of normalization. 
    - In 1NF, each table cell should contain only a single value, and each column should have a unique name. The first normal form helps to eliminate duplicate data and simplify queries.
- Second Normal Form (2NF):
    - 2NF eliminates redundant data by requiring that each non-key attribute be dependent on the primary key. 
    - This means that each column should be directly related to the primary key, and not to other columns.
- Third Normal Form (3NF):
    - 3NF builds on 2NF by requiring that all non-key attributes are independent of each other. 
    - This means that each column should be directly related to the primary key, and not to any other columns in the same table.
- Boyce-Codd Normal Form (BCNF):
    - BCNF is a stricter form of 3NF that ensures that each determinant in a table is a candidate key. 
    - In other words, BCNF ensures that each non-key attribute is dependent only on the candidate key.

[(GeeksForGeeks, Explanation)](https://www.geeksforgeeks.org/normal-forms-in-dbms/)
[(GeeksForGeeks, Forms)](https://www.geeksforgeeks.org/normal-forms-in-dbms/)

# Unit 5:
## Q1. Transaction states
Transaction in DBMS is a set of logically related operations executed as a single unit. 
- These logic are followed to perform modification on data while maintaining integrity and consistency
- Example: Adding student1's exam result to the database

![Transaction States](https://media.geeksforgeeks.org/wp-content/uploads/20200501195048/Tt7.png)

- These are different types of Transaction States :  
    - ***Active State*** 
        - When the instructions of the transaction are running then the transaction is in active state. If all the ‘read and write’ operations are performed without any error then it goes to the “partially committed state”; if any instruction fails, it goes to the “failed state”. 
    - ***Partially Committed*** 
        - After completion of all the read and write operation the changes are made in main memory or local buffer. If the changes are made permanent on the DataBase then the state will change to “committed state” and in case of failure it will go to the “failed state”. 
    - ***Failed State*** 
        - When any instruction of the transaction fails, it goes to the “failed state” or if failure occurs in making a permanent change of data on Database. 
    - ***Aborted State***
        - After having any type of failure the transaction goes from “failed state” to “aborted state” and since in previous states, the changes are only made to local buffer or main memory 
        - Hence these changes are deleted or rolled-back. 
    - ***Committed State***
        - It is the state when the changes are made permanent on the Data Base and the transaction is complete and therefore terminated in the “terminated state”. 
    - ***Terminated State***
        - If there isn’t any roll-back or the transaction comes from the “committed state”, then the system is consistent and ready for new transaction and the old transaction is terminated.  

[GeeksForGeeks](https://www.geeksforgeeks.org/transaction-states-in-dbms/)
## Q2.  Transaction operations
A user can make different types of requests to access and modify the contents of a database. 

So, we have different types of operations relating to a transaction. They are discussed as follows:
- **Read**(X)
    -  A read operation is used to read the value of X from the database and store it in a buffer in the main memory for further actions such as displaying that value.
    -  Such an operation is performed when a user wishes just to see any content of the database and not make any changes to it. 
    - For example, when a user wants to check his/her account's balance, a read operation would be performed on user's account balance from the database.
- **Write**(X) 
    -  A write operation is used to write the value to the database from the buffer in the main memory. 
    - For a write operation to be performed, first a read operation is performed to bring its value in buffer, and then some changes are made to it, e.g. some set of arithmetic operations are performed on it according to the user's request, then to store the modified value back in the database, a write operation is performed.
    -  For example, when a user requests to withdraw some money from his account, 
        - his account balance is fetched from the database using a read operation, 
        - then the amount to be deducted from the account is subtracted from this value, 
        - and then the obtained value is stored back in the database using a write operation.
- **Commit**
    -  This operation in transactions is used to maintain integrity in the database. Due to some failure of power, hardware, or software, etc., a transaction might get interrupted before all its operations are completed. 
        - This may cause ambiguity in the database, i.e. it might get inconsistent before and after the transaction.
    -  To ensure that further operations of any other transaction are performed only after work of the current transaction is done, a commit operation is performed to the changes made by a transaction permanently to the database.
- **Rollback**
    -  This operation is performed to bring the database to the last saved state when any transaction is interrupted in between due to any power, hardware, or software failure.
    -  In simple words, it can be said that a rollback operation does undo the operations of transactions that were performed before its interruption to achieve a safe state of the database and avoid any kind of ambiguity or inconsistency.

[GeeksForGeeks](https://www.geeksforgeeks.org/transaction-in-dbms/)
## Q3. Properties of Transaction
A transaction is a single logical unit of work that accesses and possibly modifies the contents of a database. 
- Transactions access data using read-and-write operations. 
- To maintain consistency in a database, before and after the transaction, certain properties are followed. 
    - These are called ACID properties.

The acronym ACID stands for Atomicity, Consistency, Isolation, and Durability. ACID Can be broken down to:
- ***A***tomicity:
    - By this, we mean that either the entire transaction takes place at once or doesn’t happen at all. There is no midway i.e. transactions do not occur partially. 
    - Each transaction is considered as one unit and either runs to completion or is not executed at all
    - It involves the following two operations.
        - ***Abort*** : If a transaction aborts, changes made to the database are not visible.
        - ***Commit*** : If a transaction commits, changes made are visible.
    - Atomicity is also known as the ‘All or nothing rule’. 
- ***C***onsistency:
    - This means that integrity constraints must be maintained so that the database is consistent before and after the transaction. 
    - It refers to the correctness of a database.  
- ***I***solation:
    - This property ensures that multiple transactions can occur concurrently without leading to the inconsistency of the database state. 
    - Transactions occur independently without interference. 
    - Changes occurring in a particular transaction will not be visible to any other transaction until that particular change in that transaction is written to memory or has been committed. 
- ***D***urability:
    - This property ensures that once the transaction has completed execution, the updates and modifications to the database are stored in and written to disk and they persist even if a system failure occurs. 
    - These updates now become permanent and are stored in non-volatile memory. 
    - The effects of the transaction, thus, are never lost. 

![ACID Properties](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20191121102921/ACID-Properties.jpg)

[(GeeksForGeeks)](https://www.geeksforgeeks.org/acid-properties-in-dbms/)

## Q4. Concurrency control problem
Concurrency control is an essential aspect of database management systems that ensures transactions can execute concurrently without interfering with each other. 
- However, concurrency control can be challenging to implement
    - without it, several problems can arise, affecting the consistency of the database. 
- When multiple transactions execute concurrently in an uncontrolled or unrestricted manner, then it might lead to several problems. 
- These problems are commonly referred to as concurrency problems in a database environment. 

These problems are:
- Lost Update Problem: 
- Dirty Read Problem: 
- Inconsistent Retrevial Problem:
- Phantom Read Problem:


TODO: Finish

## Q5. concurrency control techniques
Following are the Concurrency Control techniques in DBMS:
- ***Lock-Based Protocol***
    - A lock is a variable associated with a data item that describes the status of the data item to possible operations that can be applied to it. 
    - Types:
        - **Shared Lock** (S): Shared Lock is also known as Read-only lock. 
            - As the name suggests it can be shared between transactions because while holding this lock the transaction does not have the permission to update data on the data item. 
            - S-lock is requested using lock-S instruction. 
        - **Exclusive Lock** (X): Data item can be both read as well as written.
            - This is Exclusive and cannot be held simultaneously on the same data item. 
            - X-lock is requested using lock-X instruction. 
- ***Two Phase Locking Protocol***
    - A transaction follows the two-phase locking protocol if locking and unlocking can be done in two phases. 
    - The two phases of 2PL are:
        1. *Growing Phase*: In this phase, we can acquire new locks on data items, but none of these locks can be released.
        2. *Shrinking Phase*: In this phase, the existing locks can be released, but no new locks can be
obtained
- ***Timestamp-Based Protocol***
    - A timestamp is a tag that can be attached to any transaction or any data item, which denotes a specific time on which the transaction or the data item had been used in any way. 

[GeeksForGeeks](https://www.geeksforgeeks.org/concurrency-control-techniques/)

[GeeksForGeeks(Lock Based Protocol)](https://www.geeksforgeeks.org/lock-based-concurrency-control-protocol-in-dbms/)