from deck import Deck, Card

class Player:
    # initialize the person's attributes: hand, points (initialize to 0), player_status (true for playing, false when not hitting anymore), player_name
    def __init__(self, name):
        self.player_status = True # if player wants to continue playing or show cards
        self.points = 0 # win = 1 point, loss is no points
        self.name = name # name the player
        self.hand = [] # all the cards player has is stored in array

    def deleteHand(self):
        # clear all the cards from the deck
        self.hand.clear()
        print("{}, has no cards".format(self.name))

    def addHand(self, card):
        # add a card to your hand
        self.hand.append(card)

    

# Test 1 - June 29/2021
# Test you can make a player with a name, get/set points, print/add cards to their hand
p1 = Player("Seema")
print(p1.name)
print(p1.points)
print(p1.hand)
p1.addHand(5)
print(p1.hand)
p1.addHand(6)
print(p1.hand)
p1.addHand(7)
p1.name = "Jamie"
print(p1.hand)
p1.deleteHand()

# Test 2 - June 29/2021
# Test creating a Card object and adding it to the p1's hand
card0 = Card("Spade", 10)
card0.show()
