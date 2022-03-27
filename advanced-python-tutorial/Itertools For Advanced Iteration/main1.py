import itertools

# for i in itertools.count(0, 5):
#     print(i)

counter = itertools.count(0, 5)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

print(list(range(0, 5000, 5)))
print(list(counter))