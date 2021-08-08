import hashlib

print(hashlib.sha256("Hello World".encode()).hexdigest())

def mine(block_number, transactions, previous_hash):
    pass