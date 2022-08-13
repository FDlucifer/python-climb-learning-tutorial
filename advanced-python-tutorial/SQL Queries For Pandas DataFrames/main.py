import pandas as pd
import pandasql as ps

data = pd.read_csv("data.csv")
data = data.set_index("id")

print(data.query("gender == 'f'"))

sql_query = "SELECT * FROM data WHERE age > 30"
print(ps.sqldf(sql_query, locals()))

data2 = pd.DataFrame({"id": [2], "job": ["Programmer"]})
print(data2)