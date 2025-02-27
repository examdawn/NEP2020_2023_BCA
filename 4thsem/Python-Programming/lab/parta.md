---
order: 1
title: Python Lab - Part A
---
# Python Programming - Lab Part A

Info on built-in python web editor:
> [!WARNING]
> This will not work if your browser is too old or does not support Web Assembly/Web Workers. If you're using a privacy focused browser like cromite, please enable JavaScript JIT and WebAssembly from the permissions menu.

If the Run Button doesn't load, try reloading your browser!

## Program 1: Program to check if a given number belongs to the Fibonacci sequence

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
<Editor id="fibo-prg1" />
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
<Editor id="table-prg3" />
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
<Editor id="prime-prg3" />
:::
