import itertools

number1 = [1,2,3]
number2 = [4,5,6]

prod = []

for i in number1:
    for j in number2:
        prod.append((i,j))

print(prod)
print(list(itertools.product(number1, number2)))

elements = ["A", "B", "C", "D", "E"]
print(list(itertools.permutations(elements)))
print(list(itertools.combinations(elements, 3)))
print(list(itertools.combinations_with_replacement(elements, 3)))