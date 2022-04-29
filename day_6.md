# [A walk in Python](/README.md)

## Day 5

* Classes / Objects

## **Classes / Objects**

___

An object is simply a collection of data (variables) and methods (functions) that act on those data. Similarly, a class is a blueprint for that object. Creating a new class creates a new type of object, allowing new instances of that type to be made.

We an think of a **Class** as a prototype or blueprint of something.

Classes are dynamic as they are created at runtime, and can be modified further after creation.

Classes are, by convention, named using Camel Case (camelCase). This is naming the class with words, without using spaces or underscores and starting every word with a capitalize letter.

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

Let's suppose that we don't want the instance to have a default name... we want to to create a persons instance and set a name. For that we are going to need a constructor.

For that we'll need to use the built-in **\_\_init__()** function, which is always executed when the class is being initiated.

```python
class Person:
    '''
    This is a person class and have name in it. Now we can pass it to the constructor!.
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
This is a person class and have name in it. Now we can pass it to the constructor!.
```

> Note: with the special attribute '\_\_doc__'  we can see the docstring of that class.

### inheritance

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
