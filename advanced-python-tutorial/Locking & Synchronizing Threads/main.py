import threading
import time
import random

class ThreadCounter:
    def __init__(self):
        self.counter = 0
        self.lock = threading.Lock()

    def count(self, thread_no):
        while True:
            self.lock.acquire()
            self.counter += 1
            print(f"{thread_no}: just increased counter to {self.counter}")
            time.sleep(1)
            print(f"{thread_no}: done some work, now value is: {self.counter}")
            self.lock.release()
            time.sleep(random.randint(1, 3))

tc = ThreadCounter()

for i in range(30):
    t = threading.Thread(target=tc.count, args=(i,))
    t.start()