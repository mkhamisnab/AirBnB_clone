#!/usr/bin/python3
"""
Module that is executed when the models package is imported.
"""

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
