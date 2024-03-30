numbers = list(range(100))

filtered_list = []
for x in numbers:
    if x % 5 == 0 and x % 3 == 0:
        filtered_list.append(x)

filtered_list = list(filter(lambda x: x % 5 == 0 and x % 3 == 0, numbers))
print(filtered_list)