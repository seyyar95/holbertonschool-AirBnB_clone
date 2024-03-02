#!usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Handles storage and retrieval of objects to/from a JSON file.

    Attributes:
        __file_path (str): The path to the JSOn file where objects are stored.
        __objects (dict): A dictionary containing all loaded objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns all loaded objects.

        Returns:
            dict: A dictionary containing all objects,
            keyed by their class name and ID.
        """
        return self.__objects

    def new(self, obj):
        """
        Saves all objects to the storage.

        Args:
            obj: The object to be saved.
        """
        name = obj.__class__.__name__
        self.__objects[f"{name}.{obj.id}"] = obj

    def save(self):
        """
        Saves all objects to the JSON file.
        """
        file = self.__file_path
        objd = self.__objects
        newD = {}
        for k, v in objd.items():
            newD[k] = v.to_dict()

        with open(file, "w") as f:
            json.dump(newD, f)

    def reload(self):
        """
        Loads objects from the JSON file.
        """
        file = self.__file_path

        try:
            with open(file, "r") as f:
                data = json.load(f)
            for k in data:
                class_name = k.split('.')[0]
                self.__objects[k] = eval(f"{class_name}(**data[k])")
        except FileNotFoundError:
            pass
