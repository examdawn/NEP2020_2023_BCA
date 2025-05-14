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

```python
import re 
text = "Hello There!" 
#re.match() tries to match a pattern at the beginning of the string. 
match = re.match("Hello", text) 
print("Match: ", match.group() if match else None) 
# re.search() searches the string for a match, and returns a Match object if there is a match. 
search = re.search("BCA", text) 
print("Search: ", search.group() if search else None) 
#re.findall() returns a list containing all matches. 
findall = re.findall("[0-9]", text) 
print("Findall: ", findall) 
# re.split() returns a list where the string has been split at each match. 
split = re.split("\s", text) 
print("Split: ", split) 
#re.sub() replaces the matches with the text of choice. 
sub = re.sub("4th", "Third", text) 
print("Sub: ", sub)
```
::: details Try it out
```python:line-numbers
import re 
text = "Hello There!" 
#re.match() tries to match a pattern at the beginning of the string. 
match = re.match("Hello", text) 
print("Match: ", match.group() if match else None) 
# re.search() searches the string for a match, and returns a Match object if there is a match. 
search = re.search("BCA", text) 
print("Search: ", search.group() if search else None) 
#re.findall() returns a list containing all matches. 
findall = re.findall("[0-9]", text) 
print("Findall: ", findall) 
# re.split() returns a list where the string has been split at each match. 
split = re.split("\s", text) 
print("Split: ", split) 
#re.sub() replaces the matches with the text of choice. 
sub = re.sub("4th", "Third", text) 
print("Sub: ", sub)
```
:::

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
<a href="https://examdawn.pages.dev/jupyterlite/dist/repl/index.html?kernel=python&code=import%20sqlite3%0A%0Adef%20display_rows(cursor)%3A%0A%20%20%20%20rows%20%3D%20cursor.fetchall()%0A%20%20%20%20for%20row%20in%20rows%3A%0A%20%20%20%20%20%20%20%20print(row)%0A%0Aconn%20%3D%20sqlite3.connect('%2Ftmp%2Femployee.db')%0Acursor%20%3D%20conn.cursor()%0A%0Acursor.execute(%22DROP%20TABLE%20IF%20EXISTS%20emp%22)%0A%0Acursor.execute(%22%22%22%0ACREATE%20TABLE%20emp%0A(empno%20INTEGER%20PRIMARY%20KEY%2C%0Aempname%20TEXT%2C%0Asalary%20REAL%2C%0Adepartment%20TEXT)%22%22%22)%0A%0A%0Aprint(%22Table%20Created%22)%0Acursor.execute(%22INSERT%20INTO%20emp%20VALUES%20(1%20%2C%20'Souhrud'%20%2C%2050000%20%2C%20'IT')%22)%0Acursor.execute(%22INSERT%20INTO%20emp%20VALUES%20(2%20%2C%20'John'%20%2C%2035000%20%2C%20'Sales')%22)%0Aconn.commit()%0Aprint(%22Records%20inserted%22)%0A%0A%0Acursor.execute(%22SELECT%20*%20from%20emp%22)%0Aprint(%22Records%20in%20the%20table%3A%22)%0Adisplay_rows(cursor)%0Acursor.execute(%22UPDATE%20emp%20SET%20salary%20%3D%20100000%20WHERE%20empno%20%3D%201%22)%0Aconn.commit()%0Aprint(%22Record%20Updated%22)%0A%0Acursor.execute(%22SELECT%20*%20from%20emp%22)%0Aprint(%22Records%20in%20the%20table%20after%20update%3A%22)%0Adisplay_rows(cursor)%0A%0Acursor.execute(%22DROP%20TABLE%20emp%22)%0Aconn.commit()%0Aprint(%22Table%20Dropped%22)%0A%0Aconn.close()&execute=1" target="_blank">Open in New Tab</a>
<iframe src="https://examdawn.pages.dev/jupyterlite/dist/repl/index.html?kernel=python&code=import%20sqlite3%0A%0Adef%20display_rows(cursor)%3A%0A%20%20%20%20rows%20%3D%20cursor.fetchall()%0A%20%20%20%20for%20row%20in%20rows%3A%0A%20%20%20%20%20%20%20%20print(row)%0A%0Aconn%20%3D%20sqlite3.connect('%2Ftmp%2Femployee.db')%0Acursor%20%3D%20conn.cursor()%0A%0Acursor.execute(%22DROP%20TABLE%20IF%20EXISTS%20emp%22)%0A%0Acursor.execute(%22%22%22%0ACREATE%20TABLE%20emp%0A(empno%20INTEGER%20PRIMARY%20KEY%2C%0Aempname%20TEXT%2C%0Asalary%20REAL%2C%0Adepartment%20TEXT)%22%22%22)%0A%0A%0Aprint(%22Table%20Created%22)%0Acursor.execute(%22INSERT%20INTO%20emp%20VALUES%20(1%20%2C%20'Souhrud'%20%2C%2050000%20%2C%20'IT')%22)%0Acursor.execute(%22INSERT%20INTO%20emp%20VALUES%20(2%20%2C%20'John'%20%2C%2035000%20%2C%20'Sales')%22)%0Aconn.commit()%0Aprint(%22Records%20inserted%22)%0A%0A%0Acursor.execute(%22SELECT%20*%20from%20emp%22)%0Aprint(%22Records%20in%20the%20table%3A%22)%0Adisplay_rows(cursor)%0Acursor.execute(%22UPDATE%20emp%20SET%20salary%20%3D%20100000%20WHERE%20empno%20%3D%201%22)%0Aconn.commit()%0Aprint(%22Record%20Updated%22)%0A%0Acursor.execute(%22SELECT%20*%20from%20emp%22)%0Aprint(%22Records%20in%20the%20table%20after%20update%3A%22)%0Adisplay_rows(cursor)%0A%0Acursor.execute(%22DROP%20TABLE%20emp%22)%0Aconn.commit()%0Aprint(%22Table%20Dropped%22)%0A%0Aconn.close()&execute=1" width="100%" height="100%"></iframe>
:::

