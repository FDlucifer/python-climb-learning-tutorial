import itertools

def power(a):
    power_set = [[]]
    for i in range(1, len(a)+1):
        power_set += [x for x in itertools.combinations(a, i)]
    return power_set
