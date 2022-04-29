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
        super().__init__()
        print(f'I am a Son and I have both last names')


me = Son()
print(Son.mro())
print(Son.__mro__)
