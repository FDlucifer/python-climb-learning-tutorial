# Descending Order

def descending_order(num):
    num_str = str(num)
    digits = [x for x in num_str]
    digits.sort(reverse=True)
    return int("".join(digits))