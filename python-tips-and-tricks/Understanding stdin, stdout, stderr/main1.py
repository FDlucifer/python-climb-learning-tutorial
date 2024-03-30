import sys
import time


def progress_bar(total):
    sys.stdout.write("[")
    for i in range(total):
        time.sleep(0.1)
        sys.stdout.write("#")
        sys.stdout.flush()
    sys.stdout.write("]")


print(progress_bar(50))
