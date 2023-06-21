# 0.1 + 0.2 == 0.3 es True o False?

Aca es donde se pone raro...

La respuesta a esto es False!!! Aunque si, es contraintuitivo.

Explico por qué:

```python
a = 0.1
b = 0.2
c = a + b
print(c == 3)
#output
False


print(c)

#output
0.30000000000000004

#solución
round(a + b, 10) == round(.3, 10)
```

Recomendación:
usar la libreria "decimal"

```python
from decimal import Decimal
a = Decimal('0.1')
b = Decimal('0.2')
c = Decimal(a + b)
print(c == Decimal('0.3'))
#output
True

print(c)

#output
Decimal('0.3')
```

> las comillas como parametro son porque si no existieran, estariamos casteando a decimal el float, con sus respectivos decimales, como verán en el siguiente articulo.

Acá  articulo explicativo

<https://www.laac.dev/blog/float-vs-decimal-python/>
