# [A walk in Python](/README.md)

## Day 7

* [Modules](day_7.md#modules)
* [Regular Packages](day_7.md#regular-packages)

## **Modules**

___

A Python module is nothing more than a single python file, with some functionalities that can be reused at some point.

For example:

```python
# myModule.py

def a_function():
    print('Hello! I am in a module')
```

The idea is that a can use this function in some other module of my application.
That way, we can reuse a functionality over and over.

```python
import myModule

myModule.a_function()

# output
Hello! I am in a module
```

Maybe we have a variable in our module and you want to use that too. Well, good news! You can do it! (Sorry Nike... :D)

```python
# myModule.py

def a_function():
    print('Hello! I am in a module')

a_variable = 'I am a variable'
```

```python
import myModule

myModule.a_function()
print(myModule.a_variable)

# output
Hello! I am in a module
I am a variable
```

We can also rename a module when importing...

```python
import myModule as new_name

new_name.a_function()
print(new_name.a_variable)

# output
Hello! I am in a module
I am a variable
```

And why import only what we need from the module...

```python
from myModule import a_function

a_function()
print(a_variable)

# output
Hello! I am in a module
Traceback (most recent call last):
  File "c:\a-walk-in-python\test.py", line 107, in <module>
    print(a_variable)
NameError: name 'a_variable' is not defined
```

>Note: the error is caused by not importing 'a_variable' from the module too.

We could have imported everything, by replacing a_function with '\*'. But this is not a good practice. is rare to need all that is included in a module. So, be careful with *import statements*.

Let's say that we have more than 20 functions in a module and, for the sake of best practices, we decided to separate them in different files.

## Regular Packages

That way we are going to have three files:

* int_module.py with a function called 'an_int_function()'
* string_module.py with a function called 'a_string_function()'
* bool_module.py with a function called 'a_bool_function()'

```text
project
│-- int_module.py
│-- string_module.py
│-- bool_module.py
│-- test.py
```

We can import them separately.

```python
# test.py
import int_module
import string_module
import bool_module

int_module.an_int_function()
string_module.a_string_function()
bool_module.a_bool_function()
```

That's more appropriate, but still not good enough, right?
Ok, now can move the modules to a new folder and get to a new file structure.

And now is where the **\_\_init__.py** file comes into play.

This file helps Python Interpreter to know this folder contains usable modules.

This file can be empty.

```text
project 
└───modules
│   │-- __init__.py
│   │-- int_module.py
│   │-- string_module.py
│   │-- bool_module.py
│   │   ...
│   
│-- test.py
```

```python
# test.py
import modules.int_module
import modules.string_module
import modules.bool_module

modules.int_module.an_int_function()
modules.string_module.a_string_function()
modules.bool_module.a_bool_function()
```

That's better but still a little verbose.

Actually, when a regular package is imported, this **\_\_init__.py** file is implicitly executed, and the objects it defines are bound to names in the package’s namespace.

So we can import the modules in the **\_\_init__.py** file. That way we'll have a much more easy to read files and structure.

```python
# __init__.py
from .int_module import an_int_function
from .string_module import a_string_function
from .bool_module import a_bool_function
```

>Note that the . before the module name is necessary as of Python 3 since it is more strict regarding [relative imports](https://peps.python.org/pep-0404/#imports).

```python
# test.py
import modules

modules.an_int_function()
modules.a_string_function()
modules.a_bool_function()
```
