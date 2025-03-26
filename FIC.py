import hashlib
import os

def calculate_hash(file_path):
    """
    Calculate the SHA-256 hash of a file.
    """
    hash = hashlib.sha256()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash.update(chunk)
    return hash.hexdigest()

def check_file_integrity(file_path, expected_hash):
    """
    Check if the file's hash matches the expected hash.
    """
    actual_hash = calculate_hash(file_path)
    if actual_hash == expected_hash:
        print(f"File {file_path} is intact.")
    else:
        print(f"File {file_path} has been modified.")

def main():
    file_path = input("Enter the file path: ")
    expected_hash = input("Enter the expected hash: ")
    check_file_integrity(file_path, expected_hash)

if __name__ == "__main__":
    main()

