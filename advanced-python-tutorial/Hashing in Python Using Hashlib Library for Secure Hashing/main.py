import hashlib

print(hashlib.algorithms_available)
print(hashlib.algorithms_guaranteed)

h = hashlib.new("SHA256")
h.update(b"hello world!")
print(h.digest())
print(h.hexdigest())

correct_password = "mypassword1234567"
h.update(correct_password.encode())
password_hash = h.hexdigest()
print(password_hash)

