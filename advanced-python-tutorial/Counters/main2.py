import random
from collections import Counter

obj_list = ["A", "B", "C", "D", "E"]

occurences = random.choices(obj_list, k=100)

counter = Counter(occurences)
print(counter)