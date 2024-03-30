# pip install yfinance
# pip install yahoo_fin
# pip install matplotlib

import yfinance as yf
from yahoo_fin import stock_info as si
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pickle


plt.style.use("dark_background")

stocks = ['AAPL', 'FB', 'TSLA', 'ABBV', 'TTCF', 'NVDA', 'CCL', 'BABA', 'NSRGY', 'OMV.VI', 'VYGVF']
amounts = [20, 15, 20, 10, 30, 40, 20, 50, 60, 30, 50]
values = [si.get_live_price(stocks[i]) * amounts[i] for i in range(len(stocks))]
sectors = [yf.Ticker(x).get_info()['industry'] for x in stocks]
countries = [yf.Ticker(x).get_info()['country'] for x in stocks]
market_caps = [yf.Ticker(x).get_info()['marketCap'] for x in stocks]

cash = 40000

etfs = ['IVV', 'XWD.TO']
etf_amounts = [30, 20]
etf_values = [si.get_live_price(etfs[i]) * etf_amounts[i] for i in range(len(etfs))]

cryptos = ['ETH-USD', 'BTC-USD']
crypto_amounts = [0.89, 0.34]
crypto_values = [si.get_live_price(cryptos[i]) * crypto_amounts[i] for i in range(len(cryptos))]

general_dist = {
    'Stocks': sum(values),
    'ETFs': sum(etf_values),
    'Cryptos': sum(crypto_values),
    'Cash': cash
}

sector_dist = {}
for i in range(len(sectors)):
    if sectors[i] not in sector_dist.keys():
        sector_dist[sectors[i]] = 0
    sector_dist[sectors[i]] += values[i]

country_dist = {}
for i in range(len(countries)):
    if countries[i] not in country_dist.keys():
        country_dist[countries[i]] = 0
    country_dist[countries[i]] += values[i]

market_cap_dist = {'small': 0.0, 'mid': 0.0, 'large': 0.0, 'huge': 0.0}
for i in range(len(stocks)):
    if market_caps[i] < 2000000000:
        market_cap_dist['small'] += values[i]
    elif market_caps[i] < 1000000000:
        market_cap_dist['mid'] += values[i]
    elif market_caps[i] < 100000000000:
        market_cap_dist['large'] += values[i]
    else:
        market_cap_dist['huge'] += values[i]

with open('general.pickle', 'wb') as f:
    pickle.dump(general_dist, f)

with open('industry.pickle', 'wb') as f:
    pickle.dump(sector_dist, f)

with open('country.pickle', 'wb') as f:
    pickle.dump(country_dist, f)

with open('market_cap.pickle', 'wb') as f:
    pickle.dump(market_cap_dist, f)

fig, axs = plt.subplots(2,2)
fig.suptitle("portfolio diversification analysis", fontsize=18)
axs[0.0].pie(general_dist.values(), labels=general_dist.keys(), autopct="%1.1f%%", pctdistance=0.8, colors=mcolors.TABLEAU_COLORS)
axs[0.0].set_title("general distribution")
axs[0.1].pie(sector_dist.values(), labels=sector_dist.keys(), autopct="%1.1f%%", pctdistance=0.8, colors=mcolors.TABLEAU_COLORS)
axs[0.1].set_title("stocks by industry")
axs[1.0].pie(country_dist.values(), labels=country_dist.keys(), autopct="%1.1f%%", pctdistance=0.8, colors=mcolors.TABLEAU_COLORS)
axs[1.0].set_title("stocks by country")
axs[1.1].pie(market_cap_dist.values(), labels=market_cap_dist.keys(), autopct="%1.1f%%", pctdistance=0.8, colors=mcolors.TABLEAU_COLORS)
axs[1.1].set_title("stocks by market cap")

plt.show()