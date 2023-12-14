# pip install pandas pyarrow
# https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

import pandas as pd

df_parquet = pd.read_parquet("yellow_tripdata_2023-01.parquet")
df_parquet.to_csv("yellow_tripdata_2023-01.csv")

# print(df_parquet)
