import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("text.xlsx")
print(df.groupby('Month').agg({"Volume": "sum","Open":"mean", "Close":"mean"}))

df = df.groupby('Month').agg({"Volume": "sum","Open":"mean", "Close":"mean"})

df['Metric'] = df.Open - df.Close
print(df)

sns.heatmap(df.corr(), annot=True, cmap="YlGnBu")
plt.title("correlation heatmap FB")
plt.show()
plt.savefig("heatmap.png")

plt.plot(df.Volume.pct_change())
plt.plot(df.Metric.pct_change())
plt.xticks(range(1,13))
plt.show()
