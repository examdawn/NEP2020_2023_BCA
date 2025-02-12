# Lab Practicals
## Part A
Program 8 is skipped(pascal triangle)
### Program 1 - Fibonacci Series

```C#
using System;
public class fibo
{
    public static void Main(string[] args)
    {
        int n = 10;
        int a = 0;
        int b = 1;
        int c = 0;

        Console.WriteLine("Printing Fibonacci Sequence");
        for (int i = 0; i < n; i++)
        {
            Console.Write(a+" ");
            c = a + b;
            a = b;
            b = c;
        }
    }
}
```

Output:
```
Printing Fibonacci Sequence
0 1 1 2 3 5 8 13 21 34
```

[Source](https://github.com/sounddrill31/csharp-lab-parta/blob/main/fibo/Program.cs)

### Program 2 - Prime Number Checker
```C#
using System;
public class primeno
{
    public static void Main(string[] args)
    {
        int n, i, m = 0, flag = 0;
        Console.Write("Enter the Number to check Prime: ");
        n = int.Parse(Console.ReadLine());
        m = n / 2;
        
        for (i = 2; i <= m; i++)
        {
            if (n % i == 0)
            {
                Console.Write("Number is not Prime.");
                flag = 1;
                break;
            }
        }

        if (flag == 0)
        {
            Console.Write("Number is Prime.");
        }
    }
}
```

Output:
```
Enter the Number to check Prime: 23
Number is Prime.
```

```
Enter the Number to check Prime: 17
Number is Prime.
```

[Source](https://github.com/sounddrill31/csharp-lab-parta/blob/main/primeno/Program.cs)

### Program 3 - Palindrome checker
```C#
using System;
public class palindrome
{
    public static void Main(string[] args)
    {
        int n, r, sum = 0, temp;
        Console.Write("Enter the Number: ");
        n = int.Parse(Console.ReadLine());
        temp = n;
        while (n > 0)
        {
            r = n % 10;
            sum = (sum * 10) + r;
            n = n / 10;
        }
        if (temp == sum)
        {
            Console.Write("Number is Palindrome.");
        }
        else
        {
            Console.Write("Number is not Palindrome.");
        }
    }
}
```

Output:
```
Enter the Number: 121
Number is Palindrome.
```

```
Enter the Number: 156
Number is not Palindrome.
```

[Source](https://github.com/sounddrill31/csharp-lab-parta/blob/main/palindrome/Program.cs)

### Program 4 - Factorial Finder
```C#
using System;
public class fact
{
    public static void Main(string[] args)
    {
        int i, fact = 1, number;
        Console.Write("Enter the Number: ");
        number = int.Parse(Console.ReadLine());
        for (i = 1; i <= number; i++)
        {
            fact = fact * i;
        }
        Console.Write("Factorial of " + number + " is: " + fact);
    }
}
```

Output:
```
Enter the Number: 6
Factorial of 6 is: 720
```

[Source](https://github.com/sounddrill31/csharp-lab-parta/blob/main/fact/Program.cs)

### Program 5 - Sum Of Digits
```C#
using System;
public class sumdigits
{
    public static void Main(string[] args)
    {
        int n, sum = 0, r;
        Console.Write("Enter the Number: ");
        n = int.Parse(Console.ReadLine());
        while (n > 0)
        {
            r = n % 10;
            sum = sum + r;
            n = n / 10;
        }
        Console.Write("Sum of Digits is: " + sum);
    }
}
```

Output:
```
Enter the Number: 23
Sum of Digits is: 5
```

[Source](https://github.com/sounddrill31/csharp-lab-parta/blob/main/sumdigits/Program.cs)

### Program 6 - Reverse of a Number
```C#
using System;
public class revnum
{
    public static void Main(string[] args)
    {
        int num, reverse = 0;
        Console.WriteLine("Enter a number: ");
        num = int.Parse(Console.ReadLine());
        while (num != 0)
        {
            reverse = reverse * 10;
            reverse = reverse + num % 10;
            num = num / 10;
        }
        Console.WriteLine("Reverse of the number is "+reverse);
    }
}
```

Output:
```
Enter a number: 
53432
Reverse of the number is 23435
```

[Source](https://github.com/sounddrill31/csharp-lab-parta/blob/main/revnum/Program.cs)

### Program 7 - Swap Two Numbers without 3rd Variable
```C#
using System;
public class swap
{
    public static void Main(string[] args)
    {
        int num1, num2, temp;
        Console.WriteLine("Enter the first number: ");
        num1 = int.Parse(Console.ReadLine());
        Console.WriteLine("Enter the second number: ");
        num2 = int.Parse(Console.ReadLine());
        Console.WriteLine("Before swapping: num1 = "+num1+" num2 = "+num2);
        num1 = num1 + num2;
        num2 = num1 - num2;
        num1 = num1 - num2;
        Console.WriteLine("After swapping: num1 = "+num1+" num2 = "+num2);
    }
}
```

Output:
```
Enter the first number: 
45
Enter the second number: 
2
Before swapping: num1 = 45 num2 = 2
After swapping: num1 = 2 num2 = 45
```

[Source](https://github.com/sounddrill31/csharp-lab-parta/blob/main/swap/Program.cs)

### Program 8 - Print a Pascal Triangle(Skip)
```C#
using System;
public class pascaltriangle
{
    public static void Main(string[] args)
    {
        int i, j, k, n;
        Console.WriteLine("Enter the number of rows: ");
        n = int.Parse(Console.ReadLine());
        for (i = 0; i < n; i++)
        {
            for (j = 0; j < n - i - 1; j++)
            {
                Console.Write(" ");
            }
            int number = 1;
            for (k = 0; k <= i; k++)
            {
                Console.Write(number + " ");
                number = number * (i - k) / (k + 1);
            }
            Console.WriteLine();
        }
    }
}
```

Output:
```
Enter the number of rows: 
5
    1 
   1 1 
  1 2 1 
 1 3 3 1 
1 4 6 4 1 
```

[Source](https://github.com/sounddrill31/csharp-lab-parta/blob/main/pascaltriangle/Program.cs

### Program 9 - Demonstrate Multithreaded Programming
```C#
using System;
using System.Threading;
public class multithread
{
    public static void Main(string[] args)
    {
        Thread t = Thread.CurrentThread;
        t.Name = "Main Thread";
        Console.Write("Current Executing Thread Name: " + t.Name);
        Console.Write("Current Executing Thread Name: " + Thread.CurrentThread.Name);
        Console.Read();
    }
}
```

Output:
```
Thread Name: Main Thread
Currently Executing Thread: Main Thread
```

[Source](https://github.com/sounddrill31/csharp-lab-parta/blob/main/ThreadProg/Program.cs)

### Program 10 - Find Square using Subroutines and Functions
```C#
using System;
class SubSquare
{
    public static int Square(int num)
    {
        return num * num;
    }
    public static void Main(string[] args)
    {
        int number, result;
        Console.WriteLine("Enter a number: ");
        number = int.Parse(Console.ReadLine());
        result = Square(number);
        Console.WriteLine("Square of the number is "+result);
    }
}
```

Output:
```
Enter a number: 
5
Square of the number is 25
```

[Source](https://github.com/sounddrill31/csharp-lab-parta/blob/main/SubSquare/Program.cs)

## Source:
- General Questions were found in Syllabus