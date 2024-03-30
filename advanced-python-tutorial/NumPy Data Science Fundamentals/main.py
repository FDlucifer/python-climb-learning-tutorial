# pip install numpy

import numpy as np

a = np.array([1,2,3,4,5])

print(a)
print(type(a))
a[2] = 10
print(a)

a_mul = np.array([[[1,2,3,1],
                  [4,5,6,1],
                  [7,8,9,1]],
                 [[1,1,1,1],
                  [1,1,1,1],
                  [1,1,1,1]]])

print(a_mul[0])
print(a_mul[0, 1])
print(a_mul.shape)
print(a_mul.ndim)
print(a_mul.size)
print(a_mul.dtype)