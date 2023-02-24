#!/usr/bin/python3
""" airbnb file storage module """

import json


class FileStorage:
    """ file storage class """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns objects dictionary """
        return self.__objects

    def new(self, obj):
        """ sets in object dict the new obj with key obj.id """
        self.__objects.update({f"{obj.__class__.__name__}.{obj.id}":obj})

    def save(self):
        """ serializes the obj dict to json file """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """ deserliazes the objects from json file """
        try:
            with open(self.__file_path, "r") as f:
                objects = json.load(f)
            for key, value in objects.items():
                self.new(value)
        except IOError:
            pass
