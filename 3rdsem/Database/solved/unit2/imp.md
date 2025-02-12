# Unit 2: Entity-Relationship Models

## Important Questions

### Q1. Define entity and entity type.
A. An entity is a piece of data that's uniquely identifiable within the database and usually represents something from the real world. 

An Entity type is a collection of entities with general characteristics.

For example, a database of a corporate company has entity types such as employees, departments, etc. In DBMS, every entity type contains a set of attributes that explain the entity.

[Javatpoint](https://www.javatpoint.com/entity-in-dbms)

[GeeksForGeeks](https://www.geeksforgeeks.org/entity-in-dbms/)
### Q2. What is an entity set?
A.  An entity set is a collection of similar types of entities that share the same attributes.

For example, all students of a school are a entity set of Student entities.

[GeeksForGeeks](https://www.geeksforgeeks.org/entity-in-dbms/)
### Q3. What is an attribute?
A. An attribute is a property that describes the entity. For example, in a customer database, the attributes might be name, address, and phone number.

In a relational data model, it is depicted as a column. 

[KnowledgeHut](https://www.knowledgehut.com/blog/database/attributes-in-dbms)
### Q4. What is the difference between prime and non-prime attributes?
A. Prime attributes are attributes that are part of a candidate key (Unique Key). 

Non-prime attributes are attributes that are not part of any candidate key (Unique Key).

[TechnoGeeksCS](https://technogeekscs.com/prime-attribute-in-dbms/)
### Q5. Explain a strong and weak entity set with an example.
A. In database design, an entity set is a collection of entities that share common characteristics. 

Entities are objects or concepts that have existence and can be described with a set of attributes or properties. There are two types of entity sets: 
- strong entity sets
- weak entity sets.

| **Characteristics** | **Strong Entity Set** | **Weak Entity Set** |
| --- | --- | --- |
| **Unique Identifier** | Yes (e.g. Employee ID) | No (relies on another entity) |
| **Independent Existence** | Yes (can exist alone) | No (exists with another entity) |
| **Example** | Employee (e.g. John Smith) | Order Item (e.g. Book in Order 1) |
| **ER Model Representation** | Rectangles | Double Rectangles |
| **Key Attributes** | Has its own primary key | Has a partial key (foreign key) |
| **Existence Dependency** | Exists independently | Exists dependent on another entity |
| **Identification** | Identified by its own attributes | Identified by its own and another entity's attributes |

[GeeksForGeeks](https://www.geeksforgeeks.org/difference-between-strong-and-weak-entity/)
### Q6. Explain the type of attributes.
A. There are different types of attributes:
- Simple Attribute
    - An attribute that cannot be further subdivided into components is a simple attribute. 
    - Example: The roll number of a student, the ID number of an employee, gender, and many more. 
    ![Simple Attribute](https://media.geeksforgeeks.org/wp-content/uploads/20240524154118/simple-attr.jpg)
- Composite Attribute
    - An attribute that can be split into components is a composite attribute. 
    - Example: The address can be further split into house number, street number, city, state, country, and pin code, the name can also be split into first name middle name, and last name.
    ![Composite Attribute](https://media.geeksforgeeks.org/wp-content/uploads/20240524154313/composite-attr.jpg)
- Single-Valued Attribute
    - The attribute which takes up only a single value for each entity instance is a single-valued attribute. 
    - Example: The age of a student, Aadhar card number.
    ![Single-Valued Attribute](https://media.geeksforgeeks.org/wp-content/uploads/20240524154405/single-valued.jpg)
- Multi-Valued Attribute
    - The attribute which takes up more than a single value for each entity instance is a multi-valued attribute. And it is represented by double oval shape.
    - Example: Phone number of a student: Landline and mobile. 
    ![Multival attribute](https://media.geeksforgeeks.org/wp-content/uploads/20240524154447/multivalued.jpg)
- Derived Attribute
    - An attribute that can be derived from other attributes is derived attributes. And it is represented by dotted oval shape.
    - Example: Total and average marks of a student, age of an employee that is derived from date of birth. 
    ![Derived Attribute](https://media.geeksforgeeks.org/wp-content/uploads/20240524154624/derived.jpg)
- Key Attribute
    - Key attributes are those attributes that can uniquely identify the entity in the entity set.
    - Example: Roll-No is the key attribute because it can uniquely identify the student. 
- Null Attribute
    - This attribute can take NULL value when entity does not have value for it.

[GeeksForGeeks](https://www.geeksforgeeks.org/types-of-attributes-in-er-model/)
### Q7. Define the following with examples:
- Super key
    - A super key is a set of one or more attributes that uniquely identifies each entity in an entity set.
    - Example: In table 1, the Employee ID attribute is a super key.
- candidate key 
    - A candidate key is a minimal set of attributes that uniquely identifies each entity in an entity set. 
    - A candidate key is a super key that has no redundant attributes.
    - Example: Employee ID attribute is a candidate key.
- primary key 
    - A primary key is a candidate key that is chosen as the unique identifier for an entity set. 
    - It is used to uniquely identify each entity in the entity set.
    - Example: Employee ID attribute is a primary key.
- foreign key
    - A foreign key is an attribute or set of attributes in an entity set that refers to the primary key of another entity set. 
    - It is used to establish relationships between entity sets.
    - Example: In table 2, The Order entity set has a foreign key Customer ID that refers to the primary key Customer ID in the Customer entity set.
- composite key
    - A composite key is a key that consists of two or more attributes that together uniquely identify each entity in an entity set.
    - Example: In table 3, the combination of Order ID and Product ID is a composite key because it uniquely identifies each order item.

Table 1:
| **Employee ID** | **Name** | **Department** |
| --- | --- | --- |
| 101 | John Smith | Sales |
| 102 | Jane Doe | Marketing |
| 103 | Bob Johnson | IT |

Table 2:
| **Order ID** | **Customer ID** | **Order Date** |
| --- | --- | --- |
| 1 | 101 | 2022-01-01 |
| 2 | 101 | 2022-01-15 |
| 3 | 102 | 2022-02-01 |

| **Customer ID** | **Name** | **Address** |
| --- | --- | --- |
| 101 | John Smith | 123 Main St |
| 102 | Jane Doe | 456 Elm St |

Table 3: 
| **Order ID** | **Product ID** | **Quantity** |
| --- | --- | --- |
| 1 | 101 | 2 |
| 1 | 102 | 1 |
| 2 | 101 | 3 |


### Q8. What are the symbols used in ER diagrams?
A. check Q9
### Q9. What is the notation of the ER diagram? Give an example.
A. Refer to:
- [EDrawMax](https://www.edrawmax.com/article/er-diagram-symbols-and-notations.html)
- [Simplilearn](https://www.simplilearn.com/tutorials/sql-tutorial/er-diagram-in-dbms)
### Q10. Draw and ER diagram of these three with notation and symbols:
- University
- Library

A. University: [Image](assets/university.svg)

Library: [Image](assets/library.svg)

### Q11. What are Relationship types, set and degrees of relation?
A. 
Relationship type: 
- The type of relationship between entities, such as the relationship between a student and a class, or between a salary slip and an employee 

Relationship set: 
- A set of relationships of a specific type 

Degree of relationship: 
- The number of entities involved in a relationship 

Cardinality: 
- The number of tuples or rows in a table 
### Q12. What is a relationship? Give an example of 1 to 1 and 1 to many.
A. In a DBMS, a relationship is a connection between two or more entity sets that share common attributes. Relationships are used to establish links between entities and to define how they interact with each other.

There are three main types of relationships:
- One-to-One (1:1)
- One-to-Many (1:N)
- Many-to-Many (M:N)

#### One-to-One (1:1) Relationship

In a 1:1 relationship, each entity in one entity set is related to only one entity in another entity set.

Suppose we have two entity sets: Employee and Employee Details. Each employee has only one set of details, and each set of details belongs to only one employee.

| **Employee ID** | **Name** | **Department** |
| --- | --- | --- |
| 101 | John Smith | Sales |
| 102 | Jane Doe | Marketing |
| 103 | Bob Johnson | IT |

| **Employee ID** | **Address** | **Phone Number** |
| --- | --- | --- |
| 101 | 123 Main St | 123-456-7890 |
| 102 | 456 Elm St | 987-654-3210 |
| 103 | 789 Oak St | 555-123-4567 |

In this example, the Employee ID attribute in the Employee entity set is related to the Employee ID attribute in the Employee Details entity set. This is a 1:1 relationship because each employee has only one set of details, and each set of details belongs to only one employee.

#### One-to-Many (1:N) Relationship

In a 1:N relationship, each entity in one entity set is related to multiple entities in another entity set.

Suppose we have two entity sets: Customer and Order. Each customer can place multiple orders, but each order belongs to only one customer.

| **Customer ID** | **Name** | **Address** |
| --- | --- | --- |
| 101 | John Smith | 123 Main St |
| 102 | Jane Doe | 456 Elm St |
| 103 | Bob Johnson | 789 Oak St |

| **Order ID** | **Customer ID** | **Order Date** |
| --- | --- | --- |
| 1 | 101 | 2022-01-01 |
| 2 | 101 | 2022-01-15 |
| 3 | 102 | 2022-02-01 |
| 4 | 103 | 2022-03-01 |
| 5 | 101 | 2022-04-01 |

In this example, the Customer ID attribute in the Customer entity set is related to the Customer ID attribute in the Order entity set. This is a 1:N relationship because each customer can place multiple orders, but each order belongs to only one customer.

## Source:
- Questions: Dictated in class
