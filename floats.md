# 0.1 + 0.2 == 0.3 results in True or False?

Here is where it gets weird...

The answer is False!!! Although yes, this is counterintuitive.

Here is why:

```python
a = 0.1
b = 0.2
c = a + b
print(c == 3)
# output
False


print(c)

# output
0.30000000000000004

# solution
round(a + b, 10) == round(.3, 10)
```

Recommendation:
Using the "decimal" library

```python
from decimal import Decimal
a = Decimal('0.1')
b = Decimal('0.2')
c = Decimal(a + b)
print(c == Decimal('0.3'))
# output
True

print(c)

# output
Decimal('0.3')
```

> notice the quotes in the parameter, otherwhise the number would be cast to float, with it´s precision issues, as you could see in the following article.

Go here for a deeper dive on the topic:

<https://www.laac.dev/blog/float-vs-decimal-python/>
