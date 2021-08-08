import openpyxl

workbook = openpyxl.Workbook()
sheet = workbook.active

sheet['A1'] = 10
sheet['B1'] = 20
sheet['C1'] = 30
sheet['A2'] = 10
sheet['B2'] = 20
sheet['C2'] = 30
sheet['A3'] = 10
sheet['B3'] = 20
sheet['C3'] = 30

sheet.move_range("C1:C3", rows=0, cols=-1)

'''
sheet.merge_cells("A1:C3")
sheet['A1'] = "fuck the world"

sheet.insert_rows(1, amount=5)
sheet.insert_cols(1, amount=3)
'''

workbook.save("newbook.xlsx")