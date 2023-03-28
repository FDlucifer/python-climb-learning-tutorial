import hashlib

CORRECT_HASH = ""

with open("", "rb") as f:
    file_bytes = f.read()
    h = hashlib.sha256()
    h.update(file_bytes)
    file_hash = h.hexdigest()
    # digest = hashlib.file_digest(f, "sha256")

print(file_hash == CORRECT_HASH)
