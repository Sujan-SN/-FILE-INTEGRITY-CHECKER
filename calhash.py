import hashlib

def calculate_hash(file_path):
    hash = hashlib.sha256()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash.update(chunk)
    return hash.hexdigest()

file_path = input("Enter the file path: ")
hash_value = calculate_hash(file_path)
print("Hash Value:", hash_value)
