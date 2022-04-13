#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")
storage = None
if storage_type == "db":
    from .engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from .engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
