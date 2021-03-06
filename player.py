# card import not needed
from deck import Deck, Card

class Player:
    # initialize the person's attributes: hand, points (initialize to 0), player_status (true for playing, false when not hitting anymore), player_name
    def __init__(self, name):
        self.player_status = True # if player wants to continue playing = true, or stop playing = false
        self.points = 0 # win = 1 point, loss is no points
        self.name = name # name the player
        self.hand = [] # all the cards player has is stored in array
        # NEED TO ADD SELF.SPAREHAND = [] FOR CASES WHEN PLAYER SPLITS HAND WITH 2 ACES
        # self.2ndhand = []
        # self.2ndtotal = 0
        self.total = 0 # counts the cards value held in self.hand
        self.ace = False # just to check if the player holds an Ace card (due to double numVal ace hold of 11 and 1)

    def deleteHand(self):
        # clear all the cards from the deck
        self.hand.clear()
        self.total = 0
       # print("{}, has no cards".format(self.name))

    # add card to player's hand and add num count 
    def addHand(self, card):
        # add a Card Object to your hand
        self.hand.append(card)
        # check if card is an ace
        if card.value == "Ace":
            self.ace = True
        # increment the card's value to self.total
        # caviott: if the hand has an ACE then need to check later in BJ class if the 2nd value of one is needed.
        self.total += card.numVal

    # show hand needs to call on Card.show()
    def showHand(self):
        handLen = len(self.hand)
        i = 0
        # make empty string and append player's hand
        hand = ''
        hand += "{}'s hand: ".format(self.name)
        # loop through player's hand and add string of card object (Card.strShow() -> str). Add "," to separate cards
        for card in self.hand:
            hand += card.strShow()
            if i < (handLen-1):
                hand += ", "
            i += 1
        return (hand)


class Dealer(Player):
    def __init__(self, name="Dealer"):
        super().__init__(name)

    # Dealer's hand should show all cards EXCEPT the first card dealer holds
    def dealersHand(self):
        # find start and stop from string returned by showHand()
        hand = self.showHand()
        # start at first ":" (but in for loop got +2 to include spacing)
        i = hand.find(":")
        if len(self.hand) > 1:
            # stop at first comma ","
            k = hand.find(",")
            remove = ''
            # add all letters from start to stop-1 into a string
            for letter in range (i+2, k):
                remove += hand[letter]
            # replace the string in remove with and empty X
            return hand.replace(remove, "X")
        elif len(self.hand) == 1:
            remove = ''
            for letter in range (i+2, len(hand)):
                remove += hand[letter]
            return hand.replace(remove, "X")
        else:
            return hand
        



    

# # Test 1 - June 29/2021
# # Test you can make a player with a name, get/set points, print/add cards to their hand
# p1 = Player("Seema")
# print(p1.name)
# print(p1.points)
# print(p1.hand)
# p1.addHand(5)
# print(p1.hand)
# p1.addHand(6)
# print(p1.hand)
# p1.addHand(7)
# p1.name = "Jamie"
# print(p1.hand)
# p1.deleteHand()

# # Test 2 - June 29/2021
# # Test creating a Card object and adding it to the p1's hand
# print("\n")
# card0 = Card("Spades", 10)
# card0.show()
# card1 = Card("Hearts", 10)
# card1.show()
# card2 = Card("Diamonds", 10)
# card2.show()
# card3 = Card("Clubs", 10)
# card3.show()
# p1.addHand(card0)
# p1.addHand(card1)
# p1.addHand(card2)
# p1.addHand(card3)
# print("\n\n")
# p1.showHand()
# p1.deleteHand()

# Test 3 - June 29/2021
# Create a deck and pull random cards from the deck and add it to the player's hand
# deck = Deck()
# c1 = deck.cards[0]
# c2 = deck.cards[10]
# c3 = deck.cards[36]
# c4 = deck.cards[51]
# c1.show()
# c2.show()
# c3.show()
# c4.show()
# # make a new player
# p2 = Player("Aron")
# p2.addHand(c1)
# p2.addHand(c2)
# p2.addHand(c3)
# p2.addHand(c4)
# p2.showHand()

# Test 4 - July 13th
# test out dealer class
# deck = Deck()
# c1 = deck.cards[0]
# c2 = deck.cards[10]
# c3 = deck.cards[36]
# c4 = deck.cards[51]
# p2 = Dealer()
# p2.addHand(c1)
# p2.addHand(c2)
# p2.addHand(c3)
# p2.addHand(c4)
# print ("going to showHand() of the dealer")
# print(p2.showHand())
# print ("\ngoing to show dealersHand() of the dealer")
# print(p2.dealersHand())
# print(p2.total)