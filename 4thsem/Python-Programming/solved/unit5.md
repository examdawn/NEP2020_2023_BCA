---
order: 6
title: PP - Unit 5 Solved
---

# Python Programming - Unit 5

## Q1. What is the Tkinter Module and tk() class? Explain features of the Tkinter Module
The Tkinter module is Python's standard, built-in library for creating Graphical User Interfaces (GUIs) for desktop applications. 
- As the standard Python interface to the Tcl/Tk GUI toolkit, it is lightweight, cross-platform (working on Windows, macOS, and Linux), and included with most Python installations, so no separate installation is needed.

The tk.Tk() class is the core component for starting a Tkinter application. 
- When you create an instance of this class (e.g., root = tk.Tk()), you are creating the main, top-level window that serves as the primary container for all other GUI elements, known as widgets.
- This root window is what the user sees as the application's main window, and the program is typically started by calling the mainloop() method on this object, which listens for user events.


Tkinter provides a variety of tools to build interactive applications. Its main features include:
- **Widget Library**: Tkinter offers a wide range of pre-built GUI components called widgets, which are the building blocks of an application. These include containers like Frame, buttons, labels, text entry boxes, checkboxes, and menus
- **Layout Management**: It includes geometry managers like pack(), grid(), and place() that control how widgets are arranged within the window, allowing for organized and responsive designs
- **Event Handling**: Tkinter has a robust event-driven model that allows you to bind functions (callbacks) to user actions, such as button clicks, mouse movements, or key presses, making the application interactive
- **Built-in Dialogs**: It provides modules for common pop-up dialogs, such as message boxes (`showinfo`, `showerror`) and file selection dialogs (`askopenfilename`), which simplifies user interaction
- **Graphic Drawing**: The Canvas widget allows for custom drawing of shapes, text, and images directly within the application window

## Q2. Name some widgets supported by Tkinter

| Widget        | Description                                                       |
|---------------|-------------------------------------------------------------------|
| Label         | Display static text or images.                                    |
| Button        | It is used to add buttons to your application.                   |
| Entry         | It is used to input single line text entry from user.            |
| Frame         | It is used as a container to hold and organize the widgets.      |
| RadioButton   | It is used to implement one-of-many selection as it allows only one option to be selected. |
| Checkbutton   | Create checkboxes for boolean options.                           |
| ListBox       | Display a list of items for selection.                           |
| Scrollbar     | Add scrollbars to widgets like Listbox.                          |
| Menu          | It is used to create all kinds of menu used by an application.  |
| Canvas        | Draw shapes, lines, text, and images.                            |

