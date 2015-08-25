class Monster:
    def __init__(self):
        self.name = "Mothra"
        self.status = "Out of Tokyo"
        self.health = 10
        self.victory_points = 0

    def reset(self):
        """resets health and victory points"""
        self.health = 10
        self.victory_points = 0

    def in_tokyo(self):
        """checks status"""
        if self.status == "In Tokyo":
            return True
        return False

    def flee(self):
        """monster flees"""
        flee = None
        while "y" not in flee or "n" not in flee:
            flee = input("Do you want to flee Tokyo? (y / n) ")
            if "y" in flee: #Monster flees
                return True
            elif "n" in flee: #Monster stays
                return False
            elif "y" in flee and "n" in flee: #Monster confused
                print("Yes or no? You must choose one. ")
                continue


    def heal(self,heal_amount):
        """monster flees"""
        if heal_amount <= (10-self.health):
            self.health += heal_amount
        else:
            return 10

    def attack(self, dmg_amount):
        """monster takes damage"""
        self.health -= dmg_amount
        if self.health > 0:
            return self.health
        else:
            self.status = "K.O.'d"
            print(self.status)
            return self.health

    def score(self, points):
        """Monster is victorious"""
        self.victory_points +- points
        if self.victory_points >= 20:
            self.status = "WINNING"
            print(self.status)
            return self.victory_points
        else:
            return self.victory_points
