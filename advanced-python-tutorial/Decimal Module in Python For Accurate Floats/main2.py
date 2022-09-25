import decimal
from decimal import Decimal, getcontext, Context

print(Decimal("Infinity") * (-1))
print(Decimal("NaN"))

print(list(map(Decimal, [0.1, 0.2, 0.3, 0.4])))

