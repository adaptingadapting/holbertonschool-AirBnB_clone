#!/usr/bin/python3
""" test module for base model with unittest """

import unittest
import os

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class test_base_model(unittest.TestCase):
    """ tests the base model class """

    def test_save(self):
        """ tests the save method """

        storage = FileStorage()
        storage.all().clear()
        my_model = BaseModel()
        try:
            os.remove("file.json")
        except IOError:
            pass
        my_model.save()
        try:
            with open("file.json", "r") as f:
                pass
            self.assertTrue(1)
        except IOError:
            self.assertTrue(0)

    def test_to_dict(self):
        """ tests wheter or not to dict works """

        new_base_model = BaseModel()
        self.assertIsInstance(new_base_model.to_dict(), dict)
        self.assertEqual(new_bae_model.id, new_base_model.to_dict()["id"])

    def test_self_id(self):
        """ tests wheter the model can be assigned an id """

        new_base_model = BaseModel()
        new_base_model.id = 1
        self.assertEqual(new_base_model.id, 1)

    def test_created_at(self):
        """ tests created at attribute """

        new_model = BaseModel()
        new_model.created_at = '1234-12-12'
        self.assertEqual(new_model.created_at, '1234-12-12')

    def test__str__(self):
        """ tests what str is returning """

        new_model = BaseModel()
        string = f"[BaseModel] ({new_model.id}) {vars(new_model)}"
        self.assertEqual(string, new_model.__str__())
