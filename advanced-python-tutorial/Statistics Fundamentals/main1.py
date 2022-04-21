import math
import statistics

numbers = [10,10,10,10,20,30,40,50,60,70,80,90,100000,200000]

print(statistics.stdev(numbers))
print(statistics.variance(numbers))
print(statistics.mean(numbers))
print(statistics.pstdev(numbers))
print(statistics.pvariance(numbers))

numbers1 = [0,1,2,3,10000,20000,30000]
numbers2 = [8500, 8550, 8580, 8600]

print(sum((x - statistics.mean(numbers1)) ** 2 for x in numbers1) / len(numbers1))
print(math.sqrt(sum((x - statistics.mean(numbers1)) ** 2 for x in numbers1) / len(numbers1)))

print(sum((x - statistics.mean(numbers1)) ** 2 for x in numbers1) / (len(numbers1) - 1))
print(math.sqrt(sum((x - statistics.mean(numbers1)) ** 2 for x in numbers1) / (len(numbers1) - 1)))