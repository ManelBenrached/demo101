import hashlib

msg = hashlib.sha512(b"hello  world").digest()
print(msg)
