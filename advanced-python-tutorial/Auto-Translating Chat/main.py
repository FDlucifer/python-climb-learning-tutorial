# pip install googletrans==3.1.0a0

from googletrans import Translator

translator = Translator()

text = "Hallo Wolt"
translation = translator.translate(text, src="de", dest="en")

print(translation.text)