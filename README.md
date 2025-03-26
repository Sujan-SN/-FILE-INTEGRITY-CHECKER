# FILE-INTEGRITY-CHECKER

*COMPANY*: CODETECH IT SOLUTIONS

*NAME*: SUJAN S N

*INTERN ID*: CT12WPAW

*DOMAIN*: CYBER SECURITY & ETHICAL HACKING 

*DURATION*: 12 WEEKS

*MENTOR*: NEELA SANTOSH

## DESCRIPTION OF THE TASK

Introduction

The File Integrity Checker is a Python-based tool designed to monitor changes in files by calculating and comparing their hash values. This tool ensures the integrity of files by detecting any unauthorized modifications.

Tools and Software Used

- Python 3.x (Programming Language)
- VSCode (Integrated Development Environment)
- Hashlib Library (for calculating hash values)
- Git Bash (for running Python scripts)

Editor Platform

The entire project was developed using VSCode, a popular open-source code editor. VSCode provides an excellent environment for writing, debugging, and testing Python code.

Applicability

The File Integrity Checker can be applied in various scenarios, including:

1. Data Security: Ensure the integrity of sensitive data by monitoring changes in files.
2. Software Development: Verify the integrity of code files to prevent unauthorized modifications.
3. Network Security: Monitor system files for changes to detect potential security breaches.
4. Digital Forensics: Analyze file modifications to investigate cybercrimes.

How it Works

1. The user provides a file path and an expected hash value.
2. The tool calculates the current hash value of the file using the Hashlib library.
3. The tool compares the current hash value with the expected hash value.
4. If the hash values match, the file is considered intact. Otherwise, the file has been modified.

Code Explanation

The code consists of two main functions:

1. calculate_hash(file_path): Calculates the SHA-256 hash value of a file.
2. check_file_integrity(file_path, expected_hash): Compares the current hash value with the expected hash value.

Websites Used for Reference

- https://docs.python.org/3/library/hashlib.html
- https://docs.python.org/3/
- https://code.visualstudio.com/docs
- https://stackoverflow.com/
- https://www.geeksforgeeks.org/

Challenges Faced

During the development of the File Integrity Checker, I faced several challenges:

1. Understanding Hashlib Library: I had to spend some time understanding how the Hashlib library works and how to use it to calculate hash values.
2. File Reading and Writing: I had to learn how to read and write files in Python, including handling different file modes and exceptions.
3. Error Handling: I had to implement robust error handling to handle potential errors, such as file not found or invalid hash values.

Conclusion

The File Integrity Checker is a simple yet effective tool for ensuring the integrity of files. By calculating and comparing hash values, this tool detects any unauthorized modifications to files. This project demonstrates the importance of file integrity checking in maintaining data security and integrity.

Future Enhancements

In the future, I plan to enhance the File Integrity Checker by:

1. Implementing Additional Hash Algorithms: I plan to add support for additional hash algorithms, such as MD5 and SHA-1.
2. Improving Error Handling: I plan to improve error handling by providing more detailed error messages and handling additional error scenarios.
3. Adding Support for Multiple Files: I plan to add support for checking the integrity of multiple files at once.
