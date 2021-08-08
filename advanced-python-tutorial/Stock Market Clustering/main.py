# pip install sklearn
# pip install scikit-learn

from inspect import EndOfBlock
import pandas_datareader as web
import pandas as pd
import numpy as np
import datetime as dt
from pandas_datareader import data
from sklearn import cluster
from yahoo_fin import stock_info as si

from sklearn.preprocessing import Normalizer
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.cluster import KMeans

companies_tickers = ['APPL', 'FB', 'NVDA', 'TSLA', 'ABBV', 'TTCF', 'MCD', 'CCL', 'MSFT', 'GS', 'JPM']

clusters = 4

start = dt.datetime.now() - dt.timedelta(days=365 * 2)
end = dt.datetime.now()

date = web.DataReader(list(companies_tickers), 'yahoo', start, end)

open_values = np.array(data['Open'].T)
close_values = np.array(data['Close'].T)
daily_movements = close_values - open_values

normalizer = Normalizer()
clustering_model = KMeans(n_clusters=clusters, max_iter=1000)
pipeline = make_pipeline(normalizer, clustering_model)
pipeline.fit(daily_movements)
clusters = pipeline.predict(daily_movements)

results = pd.DataFrame({
    'clusters': clusters,
    'tickers': list(companies_tickers)
}).sort_values(by=['clusters'], axis=0)

print(results)