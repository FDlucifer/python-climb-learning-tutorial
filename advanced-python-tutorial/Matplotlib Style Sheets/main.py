from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np

#plt.style.use('ggplot')
#plt.style.use('fivethirtyeight')
#plt.style.use('dark_background')
plt.style.use('myawesometheme.mplstyle')

x_data = np.arange(0, 50, 0.01)
y_data = np.sin(x_data)
y_data2 = np.cos(x_data)

plt.plot(x_data, y_data)
plt.plot(x_data, y_data2)
plt.show()