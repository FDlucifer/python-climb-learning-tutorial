from itertools import combinations

def lcs(x, y):
    length = min(len(x),len(y))

    for i in range(length):
        x_combs = list(combinations(x, length-i))
        y_combs = list(combinations(y, length-i))

        for comb in x_combs:
            if comb in y_combs:
                return "".join(comb)

        for comb in y_combs:
            if comb in x_combs:
                return "".join(comb)

    return ""


print(lcs("132535365", "123456789"))
