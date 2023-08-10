#!/usr/bin/python3
"""
Module executed when the models package is imported.
Initializes an instance of FileStorage and reloads the data.
"""

from models.engine.file_storage import FileStorage

# Initialize an instance of FileStorage
storage = FileStorage()

# Reload the data from the storage
storage.reload()
