# Python Terminology Reference

A comprehensive guide to Python programming terms and concepts.

---

## Core Concepts

### Syntax
The set of rules that define how Python code must be written. Syntax determines the structure and order of statements.

```python
# Correct syntax
if x > 5:
    print("Greater")

# Incorrect syntax (missing colon)
if x > 5
    print("Greater")
```

### Literal
A direct representation of a fixed value in code. You write the value literally as it appears.

**Examples:**
- Integer literal: `42`
- Float literal: `3.14`
- String literal: `"Hello"`
- Boolean literal: `True`, `False`
- List literal: `[1, 2, 3]`
- Dictionary literal: `{'key': 'value'}`
- Set literal: `{1, 2, 3}`
- Tuple literal: `(1, 2, 3)`

### Expression
A combination of values, variables, operators, and function calls that Python evaluates to produce a value.

```python
x + 5              # Expression
len("hello")       # Expression
x > 10 and y < 20  # Expression
```

### Statement
A complete line of code that performs an action. Statements don't return values.

```python
x = 5              # Assignment statement
print("Hi")        # Function call statement
if x > 5:          # Conditional statement
import math        # Import statement
```

### Variable
A named location in memory that stores a value. Variables act as containers for data.

```python
name = "Alice"     # 'name' is a variable
age = 25           # 'age' is a variable
```

### Identifier
A name used to identify a variable, function, class, module, or other object.

**Rules:**
- Must start with letter (a-z, A-Z) or underscore (_)
- Can contain letters, digits (0-9), and underscores
- Case-sensitive
- Cannot be a Python keyword

```python
my_variable        # Valid identifier
_private_var       # Valid identifier
variable123        # Valid identifier
123variable        # Invalid (starts with digit)
```

---

## Punctuation & Operators

### Parentheses `()`
Used for:
- Function calls: `print("Hello")`
- Grouping expressions: `(x + 5) * 2`
- Tuples: `(1, 2, 3)`
- Function definitions: `def func(param):`

### Square Brackets `[]`
Used for:
- Lists: `[1, 2, 3]`
- Indexing: `my_list[0]`
- Slicing: `my_list[1:5]`
- List comprehensions: `[x*2 for x in range(5)]`

### Curly Braces `{}`
Used for:
- Dictionaries: `{'key': 'value'}`
- Sets: `{1, 2, 3}`
- Dictionary comprehensions: `{k: v for k, v in items}`
- Set comprehensions: `{x*2 for x in range(5)}`
- f-string formatting: `f"Hello {name}"`

### Colon `:`
Used for:
- Starting code blocks: `if x > 5:`
- Dictionary key-value separator: `{'name': 'Alice'}`
- Slicing: `my_list[1:5]`
- Function annotations: `def func(x: int) -> str:`

### Comma `,`
Used for:
- Separating items in sequences: `[1, 2, 3]`
- Separating function parameters: `print(x, y, z)`
- Multiple assignments: `x, y = 1, 2`

### Semicolon `;`
Used to separate multiple statements on one line (rarely used):
```python
x = 5; y = 10; print(x + y)
```

### Dot `.`
Used for:
- Accessing attributes/methods: `string.upper()`
- Module imports: `import math.pi`
- Decimal numbers: `3.14`

### Underscore `_`
Used for:
- Variable names: `my_variable`
- Private variables: `_private`
- Unused variables: `for _ in range(5):`
- Number separators: `1_000_000`
- Last result in interactive shell

---

## Operators

### Arithmetic Operators
- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division
- `//` Floor division (integer division)
- `%` Modulo (remainder)
- `**` Exponentiation (power)

### Comparison Operators
- `==` Equal to
- `!=` Not equal to
- `>` Greater than
- `<` Less than
- `>=` Greater than or equal to
- `<=` Less than or equal to

### Logical Operators
- `and` Logical AND
- `or` Logical OR
- `not` Logical NOT

### Assignment Operators
- `=` Assignment
- `+=` Add and assign
- `-=` Subtract and assign
- `*=` Multiply and assign
- `/=` Divide and assign
- `//=` Floor divide and assign
- `%=` Modulo and assign
- `**=` Exponent and assign

### Membership Operators
- `in` Check if value exists in sequence
- `not in` Check if value doesn't exist in sequence

### Identity Operators
- `is` Check if objects are the same
- `is not` Check if objects are different

### Bitwise Operators
- `&` Bitwise AND
- `|` Bitwise OR
- `^` Bitwise XOR
- `~` Bitwise NOT
- `<<` Left shift
- `>>` Right shift

