# pip install pandas
# pip install pandas-datareader
# pip install yahoo-fin

from collections import Counter
import pandas_datareader as web
import pandas as pd
from yahoo_fin import stock_info as si
import datetime as dt

tickers = si.tickers_sp500()

start = dt.datetime.now() - dt.timedelta(days=365)
end = dt.datetime.now()

sp500_df = web.DataReader('^GSPC', 'yahoo', start, end)
sp500_df['Pct Change'] = sp500_df['Adj Close'].pct_change()
sp500_return = (sp500_df['Pct Change'] + 1).cumprod()[-1]

return_list = []
final_df = pd.DataFrame(columns=['Ticker', 'Latest_Price', 'Score', 'PE_Ratio', 'PEG_Ratio', 'SMA_150', 'SMA_200', '52_Week_Low', '52_Week_High'])

counter = 0

for ticker in tickers:
    df = web.DataReader(ticker, 'yahoo', start, end)
    df.to_csv(f'stock_data/{ticker}.csv')

    df['Pct Change'] = df['Adj Close'].pct_change()
    stock_return = (df['Pct Change'] + 1).cumprod()[-1]

    return_compared = round((stock_return / sp500_return), 2)
    return_list.append(return_compared)

    counter += 1
    if counter == 10:
        break

best_performers = pd.DataFrame(list(zip(tickers, return_list)), columns=['Ticker', 'Returns Compare'])
best_performers['Score'] = best_performers['Returns Compared'].rank(pct=True) * 100
best_performers = best_performers[best_performers['Score'] >= best_performers['Score'].quantile(0.7)]

for ticker in best_performers['Ticker']:
    try:
        df = pd.read_csv(f'stock_data/{ticker}.csv', index_col=0)
        moving_averages = [150, 200]
        for ma in moving_averages:
            df['SMA_' + str(ma)] = round(df['Adj Close'].rolling(window=ma).mean(), 2)

        latest_price = df['Adj Close'][-1]
        pe_ratio = float(si.get_quote_table(ticker)['PE Ratio (TTM)'])
        peg_ratio = float(si.get_stats_valuation(ticker)[1][4])
        moving_averages_150 = df['SMA_150'][-1]
        moving_averages_200 = df['SMA_200'][-1]
        low_52week = round(min(df['Low'][-(52*5):]), 2)
        high_52week = round(max(df['High'][-(52*5):]), 2)
        score = round(best_performers[best_performers['Ticker'] == ticker]['Score'].tolist()[0])

        condition_1 = latest_price > moving_averages_150 > moving_averages_200
        condition_2 = latest_price >= (1.3 * low_52week)
        condition_3 = latest_price >= (0.75 * high_52week)
        condition_4 = pe_ratio < 40
        condition_5 = peg_ratio < 2

        if condition_1 and condition_2 and condition_3 and condition_4 and condition_5:
            final_df = final_df.append({
                'Ticker': ticker,
                'Latest_Price': latest_price,
                'Score': score,
                'PE_Ratio': pe_ratio,
                'PEG_Ratio': peg_ratio,
                'SMA_150': moving_averages_150,
                'SMA_200': moving_averages_200,
                '52_Week_Low': low_52week,
                '52_Week_High': high_52week
            }, ignore_index=True)
    except Exception as e:
        print(f"{e} for {ticker}")

final_df.sort_values(by='Score', ascending=False)
pd.set_option("display.max_columns", 10)
print(final_df)
final_df.to_csv('final.csv')