#!/usr/bin/python3
""" test module for amenity class """

from models.amenity import Amenity

import unittest


class test_amenity(unittest.TestCase):
    """ tests amenity attribute """

    def test_name(self):
        """ test name initialization and assignemnt """

        food = Amenity()
        self.assertTrue(food.name == "")
        food.name = "bananas"
        self.assertTrue(food.name == "bananas")
