import pandas_datareader as web
import matplotlib.pyplot as plt
import mplfinance as mpf

import datetime as dt

crypto = "BTC"
currency = "USD"

start = dt.datetime(2020,1,1)
end = dt.datetime.now()

btc = web.DataReader(f"{crypto}-{currency}", "yahoo", start, end)
eth = web.DataReader(f"ETH-{currency}", "yahoo", start, end)

plt.yscale("log")

plt.plot(btc['Close'], label="BTC")
plt.plot(eth['Close'], label="ETH")
plt.legend(loc="upper left")
plt.show()

#print(data)
#plt.plot(data['Close'])
#plt.show()
#mpf.plot(data, type="candle", volume=True, style="yahoo")