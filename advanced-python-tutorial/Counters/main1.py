import random
from collections import Counter

obj_list = ["A", "B", "C", "D", "E"]

counter = Counter()

for _ in range(100):
    recv_obj = random.choice(obj_list)
    counter[recv_obj] += 1

occurences = random.choices(obj_list, k=100)

print(counter)
print(occurences)