## Program 6: Create GUI using Tkinter Module 

```python
import tkinter as tk
from tkinter import messagebox, ttk

def submit():
    messagebox.showinfo("Submitted", "Form Submitted Successfully.")

root = tk.Tk()
root.geometry("300x300")

root.title("Student Registration Form")

tk.Label(root, text="Student Name").grid(row=0)
tk.Label(root, text="Phone Number").grid(row=1)
tk.Label(root, text="Email Address").grid(row=2)
tk.Label(root, text="Residential Address").grid(row=3)
tk.Label(root, text="Gender").grid(row=4)
tk.Label(root, text="Course").grid(row=5)


name_entry = tk.Entry(root)
phone_entry = tk.Entry(root)
email_entry = tk.Entry(root)
address_text = tk.Text(root, width=20, height=5)

name_entry.grid(row=0, column=1)
phone_entry.grid(row=1, column=1)
email_entry.grid(row=2, column=1)
address_text.grid(row=3, column=1)

gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=4,column=1, sticky='w')
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=4,column=1, sticky='e')

course_var = tk.StringVar()
course_combobox = ttk.Combobox(root, textvariable=course_var)
course_combobox['values'] = ('BCA','BBA','BCOM')
course_combobox.grid(row=5, column=1)

tk.Button(root, text="Submit", command=submit).grid(row=10,column=1)

root.mainloop()

```
TODO: Upload output
## Program 7: Demonstrate exceptions in Python
```python
try: 
    num = int(input("Enter a number: ")) 
except ValueError: 
    print("That's not a valid number!") 
else: 
    print (f"You entered {num}.") 
finally: 
    print("This statement is always executed.")
```
::: details Try it out
```python:line-numbers
try: 
    num = int(input("Enter a number: ")) 
except ValueError: 
    print("That's not a valid number!") 
else: 
    print (f"You entered {num}.") 
finally: 
    print("This statement is always executed.")
```
:::
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

