#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel

class Review(BaseModel):
    """Represents a Review.

    Properties:
        place_id (str): The ID of the associated Place.
        user_id (str): The ID of the associated User.
        text (str): The content of the review.
    """
    place_id = ""  # ID of the corresponding Place.
    user_id = ""  # ID of the associated User.
    text = ""  # Content of the review.
