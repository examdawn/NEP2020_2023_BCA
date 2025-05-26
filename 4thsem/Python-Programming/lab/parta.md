---
order: 1
title: Python Lab - Part A
---
# Python Programming - Lab Part A

> [!TIP]
> This Page supports running Python directly from your browser!

::: details  Click for more details. If this feature is not working as expected, [please report it to us on Github!](https://github.com/examdawn/NEP2020_2023_BCA/issues/new)

> [!WARNING]
> This will not work if your browser is too old or does not support Web Assembly/Web Workers. If you're using a privacy focused browser like cromite, please enable JavaScript JIT and WebAssembly from the permissions menu.

If the Run Button doesn't show the run or loading button, try reloading your browser!

It will take some time to load, especially if your internet is slow.
:::

<!--

Usage Example for code:

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
## Program 1: Program to check if a given number belongs to the Fibonacci sequence

```python
def fabo(n):
    a = 0
    b = 1
    while (b<n):
        temp = b
        b += a
        a = temp
    return b==n or n==0

n = int(input("Enter a number: "))
if fabo(n):
    print(f"{n} belongs to Fibonacci Sequence.")
else:
    print(f"{n} does not belongs to Fibonacci Sequence.")
```

::: details Try it out
```python:line-numbers
def fabo(n):
    a = 0
    b = 1
    while (b<n):
        temp = b
        b += a
        a = temp
    return b==n or n==0

n = int(input("Enter a number: "))
if fabo(n):
    print(f"{n} belongs to Fibonacci Sequence.")
else:
    print(f"{n} does not belongs to Fibonacci Sequence.")
```
<Editor id="fibo1-prg1" />
:::

::: details Show Output
```
Enter a number: 15
15 does not belongs to Fibonacci Sequence.
```
:::

::: details Alternative Code
```python
import math as m  
   
def isPerfectSquare(n):  
    val = int(m.sqrt(n))
    return val * val == n
   
def isFibo(x): 
    return isPerfectSquare(5 * x * x + 4) or isPerfectSquare(5 * x * x - 4)

num = int(input("Enter your Number:"))
if(isFibo(num)):
    print("Yes, given number", num, "occurs in the Fibonacci series")
else:
    print("No, given number", num, "is not a Fibonacci number")
```

::: details Try it out
```python:line-numbers
import math as m  
   
def isPerfectSquare(n):  
    val = int(m.sqrt(n))
    return val * val == n
   
def isFibo(x): 
    return isPerfectSquare(5 * x * x + 4) or isPerfectSquare(5 * x * x - 4)

num = int(input("Enter your Number:"))
if(isFibo(num)):
    print("Yes, given number", num, "occurs in the Fibonacci series")
else:
    print("No, given number", num, "is not a Fibonacci number")
```
<Editor id="fibo2-prg1" />
:::

## Program 2: Program to solve Quadratic equation.

```python
import math as m

def quad(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant >= 0:
        root1 = (-b + m.sqrt(discriminant)) / (2*a)
        root2 = (-b - m.sqrt(discriminant)) / (2*a)
        return (root1, root2)
    else:
        return None

a = float(input("Enter Coefficient for x^2[a]: "))
b = float(input("Enter Coefficient for x[b]  : "))
c = float(input("Enter Constant Term[c]      : "))

roots = quad(a, b, c)

if roots is not None:
    print(f"The roots of the equation {a} x^2 + {b} x + {c} = 0 are {roots[0]:.2f} and {roots[1]:.2f}")
else:
    print("The given equation has no real roots")
```

::: details Show output

Enter Coefficient for x^2[a]: 1
Enter Coefficient for x[b]  : 6
Enter Constant Term[c]      : 9
The roots of the equation 1.0 x^2 + 6.0 x + 9.0 = 0 are -3.00 and -3.00

:::


::: details Try it out
```python:line-numbers
import math as m

def quad(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant >= 0:
        root1 = (-b + m.sqrt(discriminant)) / (2*a)
        root2 = (-b - m.sqrt(discriminant)) / (2*a)
        return (root1, root2)
    else:
        return None

a = float(input("Enter Coefficient for x^2[a]: "))
b = float(input("Enter Coefficient for x[b]  : "))
c = float(input("Enter Constant Term[c]      : "))

roots = quad(a, b, c)

if roots is not None:
    print(f"The roots of the equation {a} x^2 + {b} x + {c} = 0 are {roots[0]:.2f} and {roots[1]:.2f}")
else:
    print("The given equation has no real roots")
```
<Editor id="quad-prg2" />
:::

## Program 3: Program to find the Sum of n Natural number. *

```python
n = int(input("Enter a Natural Number: "))
sum_of_n_number = n*(n+1)//2
print(f"The sum of the first {n} natural number: {sum_of_n_number}")
```

::: details Show Output
```
Enter a Natural Number: 5
The sum of the first 5 natural number: 15
```
:::

::: details Try it out
```python:line-numbers
n = int(input("Enter a Natural Number: "))
sum_of_n_number = n*(n+1)//2
print(f"The sum of the first {n} natural number: {sum_of_n_number}")
```
<Editor id="sonn-prg3" />
:::

## Program 4: Program to Display Multiple Tables. *

```python
num = int(input("Enter a Number: "))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")
```

::: details Show Output
```
Enter a Number: 5
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

::: details Try it out
```python:line-numbers
num = int(input("Enter a Number: "))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")
```
<Editor id="table-prg4" />
:::

## Program 5: Program to check if the given number is Prime or not. *

```python
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

n = int(input("Enter a Number: "))

if is_prime(n):
    print(f"{n} is a Prime number.")
else:
    print(f"{n} is not a Prime number.")
```

::: details Show Output
```
Enter a Number: 15
15 is not a Prime number.
```
:::

::: details Try it out
```python:line-numbers
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

n = int(input("Enter a Number: "))

if is_prime(n):
    print(f"{n} is a Prime number.")
else:
    print(f"{n} is not a Prime number.")
```
<Editor id="prime-prg5" />
:::

## Program 6: Program to implement a Sequential Search. *

```python
def search(lst, key):
    for i in range(len(lst)):
        if lst[i] == key:
            return i
    return -1

num = list(map(int, input("Enter number separated with a Space: ").split()))    
key = int(input("Enter a number to be Searched: "))

result = search(num, key)

if result != -1:
    print(f"Elements found at Position   : {result + 1}")
else:
    print("Element not found in the list")
```

::: details Show Output
```
Enter number separated with a Space: 1 2 5 3 0
Enter a number to be Searched: 3
Elements found at Position   : 4
```
:::

::: details Try it out
```python:line-numbers
def search(lst, key):
    for i in range(len(lst)):
        if lst[i] == key:
            return i
    return -1

num = list(map(int, input("Enter number separated with a Space: ").split()))    
key = int(input("Enter a number to be Searched: "))

result = search(num, key)

if result != -1:
    print(f"Elements found at Position   : {result + 1}")
else:
    print("Element not found in the list")
```
<Editor id="Seque-prg6" />
:::

::: details Alternative Code
```python
list = list(map(str, input("Enter multiple items seperated by space: ").split()))

target = input("Search for: ")
for i in list:
    if i == target:
        print(f"Found at index {list.index(i)}")
        break
else:
    print(f"{target} not found.")
```

::: details Try it out
```python:line-numbers
list = list(map(str, input("Enter multiple items seperated by space: ").split()))

target = input("Search for: ")
for i in list:
    if i == target:
        print(f"Found at index {list.index(i)}")
        break
else:
    print(f"{target} not found.")
```
<Editor id="alt-sq-prg6" />
:::


## Program 7: Program to create a Calculator *

```python
def add(x, y):
    return x + y

def sub(x, y):
    return x - y
    
def mul(x, y):
    return x * y
    
def div(x, y):
    if y != 0:
        return x / y
    else: 
        return "Undefined! Can't divide by Zero"
        
while True:
    print("\n-----------------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. QUIT")
    print("-----------------")
    
    choice = input("\nEnter Choice: ")
    
    if choice == '5':
        print("\nExiting The Program!")
        break
    
    num1 = float(input("Enter First  Number: "))
    num2 = float(input("Enter Second Number: "))
    
    if choice == '1':
        print("\nThe Result: ", add(num1, num2))
        
    elif choice == '2':
        print("\nThe Result: ", sub(num1, num2))
            
    elif choice == '3':
        print("\nThe Result: ", mul(num1, num2))
            
    elif choice == '4':
        print("\nThe Result: ", div(num1, num2))
        
    else:
        print("\nINVALID INPUT!")
```

::: details Show Output
```

-----------------
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. QUIT
-----------------

Enter Choice: 1
Enter First  Number: 5
Enter Second Number: 10

The Result:  15.0

-----------------
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. QUIT
-----------------

Enter Choice: 3
Enter First  Number: 10
Enter Second Number: 15

The Result:  150.0

-----------------
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. QUIT
-----------------

Enter Choice: 5

Exiting The Program!
```
:::

::: details Try it out
```python:line-numbers
def add(x, y):
    return x + y

def sub(x, y):
    return x - y
    
def mul(x, y):
    return x * y
    
def div(x, y):
    if y != 0:
        return x / y
    else: 
        return "Undefined! Can't divide by Zero"
        
while True:
    print("\n-----------------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. QUIT")
    print("-----------------")
    
    choice = input("\nEnter Choice: ")
    
    if choice == '5':
        print("\nExiting The Program!")
        break
    
    num1 = float(input("Enter First  Number: "))
    num2 = float(input("Enter Second Number: "))
    
    if choice == '1':
        print("\nThe Result: ", add(num1, num2))
        
    elif choice == '2':
        print("\nThe Result: ", sub(num1, num2))
            
    elif choice == '3':
        print("\nThe Result: ", mul(num1, num2))
            
    elif choice == '4':
        print("\nThe Result: ", div(num1, num2))
        
    else:
        print("\nINVALID INPUT!")
```
<Editor id="calc-prg7" />
:::


::: details Alternative Code
```python
while True:
    print("Calculator")
    op = input("Enter Operation ('+', '-', '*', '/', 'quit'): ")
    if op == 'quit':
        break
    num1=float(input("Enter Operand 1: "))
    num2=float(input("Enter Operand 2: "))
    expr = f"{num1} {op} {num2}"
    print(expr, " = ", eval(expr))
```

::: details Try it out
```python:line-numbers
while True:
    print("Calculator")
    op = input("Enter Operation ('+', '-', '*', '/', 'quit'): ")
    if op == 'quit':
        break
    num1=float(input("Enter Operand 1: "))
    num2=float(input("Enter Operand 2: "))
    expr = f"{num1} {op} {num2}"
    print(expr, " = ", eval(expr))
```
<Editor id="alt-calc-prg7" />
:::


## Program 8: Program to explore String Functions *
```python
str = input("Enter a string: ")

print("Capital string: ", str.capitalize())
print("Upper string: ", str.upper())
print("Lower string: ", str.lower())
print("Is string AlphaNumeric? ", str.isalnum())
print("Is string Numeric? ", str.isnumeric())

substring = input("Enter substring to search: ")
print(f"Substring '{substring}' found at index: {str.find(substring)}")

old_sub = input("Enter old substring to replace: ")
new_sub = input("Enter new substring: ")
print("Replaced String: ", str.replace(old_sub, new_sub))

print("List of Words: ", str.split())
```

::: details Show Output
```
Enter a string: Hello
Capital string:  Hello
Upper string:  HELLO
Lower string:  hello
Is string AlphaNumeric?  True
Is string Numeric?  False
Enter substring to search: lo
Substring 'lo' found at index: 3
Enter old substring to replace: llo
Enter new substring: hi
Replaced String:  Hehi
List of Words:  ['Hello']
```
:::

::: details Try it out
```python:line-numbers
str = input("Enter a string: ")

print("Capital string: ", str.capitalize())
print("Upper string: ", str.upper())
print("Lower string: ", str.lower())
print("Is string AlphaNumeric? ", str.isalnum())
print("Is string Numeric? ", str.isnumeric())

substring = input("Enter substring to search: ")
print(f"Substring '{substring}' found at index: {str.find(substring)}")

old_sub = input("Enter old substring to replace: ")
new_sub = input("Enter new substring: ")
print("Replaced String: ", str.replace(old_sub, new_sub))

print("List of Words: ", str.split())
```
<Editor id="string-prg8" />
:::

## Program 9: Program to implement Selection Sort. *

```python
def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst

numbers = list(map(int, input("Enter numbers seperated by space: ").split()))

sorted_numbers = selection_sort(numbers)

print("Sorted List: ", sorted_numbers)

```

::: details Show Output
```
Enter numbers seperated by space: 10 200 30 45 1 2 4 7 3
Sorted List:  [1, 2, 3, 4, 7, 10, 30, 45, 200]
```
:::

::: details Try it out
```python:line-numbers
def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst

numbers = list(map(int, input("Enter numbers seperated by space: ").split()))

sorted_numbers = selection_sort(numbers)

print("Sorted List: ", sorted_numbers)
```
<Editor id="Seque-prg9" />
:::

## Program 10: Program to implement Stack. *
```python
# Empty stack
stack = []

while True:
    print("""
    1: Push
    2: Pop
    3: Peek
    4: Display Stack
    5: Exit
    """)
    ch = int(input("Enter choice: "))

    match ch:
        case 1:
            num = int(input("Enter number to push: "))
            stack.append(num)
        case 2:
            if len(stack) < 1:
                print("Stack is empty, nothing to pop")
            else:
                print("Popped Value: ", stack.pop())
        case 3:
            if len(stack) < 1:
                print("Stack is empty")
            else:
                print("Top Value: ", stack[-1])
        case 4:
            print("Stack: ", stack)
        case 5:
            break # Breaks the loop. Match case doesn't support break/continue
        case _: # Equivalent to else
            print("Invalid Choice. Please try again")

```

::: details Show Output
```
    1: Push
    2: Pop
    3: Peek
    4: Display Stack
    5: Exit
    
Enter choice: 1
Enter number to push: 500

    1: Push
    2: Pop
    3: Peek
    4: Display Stack
    5: Exit
    
Enter choice: 3
Top Value:  500

    1: Push
    2: Pop
    3: Peek
    4: Display Stack
    5: Exit
    
Enter choice: 1
Enter number to push: 232

    1: Push
    2: Pop
    3: Peek
    4: Display Stack
    5: Exit
    
Enter choice: 1
Enter number to push: 50

    1: Push
    2: Pop
    3: Peek
    4: Display Stack
    5: Exit
    
Enter choice: 4
Stack:  [500, 232, 50]

    1: Push
    2: Pop
    3: Peek
    4: Display Stack
    5: Exit
    
Enter choice: 2
Popped Value:  50

    1: Push
    2: Pop
    3: Peek
    4: Display Stack
    5: Exit
    
Enter choice: 5
```
:::

::: details Try it out
```python:line-numbers
# Empty stack
stack = []

while True:
    print("""
    1: Push
    2: Pop
    3: Peek
    4: Display Stack
    5: Exit
    """)
    ch = int(input("Enter choice: "))

    match ch:
        case 1:
            num = int(input("Enter number to push: "))
            stack.append(num)
        case 2:
            if len(stack) < 1:
                print("Stack is empty, nothing to pop")
            else:
                print("Popped Value: ", stack.pop())
        case 3:
            if len(stack) < 1:
                print("Stack is empty")
            else:
                print("Top Value: ", stack[-1])
        case 4:
            print("Stack: ", stack)
        case 5:
            break # Breaks the loop. Match case doesn't support break/continue
        case _: # Equivalent to else
            print("Invalid Choice. Please try again")
```
<Editor id="stack-prg10" />
:::

## Program 11: Read and Write into a File
```python
def accept_details():
    students = [] # List of dict values
    while True:
        student = {}
        student['name'] = input("Enter student name (q to exit): ")
        if student['name'].lower() == 'q':
            break
        student['roll_number'] = input("Enter Roll Number: ")
        student['marks'] = float(input("Enter marks: "))
        students.append(student)
    return students

def write_details(students):
    with open('student_details.txt', 'w') as file:
        for student in students:
            file.write(student['name'] + ',')
            file.write(student['roll_number'] + ',')
            file.write(str(student['marks']) + '\n')

def display_details():
    with open('student_details.txt', 'r') as file:
        print("Name\tRoll Number\tMarks")
        for line in file:
            name, roll_number,marks=line.strip().split(',')
            print(f"{name}\t{roll_number}\t{marks}")

students = accept_details()
write_details(students)
display_details()
```

::: details Show Output
```
Enter student name (q to exit): Souhrud
Enter Roll Number: 026
Enter marks: 80
Enter student name (q to exit): John
Enter Roll Number: 000
Enter marks: 50
Enter student name (q to exit): q
Name	Roll Number	Marks
Souhrud	026	80.0
John	000	50.0
```
:::

::: details Try it out
```python:line-numbers
def accept_details():
    students = [] # List of dict values
    while True:
        student = {}
        student['name'] = input("Enter student name (q to exit): ")
        if student['name'].lower() == 'q':
            break
        student['roll_number'] = input("Enter Roll Number: ")
        student['marks'] = float(input("Enter marks: "))
        students.append(student)
    return students

def write_details(students):
    with open('student_details.txt', 'w') as file:
        for student in students:
            file.write(student['name'] + ',')
            file.write(student['roll_number'] + ',')
            file.write(str(student['marks']) + '\n')

def display_details():
    with open('student_details.txt', 'r') as file:
        print("Name\tRoll Number\tMarks")
        for line in file:
            name, roll_number,marks=line.strip().split(',')
            print(f"{name}\t{roll_number}\t{marks}")

students = accept_details()
write_details(students)
display_details()
```
<Editor id="filehandle-prg11" />
:::
