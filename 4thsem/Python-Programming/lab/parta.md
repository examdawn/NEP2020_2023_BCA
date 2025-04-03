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

## Program 3: Program to find the Sum of n Natural number.

```python
n = int(input("Enter a Natural Number: "))
sum_of_n_number = n*(n+1)//2
print(f"The sum of the digits of the first {n} natural number: {sum_of_n_number}")
```

::: details Try it out
```python:line-numbers
n = int(input("Enter a Natural Number: "))
sum_of_n_number = n*(n+1)//2
print(f"The sum of the digits of the first {n} natural number: {sum_of_n_number}")
```
<Editor id="sonn-prg3" />
:::

## Program 4: Program to Display Multiple Tables.

```python
num = int(input("Enter a Number: "))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")
```

::: details Try it out
```python:line-numbers
num = int(input("Enter a Number: "))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")
```
<Editor id="table-prg4" />
:::

## Program 5: Program to check if the given number is Prime or not.

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

## Program 6: Program to implement a Sequential Search.

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

## Program 7: Program to create a Calculator

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

## Program 8: Program to implement Selection Sort.

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
<Editor id="Seque-prg8" />
:::
