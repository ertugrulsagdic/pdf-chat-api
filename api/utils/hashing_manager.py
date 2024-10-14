import hashlib


class HashingManager:
    @staticmethod
    def md5_file_hashing(file):
        return hashlib.md5(file).hexdigest()