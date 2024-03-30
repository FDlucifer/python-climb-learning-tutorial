# pip install easyocr

import easyocr

reader = easyocr.Reader(['en'])
result = reader.readtext('text.jpg')

print(result)
