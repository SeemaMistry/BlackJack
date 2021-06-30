class Card:
    def __init__(self, suit, value):
        self.suit = suit # Spades, Clubs, Hearts, Diamonds
        self.value = value # 2-10, Jack, Queen, King, Ace

    def show(self):
        # print to console example: 
        # 6 of Clubs
        print ("{} of {}".format(self.value, self.suit))

