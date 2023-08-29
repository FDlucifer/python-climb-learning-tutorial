import time
import threading

lock = threading.Lock()

def increase_counter(amount: int):
    for _ in range(amount):
        with lock:
            with open('counter.txt', 'r') as f:
                current = int(f.read())

            current += 1

            with open('counter.txt', 'w') as f:
                f.write(str(current))

            time.sleep(1)

for _ in range(15):
    threading.Thread(target=increase_counter, args=(10,)).start()
