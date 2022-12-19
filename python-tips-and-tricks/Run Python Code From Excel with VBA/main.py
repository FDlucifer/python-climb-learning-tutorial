import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel("mydata.xlsm")
print(data)

data.Prices.list()
plt.show()

grouped_data = data.groupby(by="Categories").mean()
plt.bar(grouped_data.index, grouped_data.Prices)
plt.show()

one_hot_categories = pd.get_dummies(data.Categories)
data = data.join(one_hot_categories)
data.drop(["Categories"], axis=1)

sns.heatmap(data.corr(), annot=True, cmap="YlGnBu")
plt.show()

