#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents a State.

    Properties:
        name (str): The name of the state.
    """
    name = ""  # The name of the state.
