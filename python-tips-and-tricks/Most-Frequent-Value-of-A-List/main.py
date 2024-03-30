mylist = [1,2,3,4,1,2,1,1,2,3,2,2,4,2,3,2,1,2,2,2,1,1,3,4]

current_max = 0
current_val = None
for x in mylist:
    if mylist.count(x) > current_max:
        current_max = mylist.count(x)
        current_val = x

print(f"value: {current_val}, occurrences: {current_max}")