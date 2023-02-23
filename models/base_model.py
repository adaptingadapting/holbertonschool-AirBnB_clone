#!/usr/bin/python3
"""Console AirBnB Clone"""


import uuid
from datetime import datetime


class BaseModel:
    """class BaseModel"""

    def __init__(self, *args, **kwargs):
        """__init__ method
        Args:
            *args: no_keyword argument
            **kwargs:keyword argument
        """
        if len(kwargs) > 0 and kwargs is not None:
            for key, val in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """string representation of an object
        Return: String representation of an object
        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

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
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return (dictionary)
