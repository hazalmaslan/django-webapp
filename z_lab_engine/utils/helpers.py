import hashlib


def sha1(text):
    return hashlib.sha1(text.encode()).hexdigest()


def sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()


def md5(text):
    return hashlib.md5(text.encode()).hexdigest()


