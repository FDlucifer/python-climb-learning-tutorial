import pandas as pd

names = {
    'SSN': [2, 5, 7, 8],
    'Name': ['Anna', 'Bob', 'John', 'Mike']
}

ages = {
    'SSN': [1, 2, 3, 5],
    'Age': [28, 34, 45, 62]
}

df1 = pd.DataFrame(names)
df2 = pd.DataFrame(ages)

df = pd.merge(df1, df2, on='SSN', how='right')
df.set_index('SSN', inplace=True)

print(df)