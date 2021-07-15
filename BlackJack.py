from player import Player, Dealer, Deck, Card

class BlackJack:
    def __init__(self):
        # initialize game:
        # deck
        # shuffle the deck
        # dealer
        # allPlayers
        # gameCount = 1

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

    # newGame() - reset all assests to start a new game. Call Player.deleteHand (including dealer's), deck.build().shuffle(). Increment gameCount

    # reset() - reset all assets to zero, gameCount to 0 and delete all players/dealers

    