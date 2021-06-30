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

    # show hand needs to call on Card.show()
    def showHand(self):
        print("{}'s hand: ".format(self.name))
        # per card in the player's hand, display each card (use Card.show())
        for card in self.hand:
            card.show()


    

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
print("\n")
card0 = Card("Spades", 10)
card0.show()
card1 = Card("Hearts", 10)
card1.show()
card2 = Card("Diamonds", 10)
card2.show()
card3 = Card("Clubs", 10)
card3.show()
p1.addHand(card0)
p1.addHand(card1)
p1.addHand(card2)
p1.addHand(card3)
print("\n\n")
p1.showHand()