#### Histogram
```python
import matplotlib.pyplot as plt 
ages = [25, 22, 23, 23, 30, 31, 22, 35, 34, 56, 27, 45, 41, 19, 19, 26, 32, 33, 45, 40] 
plt.hist(ages, bins=5, edgecolor='black') 
plt.title('Ages of Customers')
plt.xlabel('Age')
plt.ylabel('Number')

plt.show()
```

::: details Try it out
<a href="https://examdawn.pages.dev/jupyterlite/dist/repl/index.html?kernel=python&code=import%20matplotlib.pyplot%20as%20plt%20%0Aages%20%3D%20%5B25%2C%2022%2C%2023%2C%2023%2C%2030%2C%2031%2C%2022%2C%2035%2C%2034%2C%2056%2C%2027%2C%2045%2C%2041%2C%2019%2C%2019%2C%2026%2C%2032%2C%2033%2C%2045%2C%2040%5D%20%0Aplt.hist(ages%2C%20bins%3D5%2C%20edgecolor%3D'black')%20%0Aplt.title('Ages%20of%20Customers')%0Aplt.xlabel('Age')%0Aplt.ylabel('Number')%0A%0Aplt.show()&execute=1" target="_blank">Open in New Tab</a>
<iframe src="https://examdawn.pages.dev/jupyterlite/dist/repl/index.html?kernel=python&code=import%20matplotlib.pyplot%20as%20plt%20%0Aages%20%3D%20%5B25%2C%2022%2C%2023%2C%2023%2C%2030%2C%2031%2C%2022%2C%2035%2C%2034%2C%2056%2C%2027%2C%2045%2C%2041%2C%2019%2C%2019%2C%2026%2C%2032%2C%2033%2C%2045%2C%2040%5D%20%0Aplt.hist(ages%2C%20bins%3D5%2C%20edgecolor%3D'black')%20%0Aplt.title('Ages%20of%20Customers')%0Aplt.xlabel('Age')%0Aplt.ylabel('Number')%0A%0Aplt.show()&execute=1" width="100%" height="100%"></iframe>
:::


#### Pie Chart

```python
import matplotlib.pyplot as plt 
# Data 
languages = ['Python', 'Java', 'C++', 'JavaScript', 'C#'] 
votes = [250, 150, 100, 75, 50] 
# Create a pie chart 
plt.figure(figsize=[5,5]) 
plt.pie(votes, labels=languages, autopct='%1.1f%%') 
plt.title('Favorite Programming Languages') 
plt.show()
```

::: details Try it out
<a href="https://examdawn.pages.dev/jupyterlite/dist/repl/index.html?kernel=python&code=import%20matplotlib.pyplot%20as%20plt%20%0A%23%20Data%20%0Alanguages%20%3D%20%5B'Python'%2C%20'Java'%2C%20'C%2B%2B'%2C%20'JavaScript'%2C%20'C%23'%5D%20%0Avotes%20%3D%20%5B250%2C%20150%2C%20100%2C%2075%2C%2050%5D%20%0A%23%20Create%20a%20pie%20chart%20%0Aplt.figure(figsize%3D%5B5%2C5%5D)%20%0Aplt.pie(votes%2C%20labels%3Dlanguages%2C%20autopct%3D'%251.1f%25%25')%20%0Aplt.title('Favorite%20Programming%20Languages')%20%0Aplt.show()%0A&execute=1" target="_blank">Open in New Tab</a>
<iframe src="https://examdawn.pages.dev/jupyterlite/dist/repl/index.html?kernel=python&code=import%20matplotlib.pyplot%20as%20plt%20%0A%23%20Data%20%0Alanguages%20%3D%20%5B'Python'%2C%20'Java'%2C%20'C%2B%2B'%2C%20'JavaScript'%2C%20'C%23'%5D%20%0Avotes%20%3D%20%5B250%2C%20150%2C%20100%2C%2075%2C%2050%5D%20%0A%23%20Create%20a%20pie%20chart%20%0Aplt.figure(figsize%3D%5B5%2C5%5D)%20%0Aplt.pie(votes%2C%20labels%3Dlanguages%2C%20autopct%3D'%251.1f%25%25')%20%0Aplt.title('Favorite%20Programming%20Languages')%20%0Aplt.show()%0A&execute=1" width="100%" height="100%"></iframe>
:::

