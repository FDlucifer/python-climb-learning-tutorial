from functools import cached_property
import time

class ExpensiveComputation:
    def __init__(self, value):
        self.value = value

    @property
    def computation_result(self):
        print('calculating result...')
        time.sleep(3)
        return self.value * 5

ec = ExpensiveComputation(10)
print(ec.computation_result)
print(ec.computation_result)
print(ec.computation_result)

ec.value = 100
print(ec.computation_result)

del ec.computation_result

print(ec.computation_result)
