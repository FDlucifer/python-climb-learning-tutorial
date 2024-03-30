from numba import jit
import random
import math
import time
import numpy as np
import pandas as pd
import pandas_datareader as web

@jit
def pandas_function(data):
    result = data.sort_values(by=['Volume'])
    result = result.applymap(math.sqrt)
    result += 2
    result = result.T
    return result

data = web.DataReader('AAPL', 'yahoo')

start = time.time()
pandas_function(data)
end = time.time()
print(end - start)

start = time.time()
pandas_function(data)
end = time.time()
print(end - start)
