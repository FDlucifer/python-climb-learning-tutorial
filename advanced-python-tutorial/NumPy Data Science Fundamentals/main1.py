import numpy as np

a = np.array(
    [[1,2,3],
    [4,"hello",6],
    [7,8,9]]
)

print(a.dtype)
print(a[0][0])
print(a[0][0].dtype)
print(a[1][1].dtype)
print(a[1][1])
print(type(a[0][0]))