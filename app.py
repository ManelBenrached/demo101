import hashlib

msg = hashlib.md5(b"hello  world").digest()
print(msg)
