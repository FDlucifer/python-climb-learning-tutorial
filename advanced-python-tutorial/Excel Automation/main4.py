# pip install pandas-datareader
import openpyxl
import datetime as dt
import pandas_datareader as web

workbook = openpyxl.load_workbook('example.xlsx')
sheet = workbook.active

for row in range(5, 10):
    date = sheet[f'C{row}'].value
    today = dt.datetime.now()
    age = today.year - date.year - ((today.month, today.day) < (date.month, date.day))
    sheet[f'D{row}'] = age

    usd_to_eur = web.get_data_fred('DEXUSEU').iloc[-1]['DEXUSEU']
    sheet[f'E{row}'] = sheet[f'E{row}'].value * usd_to_eur
    sheet[f'E{row}'].number_format = "#,##0.00$"

workbook.save('example.xlsx')