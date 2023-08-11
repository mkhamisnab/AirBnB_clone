#!/usr/bin/python3
"""
Module class: State
"""

from models.base_model import BaseModel

class State(BaseModel):
    """
    State - Class representing a state, inherits from BaseModel.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Constructor method to initialize a State instance.
        """
        super().__init__(self, *args, **kwargs)
