# pip install pdfkit

import pdfkit as pdf
from pyvirtualdisplay import Display

with Display() as display:
    pdf.from_file('file.html', 'file.pdf')

