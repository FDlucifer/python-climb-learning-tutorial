numbers = [11, 12, 76, 55, 9, 88, 10]

even = lambda x: x % 2 == 0

result = [even(number) for number in numbers]

if any(result):
    print("at least one number is even!")
else:
    print("no number is even!")

if all(result):
    print("all numbers are even!")