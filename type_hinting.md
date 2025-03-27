# Chapter: Type hinting in Python

## 1. Introduction to Type hinting in Python

Python is a dynamically typed language, meaning variables do not require explicit type definitions. However, Python introduced type hints (also called static typing) in [PEP 484](https://peps.python.org/pep-0484/) to improve readability, maintainability, and error detection.

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

| Type   | Example                     |
|--------|-----------------------------|
| `int`  | `x: int = 10`              |
| `float`| `y: float = 3.14`          |
| `str`  | `name: str = "Alice"`      |
| `bool` | `is_active: bool = True`   |
| `list` | `numbers: list[int] = [1, 2, 3]` |
| `tuple`| `coords: tuple[int, int] = (10, 20)` |
| `dict` | `user: dict[str, int] = {"age": 25}` |

---

## 3. Using `List`, `Tuple`, `Dict` from `typing`

For more complex data structures, use `typing` module annotations:

```python
from typing import List, Tuple, Dict

numbers: List[int] = [1, 2, 3]
coordinates: Tuple[int, float] = (10, 3.5)
user_data: Dict[str, int] = {"age": 30, "score": 100}
```

- `List[int]`: A list where all elements are integers.
- `Tuple[int, float]`: A tuple with an integer and a float.
- `Dict[str, int]`: A dictionary where keys are strings, and values are integers.

---

## 4. Optional Types (`Optional`)

If a variable can be `None`, use `Optional`:

```python
from typing import Optional

def get_user(id: int) -> Optional[str]:
    if id == 1:
        return "Alice"
    return None  # Function may return None
```

Equivalent to:

```python
str | None
```

---

## 5. Function Type Annotations

### Example: Function with Type Hints

```python
from typing import List

def multiply(numbers: List[int], factor: int) -> List[int]:
    return [n * factor for n in numbers]
```

- `numbers: List[int]`: Expects a list of integers.
- `factor: int`: Expects an integer.
- `-> List[int]`: Returns a list of integers.

---

## 6. Type Hints for Classes

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

## 7. Type Checking at Runtime (`isinstance`)

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

## 8. Advanced Typing Concepts

### Using `Any` (Accepts Any Type)

If a function can accept any type, use `Any`:

```python
from typing import Any

def echo(value: Any) -> Any:
    return value  # Can accept and return any type
```

### Using `Union` (Multiple Allowed Types)

Instead of `Any`, you can specify specific allowed types with `Union`:

```python
from typing import Union

def process(value: Union[int, str]) -> None:
    print(value)
```

Equivalent in Python 3.10+:

```python
def process(value: int | str) -> None:
    print(value)
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

## 9. Enforcing Type Checking with `mypy`

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

## 10. Summary

- Type hints improve code readability and help with error detection.
- Use basic types (`int`, `str`, `bool`, etc.) and collections (`List`, `Dict`, etc.).
- Use `Optional` for `None` values, `Union` for multiple types, and `Callable` for function arguments.
- Type hints do not affect runtime behavior but can be checked statically with `mypy`.