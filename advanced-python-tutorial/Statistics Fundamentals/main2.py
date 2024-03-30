import math
import statistics

numbers1 = [1,2,3,10000,20000, 30000000000000000]
numbers2 = [8500, 8550, 8580, 8600, 10000000000000000]

print(statistics.harmonic_mean(numbers1))
print(statistics.harmonic_mean(numbers2))

print(len(numbers1) / sum(1 / x for x in numbers1))
print(len(numbers2) / sum(1 / x for x in numbers2))