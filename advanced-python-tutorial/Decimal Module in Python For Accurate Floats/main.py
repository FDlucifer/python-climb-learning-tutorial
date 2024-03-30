from decimal import Decimal, getcontext

print(1+2 == 3)
print(0.1+0.2 == 0.3)
print(0.2+0.2 == 0.4)
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
print(getcontext())

getcontext().prec = 6

a = Decimal(0.1) + Decimal(0.2)
b = Decimal(0.3)

print(float(a) == float(b))