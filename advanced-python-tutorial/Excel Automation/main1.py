# pip install openpyxl

import openpyxl

workbook = openpyxl.load_workbook("myfile.xlsx")
sheet = workbook.active
sheet.title = "Changed"

sheet['A1'] = "fuck world"
sheet['A2'] = True
sheet['F8'] = "=B2+C3"

workbook.save('myfile1.xlsx')