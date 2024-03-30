def greater_than(a,b):
    return a > b

def make_comparator(n):
    return lambda a: a > n

greater_than_20 = make_comparator(20)

print(greater_than_20(10))
print(greater_than_20(20))
print(greater_than_20(30))