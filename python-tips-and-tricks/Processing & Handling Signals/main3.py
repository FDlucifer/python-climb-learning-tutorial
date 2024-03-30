import signal
import time
import sys

done = False

def alarm_handler(signum, frame):
    global done
    done = True
    signal.alarm(0)

signal.signal(signal.SIGALRM, alarm_handler)

time_limit = 3
signal.alarm(time_limit)

counter = 1
while not done:
    print(counter ** 4)
    counter += 1

print("reached counter", counter)