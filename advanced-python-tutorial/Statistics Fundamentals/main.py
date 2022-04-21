import math
import statistics

numbers = [10,20,30,40,50,60,70,80,90,100000]

print(sum(numbers)/len(numbers))
print(statistics.mean(numbers))

if len(numbers) % 2 == 0:
    print((numbers[len(numbers)//2] + numbers[len(numbers)//2 - 1]) / 2)
else:
    print(numbers[len(numbers//2)])

print(statistics.median_high(numbers))
print(statistics.median_low(numbers))

print(statistics.median(numbers))
print(statistics.mode(numbers))

print(max(set(numbers), key=numbers.count))