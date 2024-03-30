import numpy as np
from scipy.stats import binom

total = 2332 + 1059
heads = np.random.binomial(n = total, p = 0.5)
print(f"heads: {heads}, tails: {total - heads}")