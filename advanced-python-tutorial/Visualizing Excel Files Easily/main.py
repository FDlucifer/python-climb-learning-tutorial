# pip install pandas matplotlib seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel("data.xlsx", skiprows=2)
data = data.iloc[:, 1:]
data = data.set_index("Date")

print(data)

plt.plot(data.index, data['Workout'])
plt.title("Workout Stats")
plt.xlabel("Date")
plt.ylabel("Workout Time (in Minutes)")
plt.show()

sns.lineplot(data=data, x="Date", y="Workout")
plt.title("Workout Stats")
plt.xlabel("Date")
plt.ylabel("Workout Time (in Minutes)")
plt.show()

