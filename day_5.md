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

In a function, we can alwyas set a **default value** for a parameter.

For example...

```python
def im_from(country = 'Argentina'):
    print(f'I am from {country}')

im_from('Canada')
im_from()

# output
I am from Canada
I am from Argentina
```

> Note that in the second call to the function, we are not passing an argument to the function, so it's printing the default value on the function definition. When we pass the argument, the function behaves as always.

One more very nice thing ¡ about functions in Python for me is, that you can return more than one value.

We said that we have void functions that doesn't retunr a value, and functions that does return a value... or more!

Let's see an example of that.

```python
def sum_and_square(a_number, another_number):
    sum_total = a_number + another_number
    square = a_number ** 2
    return sum_total, square

print(sum_and_square(5, 2))

# output
(7, 25)
```

> Note that the returned value is tuple with two values, the sum of he values and the first number squared.

Just like any tuple we can unpack it.

```python
def sum_and_square(a_number, another_number):
    sum_total = a_number + another_number
    square = a_number ** 2
    return sum_total, square

addition, squared = sum_and_square(5, 2)
print(addition)
print(squared)

# output
7
25
```

### Recursion

What is recursion?

Recursion is a mathematical and programming concept in wich a function calls itself.
It can be dangerous because we need to define a base case in wich the function reach of stopping point.

For example, in a countdown we start on a certain number, it substracts 1,and call it self. Every time it calls itself, the call of the function pass the result as an argument. But we need to stop when the result is 0. If not, we are trapped in an infinite loop.

Let's see...

```python
def recursive_substraction(number):
    if number > 0:
        print(number)    
        number -= 1
        recursive_substraction(number)
    
    return 'Done!'

print(recursive_substraction(10))

# output
10
9
8
7
6
5
4
3
2
1
Done!
```

This exmple is pretty silly. I bet most of you realized that you could have done it wuth a simple for loop.
You're right!

Let's go with something more difficult... What about a factorial function?

```python
def factorial(number):
    return_value = 1
    for i in range(2, number + 1):
        return_value *= i

    return return_value

print(factorial(6))

# output
720
```

Ok! This is not recursion... I know!
So, hands on!

```python
def factorial(number):
    return 1 if number <= 1 else number * factorial(number - 1)

print(factorial(6))

# output
720
```

One of the advantages is that the code looks cleaner, and easier. On the other hand, sometimes recursions are more complicate to follow, and are more expensive in terms of memory usage.
If we follow the execution of the code we could understand why.

## Lambdas

A lambda function is a small anonimous function. It can have multiple parameters, but only one expression.

Syntax:

```python
lamba arguments : expression
```

For example:

```python
square_lambda = lambda a : a ** 2 # or print((lambda a : a ** 2)(5))

print(square_lambda(5))

# output
25
```

Python doesn't encourage using immediately invoked lambda expressions like in the exmaple. It simply results from a lambda expression being callable, unlike the body of a normal function.

```python
print((lambda a : a ** 2)(5))

# output
25
```

Lambda functions are frequently used with higher-order functions.

Higher-order functions are functions that takes one or more functions as arguments or return one or more functions.

Let's see 2 examples...

```python
def n_times(times):
    return lambda n : n * times

doubler = n_times(2)
tripler = n_times(3)

print(doubler(10))
print(tripler(10))

# output
20
30
```

Here we are returning a lambda function. This way we can re use it in order to create another.

```python
n_times = lambda n, func: func(n)

print(n_times(10, lambda n : 2 * n))
print(n_times(10, lambda n : 3 * n))

# output
20
30
```

In this case we are passing to 'n_times', a value and a lambda function. Again it doesn't make much sense, but is an example.

More about [lambdas here](https://realpython.com/python-lambda/).
