__author__ = 'DanielPearl'

import unittest
from monster import Monster
from unittest.mock import patch
from io import StringIO

#Tests Attack
class test_attack(unittest.TestCase):
    def setUp(self):
        self.monsta = Monster()
        print(self.shortDescription())

    #Tests if heal function works
    def test_attack_live(self):
        self.monsta.health = 6
        expected = 1
        actual = self.monsta.attack(5)
        self.assertEqual(expected, actual)

    #Heal function should not work if total > 10
    def test_attack_die(self):
        self.monsta.health = 4
        expected = -1
        actual = self.monsta.attack(5)
        self.assertEqual(expected, actual)

    #Tests if invalid output was printed
    @patch ('sys.stdout', new_callable=StringIO)
    def test_attack_die_KO(self, mock_stdout):
        health = self.monsta.health(4)

        expected = "K.O.'d"
        actual = self.monsta.attack(6)
        self.assertNotEqual(mock_stdout.getValue(), text)


if __name__ == '__main__':
    unittest.main()
