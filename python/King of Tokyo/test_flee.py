__author__ = 'DanielPearl'

import unittest
from monster import Monster
from unittest.mock import patch
from io import StringIO

#Tests Flee
class test_flee(unittest.TestCase):
    def setUp(self):
        self.monsta = Monster()

    @patch ('sys.stdout', new_callable=StringIO)
    def test_flee_true(self, mock_stdout):
        pass

    @patch ('sys.stdout', new_callable=StringIO)
    def test_flee_false(self, mock_stdout):
        pass

if __name__ == '__main__':
    unittest.main()
