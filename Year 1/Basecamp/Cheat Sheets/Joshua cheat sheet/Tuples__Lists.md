> [!info] Reference
> [[Introducing Python - Book]] - Chapter 7.
# Tuples
- Are *immutable*
- *"too-pull"* or *"tub-pul"* ?
``` Python
# Creating an empty tuple
>>> empty_tuple = ()
>>> empty_tuple = tuple()


# Initializing a tuple
>>> filled_tuple = ("Item",)

# Or
>>> filled_tuple = "Item",

# This does not work
>>> filled_tuple = ("Item")
>>> type(filled_tuple)
<class 'str'>
```
### Tuples let you assign multiple variables at once
``` Python
>>> animals = ("Dog", "Cat", "Fish")
>>> a, b, c = animals
>>> b
'Cat'
```
### Converting from other items to a tuple with `tuple()`
``` Python
>>> names = ["John", "Max", "Bob"]
>>> my_tuple = tuple(names)
```
### Combining tuples with `+`
- Similar to combining [[Text Strings]]
``` Python
>>> ("Dog") + ("Cat", "Fish")
('Dog', 'Cat', 'Fish')
```
### Duplicate items with `*`
``` Python
>>> ("Yada") * 3
('Yada', 'Yada', 'Yada')
```
### Comparing tuples
- The `<`, `<=`, `>`, `>=` operators compare tuple sizes
``` Python
>>> ("Cat", "Dog") == ("Cat", "Dog", "Fish")
False
>>> ("Cat", "Dog") < ("Cat", "Dog", "Fish")
True
```
# Lists
- Are *mutable*
``` Python
# Creating an empty list
>>> empty_list = []
>>> empty_list = list()


# Initializing a list
filled_list = ["Item"]
```
### Converting from other items to a list with `list()`
``` Python
>>> list["Cat"]
['C', 'a', 't']
```
### Creating a list from a string with `split()`
``` Python
>>> date = "20-10-2002"
>>> date.split("-")
['20', '10', '2002']
```
### Get subsets with a slice
- Similar to slicing [[Text Strings]]
``` Python
>>> names = ["John", "Max", "Bob"]
>>> names[0:2:1]
['John', 'Max']
```
### Changing items in a list
- Possible because lists are *mutable*
``` Python
>>> names = ["John", "Max", "Bob", "Alex", "Tim"]
>>> names[2] = "Joshua"
>>> names
['John', 'Max', 'Joshua', 'Alex', 'Tim']

# Also works with slices
>>> names = ["John", "Max", "Bob", "Alex", "Tim"]
>>> names[1:3] = ["Joshua", "Noah"]
>>> names
['John', 'Joshua', 'Noah', 'Alex', 'Tim']
```
### Add items to the end of a list with `append()`
### Insert items at an index with `insert()`, this moves items to the right of this index further to the right
### Combine lists with `extend()`, `+` or `+=`
### Deleting an item at index with `del`
``` Python
>>> names = ["John", "Max", "Bob", "Alex", "Tim"]
>>> del names[1]
>>> names
>>> ["John", "Bob", "Alex", "Tim"]
```
### Deleting an item by value with `remove()`
``` Python
>>> names = ["John", "Max", "Bob", "Alex", "Tim"]
>>> names.remove("Alex")
>>> names
>>> ["John", "Max", "Bob", "Tim"]
```
### Getting an item by offset and deleting it with `pop()`
``` Python
>>> names = ["John", "Max", "Bob", "Alex", "Tim"]
>>> names.pop()
'Tim'
>>> names
['John', 'Max', 'Bob', 'Alex']

>>> names.pop(1)
'Max'
>>> names
['John', 'Bob', 'Alex']
```
### Delete all items from a list with `clear()`
### Find an items offset by value with `index()`
### Count item occurrences with `count()`
### Converting a list to a string with `join()`
``` Python
>>> names = ["John", "Max", "Bob"]
>>> ", ".join(names)
'John, Max, Bob'
```
### Sort a list *in place* with `sort()`
### Get a sorted *copy* of a list with `sorted()`
### Get list length with `len()`
### Get a copy of a list with `copy()`, `list()`, or `[:]`
### Copy nested lists with `deepcopy()`
``` Python
>>> import copy
>>> a = [1, 2, [8, 9]]
>>> b = copy.deepcopy(a)
>>> a[2][1] = 10
>>> a
[1, 2, [8, 10]]
>>> b
[1, 2, [8, 9]]
```
### Iterating over multiple lists in parallel with `zip()`
- Stops when the shortest sequence is done
``` Python
>>> days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
>>> names = ["John", "Max", "Bob", "Alex", "Tim"]
>>> for day, name in zip(days, names):
...     print(f"{day} : {name}")
...
Mon : John
Tue : Max
Wed : Bob
Thu : Alex
Fri : Tim
```
### List comprehensions
``` Python
>>> number_list = [number - 1 in range(1,6)]
>>> number_list
[0, 1, 2, 3, 4]


>>> rows = range(1,4)
>>> cols = range(1,3)
>>> cells = [(row, col) for row in rows for col in cols]
>>> for cell in cells:
...     print(cell)
...
(1, 1)
(1, 2)
(2, 1)
(2, 2)
(3, 1)
(3, 2)
```
## Tuples vs Lists
- Tuples use less space
- You can use tuples as dictionary keys
- *Named tuples* can be a simple alternative to objects
### Tuple unpacking
``` Python
>>> for row, col in cells:
...     print(row, col)
...
1 1
1 2
2 1
2 2
```
### There are no tuple comprehensions
- Note that the type is not of class `tuple`
``` Python
>>> numbers = (number for number in range(1, 6))
>>> type(numbers)
<class 'generator'>
```
