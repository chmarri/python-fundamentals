# Python Interview Guide

This comprehensive guide covers key Python concepts, functions, and techniques based on the Python Fundamentals course structure. It is designed to serve as a quick reference for technical interviews.

---

## 02 - Installing and Running Python

### Virtual Environments
**Definition**: A self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages. It prevents dependency conflicts between projects.
**Code Example**:
```bash
# Creating a virtual environment
python3 -m venv .venv

# Activating it (Linux/Mac)
source .venv/bin/activate
```

### pip
**Definition**: The standard package installer for Python.
**Code Example**:
```bash
pip install requests
pip freeze > requirements.txt
```

---

## 03 - Python Basics

### Basic Data Types
**Definition**: The fundamental types in Python including Integers (`int`), Floating point numbers (`float`), and Booleans (`bool`).
**Code Example**:
```python
x = 10          # int
y = 3.14        # float
is_valid = True # bool
```

### Arithmetic & Comparison
**Definition**: Standard operators for math (`+`, `-`, `*`, `/`, `//`, `%`) and comparison (`==`, `!=`, `>`, `<`).
**Code Example**:
```python
result = 10 // 3  # Integer division: 3
remainder = 10 % 3 # Modulus: 1
check = 5 > 3     # True
```

---

## 04 - Conditional Execution

### if, elif, else
**Definition**: Control flow statements that execute code blocks based on boolean conditions.
**Code Example**:
```python
x = 10
if x > 10:
    print("High")
elif x == 10:
    print("Equal")
else:
    print("Low")
```

### Ternary Operator
**Definition**: A one-line shorthand for an if-else statement.
**Code Example**:
```python
status = "Adult" if age >= 18 else "Minor"
```

---

## 05 - Sequence Types

### Lists & Tuples
**Definition**: Ordered collections of items. Lists are mutable (can be changed), while tuples are immutable.
**Code Example**:
```python
my_list = [1, 2, 3]
my_list[0] = 10      # Allowed

my_tuple = (1, 2, 3)
# my_tuple[0] = 10   # Raises TypeError
```

### Slicing
**Definition**: A technique to extract a portion of a sequence using the syntax `[start:stop:step]`.
**Code Example**:
```python
nums = [0, 1, 2, 3, 4, 5]
subset = nums[1:4]   # [1, 2, 3]
reversed = nums[::-1] # [5, 4, 3, 2, 1, 0]
```

### Unpacking
**Definition**: Assigning elements of a sequence to individual variables in a single statement.
**Code Example**:
```python
a, b, c = (1, 2, 3)
first, *rest = [1, 2, 3, 4] # first=1, rest=[2, 3, 4]
```

---

## 06 - Strings

### Common Methods
**Definition**: Built-in methods to manipulate text.
**Code Example**:
```python
s = "  python  "
clean = s.strip().upper()  # "PYTHON"
parts = "a,b,c".split(",") # ['a', 'b', 'c']
joined = "-".join(parts)   # "a-b-c"
```

### String Interpolation (f-strings)
**Definition**: A concise way to embed expressions inside string literals, using `{}`.
**Code Example**:
```python
name = "Alice"
greeting = f"Hello, {name.upper()}" # "Hello, ALICE"
```

---

## 07 - Iteration

### Loops (for & while)
**Definition**: Constructs to repeat a block of code. `for` iterates over sequences; `while` repeats as long as a condition is true.
**Code Example**:
```python
for i in range(3):
    print(i) # 0, 1, 2

count = 0
while count < 3:
    count += 1
```

### break, continue, else
**Definition**: `break` exits the loop; `continue` skips to the next iteration; `else` runs if the loop completes without breaking.
**Code Example**:
```python
for n in range(5):
    if n == 2: continue
    if n == 4: break
    print(n) # Prints 0, 1, 3
```

---

## 08 - Dictionaries

### Dictionary Methods
**Definition**: Key-value stores with methods to access and manipulate data.
**Code Example**:
```python
d = {"name": "Alice", "age": 30}
age = d.get("age", 0)          # Safe access
keys = list(d.keys())          # ['name', 'age']
items = list(d.items())        # [('name', 'Alice'), ('age', 30)]
```

---

## 09 - Sets

### Set Operations
**Definition**: Unordered collections of unique elements. Supports mathematical set operations.
**Code Example**:
```python
A = {1, 2, 3}
B = {3, 4, 5}
union = A | B        # {1, 2, 3, 4, 5}
intersection = A & B # {3}
diff = A - B         # {1, 2}
```

---

## 10 - Comprehensions

### List, Dict, Set Comprehensions
**Definition**: Concise syntax to create new collections from existing iterables.
**Code Example**:
```python
squares = [x**2 for x in range(5)]             # [0, 1, 4, 9, 16]
even_map = {x: x%2==0 for x in range(3)}       # {0: True, 1: False, 2: True}
unique_lengths = {len(w) for w in ["a", "bb"]} # {1, 2}
```

---

## 11 - Exceptions

### Handling Exceptions
**Definition**: Managing runtime errors using `try`, `except`, `finally` blocks to prevent program crashes.
**Code Example**:
```python
try:
    val = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Execution complete")
```

---

## 12 - Iterables and Iterators

### Iterators & Generators
**Definition**: An iterable is an object you can loop over. A generator is a function that yields values one at a time using `yield`, saving memory.
**Code Example**:
```python
def my_gen(n):
    for i in range(n):
        yield i * 2

g = my_gen(3)
print(next(g)) # 0
print(next(g)) # 2
```

---

## 13 - Functions

