# [A walk in Python](/README.md)

## Day 2

* Variables
  * [What are Variables?](./day_2.md#what-are-variables)
  * [Constants](./day_2.md#constants)
  * [Global Variables](./day_2.md#global-variables)
  * [Multiple assignment and unpacking](./day_2.md#multiple-assignment-and-unpacking)
* Data Types
  * [Built-in Data Types](day_2.md#data-types)

## **Variables**

___

## What are variables?

Variables in Python are containers for storing data. There is no reserved word for declaring a variables. You just go like this...

```python
a = "Hello world!"

b = 1

c = True
```

As we said before, Python is dynamically typed, so the interpreter assumes the type from the type of the value assigned to that variable name. You can even change the type after they have been set.

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

To know the type of a variable you can use the reserved word **type**

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

Another one of these conventions, are constants as we just saw. There is no way to declare a variable as a constant. The convention says that if you see a variable name in uppercase, it is a constant.

```python
CONSTANT_NAME = 1
ANOTHER_CONSTANT = 'Hello'
```

You can change the value of these constants, although if you see the name in uppercase, you're not supposed to. You will be cursed by the Python Community (:D).

## Global variables

All variables that are created outside of a function in Python are, by default, global variables. Global variables can be used outside and inside of a function.

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

However, if a variable with the same name is declared inside the function, this variable is going to be local, available to use inside the function, and the one declared outside, will be used outside the function.

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

## Multiple assignment and unpacking

You can also assign multiple variables, like this...

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

>Note: the number of values and variable names, should match, or you will get an error.

Also, you can assign the same value to different variables in one line, like this...

```python
x, y, z = ['Ezequiel']*3
print(x)
print(y)
print(z)

#output
Ezequiel
Ezequiel
Ezequiel
```

There is a way to extract the values of a collection into different variables. This is called **unpacking**

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

## **Data Types**

## Built-in Data Types

In programming in general, data types are very important. You can do different things with different data types.
As in Python everything is an object, every type has its own methods and attributes.

Python has the following data types built-in by default, divided into these categories:

Text Type: ***str***

* Strings in python are surrounded by either single quotation marks, or double quotation marks.
'hello' is the same as "hello".
You can display a string literal with the print() function.
* Strings are immutable

Numeric Types: ***int, float, complex***

* Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
* Float, or "floating point number" is a number, positive or negative, containing one or more decimals. Float can also be scientific numbers with an "e" to indicate the power of 10.
* Complex numbers are written with a "j" as the imaginary part.

Boolean Type: ***bool***

* In programming you often need to know if an expression is True or False. Those are boolean values.

Sequence Types: ***list, tuple***

* Lists are one of 4 built-in data types in Python used to store collections of data.
Lists are created using square brackets.

* Tuples are used to store multiple items in a single variable.
A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets.

Mapping Type: ***dict***

* Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

Set Types: ***set, frozenset***

* Sets are used to store multiple items in a single variable.
A set is a collection which is unordered, unchangeable*, and unindexed.
* Frozenset is just an inmutable version of a set.

In order to get the data type from a variable you can just run:

```python
name = 'pepe'
print(type(name))

# output
<class 'str'>
```

Again, if you want to set a specific data type to a variable, you need to use the casting method.

```python
a = int(1)
print(a)
print(type(a))

b = float(1)
print(b)
print(type(b))

c = str(1)
print(c)
print(type(c))

# output
1
<class 'int'>
1.0
<class 'float'>
1
<class 'str'>
```

___

[Go to Day 3](day_3.md)

___
