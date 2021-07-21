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
        validN = False
        # loop through until user gives unique player name that does not already exist
        while validN == False:
            # use private function validName(name) to check user inputted name against list of existing Player.name
            checkName = self.validName(name)
        
            if checkName == False:
                # user inputted name already exist, ask user for another name
                print ("The name, '{}' already exists. Select another name".format(name))
                name = input("Enter your name: ")
            else:
                # user inputted name is valid. Create new Player and welcome them to the game
                validN = True
                newplayer = Player(name)
                self.allPlayers.append(newplayer)
                print("Welcome to the game player {}".format(newplayer.name))

                
    # deletePlayer(player_index) - remove specified player
    def deletePlayer(self, player_index):
        name = self.allPlayers.pop(player_index).name
        print("\nPlayer '{}' has been removed from the game\n".format(name))

    
    # hit(player_index) - get the top card (via deck.topCard) and add it to player hand (player.addHand). Then check if player's count goes above 21
    def hit(self, player_index):
        # get the top card from the deck and add it to specified player
        self.allPlayers[player_index].addHand(self.deck.topCard())

    def hitDealer(self):
        self.dealer.addHand(self.deck.topCard())

    # checkTotal(player) - Has 2 checks: ace and bust
    #               check if player went bust (via player.total > 21)
    #               check if player has ace (and bust), then change Player.total by (-= 11) and (+= 1)
    #               if only bust and no ace, then change Player.player_status to false
    def checkTotal(self, player_index):
        ace = self.allPlayers[player_index].ace
        # if player has over 21
        print("Player '{}' has a total of {}".format(self.allPlayers[player_index].name, self.allPlayers[player_index].total))
        if self.allPlayers[player_index].total > 21:
            
            # check if player holds an ace (double value of 11 and 1)
            if ace == True:
                # if there is an ace (and total > 21), has double value of 11 and 1. Add -10 to total
                self.allPlayers[player_index].total += (-10)
                # check again if over 21 with new total
                if self.allPlayers[player_index].total > 21:
                    # over 21 so bust
                    self.allPlayers[player_index].player_status = False
                    print(self.bust(player_index, self.allPlayers[player_index].total))
            
            else:
                # if over 21 but no ace, then change player status to false
                self.allPlayers[player_index].player_status = False
                print(self.bust(player_index, self.allPlayers[player_index].total))
              

        

    # pass(player) - player wants no more cards. Change Player.player_status to false
    def ppass(self, player_index):
        (self.allPlayers[player_index]).player_status = False


    # call() - check all Player.total to determine winner against the dealer


    # win(player) - message for winning player. Add point to Player.points

    # bust(player) - check if player gone bust. if they do then send message
    def bust(self, player_index, num):
        return ("Player '{}' has {}, it's a bust!".format(self.allPlayers[player_index].name, num))

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
# game.addPlayer()
# game.addPlayer()
game.deletePlayer(2)
game.hit(0)
game.hit(0)
game.hit(0)
game.hit(1)
game.hit(1)
#game.hit(2)
#game.hitDealer()
# game.hitDealer()
# game.hitDealer()
print(game.allPlayers[0].showHand())
print(game.allPlayers[1].showHand())
print(game.allPlayers[2].showHand())
print(game.dealer.dealersHand())
game.checkTotal(0)








    