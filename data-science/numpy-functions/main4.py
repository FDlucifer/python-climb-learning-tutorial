import numpy as np

a = np.array([
    [1,2,3,7],
    [4,5,6,7],
    [7,8,9,7]
])

b = np.array([
    [10,20,30,40],
    [40,50,60,70],
    [70,80,90,20]
])

c = np.concatenate((a,b))
c2 = np.vstack((a,b))

print(c.shape)
print(c2)