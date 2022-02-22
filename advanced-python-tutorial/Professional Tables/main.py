# pip install tabulate

from tabulate import tabulate
import numpy as np
import pandas as pd

table_data = [['Name', 'Age', 'Job'],
            ['Mike', '22', 'Programmer'],
            ['John', '24', 'Teacher'],
            ['Jane', '23', 'Designer'],
            ['Jack', '25', 'Manager'],
            ['Jill', '26', 'Programmer']]

data = {
    'Name': ['Mike', 'John', 'Jane', 'Jack', 'Jill'],
    'Age': ['22', '24', '23', '25', '26'],
    'Job': ['Programmer', 'Teacher', 'Designer', 'Manager', 'Programmer']
}

print(table_data)

for row in table_data:
    for col in row:
        print(col, end=' ')
    print()

print(tabulate(table_data, headers="firstrow", tablefmt="psql"))
print(tabulate(table_data, headers="firstrow", tablefmt="plain"))
print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))
print(tabulate(table_data, headers="firstrow", tablefmt="html"))

with open('mytable.html', 'w') as f:
    f.write(tabulate(table_data, headers="firstrow", tablefmt="html"))

with open('mytable.tex', 'w') as f:
    f.write(tabulate(table_data, headers="firstrow", tablefmt="latex"))

print(tabulate(data, headers="keys", tablefmt="fancy_grid", showindex="always"))

columns = ['COL1', 'COL2', 'COL3']
arr = np.array([[1,2,3], [4,5,6], [7,8,9]])

print(tabulate(arr, headers=columns, tablefmt="fancy_grid", showindex="always"))

df = pd.DataFrame(data)
print(df)
print(tabulate(df, headers="keys", tablefmt="fancy_grid", showindex="always"))