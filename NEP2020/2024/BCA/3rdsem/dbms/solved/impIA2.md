## Section-A (2 Marks) 

### Mention any two feature of PL/SQL.
PL/SQL (Procedural Language/Structured Query Language) is a block-structured language developed by Oracle that allows developers to combine the power of SQL with procedural programming constructs. 
- The PL/SQL language enables efficient data manipulation and control-flow logic
- This is done within the Oracle Database in the same shell/interface we use for SQL queries

[(GeeksForGeeks)](https://www.geeksforgeeks.org/plsql-introduction/)

### What is single-user system in DBMS?
A single-user database management system (DBMS) like SQLite is a system that only allows one user to access the database at a time. 
- Single-user DBMSs are usually found on personal computers 
- They are designed to be simple and easy to use. 
- They are often used for personal projects or small-scale applications
### What is time stamping?
Time Stamping is a Concurrency Control method used to ensure that transactions are executed safely and without conflicts even when multiple transactions happen at one go.
- It uses Time Stamps to co-ordinate the execution order of transactions 

[(GeeksForGeeks)](https://www.geeksforgeeks.org/timestamp-based-concurrency-control/)
### What is an insert anomaly?
Anomalies refer to inconsistencies or errors that can arise when working with relational databases. They can be broken down into 3 types:
- Insertion Anomalies
- Deletion Anomalies
- Update Anomalies

Insert Anomalies occur when it is not possible to insert data into a database because the required fields are missing or because the data is incomplete. 
- For example, if a database requires that every record has a primary key, but no value is provided for a particular record, it cannot be inserted into the database.

[(GeeksForGeeks)](https://www.geeksforgeeks.org/anomalies-in-relational-model/)

### What is a transaction failure?
Transaction Failure is when a transaction is unable to execute further due to a logical error in the procedure or a system error like deadlocks or resource constraints  

[(GeeksForGeeks)](https://www.geeksforgeeks.org/failure-classification-in-dbms/)
### What is a transaction processing?
Transaction Processing is how a transaction is processed on a DBMS. 
- Types:
    - Interleaved Processing 
        - In this, the concurrent execution of processes is interleaved in a single CPU. 
        - The transactions are interleaved, meaning the second transaction is started before the primary one could finish. 
        - Execution can switch between the transactions. 
        - It can also switch between multiple transactions. This causes inconsistency in the system.
    - Parallel Processing
        - It is defined as the processing in which a large task into various smaller tasks and smaller task also executes concurrently on several nodes. 
        - In this, the processes are concurrently executed in multiple CPUs.

[(GeeksForGeeks)](https://www.geeksforgeeks.org/introduction-to-transaction-processing/)
### What is concurrency control?
Concurrency Control is the process of ensuring simultaneous execution or updation of data by several processes or users
- This is done while maintaining data consistency and integrity

## Section-B (4 Marks)

### Explain basic syntax of PL/SQL?
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
    executable statements

EXCEPTIONS
    exception handling statements

END;
```

[(GeeksForGeeks)](https://www.geeksforgeeks.org/plsql-introduction/)

### Write a note in anomalies in relational database design.

Anomalies refer to inconsistencies or errors that can arise when working with relational databases. These anomalies can be categorized into three types:
- Insertion Anomalies:
    - These anomalies occur when it is not possible to insert data into a database because the required fields are missing or because the data is incomplete. 
    - For example, if a database requires that every record has a primary key, but no value is provided for a particular record, it cannot be inserted into the database.
- Deletion anomalies:
    - These anomalies occur when deleting a record from a database and can result in the unintentional loss of data. 
    - For example, if a database contains information about customers and orders, deleting a customer record may also delete all the orders associated with that customer.
- Update anomalies:
    -  These anomalies occur when modifying data in a database and can result in inconsistencies or errors. 
    - For example, if a database contains information about employees and their salaries, updating an employee’s salary in one record but not in all related records could lead to incorrect calculations and reporting.

[(GeeksForGeeks)](https://www.geeksforgeeks.org/anomalies-in-relational-model/)

### Write a note on properties of transactions.
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
<img src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/20191121102921/ACID-Properties.jpg" alt="ACIDDBMS" width="400" />

[(GeeksForGeeks)](https://www.geeksforgeeks.org/acid-properties-in-dbms/)

### What is functional dependency? Explain
In relational database management, functional dependency is a concept that specifies the
relationship between two sets of attributes where one attribute determines the value of another
attribute. It is denoted as X → Y, where the attribute set on the left side of the arrow, X is
called Determinant, and Y is called the Dependent.
### Explain function with example in PL/SQL.

A standalone function is created using the CREATE FUNCTION statement. The simplified syntax for the CREATE OR REPLACE PROCEDURE statement is:
```plsql
CREATE [OR REPLACE] FUNCTION function_name 
[(parameter_name [IN | OUT | IN OUT] type [, ...])] 
RETURN return_datatype 
{IS | AS} 
BEGIN 
   < function_body > 
END [function_name];
```

- function-name specifies the name of the function.
- [OR REPLACE] option allows the modification of an existing function.
- The optional parameter list contains name, mode and types of the parameters. IN represents the value that will be passed from outside and OUT represents the parameter that will be used to return a value outside of the procedure.
- The function must contain a return statement.
- The RETURN clause specifies the data type you are going to return from the function.
- function-body contains the executable part.
- The AS keyword is used instead of the IS keyword for creating a standalone function.

Eg.

```SQL
Select * from customers; 
```
| ID | NAME     | AGE | ADDRESS   | SALARY   | 
|----|----------|-----|-----------|----------|
|  1 | Ramesh   |  32 | Ahmedabad |  2000.00 | 
|  2 | Khilan   |  25 | Delhi     |  1500.00 | 

```plsql
CREATE OR REPLACE FUNCTION totalCustomers 
RETURN number IS 
   total number(2) := 0; 
BEGIN 
   SELECT count(*) into total 
   FROM customers; 
    
   RETURN total; 
END; 
/
```

Calling the Function
```plsql
DECLARE 
   c number(2); 
BEGIN 
   c := totalCustomers(); 
   dbms_output.put_line('Total no. of Customers: ' || c); 
END; 
/
```

[(TutorialsPoint)](https://www.tutorialspoint.com/plsql/plsql_functions.htm)

### Explain various transaction failure in DBMS

If a transaction is not able to execute or it comes to a point from where the transaction becomes incapable of executing further then it is termed as a failure in a transaction.

Reason for a transaction failure in DBMS:

- Logical error:
    - A logical error occurs if a transaction is unable to execute because of some mistakes in the code or due to the presence of some internal faults.
- System error:
    - Where the termination of an active transaction is done by the database system itself due to some system issue or because the database management system is unable to proceed with the transaction. 
    - For example– The system ends an operating transaction if it reaches a deadlock condition or if there is an unavailability of resources.

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20220122170232/FailureClassificationinDBMS.png" alt="FailureClassification" width="400" />

[(GeeksForGeeks)](https://www.geeksforgeeks.org/failure-classification-in-dbms/)

## Section-C (8 Marks)

### What is normalization? Explain 1NF, 2NF, 3NF, BCNF.
Normalization for relational databases is used to extensively reduce data redundancy and dependency by streamlining database data correctly
- What normalization basically does is ensure that your data is free of data redundancy or duplicate data and does not have data anomalies that would otherwise compromise its integrity.

Data can be normalized into these forms:
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
### Explain transaction states in DBMS

In DBMS, a transaction passes through various states such as active, partially committed, failed, and aborted.
- These are different types of Transaction States :  
    - Active State 
        - When the instructions of the transaction are running then the transaction is in active state. If all the ‘read and write’ operations are performed without any error then it goes to the “partially committed state”; if any instruction fails, it goes to the “failed state”. 
    - Partially Committed 
        - After completion of all the read and write operation the changes are made in main memory or local buffer. If the changes are made permanent on the DataBase then the state will change to “committed state” and in case of failure it will go to the “failed state”. 
    - Failed State 
        - When any instruction of the transaction fails, it goes to the “failed state” or if failure occurs in making a permanent change of data on Database. 
    - Aborted State
        - After having any type of failure the transaction goes from “failed state” to “aborted state” and since in previous states, the changes are only made to local buffer or main memory 
        - Hence these changes are deleted or rolled-back. 
    - Committed State
        - It is the state when the changes are made permanent on the Data Base and the transaction is complete and therefore terminated in the “terminated state”. 
    - Terminated State  
        - If there isn’t any roll-back or the transaction comes from the “committed state”, then the system is consistent and ready for new transaction and the old transaction is terminated.  

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20200501195048/Tt7.png" alt="TransactionStates" width="400" />

[(GeeksForGeeks)](https://www.geeksforgeeks.org/transaction-states-in-dbms/)

### Write a note on types of lock in concurrency control.
A lock is a variable associated with a data item that describes the status of the data item to possible operations that can be applied to it. 
- They synchronize the access by concurrent transactions to the database items. 
- It is required in this protocol that all the data items must be accessed in a mutually exclusive manner
- Types: 
    - Shared Lock (S):
        - Shared Lock is also known as Read-only lock. 
        - As the name suggests it can be shared between transactions because while holding this lock the transaction does not have the permission to update data on the data item. 
        - S-lock is requested using lock-S instruction.
    - Exclusive Lock (X):
        - Data item can be both read as well as written.
        - This is Exclusive and cannot be held simultaneously on the same data item. 
        - X-lock is requested using lock-X instruction.

[(GeeksForGeeks)](https://www.geeksforgeeks.org/lock-based-concurrency-control-protocol-in-dbms/)

### Differentiate between single-user and multi-user system.
| Feature | Single-User DBMS | Multi-User DBMS | 
|-----------------------|-------------------------------------------|------------------------------------------| 
| Definition | Supports one user at a time. | Supports multiple users simultaneously. | 
| Usage | Typically used for personal applications. | Common in enterprise and collaborative environments. | 
| Performance | Generally faster due to no contention. | May experience delays due to concurrent access. | 
| Complexity | Simpler design and management. | More complex, requiring concurrency control. | 
| Examples | Microsoft Access, SQLite. | Oracle, MySQL, PostgreSQL. |
### Write a note on decomposition?
Decomposition refers to the division of tables into multiple tables to produce consistency in the data.
- When we divide a table into multiple tables or divide a relation into multiple relations, then this process is termed Decomposition in DBMS. 
- We perform decomposition in DBMS when we want to process a particular data set. 
- It is performed in a database management system when we need to ensure consistency and remove anomalies and duplicate data present in the database. 
- When we perform decomposition in DBMS, we must try to ensure that no information or data is lost. 

[(GeeksForGeeks)](https://www.geeksforgeeks.org/decomposition-in-dbms/)
### Write a note on transaction read and write operations.

A user can make different types of requests to access and modify the contents of a database. So, we have different types of operations relating to a transaction:
- Read(X)
    - A read operation is used to read the value of X from the database and store it in a buffer in the main memory for further actions such as displaying that value.
    - Such an operation is performed when a user wishes just to see any content of the database and not make any changes to it. 
    - For example, when a user wants to check his/her account's balance, a read operation would be performed on user's account balance from the database.
- Write(X)
    - A write operation is used to write the value to the database from the buffer in the main memory.
    - For a write operation to be performed, first a read operation is performed to bring its value in buffer, and then some changes are made to it, e.g. some set of arithmetic operations are performed on it according to the user's request, then to store the modified value back in the database, a write operation is performed.
    - For example, when a user requests to withdraw some money from his account, his account balance is fetched from the database using a read operation, then the amount to be deducted from the account is subtracted from this value, and then the obtained value is stored back in the database using a write operation.
- Commit
    - This operation in transactions is used to maintain integrity in the database. 
    - Due to some failure of power, hardware, or software, etc., a transaction might get interrupted before all its operations are completed. 
        - This may cause ambiguity in the database, i.e. it might get inconsistent before and after the transaction.
    - To ensure that further operations of any other transaction are performed only after work of the current transaction is done, a commit operation is performed to the changes made by a transaction permanently to the database.
- Rollback
    - This operation is performed to bring the database to the last saved state when any transaction is interrupted in between due to any power, hardware, or software failure.
    - In simple words, it can be said that a rollback operation does undo the operations of transactions that were performed before its interruption to achieve a safe state of the database and avoid any kind of ambiguity or inconsistency.

[(GeeksForGeeks)](https://www.geeksforgeeks.org/transaction-in-dbms/)
