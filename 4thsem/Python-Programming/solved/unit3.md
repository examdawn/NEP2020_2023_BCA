---
order: 4
title: PP - Unit 3 Solved
---
# Python Programming - Unit 3

## 1. Explain Membership Operator with an example
The membership operators in Python help us determine whether an item is present in a given container type object, or in other words, whether an item is a member of the given container type object. Python has two membership operators: in and not in. Both return a Boolean result. The result of in operator is opposite to that of not in operator.
### 1. ***The `in` Operator:***
- It's used to check whether a substring is present in a bigger string, any item is present in a list or tuple, or a sub-list or sub-tuple is included in a list or tuple. Syntax: `{value} in {sequence}:`


EXAMPLE:

`Input`:
```python
var = "oh myy gawd"
a = "oh"
b = "tor"
print (a, "in", var, ":", a in var)
print (b, "in", var, ":", b in var)
```
`Output`:
```txt
oh in oh myy gawd : True
tor in oh myy gawd : False
```

### 2. ***The `not in` Operator:***
- It's used to check a sequence with the given value is not present in the object like string, list, tuple, etc. Syntax: `{value} not in {sequence}:`

EXAMPLE:

`Input`:
```python
var = "oh myy gawd"
a = "oh"
b = "tor"
print (a, "not in", var, ":", a not in var)
print (b, "not in", var, ":", b not in var)
```
`Output`:
```txt
oh not in oh myy gawd : False
tor not in oh myy gawd : True
```

