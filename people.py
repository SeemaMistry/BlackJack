# People class to create players and dealers for card games
# Import Deck class

class People:
    # initialize the person's attributes: hand, points (initialize to 0), player_status (true for playing, false when not hitting anymore), player_name
    def __init__(self, name):
        self.points = 0
        self.player_status = True
        self.points = 0
        self.name = name
        self.hand = []

    # getPoints() shows total points accumulated by player
    def getPoints(self):
        return self.points
    
    # addPoint() add a point for the player when they win
    def addPoint(self):
        # add a point only when player won. One win = One point
        self.point +=1
    
    def getHand(self):
        return self.hand
    
    def setHand(self, card):
        # take the card and add it to the player's hand
        self.hand.append(card)

    
    # printHand() Print playerHand() on console every turn (players cards are all shown up)

    # playerCall(str) string check for hit, pass
    # while loop until player_status is false
    # - if hit -> get another card from the deck (use Deck.get_random_card) and store it into players hand
    #                   - update, it will be getting a card from Game.card (to be made)
    # - if pass -> update player_status to false



class Dealer(People):
    # same as the people class but need to modify the cardDealt() to only show cards in index 1+ of array, not index 0

    # printHand() only show 2nd card, first card should be hidden
    # printFullHand() show all the cards only at the end of the game
