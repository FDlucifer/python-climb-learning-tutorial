def infinite_sequence():
    result = 1
    while True:
        yield result
        result *= 5

values = infinite_sequence()

for x in range(500):
    print(x)