[TutorialsPoint](https://www.tutorialspoint.com/python/python_membership_operators.htm)

## 2. Explain Splice Operator in detail with examples
The `slice()` function returns a slice object. A slice object is used to specify how to slice a sequence. You can specify where to start the slicing, and where to end. You can also specify the step, which allows you to e.g. slice only every other item.  
Syntax: `slice(start, end, step)`  
EXAMPLE:  
`Input`:
```python
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(3, 5)
print(a[x])
```
`Output`:
```txt
('a', 'b')
```

[w3Schools](https://www.w3schools.com/python/ref_func_slice.asp)

## 3. What are iterable data types?
In Python, an iterable object (or simply an iterable) is a collection of elements that you can loop (or iterate) through one element at a time. Simply put, an iterable is a list-like (or array-like) object. There are many kinds of iterables, which differ in many ways, including whether they are ordered and mutable:
- An iterable is ordered if you can retrieve its elements in a predictable order
- An iterable is mutable if you can change which elements it contains
Python has four built-in iterable types: list, dict, tuple, and set

## 4. What is a list ? Mention any four operations performed on list.
A Python list is a data structure that stores an ordered collection of items, which can be of different data types. Lists are mutable, meaning that their contents can be changed after creation. Lists are represented using square brackets `[]`.

The four operations performed on lists:
- `append()`: Adds an item to the end of the list.
- `remove()`: Removes the first occurrence of a specified value from the list.
- `sort()`: Sorts the items of the list in ascending order.
- `pop()`: Removes and returns the item at the specified position in the list.

EXAMPLE:

`Input`:
```python
val = [3, 1, 4, 1, 5, 9]

val.append(2)
print("After append():", val)

val.remove(1)
print("\nAfter remove(1):", val)

val.sort()
print("\nAfter sort():", val)

popped_value = val.pop(2)
print("\nPopped value:", popped_value)
print("After pop(2):", val)
```

`Output`:
```txt
After append(): [3, 1, 4, 1, 5, 9, 2]

After remove(1): [3, 4, 1, 5, 9, 2]

After sort(): [1, 2, 3, 4, 5, 9]

Popped value: 3
After pop(2): [1, 2, 4, 5, 9]
```

[GeeksforGeeks](https://www.geeksforgeeks.org/python/python-lists/)

## 5. What is a tuple? Mention any four operations performed on it.
A Python tuple is a data structure that stores an ordered collection of items, similar to a list, but tuples are immutable, meaning that their contents cannot be changed after creation. Tuples are represented using parentheses `()`.

The four operations performed on tuples:
- `count()`: Returns the number of times a specified value appears in the tuple.
- `index()`: Returns the index of the first occurrence of a specified value in the tuple.
- `len()`: Returns the number of items in the tuple.
- `concatenate`: Combines two tuples into one.

EXAMPLE:

`Input`:
```python
val = (1, 2, 3, 2, 4)

count_of_2 = val.count(2)
print("Count of 2:", count_of_2)

index_of_3 = val.index(3)
print("Index of 3:", index_of_3)

length = len(val)
print("Length of tuple:", length)

new_tuple = val + (5, 6)
print("After concatenation:", new_tuple)
```

`Output`:
```txt
Count of 2: 2
Index of 3: 2
Length of tuple: 5
After concatenation: (1, 2, 3, 2, 4, 5, 6)
```

[GeeksforGeeks](https://www.geeksforgeeks.org/tuples-in-python/)

## 6. What is a set? Mention any four operations performed on it.

A Python set is a data structure that stores an unordered collection of unique items. Sets are mutable, meaning that their contents can be changed after creation, but they do not allow duplicate values. Sets are represented using curly brackets `{}`.

The four operations performed on sets:
- `add()`: Adds an element to the set.
- `remove()`: Removes a specified element from the set. Raises an error if the element is not found.
- `union()`: Returns a new set containing all elements from both sets.
- `intersection()`: Returns a new set containing only the elements that are present in both sets.

EXAMPLE:

`Input`:
```python
val = {1, 2, 3, 4}

val.add(5)
print("After add(5):", val)

val.remove(2)
print("\nAfter remove(2):", val)

another_set = {3, 4, 5, 6}
union_set = val.union(another_set)
print("\nUnion:", union_set)

intersection_set = val.intersection(another_set)
print("Intersection:", intersection_set)
```

`Output`:
```txt
After add(5): {1, 2, 3, 4, 5}

After remove(2): {1, 3, 4, 5}

Union: {1, 3, 4, 5, 6}

Intersection: {3, 4, 5}
```

[GeeksforGeeks](https://www.geeksforgeeks.org/python/sets-in-python/)

## 7. What is a dictionary? Mention any four operations performed on it.
Python dictionary is a data structure that stores the value in key: value pairs. Values in a dictionary can be of any data type and can be duplicated, whereas keys can't be repeated and must be immutable. The keys and values are represented inside the Curly Brackets `{ }`.   
The four operations performed on dictonary:
- `clear()`: Removes all the elements from the dictionary.
- `copy()`: Returns a copy of the dictionary.
- `items()`: Returns a list containing a tuple for each key value pair.
- `keys()`: Returns a list containing the dictionary's keys.

EXAMPLE:

`Input`:
```python
val = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}

val.clear()
print("After clear():", val)

val = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}
copied = val.copy()
print("\nCopy:", copied)

print("\nItems:", list(val.items()))
print("Keys:", list(val.keys()))
```
`Output`:
```txt
After clear(): {}

Copy: {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

Items: [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
Keys: [1, 2, 3, 4, 5]
```

[w3Schools](https://www.w3schools.com/python/ref_dictionary_clear.asp)

## 8. Differentiate between List, Tuple, Set, Dictionary and String with an example
The difference between List, Tuple, Set, Dictionary and String are:
### List
- **Description**: A non-homogeneous data structure that stores elements in columns of a single row or multiple rows.
- **Representation**: `[ ]`
- **Allows Duplicates**: Yes
- **Nesting Capability**: Yes
- **Example**: `[1, 2, 3, 4, 5]`

### Tuple
- **Description**: A non-homogeneous data structure that stores elements in columns of a single row or multiple rows.
- **Representation**: `( )`
- **Allows Duplicates**: Yes
- **Nesting Capability**: Yes
- **Example**: `(1, 2, 3, 4, 5)`

### Set
- **Description**: A non-homogeneous data structure that stores the elements in a single row.
- **Representation**: `{ }`
- **Allows Duplicates**: No
- **Nesting Capability**: Yes
- **Example**: `{1, 2, 3, 4, 5}`

### Dictionary
- **Description**: A non-homogeneous data structure that stores key-value pairs.
- **Representation**: `{ }`
- **Allows Duplicates**: No (for keys)
- **Nesting Capability**: Yes
- **Example**: `{1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}`

### String
- **Description**: A sequence of characters used to represent text.
- **Representation**: `""` or `''`
- **Allows Duplicates**: Yes (characters can repeat)
- **Nesting Capability**: Yes (strings can be part of lists, tuples, etc.)
- **Example**: `"Hello, World!"`

[GeeksforGeeks](https://www.geeksforgeeks.org/python/differences-and-applications-of-list-tuple-set-and-dictionary-in-python/)

## 9. What is a nested list?
Lists are useful data structures commonly used in Python programming. A nested list is a list of lists, or any list that has another list as an element (a sublist). They can be helpful if we want to create a matrix or need to store a sublist along with other data types.

EXAMPLE: 

`Input`:
```python
nestedList = [1, 2, ['a', 1], 3]

subList = nestedList[2]
element = nestedList[2][0]

print("List inside the nested list: ", subList)
print("First element of the sublist: ", element)
```

`Output`:
```text
List inside the nested list:  ['a', 1]
First element of the sublist:  a
```

[how.dev](https://how.dev/answers/what-are-nested-lists-in-python)
