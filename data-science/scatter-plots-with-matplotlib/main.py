import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(50)
y = np.random.rand(50)

#x = [10,20,30,40,20]
#y = [5,7,3,2,6]

plt.scatter(x,y,c='red',marker='x',s=50)
plt.show()