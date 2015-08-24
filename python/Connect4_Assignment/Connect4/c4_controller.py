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
        player1 = ""
        player2 = ""
        player_names_valid = False
        while not player_names_valid:
            if player1 == "":
                player1 = self.view.prompt_name(1)

            if player2 == "":
                player2 = self.view.prompt_name(2)

            if len(player1) > 0 and len(player2) > 0:
                player_names_valid = True

        self.model.set_player(player1)
        self.model.set_player(player2)

    def turn_validator(self, col_num):
        """
        :param dirty_input: raw input from user
        :return: number of column
        """

        if len(col_num) == 1 and col_num.isnumeric():

            int_col = int(col_num)

            if "-" in self.model.get_column(int_col) and int_col < 8:
                return True

        return False

    def main(self):
        pass

