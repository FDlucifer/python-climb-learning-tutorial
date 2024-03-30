# pip install pandas-datareader winotify

import os
import time
import pandas_datareader as web
from winotify import Notification, audio

tickers = ["AAPL", "FB", "NVDA", "GS", "WFC"]
upper_limits = [200, 220, 240, 400, 70]
lower_limits = [100, 130, 140, 280, 30]

while True:
    last_prices = [web.DataReader(ticker, "yahoo")["Adj Close"][-1] for ticker in tickers]
    print(last_prices)
    time.sleep(2)
    for i in range(len(tickers)):
        if last_prices[i] > upper_limits[i]:
            toast = Notification(app_id="luci stock alarm bot",
                                 title="price alert for " + tickers[i],
                                 msg=f"{tickers[i]} has reached a price of {last_prices[i]:.2f}. you might want to sell.",
                                 icon=os.path.join(os.getcwd(), "sell.jpg"),
                                 duration="long")
            toast.add_actions(label="go to stockbroker", launch="https://fdlucifer.github.iio/")
            toast.set_audio(audio.LoopingAlarm6, loop=True)
            toast.show()
        elif last_prices[i] > lower_limits[i]:
            toast = Notification(app_id="luci stock alarm bot",
                                 title="price alert for " + tickers[i],
                                 msg=f"{tickers[i]} has reached a price of {last_prices[i]:.2f}. you might want to buy.",
                                 icon=os.path.join(os.getcwd(), "buy.jpg"),
                                 duration="long")
            toast.add_actions(label="go to stockbroker", launch="https://fdlucifer.github.iio/")
            toast.set_audio(audio.LoopingAlarm6, loop=True)
            toast.show()
        time.sleep(1)

