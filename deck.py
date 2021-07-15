# import the Card class and Random from python lib
from card import Card, Ace
import random
class Deck:
    def __init__(self):
        # array to store all the cards
        self.cards = []
        # initalize a built deck of 52 cards of 4 suits
        self.build() 
        self.count = 52

    def build(self):
        # use double for loops to create Card objects
        # loop through each suit and make a Card Object of each rank 
        suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
        ranks = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
        for s in suits:
            for r in ranks:
                # find rank's int value first: either int("number") or Jack/Queen/King=10, Ace=1 and 11
                # then, add the new Card Object to the deck of cards
                
                # if r in {Jack/Queen/King} -> numVal = 10
                if r in {"Jack","Queen","King"}:
                    self.cards.append(Card(s,r,10))
                # if r = Ace -> numVal = 1, numVal2 = 11
                elif r == "Ace":
                    self.cards.append(Ace(s,r,11,1))
                # else -> numVal = int(r)
                else:
                    self.cards.append(Card(s,r,int(r)))
                

    def printDeck(self):
        # loop through and print all the cards from the deck (use Card.py's show() function)
        for card in self.cards:
            card.show()

    def shuffle(self):
        # shuffle cards in the deck
        # no return value, just shuffle the deck. If you want to show the deck, call printDeck()
        random.shuffle(self.cards)

 # what happens when there are no cards in the deck?  
 # make a function to check if deck has any cards left
 # OR use a class exception for empty card deck (link in discord server) 
    def topCard(self):
        # pop off the top card (index=0) of the deck. Return Card Object
        topCard = self.cards.pop(0)
        self.count -= 1
        return topCard

    # return random card from anywhere in the deck
    def randomCard(self):
        # get total number of cards left in deck for stop range
        numCards = len(self.cards)
        # randomly select cards from 0 to len-1
        ranCard = random.randint(0, numCards-1)
        # print("\t random card is {}".format(ranCard))
        self.count -= 1
        return self.cards.pop(ranCard)



# deck = Deck()
# deck.printDeck()
# deck.shuffle()
# deck.printDeck()
# top = deck.topCard()
# print("\nAnd the top card of your shuffled deck is: ")
# top.show()
# print("\nAnd a random card of your shuffled deck selected is: ")
# print(deck.randomCard().show())

# Test 2 - June 30/2021
# Testing Card Object's new attribute numVal and numVal2 are working at deck creation
# deck = Deck()
# deck.shuffle()
# print("\nAnd a random card of your shuffled deck selected is: ")
# r = deck.randomCard()
# r.show()
# print(r.numVal)

# # Test 3 - July 6/2021
# # Testing refractored Card class (making new inherited Ace class for numVal2) to see if both Ace values appear
# if r.value == "Ace":
#     print(r.numVal2)


