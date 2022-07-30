import time
from concurrent.futures import ThreadPoolExecutor

def worker(number):
    print(f"calculating the result for number {number}")
    time.sleep(2)
    return number ** 2

pool = ThreadPoolExecutor(2)
work1 = pool.submit(worker, 7)
work2 = pool.submit(worker, 9)
work3 = pool.submit(worker, 5)
work4 = pool.submit(worker, 5)
work5 = pool.submit(worker, 8)

print(work3.result())
print(work3.done())