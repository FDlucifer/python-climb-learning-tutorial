# pip install tqdm

import math
import time
from tqdm import tqdm, trange
from joblib import Parallel, delayed
import random

results = [math.factorial(x) for x in tqdm(range(8000))]

for i in tqdm(range(8000)):
    results.append(math.factorial(i))

results = Parallel(n_jobs=2)(delayed(math.factorial)(x) for x in tqdm(range(8000)))

with trange(1000) as t:
    for i in t:
        t.set_description(f"iteration number {i+1}")
        sleeping_time = random.randint(1, 100) / 100
        t.set_postfix(something=random.randint(0,100), sleeping_time=sleeping_time)
        time.sleep(sleeping_time)
        if i % 100 == 0:
            for _ in trange(10):
                time.sleep(0.5)