---

## Data Types

### Immutable Types
Cannot be changed after creation:
- **int**: Integer numbers (`42`)
- **float**: Decimal numbers (`3.14`)
- **str**: Text strings (`"Hello"`)
- **tuple**: Ordered collection (`(1, 2, 3)`)
- **frozenset**: Immutable set (`frozenset({1, 2, 3})`)
- **bool**: Boolean values (`True`, `False`)
- **NoneType**: None value (`None`)

### Mutable Types
Can be changed after creation:
- **list**: Ordered collection (`[1, 2, 3]`)
- **dict**: Key-value pairs (`{'key': 'value'}`)
- **set**: Unordered unique values (`{1, 2, 3}`)
- **bytearray**: Mutable bytes

### Sequence Types
Collections with ordered elements:
- **list**: `[1, 2, 3]`
- **tuple**: `(1, 2, 3)`
- **str**: `"Hello"`
- **range**: `range(10)`

### Collection Types
- **list**: Ordered, mutable
- **tuple**: Ordered, immutable
- **set**: Unordered, unique, mutable
- **dict**: Key-value mapping, mutable
- **frozenset**: Unordered, unique, immutable

---

## Functions & Callables

### Function
A reusable block of code that performs a specific task.

```python
def greet(name):
    return f"Hello, {name}"
```

### Parameter
A variable in a function definition that receives a value when the function is called.

```python
def add(x, y):  # x and y are parameters
    return x + y
```

### Argument
The actual value passed to a function when calling it.

```python
result = add(5, 3)  # 5 and 3 are arguments
```

### Return Value
The value that a function sends back to the caller using `return`.

```python
def square(x):
    return x * x  # x * x is the return value
```

### Lambda Function
An anonymous, single-expression function.

```python
square = lambda x: x * x
```

### Method
A function that belongs to an object/class.

```python
text = "hello"
text.upper()  # upper() is a method of string objects
```

### Built-in Function
Functions provided by Python without importing: `print()`, `len()`, `range()`, `type()`, etc.

---

## Control Flow

### Conditional Statement
Code that executes based on a condition.

```python
if x > 5:
    print("Greater")
elif x == 5:
    print("Equal")
else:
    print("Less")
```

### Loop
Code that repeats multiple times.

**For Loop:** Iterate over a sequence
```python
for item in [1, 2, 3]:
    print(item)
```

**While Loop:** Repeat while condition is true
```python
while x < 10:
    x += 1
```

### Iterator
An object that can be iterated over (used in loops).

```python
my_list = [1, 2, 3]
iterator = iter(my_list)
```

### Iterable
An object that can return an iterator. Lists, tuples, strings, dicts, sets are all iterables.

### Break
Exit a loop prematurely.

```python
for i in range(10):
    if i == 5:
        break  # Exit loop when i is 5
```

### Continue
Skip the rest of the current iteration and move to the next.

```python
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)
```

### Pass
A null statement; does nothing. Used as a placeholder.

```python
def future_function():
    pass  # TODO: implement this later
```

---

## Object-Oriented Programming

### Class
A blueprint for creating objects. Defines attributes and methods.

```python
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        return "Woof!"
```

### Object (Instance)
A specific realization of a class.

```python
my_dog = Dog("Buddy")  # my_dog is an object/instance
```

### Attribute
A variable that belongs to an object or class.

```python
my_dog.name  # 'name' is an attribute
```

### Method
A function that belongs to a class.

```python
my_dog.bark()  # bark() is a method
```

### Constructor
The `__init__` method that initializes a new object.

### Self
A reference to the current instance of a class.

### Inheritance
When a class derives properties and methods from another class.

```python
class Puppy(Dog):  # Puppy inherits from Dog
    pass
```

---

## Exception Handling

### Exception
An error that occurs during program execution.

### Try-Except Block
Code to handle exceptions gracefully.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

### Raise
Manually trigger an exception.

```python
raise ValueError("Invalid input")
```

### Finally
Code that always executes, regardless of exceptions.

```python
try:
    file = open("data.txt")
except FileNotFoundError:
    print("File not found")
finally:
    print("This always runs")
```

---

## Modules & Packages

### Module
A Python file containing definitions and statements. Can be imported.

```python
import math
```

### Package
A collection of modules in a directory with an `__init__.py` file.

### Import
Load a module or specific functions into your script.

```python
import math
from math import sqrt
from math import *
import math as m
```

### Namespace
A container that holds identifiers (variable names, function names, etc.) and prevents naming conflicts.

---

## Comprehensions

