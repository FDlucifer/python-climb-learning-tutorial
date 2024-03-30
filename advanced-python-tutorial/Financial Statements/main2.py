# https://site.financialmodelingprep.com/register

from os import write
import requests
import matplotlib.pyplot as plt

api_key = open('api_key', 'r').read()

company = "AAPL"
years = 30

income_statement = requests.get(f"https://financialmodelingprep.com/api/v3/income-statement/{company}?datatype=csv&limit={years}&apikey={api_key}")

with open('data.csv', 'wb') as f:
    f.write(income_statement.content)