### *args and **kwargs
**Definition**: Syntax to allow a function to accept an arbitrary number of positional (`*args`) and keyword (`**kwargs`) arguments.
**Code Example**:
```python
def func(*args, **kwargs):
    print(args)   # tuple of positional args
    print(kwargs) # dict of keyword args

func(1, 2, a=3) # args=(1, 2), kwargs={'a': 3}
```

### Lambda Functions
**Definition**: Small, anonymous functions defined with the `lambda` keyword.
**Code Example**:
```python
add = lambda x, y: x + y
print(add(2, 3)) # 5
```

---

## 14 - Some Additional Built-In Functions

### zip, map, sorted
**Definition**: Utility functions for processing iterables. `zip` combines iterables; `sorted` returns a new sorted list.
**Code Example**:
```python
names = ["A", "B"]
scores = [10, 20]
combined = list(zip(names, scores)) # [('A', 10), ('B', 20)]

nums = [3, 1, 2]
sorted_nums = sorted(nums) # [1, 2, 3]
```

---

## 16 - Higher Order Functions

### Map & Closures
**Definition**: Functions that take other functions as arguments or return them. A closure is a nested function capturing the outer scope's variables.
**Code Example**:
```python
# Map
squared = list(map(lambda x: x**2, [1, 2, 3])) # [1, 4, 9]

# Closure
def outer(msg):
    def inner():
        print(msg)
    return inner

func = outer("Hello")
func() # Prints "Hello"
```

---

## 17 - Sorting and Filtering

### Custom Sorting & Filtering
**Definition**: Using `key` in `sorted()` to sort by specific criteria, and `filter()` to select elements.
**Code Example**:
```python
data = ["apple", "banana", "cherry"]
# Sort by length
by_len = sorted(data, key=len) 

# Filter items starting with 'b'
b_words = list(filter(lambda x: x.startswith('b'), data))
```

---

## 18 - Decorators

### Decorators & LRU Cache
**Definition**: Functions that modify the behavior of other functions. `lru_cache` memoizes return values.
**Code Example**:
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)
```

---

## 19 - Text Files

### Context Managers (with statement)
**Definition**: The recommended way to handle file I/O, ensuring files are properly closed even if errors occur.
**Code Example**:
```python
with open("data.txt", "w") as f:
    f.write("Hello World")

with open("data.txt", "r") as f:
    content = f.read()
```

---

## 20 - Modules and Imports

### Import Syntax
**Definition**: Mechanisms to include code from other files or libraries.
**Code Example**:
```python
import math
from datetime import datetime as dt

print(math.pi)
print(dt.now())
```

---

## 21 - Dates and Times

### datetime Module
**Definition**: Classes for manipulating dates and times.
**Code Example**:
```python
from datetime import datetime, timedelta

now = datetime.now()
tomorrow = now + timedelta(days=1)
formatted = now.strftime("%Y-%m-%d") # "2023-10-27"
```

---

## 22 - CSV Module

### Reading and Writing CSVs
**Definition**: Handling Comma Separated Value files using the `csv` module.
**Code Example**:
```python
import csv

# Writing
with open('file.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['Alice', 30])
```

---

## 23 - Random Module

### Randomness
**Definition**: Generating pseudo-random numbers and making random selections.
**Code Example**:
```python
import random

val = random.randint(1, 10)   # Random int 1-10
item = random.choice(['a', 'b', 'c'])
random.shuffle([1, 2, 3])     # Shuffles in-place
```

---

## 24 - Math and Statistics Module

### Math Operations
**Definition**: Standard mathematical functions and statistical calculations.
**Code Example**:
```python
import math
import statistics

root = math.sqrt(16)       # 4.0
avg = statistics.mean([1, 2, 3, 4]) # 2.5
```

---

## 25 - Decimal Module

### High Precision Arithmetic
**Definition**: Provides support for fast correctly-rounded decimal floating point arithmetic, avoiding binary float errors.
**Code Example**:
```python
from decimal import Decimal

price = Decimal('10.00')
tax = Decimal('0.05')
total = price + (price * tax) # Decimal('10.5000')
```

---

## 26 - Custom Classes

### Classes & Magic Methods
**Definition**: Blueprints for creating objects. Magic methods (dunder methods) like `__init__` and `__str__` define object behavior.
**Code Example**:
```python
class Dog:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Dog: {self.name}"

d = Dog("Buddy")
print(d) # "Dog: Buddy"
```

---

## 28 - 3rd Party Libraries

### requests
**Definition**: A popular HTTP library for making web requests.
**Code Example**:
```python
import requests

response = requests.get('https://api.github.com')
if response.status_code == 200:
    data = response.json()
```

---

## 29 - NumPy

### Arrays & Vectorization
**Definition**: The core library for scientific computing. It provides a high-performance multidimensional array object and tools for working with these arrays.
**Code Example**:
```python
import numpy as np

arr = np.array([1, 2, 3, 4])
doubled = arr * 2          # Vectorized operation: [2, 4, 6, 8]
matrix = arr.reshape(2, 2) # 2x2 matrix
```

---

## 30 - Pandas

### DataFrames & Series
**Definition**: A library providing high-performance, easy-to-use data structures and data analysis tools. The `DataFrame` is a tabular data structure.
**Code Example**:
```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Age': [25, 30]
})
alice = df[df['Name'] == 'Alice'] # Filtering
```

---

## 31 - Matplotlib

### Plotting
**Definition**: A plotting library for creating static, animated, and interactive visualizations.
**Code Example**:
```python
import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [2, 4, 6]

plt.plot(x, y)
plt.title("Simple Plot")
plt.show()
```
