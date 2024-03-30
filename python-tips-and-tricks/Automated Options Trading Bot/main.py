# pip install thetadata pandas matplotlib

import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from thetadata import ThetaClient, OptionReqType, OptionRight, DateRange

def create_signals(ticker, exp_date, client):
    transactions = {
        "transaction_date": [],
        "ticker": [],
        "striker": [],
        "exp_date": [],
        "transaction_type": []
    }

    strikes = client.get_strikes(ticker, exp_date)
    for strike in strikes:
        try:
            data = client.get_hist_option(
                req = OptionReqType.TRADE,
                root = ticker,
                exp = exp_date,
                strike = strike,
                right = OptionRight.CALL,
                date_range = DateRange(exp_date - dt.timedelta(90), exp_date)
            )
            if len(data) > 10:
                data.columns = ["MS_OF_DAY", "Sequence", "Size", "Condition", "Price", "Date"]
                data.set_index("Date", inplace=True)
                data['Signal'] = data['Size'] > data['Size'].mean() + 3 * data['Size'].std()
                selected_data = data[data['Signal']]

                for index, row in selected_data.iterrows():
                    transactions['transaction_date'].append(index)
                    transactions['ticker'].append(ticker)
                    transactions['strike'].append(strike)
                    transactions['exp_date'].append(exp_date)
                    transactions['transaction_type'].append("buy")

        except Exception as e:
            continue

        try:
            data = client.get_hist_option(
                req = OptionReqType.TRADE,
                root = ticker,
                exp = exp_date,
                strike = strike,
                right = OptionRight.PUT,
                date_range = DateRange(exp_date - dt.timedelta(90), exp_date)
            )
            if len(data) > 10:
                data.columns = ["MS_OF_DAY", "Sequence", "Size", "Condition", "Price", "Date"]
                data.set_index("Date", inplace=True)
                data['Signal'] = data['Size'] > data['Size'].mean() + 3 * data['Size'].std()
                selected_data = data[data['Signal']]

                for index, row in selected_data.iterrows():
                    transactions['transaction_date'].append(index)
                    transactions['ticker'].append(ticker)
                    transactions['strike'].append(strike)
                    transactions['exp_date'].append(exp_date)
                    transactions['transaction_type'].append("sell")

        except Exception as e:
            continue

    pd.DataFrame(transactions).to_csv("transactions.csv")

def backtest(ticker, exp_date, client):
    df = pd.read_csv("transactions.csv")
    df = df.sort_values(by="transaction_date")
    df.set_index("transaction_date", inplace=True)
    df.drop(['Unnamed: 0'], axis=1, inplace=True)

    strikes = sorted(set(df.strike.values))
    total_profit = 0
    for strike in strikes:
        data = client.get_hist_option(
            req = OptionReqType.EOD,
            root = ticker,
            exp = exp_date,
            strike = strike,
            right = OptionRight.CALL,
            date_range = DateRange(exp_date - dt.timedelta(90), exp_date)
        )

        data.columns = ["MS_OF_DAY", "Sequence", "Size", "Condition", "Price", "Date"]
        data.set_index("Date", inplace=True)

        plt.plot(data.index, data.Price)
        buy_data = df[df.transaction_type == "buy"]
        buy_data = buy_data[buy_data.strike == strike]
        filtered_data = data[data.index.isin(buy_data.index)]
        plt.scatter(filtered_data.index, filtered_data.Price, marker="^", color="green")

        plt.plot(data.index, data.Price)
        sell_data = df[df.transaction_type == "sell"]
        sell_data = sell_data[sell_data.strike == strike]
        filtered_data = data[data.index.isin(sell_data.index)]
        plt.scatter(filtered_data.index, filtered_data.Price, marker="v", color="red")
        plt.show()

        amount_owned = 0
        profit = 0

        for idx, row in df[df.strike == strike].iterrows():
            if row.transaction_type == "buy":
                amount_owned += 1
                profit -= data[data.index == idx]['Price'].values[0]
            else:
                if amount_owned > 0:
                    profit = data[data.index == idx]['Price'].values[0] * amount_owned
                    amount_owned = 0

        profit += amount_owned * data.iloc[-1]['Price']
        print(f"profit: {round(profit, 2)}")
        total_profit += profit

    print("total profit: ", round(total_profit, 2))

client = ThetaClient(username="luci@gmail.com", passwd=open("sec.txt", "r").read())

with client.connect():
    ticker = "BMY"
    exp_dates = client.get_expirations(ticker)

    for exp_date in exp_dates[390:400]:
        try:
            create_signals(ticker, exp_date, client)
            backtest(ticker, exp_date, client)
        except Exception as e:
            print(str(e))

