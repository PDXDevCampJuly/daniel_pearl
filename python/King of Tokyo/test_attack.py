__author__ = 'DanielPearl'

import unittest
from monster import Monster
from unittest.mock import patch
from io import StringIO

#Tests Attack
class test_attack(unittest.TestCase):
    def setUp(self):
        self.monsta = Monster()
        self.monsta.health = 5

    #Tests if heal function works
    def test_attack_live(self):
        health = self.monsta.attack(5)

        self.assertEqual(health, 0, "Attack did not work")

    #Heal function should not work if total > 10
    def test_attack_die(self):
        health = self.monsta.attack(6)

        self.assertEqual(health, -1, "Attack did not work")

    #Tests if invalid output was printed
    @patch ('sys.stdout', new_callable=StringIO)
    def test_attack_die_KO(self, mock_stdout):
        health = self.monsta.attack(6)

        text = "That is not a valid input"
        self.assertNotEqual(mock_stdout.getValue(), text)


if __name__ == '__main__':
    unittest.main()
