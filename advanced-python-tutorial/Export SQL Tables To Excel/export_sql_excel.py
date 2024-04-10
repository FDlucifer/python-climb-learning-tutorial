import sqlite3
import pandas as pd

conn = sqlite3.connect("person_data.db")

df = pd.read_sql_query("SELECT * FROM person", conn)

df.to_excel("person_table.xlsx", index=False)

df.to_csv("person_table.csv", index=False)

conn.close()
