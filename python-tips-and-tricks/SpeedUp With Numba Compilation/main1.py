from numba import jit
import random
import math
import time
import numpy as np

@jit(nopython=True)
def some_function(n):
    z = np.zeros((n,n))
    for i in range(n):
        x = np.random.rand(n, n)
        y = np.random.rand(n, n)
        z += np.sqrt(x ** 2 + y ** 2)
    return z

start = time.time()
some_function(100)
end = time.time()
print(end - start)

start = time.time()
some_function(100)
end = time.time()
print(end - start)