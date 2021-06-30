# import the Card class and Random from python lib
from card import Card
import random
class Deck:
    def __init__(self):
        # array to store all the cards
        self.cards = []
        # initalize a built deck of 52 cards of 4 suits
        self.build() 

    def build(self):
        # use double for loops to create Card objects
        # loop through each suit and make a Card Object of each rank 
        suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
        ranks = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
        for s in suits:
            for r in ranks:
                # add the new Carb Object to the deck of cards
                self.cards.append(Card(s,r))

    def printDeck(self):
        # loop through and print all the cards from the deck (use Card.py's show() function)
        for card in self.cards:
            card.show()

    def shuffle(self):
        # shuffle cards in the deck
        # no return value, just shuffle the deck. If you want to show the deck, call printDeck()
        random.shuffle(self.cards)
    
    def topCard(self):
        # pop off the top card (index=0) of the deck. Return Card Object
        topCard = self.cards.pop(0)
        return topCard

    # return random card from anywhere in the deck
    def randomCard(self):
        # get total number of cards left in deck for stop range
        numCards = len(self.cards)
        # randomly select cards from 0 to len-1
        ranCard = random.randint(0, numCards-1)
        # print("\t random card is {}".format(ranCard))
        return self.cards.pop(ranCard)



deck = Deck()
#deck.printDeck()
deck.shuffle()
deck.printDeck()
top = deck.topCard()
print("\nAnd the top card of your shuffled deck is: ")
top.show()
print("\nAnd a random card of your shuffled deck selected is: ")
deck.randomCard().show()



