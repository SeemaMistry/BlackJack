# Deck Class: A deck of cards using nummerical values. 
# Import random Class as private helper class for random number generator

# importing helper modules
import random

# make a deck of cards with associated functions
class Deck:
    def __init__(self):
        self.deck = []
        # add 4 cards per index in the array
        for i in range(14):
            self.deck.append(4)

    # cardCount(card) return how many cards exists (0-4) in the deck.
    def cardCount(self, cardNum):
        # return how many cards of cardNum exist in the deck
        return self.deck[cardNum]

    # get_random_card() return random card using random class
    def get_random_card(self):
        cardExist = False
        # loop through and find a card from the deck
        while cardExist == False:
            # find cardValue in array and check if cardCount > 0. If <0 decrement value by one, else run again
            # store a random number from 1-13 into cardValue
            cardValue = random.randint(1,13)
            if self.cardCount(cardValue) > 0:
                cardExist = True
                self.deck[cardValue] -= 1
                return cardValue
            else:
                continue

    # printDeck() print the deck array to console
    def printDeck(self):
        i = 1
        # loop through and print all the cards in the deck
        while i < len(self.deck):
            print ("Card value " + str(i) + " has " + str(self.deck[i])+ " cards\n")
            i+=1


game = Deck()
#game.printDeck()
print("Checking how many 10 cards exist in the deck:")
print(game.cardCount(10))

print("\nUse random number generator to pick a card and then show it. Also check deck for decrement:")
while game.cardCount(5) != 0:
    print(game.get_random_card())

game.printDeck()

