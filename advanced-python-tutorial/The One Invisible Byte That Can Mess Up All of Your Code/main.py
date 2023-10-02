import pandas as pd

df = pd.read_excel("data.xlsx")

print(df.email.values[2].encode("utf-8"))

mystring = "hello wo\u200drld"

mystring = mystring.replace("\u200d", "")

print(mystring.encode("ascii"))
