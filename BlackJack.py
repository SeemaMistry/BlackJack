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

    # addPlayer(str playerName) - add a new player to allPlayer
    # def addPlayer(self, name):
    #     # check if name already exists in list of players. If it does, then have to add name change to player by appending some num at end
    #     instances = 0
    #     for player in self.allPlayers:
    #         if player.name == name:
    #             instances += 1
    #     if instances != 0:
    #         # this doesnt work, just ask the player to change their name
    #         name += str(instances)

    #     newplayer = Player(name)
    #     self.allPlayers.append(newplayer)
    #     print("Welcome to the game player {}".format(newplayer.name))
    
    # validName(name) -> Bool - checks user inputed name against list of all player's name. If name already exists return false, else true
    def validName(self, name):
        # checks user inputted name against all
        validity = True
        if len(self.allPlayers) > 0:
            for player in self.allPlayers:
                if name == player.name:
                    validity = False
        return validity


    def addPlayer(self):
        # get player input for name
        name = input("Enter your name: ")
        validName = False
        # loop through until user gives unique player name that does not already exist
        while validName == False:
            # use private function validName(name) to check user inputted name against list of existing Player.name
            #checkName = validName(name)

            # try putting validName() here
            # getting type error when i use the function "Bool no callable"
            checkName = True
            if len(self.allPlayers) > 0:
                for player in self.allPlayers:
                    if name == player.name:
                        checkName = False

            if checkName == False:
                # user inputted name already exist, ask user for another name
                print ("The name, '{}' already exists. Select another name".format(name))
                name = input("Enter your name: ")
            else:
                # user inputted name is valid. Create new Player and welcome them to the game
                validName = True
                newplayer = Player(name)
                self.allPlayers.append(newplayer)
                print("Welcome to the game player {}".format(newplayer.name))

                

        # # check if name exists already. If name exists already, tell player to rename themselves
        # for player in self.allPlayers:
        #     if player.name == name:
        #         print ("The name '{}' already exists. Please input another name")
        #         # right now assuming player puts in a new name 
        #         name = input("Enter your name: ")

    # deletePlayer(playerName) - remove specified player
    #def deletePlayer(self, name):

    
    # hit(player) - get the top card (via deck.topCard) and add it to player hand (player.addHand). Then check if player's count goes above 21

    # checkTotal(player) - Has 2 checks: ace and bust
    #               check if player went bust (via player.total > 21)
    #               check if player has ace (and bust), then change Player.total by (-= 11) and (+= 1)
    #               if only bust and no ace, then change Player.player_status to false

    # pass(player) - player wants no more cards. Change Player.player_status to false
    def ppass(self, player_index):
        (self.allPlayers[player_index]).player_status = False


    # call() - check all Player.total to determine winner against the dealer

    # win(player) - message for winning player. Add point to Player.points

    # bust(player) - check if player gone bust. if they do then send message

    # clearHands() - reset all assests to start a new game. Call Player.deleteHand (including dealer's), deck.build().shuffle(). Increment gameCount
    def clearHands(self):
        # clear dealer's hand
        self.dealer.deleteHand()
        # clear all player's hand
        for people in self.allPlayers:
            people.deleteHand()

    # resetDeck() - new deck and shuffle it
    def resetDeck(self):
        self.deck = Deck()
        self.deck.shuffle()

    # newGame() - deal out cards to player and dealer. Loop till someone wins

    # delete() - reset all assets to zero, gameCount to 0 and delete all players/dealers
    def delete(self):
        # reset the dealer
        self.dealer = Dealer()
        # reset the player
        self.allPlayers = []
        self.allPlayerStatus = True
        # reset game count
        self.gameCount = 0






# Test July 15th 2021
# Test initialized BlackJack attributes
# game = BlackJack()
# # make a deck and start pulling cards
# game.deck.topCard().show()
# game.deck.topCard().show()
# game.deck.topCard().show()
# game.deck.topCard().show()
# print(game.deck.count)
# # test that a new deck is being made
# game.resetDeck()
# print(game.deck.count)

# game.addPlayer("A")
# game.addPlayer("B")
# game.addPlayer("C")
# game.addPlayer("A")
# game.addPlayer("A")

# Test July 21st 2021
# Test addPlayer(). Make sure only unique names get added
game = BlackJack()
game.addPlayer()
game.addPlayer()
game.addPlayer()
game.addPlayer()
game.addPlayer()
game.addPlayer()






    