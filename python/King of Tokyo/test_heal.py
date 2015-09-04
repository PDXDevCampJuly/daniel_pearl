__author__ = 'DanielPearl'

import unittest
from monster import Monster
from unittest.mock import patch
from io import StringIO

#Tests heal function
class test_heal(unittest.TestCase):
    def setUp(self):
        self.monsta = Monster()
         print(self.shortDescription())

    def test_valid_heal(self):
        """
        :return: health of monster int
        """
        self.monsta.health = 4
        expected = 9
        actual = self.monsta.heal(5)
        assertEqual(expected, actual)

    def test_invalid_heal(self):
        """
        :return: health of monster int
        """
        self.monsta.health = 7
        expected = 10
        actual = self.monsta.heal(5)
        assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
