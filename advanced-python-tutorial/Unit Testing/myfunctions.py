import math

def multiply_with_loop_imperfect(x, y):
    return sum(y for _ in range(x))

def multiply_with_loop_better(x, y):
    if (x >= 0 and y >= 0) or (x < 0 and y < 0):
        return sum(abs(y) for _ in range(abs(x)))
    elif x < 0:
        return sum(x for _ in range(y))
    else:
        return sum(y for _ in range(x))

def length_of_integer(n):
    if type(n) is not int:
        raise TypeError("Invalid Type")
    add = 1 if n >= 0 else 2
    return int(math.floor(math.log10(n)) + add) if n != 0 else 1

print(length_of_integer(8912373021))
print(length_of_integer(12345))
print(length_of_integer(8907321))