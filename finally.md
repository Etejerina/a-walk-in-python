Finally executes even if there is a return statement in the try block!

```python
def foo():
    try:
        global bar
        bar = 0
        raise Exception()
    except:
        bar = 1
        return bar
    finally:
        bar = 2

print(foo())
print(bar)

# output
1
2
```

And if there is also a return in the finally block, that is the one that is returned:

```python
def foo():
    try:
        global bar
        bar = 0
        raise Exception()
    except:
        bar = 1
        print(bar)
        return bar
    finally:
        bar = 2
        print(bar)
        return bar

b = foo()
print(f"{b=}")

# output
1
2
b=2
```
>Notice the pattern {<variable_name>=} in the f-string, it prints the name of the variable, "=", and then the value

For -way- more in-depth details, you can go to the oficial tutorials [here](https://docs.python.org/3/tutorial/errors.html#defining-clean-up-actions)
