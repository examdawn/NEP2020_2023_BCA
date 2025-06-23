---
order: 5
title: PP - Unit 4 Solved
---
# Python Programming - Unit 4

> [!WARNING]
> This Page is incomplete and answers will be added soon. 3/9 Remaining.

## Q1. Explain file types with example. 

Text files store character data and do not have any specific encoding, which allows them to be opened and read in a standard text editor
- In Python, when you open a text file, it returns a TextIOWrapper file object. 
- Text mode is the default when working with files in Python

Examples of text files include:
- Documents: .txt, .rtf, .tex
- Source Code: .py, .java, .c, .js
- Web Standards: .html, .xml, .css, .json
- Tabular Data: .csv, .tsv
- Configuration Files: .ini, .cfg, .reg

Binary files store data in a binary format (sequences of bytes), which is computer-readable but not human-readable in a standard text editor
- Most files on a computer system are binary files. 
- Opening these files requires specific software that can interpret their format. 
- In Python, opening a binary file for reading returns a BufferedReader object, and opening one for writing returns a BufferedWriter object

Examples of binary files include:
- **Image Files**: .png, .jpg, .gif, .bmp 
- **Document Files**: .pdf, .doc, .xls
- **Audio Files**: .mp3, .wav, .aac
- **Video Files**: .mp4, .mkv, .avi
- **Archive Files**: .zip, .rar, .iso
- **Database Files**: .sqlite, .mdb
- **Executable Files**: .exe, .dll 


## Q2. Explain creating/writing/reading/appending into a file with an example.

In Python, you can perform file operations like creating, reading, writing, and appending using the built-in `open()` function. This function requires a file path and a mode to specify the intended operation.

### Creating a File

To create a new file, you can use the `open()` function with one of three modes: `"x"`, `"a"`, or `"w"`.

*   **`"x"` (Create)**: This mode creates a new file but will raise an error if a file with the same name already exists. This is useful for avoiding accidental overwrites.
*   **`"w"` (Write)**: This mode will create a file if it does not exist.
*   **`"a"` (Append)**: This mode will also create a file if it does not already exist.

**Example using `"x"` mode:**
This code creates a new, empty file named "myfile.txt".
```python
# Creates a new file; raises an error if "myfile.txt" already exists.
f = open("myfile.txt", "x")
f.close()
```

### Writing to a File

Writing to a file is done using the `"w"` mode. This mode will overwrite any existing content in the file. If the file doesn't exist, it will be created.

You can write content using two primary methods:
*   `write()`: Writes a single string to the file.
*   `writelines()`: Writes a list of strings to the file. You must add newline characters (`\n`) to separate the lines.

**Example:**
This example opens "demofile.txt" in write mode and overwrites its contents.
```python
# Open the file in write mode ("w")
with open("demofile.txt", "w") as f:
    # Overwrite the file with new content
    f.write("Woops! I have deleted the content!")

# To verify, open and read the file
with open("demofile.txt", "r") as f:
    print(f.read())
```

### Appending to a File

To add content to the end of an existing file without deleting its current data, you use the append (`"a"`) mode. If the specified file does not exist, this mode will create it. The key difference from write mode is that append does not clear the file's contents.

**Example:**
This code adds a new line to "demofile.txt" without overwriting what's already there.
```python
# Open the file in append mode ("a")
with open("demofile.txt", "a") as f:
    # Add content to the end of the file
    f.write("\nNow the file has more content!")

# To verify, open and read the file
with open("demofile.txt", "r") as f:
    print(f.read())
```

### Reading from a File

To read a file's contents, you open it in read (`"r"`) mode, which is the default mode for `open()`. Python offers several methods for reading:

*   **`read()`**: Reads the entire content of the file as a single string. You can also specify the number of characters to read, like `read(5)`.
*   **`readline()`**: Reads a single line from the file.
*   **`readlines()`**: Reads all lines from the file and returns them as a list of strings.
*   **`for` loop**: Iterating directly over the file object is a memory-efficient way to read a file line by line.

**Example:**
This example demonstrates different ways to read from "file.txt".
```python
# Assume "file.txt" contains:
# Hello!
# This is a text file.

# 1. Reading the entire file
with open("file.txt", "r") as f:
    content = f.read()
    print(content)

# 2. Reading line by line with a for loop
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip()) # .strip() removes leading/trailing whitespace including newlines
```

[mimo](https://mimo.org/glossary/python/file-handling)


## Q3. tell() and seek() methods

### tell()
The tell() method returns the current file position in a file stream.

### seek()
You can change the current file position with the seek() method.

### Example: 
TODO



## Q4. Explain object oriented concepts in python. 
TODO
## Q5. Explain python inheritance. Explain types of inheritance with example. 
TODO 

## Q6. Explain python private, protected and public access for variables/methods. How is it related to Encapsulation?

## Q7. Explain different types of Polymorphism in Python

Polymorphism in Python, derived from the Greek words "poly" (many) and "morph" (forms), refers to the ability of an entity (like a function, method, or operator) to take on different forms or behave differently depending on the context or the type of data it operates on. 
- It is a core concept in object-oriented programming (OOP) that promotes code reusability and flexibility.

### Method Overriding

This is the most common way to achieve polymorphism in Python. 
- A child class can provide a specific implementation for a method that is already defined in its parent class. 
- When the method is called on an object of the child class, the overridden method in the child class is executed instead of the parent's method.

```python
class Animal:
    def speak(self):
        print("Animal makes a sound")
class Dog(Animal):
    def speak(self):
        print("Dog barks")
class Cat(Animal):
    def speak(self):
        print("Cat meows")
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    animal.speak()
```

### Operator Overloading

Python allows operators (like +, -, *) to be redefined for custom classes. This means the same operator can perform different actions depending on the data types involved. For example, the + operator performs addition for numbers and concatenation for strings.

```python
print(2 + 3)  # Addition for integers
print("Hello" + "World")  # Concatenation for strings
```

## Q8. What is a Magic Method? 
(Also Known as Special Methods)

## Q9. Explain constructors in python

<!-- 
Explain file types with example. 

Explain types of operations performed on file with example. 

Explain creating/writing/reading/appending into a file with an example. 

Explain object oriented concepts in python. 

Explain python inheritance. Explain types of inheritance with example. 

Explain python private, protected and public access for variables/methods. How is it related to Encapsulation?

Explain about method overloading. 

Explain different types of Polymorphism in Python

What is a Magic Method? 
(Also Known as Special Methods)

Explain constructors in python

tell() and seek() methods

-->