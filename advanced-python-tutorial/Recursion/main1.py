mylist = [10, 99, 12, 5, 4, 12, 8, 3, 9, 100, 1, 55, 43, 22, 3]

def find_min(lst):
    minimum = lst[0]
    for x in lst:
        if x < minimum:
            minimum = x
    return minimum

print(find_min(mylist))

def find_min_recursive(lst):
    if len(lst) == 0:
        return None
    if len(lst) == 1:
        return lst[0]
    return min(lst[0], find_min_recursive(lst[1:]))

print(find_min_recursive(mylist))