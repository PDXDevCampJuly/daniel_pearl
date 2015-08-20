__author__ = 'DanielPearl'
from c4_view import C4View
from c4_model import C4Model


class C4Controller:

    """Connect 4 controller"""

    def __init__(self):
        self.model = C4Model()
        self.view = C4View()
        self.player_turn = self.model.get_player()

    def update_board(self, col_num, player):
        """
        :param col_num: column number int, player str
        :param player: Player name str
        """
        pass

    def check_winner(self, board):
        """
        :param board: board list
        :return: winning player
        """
        pass

    def check_tie(self, board):
        """
        :param board: board list
        :print: no more moves, players tie
        """
        pass

    def get_player_name(self):
        """
        gets player name and sets player
        """
        pass

    def update_turn(self):
        """
        sets player turn
        """
        pass

    def turn_validator(self, dirty_input):
        """
        :param dirty_input: raw input from user
        :return: number of column
        """
        pass

    def get_turn(self):
        """
        loops tunrns between players
        """
        pass

    def main(self):
        pass

