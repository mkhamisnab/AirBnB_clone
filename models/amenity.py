#!/usr/bin/python3
"""
Module containing the class definition for Amenity
"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    Definition for the Amenity class, which inherits from BaseModel.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Constructor method for Amenity class.
        """
        super().__init__(*args, **kwargs)
