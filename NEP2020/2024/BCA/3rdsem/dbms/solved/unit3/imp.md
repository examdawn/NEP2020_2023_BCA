# Unit 3: Relational Data Model

## Important Questions

### Q1. What is a relational data model? 
 A relational data model is where we use Tables to describe how our data is stored in a Relational Databases. Rows are called Tuples and Columns are called Attributes.  

| **Student ID** | **Name** | **Age** | **Field** |
| --- | --- | --- | --- |
| 1 | John Smith | 20 | Computer Science |
| 2 | Jane Doe | 21 | Biology |
| 3 | Bob Johnson | 19 | Mathematics |

Here, Student ID, Name, Age and Field come under Attributes(columns) and the Tuples(rows) hold student data corresponding to the attributes. 

[GeeksForGeeks](https://www.geeksforgeeks.org/relational-model-in-dbms/)

### Q2. What is an attribute? 
A. An attribute is a property that describes the entity. For example, in a customer database, the attributes might be name, address, and phone number.

In a relational data model, it is depicted as a column. 

[KnowledgeHut](https://www.knowledgehut.com/blog/database/attributes-in-dbms)

### Q4. What is a table? 
A table is a collection of data organized in a table-like format within a database. It contains rows(called tuples), and columns(called attributes).
### Q5. What is a domain? 
The data type defined for a column in a database is called a database domain. This data type can either be a built-in type (such as an integer or a string) or a custom type that defines data constraints.

[Scalar](https://www.scaler.com/topics/domain-in-dbms/)
 
### Q6. Explain the various characteristics of relations. 
 
### Q7. What is a domain constraint? 
 In a database table, domain constraints are guidelines that specify the acceptable values for a certain property or field. These restrictions guarantee data consistency and aid in preventing the entry of inaccurate or inconsistent data into the database

- Data type constraints 
    − These limitations define the kinds of data that can be kept in a column. 
    - A column created as VARCHAR can take string values, but a column specified as INTEGER can only accept integer values.

- Length Constraints 
    − These limitations define the largest amount of data that may be put in a column. 
    - For instance, a column with the definition VARCHAR(10) may only take strings that are up to 10 characters long.

- Range constraints 
    − The allowed range of values for a column is specified by range restrictions. 
    - A column designated as DECIMAL(5,2), for example, may only take decimal values up to 5 digits long, including 2 decimal places.

- Nullability constraints 
    − Constraints on a column's capacity to accept NULL values are known as nullability constraints. 
    - For instance, a column that has the NOT NULL definition cannot take NULL values.

- Unique constraints 
    − Constraints that require the presence of unique values in a column or group of columns are known as unique constraints. 
    - For instance, duplicate values are not allowed in a column with the UNIQUE definition.

- Check constraints 
    − Constraints for checking data: These constraints outline a requirement that must hold for any data placed into the column. 
    - For instance, a column with the definition CHECK (age > 0) can only accept ages that are greater than zero.

- Default constraints 
    − Constraints by default: Default constraints automatically assign a value to a column in case no value is provided. 
    - For example, a column with a DEFAULT value of 0 will have 0 as its value if no other value is specified.

[TutorialsPoint](https://www.tutorialspoint.com/constraints-in-relational-database-model)
### Q8. What is a constraint in a relational model? 
In Relational Database Model , constraints are guidelines or limitations imposed on database tables to maintain the integrity, correctness, and consistency of the data. Constraints can be used to enforce data linkages across tables, verify that data is unique, and stop the insertion of erroneous data. A database needs constraints to be reliable and of high quality.

[TutorialsPoint](https://www.tutorialspoint.com/constraints-in-relational-database-model)
### Q9. Explain various constraints. 
Types of Constraints in Relational Database Model
- Domain Constraints
    - Already explained in q7.
- Key Constraints
    - Key constraints are regulations that a Relational Database Model uses to ensure data accuracy and consistency in a database. They define how the values in a table's one or more columns are related to the values in other tables, making sure that the data remains correct.
    - Types:
        - Primary Key Constraint
        - Foreign Key Constraint
        - Unique Constraint
- Entity Integrity Constraints
    - A database management system uses entity integrity constraints (EICs) to enforce rules that guarantee a table's primary key is unique and not null. 
    - The consistency and integrity of the data in a database are maintained by EICs, which are created to stop the formation of duplicate or incomplete entries.
- Referential Integrity Constraints
    - A database management system will apply referential integrity constraints (RICs) in order to preserve the consistency and integrity of connections between tables. 
    - By preventing links between entries that don't exist from being created or by removing records that have related records in other tables, RICs guarantee that the data in a database is always consistent.
- Tuple Uniqueness Constraints
    - A database management system uses constraints called tuple uniqueness constraints (TUCs) to make sure that every entry or tuple in a table is distinct. 
    - TUCs impose uniqueness on the whole row or tuple, in contrast to Entity Integrity Constraints (EICs), which only enforce uniqueness on certain columns or groups of columns.

 [TutorialsPoint](https://www.tutorialspoint.com/constraints-in-relational-database-model)

### Q9. What is relational algebra? 
Relational algebra is a procedural query language, which takes instances of relations as input and yields instances of relations as output. It uses operators to perform queries. 

An operator can be either unary or binary. They accept relations as their input and yield relations as their output. 

Relational algebra is performed recursively on a relation and intermediate results are also considered relations.

[TutorialsPoint](https://www.tutorialspoint.com/dbms/relational_algebra.htm) 
### Q10. Explain basic relational algebra operations. 
The fundamental operations of relational algebra are
- The SELECT Operation
- The PROJECT Operation
- Set Theoretic Operations
    - Union operation
    - Intersection operation
    - Set difference or Minus operation.
    - Cartesian Product
    - Division
- The JOIN Operations

Will be explained in Following Questions

[TutorialsPoint](https://www.tutorialspoint.com/dbms/relational_algebra.htm)
### Q11. What is select operation give an example? 
Select operation chooses the subset of tuples from the relation that satisfies the given condition mentioned in the syntax of selection. 

The selection operation is also known as horizontal partitioning since it partitions the table or relation horizontally. Its Notation is σ c(R). where ‘c’ is the selection condition which is a boolean expression(condition).

| Roll | Name   | Department | Fees  | Team |
|------|--------|------------|-------|------|
| 2    | Josh   | CSE        | 34000 | A    |
| 3    | Kevin  | ECE        | 36000 | C    |
| 4    | Ben    | ECE        | 56000 | D    |

**Query:** Select all the students of Team A: σ Team = 'A' (Student)
```sql
SELECT * 
FROM Students 
WHERE Team = 'A';
```

**Result:**

| Roll | Name   | Department | Fees  | Team |
|------|--------|------------|-------|------|
| 2    | Josh   | CSE        | 34000 | A    |

### Q12. What is Project operation give an example. 
 Project operation selects (or chooses) certain attributes discarding other attributes. The Project operation is also known as vertical partitioning since it partitions the relation or table vertically discarding other columns or attributes.

Notation: πA(R) where ‘A’ is the attribute list, it is the desired set of attributes from the attributes of relation(R),symbol ‘π(pi)’  is used to denote the Project operator,R is generally a relational algebra expression, which results in a relation.

| Class | Dept | Position           |
|-------|------|--------------------|
| 5     | CSE  | Assistant Professor |
| 6     | EE   | Assistant Professor |
| 6     | EE   | Assistant Professor |

**Query**: Project Class and Dept from Faculty: π Class, Dept (Faculty)

```sql
SELECT DISTINCT Class, Dept 
FROM Faculty;
```

**Result**:
| Class | Dept |
|-------|------|
| 5     | CSE  |
| 6     | EE   |


### Q13. What is union operation given example? 

UNION Operation:  A ∪ S where, A and S are the relations, symbol ‘∪’  is used to denote the Union operator. The result of Union operation, which is denoted by A ∪ S, is a relation that basically includes all the tuples that are present in A or in S, or in both, eliminating the duplicate tuples.


 | EMPID | NAME   |
|-------|--------|
| 1001  | Charles|
| 1002  | Abdul  |
| 1003  | Rohan  |

 | EMPID | NAME   |
|-------|--------|
| 1004  | Shermi|
| 1005  | Jhansi  |

**Query**: Union operation on EMPID and NAME from two tables

```sql
SELECT EMPID, NAME 
FROM Table1
UNION
SELECT EMPID, NAME 
FROM Table2;
```

**Result**:

| EMPID | NAME   |
|-------|--------|
| 1001  | Charles|
| 1002  | Abdul  |
| 1003  | Rohan  |
| 1004  | Shermi |
| 1005  | Jhansi |



### Q14. What is Cartesian product given example? 
This is a binary relation operation. It combines the tuples of two relations into one relation. It is denoted by ‘X’ symbol.  A X S. this operator will simply create a pair between the tuples of each table.

| EMPID | NAME   |
|-------|--------|
| 1001  | Charles|
| 1002  | Abdul  |
| 1003  | Rohan  |

| DEPTID| DNAME  |
|-------|--------|
|  10   |Accounts|
|  20   | Design |
|  30   |Testing |


**Query**: Cartesian product of EMPID and NAME from two tables


```sql
SELECT A.EMPID, A.NAME, B.EMPID, B.NAME 
FROM Table1 A
CROSS JOIN Table2 B;
```
**Result**:
 | EMPID | NAME    | DEPTID | DNAME    |
|-------|---------|--------|----------|
| 1001  | Charles | 10     | Design   |
| 1001  | Charles | 20     | Accounts |
| 1001  | Charles | 30     | Testing  |
| 1002  | Abdul   | 10     | Design   |
| 1002  | Abdul   | 20     | Accounts |
| 1002  | Abdul   | 30     | Testing  |
| 1003  | Rohan   | 10     | Accounts |
| 1003  | Rohan   | 20     | Design   |
| 1003  | Rohan   | 30     | Testing  |


### Q15. Explain different types of join with an example.

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


## Source:
- Questions: Dictated in class
