import numpy as np

a = np.full((2,3,4), 9)
print(a)

a = np.zeros((10,5,2))
print(a)

a = np.ones((10,5,2))
print(a)

a = np.empty((5,5,5))
print(a)

x_values = np.arange(0, 1000, 5)
print(x_values)

x_values = np.linspace(0, 1000, 4)
print(x_values)

print(np.nan)
print(np.inf)
print(np.isnan(np.nan))
print(np.isinf(np.inf))

print(np.sqrt(-1))
print(np.array([10]) / 0)