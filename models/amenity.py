#!/usr/bin/python3
"""Describes the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity.

    Properties:
        name (str): The name of the amenity.
    """

    name = ""  # Default name is empty.
