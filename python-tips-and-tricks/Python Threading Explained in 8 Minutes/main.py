import threading
import time

done = False

def worker(text):
    counter = 0
    while not done:
        time.sleep(1)
        counter += 1
        print(f"{text}: {counter}")

threading.Thread(target=worker, daemon=True, args=("abc",)).start()
threading.Thread(target=worker, daemon=False, args=("xyz",)).start()
input("press enter to quit")
done = True

