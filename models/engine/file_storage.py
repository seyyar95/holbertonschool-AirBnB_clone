#!usr/bin/python3
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        return self.__objects

    def new(self, obj):
       name = obj.__class__.__name__
       self.__objects["name"+obj.id] = obj
    
    def save(self):
        file = self.__file_path
        odict = self.__objects
        with open(file, "w") as f:
            json.dump(odict, f)

    def reload(self):
        file = self.__file_path
        try:
            with open(file, "r") as f:
                return json.load(f)
        except Exception:
            pass
