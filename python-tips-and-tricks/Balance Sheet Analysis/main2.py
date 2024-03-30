import requests
import matplotlib.pyplot as plt

api_key = open('api_key', 'r').read()

company = 'FB'
years = 5

balance_sheet = requests.get(f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{company}?period=quarterly&limit={years}&apikey={api_key}")
balance_sheet = balance_sheet.json()

assets_q1 = balance_sheet[4]['totalAssets']
assets_q2 = balance_sheet[3]['totalAssets']
assets_q3 = balance_sheet[2]['totalAssets']
assets_q4 = balance_sheet[1]['totalAssets']

assets_data = [assets_q1, assets_q2, assets_q3, assets_q4]
assets_data = [x / 1000000000 for x in assets_data]

plt.bar([1,2,3,4], assets_data)
plt.title(f"quarterly assets of {company}")
plt.xlabel("quarters")
plt.ylabel("total assets (in billion usd)")
plt.xticks([1,2,3,4], ['Q1', 'Q2', 'Q3', 'Q4'])
plt.show()