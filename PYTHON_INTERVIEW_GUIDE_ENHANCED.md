# Python Interview Reference Guide
## Comprehensive Study Guide for Technical Interviews

---

## Table of Contents
1. [Python Basics](#python-basics)
2. [Sequence Types](#sequence-types)
3. [Strings](#strings)
4. [Control Flow](#control-flow)
5. [Dictionaries](#dictionaries)
6. [Sets](#sets)
7. [Comprehensions](#comprehensions)
8. [Functions](#functions)
9. [Iterables and Iterators](#iterables-and-iterators)
10. [Exception Handling](#exception-handling)
11. [Higher Order Functions](#higher-order-functions)
12. [Decorators](#decorators)
13. [File I/O](#file-io)
14. [Object-Oriented Programming](#object-oriented-programming)
15. [Modules and Packages](#modules-and-packages)
16. [Standard Library](#standard-library)
17. [Data Science Libraries](#data-science-libraries)

---

## Python Basics

### Data Types

**Definition**: Python has several built-in data types that form the foundation of all programs. The main primitive types are `int` (integers), `float` (floating-point numbers), `bool` (booleans), and `NoneType` (None).

**Key Concepts**:
- **Immutability**: int, float, bool, and None are all immutable - once created, their value cannot be changed
- **Dynamic Typing**: Variables don't have fixed types; the same variable can hold different types at different times
- **Type Conversion**: Use `int()`, `float()`, `str()`, `bool()` for explicit conversion
- **Truthiness**: Every value in Python has an inherent boolean value

**Code Examples**:
```python
# Type checking
x = 10
print(type(x))  # <class 'int'>

# Type conversion
num_str = "123"
num_int = int(num_str)  # 123
num_float = float(num_str)  # 123.0

# Truthiness - what evaluates to False
bool(0)        # False
bool("")       # False
bool(None)     # False
bool([])       # False - empty list
bool({})       # False - empty dict

# Everything else is True
bool(42)       # True
bool("hello")  # True
bool([1, 2])   # True
```

**Common Pitfalls**:
- Floating point precision: `0.1 + 0.2 != 0.3` (use `decimal` module for precise decimal arithmetic)
- Integer division: `5 / 2 = 2.5` (float division), `5 // 2 = 2` (integer division)
- `is` vs `==`: `is` checks identity (same object), `==` checks equality (same value)

**Best Practices**:
- Use `isinstance()` for type checking instead of `type()`: `isinstance(x, int)`
- For None checks, always use `is None` or `is not None`
- Use `//` for integer division to make intent clear

### Variables and Assignment

**Definition**: Variables in Python are references to objects, not containers that hold values. Assignment creates a new reference, not a copy.

**Key Concepts**:
- **References**: Variables are names that point to objects in memory
- **Multiple Assignment**: `a = b = c = 10` creates three references to the same object
- **Tuple Unpacking**: `a, b = 1, 2` assigns multiple values simultaneously
- **Mutable vs Immutable**: Assignment behavior differs based on object mutability

**Code Examples**:
```python
# Reference behavior
a = [1, 2, 3]
b = a  # b references the same list as a
b.append(4)
print(a)  # [1, 2, 3, 4] - a is modified too!

# With immutables, reassignment creates new object
x = 10
y = x
y = 20
print(x)  # 10 - x unchanged because int is immutable

# Multiple assignment
a, b, c = 1, 2, 3

# Swapping without temp variable
a, b = b, a

# Extended unpacking
first, *middle, last = [1, 2, 3, 4, 5]
# first=1, middle=[2,3,4], last=5
```

**Common Pitfalls**:
- Mutable default arguments: `def func(lst=[]):` creates ONE list shared across all calls
- Modifying lists during iteration can skip elements
- Shallow vs deep copy confusion with nested structures

---

## Sequence Types

### Lists

**Definition**: Lists are ordered, mutable, heterogeneous collections that can contain elements of different types. They are implemented as dynamic arrays.

**Key Concepts**:
- **Mutable**: Elements can be added, removed, or modified after creation
- **Ordered**: Elements maintain insertion order and are accessed by index (0-based)
- **Heterogeneous**: Can contain mixed types: `[1, "hello", 3.14, [1,2]]`
- **Dynamic**: Automatically resizes as elements are added/removed
- **Negative Indexing**: `-1` is last element, `-2` is second-to-last, etc.

**Code Examples**:
```python
# Creating lists
empty = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, [4, 5]]

# Indexing
numbers[0]   # 1 (first element)
numbers[-1]  # 5 (last element)
numbers[-2]  # 4 (second to last)

# Common operations
numbers.append(6)           # Add to end: [1,2,3,4,5,6]
numbers.insert(0, 0)        # Insert at index: [0,1,2,3,4,5,6]
numbers.extend([7, 8])      # Add multiple: [0,1,2,3,4,5,6,7,8]
numbers.pop()               # Remove and return last: 8
numbers.remove(0)           # Remove first occurrence of value
numbers.reverse()           # Reverse in-place
numbers.sort()              # Sort in-place

# List concatenation
a = [1, 2]
b = [3, 4]
c = a + b    # [1, 2, 3, 4] - creates new list

# Repetition
zeros = [0] * 5  # [0, 0, 0, 0, 0]

# Membership testing
2 in numbers  # True
10 in numbers # False

# Length
len(numbers)
```

**Common Pitfalls**:
- `append()` vs `extend()`: append adds the whole object, extend iterates and adds each element
- Modifying list while iterating: use list copy `for item in lst[:]:`
- List multiplication with mutable objects: `[[]] * 3` creates 3 references to SAME list

**When to Use Lists**:
- Need ordered collection with index access
- Need to modify elements frequently
- Don't need uniqueness constraint
- Order matters

### Tuples

**Definition**: Tuples are ordered, immutable, heterogeneous sequences. Once created, their elements cannot be changed, added, or removed.

**Key Concepts**:
- **Immutable**: Cannot modify after creation - no append, remove, etc.
- **Hashable**: Can be used as dictionary keys (if elements are hashable)
- **Memory Efficient**: Slightly more memory efficient than lists
- **Return Multiple Values**: Functions commonly return tuples
- **Unpacking**: Primary use case is unpacking values

**Code Examples**:
```python
# Creating tuples
empty = ()
single = (1,)  # Comma required for single element
coords = (10, 20)
mixed = (1, "two", 3.0)

# Tuple unpacking
x, y = (10, 20)
a, b, c = 1, 2, 3  # Parentheses optional

# Extended unpacking
first, *rest = (1, 2, 3, 4)
# first=1, rest=[2,3,4]

first, *middle, last = (1, 2, 3, 4, 5)
# first=1, middle=[2,3,4], last=5

# Named tuples (from collections module)
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)  # Access by name

# Tuple as dictionary key
locations = {
    (0, 0): "origin",
    (1, 0): "right",
    (0, 1): "up"
}
```

**When to Use Tuples Over Lists**:
- Data shouldn't change (coordinates, RGB colors, database records)
- Need to use as dictionary key
- Want to prevent accidental modification
- Returning multiple values from function
- Unpacking pattern matching

### Slicing

**Definition**: Slicing extracts a portion of a sequence using the syntax `sequence[start:stop:step]`. It creates a new object with the selected elements.

**Key Concepts**:
- **Syntax**: `[start:stop:step]` where start is inclusive, stop is exclusive
- **Defaults**: `start=0`, `stop=len(seq)`, `step=1`
- **Negative Indices**: Count from end of sequence
- **Creates Copy**: Slicing returns a new object (shallow copy for lists)
- **Works on**: strings, lists, tuples, and any sequence type

**Code Examples**:
```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing
nums[2:5]      # [2, 3, 4] - indices 2, 3, 4
nums[:5]       # [0, 1, 2, 3, 4] - first 5 elements
nums[5:]       # [5, 6, 7, 8, 9] - from index 5 to end
nums[:]        # [0, 1, 2, ..., 9] - full copy

# With step
nums[::2]      # [0, 2, 4, 6, 8] - every other element
nums[1::2]     # [1, 3, 5, 7, 9] - every other, starting at 1
nums[::3]      # [0, 3, 6, 9] - every third

# Negative indices
nums[-3:]      # [7, 8, 9] - last 3 elements
nums[:-3]      # [0, 1, 2, 3, 4, 5, 6] - all but last 3
nums[-5:-2]    # [5, 6, 7] - from 5th last to 2nd last

# Reversing
nums[::-1]     # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
nums[::-2]     # [9, 7, 5, 3, 1] - every other, reversed

# String slicing
text = "Python"
text[1:4]      # "yth"
text[::-1]     # "nohtyP" - reversed

# Slice assignment (lists only - not strings/tuples)
nums = [0, 1, 2, 3, 4]
nums[1:4] = [10, 20, 30]  # [0, 10, 20, 30, 4]
nums[1:3] = []             # Delete elements: [0, 30, 4]
```

**Common Pitfalls**:
- Slice creates a copy - modifying sliced list doesn't affect original
- `lst = lst[:]` creates shallow copy - nested lists still reference same objects
- Out-of-bounds slices don't raise errors, they just return what's available

---

## Strings

**Definition**: Strings are immutable sequences of Unicode characters. They are one of the most commonly used data types in Python.

**Key Concepts**:
- **Immutable**: Cannot modify individual characters; operations return new strings
- **Unicode**: Python 3 strings are Unicode by default (UTF-8 encoding)
- **Sequence**: Support indexing, slicing, iteration like lists
- **Methods**: Rich set of built-in methods for manipulation
- **Formatting**: Multiple ways to format strings (%, .format(), f-strings)

**Common Methods**:
```python
s = "  Hello World  "

# Case conversion
s.upper()       # "  HELLO WORLD  "
s.lower()       # "  hello world  "
s.title()       # "  Hello World  "
s.capitalize()  # "  hello world  " - only first char

# Whitespace
s.strip()       # "Hello World" - remove leading/trailing
s.lstrip()      # "Hello World  " - left only
s.rstrip()      # "  Hello World" - right only

# Splitting and joining
text = "apple,banana,cherry"
parts = text.split(",")  # ["apple", "banana", "cherry"]
rejoined = "-".join(parts)  # "apple-banana-cherry"

# Searching
s.find("World")    # 8 - index of first occurrence, -1 if not found
s.index("World")   # 8 - like find but raises ValueError if not found
s.startswith("  ") # True
s.endswith("  ")   # True
"World" in s       # True - membership test

# Replacing
s.replace(" ", "_")  # "__Hello_World__"

# Checking content
"123".isdigit()      # True
"abc".isalpha()      # True
"abc123".isalnum()   # True
"   ".isspace()      # True
```

**String Formatting**:
```python
name = "Alice"
age = 30

# f-strings (Python 3.6+) - PREFERRED
f"Hello, {name}! You are {age} years old."
f"{name.upper()} is {age * 12} months old"  # Can have expressions

# Format method
"Hello, {}! You are {} years old.".format(name, age)
"Hello, {n}! You are {a} years old.".format(n=name, a=age)

# Old % formatting (legacy)
"Hello, %s! You are %d years old." % (name, age)

# Number formatting
pi = 3.14159
f"{pi:.2f}"      # "3.14" - 2 decimal places
f"{1000:,}"      # "1,000" - thousands separator
f"{42:05d}"      # "00042" - zero padding
```

**Common Pitfalls**:
- Strings are immutable - `s[0] = 'h'` raises TypeError
- `str + int` raises TypeError - must convert: `str(num)` or `f"{num}"`
- `split()` without arguments splits on any whitespace and removes empty strings
- Encoding/decoding between bytes and strings can cause UnicodeErrors

---

## Control Flow

### Conditionals (if/elif/else)

**Definition**: Conditional statements execute different code blocks based on boolean expressions.

**Key Concepts**:
- **Truthiness**: All values have boolean interpretation
- **Short-Circuit Evaluation**: `and` and `or` stop evaluating once result is determined
- **Ternary Operator**: One-line if-else for simple cases
- **Chained Comparisons**: `a < b < c` is equivalent to `a < b and b < c`

**Code Examples**:
```python
# Basic if/elif/else
x = 10
if x > 15:
    print("High")
elif x > 5:
    print("Medium")
else:
    print("Low")

# Truthiness
if user_input:  # False for "", [], {}, None, 0
    process(user_input)

# Ternary operator
status = "adult" if age >= 18 else "minor"

# Chained comparisons
if 0 <= score <= 100:
    print("Valid score")

# Multiple conditions
if username and password and is_valid(username):
    login()

# Short-circuit evaluation
result = expensive_operation() or default_value
# expensive_operation() only called if needed
```

### Loops

**for Loops**:
```python
# Iterate over sequence
for item in [1, 2, 3]:
    print(item)

# with index using enumerate
for index, value in enumerate(['a', 'b', 'c']):
    print(f"{index}: {value}")
# 0: a, 1: b, 2: c

# Starting index from 1
for index, value in enumerate(['a', 'b', 'c'], start=1):
    print(f"{index}: {value}")
# 1: a, 2: b, 3: c

# Iterate over range
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2):  # 2, 4, 6, 8
    print(i)

# Iterating dictionaries
person = {"name": "Alice", "age": 30}

for key in person:  # Iterates keys by default
    print(key)

for key, value in person.items():
    print(f"{key}: {value}")

# Parallel iteration with zip
names = ["Alice", "Bob"]
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name} is {age}")
```

**while Loops**:
```python
# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1

# Infinite loop with break
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == 'quit':
        break
    process(user_input)

# While with condition
while queue:  # Continue while queue is not empty
    item = queue.pop(0)
    process(item)
```

**break, continue, else**:
```python
# break - exit loop entirely
for i in range(10):
    if i == 5:
        break  # Loop stops at 5
    print(i)  # Prints 0, 1, 2, 3, 4

# continue - skip to next iteration
for i in range(5):
    if i == 2:
        continue  # Skip printing 2
    print(i)  # Prints 0, 1, 3, 4

# else clause - executes if loop completes without break
for i in range(5):
    if i == 10:
        break
else:
    print("Loop completed normally")  # This prints

# Practical example: search with else
for item in items:
    if item.id == search_id:
        found = item
        break
else:
    print("Item not found")
```

---

## Dictionaries

**Definition**: Dictionaries are mutable, unordered collections of key-value pairs. They are implemented as hash tables, providing O(1) average-case lookup time.

**Key Concepts**:
- **Hash Table**: Keys must be hashable (immutable types like int, str, tuple)
- **Unordered**: Python 3.7+ maintains insertion order, but don't rely on it for logic
- **Mutable**: Can add, remove, modify key-value pairs
- **Key Uniqueness**: Each key can appear only once; duplicate keys overwrite

**Code Examples**:
```python
# Creating dictionaries
empty = {}
person = {"name": "Alice", "age": 30, "city": "NYC"}

# Alternative creation
person = dict(name="Alice", age=30, city="NYC")

# From list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
d = dict(pairs)

# Accessing values
person["name"]  # "Alice" - KeyError if key doesn't exist

# Safe access with get
person.get("name")          # "Alice"
person.get("country", "USA")  # "USA" - default if key missing

# Adding/updating
person["country"] = "USA"  # Add new key
person["age"] = 31         # Update existing

# Removing
del person["city"]         # Remove key, KeyError if doesn't exist
age = person.pop("age")    # Remove and return value
person.clear()             # Remove all items

# Checking membership
"name" in person  # True - checks keys only
"Alice" in person.values()  # True - checks values

# Dictionary methods
keys = list(person.keys())      # ["name", "age", "city"]
values = list(person.values())  # ["Alice", 30, "NYC"]
items = list(person.items())    # [("name", "Alice"), ...]

# Merging dictionaries (Python 3.9+)
defaults = {"theme": "dark", "lang": "en"}
user_prefs = {"theme": "light"}
settings = defaults | user_prefs  # {"theme": "light", "lang": "en"}

# Update method
defaults.update(user_prefs)  # Modifies defaults in-place

# setdefault - get or set if missing
count = counts.setdefault(key, 0)
counts[key] += 1
```

**Iteration Patterns**:
```python
person = {"name": "Alice", "age": 30}

# Iterate keys (default)
for key in person:
    print(key, person[key])

# Iterate keys explicitly
for key in person.keys():
    print(key)

# Iterate values
for value in person.values():
    print(value)

# Iterate key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")
```

**Common Pitfalls**:
- Accessing missing key raises KeyError - use `.get()` for safe access
- Modifying dictionary during iteration can raise RuntimeError
- Keys must be hashable - cannot use list or dict as key

**When to Use Dictionaries**:
- Need fast lookup by key
- Associating values with unique keys
- Counting occurrences (Counter is specialized dict)
- Caching/memoization
- Configuration settings

---

## Sets

**Definition**: Sets are unordered collections of unique elements. They are implemented as hash tables and support mathematical set operations.

**Key Concepts**:
- **Uniqueness**: Automatically removes duplicates
- **Unordered**: No indexing or slicing
- **Mutable**: Can add/remove elements (frozenset is immutable version)
- **Hashable Elements**: Like dict keys, elements must be hashable
- **Fast Membership**: O(1) average-case for `in` operator

**Code Examples**:
```python
# Creating sets
empty = set()  # Note: {} creates empty dict, not set
numbers = {1, 2, 3, 4, 5}
mixed = {1, "two", 3.0}

# From list (removes duplicates)
unique = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3}

# Adding/removing
numbers.add(6)           # Add single element
numbers.update([7, 8])   # Add multiple
numbers.remove(1)        # Remove, KeyError if not present
numbers.discard(1)       # Remove, no error if not present
numbers.pop()            # Remove and return arbitrary element
numbers.clear()          # Remove all

# Membership testing (very fast)
5 in numbers  # True

# Set operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union - all elements from both
A | B                # {1, 2, 3, 4, 5, 6}
A.union(B)

# Intersection - common elements
A & B                # {3, 4}
A.intersection(B)

# Difference - in A but not in B
A - B                # {1, 2}
A.difference(B)

# Symmetric difference - in A or B but not both
A ^ B                # {1, 2, 5, 6}
A.symmetric_difference(B)

# Subset/superset
{1, 2}.issubset({1, 2, 3})     # True
{1, 2, 3}.issuperset({1, 2})   # True

# Disjoint - no common elements
{1, 2}.isdisjoint({3, 4})      # True
```

**Common Use Cases**:
```python
# Remove duplicates from list
unique_items = list(set(items))

# Fast membership testing
valid_users = {" user1", "user2", "user3"}
if username in valid_users:  # Much faster than list
    grant_access()

# Finding unique elements across collections
all_tags = set()
for article in articles:
    all_tags.update(article.tags)

# Set comprehensions
evens = {x for x in range(10) if x % 2 == 0}
```

**Common Pitfalls**:
- Sets are unordered - cannot rely on iteration order
- Elements must be hashable - cannot add lists or dicts to sets
- `{}` creates dict, not set - use `set()` for empty set

---

## Comprehensions

**Definition**: Comprehensions provide a concise way to create lists, dictionaries, and sets using a single line of code. They are often more readable and faster than equivalent for loops.

**List Comprehensions**:
```python
# Basic syntax: [expression for item in iterable]
squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With condition: [expression for item in iterable if condition]
evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

# With transformation
names = ["alice", "bob", "charlie"]
capitalized = [name.capitalize() for name in names]
# ["Alice", "Bob", "Charlie"]

# Nested comprehensions
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# With multiple conditions
filtered = [x for x in range(20) if x % 2 == 0 if x % 3 == 0]
# [0, 6, 12, 18]

# Conditional expression in output
signs = ["positive" if x > 0 else "negative" for x in [-1, 2, -3]]
# ["negative", "positive", "negative"]
```

**Dictionary Comprehensions**:
```python
# Basic syntax: {key_expr: value_expr for item in iterable}
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# From two lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}
# {"a": 1, "b": 2, "c": 3}

# With condition
filtered = {k: v for k, v in original.items() if v > 10}

# Swapping keys and values
inverted = {v: k for k, v in original.items()}

# Count word lengths
words = ["apple", "banana", "cherry"]
lengths = {word: len(word) for word in words}
# {"apple": 5, "banana": 6, "cherry": 6}
```

**Set Comprehensions**:
```python
# Basic syntax: {expression for item in iterable}
unique_lengths = {len(word) for word in ["a", "ab", "abc", "ab"]}
# {1, 2, 3}

# With condition
evens_set = {x for x in range(10) if x % 2 == 0}
# {0, 2, 4, 6, 8}
```

**When to Use Comprehensions**:
- ✓ Creating new collections from existing ones
- ✓ Simple filtering and transformation
- ✓ Mapping operations
- ✗ Complex multi-step logic (use regular loops)
- ✗ Side effects (printing, file I/O) - use regular loops

**Performance**:
Comprehensions are typically faster than equivalent for loops because they're optimized at the bytecode level.

---

## Functions

### Basic Functions

**Definition**: Functions are reusable blocks of code that perform a specific task. They are defined using the `def` keyword and can accept parameters and return values.

**Key Concepts**:
- **First-Class Objects**: Functions can be passed as arguments, returned from other functions, assigned to variables
- **Default Return**: Functions return `None` if no explicit return statement
- **Scope**: Variables defined inside function are local; use LEGB rule (Local, Enclosing, Global, Built-in)

**Code Examples**:
```python
# Basic function
def greet(name):
    return f"Hello, {name}!"

result = greet("Alice")  # "Hello, Alice!"

# Multiple return values (returns tuple)
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

min_val, max_val, avg = get_stats([1, 2, 3, 4, 5])

# No return statement returns None
def print_message(msg):
    print(msg)
    # implicit: return None

result = print_message("Hi")  # result is None
```

### Function Parameters

**Definition**: Python supports multiple parameter types that control how arguments are passed to functions.

**Parameter Types in Order**:
1. Positional parameters
2. Default parameters
3. `*args` (variable positional)
4. Keyword-only parameters
5. `**kwargs` (variable keyword)

**Complete Example**:
```python
def function(a, b, c=10, *args, d, e=20, **kwargs):
    print(f"a={a}, b={b}, c={c}")
    print(f"args={args}")
    print(f"d={d}, e={e}")
    print(f"kwargs={kwargs}")

# Calling:
function(1, 2, 3, 4, 5, d=100, e=200, x=1000, y=2000)
# Output:
# a=1, b=2, c=3
# args=(4, 5)
# d=100, e=200
# kwargs={'x': 1000, 'y': 2000}
```

**Positional and Default Parameters**:
```python
def power(base, exponent=2):
    return base ** exponent

power(5)      # 25 (uses default exponent=2)
power(5, 3)   # 125 (overrides default)
power(exponent=3, base=5)  # 125 (keyword arguments)
```

***args (Variable Positional Arguments)**:
```python
def sum_all(*numbers):
    return sum(numbers)

sum_all(1, 2, 3)        # 6
sum_all(1, 2, 3, 4, 5)  # 15

# Can combine with regular params
def format_output(sep, *values):
    return sep.join(str(v) for v in values)

format_output(", ", 1, 2, 3)  # "1, 2, 3"
```

**Keyword-Only Arguments** (after `*` or `*args`):
```python
# Everything after * must be passed by name
def create_user(name, *, email, age):
    return {"name": name, "email": email, "age": age}

# Must call with keywords for email and age
user = create_user("Alice", email="alice@example.com", age=30)

# This raises TypeError:
# user = create_user("Alice", "alice@example.com", 30)
```

****kwargs (Variable Keyword Arguments)**:
```python
def print_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="NYC")
# Output:
# name: Alice
# age: 30
# city: NYC

# Common pattern: passing options
def configure_server(host, port, **options):
    config = {"host": host, "port": port}
    config.update(options)
    return config

configure_server("localhost", 8000, debug=True, workers=4)
```

**Unpacking Arguments**:
```python
# Unpack list/tuple as positional args with *
def add(a, b, c):
    return a + b + c

values = [1, 2, 3]
result = add(*values)  # Unpacks to add(1, 2, 3)

# Unpack dictionary as keyword args with **
def greet(first, last):
    return f"Hello {first} {last}"

person = {"first": "Alice", "last": "Smith"}
result = greet(**person)  # Unpacks to greet(first="Alice", last="Smith")
```

**Common Pitfalls**:
- **Mutable default arguments**: They're created once and shared across all calls
```python
def add_item(item, lst=[]):  # DON'T DO THIS
    lst.append(item)
    return lst

add_item(1)  # [1]
add_item(2)  # [1, 2] - UNEXPECTED!

# Correct approach:
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

### Lambda Functions

**Definition**: Anonymous functions defined with `lambda` keyword. Limited to single expression.

**Syntax**: `lambda arguments: expression`

**Code Examples**:
```python
# Basic lambda
add = lambda x, y: x + y
add(2, 3)  # 5

# Used with higher-order functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Sorting with key
students = [("Alice", 85), ("Bob", 75), ("Charlie", 90)]
sorted_students = sorted(students, key=lambda x: x[1])
# Sorted by score

# Multiple arguments
multiply = lambda x, y, z: x * y * z
multiply(2, 3, 4)  # 24
```

**When to Use Lambdas**:
- ✓ Short, simple operations
- ✓ One-time use functions (callbacks, sorting keys)
- ✗ Complex logic (use def instead)
- ✗ Multiple statements (lambda limited to single expression)

---

## Iterables and Iterators

**Definition**: An iterable is any object that can be looped over (lists, tuples, strings, dicts, files). An iterator is an object that returns data one element at a time using `__next__()`.

**Key Concepts**:
- **Iterable**: Has `__iter__()` method that returns an iterator
- **Iterator**: Has `__next__()` method that returns next item
- **StopIteration**: Exception raised when iterator is exhausted
- **Lazy Evaluation**: Iterators compute values on-demand, saving memory

**Code Examples**:
```python
# Lists are iterables, not iterators
numbers = [1, 2, 3]

# Get iterator from iterable
iter_numbers = iter(numbers)

# Manually iterate
print(next(iter_numbers))  # 1
print(next(iter_numbers))  # 2
print(next(iter_numbers))  # 3
print(next(iter_numbers))  # StopIteration exception

# for loop does this automatically:
for num in numbers:
    print(num)
# Equivalent to:
# iter_numbers = iter(numbers)
# while True:
#     try:
#         num = next(iter_numbers)
#         print(num)
#     except StopIteration:
#         break

# Built-in iterators
r = range(5)  # Iterator, not list
# Doesn't create list in memory

# file objects are iterators
with open("file.txt") as f:
    for line in f:  # Reads one line at a time
        print(line)
```

### Generators

**Definition**: Generators are functions that use `yield` to produce a sequence of values lazily. They are memory-efficient iterators.

**Key Concepts**:
- **Lazy Evaluation**: Values generated on-demand, not all at once
- **State Preservation**: Function state preserved between yields
- **Memory Efficient**: Doesn't store entire sequence in memory
- **One-Time Use**: Once exhausted, must recreate to iterate again

**Code Examples**:
```python
# Generator function
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Create generator
gen = countdown(5)

# Iterate
for num in gen:
    print(num)  # 5, 4, 3, 2, 1

# Manual iteration
gen = countdown(3)
print(next(gen))  # 3
print(next(gen))  # 2
print(next(gen))  # 1
print(next(gen))  # StopIteration

# Generator expression (like list comprehension but lazy)
squares = (x**2 for x in range(10))  # Note: () not []
print(type(squares))  # <class 'generator'>

# Use as needed
for sq in squares:
    print(sq)

# Common use: large data processing
def read_large_file(file_path):
    with open(file_path) as f:
        for line in f:
            yield line.strip()

# Only one line in memory at a time
for line in read_large_file("huge_file.txt"):
    process(line)

# Infinite generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Take first 10
fib = fibonacci()
first_10 = [next(fib) for _ in range(10)]
```

**When to Use Generators**:
- ✓ Processing large datasets
- ✓ Infinite sequences
- ✓ Pipeline processing
- ✓ When you don't need entire sequence at once

---

## Exception Handling

**Definition**: Exceptions are events that disrupt normal program flow. Exception handling allows graceful error recovery instead of crashes.

**Key Concepts**:
- **try/except**: Catch and handle exceptions
- **else**: Runs if no exception occurred
- **finally**: Always runs, even if exception occurs
- **raise**: Manually raise exceptions
- **Exception Hierarchy**: All exceptions inherit from BaseException

**Code Examples**:
```python
# Basic try/except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
    result = None

# Multiple except clauses
try:
    value = int(user_input)
    result = 100 / value
except ValueError:
    print("Invalid number format")
except ZeroDivisionError:
    print("Cannot divide by zero")

# Catch multiple exception types
try:
    risky_operation()
except (ValueError, TypeError) as e:
    print(f"Error: {e}")

# Catch all exceptions (use sparingly)
try:
    risky_operation()
except Exception as e:
    log_error(e)
    raise  # Re-raise the exception

# try/except/else/finally
try:
    file = open("data.txt")
    data = file.read()
except FileNotFoundError:
    print("File not found")
else:
    # Runs only if no exception
    print("File read successfully")
finally:
    # Always runs
    if 'file' in locals():
        file.close()

# Raising exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return age

# Custom exceptions
class InsufficientFundsError(Exception):
    pass

def withdraw(amount):
    if amount > balance:
        raise InsufficientFundsError(f"Cannot withdraw {amount}")
    balance -= amount
```

**Common Exception Types**:
- `ValueError`: Invalid value (e.g., `int("abc")`)
- `TypeError`: Wrong type (e.g., `"text" + 5`)
- `KeyError`: Missing dictionary key
- `IndexError`: Invalid list index
- `FileNotFoundError`: File doesn't exist
- `AttributeError`: Invalid attribute access
- `ZeroDivisionError`: Division by zero
- `ImportError`: Failed import

**Best Practices**:
- Be specific - catch specific exceptions, not bare `except:`
- Don't silence exceptions - log or handle appropriately
- Use `finally` for cleanup (closing files, connections)
- Raise exceptions for exceptional conditions, not normal flow

---

## Higher Order Functions

**Definition**: Functions that take other functions as arguments or return functions. They enable functional programming patterns.

**map()**:
```python
# Syntax: map(function, iterable)
# Applies function to each element

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
# [1, 4, 9, 16, 25]

# With multiple iterables
a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))
# [11, 22, 33]

# With named function
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

temps_f = [32, 68, 100]
temps_c = list(map(fahrenheit_to_celsius, temps_f))
```

**filter()**:
```python
# Syntax: filter(function, iterable)
# Keeps elements where function returns True

numbers = range(10)
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [0, 2, 4, 6, 8]

# Filter None values
values = [1, None, 2, None, 3]
filtered = list(filter(None, values))  # [1, 2, 3]

# With named function
def is_positive(n):
    return n > 0

nums = [-2, -1, 0, 1, 2]
positives = list(filter(is_positive, nums))
```

**sorted()** with key:
```python
# Sort by custom criteria
students = [
    ("Alice", 85),
    ("Bob", 75),
    ("Charlie", 90)
]

# Sort by score (second element)
by_score = sorted(students, key=lambda x: x[1])

# Sort by name length
words = ["apple", "pie", "zoo", "elephant"]
by_length = sorted(words, key=len)

# Sort dictionaries
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25}
]
by_age = sorted(people, key=lambda p: p["age"])

# Reverse order
descending = sorted(numbers, reverse=True)
```

**reduce()** (from functools):
```python
from functools import reduce

# Syntax: reduce(function, iterable, initial_value)
# Applies function cumulatively

numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)  # 15
# Equivalent to: ((((1+2)+3)+4)+5)

# With initial value
product = reduce(lambda x, y: x * y, numbers, 1)  # 120

# Practical example: flatten list of lists
lists = [[1, 2], [3, 4], [5, 6]]
flattened = reduce(lambda x, y: x + y, lists)  # [1,2,3,4,5,6]
```

---

## Decorators

**Definition**: Decorators are functions that modify the behavior of other functions without changing their code. They use the `@decorator` syntax.

**Key Concepts**:
- **Wrapper Pattern**: Decorator returns wrapper function that calls original
- **@ Syntax**: Syntactic sugar for `func = decorator(func)`
- **functools.wraps**: Preserves original function metadata
- **Chaining**: Multiple decorators can be applied

**Basic Pattern**:
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        # Do something before
        result = func(*args, **kwargs)
        # Do something after
        return result
    return wrapper

# Using decorator
@my_decorator
def my_function():
    pass

# Equivalent to:
# my_function = my_decorator(my_function)
```

**Practical Examples**:
```python
# Logging decorator
def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

add(2, 3)
# Output:
# Calling add
# add returned 5

# Timing decorator
import time
from functools import wraps

def timer(func):
    @wraps(func)  # Preserves func metadata
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"

# Decorator with arguments
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}")

greet("Alice")
# Prints "Hello, Alice" 3 times
```

**functools.lru_cache**:
```python
from functools import lru_cache

# Memoization decorator - caches results
@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# First call computes, subsequent calls use cache
fibonacci(100)  # Fast due to caching
```

**Multiple Decorators**:
```python
@decorator1
@decorator2
@decorator3
def func():
    pass

# Equivalent to:
# func = decorator1(decorator2(decorator3(func)))
# Applied bottom-to-top
```

---

## File I/O

**Definition**: Reading from and writing to files. Python provides built-in functions for file operations.

**Key Concepts**:
- **Context Manager**: `with` statement ensures file is properly closed
- **File Modes**: 'r' (read), 'w' (write), 'a' (append), 'r+' (read/write)
- **Text vs Binary**: Default is text mode; add 'b' for binary
- **Encoding**: Specify encoding with `encoding='utf-8'`

**Reading Files**:
```python
# Read entire file
with open("file.txt", "r") as f:
    content = f.read()  # Returns string

# Read lines into list
with open("file.txt") as f:
    lines = f.readlines()  # Returns list of strings

# Read line by line (memory efficient)
with open("file.txt") as f:
    for line in f:
        print(line.strip())

# Read first N characters
with open("file.txt") as f:
    chunk = f.read(100)  # Read 100 characters
```

**Writing Files**:
```python
# Write (overwrites existing)
with open("output.txt", "w") as f:
    f.write("Hello World\n")
    f.write("Second line\n")

# Write lines
lines = ["line 1\n", "line 2\n", "line 3\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)

# Append (adds to end)
with open("log.txt", "a") as f:
    f.write("New log entry\n")
```

**File Paths**:
```python
from pathlib import Path

# Modern way using Path
file = Path("data.txt")
content = file.read_text()
file.write_text("new content")

# Check if exists
if file.exists():
    print("File exists")

# Get file info
print(file.stat().st_size)  # File size
```

---

## Object-Oriented Programming

### Classes and Objects

**Definition**: Classes are blueprints for creating objects. Objects are instances of classes with their own data (attributes) and behavior (methods).

**Basic Class**:
```python
class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} says Woof!"
    
    def __str__(self):
        return f"Dog(name={self.name}, age={self.age})"

# Creating instances
buddy = Dog("Buddy", 5)
miles = Dog("Miles", 3)

# Access attributes
print(buddy.name)  # "Buddy"
print(Dog.species)  # "Canis familiaris"

# Call methods
print(buddy.bark())  # "Buddy says Woof!"
print(str(buddy))    # "Dog(name=Buddy, age=5)"
```

**Magic Methods (Dunder Methods)**:
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        # String representation for users
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        # String representation for developers
        return f"Vector(x={self.x}, y={self.y})"
    
    def __add__(self, other):
        # Overload + operator
        return Vector(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        # Overload == operator
        return self.x == other.x and self.y == other.y
    
    def __len__(self):
        # Define length
        return int((self.x**2 + self.y**2)**0.5)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2  # Uses __add__
print(v3)     # Uses __str__
```

**Properties**:
```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9

temp = Temperature(25)
print(temp.celsius)     # 25
print(temp.fahrenheit)  # 77.0
temp.fahrenheit = 32
print(temp.celsius)     # 0.0
```

**Inheritance**:
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Polymorphism
animals = [Dog("Buddy"), Cat("Whiskers")]
for animal in animals:
    print(animal.speak())
```

---

## Standard Library

### datetime Module

```python
from datetime import datetime, timedelta, date, time

# Current date and time
now = datetime.now()
today = date.today()

# Creating specific datetime
dt = datetime(2024, 12, 31, 23, 59, 59)

# Date arithmetic
tomorrow = today + timedelta(days=1)
next_week = now + timedelta(weeks=1)
two_hours_ago = now - timedelta(hours=2)

# Formatting
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
# "2025-01-01 14:30:00"

# Parsing
dt = datetime.strptime("2024-12-31", "%Y-%m-%d")

# Components
print(now.year, now.month, now.day)
print(now.hour, now.minute, now.second)
```

### collections Module

```python
from collections import Counter, defaultdict, deque

# Counter - count hashable objects
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = Counter(words)
# Counter({'apple': 3, 'banana': 2, 'cherry': 1})
most_common = counts.most_common(2)  # [('apple', 3), ('banana', 2)]

# defaultdict - dictionary with default value
dd = defaultdict(list)
dd['key'].append(1)  # No KeyError, creates empty list

dd = defaultdict(int)
for word in words:
    dd[word] += 1  # No need to check if key exists

# deque - double-ended queue
dq = deque([1, 2, 3])
dq.append(4)       # Add to right
dq.appendleft(0)   # Add to left
dq.pop()           # Remove from right
dq.popleft()       # Remove from left
```

### CSV Module

```python
import csv

# Reading CSV
with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['name'], row['age'])

# Writing CSV
data = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25}
]
with open('output.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'age'])
    writer.writeheader()
    writer.writerows(data)
```

### JSON Module

```python
import json

# Python to JSON
data = {"name": "Alice", "age": 30, "city": "NYC"}
json_string = json.dumps(data)  # Serialize to string
json.dump(data, open('data.json', 'w'))  # Write to file

# JSON to Python
data = json.loads(json_string)  # Deserialize from string
data = json.load(open('data.json'))  # Read from file
```

---

## Data Science Libraries

### NumPy Basics

```python
import numpy as np

# Creating arrays
arr = np.array([1, 2, 3, 4, 5])
zeros = np.zeros((3, 4))  # 3x4 array of zeros
ones = np.ones((2, 3))
range_arr = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
linspace = np.linspace(0, 1, 5)  # 5 evenly spaced values

# Array operations (vectorized)
arr * 2      # Multiply all elements
arr + arr    # Element-wise addition
arr ** 2     # Square all elements

# Indexing and slicing
arr[0]       # First element
arr[1:4]     # Elements 1, 2, 3
arr[arr > 2] # Boolean indexing

# Useful operations
arr.mean()
arr.std()
arr.sum()
arr.min()
arr.max()
```

### Pandas Basics

```python
import pandas as pd

# Creating DataFrame
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['NYC', 'LA', 'Chicago']
})

# Reading from CSV
df = pd.read_csv('data.csv')

# Selecting data
df['name']              # Select column
df[['name', 'age']]     # Select multiple columns
df.loc[0]               # Select row by label
df.iloc[0]              # Select row by position

# Filtering
df[df['age'] > 25]
df[df['city'] == 'NYC']

# Operations
df['age'].mean()
df.groupby('city')['age'].mean()
df.sort_values('age')

# Writing to CSV
df.to_csv('output.csv', index=False)
```

### Matplotlib Basics

```python
import matplotlib.pyplot as plt

# Line plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('My Plot')
plt.show()

# Multiple plots
plt.plot(x, y, label='Line 1')
plt.plot(x, [i**2 for i in x], label='Line 2')
plt.legend()
plt.show()

# Scatter plot
plt.scatter(x, y)
plt.show()

# Bar chart
categories = ['A', 'B', 'C']
values = [10, 25, 15]
plt.bar(categories, values)
plt.show()
```

---

## Interview Tips

### Time Complexity

Know Big O notation for common operations:

**Lists**:
- Access by index: O(1)
- Append: O(1) amortized
- Insert/Delete at beginning: O(n)
- Search: O(n)

**Dictionaries/Sets**:
- Access/Insert/Delete: O(1) average
- Search: O(1) average

**Sorting**:
- sorted(): O(n log n)

### Common Patterns

**Two Pointer**:
```python
def reverse_string(s):
    left, right = 0, len(s) - 1
    s = list(s)
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return ''.join(s)
```

**Sliding Window**:
```python
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    return max_sum
```

**Frequency Counter**:
```python
from collections import Counter
def anagram(s1, s2):
    return Counter(s1) == Counter(s2)
```

This guide covers the essential Python concepts for technical interviews. Practice implementing these patterns and understanding the underlying concepts!
