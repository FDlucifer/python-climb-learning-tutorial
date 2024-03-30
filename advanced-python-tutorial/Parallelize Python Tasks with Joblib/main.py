# pip install joblib colorthief

import math
import time
from joblib import Parallel, delayed

t1 = time.time()
# results = [math.factorial(x) for x in range(10000)]
results = Parallel(n_jobs=16)(delayed(math.factorial)(x) for x in range(10000))
t2 = time.time()

print(t2-t1)

