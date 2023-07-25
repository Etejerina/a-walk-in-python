# [A walk in Python](/README.md)

## Day 6

* [Classes / Objects](day_6.md#classes--objects)
* [Inheritance](day_6.md#inheritance)
  * [Python super()](day_6.md#python-super)
* [Method Resolution Order (MRO)](day_6.md#method-resolution-order-mro)
* [Dunder Methods](day_6.md#dunder-methods)

## **Classes / Objects**

___

An object is simply a collection of data (variables) and methods (functions) that act on those data. Similarly, a class is a blueprint for that object. Creating a new class creates a new type of object, allowing new instances of that type to be made.

We an think of a **Class** as a prototype or blueprint of something.

Classes are dynamic as they are created at runtime, and can be modified further after creation.

Classes are, by convention, named using Pascal Case (PascalCase). This is naming the class with words, without using spaces or underscores and starting every word with a capitalize letter.

Syntax:

```python
class MyClass:
    '''This is a docstring. I have created a new class'''
    pass
```

> Note: It's also common and a good practice, to use a docstring as a description of the class.

A class has attributes and methods, as any other object we already used in Python. Remember that Python is a multi-paradigm language, but everything in Python is an object.

For example...

```python
class Person:
    '''
    This is a person class and have name in it.
    '''
    name = "Ezequiel"

    def say_hi(self):
        print(f'Hello, my name is {self.name}')


eze = Person() # instantiate an object or instance eze from the class Person

print(Person.name)
print(Person.say_hi)
print(eze.say_hi)
eze.say_hi()

# output
Ezequiel
<function Person.say_hi at 0x000001D2DCBC0670>
<bound method Person.say_hi of <__main__.Person object at 0x000001D2DCBADFD0>>
Hello, my name is Ezequiel
```

Maybe is too much for our first time... Let's review that!

We have a Person class to begin with... It has an attribute *name* and a method *say_hi*.

So in the example **eze** is an instance of the Person class, right? Well, I'm (almost) a Person... haha

So, if we print **Person.name** we can see the output is the name attribute with the value 'Ezequiel'.

In the next *print statement* we can see, as we said, tha *say_hi* is a function and when instantiated, is the method bound to the class method.

Finally, calling that method of the instance, we get to execute that function and print **'Hello, my name is Ezequiel'**

We can see, when defining the method *say_hi*, that there is parameter called **self**.
Self refers to each and every instance of that class.  Also we can see that when we called 'eze.say_hi()' in the example, we didn't pass an argument... What happened here??? There is one parameter declared but no argument passed! That's weird!

The answer to that question is that when we call a method, Python automatically includes as first argument the instance created. We could say that this is something like **'Person.say_hi(eze)'**

Can we change the name attribute in the instance?

```python
class Person:
    '''
    This is a person class and have name in it.
    '''
    name = "Ezequiel"

    def say_hi(self):
        print(f'Hello, my name is {self.name}')


eze = Person()
eze.name = 'Nicolas'
eze.say_hi()

#output
Hello, my name is Nicolas
```

Let's suppose that we don't want the instance to have a default name... we want to create a persons instance and set a name. For that we are going to need a special method.

For that we'll need to use the built-in **\_\_init__()** special method, which is always executed when the class is being initiated.

```python
class Person:
    '''
    This is a person class and have name in it. Now we can pass it to the __init__() special method!.
    '''

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print(f'Hello, my name is {self.name}')


a_person = Person('Nicolas')
a_person.say_hi()
print(a_person.__doc__)

# output
Hello, my name is Nicolas
This is a person class and have name in it. Now we can pass it to the __init__() special method !.
```

> Note: with the special attribute '\_\_doc__'  we can see the docstring of that class.

## Inheritance

*Inheritance* enable us to define a class that takes all the functionalities and attributes from a parent class and allows us to add more.

It refers to defining a new class with little or no modification to an existing class. The new class is called derived (or child) class and the one from which it inherits is called the base (or parent) class.

For example:

```python
class Person:
    '''
    This is a person class and have name in it.
    '''

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print(f'Hello, my name is {self.name}')


class Son(Person):
    "This is a child class from Person"
    isSon = True


my_father = Person('Pedro')
my_father.say_hi()
me = Son('Ezequiel')
me.say_hi()
print(me.isSon)

# output
Hello, my name is Pedro
Hello, my name is Ezequiel
True
```

We can see that the child class has the *say_hi()* method, inherited from the parent class Person. So we only add, in this case, one attribute (*isSon*).

We can also override a parent class method, like this.

```python
class Person:
    '''
    This is a person class and have name in it.
    '''

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print(f'Hello, my name is {self.name}')


class Son(Person):
    "This is a child class from Person"
    isSon = True

    def say_hi(self):
        print(f'Hello, I am a Son and my name is {self.name}')


my_father = Person('Pedro')
my_father.say_hi()
me = Son('Ezequiel')
me.say_hi()

# output
Hello, my name is Pedro
Hello, I am a Son and my name is Ezequiel
```

We can override all the methods from the parent class, including \_\_init__(), and all the other built-in, or dunder (preceded and succeeded by double underscores), methods.

We can also use methods from the parent class and add them some other actions.

### Python super()

The super function returns a temporary object of the parent class (superclass) that allows access to all of its methods to its child class.

Let's see it in action.

```python
class Person:
    '''
    This is a person class and have name in it.
    '''

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print(f'Hello, my name is {self.name}')


class Son(Person):
    "This is a child class from Person"
    isSon = True

    def say_hi(self):
        super().say_hi() # or Person.say_hi(self)
        print(f'I am a Son!')


my_father = Person('Pedro')
my_father.say_hi()
me = Son('Ezequiel')
me.say_hi()

# output
Hello, my name is Pedro
Hello, my name is Ezequiel # this in on the Son class, calling say_hi() from the parent class.
I am a Son
```

In Python we call inherit from more than one class. The child class will get all the methods and attributes from all the parent classes.

Let's see an example.

```python
class Father:
    '''
    This is a person class and have name in it.
    '''

    def __init__(self):
        print(f'Fathers last name')


class Mother:
    '''
    This is a person class and have name in it.
    '''

    def __init__(self):
        print(f'Mothers last name')


class Son(Father, Mother):
    "This is a child class from Mother and Father"
    isSon = True

    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)
        print(f'I am a Son and I have both last names')


me = Son()

# output
Fathers last name
Mothers last name
I am a Son and I have both last names
```

Here, in the child class, we are calling explicitly both parent classes init methods. Now, if we use the super function, Python will check, it will check first the method in the first parent class. If the method doesn't exists, i'll check the second parent class and so on (if there were more parent classes). This is called Method Resolution Order (**MRO**).

Let's see an example first.

```python
class Father:
    '''
    This is a person class and have name in it.
    '''

    def __init__(self):
        print(f'Fathers last name')


class Mother:
    '''
    This is a person class and have name in it.
    '''

    def __init__(self):
        print(f'Mothers last name')


class Son(Father, Mother):
    "This is a child class from Mother and Father"
    isSon = True

    def __init__(self):
        super().__init__(self)
        print(f'I am a Son and I have both last names')


me = Son()

# output
Fathers last name
I am a Son and I have both last names
```

## Method Resolution Order (**MRO**)

To keep it simple, it is the order in which a method is searched for in a classes hierarchy, as we saw above.

if we call that function with the last example, this is what will happen:

```python
print(Son.mro()) # or print(Son.__mro__)

# output
(<class '__main__.Son'>, <class '__main__.Father'>, <class '__main__.Mother'>, <class 'object'>)
```

There are far more complex scenarios, but you get the idea.

## Dunder Methods

Dunder Methods are the special methods that start and end with the double underscores. Dunder methods are not meant to be invoked directly by you, but the invocation happens internally from the class on a certain action.

For example, when you add two numbers using the + operator, internally, the \_\_add__() method will be called.

We can use the dir() function to see the number of dunder methods inherited by a class, but not only dunder methods but all methods.

Let's see an example with the classed defined above...

```python
print(dir(Father))

# output
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
```

As we know, everything is a class in Python, so we can run this...

```python
print(dir(int))

# output
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
```

Another example:

```python
print(dir(Son))

# output
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'isSon']
```

> Note at the end of the list, we can see the "isSon" method we have created!

We have also said that, if needed, we can override these methods. Actually, this is what many libraries do.

```python
class Person:
    '''
    This is a person class and have name in it.
    '''

    def __init__(self, name):
        self.name = name

me = Person('Ezequiel')
another_guy = Person('Nicolas')
print(me)
print(another_guy

# output
<__main__.Person object at 0x000001F95E1DDFD0>
<__main__.Person object at 0x000001F95E1DDD60>
```

In this output we can't tell which is which, so let's do something to get a more interesting output.

```python
class Person:
    '''
    This is a person class and have name in it.
    '''

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'I am of class Person and my name is {self.name}'

me = Person('Ezequiel')
another_guy = Person('Nicolas')
print(me)
print(another_guy)

# output
I am of class Person and my name is Ezequiel
I am of class Person and my name is Nicolas
```

___

[Go to Day 7](day_7.md)

___
