# pip install openpyxl

import openpyxl

workbook = openpyxl.load_workbook("myfile.xlsx")
sheet = workbook.active
sheet.title = "Changed"

workbook.create_sheet("Second")
sheet = workbook['Second']

sheet['A1'] = "what the hell is going on?"

workbook.save('myfile1.xlsx')