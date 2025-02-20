---
order: 1
title: Python Lab - Part A
---
# Python Programming - Lab Part A
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
    print(f"The roots of the equation {a} x^2 * {b} x + {c} = 0 are {roots[0]:.2f} and {roots[1]:.2f}")
else:
    print("The given equation has no real roots")
```

::: details Try it out
```python:line-number
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
    print(f"The roots of the equation {a} x^2 * {b} x + {c} = 0 are {roots[0]:.2f} and {roots[1]:.2f}")
else:
    print("The given equation has no real roots")

```
<Editor id="quad-prg2" />
:::