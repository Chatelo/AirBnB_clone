#!/usr/bin/python3
"""Definition of the BaseModel class."""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """Represents the foundational BaseModel class for the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance.

        Args:
            *args (any): Not used.
            **kwargs (dict): Attribute key/value pairs.
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """'updated_at' attribute with the current datetimesave changes."""
        self.updated_at = datetime.today()
        models.initialize_storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance.

        Includes the '__class__' key representing the class name.
        """
        result_dict = self.__dict__.copy()
        result_dict["created_at"] = self.created_at.isoformat()
        result_dict["updated_at"] = self.updated_at.isoformat()
        result_dict["__class__"] = self.__class__.__name__
        return result_dict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {} ".format(clname, self.id, self.__dict__)
