import random
from collections import Counter

obj_list = ["A", "B", "C", "D", "E"]

occurences = random.choices(obj_list, k=100)

dct = {}

for obj in obj_list:
    dct[obj] = 0

for occurence in occurences:
    dct[occurence] += 1

counter = Counter(occurences)
print(counter.most_common())
print(dct)

max_val = -1
max_key = None
for key, value in dct.items():
    if value > max_val:
        max_val = value
        max_key = key

print(max_key, max_val)