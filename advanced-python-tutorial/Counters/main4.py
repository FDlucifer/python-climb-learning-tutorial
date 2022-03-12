import random
from collections import Counter

d1 = {'A': 3, 'B': 5, 'C': 4}
d1 = {'A': 1, 'B': 2, 'C': 1}

c1 = Counter(a=3, b=5, c=4)
c2 = Counter(a=1, b=2, c=1)

print(c1 - c2)

counter = Counter(a=20, b=15, c=12)
print(sorted(counter.elements()))
print(list(counter.elements()))
print(counter.elements())