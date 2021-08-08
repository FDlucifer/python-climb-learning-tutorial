import pickle

with open('snp500.picle', 'rb') as f:
    tickers = pickle.load(f)
print(tickers)