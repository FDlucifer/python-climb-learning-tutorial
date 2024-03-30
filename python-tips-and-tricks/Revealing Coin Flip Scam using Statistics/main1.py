# pip install scipy

from scipy.stats import binom

total = 2332 + 1059

print(binom.pmf(2332, total, 0.5))
print((1 / 13983816) ** 15)
print(binom.pmf(343, 343 + 349, 0.5))