import datetime as dt
import plotext
import numpy as np
import pandas_datareader as web

start = dt.datetime(2018, 1, 1)
end = dt.datetime.now()

apple_data = web.DataReader("AAPL", "yahoo", start, end)
dates = [plotext.datetime.datetime_to_string(x) for x in apple_data.index]

plotext.plot_date(dates, list(apple_data['Adj Close']))
plotext.xlabel("Date")
plotext.ylabel("Price")
plotext.show()