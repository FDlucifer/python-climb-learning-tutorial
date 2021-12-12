# https://site.financialmodelingprep.com/register

import requests
import matplotlib.pyplot as plt

api_key = open('api_key', 'r').read()

company = "AAPL"
years = 30

income_statement = requests.get(f"https://financialmodelingprep.com/api/v3/income-statement/{company}?limit={years}&apikey={api_key}")
income_statement = income_statement.json()

revenues = list(reversed([income_statement[i]['revenue'] for i in range(len(income_statement))]))
profits = list(reversed([income_statement[i]['grossProfit'] for i in range(len(income_statement))]))

plt.plot(revenues, label="Revenue")
plt.plot(profits, label="Profit")
plt.legend(loc="upper left")
plt.show()