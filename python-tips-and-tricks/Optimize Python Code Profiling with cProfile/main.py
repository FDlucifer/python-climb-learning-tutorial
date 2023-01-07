# python -m cProfile main.py
# pip install tuna

import cProfile
import pstats
import time

def add(x,y):
    resulting_sum = 0
    resulting_sum += x
    resulting_sum += y
    return resulting_sum

def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def do_stuff():
    result = []
    for x in range(10000):
        result.append(x ** 2)
    return result

def waste_time():
    time.sleep(5)
    print("hello!")

if __name__ == "__main__":
    with cProfile.Profile() as profile:
        print(add(100, 5000))
        print(fact(70000))
        print(do_stuff())
        waste_time()

    results = pstats.Stats(profile)
    results.sort_stats(pstats.SortKey.TIME)
    results.print_stats()
    results.dump_stats("results.prof")
    # tuna results.prof

