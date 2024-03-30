import itertools

elements = ["A", 20, 4.5, True]

i = 0

mycycle = itertools.cycle(elements)

print(next(mycycle))
print(next(mycycle))
print(next(mycycle))
print(next(mycycle))
print(next(mycycle))

for i in itertools.cycle(elements):
    print(i)

while True:
    print(elements[i % len(elements)])
    i += 1
