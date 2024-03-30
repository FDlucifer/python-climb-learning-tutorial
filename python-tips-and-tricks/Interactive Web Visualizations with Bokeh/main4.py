# pip install pandas-datareader pandas

import numpy as np
import pandas_datareader as web
from bokeh.plotting import figure, show, curdoc
from bokeh.models import ColumnDataSource

df = web.DataReader("AAPL", "yahoo")
source = ColumnDataSource(data=df)
p = figure()

p.line(x = "Date", y = "Close", source=source)
show(p)

