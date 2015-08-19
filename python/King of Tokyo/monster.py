class Monster:
    def __init__(self):
        self.name = "Mothra"
        self.status = "Out of Tokyo"
        self.health = 10
        self.victory_points = 0

    def reset(self):
        self.health = 10
        self.victory_points = 0

    def in_tokyo(self):
    #checks status
        if self.status == "In Tokyo":
            return True

    def flee(self):
    #monster flees
        #prompt monster to flee
        flee = input("Do you want to flee Tokyo? (y / n)")
        #flee
        if "y" in flee:
            return True
        #don't flee
        if "n" in flee:
            return False
        #Invalid statement
        if "y" not in flee and n not in flee:
            print ("Invalid statement.")

    def heal(self,heal_amount):
    #Heals monster
        #heals monster if heal amount doesn't excede 10
        if heal_amount <= (10-self.health):
            self.health += heal_amount
        #Error message is heal amount excedes 10
        else:
            print ("Invalid heal amount")
            return self.health

    def attack(self, dmg_amount):
    #damages monster
        #returns health amount from dmg
        if self.health > 0:
            return self.health +- dmg_amount
        #returns KO if dmg greater than health
        else:
            print("K.O.'d")
            return self.health +- dmg_amount

