#!/usr/bin/python3
"""Definition of the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a City.

    Properties:
        state_id (str): The ID of the associated state.
        name (str): The name of the city.
    """

    state_id = ""  # The ID of the corresponding state.
    name = ""  # The name of the city.
