__author__ = 'DanielPearl'

import unittest
from c4_model import C4Model

class GetDiagonalTest(unittest.TestCase):
    """Tests getting the diagonals based on pieces placement"""

    def setUp(self):
        self.model = C4Model()
        self.model.board = [['O', '-', '-', '-', '-', '-'],
                            ['-', 'O', '-', '-', '-', 'O'],
                            ['-', '-', 'O', '-', 'O', '-'],
                            ['X', 'X', 'X', 'O', 'X', 'X'],
                            ['-', '-', 'O', '-', 'O', '-'],
                            ['-', 'O', '-', '-', '-', 'O'],
                            ['O', '-', '-', '-', '-', '-']]
        print(self.shortDescription())

    def test_diagonal_all_values_in_grid(self):
        """tests diagonal get of all values within grid"""
        expected_list = ["O", "O", "O", "O", "O", "O"]
        actual_list = self.model.get_diagonal(4,4)
        self.assertEqual(expected_list, actual_list)


if __name__ == '__main__':
    unittest.main()
