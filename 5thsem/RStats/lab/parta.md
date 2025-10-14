---
order: 1
title: RStats Lab - Part A
---
# R Programming - Lab Part A

## **Program 1: Different Types of Data Structures in R**

Problem Statement: Write a program for different types of data structures in R​

::: details View Code

<JupyterLite kernel="xr">

```r
# Creating a Numeric Vector
n <- c(1, 2, 3, 4, 5)
print("Numeric Vector:")
print(n)
# Creating a Character Vector
cv <- c("apple", "banana", "cherry")
print("Character Vector:")
print(cv)

# Creating a List
lst <- list(1, "apple", TRUE)
print("List:")
print(lst)

# Creating a Matrix
m <- matrix(1:6, nrow = 2, ncol = 3)
print("Matrix:")
print(m)

# Creating a Data Frame
df <- data.frame(Name = c("Alice", "Bob", "Charlie"),
                Age = c(25, 30, 22))
print("Data Frame:")
print(df)
```

</JupyterLite>
:::  

## **Program 2: Variables, Constants, and Data Types**

Problem Statement: Write a program that include variables, constants, data types

::: details View Code

<JupyterLite kernel="xr">

```r
# Constants
PI <- 3.14159
GRAVITY <- 9.81

# Variables
name <- "John Doe"
age <- 30
is_student <- TRUE
grades <- c(85, 92, 78, 95, 89)

# Displaying information
cat("Name:", name, "\n")
cat("Age:", age, "\n")
cat("Is Student:", is_student, "\n")
cat("Grades:", grades, "\n")

# Data Types
ntype <- typeof(name)
atype <- typeof(age)
itype <- typeof(is_student)
gtype <- typeof(grades)

cat("Data Type of 'name':", ntype, "\n")
cat("Data Type of 'age':", atype, "\n")
cat("Data Type of 'is_student':", itype, "\n")
cat("Data Type of 'grades':", gtype, "\n")
```

</JupyterLite>

::: 

## **Program 3: Operators, Control Structures, and Functions**

Problem Statement: Write a R program that includes different operators, control structures, default values for arguments, returning complex objects

::: details View Code

<JupyterLite kernel="xr">

```r
# Function with default argument values
calculate_area <- function(shape = "rectangle", length = 5, width = 3) {
  if (shape == "rectangle") {
    area <- length * width
  } else if (shape == "circle") {
    radius <- length / 2
    area <- pi * radius^2
  } else {
    cat("Unsupported shape:", shape, "\n")
    return(NULL)
  }
  
  # Conditional operator
  message <- ifelse(area > 10, "Large area", "Small area")
  
  result <- list(
    Shape = shape,
    Length = length,
    Width = width,
    Area = area,
    Message = message
  )
  return(result)
}

# Using the function with default arguments
result1 <- calculate_area()
result2 <- calculate_area("rectangle", 8, 4)
result3 <- calculate_area("circle", 6)
```

</JupyterLite>
::: 

## **Program 4: Quick Sort and Binary Search Tree Implementation**

Problem Statement: Write a R program for quick sort implementation, binary search tree

::: details View Code

<JupyterLite kernel="xr">

```r
# Quick Sort Implementation
quick_sort <- function(arr) {
  if (length(arr) <= 1) {
    return(arr)
  }
  
  pivot <- arr[^1]
  smaller <- arr[arr < pivot]
  equal <- arr[arr == pivot]
  larger <- arr[arr > pivot]
  
  sorted_smaller <- quick_sort(smaller)
  sorted_larger <- quick_sort(larger)
  
  return(c(sorted_smaller, equal, sorted_larger))
}

# Binary Search Tree Implementation
insert_node <- function(root, key) {
  if (is.null(root)) {
    return(list(key = key, left = NULL, right = NULL))
  }
  
  if (key < root$key) {
    root$left <- insert_node(root$left, key)
  } else if (key > root$key) {
    root$right <- insert_node(root$right, key)
  }
  
  return(root)
}

in_order_traversal <- function(root) {
  if (!is.null(root)) {
    in_order_traversal(root$left)
    cat(root$key, " ")
    in_order_traversal(root$right)
  }
}

# Example usage
arr <- c(6, 2, 8, 3, 1, 7, 5)
sorted_arr <- quick_sort(arr)
cat("Quick Sort Result:", sorted_arr, "\n")

# BST usage
bst_root <- NULL
keys <- c(6, 2, 8, 3, 1, 7, 5)
for (key in keys) {
  bst_root <- insert_node(bst_root, key)
}

cat("In-order Traversal of BST:")
in_order_traversal(bst_root)
```

</JupyterLite>

::: 

## **Program 5: Cumulative Operations and Calculus**

Problem Statement: Write a R program for calculating cumulative sums, and products minima maxima and calculus

::: details View Code

<JupyterLite kernel="xr">

```r
# Sample dataset
data <- c(2, 4, 1, 8, 5, 7)

# Cumulative sums
csum <- cumsum(data)
cat("Cumulative Sums:", csum, "\n")

# Cumulative products
cproduct <- cumprod(data)
cat("Cumulative Products:", cproduct, "\n")

# Minimum and Maximum
minvalue <- min(data)
maxvalue <- max(data)
cat("Minimum Value:", minvalue, "\n")
cat("Maximum Value:", maxvalue, "\n")

# Calculus: Differentiation
differentiate <- diff(data)
cat("Differentiation (First Difference):", differentiate, "\n")

# Calculus: Integration
integrate <- cumsum(data)
cat("Integration (Cumulative Sum):", integrate, "\n")
```

</JupyterLite>

::: 

## **Program 6: Markov Chain Stationary Distribution**

