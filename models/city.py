#!/usr/bin/python3
""" Defins city class """


from models.base_model import BaseModel


class City(BaseModel):
    """ defins the city, inherits from base model class """

    state_id = ""
    name = ""
