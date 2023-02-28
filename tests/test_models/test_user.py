#!/usr/bin/python3
""" tests module for the user class """

from models.user import User

import unittest


class test_user(unittest.TestCase):
    """ tests the user class and its attributes """

    def test_first_name(self):
        """ tests initiliazation and assignenmt """

        user = User()
        self.assertEqual(user.first_name, "")
        user.first_name = "gabriel"
        self.assertEqual(user.first_name, "gabriel")

    def test_last_name(self):
        """ tests initiliazation and assignenmt """

        user = User()
        self.assertEqual(user.last_name, "")
        user.last_name = "agustin"
        self.assertEqual(user.last_name, "agustin")

    def test_email(self):
        """ tests initiliazation and assignenmt """

        user = User()
        self.assertEqual(user.email, "")
        user.email = "blasina"
        self.assertEqual(user.email, "blasina")

    def test_pass(self):
        """ tests initiliazation and assignenmt """

        user = User()
        self.assertEqual(user.password, "")
        user.password = "curutchet"
        self.assertEqual(user.password, "curutchet")
