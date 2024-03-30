import signal
import time

def interrupt_handler(signum, frame):
    print("you are trying to interrupt me!")

signal.signal(signal.SIGINT, interrupt_handler)

while True:
    print("hey")
    time.sleep(1)
