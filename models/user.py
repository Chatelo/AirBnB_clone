#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel

class User(BaseModel):
    """Represents a User.

    Properties:
        email (str): The email address of the user.
        password (str): The password associated with the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """
    email = ""  # The user's email address.
    password = ""  # The user's password.
    first_name = ""  # The user's first name.
    last_name = ""  # The user's last name.
