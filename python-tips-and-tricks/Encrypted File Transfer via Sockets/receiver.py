import socket
import tqdm
from Crypto.Cipher import AES

key = b"lucifer11lucifer"
nonce = b"lucifer11lucifer11"

cipher = AES.new(key, AES.MODE_EAX, nonce)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen()

client, addr = server.accept()

file_name = client.recv(1024).decode()
print(file_name)
file_size = client.recv(1024).decode()
print(file_size)

file = open(file_name, "wb")
done = False
file_bytes = b""
porogress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000, total=int(file_size))

while not done:
    data = client.recv(1024)
    if file_bytes[-5:] == b"<END>":
        done = True
    else:
        file_bytes += data
    porogress.update(1024)

print("[+] sending file bytes: ", file_bytes)
file.write(cipher.decrypt(file_bytes[:-5]))
file.close()
client.close()
server.close()

