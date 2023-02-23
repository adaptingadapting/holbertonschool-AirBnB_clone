#!/usr/bin/python3
"""Console AirBnB Clone"""


import uuid
from datetime import datetime


class BaseModel:
    """class BaseModel"""

    def __init__(self):
        """__init__ method"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """string representation of an object
        Return: String representation of an object
        """
        return (f"[{type(self).__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """method to updates 'updated_at' with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """method to create a dictionary with all key/value of __dict__
        of instance
        Return:
            dictionary with all key/value of __dict__ of instance
        """
        dictionary = dict(self.__dict__)
        dictionary["__class__"] = type(self).__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return (dictionary)
