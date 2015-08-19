__author__ = 'DanielPearl'

import unittest
from monster import Monster

#Tests reset
class test_reset(unittest.TestCase):
    def setUp(self):
        self.monsta = Monster()

    #Tests if stats reset
    def test_reset(self):
        self.monsta.health = 5
        self.monsta.victory_points = 5
        self.monsta.reset()
        if self.monsta.health == 10 and self.monsta.victory_points == 0:
            self.reset = True

        self.assertTrue(self.reset, "Monster does not reset")


if __name__ == '__main__':
    unittest.main()
