import pandas as pd
from prophet import Prophet

data = pd.read_csv("stock_data.csv")
data = data[["Date", "Close"]]
data.columns = ["ds", "y"]

prophet = Prophet(daily_seasonality=True)
prophet.fit(data)

future_dates = prophet.make_future_dataframe(periods=365)
predictions = prophet.predict(future_dates)

from prophet.plot import plot_plotly

plot_plotly(prophet, predictions)

unknown_data = data.iloc[-90:]
data = data.iloc[:-90]
prophet = Prophet(daily_seasonality=True)
prophet.fit(data)

future_dates = prophet.make_future_dataframe(periods=365)
predictions = prophet.predict(future_dates)

plot_plotly(prophet, predictions)

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))

pred = predictions[predictions['ds'].isin(unknown_data['ds'])]

plt.plot(pd.to_datetime(unknown_data['ds']), unknown_data['y'], label="Actual")
plt.plot(pd.to_datetime(unknown_data['ds']), pred['yhat'], label="Prediction")

plt.legend()