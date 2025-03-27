# [A walk in Python](/README.md)

## Day 3

* Data Types
  * [Strings](day_3.md#strings)
  * [Numeric Types](day_3.md#numeric-types)
  * [Booleans](day_3.md#booleans)
* [Collections](day_3.md#collections)
  * [Lists](day_3.md#lists)
  * [Tuples](day_3.md#tuples)
  * [Sets](day_3.md#sets)
  * [Dictionaries](day_3.md#dictionaries)

## **Data Types**

___

Let's dive in Python Data Types!!!!

## Strings

A string is assignable to a variable like any other type of value. You can do that this way:

```python
greeting = 'Hello World!'
print(greeting)

#output
Hello World!
```

There is a way to assign a multiline string to a variable by using three quotes. You can do that this way:

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

>Note that the line breaks are in the same place that in the code.

As we said Strings are a list of characters, but there is not a type Char in Python. This would be a string with length equal to 1.

As Strings are list of characters, we can access them by their position:

```python
greeting = 'Hello World!'
print(greeting[1])

#output
e
```

We can also iterate through them:

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

### Slicing strings

Keeping in mind what we saw, we can extract or return a part of the string (or a list for that matter...)
This is called ***slicing***.

Let's say that I want to print parts (or substrings) of the greeting variable.
We will have to use this syntax:

{var_name}[{start}:{end}:{step}]

* start by default is 0, the start of the string.

* end by default is the length of the string.

* step by default is 1.

We can use positive and negative indexes.

Positives count from the start and negative count form the end of the string.

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

For example:

```python
greeting = 'Hello cruel World!'
print(greeting.upper())

# output
HELLO CRUEL WORLD!

print(greeting.replace('H', 'J'))

# output
Jello cruel World!
```

Another thing you can do with strings is to concatenate them. You can concatenate two or more strings, but if you try to concatenate a string with something else, you will get a TypeError.

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

We can see age's type is int, right?
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

## Numeric Types

Numeric types in general are pretty much self explanatory.

That's why I will show you some examples.

### Integers

```python
a = 0
b = 121651351
c = -63546010

print(type(a)) # or b or c with the same output

# output
<class 'int'>
```

### Floats

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

There is something on how floats are interpreted in Python that can be a litle tricky.

See [Floats and decimals](floats.md)

### Complex

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

## Booleans

As you might know, boolean values are one of two... True and False

Boolean types are used to evaluate expressions. So, if we compare to values, using a logical operator, we get a boolean response.

Let's see that with an example

```python
print(1 < 10)
print(1 == 10)
print(1 > 10)

# output
True
False
False
```

'If' statements use booleans to continue with one part of the code or the other but we'll see that later...

But at this point I feel the need to introduce **Truthy** and **Falsy** values.
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

We can see on the examples that some values are Truthy and some are Falsy.
In general terms values that are 0 or empty strings, empty sets or empty lists, are Falsy.

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

There are 4 types of collections in Python:

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
  * mutable (*but elements must be of an immutable type*)
  * no duplicates
* Dictionaries
  * ordered (*in python <3.6 are unordered*)
  * mutable
  * no duplicates **keys**

## Lists

When you need to store multiple values on one variable, maybe you'll use a **List**.

Lists are ordered, mutable, and allow repeated items. Keep in mind that Python is zero based, this means that indexes start at 0.

```python
one_list = ['Pearl jam', 'guitar', 10, True]
```

As we see up here, we can store different types of values.

Just as strings (we said that a string is kinda like a character list) we can get one item, get the length of the list, and many other things

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

Another way to create a list is using the list constructor.

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

And also, you can change a range of items

```python
a_list = ['Pearl jam', 'guitar', 10, True]
a_list[1:3] = ['bass', 23]
print(a_list)

# output
['Pearl jam', 'bass', 23, True]
```

There are more options to change a range of items. You can read about them [here](https://www.w3schools.com/python/python_lists_change.asp).

The way to join two lists, is this...

```python
first_list = ['Perl Jam', 'guitar']
second_list = [10, True]
a_list = first_list + second_list

# output
['Pearl jam', 'guitar', 10, True]
```

By the way, [here](https://www.w3schools.com/python/python_lists_methods.asp) is the list of lists methods, which are many and pretty self explanatory.

As we saw yesterday, we con *unpack* a list. Let's see some examples of it.

```python
a_list = ['Pearl jam', 'guitar', 10, True]
first, second, third, fourth = a_list

print(first)
print(second)
print(third)
print(fourth)

# output
Pearl jam
guitar
10
True
```

or we can do this...

```python
a_list = ['Pearl jam', 'guitar', 10, True]
first, second, *third = a_list

print(first)
print(second)
print(third)

# output
Pearl jam
guitar
[10, True]
```

>Note that with the '*' we can unpack the final items in one variable, creating a list.

### List Comprehension

As many of us saw when we were children, there is more than one way to create a set, or in this case a list. By extension and by comprehension.
We have covered the first one. Now let's see the second.

Here is the syntax:

```python
newlist = [expression for item in iterable if condition == True]
```

And an example:

```python
even_numbers = [x for x in range(20) if x % 2 == 0]
print(even_numbers)

# output
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

I know, we haven't seen loops and operators yet, but we will... Be patient! :D

So bare with me... we'll circle back to this.

## Tuples

Just like lists, tuples are intended to store multiple values in one variable, with the difference that tuples are **immutable**. This means that cannot be changed.

```python
a_tuple = ('Pearl jam', 'guitar', 10, True)
another_tuple = 'Alice in chains', 'guitar', 90, False
 ```

>Note than () can be omitted, but not the commas.
Try getting the type of both these variables and see what happens...

Actually, to create a tuple with one element we need to do it this way:

```python
a_tuple = ('Pearl jam',)
another_tuple = 'Alice in chains',
 ```

*Note: the comma at the end of the tuple. It's not a typo!!!*.

Like with lists, we can use a constructor to create a tuple.

```python
a_tuple = tuple(('Pearl jam', 'guitar', 10, True)) 
```

We can access a tuples item, just like with lists, using an index, negative index, a range, etc.

```python
a_tuple = ('Pearl jam', 'guitar', 10, True)
print(a_tuple[1]) # using index

# output
guitar
```

Now, what happens if we try to change an item of a tuple? Right, we can't!!!

We said before that tuples are immutable. Let's see what happens...

```python
a_tuple = ('Pearl jam', 'guitar', 10, True)
a_tuple[1] = 'bass'

# output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

We have to keep in mind that for some reason, we chose to create a tuple and not a list.

Having said that, if you need to change an item of a tuple, we have to cast it to a list and then the cast it back to a tuple.

```python
a_tuple = ('Pearl jam', 'guitar', 10, True)
a_list = list(a_tuple)
a_list[1] = 'bass'
a_tuple = tuple(a_list)
```

I'd recommend to thing thoroughly about which type of data we need in our code. We can do the same workaround in order to remove an item.

We can join two tuples using the '+' operator, just like we can do with lists.

[Here](https://www.w3schools.com/python/python_tuples_methods.asp) is the list of tuples methods, which are many and pretty self explanatory.

Do you remember how to **unpack** a List?
Cool, we can do exactly the same thing with a tuple.

## Sets

Just like lists and tuples, sets are intended to store multiple values in one variable, with the difference that sets are **unordered, no duplicates allowed and the items must be immutable**.

```python
a_set = {'Pearl jam', 'guitar', 10, True}
print(a_set)

# output
{'guitar', True, 10, 'Pearl jam'}
 ```

There we can see why we said that sets are unordered. The main thing is that multiple items in the same variable.

As sets are unordered group of items, we can **NOT** access them by index.
You can use the operator 'in' to see if an item is contained in the set, like this:

```python
a_set = {'Pearl jam', 'guitar', 10, True}
print('guitar' in a_set)

# output
True
```

Because of the same thing, you can't change an item of a set. But you have methods to remove and add a new one.

Another characteristic is that sets don't allow duplicates.

```python
a_set = {'Pearl jam', 'guitar', 10, True, 'guitar'}
print(a_set)

# output
{'guitar', True, 10, 'Pearl jam'}

a_set.add(10)
print(a_set)

# output
{'guitar', 10, True, 'Pearl jam'}
```

>Note that over and over we have the same result, or the same set if you will.

Let's try to add an immutable item to the set.

```python
a_set = {'Pearl jam', 'guitar', 10, True}
a_set.add(['Eddie', 'Mike'])

# output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

That's because, as was mentioned, sets only admit immutable item. Of course a list, is not an immutable item.

Another way to create a set is using the set constructor.

```python
a_set = set(('Pearl jam', 'guitar', 10, True))
```

Using this constructor is also the way to cast, for example, a tuple to a set.

```python
a_tuple = ('Pearl jam', 'guitar', 10, True)
a_set = set(a_set)
```

This might be used, for example, to eliminate repeated items on a list, instead of iterating the list, and checking if the item is already on the list.
Let's see that.

```python
a_list = ['Pearl jam', 'guitar', 10, True, 'guitar']
a_list = list(set(a_list))
```

In the case of the set, we can't use '+', to join to sets. But there are a few ways to do that.

```python
a_set = {'Pearl jam', 'guitar'}
another_set = {10, True}

print(a_set.union(another_set))

# output
{'guitar', True, 10, 'Pearl jam'}

print(a_set.update(another_set))

# output
{'guitar', True, 10, 'Pearl jam'}
```

By the way, [here](https://www.w3schools.com/python/python_sets_methods.asp) is the list of sets methods, which are many and pretty self explanatory.

## Dictionaries

Dictionaries are used to store data values in key:value pairs.
The key name of a dictionary must be always of an immutable type (string, boolean, int, float, complex, tuple, frozenset). If it is a collection (tuple, frozenset), all elements inside must also be immutable.


```python
a_dict = {
  'band': 'Pearl Jam',
  'instrument': 'guitar',
  'album': 10,
  'best_band': True
}
```

We can access a dictionaries item, using the key name between brackets.

```python
print(a_dict['band'])

# output
Pearl Jam
```

Seeing how you can access a dicts item, I think you could guess why dicts don't allow duplicate keys. Just to state the obvious, if there were two equal keys, how could Python realize which one you want to access?

There is another way to access a dicts item, that can be better to use in some scenarios, and is using the *get* method.

```python
print(a_dict['band'])

# output
Pearl Jam

print(a_dict.get('band'))

# output
Pearl Jam
```

What's the difference??? Well, using the *get* method, if you try to access an item which key doesn't exists, the returned value will be None, instead of an Exception.

```python
print(a_dict['drummer'])

# output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'drummer'

print(a_dict.get('drummer'))

# output
None
```

As easy as you can access an item, you can change an item.

```python
a_dict['instrument'] = 'bass' # or a_dict.update({'instrument': 'bass'})
print(a_dict)

# output
{
  'band': 'Pearl Jam',
  'instrument': 'bass',
  'album': 10,
  'best_band': True
}
```

In order to add an item to a dict, you can use the same syntax you use to change an item.

```python
a_dict['singer'] = 'Eddie Vedder' # or a_dict.update({'singer': 'Eddie Vedder'})
print(a_dict)

# output
{
  'band': 'Pearl Jam',
  'instrument': 'guitar',
  'album': 10,
  'best_band': True,
  'singer': 'Eddie Vedder'
}
```

There are also two important methods in order to know a dicts content.
One is *keys* and the other is *values*.

Let's see...

```python
print(a_dict.keys())
print(a_dict.values())

# output
dict_keys(['band', 'instrument', 'album', 'best_band'])
dict_values(['Pearl Jam', 'guitar', 10, True])
```

By the way, [here](https://www.w3schools.com/python/python_dictionaries_methods.asp) is the list of dicts methods, which are many and pretty self explanatory.

More about mutable vs immutable types [here|https://www.pythontutorial.net/advanced-python/python-mutable-and-immutable/]
___

[Go to Day 4](day_4.md)

___
