__author__ = 'DanielPearl'

import unittest
from monster import Monster
from unittest.mock import patch
from io import StringIO

#Tests heal function
class test_heal(unittest.TestCase):
    def setUp(self):
        self.monsta = Monster()
        self.monsta.health = 5

    #Tests if monster heals
    def test_valid_heal(self):
        health = self.monsta.heal(5)

        self.assertEqual(health, 10, "Heal did not work")

    #Monster should not heal if sum > 10
    def test_invalid_heal(self):
        health = self.monsta.heal(6)

        self.assertNotEqual(health, 11, "Heal should not have worked")

    #Tests invalid output
    @patch ('sys.stdout', new_callable=StringIO)
    def test_attack_die_KO(self, mock_stdout):
        health = self.monsta.attack(6)

        text = "Invalid heal amount"
        self.assertNotEqual(mock_stdout.getValue(), text)

if __name__ == '__main__':
    unittest.main()
