# People class to create players and dealers for card games
# Import Deck class
from deck import Deck

class Player:
    # initialize the person's attributes: hand, points (initialize to 0), player_status (true for playing, false when not hitting anymore), player_name
    def __init__(self, name):
        self.player_status = True # if player wants to continue playing or show cards
        self.points = 0 # win = 1 point, loss is no points
        self.name = self.setName(name) # name the player
        self.hand = [] # all the cards player has is stored in array

    # getPoints() shows total points accumulated by player
    def getPoints(self):
        return self.points
    
    # addPoint() add a point for the player when they win
    def addPoint(self):
        # add a point only when player won. One win = One point
        self.point +=1

    # get and set player's name
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    def printHand(self):
        # # print the values separated by comma
        # for i in self.hand:
        #     print(str(i) + ", ")

        # apparently you can print arrays by just printing the array name
        print(self.hand)

    # add a card to your hand
    def addHand(self, card):
        self.hand.append(card)
        
    
    def getHand(self):
        return self.hand
    
    # def setHand(self, card):
    #     # take the card and add it to the player's hand
    #     self.hand.append(card)
    def setHand(self):
        card = Deck().get_random_card()
        self.hand.append(card.getRandomCard())
        
    
    # printHand() Print playerHand() on console every turn (players cards are all shown up)
    def printHand(self):
        # layout:
        # Name: card1, card2, card3, ....
        print(str(self.name) + ": ")
        for i in self.hand:
            print(i)

    # playerCall(str) string check for hit, pass
    # while loop until player_status is false
    # - if hit -> get another card from the deck (use Deck.get_random_card) and store it into players hand
    #                   - update, it will be getting a card from Game.card (to be made)
    # - if pass -> update player_status to false



#class Dealer(People):
    # same as the people class but need to modify the cardDealt() to only show cards in index 1+ of array, not index 0

    # printHand() only show 2nd card, first card should be hidden
    # printFullHand() show all the cards only at the end of the game

# p1 = People("Player1")
# p1.printHand()
# card = Deck()
# card.get_random_card()
# #card.printCard()
# p1.setHand()
# p1.printHand()
