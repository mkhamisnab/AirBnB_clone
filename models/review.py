#!/usr/bin/python3
"""
Module class: Review
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """
    Review - Class representing a review, inherits from BaseModel.
    """
    text = ""
    place_id = ""
    user_id = ""

    def __init__(self, *args, **kwargs):
        """
        Constructor method to initialize a Review instance.
        """
        super().__init__(self, *args, **kwargs)
