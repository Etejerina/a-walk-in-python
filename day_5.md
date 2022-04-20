# [A walk in Python](/README.md)

## Day 5

* Functions

## **Functions**

___

A **function** is a series of statements wich returns some value to a caller. It can also be passed zero or more arguments, wich may be used in the execution of this block of code, or body of the function.

> A parameter is a variable in a method definition. When a method is called, the arguments are the data you pass into the method's parameters.

Having said that, in Python function definitions, are called arguments, or *args* for short.

Functions use the reserved word *def*, as follows.

```python
def a_function(arguments):
    # some code
    return some_value
```

And the function can be called this way:

```python
a_function()
```

Let's see an example:

```python
def say_hi(name):
    print(f'Hi! My name is {name}')

say_hi('Eze')
say_hi('Pedro')

# output
Hi! My name is Eze
Hi! My name is Pedro
```

It's very important that the amount of arguments you pass to a function, are the same amount of parameters on the function definition.

```python
def say_hi(name, lastname):
    print(f'Hi! My name is {name} {lastanme}')

say_hi('Eze')

# ooutput
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: say_hi() missing 1 required positional argument: 'lastname'
```

 Or the other way around...

 ```python
def say_hi(name):
    print(f'Hi! My name is {name}')

say_hi('Eze', 'Tejerina')

# output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: say_hi() takes 1 positional argument but 2 were given
 ```

>Note that the function hasn't a return statement. These are called void functions. Are functions that do something that doesn't require returnung a value.

As we said before, in the function definition, in parentheses, we have the parameters, that can be zero or many.

Also we can have what is called Arbitrary Arguments (\*args). The use of these is to avoid enumerate many positional arguments, and just use the unpacking operator '*', in particular when we don't how how many arguments where are receiving.

Let's see some examples

```python
number_list = [1, 42, 23, 4, 6]

def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(sum(number_list))
```

Here we first create a list, and pass it as an argument. Inside the function we iterate that list and make the calculation.

```python
def sum(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(sum(1, 42, 23, 4, 6))
```

In this second example, we can see we are passing what seems to be comma separated values, but is a tuple. So in the function, we use the unpacking operator '*', that will take all positional arguments given in the input and **pack** them all into a single iterable object.

Another way to pass arguments, are keyword arguments, or kwargs for short. These have the "key = value" syntax.
This way the order of the arguments does not matter.

```python
def a_function(number1, mumber2, number3):
    print(f'The first number is {number1}')

a_function(number3 = 23, number1 = 2, number2 = 125)

# output
The first number is 2
```

We also have **Arbitrery Keyword Arguments**. This way the function will receive a dictionary of arguments, and can access the items accordingly.

```python
def a_function(**numbers):
    print(f'The first number is {numbers["number1"]}')

a_function(number3 = 23, number1 = 2, number2 = 125)

# output
The first number is 2
```

>Note that **kwargs works the same as *args buy instead of accepting positional arguments, it accepts keyword arguments such as those from a dictionary (i.e. a dictionary of arguments)

In this case we use the unpacking operator '\*\*', that will take all keyword arguments given in the input and **pack** them all into a dictionary.
