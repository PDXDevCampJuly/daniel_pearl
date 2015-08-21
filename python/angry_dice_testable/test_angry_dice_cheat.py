__author__ = 'DanielPearl'

import unittest
from angry_dice_testable import Angry_roll
from unittest.mock import patch
from io import StringIO

class Test_roll_dice(unittest.TestCase):
    def setUp(self):
        self.angry = Angry_roll()

    def test_nocheat_a(self):
        self.angry.stage = 3

        returned_value = self.angry.cheat(5,6,"a")
        self.assertFalse(returned_value, "Non cheater caught for cheating")

    def test_nocheat_b(self):
        self.angry.stage = 3

        returned_value = self.angry.cheat(5,6,"b")
        self.assertFalse(returned_value, "Non cheater caught for cheating")

    def test_nocheat_stage_a(self):
        self.angry.stage = 2

        returned_value = self.angry.cheat(1,6,"a")
        self.assertFalse(returned_value, "Non cheater caught for cheating")

    def test_nocheat_stage_b(self):
        self.angry.stage = 2

        returned_value = self.angry.cheat(1,6,"b")
        self.assertFalse(returned_value, "Non cheater caught for cheating")

    @patch ('sys.stdout', new_callable=StringIO)
    def test_cheat_a(self, mock_stdout):
        self.angry.stage = 3
        angry_text = "Cheater!"

        returned_value = self.angry.cheat(1,6,"a")
        self.assertTrue(not returned_value, "Cheater got away with cheating")
        self.assertTrue(not mock_stdout.getvalue(), angry_text)

    @patch ('sys.stdout', new_callable=StringIO)
    def test_cheat_b(self, mock_stdout):
        self.angry.stage = 3
        angry_text = "Cheater!"

        returned_value = self.angry.cheat(1,6,"b")
        self.assertTrue(not returned_value, "Cheater got away with cheating")
        self.assertTrue(not mock_stdout.getvalue(), angry_text)

if __name__ == '__main__':
    unittest.main()