## Program 10: Create array using Numpy and Perform Operations on Array
```python
import numpy as np 
#Create two arrays 
a = np.array([1, 2, 3]) 
b = np.array([4, 5, 6]) 
#Perform arithmetic operations 
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b) 
#Perform relational operations 
print("a Greater than b", a > b) 
print("a Less than b", a < b) 
print("a Equal to b:", a == b) 
print("a Not Equal to b:", a != b) 
#Perform logical operations 
print("Logical OR:", np.logical_or(a, b))
print("Logical AND:", np.logical_and(a, b))
print("Logical NOT:", np.logical_not(a)) 
#Perform aggregation functions 
print("Sum of a:", np.sum(a))
print("Max of b:", np.max(b))
print("Min of a:", np.min(a))
print("Average of b:", np.average(b))
# Perform matrix operations 
print("Matrix Addition:\n", a + b) 
print("Matrix Subtraction:\n", a - b) 
print("Matrix Multiplication (element-wise):\n", a* b) 
print("Matrix Multiplication:\n", np.matmul(a, b)) 
print("Transpose of a:\n", np.transpose(a)) 
#Perform statistical functions 
print("Standard Deviation:", np.std(a)) 
print("Variance:", np.var(a)) 
print("Median:", np.median(a))
#Reshape array 
c = a.reshape((3, 1)) 
print("Reshaped a:", c) 
#Stack arrays 
print("Horizontal Stack:\n", np.hstack((a, b))) 
print("Vertical Stack:\n", np.vstack((a, b))) 
#Split array 
d= np.array([[1, 2, 3, 4], [5, 6, 7, 8]]) 
print("Horizontal Split:\n", np.hsplit(d, 2)) 
print("Vertical Split:\n", np.vsplit(d, 2)) 
#Broadcasting 
print("Broadcasting addition:\n", a + 5)
```

