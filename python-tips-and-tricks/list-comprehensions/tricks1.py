numbers = [1,2,3,4,5,6,7]

powers_of_two = [2 ** x for x in numbers]

print(powers_of_two)

powers_of_two = [2 ** x for x in range(30) if x % 5 == 0]

print(powers_of_two)

words = ['automobile', 'car', 'anger', 'fox', 'anchor']

words = [word.upper() for word in words if word.startswith('a') ]

print(words)