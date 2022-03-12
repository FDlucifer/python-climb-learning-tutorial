import random
from collections import Counter

obj_list = ["A", "B", "C", "D", "E"]

dct = {}

for obj in obj_list:
    dct[obj] = 0

for _ in range(100):
    recv_obj = random.choice(obj_list)
    print(recv_obj)
    dct[recv_obj] += 1

print(dct)