::: details Try it out
<a href="https://examdawn.pages.dev/jupyterlite/dist/repl/index.html?kernel=python&code=import%20numpy%20as%20np%20%0A%23Create%20two%20arrays%20%0Aa%20%3D%20np.array(%5B1%2C%202%2C%203%5D)%20%0Ab%20%3D%20np.array(%5B4%2C%205%2C%206%5D)%20%0A%23Perform%20arithmetic%20operations%20%0Aprint(%22Addition%3A%22%2C%20a%20%2B%20b)%0Aprint(%22Subtraction%3A%22%2C%20a%20-%20b)%0Aprint(%22Multiplication%3A%22%2C%20a%20*%20b)%0Aprint(%22Division%3A%22%2C%20a%20%2F%20b)%20%0A%23Perform%20relational%20operations%20%0Aprint(%22a%20Greater%20than%20b%22%2C%20a%20%3E%20b)%20%0Aprint(%22a%20Less%20than%20b%22%2C%20a%20%3C%20b)%20%0Aprint(%22a%20Equal%20to%20b%3A%22%2C%20a%20%3D%3D%20b)%20%0Aprint(%22a%20Not%20Equal%20to%20b%3A%22%2C%20a%20!%3D%20b)%20%0A%23Perform%20logical%20operations%20%0Aprint(%22Logical%20OR%3A%22%2C%20np.logical_or(a%2C%20b))%0Aprint(%22Logical%20AND%3A%22%2C%20np.logical_and(a%2C%20b))%0Aprint(%22Logical%20NOT%3A%22%2C%20np.logical_not(a))%20%0A%23Perform%20aggregation%20functions%20%0Aprint(%22Sum%20of%20a%3A%22%2C%20np.sum(a))%0Aprint(%22Max%20of%20b%3A%22%2C%20np.max(b))%0Aprint(%22Min%20of%20a%3A%22%2C%20np.min(a))%0Aprint(%22Average%20of%20b%3A%22%2C%20np.average(b))%0A%23%20Perform%20matrix%20operations%20%0Aprint(%22Matrix%20Addition%3A%5Cn%22%2C%20a%20%2B%20b)%20%0Aprint(%22Matrix%20Subtraction%3A%5Cn%22%2C%20a%20-%20b)%20%0Aprint(%22Matrix%20Multiplication%20(element-wise)%3A%5Cn%22%2C%20a*%20b)%20%0Aprint(%22Matrix%20Multiplication%3A%5Cn%22%2C%20np.matmul(a%2C%20b))%20%0Aprint(%22Transpose%20of%20a%3A%5Cn%22%2C%20np.transpose(a))%20%0A%23Perform%20statistical%20functions%20%0Aprint(%22Standard%20Deviation%3A%22%2C%20np.std(a))%20%0Aprint(%22Variance%3A%22%2C%20np.var(a))%20%0Aprint(%22Median%3A%22%2C%20np.median(a))%0A%23Reshape%20array%20%0Ac%20%3D%20a.reshape((3%2C%201))%20%0Aprint(%22Reshaped%20a%3A%22%2C%20c)%20%0A%23Stack%20arrays%20%0Aprint(%22Horizontal%20Stack%3A%5Cn%22%2C%20np.hstack((a%2C%20b)))%20%0Aprint(%22Vertical%20Stack%3A%5Cn%22%2C%20np.vstack((a%2C%20b)))%20%0A%23Split%20array%20%0Ad%3D%20np.array(%5B%5B1%2C%202%2C%203%2C%204%5D%2C%20%5B5%2C%206%2C%207%2C%208%5D%5D)%20%0Aprint(%22Horizontal%20Split%3A%5Cn%22%2C%20np.hsplit(d%2C%202))%20%0Aprint(%22Vertical%20Split%3A%5Cn%22%2C%20np.vsplit(d%2C%202))%20%0A%23Broadcasting%20%0Aprint(%22Broadcasting%20addition%3A%5Cn%22%2C%20a%20%2B%205)%0A&execute=1" target="_blank">Open in New Tab</a>
<iframe src="https://examdawn.pages.dev/jupyterlite/dist/repl/index.html?kernel=python&code=import%20numpy%20as%20np%20%0A%23Create%20two%20arrays%20%0Aa%20%3D%20np.array(%5B1%2C%202%2C%203%5D)%20%0Ab%20%3D%20np.array(%5B4%2C%205%2C%206%5D)%20%0A%23Perform%20arithmetic%20operations%20%0Aprint(%22Addition%3A%22%2C%20a%20%2B%20b)%0Aprint(%22Subtraction%3A%22%2C%20a%20-%20b)%0Aprint(%22Multiplication%3A%22%2C%20a%20*%20b)%0Aprint(%22Division%3A%22%2C%20a%20%2F%20b)%20%0A%23Perform%20relational%20operations%20%0Aprint(%22a%20Greater%20than%20b%22%2C%20a%20%3E%20b)%20%0Aprint(%22a%20Less%20than%20b%22%2C%20a%20%3C%20b)%20%0Aprint(%22a%20Equal%20to%20b%3A%22%2C%20a%20%3D%3D%20b)%20%0Aprint(%22a%20Not%20Equal%20to%20b%3A%22%2C%20a%20!%3D%20b)%20%0A%23Perform%20logical%20operations%20%0Aprint(%22Logical%20OR%3A%22%2C%20np.logical_or(a%2C%20b))%0Aprint(%22Logical%20AND%3A%22%2C%20np.logical_and(a%2C%20b))%0Aprint(%22Logical%20NOT%3A%22%2C%20np.logical_not(a))%20%0A%23Perform%20aggregation%20functions%20%0Aprint(%22Sum%20of%20a%3A%22%2C%20np.sum(a))%0Aprint(%22Max%20of%20b%3A%22%2C%20np.max(b))%0Aprint(%22Min%20of%20a%3A%22%2C%20np.min(a))%0Aprint(%22Average%20of%20b%3A%22%2C%20np.average(b))%0A%23%20Perform%20matrix%20operations%20%0Aprint(%22Matrix%20Addition%3A%5Cn%22%2C%20a%20%2B%20b)%20%0Aprint(%22Matrix%20Subtraction%3A%5Cn%22%2C%20a%20-%20b)%20%0Aprint(%22Matrix%20Multiplication%20(element-wise)%3A%5Cn%22%2C%20a*%20b)%20%0Aprint(%22Matrix%20Multiplication%3A%5Cn%22%2C%20np.matmul(a%2C%20b))%20%0Aprint(%22Transpose%20of%20a%3A%5Cn%22%2C%20np.transpose(a))%20%0A%23Perform%20statistical%20functions%20%0Aprint(%22Standard%20Deviation%3A%22%2C%20np.std(a))%20%0Aprint(%22Variance%3A%22%2C%20np.var(a))%20%0Aprint(%22Median%3A%22%2C%20np.median(a))%0A%23Reshape%20array%20%0Ac%20%3D%20a.reshape((3%2C%201))%20%0Aprint(%22Reshaped%20a%3A%22%2C%20c)%20%0A%23Stack%20arrays%20%0Aprint(%22Horizontal%20Stack%3A%5Cn%22%2C%20np.hstack((a%2C%20b)))%20%0Aprint(%22Vertical%20Stack%3A%5Cn%22%2C%20np.vstack((a%2C%20b)))%20%0A%23Split%20array%20%0Ad%3D%20np.array(%5B%5B1%2C%202%2C%203%2C%204%5D%2C%20%5B5%2C%206%2C%207%2C%208%5D%5D)%20%0Aprint(%22Horizontal%20Split%3A%5Cn%22%2C%20np.hsplit(d%2C%202))%20%0Aprint(%22Vertical%20Split%3A%5Cn%22%2C%20np.vsplit(d%2C%202))%20%0A%23Broadcasting%20%0Aprint(%22Broadcasting%20addition%3A%5Cn%22%2C%20a%20%2B%205)%0A&execute=1" width="100%" height="100%"></iframe>
:::

