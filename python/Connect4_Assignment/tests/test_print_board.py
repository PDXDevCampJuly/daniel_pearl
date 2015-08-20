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
    def test_print_board(self, mock_stdout):
        """test if a board is printed correctly."""
        printed_board = \
            ("| - | - | - | - | - | - | - |"
             "| - | - | - | - | - | - | - |"
             "| - | - | - | - | - | - | - |"
             "| - | - | - | - | - | - | - |"
             "| - | - | - | - | - | - | - |"
             "| - | - | - | - | - | - | - |")
        board = [[], [], [], [], [], [], []]
        self.test_view.print_board(board)
        self.assertEqual(printed_board, mock_stdout.getvalue())



if __name__ == '__main__':
    unittest.main()
