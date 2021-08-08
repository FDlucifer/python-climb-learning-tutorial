numbers = list(range(100))

squared = []
for number in numbers:
    if number % 5 == 0:
        squared.append(number ** 2)

squared = [number ** 2 for number in numbers if numbers % 5 == 0]