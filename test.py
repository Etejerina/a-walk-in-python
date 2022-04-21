def n_times(times):
    return lambda n : n * times

doubler = n_times(2)
tripler = n_times(3)

print(doubler(10))
print(tripler(10))

n_times = lambda n, func: func(n)

print(n_times(10, lambda n : 2 * n))
print(n_times(10, lambda n : 3 * n))
