from Dice2 import Die

class Angry_roll:
    def __init__(self):
        self.dice_a = Die([1,2,"angry",4,5,6]) #Creates dice a
        self.dice_b = Die([1,2,"angry",4,5,6]) #Creates dice b
        self.stage = 1
        self.prompt_user() #prompts user for die choice

    def describe_game(self):
        #Describes game
        print("Welcome to angry dice.")

    def prompt_user(self):
        #Tells user to press enter to continue
        input("Press Enter to begin ")

    def display(self,a,b):
        #Displays what is rolled
        print("Stage {}".format(self.stage))
        print("----------------")
        print("You rolled:")
        print("   a = [ {} ]".format(a))
        print("   b = [ {} ]".format(b))
        print("----------------")

    def roll_choice(self):
        #Prompts user to roll dice and returns choice
        dice = input("Please choose which dice you'd like to roll (a, b). Type 'ab' or 'ba' to roll both die: ")
        return dice

    def roll_condition(self,a,b, dice):
    #returns roll conditions

        #if player chooses a, roll a
        if "a" in dice:
            a = self.dice_a.roll()
        #if player chooses b, roll b
        if "b" in dice:
            b = self.dice_b.roll()
        else:
        #if player doesn't input a or b, tell user they are wrong
            print("That is not a valid input")
        return(a, b)

    def roll_dice(self,a,b):
    #Gets user choice and rolls die based on it
        dice = self.roll_choice() #Rolls dice and sets value to variable dice
        if self.cheat(a,b,dice) == False:
            a,b = self.roll_condition(a,b,dice)

        return(a, b)

    def count_stage(self,a,b):
        #Returns the the die stage

        #if both dice are angry, reset to the first stage
        if (self.stage != 1 and a=="angry" and b=="angry"):
            print("Oh no! You've gone back to stage 1")
            return 1

        else:
            #if dice land on 1 and 2 on stage 1, got to stage 2
            if self.stage == 1:
                if (a == 1 and b ==2) or (b == 1 and a == 2):
                    print("You are in stage 2")
                    return 2
            #If dice land on 3 and 4 on stage 2, go to stage 3
            elif self.stage == 2:
                if (a == "angry" and b == 4) or (b == "angry" and a == 4):
                    print("You are in stage 3")
                    return 3
            #if dice land on 5 and 6 on stage 3, got to stage 4 for victory
            elif self.stage == 3:
                if (a == 5 and b == 6) or (b == 5 and a == 6):
                    return 4
            #Returns the stage the player is on
            return self.stage

    def cheat(self, a,b, dice):
        #Determines whether user is cheating by holding a value of 6
        if (self.stage == 3 and a == 6 and b != 5 and dice == "b") or self.stage == 3 and b == 6 and a != 5 and dice == "a": #Set conditions for cheating
            print ("Cheater!")
            return True #return True if cheater
        return False #return false if not cheater

    #Initiates Game
    def main(self):
    #starts game and calls other functions

        #defines initial rolls for both die
        a, b = "none", "none"

        #Describes game to player
        self.describe_game()

        #Allows player to play while stage doesn't equal 4
        while self.stage != 4:
            #Rolls dice
            a, b = self.roll_dice(a, b)
            #Displays the rolled dice
            self.display(a, b)
            #Increments the stage until game is won
            self.stage = self.count_stage(a, b)
        #Win statement
        print("You win! calm down")


aroll = Angry_roll()
aroll.main()
