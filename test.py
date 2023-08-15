# def n_times(times):
#     return lambda n : n * times

# doubler = n_times(2)
# tripler = n_times(3)

# print(doubler(10))
# print(tripler(10))

# n_times = lambda n, func: func(n)

# print(n_times(10, lambda n : 2 * n))
# print(n_times(10, lambda n : 3 * n))

# def fibonacci(n, amount):
#     a = b = 1
#     result = []
#     for i in range(n):
#         result.append(a)
#         if len(result) == amount:
#             yield result
#             result = []
#         a, b = b, a + b

# gen = fibonacci(50000, 50)
# print(next(gen))
# print(next(gen))


# def wrapper_function(func):

#     def inner_function():
#         print('Printing before function!')
#         func()
#         print('Printing after function!')

#     return inner_function()

# def a_function():
#     print('I`m the function!')

# wrapping = wrapper_function(a_function)


# def wrapper_function(func):

#     def inner_function():
#         print('Printing before function!')
#         func()
#         print('Printing after function!')

#     return inner_function

# @wrapper_function
# def a_function():
#     print('I`m the function')

# a_function()

# class Father:
#     '''
#     This is a person class and have name in it.
#     '''

#     def __repr__(self):
#         return 'This is a the Father class'

# class Mother:
#     '''
#     This is a person class and have name in it.
#     '''

#     def __init__(self):
#         print(f'Mothers last name')


# class Son(Father, Mother):
#     "This is a child class from Mother and Father"
#     isSon = True

#     def __init__(self):
#         super().__init__()
#         print(f'I am a Son and I have both last names')

# somebody = Father()
# print(Son)

# class Person:
#     '''
#     This is a person class and have name in it.
#     '''

#     def __init__(self, name):
#         self.name = name

#     # def __repr__(self):
#     #     return f'I am of class Person and my name is {self.name}'

# me = Person('Ezequiel')
# another_guy = Person('Nicolas')
# print(me)
# print(another_guy)


# number = int | float

# def a_function() -> number:
#     return 1


# a_number = 1
# while a_number < 10:
#     print(a_number)
#     a_number += 1
# else:
#     print('No longer less than 10...')


# class Person:
#     def __init__(self):
#         print(f"Im Person")


# class Father(Person):
#     """
#     This is a person class and have name in it.
#     """

#     def __init__(self):
#         print(f"Fathers last name")


# class Mother:
#     """
#     This is a person class and have name in it.
#     """

#     def __init__(self):
#         print(f"Mothers last name")


# class Son(Father, Mother):
#     "This is a child class from Mother and Father"
#     __isSon = True

#     def __init__(self):
#         super().__init__()
#         print(f"I am a Son and I have both last names")


# print(dir(Son))


# class Person:
#     def __init__(self, nombre):
#         self.nombre = nombre
#         self.__password = "estoEsUnaPass"

#     @property
#     def password(self):
#         return self.__password

#     @password.setter
#     def password(self, password):
#         self.__password = password


# yo = Person("Eze")
# print(yo.password)
# yo.password = "otra"
# print(yo.password)


class ClassB:
    def __init__(self):
        # Protected member
        self.__a = 2


an_instance = ClassB()

print("Accessing private member: ", an_instance.__a)
