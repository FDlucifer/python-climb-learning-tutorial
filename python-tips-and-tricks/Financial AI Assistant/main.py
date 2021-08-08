# pip install neuralintents
# pip install matplotlib
# pip install mplfinance
# pip install pandas
# pip install pandas-datareader

import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import mplfinance as mpf

import pickle
import sys
import datetime as dt

portfolio = {'APPL': 20, 'TSLA': 5, 'GS': 10}

with open('portfolio.pkl', 'wb') as f:
    pickle.dump(portfolio, f)