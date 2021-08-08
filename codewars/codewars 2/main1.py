# Descending Order

def descending_order(num):
    return int("".join(sorted([x for x in str(num)], reverse=True)))