# pip install pandas-datareader --user

import datetime as dt
import pandas_datareader as web

start = dt.datetime(2020, 1, 1)
end = dt.datetime.now()

data = web.DataReader("TSLA", "yahoo", start, end)

data.to_csv("stock_data.csv")