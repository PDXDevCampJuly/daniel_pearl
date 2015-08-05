from random import shuffle

class Card:
    """
    Make an individual card.
    """
    dictionary = {
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "Jack": 10,
        "Queen": 10,
        "King": 10,
        "Ace": 11
    }

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.int_value = self.dictionary[value]

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)

class Deck:
    """
    Make a Deck from the Class class and actions for the Deck
    """
    def __init__(self):
        self.makeDeck()

    # for each item in 'values' list, it compares to the dictionary and retrieves the value
    def makeDeck(self):
        self.deck = []
        suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
        values = ["two","three","four","five","six","seven","eight","nine","ten","Jack", "Queen", "King","Ace"]

        # fills in deck completing four suits of 13 cards
        for i in suits:
            for j in values:
                self.deck.append(Card(j, i))

        # automatically shuffles the new deck
        shuffle(self.deck)

    # removes card from the deck
    def dealCard(self):
        return self.deck.pop()

class Player:
    """
    Make a Player and the options to hit, pass, show hand.
    """
    def __init__(self, playerName):
        self.playerName = playerName
        self.playerHand = []

    # gets a card from the deck and adds to the player's hand
    def hit(self, card):
        self.playerHand.append(card)

    # displays the player's hand
    def showHand(self):
        print("Player cards: ", end = " ")
        print(self.playerHand)

class Dealer:
    """
    Make a Dealer and the options to hit, pass, show hand
    """
    def __init__(self, dealerName):
        self.dealerName = dealerName
        self.dealerHand = []

    # gets a card from the deck and adds to the dealer's hand
    def hit(self, card):
        self.dealerHand.append(card)

    # displays the dealer's hand hiding the first card in the list
    def showHand(self):
        print("Dealer cards: ", end = " ")
        print("Hidden card &", end = " ")
        print(self.dealerHand[1:])

class BlackJack:
    def __init__(self, num_players):
        self.deck = Deck() # making a Deck instance
        self.deck.makeDeck() # making a Deck from the Deck instance
        self.dealer = Dealer("Batman") # making a Dealer instance
        self.playerList = [] # making a list of all players excl. Dealer
        self.makePlayers(num_players) # makes list based on the # of players
        self.startGame() # launches the game

    # asks for names of each player and populates a list of players
    def makePlayers(self, num_players):
        for i in range(num_players):
            playerName = input("Input Name: ")
            newPlayer = Player(playerName)
            self.playerList.append(newPlayer)

    # launches the game
    def startGame():
        count = 0
        for i in range(2):
            for each_player in playerList + count:
                each_player.hit()
                count += 1
            dealer.hit()

        print(playerList1)

        for each_player in range(playerList):
            each_player.showHand()
        dealer.show()



# TESTS
########################

# myDeck = Deck()
# myDeck.makeDeck()

# player1 = Player("Daniel")
# player1.hit(myDeck.dealCard())
# player1.hit(myDeck.dealCard())
#
# dealer = Dealer("Batman")
# dealer.hit(myDeck.dealCard())
# dealer.hit(myDeck.dealCard())
#
# print(len(myDeck.deck))
# player1.showHand()
# dealer.showHand()


newGame = BlackJack(2)
