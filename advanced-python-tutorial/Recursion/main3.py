import sys

sys.setrecursionlimit(10000)

def myfunction(n):
    if n == 0:
        pass
    else:
        print(n)
        myfunction(n-1)

myfunction(5000)