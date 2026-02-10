---
order: 2
title: RStats Lab - Part B
---
# R Programming - Lab Part B

## * **Program 1: Calculate Factorial of a Number**

Problem Statement: Write a Program to calculate the factorial of a number.

::: details View Code

<JupyterLite kernel="xr">

```r
# Function to calculate the factorial of a number
factorial <- function(n) {
  if (n == 0) {
    return(1) # The factorial of 0 is defined as 1
  } else {
    return(n * factorial(n - 1))
  }
}

# Test the factorial function
result <- factorial(5) # Calculate 5!
cat("Factorial of 5 is:", result, "\n")
```

</JupyterLite>
:::

## * **Program 2: Sum of Two Numbers Using Function**

Problem Statement: Program to find the sum of 2 numbers using a function.

::: details View Code

<JupyterLite kernel="xr">

```r
# Defining a simple function in R
sum_function <- function(a, b) {
  result <- a + b # Compute the sum of the two arguments
  return(result)  # Return the result
}

# Using the function with sample arguments
x <- 3
y <- 4
z <- sum_function(x, y)
print(z)
```

</JupyterLite>
:::

## **Program 3: List Operations**

Problem Statement: Write a program that demonstrates the use of lists.

::: details View Code

<JupyterLite kernel="xr">

```r
# Creating a list
my_list <- list(
  name = "John Doe",
  age = 30,
  is_student = TRUE,
  grades = c(85, 90, 95, 87, 92)
)

# Printing the list
print(my_list)

# Accessing elements in the list
print(paste("Name:", my_list$name))
print(paste("Age:", my_list$age))
print(paste("Is Student:", my_list$is_student))
print(paste("Grades:", my_list$grades))

# Modifying elements in the list
my_list$name <- "Jane Doe"
my_list$age <- 25
my_list$is_student <- FALSE
my_list$grades <- c(75, 80, 85, 77, 82)

# Printing the modified list
print(my_list)
```

</JupyterLite>
:::

## * **Program 4: Area of a Triangle**

Problem Statement: Program to calculate the area of a triangle.

::: details View Code

<JupyterLite kernel="xr">

```r
triangle_area <- function(base, height) {
  area <- 0.5 * base * height
  return(area)
}

# Example usage of the function
base_length <- 6
height_length <- 8
area <- triangle_area(base_length, height_length)
cat("The area of the triangle is:", area, "\n")
```

</JupyterLite>
:::

## * **Program 5: Swap Variable Values**

Problem Statement: Program to swap the values of two variables.

::: details View Code

<JupyterLite kernel="xr">

```r
# Function to swap two numbers
swap_numbers <- function(a, b) {
  temp <- a
  a <- b
  b <- temp
  return(list(a = a, b = b))
}

# Example usage of the function
num1 <- 5
num2 <- 10
cat("Before swapping: num1 =", num1, "and num2 =", num2, "\n")

# Call the function to swap the numbers
result <- swap_numbers(num1, num2)
cat("After swapping: num1 =", result$a, "and num2 =", result$b, "\n")
```

</JupyterLite>
:::

## **Program 6: Basic Matrix Operations**

Problem Statement: Write a Program to perform basic matrix operations such as addition, subtraction, multiplication, and transpose.

::: details View Code

<JupyterLite kernel="xr">

```r
# Create matrices
matrix1 <- matrix(c(1, 2, 3, 4), nrow = 2, ncol = 2, byrow = TRUE)
matrix2 <- matrix(c(5, 6, 7, 8), nrow = 2, ncol = 2, byrow = TRUE)

# Print the matrices
cat("Matrix 1:\n")
print(matrix1)
cat("\nMatrix 2:\n")
print(matrix2)

# Addition of matrices
addition_result <- matrix1 + matrix2
cat("\nAddition Result:\n")
print(addition_result)

# Subtraction of matrices
subtraction_result <- matrix1 - matrix2
cat("\nSubtraction Result:\n")
print(subtraction_result)

# Multiplication of matrices
multiplication_result <- matrix1 %*% matrix2
cat("\nMultiplication Result:\n")
print(multiplication_result)

# Transpose of matrices
transpose_matrix1 <- t(matrix1)
transpose_matrix2 <- t(matrix2)

cat("\nTranspose of Matrix 1:\n")
print(transpose_matrix1)
cat("\nTranspose of Matrix 2:\n")
print(transpose_matrix2)
```

</JupyterLite>
:::

## * **Program 7: Data Frame Operations**

Problem Statement: Program to demonstrate creating, modifying, and accessing data in data frames.

::: details View Code

<JupyterLite kernel="xr">

```r
# Creating a dataframe
data <- data.frame(
  Name = c("John", "Doe", "Jane", "Smith"),
  Age = c(25, 30, 28, 35),
  Salary = c(50000, 60000, 55000, 70000)
)

# Printing the dataframe
cat("Initial Dataframe:\n")
print(data)

# Adding a new column
data$Department <- c("HR", "Finance", "IT", "Marketing")

# Printing the updated dataframe
cat("\nDataframe with New Column:\n")
print(data)

# Modifying a value in the dataframe
data[3, "Salary"] <- 60000

# Printing the dataframe after modification
cat("\nDataframe after Modification:\n")
print(data)

# Accessing specific elements
cat("\nAccessing Specific Elements:\n")
cat("Second row, second column:", data[2, 2], "\n")
cat("Name column:", data$Name, "\n")

# Filtering data
cat("\nFiltered Dataframe (Age > 25):\n")
filtered_data <- data[data$Age > 25, ]
print(filtered_data)
```

</JupyterLite>
:::

## * **Program 8: Basic Plot Generation**

Problem Statement: Program to generate a basic plot in R.

::: details View Code

<JupyterLite kernel="xr">

```r
# Creating data for the plot
x <- c(1, 2, 3, 4, 5)
y <- c(2, 4, 6, 8, 10)

# Plotting the data
plot(x, y, type = "o", col = "blue", xlab = "X-axis", ylab = "Y-axis", main = "Simple Plot")

# Adding points to the plot
points(x, y, col = "red")

# Adding a line to the plot
# Using lm() for linear model (regression line)
abline(lm(y ~ x), col = "green")
```

</JupyterLite>
:::

## * **Program 9: Loop and Summation**

Problem Statement: Program to calculate the sum of the first 10 natural numbers.

::: details View Code

<JupyterLite kernel="xr">

```r
# Initializing sum variable
sum_result <- 0

# Using a for loop to calculate the sum of the first 10 natural numbers
for (i in 1:10) {
  sum_result <- sum_result + i
}

# Printing the result
cat("Sum of the first 10 natural numbers is:", sum_result)
```

</JupyterLite>
:::

## **Program 10: Mean, Variance, and Bar Chart**

Problem Statement: Program to find the mean, variance, and plot bar chart.

::: details View Code

<JupyterLite kernel="xr">

```r
# Define the probabilities for each value
pmf <- c(0.1, 0.2, 0.15, 0.3, 0.1, 0.15) # Example probabilities for values 1 to 6

# Set the corresponding values
values <- 1:6

# Print the PMF
print(pmf)

# Print the values
print(values)

# Calculate the mean
mean_value <- sum(pmf * values)
print(paste("Mean:", mean_value))

# Calculate the variance
var_value <- sum(pmf * (values - mean_value)^2)
print(paste("Variance:", var_value))

# Plot the PMF
barplot(pmf, names.arg = values, xlab = "Values", ylab = "Probabilities", 
        main = "Probability Mass Function (PMF)")
```

</JupyterLite>
:::