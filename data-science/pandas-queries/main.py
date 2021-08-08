import pandas as pd

df = pd.read_csv("people.csv", delimiter=',')
df.set_index('SSN', inplace=True)

print(df.loc[(df['Age'] >= 45) & (df['Height'] > 170)]['Name'])