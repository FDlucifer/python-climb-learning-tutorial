import numpy as np

a1 = np.array([1,2,3])
a2 = np.array([[1], [2]])

print(a1 + a2)

a = np.array([[1,2,3], [4,5,6]])
print(np.sqrt(a))
print(np.sin(a))
print(np.cos(a))
print(np.exp(a))
print(np.log10(a))

print(np.append(a, [7,8,9]))
print(a)

a = np.insert(a, 3, [4,5,6])
print(a)
print(np.delete(a, 1, 0))
print(np.delete(a, 3))
print(np.delete(a, 4))

a = np.array([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]])

print(a.shape)
print(a.reshape((5,4)))
print(a.reshape((20,)))
print(a.reshape((20,1)))
a.resize(10,2)
print(a)
print(a.flatten())
print(a.ravel())

var = [v for v in a.flat]
print(var)
print(a.transpose())
print(a.T)
print(a.swapaxes(0,1))