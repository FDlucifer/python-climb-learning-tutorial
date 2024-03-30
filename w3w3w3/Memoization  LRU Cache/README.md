# Python-LRU-Cache
*#python* *#python3* *#3* *#cache* *#caching* *#lru* *#lrucache* *#memoization* *#create* *#function* #*array* #*lists* #*linked*
*#doubly* *#chaining* *#lru* *#LRU* *#cached* *#cachette* *#cache* *#memoisaation* *#dict* *#wrapper* *#class* *#cache_limit*

Python implementation of Least Recently Used Cache (LRU Cache) using dict and linked list.

*Simple, Elegant, Lru Cache wrapper...*

## Description
This LRUCache code, will create a cache(dict) and a linked list per each *instance* eg. per each function the wrapper class is used on
like so..

```
LRUCache.cache_limit = 3 # Defaults to None.
 #Once cache > cache_limit, it then removes cached result from bottom, appends new result to top.

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
print(ex_func_01(4)) # Cache: {(4,): 16} <-- 4 is at top / only on here.
print(ex_func_01(5)) # Cache: {(4,): 16, (5,): 25} <-- 4 is at bottom with 5 at top
print(ex_func_01(4)) # Cache: {(5,): 25, (4,): 16} <-- 4 gets called from cache and gets moved to top again.
print(ex_func_01(6)) # Cache: {(5,): 25, (4,): 16, (6,): 36}
print(ex_func_01(7)) # Cache: {(5,): 25, (4,): 16, (6,): 36, (7,): 49} <-- cache limit reached.
print(ex_func_01(8)) # Cache: {(4,): 16, (6,): 36, (7,): 49, (8,): 64} <-- 5 is removed and 8 joins top

print(f'\nFunction: ex_func_02')
print(ex_func_02(8)) # Cache: {(8,): 64}
print(ex_func_02(7)) # Cache: {(8,): 64, (7,): 49}
print(ex_func_02(6)) # Cache: {(8,): 64, (7,): 49, (6,): 36}
print(ex_func_02(4)) # Cache: {(8,): 64, (7,): 49, (6,): 36, (4,): 16} <-- 4 on end + at cache limit. 1 over cache limit 3 = 4
print(ex_func_02(5)) # Cache: {(7,): 49, (6,): 36, (4,): 16, (5,): 25} <-- 8 gets removed and 5 joins the top
print(ex_func_02(4)) # Cache: {(7,): 49, (6,): 36, (5,): 25, (4,): 16} <-- 4 get called from cache and gets moved to top

```

* This cache will remove the least used(at the bottom) when the cache limit is reached or in this case is one over the cache limit.
* Each cache wrapper used is its own instance and has its own cache list and its own cache limit to fill.
* Cached results move to the top, if are called again.
* New results get added to the top
* keeping most recently used at the top for further use.

*Simple system.*

## To use
Put **LRUCache.py** file into the same directory as the python file your working on and do **from LRUCache import LRUCache**
then set **LRUCache.cache_limit** and use the wrapper **@LRUCache** above the functions you wish to use LRU Cache(Least Recently Used Cache) with, its really as simple as that.

## Testing
* To test it and see what i mean *Fork* the repository and run the code, **python LRUCache_test.py** in terminal.
* The test file has DEBUG set to True, it will output debugging mode and show how the cache works etc. It defaults to False - which is normal mode.

## Built With

* **Python 3.6.5** - [https://www.python.org/](https://www.python.org/)