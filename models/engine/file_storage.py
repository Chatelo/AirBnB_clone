#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """Represents an abstracted storage engine.

    Attributes:
        __file_path (str): The file name for storing objects.
        __objects (dict): A dictionary containing object instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Retrieve the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Add obj with the key <obj_class_name>.id to __objects."""
        obj_class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_class_name, obj.id)] = obj

    def save(self):
        """Serialize __objects into the JSON file __file_path."""
        objects_dict = FileStorage.__objects
        serialized_dict = \
            {key: objects_dict[key].to_dict()for key in objects_dict.keys()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(serialized_dict, file)

    def reload(self):
        """Deserialize the JSON file __file_path into \
            __objects, if the file exists."""
        try:
            with open(FileStorage.__file_path) as file:
                deserialized_dict = json.load(file)
                for serialized_obj in deserialized_dict.values():
                    class_name = serialized_obj["__class__"]
                    del serialized_obj["__class__"]
                    self.new(eval(class_name)(**serialized_obj))
        except FileNotFoundError:
            return
