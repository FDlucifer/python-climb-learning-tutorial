# pip install openpyxl

import openpyxl

workbook = openpyxl.load_workbook("myfile.xlsx")
sheet = workbook.active
sheet.title = "Changed"

print(sheet['A1'].value)
print(sheet['B1'].value)
print(sheet['C1'].value)
print(sheet['A2'].value)
print(sheet['B2'].value)
print(sheet['C2'].value)