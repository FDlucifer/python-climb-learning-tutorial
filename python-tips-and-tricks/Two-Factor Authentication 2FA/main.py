# pip install pyotp

import time
import pyotp

keytest = pyotp.random_base32()
print(keytest)

key = "234567abcdefghij"
totp = pyotp.TOTP(key)
print(totp.now())
# time.sleep(30)
# print(totp.now())
input_code = input("enter 2fa code: ")
print(totp.verify(input_code))

