import signal
import time
import sys
import os

print(os.getpid())

def special_handler(signum, frame):
    print("special signal was received!")

signal.signal(signal.SIGUSR1, special_handler)

while True:
    print("hey")
    time.sleep(1)