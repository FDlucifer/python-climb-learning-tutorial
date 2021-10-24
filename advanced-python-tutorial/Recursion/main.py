mylist = [2,0,2,3,0,5,4,0,3,2,0,0,1,2,0,2]

def count_zeros(lst):
    counter = 0
    for x in lst:
        if x == 0:
            counter += 1
    return counter

print(count_zeros(mylist))

def count_zeros_recursively(lst):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return 1 if lst[0] == 0 else 0
    if lst[0] == 0:
        return 1 + count_zeros_recursively(lst[1:])
    else:
        return 0 + count_zeros_recursively(lst[1:])

print(count_zeros_recursively(mylist))