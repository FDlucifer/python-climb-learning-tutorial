import time
import pandas as pd
import sys

selected_columns = ["VendorID", "payment_type", "tip_amount"]

start = time.perf_counter()
df_parquet = pd.read_parquet("yellow_tripdata_2023-01.parquet", columns=selected_columns)
end = time.perf_counter()
print(end - start)


start = time.perf_counter()
df_csv = pd.read_csv("yellow_tripdata_2023-01.csv", usecols=selected_columns)
end = time.perf_counter()
print(end - start)

print(sys.getsizeof(df_parquet))
print(sys.getsizeof(df_csv))
print(df_parquet.columns)
