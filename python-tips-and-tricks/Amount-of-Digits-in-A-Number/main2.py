import math
from typing import Counter

number = 99999999999999999999997

print(len(str(number)))

counter = 1

while abs(number) >= (10 ** counter):
    counter += 1

print(counter)