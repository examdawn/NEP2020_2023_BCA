---
order: 3
title: PP - Unit 2 Solved
---
# Python Programming - Unit 2

## Q1. What are errors? Explain the following types of errors: 
- Syntax
- logical
- runtime error

Errors are problems in a program that causes the program to stop its execution. On the other hand, exceptions are raised when some internal events change the program's normal flow. 
- Syntax Errors 
    - occur when the code doesn't follow Python's rules, like using incorrect grammar in English.
    - Python stops and points out the issue before running the program.
- Logical Errors
    - Subtle bugs in the program that allow the code to run, but produce incorrect or unintended results. 
    - These are often harder to detect since the program doesn’t crash, but the output is not as expected.
- Runtime Errors
    - A runtime error in a program is an error that occurs while the program is running after being successfully compiled.
    - Runtime errors are commonly called referred to as "bugs" and are often found during the debugging process
[GeeksForGeeks(Syntax and Logical Errors)](https://www.geeksforgeeks.org/python/errors-and-exceptions-in-python/)

[GeeksForGeeks(Runtime Errors)](https://www.geeksforgeeks.org/runtime-errors/)

## Q2. What is an exception? Explain Exception Handling and Describe about any four types of built-in exceptions. 
An exception in Python is an error that occurs during program execution, interrupting the normal flow of the program. 
- Exception handling allows you to manage these errors gracefully using try and except blocks, so your program can respond to problems without crashing


```python
try:
    # Code that might raise an exception
except ExceptionType:
    # Code to handle the exception
```

### Common Built-in exceptions
**ZeroDivisionError**: Raised when you try to divide by zero.
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

**ValueError**: Raised when a function receives an argument of the correct type but an inappropriate value (e.g., converting a letter to int).
```python
try:
    num = int("abc")
except ValueError:
    print("Invalid value for integer conversion")
```

**TypeError**: Raised when an operation is applied to an object of inappropriate type (e.g., adding a string and an integer).
```python
try:
    result = "2" + 3
except TypeError:
    print("Cannot add string and integer")
```
**NameError**: Raised when a variable is not defined.
```python
try:
    print(x)
except NameError:
    print("Variable x is not defined")
```

[Python Docs](https://docs.python.org/3/tutorial/errors.html#handling-exceptions)


## Q3. Differentiate between syntax error and exception.
| Feature            | Syntax Error                                              | Exception                                              |
|--------------------|----------------------------------------------------------|--------------------------------------------------------|
| Definition         | Error caused by violating Python's grammar or syntax rules| Error detected during program execution (runtime error)|
| When Occurs        | During code parsing, before execution starts              | During program execution, after code is syntactically correct |
| Example            | `if True print("Hello")` (missing colon)                  | `10 / 0` (division by zero)                            |
| Handling           | Cannot be handled with try-except; must fix the code      | Can be handled using try-except blocks                 |
| Effect             | Prevents the program from running at all                  | Interrupts normal flow, but program can recover if handled |
| Error Message Type | SyntaxError, IndentationError, etc.                       | ZeroDivisionError, ValueError, NameError, etc.         |

## Q4. Describe strings in python with any four operations performed on strings. 
A string is a sequence of characters. 
- Python treats anything inside quotes as a string. 
- This includes letters, numbers, and symbols. 
- Python has no character data type so single character is a string of length 1.
- It is an iterable sequence.
- Single Line strings are made by wrapping single or double quotes around a sentence
    - Eg. `"Hello"` or `'Hello'`
- Multiline Strings are made by wrapping content in three single/double quotes
    - Eg. ```
        """Hello
        World"""
        ```

| Method        | Description                                           | Example                          | Expected Output                  |
|---------------|------------------------------------------------------|----------------------------------|----------------------------------|
| capitalize()  | Converts the first character to upper case           | `"hello world".capitalize()`     | `Hello world`                    |
| casefold()    | Converts string into lower case                      | `"HELLO WORLD".casefold()`       | `hello world`                    |
| center()      | Returns a centered string                            | `"hello".center(11, '*')`        | `***hello***`                    |
| count()       | Returns the number of times a specified value occurs in a string | `"banana".count("a")`            | `3`                              |


[W3Schools](https://www.w3schools.com/python/python_ref_string.asp)


## Q5. What is a raw string?
In Python, a raw string is a string literal prefixed with an r or R. 
- The primary purpose of raw strings is to treat backslashes (`\`) as literal characters
- preventing them from being interpreted as escape sequences.

eg. 

```python
print("Hello \there") # Expected Output: Hello 	here
print(r"Hello \there") # Expected Output: Hello \there
```

## Q6. Program to display multiplication table
```python
for i in range(1,11):
    print(f"5 x {i} = {5*i}")
```

::: details Show Output {open}
```
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```
:::

## Q7. Program to find factorial with recursive function
```python
def fact(i):
    if i-1 >= 0:
        return i * fact(i - 1)
    else:
        return 1

print(f"Factorial of 3 is {fact(3)}") # Find and Output Factorial of 3
```
::: details Show Output {open}
```
Factorial of 3 is 6
```

Verify: 3 * 2 * 1 = 6 ✅
:::
<!--
What are errors? Explain the following types of errors: 
- Syntax
- logical
- runtime error

What is an exception? Describe about any four types of built-in exceptions. 

Explain Exception Handling

Difference between syntax error and exception.

Explain exception handling mechanism in python.

Describe strings in python with any four operations performed on strings. 

What is a raw string?

Explain String formatting using `%` operator

Program to find factorial with recursive function

Program to display multiplication table

-->