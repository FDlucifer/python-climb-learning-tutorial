import qrcode

img = qrcode.make("hello, this is lucifer11!")
img.save("mycode.png")
