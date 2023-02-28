#!/usr/bin/python3
""" test module for file storage """

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

import unittest
import os


class test_file_storage(unittest.TestCase):
    """ tests the file storage class and its methods and attrs """

    def test_all(self):
        """ tests the all method """

        storage = FileStorage()
        new_model = BaseModel()
        key = f"BaseModel.{new_model.id}"

        storage.new(new_model)
        self.assertTrue(key in storage.all().keys())
        self.assertEqual(type(storage.all()), dict)

    def test_new(self):
        """ test new method """

        storage = FileStorage()
        new_model = BaseModel()
        key = f"BaseModel.{new_model.id}"

        storage.new(new_model)
        self.assertTrue(key in storage.all().keys())

    def test_save(self):
        """ tests the save  method """

        storage = FileStorage()
        new_model = BaseModel()
        key = f"BaseModel.{new_model.id}"
        
        try:
            os.remove("file.json")
        except IOError:
            pass

        storage.new(new_model)
        storage.save()
        storage.all().clear()
        storage.reload()
        self.assertTrue(key in storage.all())

    def test_reload(self):
        """ tests the reload method """

        storage = FileStorage()
        new_model = BaseModel()
        key = f"BaseModel.{new_model.id}"
        
        try:
            os.remove("file.json")
        except IOError:
            pass

        storage.new(new_model)
        storage.save()
        storage.all().clear()
        storage.reload()
        self.assertTrue(key in storage.all())
