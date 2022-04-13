#!/usr/bin/python3
""" State Module for HBNB project """
from .base_model import BaseModel


class Amenity(BaseModel):
    """Represent an Amenity.
    Attributes:
        name (str): The name of the amenity.
    """
    name = ""
