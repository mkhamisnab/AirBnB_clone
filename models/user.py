#!/usr/bin/python3
"""
Module class: User
"""

from models.base_model import BaseModel

class User(BaseModel):
    """
    User - Class representing a user, inherits from BaseModel.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
