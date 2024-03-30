import numpy as np

a = np.array([
    [1,2,3,7],
    [4,5,6,7],
    [7,8,9,7],
    [8,5,3,1]
])

b = [10,20,30,40]

a = np.insert(a,2,b,axis=1)
print(a)