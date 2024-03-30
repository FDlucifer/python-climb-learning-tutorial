from inspect import signature
import rsa

with open("public.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open("private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

message = "hello my password is lUc1f3r11!"

encrypted_messasge = rsa.encrypt(message.encode(), public_key)
with open("encrypted.message", "wb") as f:
    f.write(encrypted_messasge)
print("encrypted_messasge: ", encrypted_messasge)

encrypted_messasge = open("encrypted.message", "rb").read()
decrypted_messasge = rsa.decrypt(encrypted_messasge, private_key)
print("decrypted_messasge: ", decrypted_messasge)

signature = rsa.sign(message.encode(), private_key, "SHA-256")

with open("signature", "wb") as f:
    f.write(signature)

with open("signature", "rb") as f:
    signature = f.read()

print("signature verifyed: ", rsa.verify(message.encode(), signature, public_key))

