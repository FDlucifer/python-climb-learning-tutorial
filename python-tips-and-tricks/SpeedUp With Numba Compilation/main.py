# pip install numba

from numba import jit
import random
import math
import time

@jit(nopython=True)
def some_function(n):
    z = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        z += math.sqrt(x ** 2 + y ** 2)
    return z

start = time.time()
some_function(10000000)
end = time.time()
print(end - start) # 6.500698089599609 s

start = time.time()
some_function(10000000)
end = time.time()
print(end - start) # 6.500698089599609 s

start = time.time()
some_function(10000000)
end = time.time()
print(end - start) # 6.500698089599609 s