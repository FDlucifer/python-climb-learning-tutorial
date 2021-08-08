import qrcode

qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=20,border=2)

qr.add_data("https://fdlucifer.github.io/")
qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color="blue")
img.save("advanced.png")