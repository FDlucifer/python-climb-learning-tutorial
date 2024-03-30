# pip install xlwings

import xlwings as xw

book = xw.Book()
sheet = book.sheets[0]
sheet.name = 'test sheet'
sheet['A1'].value = 'my cell'
sheet['A1:D3'].value = 'AAA'
sheet[(3,7)].value = 'BBB'
sheet['E1'].color = (255,0,0)