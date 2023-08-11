#!/usr/bin/python3
"""
place.py - Module containing the Place class, a subclass of BaseModel.
"""

from models.base_model import BaseModel

class Place(BaseModel):
    """
    Place - Class representing a place, inherits from BaseModel.
    """
    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """
        Constructor method to initialize a Place instance.
        """
        super().__init__(self, *args, **kwargs)
