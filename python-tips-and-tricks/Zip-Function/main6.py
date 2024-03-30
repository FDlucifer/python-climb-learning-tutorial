letters = ['b', 'd', 'a', 'c']
numbers = [3, 2, 4, 1]

data = sorted(zip(letters, numbers))
letters, numbers = zip(*data)

print(letters)
print(numbers)