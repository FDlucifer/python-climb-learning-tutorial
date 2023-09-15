import multiprocessing
import time

def increase_counter(counter, lock):
    for _ in range(20):
        lock.acquire()
        counter.value += 10
        lock.release()
        time.sleep(0.1)

def decrease_counter(counter, lock):
    for _ in range(20):
        lock.acquire()
        counter.value -= 50
        lock.release()
        time.sleep(0.3)

counter = multiprocessing.Value('i', 0)
lock = multiprocessing.Lock()

increase_processes = []
decrease_processes = []

for _ in range(5):
    p = multiprocessing.Process(target=increase_counter, args=(counter,lock))
    p.start()
    increase_processes.append(p)

for _ in range(5):
    p = multiprocessing.Process(target=decrease_counter, args=(counter,lock))
    p.start()
    decrease_processes.append(p)

for p in increase_processes:
    p.join()

for p in decrease_processes:
    p.join()

print(counter.value)
