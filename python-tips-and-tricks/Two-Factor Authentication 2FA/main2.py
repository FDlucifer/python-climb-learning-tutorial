# pip install qrcode

import time
import pyotp
import qrcode

key = "234567abcdefghij"

uri = pyotp.totp.TOTP(key).provisioning_uri(name="lucifer11", issuer_name="lucifer11's app")

print(uri)
qrcode.make(uri).save("totp.png")

