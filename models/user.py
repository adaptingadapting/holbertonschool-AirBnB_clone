#!/usr/bin/python3
""" Defins user class """


from base_model import BaseModel


class User(BaseModel):
    """ defins the user, inherits from base model class """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
