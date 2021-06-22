# Deck Class:
#   A deck of cards using nummerical values. Functions contain: showCard(), get_random_card(), cardCount(card)
# Helper random Class: (Private)
#   Random Number generator (1-13) for selecting cards

# importing helper modules
import random

# make a deck of cards with associated functions
class Deck:
    def __init__(self):
        self.deck = []
        # add 4 cards per index in the array
        for i in range(14):
            self.deck.append(4)
    
    # showCard(card) return the card IF card exists in the deck as true. Else, if card is not in deck return false.
    # wait ... might not need this function

    # cardCount(card) return how many cards exists (0-4) in the deck.
    # get_random_card() return random card using random class

    # printDeck() print the deck array to console
    def printDeck(self):
        i = 1
        while i < len(self.deck):
            print ("Card value " + str(i) + " has " + str(self.deck[i])+ " cards\n")
            i+=1


game = Deck()
game.printDeck()
