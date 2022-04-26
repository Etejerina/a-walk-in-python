# [A walk in Python](/README.md)

## Day 1

* Introduction to Python
  * [What is Python?](./day_1.md#what-is-python)
  * [Why Python?](./day_1.md#why-python)
  * [Clarifying](./day_1.md#clarifying)
  * [The *Zen* of Python](./day_1.md#the-zen-of-python)
  * [PEP's](./day_1.md#peps)
* [Starting with Python](day_1.md#staring-with-python)
  * [Installing Python](https://www.python.org/downloads/)
  * [IDE (VS Code)](https://code.visualstudio.com/)
  * [Pip](day_1.md#pip)
  * [Virtual Environments](day_1.md#virtual-environments)
  * [Syntax](day_1.md@syntax)

## **Introduction**

___

## What is Python

Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.
There are two versions of Python, *Python 2* and *Python 3*. The latter is the one we are going to see throughout this course.

We can say that Python is:

* [Interpreted](day_1.md#interpreted)
* [High-level](day_1.md#high-level)
* [Cross-platform](day_1.md#cross-platform)
* [Multi-paradigm](day_1.md#multi-paradigm)
* [Dynamically and strongly typed](day_1.md#dynamically-and-strongly-typed)

### Interpreted

The program directly executes the instructions written, without requiring them to have been previously compiled into a machine language program.

### High-level

It is a programming language with strong abstraction from the details of the computer.

### Cross-platform

Refers to a language that is supportes in multiple platforms, such as Windows, Linux, Mac, Raspberry Pi, etc.

### Multi-paradigm

It is a language that can use procedural programming, functional programming and/or object-oriented.

### Dynamically and strongly typed

It is dynamically typed because we don't have to define the type of a variable.

It is also strongly typed because the interpreter keeps track of all variables types.

## Why Python?

Python is an easy to learn language since it has a simple syntax similar to the English language. It also has syntax that allows developers to write programs with fewer lines than some other programming languages.

There are many more advantages, but these two qualities were the most important for me, since like many of us, we are self-taught developers.

Having both an easy to learn and a very rich language, that can be suplemented with lots of libraries, are the things that makes Python a very powerful one.

## Clarifying

One of the key features of Python is that everything is an **Object**, and the type is just one attribute of an object. As an illustration, we can assign a single integer to a variable, and use the Python built-in function dir for finding out the attributes of the object.

Having said that, you might read that Python is by definition a Object-oriented language. As we have seen before, Python is multiparadigm, so don't be confused with these two concepts.

## The *Zen* of Python

It is a collection of 19 *guiding principles* for writing computer programs that influence the design of the Python programming language.

The principles are:

```cmd
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one, and preferably only one, obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.>
Now is better than never.
Although never is often better than right now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea... let's do more of those!
```

You can check them out, only running python on the console and then

```python
import this
```

## PEP's

Python's development is conducted largely through the Python Enhancement Proposal (PEP) process, the primary mechanism for proposing major new features, collecting community input on issues and documenting Python design decisions.

Python coding style is covered in [PEP 8](https://www.python.org/dev/peps/pep-0008/). Outstanding PEPs are reviewed and commented on by the Python community and the steering council.

## **Starting with Python**

___

### Install Python and Pip

[https://www.python.org/downloads/](https://www.python.org/downloads/)

### Install IDE (VS Code)

[https://code.visualstudio.com/](https://code.visualstudio.com/)

### Pip

[Pip](https://pypi.org/project/pip/) is the package installer for Python. You can use pip to install packages from the Python Package Index and other indexes.

### Virtual Environments

Most of the times when developing with Python, you might need external libraries or packages. In order to do that, you'll need to install them. This can be done with Pip command.

But if we don't create a virtual Environment, those packages are going to be installed globally and we might want to install only the packages we need for a certain program and not another.

To do that, I recommend to use **virtualenv**.

It can be installed with pip:

```bash
pip install virtualenv
```

Then we'll need to create our own virtual Environment.

```bash
virtualenv <environment_name>
```

Once this is done we can activate/deactivate with

* On Windows run `<environment_name>\Scripts\activate.bat`  (*`deactivate.bat` to deactivate the environment*).
* On Windows using PowerShell, run `<environment_name>\Scripts\activate.ps1`  (*just `deactivate` to deactivate the environment*).
* On Windows using Git Bash run `<environment_name>\Scripts\activate`  (*`deactivate` to deactivate the environment*).
* On Linux run `source <environment_name>/bin/activate`     (*`deactivate` to deactivate the environment*)

### Syntax

Python uses indentation to indicate a block of code. Indentation refers to the spaces at the beginning of a code line.

Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

```python
if a > 5:
    print("Es mayor a 5")
```

___

[Go to Day 2](day_2.md)

___
