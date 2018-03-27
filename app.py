import hashlib

def hash(msg):
    return hashlib.md5(msg.encode()).digest()
print(hash (b"hello world"))
