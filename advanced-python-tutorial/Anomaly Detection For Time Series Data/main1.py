import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

from adtk.data import validate_series
from adtk.visualization import plot
from adtk.detector import *

data = yf.download("TSLA")['Close']
data = validate_series(data)

volatility_detector = VolatilityShiftAD(c=6.0, side="positive", window=30)
anomalies = volatility_detector.fit_detect(data)
plot(data, anomaly=anomalies, anomaly_color="red")
plt.show()