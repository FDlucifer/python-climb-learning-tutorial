# seq 1 to 9000000

def mygenerator(n):
    for x in range(n):
        yield x ** 3

values = mygenerator(100)

for x in values:
    print(x)