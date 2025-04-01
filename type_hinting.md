# Chapter: Type hinting in Python

## 1. Introduction to Type hinting in Python

Python is a dynamically typed language, meaning variables do not require explicit type definitions. However, Python introduced type hints (also called static typing) in [PEP 484](https://peps.python.org/pep-0484/) to improve readability, maintainability, and error detection. Then some improvements were introduced in 3.9 with [PEP 585](https://peps.python.org/pep-0585/)

### Example: Dynamic Typing in Python

```python
def add(a, b):
    return a + b  # No type specified
```

The function `add()` works for integers, floats, and even strings, but this flexibility can lead to unexpected errors.

### Example: Using Type Hints

```python
def add(a: int, b: int) -> int:
    return a + b
```

- `a: int` and `b: int` indicate that `a` and `b` should be integers.
- `-> int` specifies that the function returns an integer.

Type hints do not enforce types at runtime, but tools like [mypy](https://mypy-lang.org/) can check for type errors statically.

---

## 2. Basic Type Hints

Python provides basic type hints for primitive types:

| Type   | Example                              |
|--------|--------------------------------------|
| `int`  | `x: int = 10`                        |
| `float`| `y: float = 3.14`                    |
| `str`  | `name: str = "Alice"`                |
| `bool` | `is_active: bool = True`             |
| `list` | `numbers: list[int] = [1, 2, 3]`     |
| `tuple`| `coords: tuple[int, int] = (10, 20)` |
| `dict` | `user: dict[str, int] = {"age": 25}` |

```python

numbers: list[int] = [1, 2, 3]
coordinates: tuple[int, float] = (10, 3.5)
user_data: dict[str, int] = {"age": 30, "score": 100}
```

- `list[int]`: A list where all elements are integers.
- `tuple[int, float]`: A tuple with an integer and a float.
- `dict[str, int]`: A dictionary where keys are strings, and values are integers.

---

## 3. Function Type Annotations

### Example: Function with Type Hints

```python

def multiply(numbers: list[int], factor: int) -> list[int]:
    return [n * factor for n in numbers]
```

- `numbers: list[int]`: Expects a list of integers.
- `factor: int`: Expects an integer.
- `-> list[int]`: Returns a list of integers.

---

## 4. Type Hints for Classes

### Annotating Class Attributes

```python
class Person:
    name: str
    age: int

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
```

---

## 5. Type Checking at Runtime (`isinstance`)

While type hints do not enforce types at runtime, you can check types using `isinstance()`:

```python
def process(value: int | str) -> None:
    if isinstance(value, int):
        print(f"Processing an integer: {value}")
    elif isinstance(value, str):
        print(f"Processing a string: {value}")

process(42)
process("hello")
```

---

## 6. Advanced Typing Concepts


### Multiple Allowed Types

If two or more types are allowed, you can separate them with `|`, as in the following example:

```python
def process(value: int | str) -> None:
    print(value)

# so these would be valid:
process(1)
process("2")

# and these would not:
process(None)
process(True)
process([])
process((,))
```

This also applies if  one of the valid types is None:
```python
def accept_int_or_None(val: int | None) -> None:
    print(val)
```
### Using `Callable` (Type Hint for Functions)

```python
from typing import Callable

def apply(func: Callable[[int, int], int], x: int, y: int) -> int:
    return func(x, y)

def add(a: int, b: int) -> int:
    return a + b

print(apply(add, 2, 3))  # Output: 5
```

- `Callable[[int, int], int]` means a function that takes two `int` arguments and returns an `int`.

---
### Using `Any` (Accepts Any Type)

If a function can accept any type, use `Any`:

```python
from typing import Any

def echo(value: Any) -> Any:
    return value  # Can accept and return any type
```

---
### Using aliases:

You can use aliases to avoid code duplication like this:

```python
optional_number: int|float|complex|None

def foo(value: optional_number) -> optional_number:
    return value

```

---
## 7. Enforcing Type Checking with `mypy`

Even though Python does not enforce types at runtime, you can check them using `mypy`:

### Install `mypy`:

```bash
pip install mypy
```

### Run Type Checking:

```bash
mypy script.py
```

If there are mismatched types, `mypy` will report them.

---
## 8. Legacy typing uses

Before PIP 585 you had to import special type aliases and utilities from typing:
* for collection types, you had to import `List`, `Tuple`, `Dict`, etc from `typing` (instead of just uding `list`, `tuple`, `dict`, etc)
* to specify two (or more) types you needed to import `Union` (instead of `|`)
* to specify an optional type (you can think of it as an union where one of the possible values is None) you could import `Optional` (instead of `<some_type> | None`)

For more complex data structures, use `typing` module annotations:

```python
from typing import List, Tuple, Dict
from typing import Union, Optional

numbers: List[int] = [1, 2, 3]
coordinates: Tuple[int, float] = (10, 3.5)
user_data: Dict[str, int] = {"age": 30, "score": 100}
a_number: Union[int, float] = 1
a_number = 1.1  # this would be allowed
discount: Optional[float] = 0.2
```
This is deprecated and you should use the newer style.

---

## 9. Summary

- Type hints improve code readability and help with error detection.
- Use types (`int`, `str`, `bool`, `list`, `dict`, etc.).
- Use `|` to allow more than one type (even if the value is optional: `<some_type>|None` ).
- Use `Any` (from the typing module) if every type should be allowed.
- Use `Callable` (from the typing module) for a function that is passed as argument.
- Type hints do not affect runtime behavior but can be checked statically with `mypy`.
