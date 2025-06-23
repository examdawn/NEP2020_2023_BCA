---
order: 2
title: PP - Unit 1 Solved
---

## 1. Features of Python 
The features of Python are as follows:
- Simple and Easy to Learn
- Interpreted Language
- Dynamically Typed Language
- OOP Language 
- High Level Language

## 2. Applications of Python
The Applications of Python are as follows:
- Web Development
- Game Development
- ML and AI
- Software Development
- Network Programming 

## 3. Describe in detail about Python data types.
The Python Data-Types are as follows:
### 1. Numeric Types
- **Integers (`int`)**: Whole numbers, both positive and negative, without a decimal point. For example, `5`, `-3`, and `42`.
- **Floating Point Numbers (`float`)**: Numbers that contain a decimal point. For example, `3.14`, `-0.001`, and `2.0`.
- **Complex Numbers (`complex`)**: Numbers that have a real and an imaginary part, represented as `a + bj`, where `a` is the real part and `b` is the imaginary part. For example, `2 + 3j`.
### 2. Sequence Types
- **Strings (`str`)**: A sequence of characters enclosed in single, double, or triple quotes. For example, `'Hello'`, `"World"`, or `"""This is a multi-line string."""`.
- **Lists (`list`)**: Ordered, mutable collections of items, which can be of different types. Lists are defined using square brackets. For example, `[1, 2, 3]`, `['apple', 'banana', 'cherry']`.
- **Tuples (`tuple`)**: Ordered, immutable collections of items, defined using parentheses. For example, `(1, 2, 3)` or `('a', 'b', 'c')`.
### 3. Mapping Type
- **Dictionaries (`dict`)**: Unordered collections of key-value pairs, defined using curly braces. Keys must be unique and immutable. For example, `{'name': 'Alice', 'age': 25}`.
### 4. Set Types
- **Sets (`set`)**: Unordered collections of unique items, defined using curly braces. For example, `{1, 2, 3}`. Sets are useful for membership testing and eliminating duplicate entries.
- **Frozen Sets (`frozenset`)**: Immutable versions of sets, which cannot be modified after creation. For example, `frozenset([1, 2, 3])`.
### 5. Boolean Type
- **Booleans (`bool`)**: Represents one of two values: `True` or `False`. This type is often used in conditional statements and logical operations.
### 6. None Type
- **NoneType (`None`)**: Represents the absence of a value or a null value. It is a singleton in Python, meaning there is only one instance of `None`.

## 4. Describe operators in Python.
In Python programming, Operators in general are used to perform operations on values and variables. These are standard symbols used for logical and arithmetic operations. The different types of Python operators are:
### 1. Arithmetic Operators 
- It is used to perform basic mathematical operations like addition, subtraction, multiplication and division.
### 2. Comparison Operators 
- It compares the values and returns either True or False according to the condition.
### 3. Logical Operators  
- It is used to combine conditional statements.
### 4. Bitwise Operators 
- It acts on bits and perform bit-by-bit operations. These are used to operate on binary numbers.
### 5. Assignment Operators 
- It is used to assign values to the variables. This operator is used to assign the value of the right side of the expression to the left side operand.
### 6. Identity Operators 
- In Python, `is` and `is not` are the identity operators both are used to check if two values are located on the same part of the memory. Two variables that are equal do not imply that they are identical. 
### 7. Membership Operators 
- In Python, `in` and `not in` are the membership operators that are used to test whether a value or variable is in a sequence.
### 8. Ternary Operator 
It's a operators that evaluate something based on a condition being true or false.  

[GeeksForGeeks](https://www.geeksforgeeks.org/python/python-operators/)

## 5. What is a Python Comment
- Comments can be used to explain Python code, make the code more readable and also prevent execution when testing code.

[W3Schools](https://www.w3schools.com/python/python_comments.asp)

## 6. What is a Python Indentation
In Python, indentation is used to define blocks of code. It tells the Python interpreter that a group of statements belongs to a specific block. All statements with the same level of indentation are considered part of the same block. Indentation is achieved using whitespace (spaces or tabs) at the beginning of each line.

[GeeksForGeeks](https://www.geeksforgeeks.org/python/indentation-in-python/)

## 7. What is console input & console output in Python.
Console (also called Shell) is basically a command line interpreter that takes input from the user with `input()` function and print output with `print()` function.
- ***Console input*** is the method by which a program receives data from the user. 
- ***Console output:*** is the method by which a program displays data to the user. 
EXAMPLE:
```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

## 8. Describe in detail the control flow in python.
A program’s control flow is the order in which the program’s code executes. The control flow of a Python program is regulated by conditional statements, loops, and function calls.
Python has three types of control structures:
1. Sequential: Default mode
2. Selection: Used for decisions and branching. They are `if`, `if-else`, `nested if`, `if-elif-else`.
3. Repetition: Used for looping, i.e., repeating a code multiple times. They are `for loop`, `while loop`.

[Educactive](https://www.educative.io/answers/what-are-control-flow-statements-in-python)

## 9. Describe Looping statements in Python with example.
Looping simplifies complicated problems into smooth ones. It allows programmers to modify the flow of the program so that rather than writing the same code again and again, programmers are able to repeat the code a finite number of times.

1. ***For Loop:***
- The for loop is used in cases where a programmer needs to execute a part of the code until the given condition is satisfied. The for loop is also called a pre-tested loop. It is best to use a for loop if the number of iterations is known in advance.
EXAMPLE:

Input:
```python
a = 5
for i in range(0, a):
    print(i)
```
Output:
```txt
0
1
2
3
4
```

2. ***While Loop:***
- The while loop is to be used in situations where the number of iterations is unknown at first. The block of statements is executed in the while loop until the condition specified in the while loop is satisfied. It is also called a pre-tested loop. In Python, the while loop executes the statement or group of statements repeatedly while the given condition is True. And when the condition becomes false, the loop ends and moves to the next statement after the loop.
EXAMPLE
Input:
```python
count = 0
while (count < 5):
    count = count + 1
    print("Ligma")
```
Output:
```txt
Ligma
Ligma
Ligma
Ligma
Ligma
```

[flexiple](https://flexiple.com/python/looping-statements-in-python)

## 10. Explain the Membership operator
Membership operators are used to test if a value exists within a sequence (like a string, list, tuple, set, or dictionary):
| Operator   | Description                                                                 | Syntax     |
|------------|-----------------------------------------------------------------------------|-------------|
| `in`         | Returns True if a sequence with the specified value is present in the object | x in y     |
| `not in`     | Returns True if a sequence with the specified value is not present in the object | x not in y |

## 11. Conditional statement in python
Conditional statements in Python are used to execute certain blocks of code based on specific conditions. These statements help control the flow of a program, making it behave differently in different situations. The types of conditional statements are:
1. if statement
2. if-else statement
3. if-else-if ladder statement