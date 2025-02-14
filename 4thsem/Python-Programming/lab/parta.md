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
