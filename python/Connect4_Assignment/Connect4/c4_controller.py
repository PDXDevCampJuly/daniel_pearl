__author__ = 'DanielPearl'
from c4_view import C4View
from c4_model import C4Model


class C4Controller:

    """Connect 4 controller"""

    def __init__(self):
        self.model = C4Model()
        self.view = C4View()
        # self.player_turn = self.model.get_player()

    def update_board(self, col_num):
        """
        :param col_num: column number int, player str
        :param player: Player name str
        """
        pass

    def check_winner(self, col_num, row_num):
        """
        :param board: board list
        :return: winning player
        """
        pass

    def check_tie(self, col_num, row_num):
        """
        :param board: board list
        :print: no more moves, players tie
        """
        pass

    def get_player_names(self):
        """
        gets player name and sets player
        """
        player1, player2 = "Player1", "Player2"
        while player1 != "" and player2 != "":
            if player1 == "Player1" or player1 == "":
                player1 = self.view.prompt_name(1)
            if player2 == "Player2" or player2 == "":
                player2 = self.view.prompt_name(2)

        self.model.set_player(player1)
        self.model.set_player(player2)

    def turn_validator(self, dirty_input):
        """
        :param dirty_input: raw input from user
        :return: number of column
        """
        pass

    def get_turn(self):
        """
        loops turns between players
        """
        pass

    def main(self):
        pass

