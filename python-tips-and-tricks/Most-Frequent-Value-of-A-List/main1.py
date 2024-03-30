from collections import Counter

mylist = [1,2,3,4,1,2,1,1,2,3,2,2,4,2,3,2,1,2,2,2,1,1,3,4]

counter = Counter(mylist)
x = counter.most_common(1)[0]
print(f"value: {x[0]}, frequency: {x[1]}")