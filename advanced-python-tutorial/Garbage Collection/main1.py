import gc
import sys
import time

# gc.set_debug(True)
# gc.disable()
gc.set_threshold(20000, 50, 100)

class Link:
    def __init__(self, next_link, value):
        self.next_link = next_link
        self.value = value

    def __repr__(self):
        return self.value


l = Link(None, "Main Link")

mylist = []

start = time.perf_counter()
for i in range(5000000):
    l_temp = Link(l, "L")
    mylist.append(l_temp)
end = time.perf_counter()

print(end - start)
