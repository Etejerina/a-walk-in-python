def factorial(number):
    return 1 if number == 1 else number * factorial(number - 1)

print(factorial(6))