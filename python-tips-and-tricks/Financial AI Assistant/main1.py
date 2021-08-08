# pip install neuralintents
# pip install matplotlib
# pip install mplfinance
# pip install pandas
# pip install pandas-datareader

from neuralintents import GenericAssistant
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import mplfinance as mpf

import pickle
import sys
import datetime as dt


with open('portfolio.pkl', 'rb') as f:
    portfolio = pickle.load(f)
# print(portfolio)

def save_portfolio():
    with open('portfolio.pkl', 'wb') as f:
        pickle.dump(portfolio, f)

def add_portfolio():
    ticker = input("whitch stock do you want to add: ")
    amount = input("how many shares do you want to add: ")

    if ticker in portfolio.keys():
        portfolio[ticker] += int(amount)
    else:
        portfolio[ticker] = int(amount)
    save_portfolio()

def remove_portfolio():
    ticker = input("whitch stock do you want to sell: ")
    amount = input("how many shares do you want to sell: ")

    if ticker in portfolio.keys():
        if amount <= portfolio[ticker]:
            portfolio[ticker] -= int(amount)
            save_portfolio()
        else:
            print("you don't have enough shares!")
    else:
        print(f"you don't own any shares of {ticker}")

def show_portfolio():
    print("your portfolio:")
    for ticker in portfolio.keys():
        print(f"you own {portfolio[ticker]} shares of {ticker}")

def portfolio_worth():
    sum = 0
    for ticker in portfolio.keys():
        data = web.DataReader(ticker, 'yahoo')
        price = data['Close'].iloc[-1]
        sum += price
    print(f"your portfolio is worth {sum} USD")

def portfolio_gains():
    starting_date = input("enter a date for comparison (YYYY-MM-DD): ")

    sum_now = 0
    sum_then = 0

    try:
        for ticker in portfolio.keys():
            data = web.DataReader(ticker, 'yahoo')
            price_now = data['Close'].iloc[-1]
            price_then = data.loc[data.index == starting_date]['Close'].values[0]
            sum_now += price_now
            sum_then += price_then
        print(f"relative gains: {(sum_now-sum_then)/sum_then * 100}%")
        print(f"absolute gains: {sum_now-sum_then} USD")
    except IndexError:
        print("there was no trading on this day!")

def plot_chart():
    ticker = input("choose a ticker symbol: ")
    starting_string = input("choose a starting date (YYYY-MM-DD): ")

    plt.style.use('dark_background')

    start = dt.datetime.strptime(starting_string, "%d/%m/%Y")
    end = dt.datetime.now()

    data = web.DataReader(ticker, 'yahoo', start, end)

    colors = mpf.make_marketcolors(up='#00ff00', down='#ff0000', wick='inherit', edge='inherit', volume='in')
    mpf_style = mpf.make_mpf_style(base_mpf_style='nightclouds', marketcolors=colors)
    mpf.plot(data, type='candle', style=mpf_style, volume=True)

def bye():
    print("Goodbye")
    sys.exit(0)

mappings = {
    'plot_chart': plot_chart,
    'add_portfolio': add_portfolio,
    'remove_portfolio': remove_portfolio,
    'show_portfolio': show_portfolio,
    'portfolio_worth': portfolio_worth,
    'portfolio_gains': portfolio_gains,
    'bye': bye
}

assistant = GenericAssistant('intents.json', mappings, "financial_assistant_model")

# assistant.load_model()

assistant.train_model()
assistant.save_model()

while True:
    message = input("")
    assistant.request(message)