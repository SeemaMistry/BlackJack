class Card:
    def __init__(self, suit, value, numVal, numVal2=0):
        self.suit = suit # Spades, Clubs, Hearts, Diamonds
        self.value = value # 2-10, Jack, Queen, King, Ace
        self.numVal = numVal # int value of the card
        self.numVal2 = numVal2 # FOR Ace ONLY! 2 values: 1 or 11. 11 value goes here, 1 goes in numVal

    def show(self):
        # print to console example: 
        # 6 of Clubs
        print ("{} of {}".format(self.value, self.suit))

    def strShow(self):
        # return str of show(self)
        return ("{} of {}".format(self.value, self.suit))


