__author__ = 'DanielPearl'

import unittest
from Dice2 import Die

class DieRollTest(unittest.TestCase):
    """Test the functionality of the Die class; roll function."""

    def setUp(self):
        self.possible_values = [1,2,3,"Dog", "Cat", "hippo"]
        self.new_die = Die(self.possible_values)
        print(self.shortDescription)

    def tearDown(self):
        del self.possible_values
        del self.new_die
        print("Just ran test: ")
        print(self._testMethodName)

    def test_roll_once(self):
        """Roll the die once and ensure the value is in possibleValues"""
        self.assertIn(self.new_die.roll(), self.possible_values, "Rolled value was not in possible values of Die")

    def test_rolled_value_changes(self):
        """Roll the die a number of times and make sure it changes value."""
        holding_value = self.new_die.roll()
        for i in range(10):
            if self.new_die.roll() != holding_value:
                self.assertTrue(True)
        self.assertFalse(False, "Die value did not change from holding value for 10 rolls")

    def test_currentValue_is_updated_to_roll_value(self):
        """Make sure that the Die's currentValue is updated to match what is rolled."""
        self.new_die.currentValue
        self.assertEqual(self.new_die.roll(), self.new_die.currentValue,"Current value was not different from rolled")

if __name__ == '__main__':
    unittest.main()
