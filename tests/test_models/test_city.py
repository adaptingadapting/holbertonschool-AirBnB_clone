#!/usr/bin/python3
""" module for testing city class """

from models.city import City

import unittest


class test_city(unittest.TestCase):
    """ tests the city class and its attributes """

    def test_state_id(self):
        """ tests stated ids initialization and assignment """

        kansas_city = City()
        self.assertTrue(kansas_city.state_id == "")
        kansas_city.state_id = "kansas"
        self.assertTrue(kansas_city.state_id == "kansas")

    def test_name(self):
        """ tests name initialization and assignment """

        kansas_city = City()
        self.assertTrue(kansas_city.name == "")
        kansas_city.name = "kc"
        self.assertTrue(kansas_city.name == "kc")
