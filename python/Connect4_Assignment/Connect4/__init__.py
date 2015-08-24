__author__ = 'DanielPearl'

from c4_controller import C4Controller

class Connect4:
    def __init__(self):
        new_game = C4Controller()
        new_game.main()