from functools import partial

def greater_than(a,b):
    return a > b

greater_than_20 = partial(greater_than, 20)

print(greater_than_20(10))
print(greater_than_20(20))
print(greater_than_20(30))