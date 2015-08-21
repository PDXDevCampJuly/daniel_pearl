__author__ = 'DanielPearl'

import unittest
from angry_dice_testable import Angry_roll

class Test_roll_dice(unittest.TestCase):
    def setUp(self):
        self.angry = Angry_roll()

    def test_pass_a_nocheat(self):
        self.angry.dice_a.currentValue = "8"

        self.angry.roll_dice("a")
        self.assertEqual(self.angry.dice_a.currentValue, 8, "Die a was not rolled")

    def test_pass_b_nocheat(self):
        self.angry.dice_b.currentValue = "8"

        self.angry.roll_dice("b")
        self.assertEqual(self.angry.dice_b.currentValue, 8, "Dice b was not rolled")

    def test_pass_ab_nocheat(self):
        self.angry.dice_a.currentValue = "8"
        self.angry.dice_b.currentValue = "8"

        self.angry.roll_dice("ab")
        self.assertEqual(self.angry.dice_b.currentValue, 8, "Dice b was not rolled")

    def test_pass_b_cheat(self):
        self.angry.dice_a.currentValue = "6"
        self.angry.dice_b.currentValue = "8"

        self.angry.roll_dice("b")
        self.assertEqual(self.angry.dice_b.currentValue, 8, "Dice b was rolled")

    def pass_a_cheat(self):
        self.angry.dice_a.currentValue"
        self.angry.dice_b.currentValue = "6"

        self.angry.roll_dice("b")
        self.assertEqual(self.angry.dice_a.currentValue, 8, "Dice a wase, "Die we not rolled")

if __name__ == '__main__':
    unittest.main()
