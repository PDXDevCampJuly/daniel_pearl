__author__ = 'DanielPearl'


class C4Model:

    """Connect 4 model"""

    def __init__(self):
        self.board = self.make_board()
        self.players = []

    def make_board(self):
        """
        Creates empty board
        :return: 2D array
        """
        board = []
        for row in range(7):
            board.append(["-"]*6)
        return board

    def get_player(self, player_postion):
        """
        :param player_postion: position of player
        :return: player str
        """
        return self.players[player_postion-1]

    def set_player(self, name):
        """
        :param name: Player name
        :return: player name
        """
        return self.players.append(name)

    def get_column(self, col_num):
        """
        Given column, return row
        :param col_num: column number as int
        :return: list of pieces
        """
        if len(self.board) < col_num:
            return []
        return self.board[col_num-1]

    def get_row(self, row_num):
        """
        Given row, return column
        :param row_num: row number as int
        :return: dictionary
        """
        pass

    def add_piece(self, col_num, player):
        """
        :param col_num: column int
        :param player: player
        :return: true if successful
        """
        pass