import os
import glob

# Find and remove all .pyc files
for pyc_file in glob.glob("**/*.pyc", recursive=True):
    os.remove(pyc_file)

# Find and remove all __pycache__ directories
for pycache_dir in glob.glob("**/__pycache__", recursive=True):
    os.rmdir(pycache_dir)

# from app.utils.hash import verify_password, hash_password

# print(verify_password("123456", "$2b$12$STt8FpTZfmgOpkiisv8gEudAk4udX9RqhOlpusbbQe4hjCd2HWKZ."))

# print(hash_password("123456"))
