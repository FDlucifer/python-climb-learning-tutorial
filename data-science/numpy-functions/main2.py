import numpy as np

a = np.array([
    [1,2,3,7],
    [4,5,6,7],
    [7,8,9,7]
])

a = a.reshape((2,3,2))
print(a)