# pip install PyPDF2

from PyPDF2 import PdfFileReader, PdfFileWriter

pages = [1, 2]

chapter1 = list(range(0,3))
chapter2 = [3,4]
chapter3 = [5]

with open("merged.pdf", "rb") as f:
    reader = PdfFileReader(f)
    c1writer = PdfFileWriter()
    c2writer = PdfFileWriter()
    c3writer = PdfFileWriter()

    for page in range(len(reader.pages)):
        if page in chapter1:
            c1writer.addPage(reader.getPage(page))
        elif page in chapter2:
            c2writer.addPage(reader.getPage(page))
        elif page in chapter3:
            c3writer.addPage(reader.getPage(page))

    with open("chapter1.pdf", "wb") as f2:
        c1writer.write(f2)

    with open("chapter2.pdf", "wb") as f2:
        c2writer.write(f2)

    with open("chapter3.pdf", "wb") as f2:
        c3writer.write(f2)

