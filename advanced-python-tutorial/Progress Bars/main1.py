import math
import pandas_datareader as web

def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = '#' * int(percent) + '-' * (100 - int(percent))
    print(f"\r|{bar}| {percent:.2f}%", end="\r")

tickers = ["AAPL", "FB", "TSLA", "NVDA", "GS", "WFC"]
closing_prices = []

progress_bar(0, len(tickers))
for index, ticker in enumerate(tickers):
    last_price = web.DataReader(ticker, "yahoo").iloc[-1]['Close']
    closing_prices.append(last_price)
    progress_bar(index + 1, len(tickers))