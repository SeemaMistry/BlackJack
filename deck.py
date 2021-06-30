# import the Card class
from card import Card
class Deck:
    def __init__(self):
        self.cards = []
        # initalize a built deck of 52 cards of 4 suits
        self.build() 

    def build(self):
        # use double for loops to create Card objects
        # Make 4 ranks of each suit
        suits = ["Spade", "Clubs", "Hearts", "Diamonds"]
        ranks = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
        for s in suits:
            for r in ranks:
                #print ("{} of {}".format(r,s))
                self.cards.append(Card(s,r))

    def printDeck(self):
        # loop through and print all the cards from the deck (use Card.py's show() function)
        for card in self.cards:
            card.show()

deck = Deck()
deck.printDeck()