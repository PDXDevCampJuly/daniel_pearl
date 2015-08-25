__author__ = 'DanielPearl'

import unittest
from monster import Monster


class MonsterResetTest(unittest.TestCase):

    def setUp(self):
        self.monsta = Monster()
        print(self.shortDescription())

    def test_valid_health_reset(self):
        """
        Tests for valid health reset
        """
        self.monsta.health = 5
        self.monsta.reset()
        expected = 10
        actual = self.monsta.health

        assertEqual(expected, actual)

    def test_valid_victory_reset(self):
        """
        Tests for valid victory point reset
        """
        self.monsta.victory_points = 5
        self.monsta.reset()
        expected = 0
        actual = self.monsta.victory_points

        assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
