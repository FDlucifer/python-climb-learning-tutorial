import numpy as np
import pandas as pd

df = pd.read_csv('DOGECOIN.csv')
df = df.set_index(pd.DatetimeIndex(df['Date'].values))

amount_invested = input('enter amount invested in dollars: ')
print(amount_invested)
invest_data = input('enter the date that you invested: ')
print(invest_data)

col1 = 'Low'
col2 = 'High'

price1 = df[col1][invest_data]
price2 = df[col2][invest_data]

quantity1 = int(amount_invested) / price1
quantity2 = int(amount_invested) / price2

profit1 = (quantity1 * df[col1][-1]) - int(amount_invested)
profit2 = (quantity2 * df[col2][-1]) - int(amount_invested)

print('you would have made between $', round(profit1, 2), 'and $', round(profit2, 2), 'as of ', df['Date'][-1])

ROT1 = profit1 / int(amount_invested) * 100
ROT2 = profit2 / int(amount_invested) * 100
print('your return on investment (ROI) would be between', round(ROT1, 2), '% and', round(ROT2, 2), '% as of', df['Date'][-1])
