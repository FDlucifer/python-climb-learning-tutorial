import sympy
import math
from sympy import symbols, factor, expand, diff, integrate, limit, oo, Eq, solve, dsolve

print(math.sqrt(15))
print(sympy.sqrt(15))

x = symbols("x")
y = symbols("y")
t = symbols("t")

expression = 2 * (x + y)

print(expression)
print(expression - y)
print(factor(expression))
print(expand(expression))

formula = x ** 2
print(diff(formula))
print(diff(sympy.exp(x)))
print(diff(sympy.sin(x) + sympy.cos(x)))
print(integrate((formula)))
print(integrate(sympy.sin(x), (x, -oo, oo)))
print(limit(x,x,0))
print(limit(sympy.sin(x)/x,x,0))

print(solve(2 * x + x + 5))
print(solve(Eq(x ** 2, 16)))
print(solve(Eq(x ** 17, 15)))

