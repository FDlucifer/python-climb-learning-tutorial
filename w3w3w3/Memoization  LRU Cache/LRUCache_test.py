
import time
from LRUCache import LRUCache

# Only setting this for testing purpose/testing file.
LRUCache.DEBUG = True # DEFAULTS to False. When True, will print Cached list per each result, and show in test file
                      # when result is cached etc... used for debugging/testing purposes only.

LRUCache.cache_limit = 3 # DEFAULTS to None. If None...There is no limit to the cach list. Setting to 3 in test file..
                          # for testing purposes.
  
@LRUCache
def ex_func_01(n):
    print(f'Computing...{n}x{n}')
    time.sleep(1)
    return n*n


@LRUCache
def ex_func_02(n):
    print(f'Computing...{n}x{n}')
    time.sleep(1)
    return n*n

print(f'\nFunction: ex_func_01')
print(ex_func_01(4)) # Cache: {(4,): 16}
print(ex_func_01(5)) # Cache: {(4,): 16, (5,): 25}
print(ex_func_01(4)) # Cache: {(5,): 25, (4,): 16}
print(ex_func_01(6)) # Cache: {(5,): 25, (4,): 16, (6,): 36}
print(ex_func_01(7)) # Cache: {(5,): 25, (4,): 16, (6,): 36, (7,): 49}
print(ex_func_01(8)) # Cache: {(4,): 16, (6,): 36, (7,): 49, (8,): 64}

print(f'\nFunction: ex_func_02')
print(ex_func_02(8)) # Cache: {(8,): 64}
print(ex_func_02(7)) # Cache: {(8,): 64, (7,): 49}
print(ex_func_02(6)) # Cache: {(8,): 64, (7,): 49, (6,): 36}
print(ex_func_02(4)) # Cache: {(8,): 64, (7,): 49, (6,): 36, (4,): 16}
print(ex_func_02(5)) # Cache: {(7,): 49, (6,): 36, (4,): 16, (5,): 25}
print(ex_func_02(4)) # Cache: {(7,): 49, (6,): 36, (5,): 25, (4,): 16}
