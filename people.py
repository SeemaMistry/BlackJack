# People class to create players and dealers for card games
# Import Deck class

class People:
    # initialize the person's attributes: hand, points (initialize to 0), player_status (true for playing, false when not hitting anymore), player_name
    def __init__(self, name):
        self_points = 0
        self_player_status = True
        self_points = 0
        self_name = name
        self_hand = []

    # pointsCounter() shows total points accumulated by player
    
    # addPoint() add a point for the player when they win
    
    # playerHand() store cards player is holding in an array. 
    # - you get cards from the Deck class
    # - store cards in an array
    
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
