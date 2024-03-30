import signal
import time
import sys

def resize_handler(signum, frame):
    print("window was resized")

signal.signal(signal.SIGWINCH, resize_handler)

while True:
    print("hey")
    time.sleep(1)