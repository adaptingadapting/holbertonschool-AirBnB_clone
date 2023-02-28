#!/usr/bin/python3
""" test module for review class """

from models.review import Review

import unittest


class test_review(unittest.TestCase):
    """ tests the review class and its methods """

    def test_place_id(self):
        """ tests places id initliaziation """

        rev = Review()
        self.assertTrue(rev.place_id == "")

    def test_user_id(self):
        """ tests users id initliazation """

        rev = Review()
        self.assertTrue(rev.user_id == "")

    def test_text(self):
        """ test text initialization and assignment """

        rev = Review()
        self.assertTrue(rev.text == "")
        rev.text = "bad place"
        self.assertTrue(rev.text == "bad place")
