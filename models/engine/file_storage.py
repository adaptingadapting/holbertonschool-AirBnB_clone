#!/usr/bin/python3
""" module for file storage handling """

import json


class FileStorage:
    """ defines a class that serializes and de serializes with json """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the objects dictionary """

        return self.__objects

    def new(self, obj):
        """ sets the objects dict """

        self.__objects.update({f"{obj.__class__.__name__}.{obj.id}": obj})

    def save(self):
        """ serializes objects to a json file """

        new_dict = {}
        for key, value in self.__objects.items():
            new_dict.update({key: value.to_dict()})
        with open(self.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """ deserializes objects from a json file """

        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        classes = {
                "BaseModel": BaseModel,
                "User": User,
                "Place": Place,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Review": Review,
                  }

        try:
            with open(self.__file_path, "r") as f:
                json_dict = json.load(f)
            for value in json_dict.values():
                self.new(classes[value["__class__"]](**value))
                """
                the object being sent to new() is a
                base mode instance initialized with
                value kwargs
                """
        except IOError:
            pass
