import requests
import matplotlib.pyplot as plt

api_key = open('api_key', 'r').read()

company = 'FB'
years = 2

balance_sheet = requests.get(f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{company}?limit={years}&apikey={api_key}")

balance_sheet = balance_sheet.json()

total_current_assets = balance_sheet[0]['totalCurrentAssets']
print(f"total current assets of {company}: {total_current_assets:,}")

total_current_liabilities = balance_sheet[0]['totalCurrentLiabilities']
print(f"total current liabilities of {company}: {total_current_liabilities:,}")

total_debt = balance_sheet[0]['totalDebt']
cash_and_equivalents = balance_sheet[0]['cashAndCashEquivalents']
cash_debt_difference = cash_and_equivalents - total_debt
print(f"cash debt difference: {cash_debt_difference:,}")

goodwill_and_intangibles = balance_sheet[0]['goodwillAndIntangibleAssets']
total_assets = balance_sheet[0]['totalAssets']
pct_intangible = goodwill_and_intangibles / total_assets
print(f"pct: {pct_intangible * 100:.2f}")