Problem Statement: Write a R program for finding stationary distribution of markanov chains

::: details View Code

<JupyterLite kernel="xr">

```r
# Install and load the markovchain package
# install.packages("markovchain")
library(markovchain)

# Define the transition matrix for your Markov chain
tm <- matrix(c(
  0.7, 0.3,
  0.2, 0.8
), byrow = TRUE, nrow = 2, dimnames = list(c("State1", "State2"), c("State1", "State2")))

# Create a Markov chain object
markov_chain <- new("markovchain", states = c("State1", "State2"), transitionMatrix = tm)

# Find the stationary distribution
stationary_distribution <- steadyStates(markov_chain)
print("Stationary Distribution:")
print(stationary_distribution)
```
</JupyterLite>

::: 

## **Program 7: Linear Algebra Operations**

Problem Statement: Write a R program that include linear algebra operations on vectors and matrices

::: details View Code

<JupyterLite kernel="xr">

```r
# Create vectors
vector1 <- c(1, 2, 3)
vector2 <- c(4, 5, 6)

# Create matrices
matrix1 <- matrix(c(1, 2, 3, 4, 5, 6), nrow = 2, ncol = 3)
matrix2 <- matrix(c(7, 8, 9, 10, 11, 12), nrow = 2, ncol = 3)

# Vector operations
vector_sum <- vector1 + vector2
vector_diff <- vector1 - vector2
scalar <- 2
vector_scalar_mult <- scalar * vector1

# Matrix operations
matrix_sum <- matrix1 + matrix2
matrix_diff <- matrix1 - matrix2
matrix_product <- matrix1 %*% t(matrix2)
matrix1_transpose <- t(matrix1)

# Display results
cat("Vector Addition:", vector_sum, "\n")
cat("Vector Subtraction:", vector_diff, "\n")
cat("Scalar Multiplication:", vector_scalar_mult, "\n")
print("Matrix Addition:")
print(matrix_sum)
print("Matrix Multiplication:")
print(matrix_product)
print("Matrix Transpose:")
print(matrix1_transpose)
```
</JupyterLite>

::: 

## **Program 8: Data Visualization with Graphics Functions**

Problem Statement: Write a R program for any visual representation of an object with creating graphs using graphic functions Plot,Hist,Linechart,Pie,Boxplot,Scatterplots

::: details View Code

<JupyterLite kernel="xr">

```r
# Scatter Plot
x <- c(1, 2, 3, 4, 5)
y <- c(3, 5, 7, 2, 8)
plot(x, y, main = "Scatter Plot", xlab = "X-axis", ylab = "Y-axis", pch = 19, col = "blue")

# Line Chart
plot(x, y, type = "l", main = "Line Chart", xlab = "X-axis", ylab = "Y-axis", col = "green")

# Histogram
data <- c(1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5)
hist(data, main = "Histogram", xlab = "Values", ylab = "Frequency", col = "lightblue")

# Box Plot
data <- list(A = c(2, 4, 6, 8), B = c(1, 3, 5, 7, 9))
boxplot(data, main = "Box Plot", xlab = "Groups", ylab = "Values", col = "orange")

# Pie Chart
categories <- c("A", "B", "C")
values <- c(30, 40, 20)
pie(values, labels = categories, main = "Pie Chart", col = c("red", "green", "blue"))
```
</JupyterLite>

::: 

## **Program 9: Data Frame Operations and Analysis**

Problem Statement: ​Write a R program for with any dataset containing dataframe objects, indexing and subsetting data frames, and employ manipulating and analyzing data

::: details View Code

<JupyterLite kernel="xr">

```r
# Create employee dataset
employee_data <- data.frame(
  EmployeeID = c(1, 2, 3, 4, 5),
  FirstName = c("John", "Alice", "Bob", "Carol", "David"),
  LastName = c("Smith", "Johnson", "Johnson", "Smith", "Davis"),
  Age = c(30, 25, 28, 35, 32),
  Department = c("HR", "Marketing", "Finance", "HR", "IT"),
  Salary = c(50000, 55000, 60000, 52000, 70000)
)

# Subsetting operations
hr_employees <- employee_data[employee_data$Department == "HR", ]
older_employees <- employee_data[employee_data$Age >= 30, ]
high_salary_employees <- employee_data[employee_data$Salary > 55000, ]

# Data analysis
average_salary <- mean(employee_data$Salary)
max_age <- max(employee_data$Age)
department_counts <- table(employee_data$Department)
department_payroll <- tapply(employee_data$Salary, employee_data$Department, sum)

# Display results
print(employee_data)
print(hr_employees)
cat("Average Salary:", average_salary, "\n")
cat("Maximum Age:", max_age, "\n")
print(department_counts)
print(department_payroll)
```
</JupyterLite>

::: 

## **Program 10: Multivariate Linear Regression**

Problem Statement: Write a program to create an any application of Linear Regression in a multivariate context for predictive purpose

::: details View Code

<JupyterLite kernel="xr">

```r
# Sample dataset: Salary, Experience, Education
data <- data.frame(
  Salary = c(50000, 60000, 75000, 80000, 95000, 110000, 120000, 130000),
  Experience = c(1, 2, 3, 4, 5, 6, 7, 8),
  Education = c(12, 14, 16, 16, 18, 20, 20, 22)
)

# Perform multivariate linear regression
model <- lm(Salary ~ Experience + Education, data = data)

# Predict salaries for new data
new_data <- data.frame(
  Experience = c(9, 10),
  Education = c(22, 24)
)
predicted_salaries <- predict(model, newdata = new_data)

# Display results
summary(model)
cat("Predicted Salaries:\n")
print(predicted_salaries)
```

</JupyterLite>

::: 