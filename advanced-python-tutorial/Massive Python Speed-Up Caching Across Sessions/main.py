import os
import time
import pickle
from functools import lru_cache, wraps


def exportable_cache(func):
    func.cache = {}
    if os.path.exists("factorial_cache.pkl"):
        with open("factorial_cache.pkl", "rb") as f:
            func.cache = pickle.load(f)

    @wraps(func)
    def wrapper(*args):
        if args in func.cache.keys():
            return func.cache[args]
        else:
            result = func(*args)
            func.cache[args] = result
            return result

    return wrapper


# @lru_cache(maxsize=None)
@exportable_cache
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


start = time.perf_counter()
for x in range(20000, 20100):
    factorial(x)
end = time.perf_counter()

print(end - start)

with open("factorial_cache.pkl", "wb") as f:
    pickle.dump(factorial.cache, f)
