import numpy as np
from sklearn.preprocessing import scale

numbers = np.random.randint(2, size=(2,3,4))
print(numbers)

numbers = np.random.binomial(10, p = 0.5, size=(5,10))
print(numbers)

numbers = np.random.normal(loc=70, scale = 15, size=(5,10))
print(numbers)

numbers = np.random.choice([10,20,30,40,50], size=(5,10))
print(numbers)

a = np.array([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]])

np.save("myarray.npy", a)
b = np.load("myarray.npy")
print(b)

np.savetxt("myarray.csv", a, delimiter=",")
c = np.loadtxt("myarray.csv", delimiter=",")
print(c)