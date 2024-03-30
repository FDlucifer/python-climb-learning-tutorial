# pip install yfinance
# pip install yahoo_fin
# pip install matplotlib

import yfinance as yf
from yahoo_fin import stock_info as si
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pickle

plt.style.use("dark_background")

with open('general.pickle', 'rb') as f:
    general_dist = pickle.load(f)

with open('industry.pickle', 'rb') as f:
    sector_dist = pickle.load(f)

with open('country.pickle', 'rb') as f:
    country_dist = pickle.load(f)

with open('market_cap.pickle', 'rb') as f:
    market_cap_dist = pickle.load(f)

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