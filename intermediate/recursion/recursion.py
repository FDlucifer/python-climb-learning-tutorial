n = 8

fact = 1
while n > 0:
    fact = fact * n
    n -= 1

print(fact)

def factorial(n):
    if n < 1:
        return 1
    else:
        number = n * factorial(n-1)
        return number

print(factorial(7))