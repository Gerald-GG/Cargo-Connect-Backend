import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(hash, password):
    return hash == hashlib.sha256(password.encode()).hexdigest()
