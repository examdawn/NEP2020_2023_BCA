# Assignment 2

## 1. Write a note on decomposition with examples.
Decomposition refers to the division of tables into multiple tables to produce consistency in the data. When we divide a table into multiple tables or divide a relation into multiple relations, then this process is termed Decomposition in DBMS. We perform decomposition in DBMS when we want to process a particular data set. It is performed in a database management system when we need to ensure consistency and remove anomalies and duplicate data present in the database. When we perform decomposition in DBMS, we must try to ensure that no information or data is lost. 
[(1)](https://www.geeksforgeeks.org/decomposition-in-dbms/)

### Types of Decomposition

There are two types of Decomposition:  
![Types](https://media.geeksforgeeks.org/wp-content/uploads/20240225103808/Screenshot-2024-02-25-103756.png)

### Lossless Decomposition
The process in which where we can regain the original relation R with the help of joins from the multiple relations formed after decomposition. This process is termed as lossless decomposition.

It is used to remove the redundant data from the database while retaining the useful information.

The lossless decomposition tries to ensure following things:
- While regaining the original relation, no information should be lost.
- If we perform join operation on the sub-divided relations, we must get the original relation.

- EXAMPLE:
    - We have:

        | **A** | **B** | **C** |
        |-------|-------|-------|
        |  55   |  16   |  27   |
        |  48   |  52   |  89   |

    - Now, we decompose this relation into two sub relations R1 and R2  

        | **A** | **B** |
        |-------|-------|
        |  55   |  16   |
        |  48   |  52   |

        | **B** | **C** |
        |-------|-------|
        |  16   |  27   |
        |  52   |  89   |

    - After performing the Join operation we get the same original relation

        | **A** | **B** | **C** |
        |-------|-------|-------|
        |  55   |  16   |  27   |
        |  48   |  52   |  89   |


### Lossy decomposition:
As the name suggests, lossy decomposition means when we perform join operation on the sub-relations it doesn't result to the same relation which was decomposed. After the join operation, we always found some extraneous tuples. These extra tuples genrates difficulty for the user to identify the original tuples.

- EXAMPLE:
    - We have:

        | **A** | **B** | **C** |
        |-------|-------|-------|
        |   1   |   2   |   1   |
        |   2   |   5   |   3   |
        |   3   |   3   |   3   |

    - Now, we decompose it into sub-relations R1 and R2

        | **A** | **B** |
        |-------|-------|
        |   1   |   2   |
        |   2   |   5   |
        |   3   |   3   |

        | **B** | **C** |
        |-------|-------|
        |   2   |   1   |
        |   5   |   3   |
        |   3   |   3   |

    - Now After performing join operation

        | **A** | **B** | **C** |
        |-------|-------|-------|
        |   1   |   2   |   1   |
        |   2   |   5   |   3   |
        |   2   |   3   |   3   |
        |   3   |   5   |   3   |
        |   3   |   3   |   3   |


## 2. What is Normalisation? Explain three types of Normalisation with examples.
Normalization is the process of organizing the data in the database.
Normalization is used to minimize the redundancy from a relation or set of relations. It is also used to eliminate undesirable characteristics like Insertion, Update, and Deletion Anomalies.
Normalization divides the larger table into smaller and links them using relationships.
The normal form is used to reduce redundancy from the database table.  [(1)](https://www.javatpoint.com/dbms-normalization)  
Types of Normal Forms: