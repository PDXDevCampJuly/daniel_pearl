__author__ = 'DanielPearl'

import unittest
from monster import Monster

#Tests status
class test_in_tokyo(unittest.TestCase):
    #Defines status
    def setUp(self):
        self.monsta = Monster()
        self.monsta.status = "In Tokyo"

    #Tests if monster shows up in Tokyo
    def test_in_toyko_true(self):
        tokyo = self.monsta.in_tokyo()

        self.assertTrue(tokyo, "Monster not showing up in Tokyo")

    #Tests if monster does not show up in Tokyo
    def test_in_tokyo_false(self):
        self.monsta.status = "Out of Tokyo"
        tokyo = self.monsta.in_tokyo()
        self.assertFalse(tokyo,"Monster is showing up in Tokyo")

if __name__ == '__main__':
    unittest.main()
