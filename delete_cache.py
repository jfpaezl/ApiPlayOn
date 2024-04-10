# import os
# import glob

# # Find and remove all .pyc files
# for pyc_file in glob.glob("**/*.pyc", recursive=True):
#     os.remove(pyc_file)

# # Find and remove all __pycache__ directories
# for pycache_dir in glob.glob("**/__pycache__", recursive=True):
#     os.rmdir(pycache_dir)

from fastapi import Depends, HTTPException
from app.persistence.crud.user_crud import getByToken
from app.config.connection import get_db

db = next(get_db())
user = getByToken(db, "g0ScxCXDjuQAeCIkt3-cUsOG-FodpdxY6JnN-iV9HfY")
print(f"User(id={user.id}, name={user.name}, email={user.email})")
