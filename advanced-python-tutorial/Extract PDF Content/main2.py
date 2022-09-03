# pip install tabula-py

import tabula

tables = tabula.read_pdf("sample.pdf", pages="all")
print(tables[0])
print(type(tables[0]))
