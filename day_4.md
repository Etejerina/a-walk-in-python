# [A walk in Python](/README.md)

## Day 4

* Operators
  * [Arithmetic operators](day_4.md#arithmetic-operators)
  * [Assignment operators](day_4.md#assignment-operators)
  * [Comparison operators](day_4.md#comparison-operators)
  * [Logical operators](day_4.md#logical-operators)
  * [Identity operators](day_4.md#identity-operators)
  * [Membership operators](day_4.md#membership-operators)
  * [Bitwise operators](day_4.md#bitwise-operators)
* [Control Structures](day_4.md#control-structures)
  * [Conditionals](day_4.md#conditionals)
  * [Loops](day_4.md#loops)
    * [While Loop](day_4.md#while-loop)
    * [For Loop](day_4.md#for-loop)
  * [Exceptions](day_4.md#exceptions)

## **Operators**

___

In Python, and in general, operators are symbols used to perform arithmetic and logical operations on values and variables.

We have:

* Arithmetic operators
* Assignment operators
* Comparison operators
* Logical operators
* Identity operators
* Membership operators
* Bitwise operators

## Arithmetic operators

These are used to perform common mathematical operations.

| Operator | Name
|---|---
| + | addition
| - | subtraction
| * | multiplication
| / | division
| % | modulus
| ** | exponentiation
| // | floor division

```python
print(1 + 5)
print(10 - 6)
print(2 * 8)
print(8 / 4)
print(9 % 2)
print(3 ** 3)
print(9 // 2)

# output
6
4
16
2.0
1
27
4
```

## Assignment operators

These are used to assign values to variables.
Basically is used the '=' operator, but can be combined with other operators.

```python
a = 1
print(a)
a += 2 # or a = a + 1
print(a)
a **= 2 # or a = a ** 2
print(a)

# output
1
3
9
```

## Comparison operators

These are used to compare values, or variables with values assigned. The result (or returned value) of that evaluation is a boolean.

That's why these are most commonly used on if statements.

| Operator | Name
|---|---
| == | Equal
| != | Not equal
| > | Greater than
| < | Less than
| >= | Greater than or equal than
| <= | Less than or equal than

```python
print(2 == 2)
print(2 == 2.0)
print('hola' == 'Hola')
print('Eze' == 'Eze')
print(2 != 2)
print(10 > 5)
# ...and many more

# output
True
True
False
True
False
True
```

## Logical operators

These are used to combine conditional statements, or the boolean result of a statement.

| Operator | Description
|---|---
| and | Returns True if both statements are true
| or | Returns True if one of the statements is true
| not | Reverse the result, returns False if the result is true

```python
print(True and False)
print(True or False)
print(not True)
print(2 == 2 and True) # 2 == 2 is True and then True and True is True

# output
False
True
False
True
```

You can also use 'truthy' or 'falsy' values here...

```python
print(bool(1 and 3))
print(bool(1 or 3))
print(bool(1 and [])) # remember we saw that [] (empty list) is falsy

# output
True
True
False
```

## Identity operators

These are used to check if two values (or variables) are located on the same part of the memory.

| Operator | Description
|---|---
| is |  Returns True if both variables are the same object
| is not | Returns True if both variables are not the same object

```python
a_number = 1
another_number = 1
a_string = 'People'
another_string = 'People'
a_list = [1, 2]
another_list = [1, 2]

print(a_number is another_number)
print(True is not True)
print(a_string is another_string)
print(a_list is another_list)

# output
True
False
True
False 
```

>Note that in the last example, we are comparing list that have the same content, but they are different lists. I mean, they are not the same object.

## Membership operators

These are use to check if an element (or sequence of elements) are contained in an object.

| Operator | Description
|---|---
| in | Returns True if a sequence with the specified value is present in the object
| not in | Returns True if a sequence with the specified value is not present in the object

```python
original_bands = ['Faith No More', 'Soundgarden']
print('Bush' in original_bands)
print('ABBA' not in original_bands)

# output
False
True
```

## Bitwise operators

These are use to operate bit by bit, and act on operands as if they were strings of binary digits.

| Operator | Name | Description
|---|---|---
| & | AND | Sets each bit to 1 if both bits are 1
| \| | OR | Sets each bit to 1 if one of two bits is 1
| ^ | XOR | Sets each bit to 1 if only one of two bits is 1
| ~ | NOT | Inverts all the bits
| << | Zero fill left | Shift left by pushing zeros in from the right and let the leftmost bits fall off
| >> | Signed right | Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off.

```python
a_number = 10       # binary: 0000 1010
another_number = 23 # binary: 0001 0111

print(a_number & another_number)
print(a_number | another_number)
print(a_number ^ another_number)
print(~a_number)
print(<<a_number)
print(>>a_number)

# output
2                   # binary: 0000 0010
31                  # binary: 0001 1111
29                  # binary: 0001 1101
-11                 # binary: 1111 0101
2                   # binary: 0000 0010
40                  # binary: 0010 1000
```

___

Now that we now about data types, variables and operators, we might need a lot of things in order to put all that to work.

One of those 'things' are **Control Structures**, which are used to modify the flow of execution of a certain code.

## Control Structures

There are two kinds of Control Structures:

* **Conditionals**, used to execute one or more statements if a condition is met.
  * If conditional
* **Loops**, which purpose is to repeat a statement a certain number of times or while a condition is met.
  * While loops
  * For loops
* **Exceptions**
  * Try...Except
  * Raise

## Conditionals

### If statement

The `if` statement is used to execute a bunch of code, or another, depending on the evaluation of a condition.

Syntax:

```python
if condition:
    # some code
```

Always remember that in Python we relay on indentation in order to define a scope on the code.

```python
a_number = 100
other_number = 55
if a_number > other_number:
    print('a_number is greater than other_number')

# output
a_number is greater than other_number
```

As we see `a_number > other_number` is the condition in the example. This can be everything that evaluates as a Boolean value `True` or `False`, or even a `truthy` or `falsy` value.

```python
if False:
    print('This is True')

# output (blank output)

```

Here we see that the condition is not met, or in this case is False, so the code indented under the if statement is not executed.

We might need to do one thing if true, and another if false.
For that we have `if...else` statements.

### If...else statement

Syntax:

```python
if condition:
    # some code
else:
    # some other code
```

Let's see an example of that.

```python
if False:
    print('This is True')
else:
    print('This is False')

# output
This is False
```

Very straightforward, right?
Ok, let's move on...

There is another way to write this code and that way is using one liners, ternary operators, or Conditional Expressions.

```python
if True: print('This is True') # if statement

print('This is True') if True else print('This is False') # if...else statement
```

>Note that we used one line instead of four in the last example and it look's nicer sometimes. But be careful!!! When the code is longer it might be easier to read in the traditional multiline way.

### Elif

We also have `elif` in tha case that we have a few different options in an if statement.

Here is the syntax:

```python
if first_condition:
    # some code
elif second_condition:
    # some other code
else:
    #another piece of code
```

Let's see an example:

```python
a_number = -10

if a_number > 0:
    print('The number is positive')
elif a_number < 0:
    print('The number is negative')
else:
    print('The number is zero')

print("Positive") if a_number > 0 else print("Negative") if a_number < 0 else print("Zero") # one liner

print(f'The number is {'positive' if a_number > 0 else 'negative' if a_number < 0 else 'zero'}') # another one line solution
```

Remember that the `condition` in an if statement, can be as small or extended as we need. This means that can be a simple **boolean**, a condition with two values and a operator, or multiple values and operators.

```python
if True:
    pass

if a > b:
    pass

if a > b and b > c or b == c:
    pass
```

>Note that we used the `pass` reserved word, to express that this part of the code has no code to execute. This also avoid an error to be raised.

In Python there is not such thing as a Switch/Case, so you'll have to use the complete if statement.

**Wait!** (Update)

In Python 3.10+ we have Switch/Case statement, but it's called Match/Case
Let's see some examples.

In the past we could have done this:

```python
http_code = "418"

if http_code == "418":
    print("OK")
    do_something()
elif http_code == "404":
    print("Not Found")
    do_something()
elif http_code == "418"
    print("I'm a teapot")
    do_something()
else:
    print("Code not found")
    do_something_else()
```

Now, we can do this with Match/Case. so let's...

```python
http_code = "418"

match http_code:
    case "418":
        print("OK")
        do_something()
    case "404":
        print("Not Found")
        do_something()
    case "418":
        print("I'm a teapot")
        do_something()
    case _:
        print("Code not found")
        do_something_else()
```

It is pretty much the same, but some people find it more neat to use it this way... I mean, they must have added Match/Case statement for some reason! :D

Note in the last case of the statement the use of '_'.

Not only for this notation. '_' kind of means "something else".

The following peace of code, is used to get only the first element of the tuple, disregarding the second element.

```python
first, _ = ("first_string","second_string")
```

This piece of code is for the purpose of ignoring everything but the first element, since whe are not assigning the second element.

Another use case is this...

```python
# x = ('www.hola.com', 25)          # the output would be: http mode
# x = ("www.hola.com", 21, "ftp")   # the output would be: ftp mode

match x:
    case host, port:
        print('http mode')
    case host, port, mode:
        print(f'{ mode } mode')
```

In this case, the unreferenced names (host, port, mode) would become variables if an unpacking operation is able to be performed.
This show us how to use Match/Case to check the type and structure of our subject.
If you want to learn more about the `match` instruction, you can head over [here](https://peps.python.org/pep-0636/) to go into the rabit hole. (don´t come back later saying you were not warned :D)

## Loops

### While Loop

The While loop is used to perform an action, or a bunch of code, as long as a condition is true.

Syntax:

```python
while condition:
    # some code
```

For example...

```python
a_number = 1
while a_number < 10:
    print(a_number)
    a_number += 1

# output
1
2
3
4
5
6
7
8
9
```

>Note that we need to increment `a_number`, otherwise the loop will continue for ever.

We have two reserved words that we can use inside a While loop. These are `break` and `continue`.

With `continue` we continue with the next iteration of the look.

Let's see an example.

```python
a_number = 0
while a_number < 10:
    a_number += 1
    if a_number == 5:
        continue
    print(a_number)

# output
1
2
3
4
6
7
8
9
10
```

>Note that the `5`was not printed, as we have the continue statement, that "jumps" to the next iteration.

With `break` in the other hand, stops the loop, right where it's executed.

```python
a_number = 1
while a_number < 10:
    if a_number == 5:
        break
    print(a_number)
    a_number += 1

# output
1
2
3
4
```

>This code doesn't make much sense, but let's just take this as an example, and something we shouldn't do... :D

In order to complete the While loop syntax, we should include the `else` statement.

This will be executed when the condition is not met.

Let's take a look at it...

```python
a_number = 1
while a_number < 10:
    print(a_number)
    a_number += 1
else:
    print('No longer less than 10...')

# output
1
2
3
4
5
6
7
8
9
No longer less than 10...
```

### For Loop

The For loop is use to iterate over a sequence. As we saw we know the lists, tuples, sets, dictionaries are sequences... even a string is one.

So, we can do *something* with every item of a sequence.

Syntax:

```python
for item in sequence:
    # some code
```

An example...

```python
bands = ['Pearl Jam', 'Faith No More', 'Soundgarden']
for band in bands:
    print(band)

# output
Pearl Jam
Faith No More
Soundgarden
```

With For loops we also have `break` and `continue` reserved words, and even the `else` statement.

We said that we can iterate over a string, right? Let's see that.

```python
for char in 'Soundgarden':
    print(char)

# output
S
o
u
n
d
g
a
r
d
e
n
```

Let's say that we can print the first 10 numbers... We don't have to create a list of numbers first, in order to iterate over it. We can do it this way...

```python
for number in range(10):
    print(number)

# output
0
1
2
3
4
5
6
7
8
9
```

The built-in `range()` function, creates a sequence of numbers from 0 (default value) to the number before a specified number, incrementing by 1 (default value).

A quick peak into range examples...

```python
print(*range(5))

# output
0 1 2 3 4

print(*range(2,5))

# output
2 3 4

print(*range(2,5,2))
2 4
```

>Note the '*' before the range() function? It's not a typo! This is used to unpack a sequence

Just like in slicing, we can reverse a range...

```python
print(*range(5, 0, -1))

# output
5 4 3 2 1
```

Now we know about Lists and For loops, we can return to lists comprehension, something that we took a look at [day 3](day_3.md#list-comprehension).

I think we are now tying loose ends, right?

We've seen this, for instance...

```python
even_numbers = [x for x in range(20) if x % 2 == 0]
print(even_numbers)

# output
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

Here we have, besides a list, a for loop and an if statement.

Putting it into words it would be **"we have x for every x, from 0 to 19 (range(20)), that the modulus is 0"** or to be simpler, **"a list of even numbers between 0 and 19"**. *Let's save for another day if 0 is even, odd or none of the above...*

>Note: remember that modulus is the remainder of a division, after one number is divided by another.

We'll see that the previous expression is equivalent to this...

```python
even_numbers = []

for x in range(20):
    if x % 2 == 0:
        even_numbers.append(x)

print(even_numbers)

# output
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

What if we want every item in that list multiplied by 2?

Let's do it both ways...

```python
even_numbers = []

for x in range(20):
    if x % 2 == 0:
        even_numbers.append(x * 2)

print(even_numbers)

# output
[0, 4, 8, 12, 16, 20, 24, 28, 32, 36]
```

So, what do you think we should do to get the same result, using list comprehension?
Take a minute a think about it...

59... 58... 57... 56... Just kidding!!! :D

```python
even_numbers = [x * 2 for x in range(20) if x % 2 == 0]
print(even_numbers)

# output
[0, 4, 8, 12, 16, 20, 24, 28, 32, 36]
```

This can be used in loads of scenarios, so keep it on your cheat-sheet!!!

## Exceptions

### Try...Except

When Python finds a problem in the execution, the interpreter stops and generates an error.

These are called **Exceptions**.

There are many built-in types of Exceptions, like NameError, ArithmeticError, AttributeError, FloatingPointError, ImportError, ModuleNotFoundError, etc.

Let's see an example.

```python
print(x)
print('The code continues...')

Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
```

Another....

```python
print(10 / 0)
print('The code continues...')

Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

So, we might want to **catch** that exception in order to avoid stopping the program's execution.

We can do this, using the **try...except** statement.

```python
try:
    print(10 / 0)
except:
    print('An exception occurred')

print('The code continues...')

# output
An exception occurred
The code continues...
```

This way, the exception is caught, an error is shown but the code keeps running. The idea is to include the block of code that can fail, in the try statement.

As many different errors can occur, we can catch different types of exceptions. For example:

```python
x = 0

try:
    print(10 / x)
except ZeroDivisionError:
    print('You can not divide by zero')
except NameError:
    print('x is not defined')
except:
    print('An exception occurred')

# output
You can not divide by zero
```

But what if we comment the first line? Let's see...

```python
# x = 0

try:
    print(10 / x)
except ZeroDivisionError:
    print('You can not divide by zero')
except NameError:
    print('x is not defined')
except:
    print('An exception occurred')

# output
x is not defined
```

We can see, that we see different messages, depending the type of exception that is raised.

>Keep in mind that we need to order the exceptions from most to least specific, otherwise the more generic exception block will be executed and the code will never reach the more specific error type.

We have also an **else** block, that lets you execute a code if there is no error.

```python
x = 1

try:
    print(10 / x)
except:
    print('An exception occurred')
else:
    print('There was no error')

print('The code continues...')

# output
10
There was no error
The code continues...
```

The difference with the last line, is that this line will always be executed.

There is also a **finally** block, that lets you execute a code, no matter the result the try block.

It's most commonly used to close connections or free resources in an ordered fashion.

```python
x = 1

try:
    print(10 / x)
except:
    print('An exception occurred')
else:
    print('There was no error')
finally:
    print('The code continues...')

# output
There was no error
The code continues...
```

More details on finally [here](finally.md)

We can also create a custom exception and raise it. This is used to raise an exception and stop the execution on the code.

```python
X = 0

if x == 0:
    raise Exception('We don`t want the value of x to be zero!')

# output
Traceback (most recent call last):
    File "<stdin>", line 2, in <module>
Exception: We don`t want the value of x to be zero!
```

We can see the last line of the exception, with the description we have created.

___

[Go to Day 5](day_5.md)

___
