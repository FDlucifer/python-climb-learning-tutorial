# pip install yahoo_fin
# pip install pandas

from yahoo_fin import options
import pandas as pd

stock = 'AAPL'

print(options.get_expiration_dates(stock))

pd.set_option('display.max_columns', None)
chain = options.get_calls(stock, 'November 19, 2021')

print(chain[chain['Ask'] < 100][chain['Strike'] < 100])