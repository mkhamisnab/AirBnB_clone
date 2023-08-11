!/usr/bin/python3
"""
city.py - Module containing the City class, a subclass of BaseModel.
"""

from models.base_model import BaseModel

class City(BaseModel):
    """
    City - Class representing a city, inherits from BaseModel.
    """
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """
        Constructor method to initialize a City instance.
        """
        super().__init__(self, *args, **kwargs)
