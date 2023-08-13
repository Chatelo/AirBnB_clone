#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel

class Place(BaseModel):
    """Represents a Place.

    Properties:
        city_id (str): The ID of the associated City.
        user_id (str): The ID of the associated User.
        name (str): The name of the place.
        description (str): A description of the place.
        number_rooms (int): The number of rooms available.
        number_bathrooms (int): The number of bathrooms available.
        max_guest (int): The maximum number of guests allowed.
        price_by_night (int): The price per night for the place.
        latitude (float): The latitude coordinate of the place.
        longitude (float): The longitude coordinate of the place.
        amenity_ids (list): A list of Amenity IDs associated with the place.
    """
    city_id = ""  # ID of the related City.
    user_id = ""  # ID of the associated User.
    name = ""  # Name of the place.
    description = ""  # A brief description of the place.
    number_rooms = 0  # Number of available rooms.
    number_bathrooms = 0  # Number of available bathrooms.
    max_guest = 0  # Maximum number of guests allowed.
    price_by_night = 0  # Price per night for the place.
    latitude = 0.0  # Latitude coordinate of the place.
    longitude = 0.0  # Longitude coordinate of the place.
    amenity_ids = []  # List of associated Amenity IDs.
