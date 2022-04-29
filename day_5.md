# [A walk in Python](/README.md)

## Day 5

* Functions

## **Functions**

___

A **function** is a series of statements which returns some value to a caller. It can also be passed zero or more arguments, which may be used in the execution of this block of code, or body of the function.

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
    print(f'Hi! My name is {name} {lastname}')

say_hi('Eze')

# output
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

>Note that the function hasn't a return statement. These are called void functions. Are functions that do something that doesn't require returning a value.

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
def a_function(number1, number2, number3):
    print(f'The first number is {number1}')

a_function(number3 = 23, number1 = 2, number2 = 125)

# output
The first number is 2
```

We also have **Arbitrary Keyword Arguments**. This way the function will receive a dictionary of arguments, and can access the items accordingly.

```python
def a_function(**numbers):
    print(f'The first number is {numbers["number1"]}')

a_function(number3 = 23, number1 = 2, number2 = 125)

# output
The first number is 2
```

>Note that **kwargs works the same as *args buy instead of accepting positional arguments, it accepts keyword arguments such as those from a dictionary (i.e. a dictionary of arguments)

In this case we use the unpacking operator '\*\*', that will take all keyword arguments given in the input and **pack** them all into a dictionary.

In a function, we can always set a **default value** for a parameter.

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

We said that we have void functions that doesn't return a value, and functions that does return a value... or more!

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

Recursion is a mathematical and programming concept in which a function calls itself.
It can be dangerous because we need to define a base case in which the function reach of stopping point.

For example, in a countdown we start on a certain number, it subtracts 1,and call it self. Every time it calls itself, the call of the function pass the result as an argument. But we need to stop when the result is 0. If not, we are trapped in an infinite loop.

Let's see...

```python
def recursive_subtraction(number):
    if number > 0:
        print(number)    
        number -= 1
        recursive_subtraction(number)
    
    return 'Done!'

print(recursive_subtraction(10))

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

This example is pretty silly. I bet most of you realized that you could have done it with a simple for loop.
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

A lambda function is a small anonymous function. It can have multiple parameters, but only one expression.

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

Python doesn't encourage using immediately invoked lambda expressions like in the example. It simply results from a lambda expression being callable, unlike the body of a normal function.

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

### Wrapper Functions

We have talked about high-order functions. Another way to see this particular case, is a function wrapping another one...

```python
def wrapper_function(func):

    def inner_function():
        print('Printing before function!')
        func()
        print('Printing after function!')

    return inner_function()

def a_function():
    print('I`m the function!')

wrapping = wrapper_function(a_function)

# output
Printing before function!
I`m the function!
Printing after function!
```

This a call a Wrapper Function. Or one way to write a wrapper function or just **wrapper**...

This is used to modify the behavior of a function.

Another way to use a wrapper is with decorators. Decorators, allow us to do the same thing as the last example, but in a simpler way.

Let's see that...

```python
def wrapper_function(func):

    def inner_function():
        print('Printing before function!')
        func()
        print('Printing after function!')
        
    return inner_function
 
@wrapper_function
def a_function():
    print('I`m the function')
 
a_function()

# output
Printing before function!
I`m the function!
Printing after function!
```

 > Note that every time we call 'a_function', the execution of that, will we wrapped with the 'wrapper_function'.

## Iterators and Generators

### Iterators

An iterator is an object that contains a countable number of values and can be iterated upon.

In Python these objects have both methods, \_\_iter__() and \_\_next__().

As we saw, lists, tuples, sets and dictionaries (*and even strings*) are iterable objects, which you can get an iterator from.

These have the iter() method which is used to get an iterator.

```python
a_list = ['Ezequiel', 'Javier', 'Emilio', 'Nicolas']
an_iter = iter(a_list)

print(next(an_iter))
print(next(an_iter))
print(next(an_iter))
print(next(an_iter))

# output
Ezequiel
Javier
Emilio
Nicolas
```

> Note that in between these *print* lines, we can do another thing, print something else, call a function or whatever we want, and the result of the next on that iterator, would be the next item on the iterable.

Of course we can loop through an iterable too as we saw previously.

Later, when we learn about Classes, we0ll see how toi create an Iterator Class.

### Generators

A Generator or generator function is a kind of function that creates a lazy iterator. These are objects that you can loop over like a *list*. However, unlike lists, lazy iterators do not store their contents in memory.

Let's see something first...

```python
a_list = list(range(10))
print(*a_list, end=" ")

# output
0 1 2 3 4 5 6 7 8 9
```

Another way to do this...

```python
for n in range(10):
    print(n, end=" ")

# output
0 1 2 3 4 5 6 7 8 9
```

Now, what if want to create a list from 0 to infinite?
We could do the same as above, but we0ll have an unstoppable (not really) loop of increasing numbers, with no possibility to do anything while the code is executing, not to mention, the enormous amount of memory the the list will occupy.

So, using a generator function we have a much better alternative!

```python
def infinite_sequence():
    number = 0
    while True:
        yield number
        number += 1
```

> Note that we are just emulating the range built-in method. In a moment you will see why...

Now we have that function that looks pretty much like a regular function, except for the yield statement. The *yield* will return the value in the statement, and wait to continue the execution, but it needs to be done with the *next()* method, otherwise would behave as a regular function.

Let's continue...

```python
for i in infinite_sequence():
    print(i, end = " ")

# output
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29
30 31 32 33 34
[...]
1251235 1251236 1251237 1251238 1251239 1251240 1251241
KeyboardInterrupt
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
```

As we said above, we have iterate the function with a for loop and we are in the exact same scenario as before, but if we do this...

```python
a_generator = infinite_sequence()
next(a_generator)
next(a_generator)
next(a_generator)
next(a_generator)

# output
0
1
2
3
```

And every time we call the next method of the generator, we'll have the next value.

As we always say, this is a dumb example.
But what if we want the first 50000 items of the fibonacci sequence, to do some batch processing?

Option 1:

```python
def fibonacci(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

fibonacci(50000)
```

We can create a list like this and process tha data on the list. But this way we are going to have a huge list, occupying a lot of memory.

Option 2:

```python
def fibonacci(n):
    a = b = 1
    result = []
    for i in range(n):
        '''
        block of code to process
        '''
        result.append(processed_data)
        a, b = b, a + b
    return result

fibonacci(50000)
```

This time, we already have the processed data, but again, a huge list, occupying loads of memory.

Option 3:

```python
def fibonacci(from, count):
    a = b = from
    result = []
    for i in range(count):
        result.append(a)
        a, b = b, a + b
    return result

total = 50000
from  = 1
count = 50
for n in range(count / to):
    print(fibonacci(from, count))
    from += count
    to += count
    # or whatever we need to do...
```

Here we have to loops, and have to keep track of the variables, which in a complicated context can lead to a large number of mistakes and bugs.

Best option:

```python
def fibonacci(n, amount):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        if len(result) == amount:
            yield result
            result = []
        a, b = b, a + b

gen = fibonacci(50000, 50)
print(next(gen))
print(next(gen))
# ...
print(next(gen))
```

This way we don't have to keep track on which batch in coming next or any other thing. We just call the next method the times we need, even inside a loop.

What we are doing is to avoid using a callback, and use a generator and the *yield* reserved word.

### Generator expressions

Similar to the lambda functions which create anonymous functions, generator expressions create anonymous generator functions.

The syntax for generator expression is similar to that of a list comprehension in Python. But the square brackets are replaced with round parentheses.

Let's see an example...

```python
a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared = (x**2 for x in a_list)

print(next(squared))
print(next(squared))
print(next(squared))
print(next(squared))

# output
1
4
9
16
```
