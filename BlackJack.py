from player import Player, Dealer, Deck, Card

class BlackJack:
    def __init__(self):
        # initialize game:
        # deck
        # shuffle the deck
        self.deck = Deck()
        self.deck.shuffle()
        # dealer
        self.dealer = Dealer()
        # allPlayers
        self.allPlayers = []
        # allPlayerStatus = true (as long as one player has player_status as true, not including dealer)
        self.allPlayerStatus = True
        # gameCount = 0
        self.gameCount = 0

    # addPlayer(playerName) - add a new player to allPlayer

    # deletePlayer(playerName) - remove specified player
    
    # hit(player) - get the top card (via deck.topCard) and add it to player hand (player.addHand). Then check if player's count goes above 21

    # checkTotal(player) - Has 2 checks: ace and bust
    #               check if player went bust (via player.total > 21)
    #               check if player has ace (and bust), then change Player.total by (-= 11) and (+= 1)
    #               if only bust and no ace, then change Player.player_status to false

    # pass(player) - player wants no more cards. Change Player.player_status to false

    # call() - check all Player.total to determine winner against the dealer

    # win(player) - message for winning player. Add point to Player.points

    # bust(player) - message for player gone bust

    # clearHands() - reset all assests to start a new game. Call Player.deleteHand (including dealer's), deck.build().shuffle(). Increment gameCount

    # resetDeck() - new deck and shuffle it
    def resetDeck(self):
        self.deck = Deck()
        self.deck.shuffle()

    # newGame() - deal out cards to player and dealer. Loop till someone wins

    # delete() - reset all assets to zero, gameCount to 0 and delete all players/dealers


# Test July 15th 2021
# Test initialized BlackJack attributes
game = BlackJack()
# make a deck and start pulling cards
game.deck.topCard().show()
game.deck.topCard().show()
game.deck.topCard().show()
game.deck.topCard().show()
print(game.deck.count)
# test that a new deck is being made
game.resetDeck()
print(game.deck.count)

    