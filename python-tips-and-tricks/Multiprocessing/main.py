import multiprocessing as mp
import time
import math

results_a = []
results_b = []
results_c = []

def make_calculation_one(numbers):
    for number in numbers:
        results_a.append(math.sqrt(number ** 3))

def make_calculation_two(numbers):
    for number in numbers:
        results_b.append(math.sqrt(number ** 4))

def make_calculation_three(numbers):
    for number in numbers:
        results_c.append(math.sqrt(number ** 5))

if __name__ == '__main__':
    number_list = list(range(5000000))

    p1 = mp.Process(target=make_calculation_one, args=(number_list,))
    p2 = mp.Process(target=make_calculation_two, args=(number_list,))
    p3 = mp.Process(target=make_calculation_three, args=(number_list,))

    start = time.time()
    p1.start()
    p2.start()
    p3.start()
    end = time.time()

    print(end - start)

    temp_a = results_a
    temp_b = results_b
    temp_c = results_c

    start = time.time()
    make_calculation_one(number_list)
    make_calculation_two(number_list)
    make_calculation_three(number_list)
    end = time.time()

    print(end - start)

    print(temp_a == results_a)
    print(temp_b == results_b)
    print(temp_c == results_c)