### List Comprehension
Create a list using a compact syntax.

```python
squares = [x**2 for x in range(10)]
```

### Dictionary Comprehension
Create a dictionary using compact syntax.

```python
square_dict = {x: x**2 for x in range(5)}
```

### Set Comprehension
Create a set using compact syntax.

```python
unique_squares = {x**2 for x in range(-5, 5)}
```

### Generator Expression
Like list comprehension but creates a generator (lazy evaluation).

```python
squares_gen = (x**2 for x in range(10))
```

---

## Special Concepts

### Scope
The region where a variable is accessible.
- **Local scope**: Inside a function
- **Enclosing scope**: In enclosing functions
- **Global scope**: At the module level
- **Built-in scope**: Python built-in names

### Keyword
Reserved words with special meaning in Python. Cannot be used as identifiers.

Examples: `if`, `else`, `for`, `while`, `def`, `class`, `import`, `return`, `try`, `except`, `with`, `as`, `from`, `True`, `False`, `None`, etc.

### Indentation
Whitespace at the beginning of a line. Python uses indentation to define code blocks.

```python
if True:
    print("Indented")  # 4 spaces of indentation
```

### Comment
Text in code that Python ignores. Used for documentation.

```python
# This is a single-line comment

"""
This is a multi-line comment
or docstring
"""
```

### Docstring
A string literal that documents a module, function, class, or method.

```python
def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}"
```

### Slice
A portion of a sequence extracted using indexing.

```python
my_list = [0, 1, 2, 3, 4, 5]
my_list[1:4]  # [1, 2, 3]
```

### Index
The position of an element in a sequence (starts at 0).

```python
my_list[0]  # First element
my_list[-1]  # Last element
```

### Unpacking
Assigning elements from a sequence to multiple variables.

```python
x, y, z = [1, 2, 3]
```

### Type Annotation
Optional syntax to specify expected types.

```python
def add(x: int, y: int) -> int:
    return x + y
```

### Decorator
A function that modifies another function's behavior.

```python
@decorator
def my_function():
    pass
```

### Context Manager
An object that manages resources using `with` statement.

```python
with open("file.txt") as f:
    content = f.read()
```

### Duck Typing
"If it walks like a duck and quacks like a duck, it's a duck." Python cares about what an object can do, not what it is.

### Memoization
Caching function results to avoid redundant computation.

### Recursion
When a function calls itself.

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

---

## String Concepts

### String Interpolation
Inserting variable values into strings.

```python
name = "Alice"
f"Hello, {name}"        # f-string
"Hello, {}".format(name)  # format method
"Hello, %s" % name      # % formatting
```

### Escape Character
Backslash `\` used to include special characters.

```python
"Hello\nWorld"  # \n is newline
"She said \"Hi\""  # \" is quote
```

### Raw String
String that treats backslashes as literal characters.

```python
r"C:\Users\name"  # Raw string
```

---

## Common Abbreviations

- **REPL**: Read-Eval-Print Loop (interactive Python shell)
- **PEP**: Python Enhancement Proposal
- **DRY**: Don't Repeat Yourself
- **EAFP**: Easier to Ask for Forgiveness than Permission (try-except)
- **LBYL**: Look Before You Leap (check before action)
- **PEP 8**: Python style guide
- **IDE**: Integrated Development Environment
- **API**: Application Programming Interface

---

## Best Practices Terms

### Pythonic
Code that follows Python's idioms and conventions. Readable, clear, and elegant.

```python
# Pythonic
for item in my_list:
    print(item)

# Not Pythonic
for i in range(len(my_list)):
    print(my_list[i])
```

### Zen of Python
Python's design philosophy. Access with `import this`.

Key principles:
- Beautiful is better than ugly
- Explicit is better than implicit
- Simple is better than complex
- Readability counts

---

## Quick Reference Table

| Term | Symbol | Example |
|------|--------|---------|
| Assignment | `=` | `x = 5` |
| Equality | `==` | `x == 5` |
| Not equal | `!=` | `x != 5` |
| Comment | `#` | `# comment` |
| String | `"` or `'` | `"text"` |
| List | `[]` | `[1, 2, 3]` |
| Tuple | `()` | `(1, 2, 3)` |
| Dict | `{}` | `{'k': 'v'}` |
| Set | `{}` | `{1, 2, 3}` |
| Colon | `:` | `if x:` |
| Line continuation | `\` | `x = 1 + \` |
| Indentation | 4 spaces | Standard |

---

This reference covers the essential Python terminology you'll encounter while learning and programming in Python!
