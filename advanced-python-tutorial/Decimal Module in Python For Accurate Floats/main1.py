import decimal
from decimal import Decimal, getcontext, Context

new_context = Context(prec=2, rounding=decimal.ROUND_UP)
decimal.setcontext(new_context)
getcontext().traps[decimal.DivisionByZero] = False

print(Decimal(0.1234) + Decimal(0.5678))
print(Decimal(5) + Decimal(0))

import math

print(math.sqrt(0.3))
print(Decimal(0.3).log10())

a = Decimal(0.3)
print(a)
print(a.quantize(Decimal('0.000'), decimal.ROUND_UP))

