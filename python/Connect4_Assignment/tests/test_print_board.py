__author__ = 'DanielPearl'

import unittest
from unittest.mock import patch
from io import StringIO

from c4_view import C4View

class PrintBoardTest(unittest.TestCase):
    """ Tests if winning statement is printed."""
    # TODO add error messages.

    def setUp(self):
        self.test_view = C4View()
        print(self.shortDescription())

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_empty_board(self, mock_stdout):
        """test if a board is printed correctly."""
        printed_board = \
                ("    1   2   3   4   5   6   7\n"
                "1 | - | - | - | - | - | - | - |\n"
                "2 | - | - | - | - | - | - | - |\n"
                "3 | - | - | - | - | - | - | - |\n"
                "4 | - | - | - | - | - | - | - |\n"
                "5 | - | - | - | - | - | - | - |\n"
                "6 | - | - | - | - | - | - | - |\n")

        board = [['-', '-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-']]
        self.test_view.print_board(board)
        self.assertEqual(printed_board, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_board(self, mock_stdout):
        """test if a board is printed correctly."""
        printed_board = \
                ("    1   2   3   4   5   6   7\n"
                "1 | - | - | - | - | - | - | - |\n"
                "2 | - | - | - | - | - | - | - |\n"
                "3 | - | - | - | - | - | - | - |\n"
                "4 | - | - | - | - | - | - | - |\n"
                "5 | - | - | - | - | - | - | - |\n"
                "6 | x | - | - | - | - | - | - |\n")

        board = [['-', '-', '-', '-', '-', 'x'],
                 ['-', '-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-']]
        self.test_view.print_board(board)
        self.assertEqual(printed_board, mock_stdout.getvalue())

    # def test_print_invalid_board(self):
    #     """test does our handle invalid board sizes."""
    #     board = [['-', '-', '-', '-', '-', 'x'],
    #              ['-', '-', '-', '-', '-', '-'],
    #              ['-', '-', '-', '-', '-', '-'],
    #              ['-', '-', '-', '-', '-', '-'],
    #              ['-', '-', '-', '-', '-', '-'],
    #              ['-', '-', '-', '-', '-', '-']
    #              ]
    #
    #     with self.assertRaises(ValueError):
    #         self.test_view.print_board(board)

if __name__ == '__main__':
    unittest.main()
