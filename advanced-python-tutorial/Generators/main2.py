# seq 1 to 9000000

import sys

def mygenerator(n):
    for x in range(n):
        yield x ** 3

values = mygenerator(100)
print(sys.getsizeof(values))