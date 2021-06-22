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
    # no do need this helper function for when using random num generator

    # cardCount(card) return how many cards exists (0-4) in the deck.
    def cardCount(self, card):
        # go to index in array and see array.value
        cardCount = self.deck[card]
        # return array value
        return cardCount

    # get_random_card() return random card using random class
    def get_random_card(self):
        # store a random number from 1-13 into cardValue
        cardValue = random.randint(1,13)
        # find cardValue in array and check if cardCount > 0. If greater decrement value by one, else run again
        cardExist = False
        while cardExist == False:
            if self.cardCount(cardValue) > 0:
                cardExist = True
                self.deck[cardValue] -= 1
                return cardValue
            else:
                cardValue = random.randint(1,13)

    # printDeck() print the deck array to console
    def printDeck(self):
        i = 1
        while i < len(self.deck):
            print ("Card value " + str(i) + " has " + str(self.deck[i])+ " cards\n")
            i+=1


game = Deck()
game.printDeck()
print("Checking how many 10 cards exist in the deck:")
print(game.cardCount(10))

print("\nUse random number generator to pick a card and then show it. Also check deck for decrement:")
print(game.get_random_card())
game.printDeck()

