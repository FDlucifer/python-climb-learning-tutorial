mysquare = lambda x: x * x

print(mysquare(5))

mysum = lambda x, y: x + y

print(mysum(5, 10))

mysum1 = lambda *args: sum(args)

print(mysum1(10, 20, 30, 5))

print((lambda x: x ** 3)(5))

numbers = [8, 66, 12, 14, 15, 7, 99, 109, 88, 76]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)

squared_numbers = list(map(lambda x: x ** 2, numbers))

print(squared_numbers)

def myfunction(num):
    return lambda x: x * num

ten_multiplier = myfunction(10)
print(ten_multiplier(20))