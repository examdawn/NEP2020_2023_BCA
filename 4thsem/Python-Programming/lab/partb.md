---
order: 2
title: Python Lab - Part B
---
# Python Programming - Lab Part B

> [!TIP]
> This Page supports running Python directly from your browser!

::: details  Click for more details. If this feature is not working as expected, [please report it to us on Github!](https://github.com/examdawn/NEP2020_2023_BCA/issues/new)

> [!WARNING]
> This will not work if your browser is too old or does not support Web Assembly/Web Workers. If you're using a privacy focused browser like cromite, please enable JavaScript JIT and WebAssembly from the permissions menu.

If the Run Button doesn't show the run or loading button, try reloading your browser!

It will take some time to load, especially if your internet is slow.

Some examples are run with [JupyterLite](https://jupyterlite.github.io) instead for compatibility with matplotlib and other libraries. The iframe embeds are generated with https://examdawn.github.io/url-py <!-- Personal Note: JupyterLite with SQLite3 needs you to set the db file in another location like /tmp/filename.db https://github.com/jupyterlite/pyodide-kernel/issues/35#issuecomment-1487234353 -->
:::


<!-- ## Program 1: Demonstrate usage of Basic Regular Expressions

-->

## Program 1: Demonstrate use of Basic Regular Expressions
## Program 2: Demonstrate use of Advanced Regular Expressions for Data Validation

```python
import re

def validate_data():
    email = input("Enter Email Addr: ")
    phone = input("Enter Mobile Number: ")
    url = input("Enter a URL: ")
    password = input("Enter Password: ")

    email_regex = r'\S+@\S+\.\S+'
    phone_regex = r'\d{10}'
    url_regex = r'https?://(www\.)?(\S+\.\S+)'
    password_regex = r'.{8,}'

    if not re.fullmatch(email_regex, email):
        print("Invalid Email Address")
    elif not re.fullmatch(phone_regex, phone):
        print("Invalid Phone")
    elif not re.fullmatch(url_regex, url):
        print("Invalid URL")
    elif not re.fullmatch(password_regex, password):
        print("Invalid Password. Minimum 8 Characters.")
    else:
        print("Data is Valid.")
validate_data()
```

::: details Try it out
```python:line-numbers
import re

def validate_data():
    email = input("Enter Email Addr: ")
    phone = input("Enter Mobile Number: ")
    url = input("Enter a URL: ")
    password = input("Enter Password: ")

    email_regex = r'\S+@\S+\.\S+'
    phone_regex = r'\d{10}'
    url_regex = r'https?://(www\.)?(\S+\.\S+)'
    password_regex = r'.{8,}'

    if not re.fullmatch(email_regex, email):
        print("Invalid Email Address")
    elif not re.fullmatch(phone_regex, phone):
        print("Invalid Phone")
    elif not re.fullmatch(url_regex, url):
        print("Invalid URL")
    elif not re.fullmatch(password_regex, password):
        print("Invalid Password. Minimum 8 Characters.")
    else:
        print("Data is Valid.")
validate_data()
```
<Editor id="valid-prg2" />
:::


## Program 3: Demonstrate use of List

```python
my_list = [10, 20, 30, 3.142, 'Python', 'BCA']
print("Initial List: ", my_list)

print("Element at list index 0: ", my_list[0])
print("Element at list index 2: ", my_list[2])

my_list[4] = 'Java'
print("List after modifying an item: ", my_list)

my_list.append('ExamDawn')
print("List after appending an item: ", my_list)

my_list.remove('Java')
print("List after removing an item: ", my_list)

del my_list[0]
print("List after deleting an item: ", my_list)

print("Popped item: ", my_list.pop(1))
print("List after popping an item: ", my_list)

print("Index of 'BCA': ", my_list.index('BCA'))

print("Count of '3.142'", my_list.count(3.142))

print("Length of List: ", len(my_list))

my_list.reverse()
print("Reversed List: ", my_list)

my_list.clear()
print("List after clearing: ", my_list)
```

::: details Try it out
```python:line-numbers
my_list = [10, 20, 30, 3.142, 'Python', 'BCA']
print("Initial List: ", my_list)

print("Element at list index 0: ", my_list[0])
print("Element at list index 2: ", my_list[2])

my_list[4] = 'Java'
print("List after modifying an item: ", my_list)

my_list.append('ExamDawn')
print("List after appending an item: ", my_list)

my_list.remove('Java')
print("List after removing an item: ", my_list)

del my_list[0]
print("List after deleting an item: ", my_list)

print("Popped item: ", my_list.pop(1))
print("List after popping an item: ", my_list)

print("Index of 'BCA': ", my_list.index('BCA'))

print("Count of '3.142'", my_list.count(3.142))

print("Length of List: ", len(my_list))

my_list.reverse()
print("Reversed List: ", my_list)

my_list.clear()
print("List after clearing: ", my_list)
```
<Editor id="list-prg3-b" />
:::

## Program 4: Demonstrate use of Dictionaries
```python
my_dict = {'name': 'Souhrud', 'age': 19, 'city': 'Bangalore'}
print("Initial dictionary:", my_dict)
print("Value for 'name':", my_dict['name'])
print("Value for 'age':", my_dict['age'])

print("Value for 'country':", my_dict.get('country'))

print("Value for 'country' with default:", my_dict.get('country', 'India'))

my_dict['age'] = 25
print("Dictionary after modifying an item:", my_dict)

my_dict['job'] = 'Developer'
print("Dictionary after adding an item:", my_dict)

del my_dict['city']
print("Dictionary after deleting an item by key:", my_dict)

print("Popped item:", my_dict.pop('job'))
print("Dictionary after popping an item:", my_dict)

print("Keys:", list(my_dict.keys()))
print("Values:", list(my_dict.values()))
print("Items:", list(my_dict.items()))

print("Number of items:", len(my_dict))

print("'name' in dictionary:", 'name' in my_dict)
print("'city' in dictionary:", 'city' in my_dict)

my_dict2 = {'country': 'India', 'job': 'Developer'}
my_dict.update(my_dict2)
print("Dictionary after merging:", my_dict)

my_dict.clear()
print("Dictionary after clearing:", my_dict)
```

::: details Try it out
```python:line-numbers
my_dict = {'name': 'Souhrud', 'age': 19, 'city': 'Bangalore'}
print("Initial dictionary:", my_dict)
print("Value for 'name':", my_dict['name'])
print("Value for 'age':", my_dict['age'])

print("Value for 'country':", my_dict.get('country'))

print("Value for 'country' with default:", my_dict.get('country', 'India'))

my_dict['age'] = 25
print("Dictionary after modifying an item:", my_dict)

my_dict['job'] = 'Developer'
print("Dictionary after adding an item:", my_dict)

del my_dict['city']
print("Dictionary after deleting an item by key:", my_dict)

print("Popped item:", my_dict.pop('job'))
print("Dictionary after popping an item:", my_dict)

print("Keys:", list(my_dict.keys()))
print("Values:", list(my_dict.values()))
print("Items:", list(my_dict.items()))

print("Number of items:", len(my_dict))

print("'name' in dictionary:", 'name' in my_dict)
print("'city' in dictionary:", 'city' in my_dict)

my_dict2 = {'country': 'India', 'job': 'Developer'}
my_dict.update(my_dict2)
print("Dictionary after merging:", my_dict)

my_dict.clear()
print("Dictionary after clearing:", my_dict)
```
:::

## Program 5: Create SQLite Database and Perform Operations on tables
```python
import sqlite3

def display_rows(cursor):
    rows = cursor.fetchall()
    for row in rows:
        print(row)

conn = sqlite3.connect('employee.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS emp")

cursor.execute("""
CREATE TABLE emp
(empno INTEGER PRIMARY KEY,
empname TEXT,
salary REAL,
department TEXT)""")


print("Table Created")
cursor.execute("INSERT INTO emp VALUES (1 , 'Souhrud' , 50000 , 'IT')")
cursor.execute("INSERT INTO emp VALUES (2 , 'John' , 35000 , 'Sales')")
conn.commit()
print("Records inserted")


cursor.execute("SELECT * from emp")
print("Records in the table:")
display_rows(cursor)
cursor.execute("UPDATE emp SET salary = 100000 WHERE empno = 1")
conn.commit()
print("Record Updated")

cursor.execute("SELECT * from emp")
print("Records in the table after update:")
display_rows(cursor)

cursor.execute("DROP TABLE emp")
conn.commit()
print("Table Dropped")

conn.close()
```

::: details Try it out
```python:line-numbers
import sqlite3

def display_rows(cursor):
    rows = cursor.fetchall()
    for row in rows:
        print(row)

conn = sqlite3.connect('employee.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS emp")

cursor.execute("""
CREATE TABLE emp
(empno INTEGER PRIMARY KEY,
empname TEXT,
salary REAL,
department TEXT)""")


print("Table Created")
cursor.execute("INSERT INTO emp VALUES (1 , 'Souhrud' , 50000 , 'IT')")
cursor.execute("INSERT INTO emp VALUES (2 , 'John' , 35000 , 'Sales')")
conn.commit()
print("Records inserted")


cursor.execute("SELECT * from emp")
print("Records in the table:")
display_rows(cursor)
cursor.execute("UPDATE emp SET salary = 100000 WHERE empno = 1")
conn.commit()
print("Record Updated")

cursor.execute("SELECT * from emp")
print("Records in the table after update:")
display_rows(cursor)

cursor.execute("DROP TABLE emp")
conn.commit()
print("Table Dropped")

conn.close()
```
:::

## Program 6: Create GUI using Tkinter Module 

## Program 7: Demonstrate exceptions in Python

## Program 8: Drawing Line Chart and Bar Chart using Matplotlib

#### Line Chart

```python
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,4,9,16,25]

plt.plot(x,y)

plt.title("Simple Line Graph")
plt.xlabel("Number")
plt.ylabel("Square")

plt.show()

plt.savefig("simple_line_graph.png")
```

::: details Try it out
<a href="https://examdawn.pages.dev/jupyterlite/dist/repl/index.html?kernel=python&code=import%20matplotlib.pyplot%20as%20plt%0A%0Ax%20%3D%20%5B1%2C2%2C3%2C4%2C5%5D%0Ay%20%3D%20%5B1%2C4%2C9%2C16%2C25%5D%0A%0Aplt.plot(x%2Cy)%0A%0Aplt.title(%22Simple%20Line%20Graph%22)%0Aplt.xlabel(%22Number%22)%0Aplt.ylabel(%22Square%22)%0A%0Aplt.show()%0A%0Aplt.savefig(%22simple_line_graph.png%22)%0A&execute=1" target="_blank">Open in New Tab</a>
<iframe src="https://examdawn.pages.dev/jupyterlite/dist/repl/index.html?kernel=python&code=import%20matplotlib.pyplot%20as%20plt%0A%0Ax%20%3D%20%5B1%2C2%2C3%2C4%2C5%5D%0Ay%20%3D%20%5B1%2C4%2C9%2C16%2C25%5D%0A%0Aplt.plot(x%2Cy)%0A%0Aplt.title(%22Simple%20Line%20Graph%22)%0Aplt.xlabel(%22Number%22)%0Aplt.ylabel(%22Square%22)%0A%0Aplt.show()%0A%0Aplt.savefig(%22simple_line_graph.png%22)%0A&execute=1" width="100%" height="400%"></iframe>
:::

#### Bar Chart

```python
import matplotlib.pyplot as plt


courses = ["BCA","BCOM", "BBA", "BSc", "BA" ]
count = [120, 180, 60, 30, 80]
plt.bar(courses, count, color="maroon", width=0.4)

plt.xlabel("Courses")
plt.ylabel("Count")
plt.title("Count of Students in Different Courses")

plt.show()
```

::: details Try it out
<a href="https://examdawn.pages.dev/jupyterlite/dist/repl/index.html?kernel=python&code=import%20matplotlib.pyplot%20as%20plt%0A%0A%0Acourses%20%3D%20%5B%22BCA%22%2C%22BCOM%22%2C%20%22BBA%22%2C%20%22BSc%22%2C%20%22BA%22%20%5D%0Acount%20%3D%20%5B120%2C%20180%2C%2060%2C%2030%2C%2080%5D%0Aplt.bar(courses%2C%20count%2C%20color%3D%22maroon%22%2C%20width%3D0.4)%0A%0Aplt.xlabel(%22Courses%22)%0Aplt.ylabel(%22Count%22)%0Aplt.title(%22Count%20of%20Students%20in%20Different%20Courses%22)%0A%0Aplt.show()&execute=1" target="_blank">Open in New Tab</a>
<iframe src="https://examdawn.pages.dev/jupyterlite/dist/repl/index.html?kernel=python&code=import%20matplotlib.pyplot%20as%20plt%0A%0A%0Acourses%20%3D%20%5B%22BCA%22%2C%22BCOM%22%2C%20%22BBA%22%2C%20%22BSc%22%2C%20%22BA%22%20%5D%0Acount%20%3D%20%5B120%2C%20180%2C%2060%2C%2030%2C%2080%5D%0Aplt.bar(courses%2C%20count%2C%20color%3D%22maroon%22%2C%20width%3D0.4)%0A%0Aplt.xlabel(%22Courses%22)%0Aplt.ylabel(%22Count%22)%0Aplt.title(%22Count%20of%20Students%20in%20Different%20Courses%22)%0A%0Aplt.show()&execute=1" width="100%" height="400%"></iframe>
                
:::


## Program 9: Drawing Histograms and Pie Chart using Matplotlib

## Program 10: Create array using Numpy and Perform Operations on Array

## PRogram 11: Create Data Frame from Excel Sheets using Pandas and Perform Operations on Data Frames


<!--

Usage Example for code:

## Program 1: Program to print: Hello world

```python
print("Hello world")
```

::: details Try it out
```python:line-numbers
print("Hello world")
```
<Editor id="helloworld-trial" />
:::


-->
