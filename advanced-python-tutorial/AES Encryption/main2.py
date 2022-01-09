# pip install pycryptodome

from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

salt = b"\x80!\x10\xe7\x8d?z\xb9{\xe7=\xc3\xe24\x1ap\xe1>\xa0\xe5y\x17\xf2\xff\xd7+5/X\xac'\xdb"
password = "mypassword"

key = PBKDF2(password, salt, dkLen=32)

with open('encrypted.bin', 'rb') as f:
    iv = f.read(16)
    decrypt_data = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv=iv)
original = unpad(cipher.decrypt(decrypt_data), AES.block_size)
print(original)