class Card:
    def __init__(self, suit, value, numVal):
        self.suit = suit # Spades, Clubs, Hearts, Diamonds
        self.value = value # 2-10, Jack, Queen, King, Ace
        self.numVal = numVal # int value of the card

    def show(self):
        # print to console example: 
        # 6 of Clubs
        print ("{} of {}".format(self.value, self.suit))

    def strShow(self):
        # return str of show(self)
        return ("{} of {}".format(self.value, self.suit))

class Ace(Card):
    # FOR Ace ONLY! 2 values: 1 or 11
    def __init__(self, suit, value, numVal, numVal2):
        super().__init__(suit, value, numVal) # numVal = 11
        self.numVal2 = numVal2 # numVal2 = 1



