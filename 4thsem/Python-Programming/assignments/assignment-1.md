---
order: 0
title: Python Assignment 1(28/2/25)
---
# Python Assignment 1(28/2/25)

> [!TIP]
> This Page supports running Python directly from your browser!

::: details  Click for more details. If this feature is not working as expected, [please report it to us on Github!](https://github.com/examdawn/NEP2020_2023_BCAissues/new)

> [!WARNING]
> This will not work if your browser is too old or does not support Web Assembly/Web Workers. If you're using a privacy focused browser like cromite, please enable JavaScript JIT and WebAssembly from the permissions menu.

If the Run Button doesn't show the run or loading button, try reloading your browser!

It will take some time to load, especially if your internet is slow.
:::

## Q1. Explain the Features of Python

Python has many useful characteristics:
- Python is easy to learn and use
- High level language, don't need to bother with low level concepts like Garbage Collection and more.
- Python is interpreted, where the code executes line-by-line so you know where the error came from.
- Python is Open Source
    - Python software and documentation are licensed under the Python Software Foundation License Version 2.
    - Starting with Python 3.8.6, examples, recipes, and other code in the documentation are dual licensed under the PSF License Version 2 and the Zero-Clause BSD license.
- Don't need to port apps between platforms, it runs as-is on any supported platform

## Q2. Explain Tokens with examples

| Tokens | Explanation | Some Examples |
| --- | --- | --- |
| Keyword | Reserved Words, cannot use as Identifiers.\nThey have a distinct meaning | True, for |
| Identifier | Name that is given to class, function, variable, etc | `a = 5` Here, `a` is the identifier |
| Operator | Performs a specific action with the given operands | `a+5` Here, `+` is the operator and it will add the value of a and 5 together |
| Literal | Data Elements with a fixed value | lists, tuples, dictionaries |
| Punctuators | Used to structure the sentences and syntax of python code | `,`, `#`, `\`, `()`, `{}` |

[Unacademy](https://unacademy.com/content/cbse-class-11/study-material/computer-science/python-tokens/)
## Q3. Explain the Applications of Python
- Web Development: Django and Flask to make websites
- Data Analysis: Graphing libraries like numpy, scipy to visualize data
- AI Libraries
- Game development using PyGame
- Web Scraping using Selenium Browser
- Desktop GUI apps using TKinter, PyQT, etc
## Q4. Explain different Data Types of Python
| Category      | Type Names                  | Description                     |
|---------------|-----------------------------|---------------------------------|
| Text          | `str`                      | `Textual data representation`(string)  |
| Numeric       | `int`, `float`, `complex`  | `Numbers with various precision` |
| Sequence      | `list`, `tuple`, `range`   | `Ordered collection containers`  |
| Mapping       | `dict`                     | `Key-value pair associations`    |
| Set           | `set`, `frozenset`         | `Unique element collections`     |
| Boolean       | `bool`                     | `True/False value storage`       |
| Binary        | `bytes`, `bytearray`, `memoryview` | `Binary data handling`   |
| None          | `NoneType`                 | `Representation of null`         |

[W3Schools](https://www.w3schools.com/python/python_datatypes.asp)
## Q5. Explain Different Types of Conversion with Examples
- Implicit conversion or coercion is when data type conversion takes place either during compilation or during run time and is handled directly by Python for you. 
    - Example:
      ```python:line-numbers
      a_int = 1
      b_float = 1.0
      c_sum = a_int + b_float
      print(c_sum)
      ``` 
      <Editor id="implicit-trial-assign1" />
- Explicit data type conversion, often referred to as type casting, occurs when you deliberately convert a value from one data type to another
    - Syntax: `target_data_type(expression)`
    - Example:
      ```python:line-numbers
      a = int(3.14)
      print(a)
      ```
      <Editor id="explicit-trial-assign1" />
[DataCamp](https://www.datacamp.com/tutorial/python-data-type-conversion)
