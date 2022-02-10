# [A walk in Python](/README.md)

## Day 2

* Variables
  * [What are Variables?](./day_2.md#what-are-variables)
  * [Constants](./day_2.md#constants)
  * [Global Variables](./day_2.md#global-variables)
  * [Multiple assigment and unpacking](./day_2.md#multiple-assigment-and-unpacking)
* [Data Types](day_2.md#data-types)
  * [Installing Python](https://www.python.org/downloads/)
  * [IDE (VS Code)](https://code.visualstudio.com/)
  * [Pip](day_1.md#pip)
  * [Virtual Environments](day_1.md#virtual-environments)
  * [Syntax](day_1.md@syntax)

## **Variables**

___

## What are variables?

Variables in Python are containers for storing data. There is no reserved word for declaring a variables. Yo just go like this...

```python
a = "Hello world!"

b = 1

c = True
```

As we said before, Python is dinamically typed, so the interpreter assumes the type from the type of the value assigened to that variable name. You can even change the tyoe after they have been set.

```python
a = "Hello world!"
print(a)

a = 1
print(a)
```

If you want to specify the type of a variable, this can be done using casting.

```python
a = str('Hello world!')  # a will be 'Hello World!'
b = str(1)               # b will be '1'
c = int(1)               # c will be 1
d = float(1)             # d will be 1.0
```

To know the tyope of a variable ypou can use the reserved word **type**

```python
a = "Hello world!"
print(type(a))

# output
<class 'str'>  
```

In Python there are lots of things that are just conventions ([PEP8](https://www.python.org/dev/peps/pep-0008/#naming-conventions)), this means that some things are in a certain way and all python developers should use them.

For variables names, these are the rules:

* must start with a letter or _
* cannot start with a number
* can only contain alpha-numeric characters and _
* are case sensitive

Lowercase letters are commonly used in variable names, with word separated by '_' as necessary in order to improve readability.

Other conventions are:

* Module in lowercase
* Class in CapWords
* Functions in lowercase
* Methods in lowercase
* Type variables in CapWords
* Constants in UPPERCASE
* Package in lowercase

## Constants

Another one of these conventions, are constants as we just saw. There is no way to declare a variable as a contant. The convention says that if you see a variable name in uppercases, it is a constant.

```python
CONSTANT_NAME = 1
ANOTHER_CONSTANT = 'Hello'
```

You can change the value of these contants, although if you see the name in upeercase, you're not supposed to. You will be cursed by the Python Community (:D).

## Global variables

All the variables that are created outside of a function, in Python is by default a global variable. This variable can be used outside and inside a function.

```python
name = 'Ezequiel'

def greeting():
    print('Hello ' + name)

print('My name is ' + name)
greeting()

#output
My name is Ezequiel
Hello Ezequiel
```

But if a variable with the same name, is declared inside the function, this variable is going to be local, available to use inside the function, and the one declared outside, will be used outside the function.

```python
name = 'Ezequiel'

def greeting():
    name = 'Jose'
    print('Hello ' + name)

print('My name is ' + name)
greeting()

#output
My name is Ezequiel
Hello Jose
```

There is a way to declare a global variable inside a function though, using the reserved word 'global'.

```python
name = 'Ezequiel'

def greeting():
    global name = 'Jose'

greeting()
print('My name is ' + name)

#output
My name is Jose
```

## Multiple assigment and unpacking

You also can assign multiple variables, like this...

```python
x, y, z = 'Hello', 'beautiful', 'World'
print(x)
print(y)
print(z)

#output
Hello
beautiful
World
```

*Note: the number of values and variable names, should match, or you will get an error.*

Also you can assign the same value to different variables in one line, like this...

```python
x, y, z = 'Ezequiel'
print(x)
print(y)
print(z)

#output
Ezequiel
Ezequiel
Ezequiel
```

There is a way to extract the values of a collection, into different variables. This is called **unpacking**

```python
words = ['Hello', 'beautiful', 'World']
x, y, z = words
print(x)
print(y)
print(z)

#output
Hello
beautiful
World
```

___

## Data Types
