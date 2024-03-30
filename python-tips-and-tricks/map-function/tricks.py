numbers = [14, 23, 8, 12, 2, 5, 90]

def square(x):
    return x * x

new_list = []

for i in numbers:
    new_list = [square(i) for i in numbers]

print(new_list)