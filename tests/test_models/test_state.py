#!/usr/bin/python3
""" test module for state class """

from models.state import State

import unittest


class test_state(unittest.TestCase):
    """ tests the states class attribute """

    def test_name(self):
        """ tests the assignment and initlalization of name """

        state = State()
        self.assertTrue(state.name == "")
        state.name = "JayZ"
        self.assertTrue(state.name == "JayZ")
