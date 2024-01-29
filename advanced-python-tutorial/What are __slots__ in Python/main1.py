# pip install memory_profiler

import timeit
import statistics
from memory_profiler import memory_usage

class PointWithSlots:
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y

# p = PointWithoutSlots(10, 20)
# print(p.x)
# print(p.y)
# print(p.__dict__)

def create_points():
    return [PointWithSlots(i, i) for i in range(1000000)]

mem_values = []
time_values = []

for _ in range(10):
    mem_usage_without_points = memory_usage(create_points, interval=0.01)
    mem_values.append(max(mem_usage_without_points))

    point = PointWithSlots(1, 2)
    time_without_slots = timeit.timeit(lambda: (point.x, point.y), number=1000000)
    time_values.append(time_without_slots)

print(statistics.mean(mem_values))
print(statistics.mean(time_values))
