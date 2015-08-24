__author__ = 'DanielPearl'

import unittest
from unittest.mock import patch
from c4_controller import C4Controller
from c4_model import C4Model

class GetPlayerTest(unittest.TestCase):
    def setUp(self):
        self.controller = C4Controller()
        self.model = C4Model()
        print(self.shortDescription())

    @patch('builtins.input', side_effects=["Mr. Smith", "Mr. Joe"])
    def test_valid_player(self, mock_stdin):
        self.controller.get_player_names()
        expected_player_list = ["Mr. Smith", "Mr. Joe"]
        actual_player_list = self.model.players
        self.assertEqual(expected_player_list, actual_player_list)

    @patch('builtins.input', side_effects=["", "", "Why Hello", "Yes"])
    def test_valid_player(self, mock_stdin):
        self.controller.get_player_names()
        expected_player_list = ["Why Hello", "Yes"]
        actual_player_list = self.model.players
        self.assertEqual(expected_player_list, actual_player_list)

if __name__ == '__main__':
    unittest.main()
