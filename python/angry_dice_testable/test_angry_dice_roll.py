from angry_dice_testable import Angry_roll

class Angry_roll(unittest.TestCase):

    def test_roll_empty_list(self):
        angry_game = AngryDiceGame()
        exception = False

        try:
            self.assertangry_game.roll_the_dice([])
        except:
            exception = True

        self.assertFalse(exception)

    def test_roll_invalid_input(self):
        angry_game = Angry_roll()

        try:
            angry_game.roll_the_dice(2)
        except TypeError:
            self.assertTrue(False, "Invalid type passed and not handled")
if __name__ == '__main__':
    unittest.main()