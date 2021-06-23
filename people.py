# People class to create players and dealers for card games
# Import Deck class

class People:
    # initialize the person's attributes: hand, points (initialize to 0), player_status (true for playing, false when not hitting anymore)

    # pointsCounter() shows total points accumulated by player
    # addPoint() add a point for the player when they win
    
    # playerHand() store cards player is holding in an array. 
    # - you get cards from the Deck class
    # - store cards in an array
    # printHand() Print playerHand() on console every turn (players cards are all shown up)

    # playerCall(str) string check for hit, pass
    # - if hit -> get another card from the deck (use Deck.get_random_card) and store it into players hand
    # - if pass -> update player_status to false



class Dealer(People):
    # same as the people class but need to modify the cardDealt() to only show cards in index 1+ of array, not index 0