## Program 11: Create Data Frame from Excel Sheets using Pandas and Perform Operations on Data Frames
```python
import pandas as pd 
#Read DataFrame from excel file 
df = pd.read_excel("emp.xlsx") 
#Data selection of single column print("Single column: \n", df[ 'Name']) 
#Data selection of double columns 
print("\nDouble columns: \n", df[['Name', 'Gender']]) 
# Select first row by index label using .loc[] 
print("\nFirst row using loc[]:\n", df.loc[0]) 
# Select first row by position using iloc[] print("\nFirst row using .iloc[]: \n", df.iloc[0]) 
#Slice the first two rows and select 'Student Name' and 'Age' columns print("The first two rows of Name and Age Columns: ") 
print(df[:2][['Name', 'Age']]) 
#Filtering based on age>30 
print("\nFiltered DataFrame (Age > 30):\n", df [df['Age'] > 30]) 
# Grouping based on Course and Age 
grouped_df = df.groupby('Gender') ['Age'].mean() 
print("\nGrouped DataFrame (based on 'Gender' and 'Age'):\n", grouped_df) 
# Sorting by index 
df_by_index= df.sort_index(ascending=False) 
print("\nDataFrame sorted by index: \n", df_by_index) 
# Sorting by values 
df_by_value = df.sort_values (by='Age') 
print("\nDataFrame sorted by 'Age' column: \n", df_by_value)
```

TODO: Add Sample data and output 

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
