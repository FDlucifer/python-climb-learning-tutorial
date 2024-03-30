def print_and_decrease(num):
    if num == 0:
        return
    print(num)
    print_and_decrease(num - 1)

print_and_decrease(10)