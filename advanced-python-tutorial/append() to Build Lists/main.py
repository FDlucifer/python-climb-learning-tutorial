numbers = [1,2,3]

numbers.append(4)
print(numbers)
numbers.append("four")
print(numbers)
numbers.append(5.0)
print(numbers)
numbers[len(numbers):] = [4]
print(numbers)
numbers.append([4,5,6])
print(numbers)

x = [1,2,3,4]
y = (5,6)

x.append(y)
print(x)
x.extend(y)
print(x)

# show square roots

import math

def square_root(numbers):
    result = []
    for number in numbers:
        result.append(math.sqrt(number))
    return result

numbers = [1,4,9,16,25,36,49,64,81]
print(square_root(numbers))