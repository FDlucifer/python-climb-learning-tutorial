import signal
import time
import sys

def termination_handler(signum, frame):
    print("termination requested!")
    print("clean up")
    sys.exit()

signal.signal(signal.SIGTERM, termination_handler)

while True:
    print("hey")
    time.sleep(1)