[GeeksForGeeks](https://www.geeksforgeeks.org/python/what-are-widgets-in-tkinter/)

## Q3. Explain the process of creating a simple GUI Application with Tkinter using a neat Diagram
### 1. Import the Tkinter Module
First, you must import the Tkinter library. It's a standard convention to import it using the alias tk to make the code shorter and more readable
### 2. Create the Main Application Window
Next, create the main window, also known as the root window. This is done by creating an instance of the Tk class. This window will serve as the container for all other GUI elements (widgets)
### 3. Add Widgets to the Window
Widgets are the building blocks of the GUI, such as buttons, labels, and text boxes
- To add a widget, you create an instance of a widget class (e.g., tk.Label) and specify its parent, which is the main window you just created.
- After creating a widget, you must add it to the window using a geometry manager like `.pack()`, `.grid()`, or `.place()`. The `.pack()` method is the simplest way to place a widget in the window
### 4. Start the Event Loop
Finally, you must call the `mainloop()` method on the main window. 
- This command displays the window and tells the program to wait for user events, like mouse clicks or key presses, until the window is closed. 
- Without `mainloop()`, the window would appear and disappear instantly


### Putting all the steps together, a very simple Tkinter application looks like this:

```python
import tkinter as tk

# 1. Create the main window
window = tk.Tk()
window.title("Simple GUI")

# 2. Add a widget
label = tk.Label(window, text="Hello, Tkinter!")

# 3. Place the widget in the window
label.pack()

# 4. Start the event loop to display the window
window.mainloop()
```


::: details Output
![Tkinter Demo](image-1.png)
:::

## Q4. What is SQLite? Explain some features of an SQLite Database from sqlite3 module
SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language. Some applications can use SQLite for internal data storage. It’s also possible to prototype an application using SQLite and then port the code to a larger database such as PostgreSQL or Oracle. The features of an SQLite Database from sqlite3 module are:
- ***Serverless***:
    - SQLite does not require a server to run. SQLite database read and write directly from the database files stored on disk and applications interact with that SQLite database. 
- ***Self-Contained***:
    - It has no external dependencies. Everything it needs is included in a single library.
    - The entire database (schema + data) is stored in a single .sqlite or .db file.
    - This file can be copied, backed up, shared or moved like any other document.
- ***Zero-Configuration***:
    - No configuration files or startup services are needed.
    - You can start using SQLite as soon as you import the sqlite3 module in Python.
    - We can simply connect to a database file and if it doesn’t exist, SQLite automatically creates it.
- ***Transactional***:
    - SQLite supports full ACID (Atomicity, Consistency, Isolation, Durability) transactions:
    - Every operation in SQLite is atomic, i.e changes are either fully applied or not applied at all.
    - By default, SQLite wraps commands like INSERT, UPDATE and DELETE inside implicit transactions, ensuring data integrity.
- ***Single-Database***:
    - The entire database, i.e. tables, indexes, triggers and data, lives in a single file only.
    - This simplifies database management, as there's no need to manage multiple configuration or log files.
    - The file can be used across different platforms, tools and programming languages.  

[GeeksForGeeks](https://www.geeksforgeeks.org/python/introduction-to-sqlite-in-python/)

## Q5. Explain the process of creating database tables, performing read and update operations on an sqlite3 database using sqlite3 module in python
To create database tables and perform read and update operations using the `sqlite3` module in Python, follow these steps:

1. ***Establish a Database Connection***: Start by importing the `sqlite3` module and creating a connection to the database. If the database file does not exist, it will be created automatically.
   ```python
   import sqlite3
   con = sqlite3.connect("tutorial.db")
   ```
2. ***Create a Cursor***: A cursor is required to execute SQL commands. Create a cursor object from the connection.
   ```python
   cur = con.cursor()
   ```
3. ***Create a Table***: Use the `CREATE TABLE` SQL statement to define a new table. In this example, we create a `movie` table with columns for `title`, `year`, and `score`.
   ```python
   cur.execute("CREATE TABLE movie(title, year, score)")
   ```
4. ***Insert Data***: To add records to the table, use the `INSERT INTO` statement. You can insert multiple rows at once using `executemany()` with placeholders to prevent SQL injection.
   ```python
   data = [
       ('Monty Python and the Holy Grail', 1975, 8.2),
       ('And Now for Something Completely Different', 1971, 7.5)
   ]
   cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
   con.commit()  # Commit the transaction to save changes
   ```
5. ***Read Data***: To retrieve data, use the `SELECT` statement. You can fetch all results or iterate through them.
   ```python
   res = cur.execute("SELECT title, year FROM movie ORDER BY score DESC")
   for row in res:
       print(row)
   ```
6. ***Update Data***: To modify existing records, use the `UPDATE` statement. For example, to change the score of a movie:
   ```python
   cur.execute("UPDATE movie SET score = ? WHERE title = ?", (9.0, 'Monty Python and the Holy Grail'))
   con.commit()  # Commit the changes
   ```
7. ***Close the Connection***: After completing the operations, close the connection to ensure all changes are saved and resources are released.
   ```python
   con.close()
   ```  

   [python](https://docs.python.org/3/library/sqlite3.html)

## Q6. What is NumPy? Explain the features of NumPy
NumPy, short for "Numerical Python," is the fundamental open-source library for scientific computing in Python
- Its primary feature is the powerful N-dimensional array object, or ndarray, which provides an efficient way to store and operate on large, homogeneous datasets (arrays where all elements are of the same data type)
- NumPy is significantly faster than traditional Python lists because its arrays are stored in a continuous block of memory, and its core computational parts are written in high-performance languages like C and C++
- It serves as the foundational building block for many other data science libraries, including pandas, SciPy, and scikit-learn

NumPy's power comes from a rich set of features designed for high-performance numerical operations:
- Multidimensional Arrays: The core of NumPy is the ndarray object, which allows for the efficient creation and manipulation of vectors, matrices, and higher-dimensional arrays
- Element-wise Operations: NumPy allows you to perform mathematical operations on entire arrays at once without writing explicit loops, a concept known as vectorization. This makes the code cleaner and much faster
- Broadcasting: This powerful feature enables NumPy to perform operations on arrays of different shapes and sizes, simplifying calculations by automatically expanding the smaller array to match the larger one
- Mathematical Functions: It includes a vast collection of high-level mathematical functions for operations in linear algebra, statistical analysis, Fourier transforms, and more
- Memory Efficiency: NumPy arrays are more memory-efficient than Python lists, especially for large datasets, due to their contiguous memory storage
- Advanced Indexing and Slicing: It offers flexible and powerful ways to access, select, and manipulate data within arrays
- Integration with Other Libraries: NumPy integrates seamlessly with other scientific computing libraries, forming the backbone of the Python data science ecosystem

[DevOpsSchool](https://www.devopsschool.com/blog/what-is-numpy-and-use-cases-of-numpy/)
## Q7. Explain 4 Operations on NumPy Arrays with examples. 
NumPy arrays support a wide range of fast and efficient operations. These operations are vectorized, meaning they are applied to entire arrays at once without the need for explicit Python loops. Here are four fundamental types of operations you can perform on NumPy arrays.

### 1. Element-wise Arithmetic
Standard arithmetic operators like `+`, `-`, `*`, and `/` operate on an element-by-element basis. This means the operation is applied to each corresponding pair of elements in the arrays. The arrays must either have the same shape or be compatible for broadcasting.

**Example:**
```python
import numpy as np

# Create two arrays
array1 = np.array([10, 20, 30, 40])
array2 = np.array([1, 2, 3, 4])

# Addition
addition_result = array1 + array2
print(f"Addition: {addition_result}")

# Multiplication
multiplication_result = array1 * array2
print(f"Multiplication: {multiplication_result}")
```
**Output:**
```
Addition: [11 22 33 44]
Multiplication: [ 10  40  90 160]
```

### 2. Aggregation (Reductions)
Aggregation functions compute a summary statistic, like a sum or mean, across an array. These methods can be applied to the entire array or along a specific axis (rows or columns).

**Example:**
```python
import numpy as np

# Create a 2D array (matrix)
matrix = np.array([[1, 2], [3, 4]])

# Sum of all elements
total_sum = matrix.sum()
print(f"Total Sum: {total_sum}")

# Sum along columns (axis=0)
column_sum = matrix.sum(axis=0)
print(f"Sum of columns: {column_sum}")

# Sum along rows (axis=1)
row_sum = matrix.sum(axis=1)
print(f"Sum of rows: {row_sum}")
```
**Output:**
```
Total Sum: 10
Sum of columns: [4 6]
Sum of rows: [3 7]
```

### 3. Matrix Multiplication
While the `*` operator performs element-wise multiplication, it is not used for matrix multiplication. For true matrix multiplication, Python (version 3.5+) uses the `@` operator or NumPy's `.dot()` method.

**Example:**
```python
import numpy as np

matrix_A = np.array([[1, 1], [0, 1]])
matrix_B = np.array([[2, 0], [3, 4]])

# Element-wise product (NOT matrix multiplication)
elementwise_product = matrix_A * matrix_B
print(f"Element-wise Product:\n{elementwise_product}")

# Matrix product
matrix_product = matrix_A @ matrix_B
print(f"\nMatrix Product:\n{matrix_product}")
```

**Output:**
```
Element-wise Product:
[[2 0]
 [0 4]]

Matrix Product:
[[5 4]
 [3 4]]
```

### 4. Comparisons
You can compare two arrays element-wise using standard comparison operators like `==`, `>`
- The result is a new boolean array where each element is True or False based on the comparison of the corresponding elements in the original arrays

```python
import numpy as np

array_a = np.array([1, 2, 3, 4])
array_b = np.array([4, 2, 2, 4])

# Check for equality
equality_check = (array_a == array_b)
print(f"Equality check: {equality_check}")

# Check which elements in array_a are greater than 2
greater_than_check = (array_a > 2)
print(f"Greater than 2: {greater_than_check}")
```
**Output:**
```
Equality check: [False  True False  True]
Greater than 2: [False False  True  True]
```

[NumPy DevDocs](https://numpy.org/devdocs/user/absolute_beginners.html)

## Q8. Explain the importance of Data Visualization
Data visualization is a field in data analysis that deals with visual representation of data. It graphically plots data and is an effective way to communicate inferences from data. In other words, It's crucial as it transforms complex data into visual formats, making it easier to identify patterns, trends, and outliers. This enhances data interpretation, supports better decision-making, and effectively communicates insights to diverse audiences.
Using data visualization, we can get a visual summary of our data. With pictures, maps and graphs, the human mind has an easier time processing and understanding any given data. Data visualization plays a significant role in the representation of both small and large data sets, but it is especially useful when we have large data sets, in which it is impossible to see all of our data, let alone process and understand it manually. Python offers several plotting libraries, namely Matplotlib, Seaborn.   

[GeeksForGeeks](https://www.geeksforgeeks.org/data-visualization/data-visualization-with-python/)

## Q9. What is matplotlib? Mention its Features.
Matplotlib is a comprehensive and widely-used plotting library for the Python programming language and frequently used alongside its numerical extension, NumPy
- It is considered a foundational data visualization utility, allowing users to create a wide variety of static, animated, and interactive graphs and plots with just a few lines of code. 
- Matplotlib is designed to produce publication-quality figures and integrates seamlessly into the broader Python data science ecosystem.


Matplotlib provides a robust set of features that make it a versatile tool for data visualization:

- **Wide Variety of Plots**: It supports a diverse range of 2D plots, including line charts, bar graphs, scatter plots, histograms, and pie charts
- **High-Quality Output**: The library is designed to produce high-quality, publication-ready figures that can be fine-tuned for professional use
- **Extensive Customization**: Users have full control over nearly every element of a plot, such as line styles, colors, fonts, and axes properties, allowing for highly personalized visualizations
- **Multiple Output Formats**: Plots can be saved and exported in many common file formats, including PNG, PDF, SVG, and JPEG, making them easy to use in reports and presentations
- **Seamless Integration**: Matplotlib works well with other popular Python libraries, particularly NumPy and pandas, allowing for direct plotting of data from their data structures
- **Interactive Figures**: It can generate interactive plots that allow users to zoom, pan, and update the visualization, which is especially useful for data exploration in environments like Jupyter notebooks
- **Extensible Framework**: Matplotlib serves as the foundation for many other high-level plotting libraries, such as seaborn and Cartopy, which extend its functionality for more specific use cases


[MatPlotLib](https://matplotlib.org/)

[Wikipedia](https://en.wikipedia.org/wiki/Matplotlib)


## Q10. Mention a few matplotlib methods and some of their parameters
Matplotlib offers various methods for creating visualizations, each with specific parameters. Key methods include `plot()` for line charts, `bar()` for bar charts, and `scatter()` for scatter plots, with parameters like `color`, `linestyle`, and `marker` to customize the appearance of the plots. 

- ***`plt.plot()`***
  - **Parameters:**
    - `x`: The x-coordinates of the data points.
    - `y`: The y-coordinates of the data points.
    - `color`: Specifies the color of the line.
    - `linestyle`: Defines the style of the line (e.g., solid, dashed).
    - `marker`: Determines the style of the markers at data points.
  
- ***`plt.xlabel()` and `plt.ylabel()`***
  - **Parameters:**
    - `label`: The text label for the axis.
    - `fontsize`: Size of the font for the label.
    - `color`: Color of the label text.
  
- ***`plt.title()`***
  - **Parameters:**
    - `label`: The title text for the plot.
    - `fontsize`: Size of the font for the title.
    - `color`: Color of the title text.
  
- ***`plt.legend()`***
  - **Parameters:**
    - `labels`: A list of labels for each plot.
    - `loc`: Location of the legend (e.g., upper right).
    - `fontsize`: Size of the font for the legend text.
  
- ***`plt.grid()`***
  - **Parameters:**
    - `visible`: Boolean to show or hide the grid.
    - `color`: Color of the grid lines.
    - `linestyle`: Style of the grid lines (e.g., dashed).

- ***`plt.savefig()`***
  - **Parameters:**
    - `fname`: The filename for saving the plot.
    - `dpi`: Dots per inch for the output file.
    - `quality`: Quality of the saved image (for formats like JPEG).

[GeeksForGeeks](https://www.geeksforgeeks.org/python-introduction-matplotlib/)

## Q11. Explain different types of Charts supported by matplotlib
Python offers a variety of plotting functionalities, including line plots, bar charts, histograms, scatter plots and 3D visualizations.
Matplotlib supports various types of charts for data visualization, including:

1. ***Line Charts***: Great for showing trends over time.
   - Used to display trends over time or continuous data.
   - Created using the `plot()` function.
   - Can be customized with different colors, line styles, and markers.

2. ***Bar Charts***: Useful for comparing quantities across categories.
   - Ideal for comparing quantities across different categories.
   - Can be vertical (using `bar()`) or horizontal (using `barh()`).
   - Supports grouped and stacked variations for comparing multiple datasets.

3. ***Histograms***: Ideal for displaying data distributions.
   - Effective for visualizing the distribution of a dataset.
   - Data is grouped into bins, and the frequency of data points in each bin is displayed.
   - Created using the `hist()` function, with options for customizing the number of bins and normalization.

4. ***Scatter Plots***: Show relationships between two variables.
   - Used to show the relationship between two variables.
   - Each point represents an observation, allowing for the visualization of correlations.
   - Customizable with different colors, sizes, and marker styles using the `scatter()` function.

5. ***Pie Charts***: Represent proportions of a whole.
   - Represent proportions of a whole, with each slice corresponding to a category.
   - Created using the `pie()` function, with options for exploding slices and customizing colors.
   - Useful for displaying percentage data.

[GeeksForGeeks](https://www.geeksforgeeks.org/matplotlib-tutorial/)

<!--

What is the Tkinter Module and tk() class? Explain features of the Tkinter Module

Name some widgets supported by Tkinter

Explain the process of creating a simple GUI Application with Tkinter using a neat Diagram

Explain the importance of Data Visualization

What is SQLite? Explain some features of an SQLite Database from sqlite3 module

Explain the process of creating database tables, performing read and update operations on an sqlite3 database using command prompt

Explain the process of creating database tables, performing read and update operations on an sqlite3 database using sqlite3 module in python


What is NumPy? Explain the features of NumPy

Explain NumPy arrays with an example. 

Explain 4 Operations on Arrays with examples. 

What is matplotlib? Mention its Features.

Mention a few matplotlib methods and some of their parameters

Explain different types of Charts supported by matplotlib

-->
