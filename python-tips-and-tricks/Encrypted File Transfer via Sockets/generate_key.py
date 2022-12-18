# pip install pycrypto tqdm

from Crypto.Cipher import AES

key = b"lucifer11lucifer"
nonce = b"lucifer11lucifer11"

cipher = AES.new(key, AES.MODE_EAX, nonce)
ciphertext = cipher.encrypt(b"hello world!")

print("[+] encrypt: ", ciphertext)

cipher = AES.new(key, AES.MODE_EAX, nonce)

print("[+] decrypt: ", cipher.decrypt(ciphertext))
