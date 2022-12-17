import signal
import time
import sys

def stop_handler(signum, frame):
    print("you cannot put me into the background!")

signal.signal(signal.SIGTSTP, stop_handler)

while True:
    print("hey")
    time.sleep(1)
