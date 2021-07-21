from player import Player, Dealer, Deck, Card
# Game rules:
# All players and dealer given 2 cards.
# Give cards all around to player until they go bust or stay
# Dealer given cards at the end. Must have hand total >=17
#
# Winners and Losers:
#   - 2 cards add to 21 (winner) -> +3 points
#   - 2+ cards add up to 21 (winner) -> +3 points
#   - 2+ cards >21 but <Dealer's total (win) -> +1 point
#   - 2+cards <21 (bust) -> +0
# 

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
# --------------------------------------------------------
# -------------- CREATE AND DELETE PLAYERS ---------------
# --------------------------------------------------------
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

# --------------------------------------------------------
# -------------- PLAYER AND DEALER MOVES ---------------
# --------------------------------------------------------
    # stay(player) - player wants no more cards. Change Player.player_status to false
    def stay(self, player_index):
        # change player status to false
        (self.allPlayers[player_index]).player_status = False
        # check if they got 21 using checkTotal(). If they didnt, itll do nothing
        self.checkTotal(player_index)


    
    # hit(player_index) - get the top card (via deck.topCard) and add it to player hand (player.addHand). Then check if player's count goes above 21
    def hit(self, player_index):
        # if giving first card, just add to player hand
        if len(self.allPlayers[player_index].hand) < 1 and self.allPlayers[player_index].player_status == True:
            self.allPlayers[player_index].addHand(self.deck.topCard())
        
        # for more than 1 card in the deck, add and checktotal
        else:
            # only hit if player status is true
            if self.allPlayers[player_index].player_status == True:
                # get the top card from the deck and add it to specified player
                self.allPlayers[player_index].addHand(self.deck.topCard())
                # check total to see if player has gone bust or not. If bust, change player_status to false
                self.checkTotal(player_index)
            else:
                # player_status is false: do not give card, give error statement
                print("Error: Player '{}' can NOT recieve anymore cards".format(self.allPlayers[player_index].name))

# NEED TO ADD STATEMENT OF >=17. MAKE THIS A LOOP FOR MORE THAN 2 CARDS
    def hitDealer(self):
        # if dealer has <2 cards (0,1,2), just give the dealer the single card
        if len(self.dealer.hand) < 2:
            self.dealer.addHand(self.deck.topCard())
        else:
            # if dealer has 2 cards, keep giving dealer cards until total >= 17
            while self.dealer.total < 17:
                self.dealer.addHand(self.deck.topCard())

# --------------------------------------------------------
# -------------- HAND COUNT FOR WIN/BUST ---------------
# --------------------------------------------------------

    # checkTotal(player) - Has 2 checks: ace and bust
    #               check if player went bust (via player.total > 21)
    #               check if player has ace (and bust), then change Player.total by (-= 11) and (+= 1)
    #               if only bust and no ace, then change Player.player_status to false
    def checkTotal(self, player_index):
        ace = self.allPlayers[player_index].ace
        # if player has over 21
        #print("Player '{}' has a total of {}".format(self.allPlayers[player_index].name, self.allPlayers[player_index].total))
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
        
        # 21 is a winner
        elif self.allPlayers[player_index].total == 21:
            self.winner(player_index)
# ALSO NEED TO CHANGE PLAYER STATUS HERE TO FALSE CUZ THEY WON AND NOW ARE NOT PLAYING. OR DO THAT IN WIN
# GIVE 3 POINTS FOR GETTING 21
            
    # win(player) - When player gets 21: give message for winning player, remove their cards, and add 3 points to Player.points
# CHANGE TO winnerMsg i.e. JUST GIVE MESSAGE TO PLAYER
# OR CHANGE TO WINNER21() THIS WAY YOU CAN KEEP THE POINTS +=3 AND GIVE SPECIAL MESSAGE OF WINNING 21
    def winner(self, player_index):
        # take their cards away and return winner message
        self.allPlayers[player_index].deleteHand()
# REMOVE POINTS GIVEN OR LEAVE IT IF CHANGING TO WINNER21()
# NEED TO CHANGE PLAYER STATUS HERE AFTER YOU REMOVE THEIR CARDS
        # give player a point
        self.allPlayers[player_index].points += 3
        return ("Player '{}' has {}, you're a winner!".format(self.allPlayers[player_index].name, 21))

    # bust(player) - When player goes bust: remove their hand and give bust message. No points given
    def bust(self, player_index, num):
# I just want to see the player's hand
        print(self.allPlayers[player_index].showHand())
        # change player status!!!! Otherwise youll delete their hand and keep giving them cards!!
        self.allPlayers[player_index].player_status = False
        # remove player's hand then return statment
        self.allPlayers[player_index].deleteHand()
        return ("Player '{}' has {}, it's a bust!".format(self.allPlayers[player_index].name, num))

   # call() - check all Player.total to determine winner against the dealer
    def compare2dealer():
        # get dealer's total
        # check each player's status. 
        pass

# --------------------------------------------------------
# -------------- RESET FOR A NEW ROUND ---------------
# --------------------------------------------------------

    # clearHands() - reset all players to start a new game. Call Player.deleteHand (including dealer's)
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
    def newGame():
        # INCREMENT GAME COUNT
        # loop through and add player's until user says no more players 
        # in a loop, give each player 2 cards, including dealer
        # call on each player and ask for hit/stay
            # has anyone got 21? -> give winning statment + points, remove their cards
            # has anyone gone bust? -> give bust statement, remove their cards
        # once all players are stay (but not at 21) let dealer hit (has to hit if below 17)
        # compare remaining players (>21) to dealer. 
            # Anyone above dealer's value but >22 wins -> take away their cards and give them 0.5 points
            # anyone <dealer losses -> take away their cards
        pass

# --------------------------------------------------------
# -------------- RESET FOR A NEW GAME ---------------
# --------------------------------------------------------

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
# game = BlackJack()
# game.addPlayer()
# game.addPlayer()
# game.addPlayer()
# game.addPlayer()
# # game.addPlayer()
# # game.addPlayer()
# game.deletePlayer(2)
# game.hit(0)
# game.hit(0)
# game.hit(0)
# game.hit(0)

# game.hit(1)
# game.hit(1)
# game.hit(1)
# game.hit(2)
# game.hit(2)

# game.hitDealer()
# game.hitDealer()
# game.hitDealer()
# print(game.allPlayers[0].showHand())
# print(game.allPlayers[1].showHand())
# print(game.allPlayers[2].showHand())

# print("\n")
# print(game.dealer.dealersHand())
# print(game.dealer.showHand())
# print("The dealer's total is: {}\n".format(game.dealer.total))

# print("\n")
# game.checkTotal(0)
# game.checkTotal(1)
# game.checkTotal(2)


# Test July 21/2021
# Testing checkTotal/win/bust for players
# make a new game and add 1 player
game = BlackJack()
game.addPlayer()
print("\n")
# give player 2 cards then print their hand
game.hit(0)
game.hit(0)
print(game.allPlayers[0].showHand())
print(game.allPlayers[0].total)
print("\n")
# give player another card and print hand
game.hit(0)
print(game.allPlayers[0].showHand())
print(game.allPlayers[0].total)
print("\n")
# give player another card and print hand
game.hit(0)
print(game.allPlayers[0].showHand())
print(game.allPlayers[0].total)
print("\n")







    