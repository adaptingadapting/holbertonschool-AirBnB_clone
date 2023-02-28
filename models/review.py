#!/usr/bin/python3
""" Defins review class """


from models.base_model import BaseModel


class Review(BaseModel):
    """ defins the user, inherits from base model class """

    place_id = ""
    user_id = ""
    text = ""
