#!/usr/bin/python3
""" test module for place class """

from models.place import Place

import unittest


class test_place(unittest.TestCase):
    """ tests the place class and its methods """

    def test_city_id(self):
        """ tests city id initlization and assignment """

        Uruguay = Place()
        self.assertTrue(Uruguay.city_id == "")
        Uruguay.city_id = "montevideo"
        self.assertTrue(Uruguay.city_id == "montevideo")

    def test_user_id(self):
        """ tests user id initialization and assignment """

        Uruguay = Place()
        self.assertTrue(Uruguay.user_id == "")
        Uruguay.user_id = "2"
        self.assertTrue(Uruguay.user_id == "2")

    def test_name(self):
        """ tests name initialization and assignment """

        Uy = Place()
        self.assertTrue(Uy.name == "")
        Uy.name = "Uruguay"
        self.assertTrue(Uy.name == "Uruguay")

    def test_desc(self):
        """ tests descriptions initliaztation and assignment """

        Uy = Place()
        self.assertTrue(Uy.description == "")
        Uy.description = "nice place"
        self.assertTrue(Uy.description == "nice place")

    def test_number_rooms(self):
        """ tests the initlialization of n rooms """

        Uy = Place()
        self.assertTrue(type(Uy.number_rooms) is int)
        self.assertTrue(Uy.number_rooms == 0)

    def test_number_bathroom(self):
        """ test the initialization of n bathrooms """

        uy = Place()
        self.assertTrue(type(uy.number_bathrooms) is int)
        self.assertTrue(uy.number_bathrooms == 0)

    def test_max_guest(self):
        """ test initliazation of max guest """

        arg = Place()
        self.assertTrue(type(arg.max_guest) is int)
        self.assertTrue(arg.max_guest == 0)

    def test_price_by_night(self):
        """ tests initliazation of price by night """

        arg = Place()
        self.assertTrue(type(arg.price_by_night) is int)
        self.assertTrue(arg.price_by_night == 0)

    def test_latitude(self):
        """ tests initlaization of latitude """

        arg = Place()
        self.assertTrue(type(arg.latitude) is float)
        self.assertTrue(arg.latitude == 0.0)

    def test_longitude(self):
        """ test initliaztion of longitude """

        arg = Place()
        self.assertTrue(type(arg.longitude) is float)
        self.assertTrue(arg.longitude == 0.0)

    def test_amenity_ids(self):
        """ tests assignemnt of amenity id """

        arg = Place()
        self.assertTrue(type(arg.amenity_ids) is list)
        self.assertTrue(arg.amenity_ids == [])
