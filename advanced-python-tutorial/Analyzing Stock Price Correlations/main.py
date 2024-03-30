# pip install matplotlib seaborn pandas pandas-datareader

from cProfile import label
from tkinter import dnd
import pandas_datareader as web
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

start = dt.datetime(2018, 1, 1)
end = dt.datetime.now()

tickers = ["FB", "GS", "NVDA", "MSFT", "TSLA", "AAPL", "CCL", "BA"]
colnames = []

for ticker in tickers:
    data = web.DataReader(ticker, "yahoo", start, end)
    if len(colnames) == 0:
        combined = data[['Adj Close']].copy()
    else:
        combined = combined.join(data['Adj Close'])
    colnames.append(ticker)
    combined.columns = colnames

# plt.yscale("log")

# # print(combined)
# for ticker in tickers:
#     plt.plot(combined[ticker], label=ticker)

# plt.legend(loc="upper right")
# plt.show()

corr_data = combined.pct_change().corr(method="pearson")
sns.heatmap(corr_data, annot=True, cmap="coolwarm")

plt.show()