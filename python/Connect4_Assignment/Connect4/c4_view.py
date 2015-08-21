__author__ = 'DanielPearl'

class C4View:

    """Connect 4 view"""

    def __init__(self):
        pass

    def prompt_turn(self, name):
        """
        :param name: player name
        :return: return column choice
        """
        choice = input("{}, where would you like to go? ".format(name))
        return choice

    def show_instructions(self):
        """
         :print: instructions for game
        """
        print_statement = \
            ("1. On your turn, drop one of your discs into any slot in the top of "
             "the grid.\n"
             "2. Take turns until one player get four\nof their color discs in a"
             "row -\n"
             "horizontally, vertically, or diagonally\n"
             "3. The first player to 4-in-a-row wins!")
        print(print_statement, sep="", end="")

    def win_statement(self, name):
        """
        :param name: winning players name
        :print: game winner
        """
        winning_statement = \
            ("Congrats {} you've won!!!!").format(name)
        print(winning_statement)


    def tie_statement(self):
        """
        :print: game tied
        """
        tie_statement = \
            ("The board is full, no one wins X_x,"
             "basically you're both losers.")
        print(tie_statement)

    def print_board(self,board):
        """
        :print: board
        :param name: board list
        """
        print('    1   2   3   4   5   6   7')

        for y in range(6):

            print(y+1, end = ' ')

            for x in range(7):

                print("| {}".format(board[x][y]), end=' ')
            print('|')

    def prompt_name(self):
        """
        prompts user for name
        :return: str name entered by user
        """
        pass

if __name__ == '__main__':
    new = C4View()
    board = [['x', '-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-']]
    new.print_board(board)

