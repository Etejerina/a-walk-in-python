# [A walk in Python](/README.md)

## Day 4

* Operators
  * [Built-in Data Types](day_2.md#data-types)

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
|---|---|
| + | addition
| - | substraction
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
|---|---|
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
|---|---|
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
|---|---|
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
|---|---|
| in | Returns True if a sequence with the specified value is present in the object
| not in | Returns True if a sequence with the specified value is not present in the object

```python
original_bands = ['Faith No More', 'Soudgarden']
print('Bush' in original_bands)
print('ABBA' not in original_bands)

# output
False
True
```

## Bitwise operators

These are use to operate bit by bit, and act on operands as if they were strings of binary digits.

| Operator | Name | Description
|---|---|---|
| & | AND | Sets each bit to 1 if both bits are 1
| \| | OR | Sets each bit to 1 if one of two bits is 1
| ^ | XOR | Sets each bit to 1 if only one of two bits is 1
| ~ | NOT | Inverts all the bits
| << | Zero fill left | Shift left by pushing zeros in from the right and let the leftmost bits fall off
| >> | Signed right | Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off.

```python
a_number = 10       # en binario 0000 1010
another_number = 23 # en binario 0001 0111 

print(a_number & another_number)
print(a_number | another_number)
print(a_number ^ another_number)
print(~a_number)
print(<<a_number)
print(>>a_number)

# output
2   # en binario 0000 0010
31  # en binario 0001 1111
29  # en binario 0001 1101 
-11 # en binario 1111 0101
2   # en binario 0000 0010
40  # en binario 0010 1000
```

___

Now that we now about data types, variables and operators, we might need a lot of things in order to put all that to work.

One of those 'things' are **Control Structures**, wich are used to modify the flow of execution of a certain code.

## Control Structures

There are two kinds of Control Structures:

* **Conditionals**, used to execute one or more statements if a condition is met.
* **Loops**, which purpose is to repeat a statement a certain number of times or while a condition is met.

### If statement

The If statement is used to execute a bunch of code, or another, depending on the evaluation of a condition.

Sintax:

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
a_number is bigger than other_number
```

As we see `a_number > other_number` ois the condition in the example. This can be everything that evañluates as a Boolean value `True` or `False`, or even a `truthy` or `falsy` value.

```python
if False:
    print('This is True')

# output (blank output)

```

Here we see that the condition is not met, or in this case is False, so the code indented under the if statement is not executed.

We might need to do one thing if true, and another if false.
For that we have `If...else` statementes.

### If...else statement

Sintax:

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

There is another way to write this code and that way is using one liners or one line statements.

```python
if True: print('This is True') # if statemente

print('This is True') if True else print('This is False') # if...else statement

```

>Note that we used one line instead of four in the last example and it look's nicer sometimes. But be careful!!! When the code is longer it might be easier to read in the traditional multiline way.
