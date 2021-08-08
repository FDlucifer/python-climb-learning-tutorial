letters = ['b', 'd', 'a', 'c']
numbers = [3, 2, 4, 1]

data1 = sorted(zip(numbers, letters))
data2 = sorted(zip(letters, numbers))

print(data1)
print(data2)