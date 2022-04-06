# [A walk in Python](/README.md)

## Day 3

* Data Types
  * [Built-in Data Types](day_2.md#data-types)

## **Data Types**

___

## Data types in details

Let's dive in Python Data Types!!!!

## Text Type: ***str***

A string is assignable to a variable like any other type of value. You can do it that, this way:

```python
greeting = 'Hello World!'
print(greeting)

#output
Hello Wolrd!
```

There's a way to assign a multiline string to a variable by using three quotes. You can do that this way:

```python
blacks_chorus = """And now my bitter hands
Chafe beneath the clouds
Of what was everything
Oh the pictures have
All been washed in black
Tattooed everything"""

print(blacks_chorus)

#output

And now my bitter hands
Chafe beneath the clouds
Of what was everything
Oh the pictures have
All been washed in black
Tattooed everything
```

Note that the line breaks are in the same place that in the code.

As we said Strings are a list of character, but there is not a type Char in Python. This would be a string with length equal to 1.

As Strings are list of characters, we can access to them by their position:

```python
greeting = 'Hello World!'
print(greeting[1])

#output
e
```

We can alse iterate through them:

```python
greeting = 'Hello World!'
for c in greeting:
  print(c)

#output
H
e
l
l
o
 
W
o
r
l
d
!
```

Or apply operators...

```python
greeting = 'Hello World!'
print('Hello' in greeting)

#output
True
```

Or check the length of a string:

```python
greeting = 'Hello World!'
print(len(greeting))

#output
12
```

## Slicing strings

Keeping in mind what we saw, we can extract or return a part of the string (or a list for that matter...)
This is called ***slicing***.

Let's say i want to print parts (or substrings) of the greeting variable.
We will have to use this sintax:

{var_name}[{start}:{end}:{step}]

* start by default is 0, the start of the string.

* end by default is the ength of the string.

* step by default is 1.

We can use positive and negative indexes.

Positives count from the start anmd negative count form the end of the string.

```python
greeting = 'Hello cruel World!'
print(greeting[0:5]) # or print(greeting[:5])

#output
Hello

print(greeting[12:18]) # or print(greeting[12:])

#output
World!

print(greeting[6:11]) 

#output
cruel

print(greeting[0:-7]) # or print(greeting[:-7]) using negative index

#output
Hello cruel
```

In the case of the step parameter, it indicates the increment between each index for slicing.

```python
greeting = 'Hello cruel World!'
print(greeting[::]) # or print(greeting[0:18:1])

#output
Hello cruel World!

print(greeting[::2]) # or print(greeting[0:18:2])

#output
HloculWrd

print(greeting[::-1]) # or print(greeting[0:18:-1]) using negative index on step

#output
!dlroW leurc olleH

print(greeting[10:6:-1]) 

#output
leurc

print(greeting[::-2]) # or print(greeting[0:18:-2])

#output
!lo er le
```

**Remember!!!! Strings are immutable!!!**

So, we have a list of methods that returns a **modified copy** of the string, like *upper*, *lower*, *strip*, *replace*, etc.

You can see the complete list [here](https://www.w3schools.com/python/python_ref_string.asp).

For examnple:

```python
greeting = 'Hello cruel World!'
print(greeting.upper())

# output
HELLO CRUEL WORLD!

print(greeting.replace('H', 'J'))

# output
Jello cruel World!
```

Another thing you can do sith strings is concatenate them. But as I said, you can concatenate two strings, and not a string and something else.

For example:

```python
txt_1 = 'World!'
txt_0 = 'Hello ' 
print(txt_0 + txt_1)

# output
Hello World!

age = 46
txt = 'My age is ' 
print(txt + age)

# output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

We can see ages type is int, right?
So we can do various things. Let's see...

```python
age = 46
txt = 'My age is ' 
print(txt + str(age))

# output
My age is 46

txt = 'My age is {}' 
print(txt.format(age))

# output
My age is 46

name = 'Ezequiel'
txt = 'My age is {} and my name is {}' 
print(txt.format(age, name))

# output
My age is 46 and my name is Ezequiel

txt = 'My age is {1} and my name is {0}' 
print(txt.format(name, age))

# output
My age is 46 and my name is Ezequiel
```

Another way to do the exact same thing is with f-Strings:

```python
age = 46
print(f'My age is {age}')

# output
My age is 46

name = 'Ezequiel'
print(f'My age is {age} and my name is {name}')

# output
My age is 46 and my name is Ezequiel
```

## Numeric Types: ***int, float, complex***

Numeric typoes in general are pretty much self explanatory.

That's why I will show you some examples.

## Integers

```python
a = 0
b = 121651351
c = -63546010

print(type(a)) # or b or c with the same output

# output
<class 'int'>
```

## Floats

```python
a = 1.25
b = 1.0
c = -53.785

print(type(a)) # or b or c with the same output

# output
<class 'float'>
```

Floats can also be scientific numbers with an "e" to indicate the power of 10. For example:

```python
a = 35e3
b = 12E4
c = -87.7e10

print(a) 
print(b) 
print(c) 

# output
35000.0
120000.0
-877000000000.0
```

Complex are part of the numbers too.

These numbers are written with a "j" as the imaginary part:

```python
a = 3+5j
b = 5j
c = -5j

print(type(a)) # or b or c with the same output

# output
<class 'complex'>
```

Floats, ints and complex numbers can be casted using *int()*, *float()* or *complex()*.

**But!!!!** Complex cannot be casted to other types.

## Boolean Type: ***bool***

As you might know, boolean values are one of two... True and False

Boolean types are used to evaluate expressions. So, if we compare to values, using a logilcal operator, we get a boolean response.

Let's se that with an example

```python
print(1 < 10)
print(1 == 10)
print(1 > 10)

# output
True
False
False
```

If statements use booleans to continue with one part of the code or the other but we'll see that later...

But at this point I feel the need to intriduce **Truthy** and **Falsy** values.
These are non-boolean values that can count, or be evaluated, as True or False.

We can see that, when we try to cast some values...

```python
print(bool(15))
True
print(bool(-15))
True
print(bool(0))
False
print(bool('Hi!'))
True
print(bool(''))
False

```

We can see on the examples that some values are Trythy and some are Falsy.
In general terms values that are 0 or empty strngs, empty sets or empty lists, are Falsy.

Falsy Values
Sequences and Collections:

* Empty lists: []
* Empty tuples: ()
* Empty dictionaries: {}
* Empty sets: set()
* Empty strings: ""
* Empty ranges: range(0)

Numbers

* Zero of any numeric type.
  * Integer: 0
  * Float: 0.0
  * Complex: 0j

Constants

* None
* False

___

## Collections

There are 4 types of conllections in Python:

* Lists
  * ordered
  * mutable
  * allows duplicates
* Tuples
  * ordered
  * immutable
  * allows duplicates
* Sets
  * unordered
  * immutable
  * no duplicates
* Dictionaries
  * ordered (in python 3.6< are unordered)
  * mutable
  * no duplicates

## Lists

When you need to store multiple values on one variable, maybe you'll use a **List**.

Lists are ordered, mutable, and allow repeated items. Keep in mind that Python is zero based, this means that indexes start at 0.

```python
one_list = ['Pearl jam', 'guitar', 10, True]
```

As we see up here, we can store different types of values.

Just as strings (we sais that a string is kinda linke a chararcter list) we can get one item, get the length of the list, and many other things

```python
one_list = ['Pearl jam', 'guitar', 10, True]
print(one_list[1]) # using index

# output
guitar

print(one_list[-2]) # using negative index

# output
10

print(one_list[1:3]) # using slicing

# output
['guitar', 10]

print(len(one_list)) # length

# output
4
```

Another way to vreate a list is using the list constructor.

```python
a_list = list(('Pearl jam', 'guitar', 10, True))
```

Using this constructor is also the way to cast, for example, a tuple to a list.

```python
a_tuple = ('Pearl jam', 'guitar', 10, True)
a_list = list(a_tuple)
```

You can change a value on the list this way...

```python
a_list = ['Pearl jam', 'guitar', 10, True]
a_list[1] = 'bass'
print(a_list)

# output
['Pearl jam', 'bass', 10, True]
```

And also, yopu can change a range of items

```python
a_list = ['Pearl jam', 'guitar', 10, True]
a_list[1:3] = ['bass', 23]
print(a_list)

# output
['Pearl jam', 'bass', 23, True]
```
