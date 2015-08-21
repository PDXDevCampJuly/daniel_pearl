__author__ = 'DanielPearl'

import unittest
from angry_dice_testable import Angry_roll
from unittest.mock import patch
from io import StringIO

class Test_roll_condition(unittest.TestCase):
    def setUp(self):
        self.angry = Angry_roll()

    def test_pass_a_b(self):
        self.angry.dice_a.currentValue = "8"
        self.angry.roll_condition("ab")
        self.assertEqual(self.angry.dice_a.currentValue, 8, "Die were not rolled")

    def test_pass_b(self):
        self.angry.dice_a.currentValue = "8"
        self.angry.roll_condition("b")
        self.assertEqual(self.angry.dice_a.currentValue, 8, "Die were not rolled")

    @patch ('sys.stdout', new_callable=StringIO)
    def test_pass_int(self, mock_stdout):
        self.angry.dice_a.currentValue = "8"
        self.angry.roll_condition("5")
        self.assertNotEqual(self.angry.dice_a.currentValue, 8, "Die were not rolled")

        angry_text = "That is not a valid input"
        self.assertNotEqual(mock_stdout.getvalue(), angry_text)

if __name__ == '__main__':
    unittest.main()
