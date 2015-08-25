__author__ = 'DanielPearl'

import unittest
from monster import Monster

#Tests status
class test_in_tokyo(unittest.TestCase):
    def setUp(self):
        self.monsta = Monster()
        print(self.shortDescription())

    def test_in_toyko_valid(self):
        """
        Tests if monster shows up in Tokyo
        :return: Boolean
        """
        self.monsta.status = "In Tokyo"

        actual = self.monsta.intokyo()
        self.assertTrue(actual)

    def test_in_tokyo_false(self):
        """
        Tests if monster does not shows up in Tokyo
        :return: Boolean
        """
        self.monsta.status = "Out of Tokyo"

        actual = self.monsta.intokyo()
        self.assertFalse(actual)

if __name__ == '__main__':
    unittest.main()
