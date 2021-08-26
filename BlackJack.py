from card import Ace
from player import Player, Dealer, Deck, Card
# Game rules:
# All players and dealer given 2 cards.
# Give cards all around to player until they go bust or stay
# Dealer given cards at the end. Must have hand total >=17
#
# Winners and Losers:
#   - 2 cards add to 21 (winner) -> +3 points
#   - 2+ cards add up to 21 (winner) -> +3 points
#   - 2+ cards <21 but >Dealer's total (win) -> +1 point
#   - 2+cards <21 (bust) -> +0
# 

class BlackJack:
    def __init__(self):
        # shuffle the deck
        self.deck = Deck()
        self.deck.shuffle()
        # dealer
        self.dealer = Dealer()
        # allPlayers
        self.allPlayers = []
        # number of games played
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

    # addPlayer() -> use user input to create new player of inputed name. Helper function validName() ensures no duplicate names.
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
                print("Welcome to the game player {}!\n".format(newplayer.name))

    # deletePlayer(player_index) -> remove specified player delete_name
    def deletePlayer(self, delete_name):
        i = 0
        # find index i of player with delete_name and pop it out of array of players
        for player in self.allPlayers:
            if player.name == delete_name:
                self.allPlayers.pop(i).name                
                print("\nPlayer '{}' has been removed from the game\n".format(player.name))
            i += 1

# --------------------------------------------------------
# -------------- PLAYER AND DEALER MOVES ---------------
# --------------------------------------------------------
    # stay(player_index) -> player wants no more cards. Change Player.player_status to false
    def stay(self, player_index):
        # change player status to false and checktotal() 
        (self.allPlayers[player_index]).player_status = False
        self.checkTotal(player_index)


    
    # hit(player_index) -> get the top card (via deck.topCard) and add it to player hand (player.addHand). Then check if player's count goes above 21
    def hit(self, player_index):
        # if player_status == true: +card to player hand. If hand <= 2, checktotal
        if self.allPlayers[player_index].player_status == True:
            # give the player a card
            self.allPlayers[player_index].addHand(self.deck.topCard())
            if len(self.allPlayers[player_index].hand) > 1:
                self.checkTotal(player_index)
        # else (player_status = false): print error error message
        else:
            print ("Error: Player '{}' can NOT recieve anymore cards".format(self.allPlayers[player_index].name))

    # hitDealer() -> gives dealer cards. When all players given cards, then dealer will continously take cards until dealer hand has a total min of 17
    def hitDealer(self):
        # if dealer has <2 cards (0 or 1 card), just give the dealer another card
        if len(self.dealer.hand) < 2:
            self.dealer.addHand(self.deck.topCard())
        else:
            # if dealer has 2 cards, keep giving dealer cards until total >= 17
            while self.dealer.total < 17:
                self.dealer.addHand(self.deck.topCard())
                # if dealer holds ace and total currently >21 use helper function dealerTotal() to account for double value of ace
                if self.dealer.ace == True:
                    self.dealerTotal()
    
    # dealerTotal() -> when dealer is holding ace and value is above 21, change ace value from 11 to 1
    def dealerTotal(self):
        self.dealer.ace = False
        if self.dealer.total > 21:
            self.dealer.total -= 10
            
         
# --------------------------------------------------------
# -------------- HAND COUNT FOR WIN/BUST ---------------
# --------------------------------------------------------

    # checkTotal(player) - Check the total of player hands: ==21 is winner, >21 is bust, <21 do nothing, >21 & ace is change ace value from 11 to 1 and recheck
    def checkTotal(self, player_index):
        ace = self.allPlayers[player_index].ace
        if self.allPlayers[player_index].total > 21:
            # check if player holds an ace (double value of 11 and 1) and over 21, then -10 from total
            if ace == True:
                # reset ace to false or it will continuously remove 10
                self.allPlayers[player_index].ace = False 
                self.allPlayers[player_index].total += (-10)
                # check total again if over 21 with new total
                if self.allPlayers[player_index].total > 21:
                    self.bust(player_index)
                elif self.allPlayers[player_index].total == 21:
                    self.winner(player_index)
            else:
                # if over 21 but no ace, then bust
                self.bust(player_index)
        # 21 is a winner
        elif self.allPlayers[player_index].total == 21:
             self.winner(player_index)

    # win_bust_prep(player_index) -> win/bust preparation (showhand, get total, status to false, delete hand) and return total player_index hand holds. 
    def win_bust_prep(self, player_index):
        # print hand to console
        print(self.allPlayers[player_index].showHand())
        # store total
        total = self.allPlayers[player_index].total
        # change status to false and delete hand
        self.allPlayers[player_index].player_status = False
        self.allPlayers[player_index].deleteHand()
        # return total
        return total

    # win(player_index) -> When player gets 21: give message for winning player and add +3 or +1 points to Player.points and remove their hand
    def winner(self, player_index):
        # perform win preparation and get total
        total = self.win_bust_prep(player_index)
        # check which winning message to give (based on total == 21 or <21). Give point appropriately 
        if total == 21:
            self.allPlayers[player_index].points += 3
            print ("BlackJack!\nPlayer {} has {}, you're a winner!\n".format(self.allPlayers[player_index].name, 21))
        else:
            self.allPlayers[player_index].points += 1
            print ("Player's {}, to Dealer's {}\nPlayer {} has won against the Dealer!\n".format(total, self.dealer.total, self.allPlayers[player_index].name))


    # bust(player_index) -> When player goes bust remove their hand and give bust message. No points given
    def bust(self, player_index):
        # perform win preparation and get total
        total = self.win_bust_prep(player_index)
        print ("Player {} has {}, it's a bust!\n".format(self.allPlayers[player_index].name, total))

   # compare2dealer() -> check all Player.total to determine winners against the dealer's hand
    def compare2dealer(self):
        print("\nAll players have been served by the dealer.\nNow we will compare remaining players hands against the dealer:\n")
        print(self.dealer.showHand())
        i = 0 # player index
        for player in self.allPlayers:
            # if player doesnt have any cards -> continue to next player i++
            if len(player.hand) == 0:
                i += 1
            else:
                print("\nComparing Player {}'s hand to dealer's hand:\n".format(player.name))
                # if dealer is bust (>21) and player is less than 21 (p<21) -> player won against dealer
                if player.total <= 21 and self.dealer.total > 21:
                    self.winner(i)
                # if dealer >=21: a) dealer < player -> player won against dealer. b) dealer > player -> dealer won against player
                elif self.dealer.total <= 21:
                    if self.dealer.total < player.total:
                        self.winner(i)
                    elif self.dealer.total >= player.total:
                        total = self.win_bust_prep(i)
                        print("Dealer's {} won against Player {}'s hand of {}".format(self.dealer.total, player.name, total))
                # increment to next player index
                i += 1
   
# --------------------------------------------------------
# -------------- RESET FOR A NEW ROUND ---------------
# --------------------------------------------------------

    # clearHands() -> reset all players to start a new game. Call Player.deleteHand (including dealer's)
    def clearHands(self):
        # clear dealer's hand, and loop through all player's hand and set player_status to true
        self.dealer.deleteHand()
        for people in self.allPlayers:
            people.deleteHand()
            people.ace = False
            people.player_status = True

    # resetDeck() - new deck and shuffle it
    def resetDeck(self):
        self.deck = Deck()
        self.deck.shuffle()
 
    # newGame() - deal out cards to player and dealer in accordance with game of BlackJack rules
    def newGame(self):
        # INCREMENT GAME COUNT
        self.gameCount += 1
        print("\nWelcome to the BlackJack table!\t\t\tGame #: {}\n\n".format(self.gameCount))
        # loop through and add player's until user says no more players 
        morePlayer = input("Would you like to add another player? [y/n]: ")
        while morePlayer == "y":
            self.addPlayer()
            morePlayer = input("Would you like to add another player? [y/n]: ")
        print("\n")
        # in a loop, give each player 2 cards, including dealer
        cards = 0
        i = 0 # player_index
        while cards < 2:
            self.hitDealer()
            for player in self.allPlayers:
                self.hit(i)
                i += 1
            cards += 1
            i = 0

        # print everyone's cards
        for player in self.allPlayers:
            print(player.showHand())
            print("\n")
        print(self.dealer.dealersHand())
        print("\n")

        # call on each player and ask for hit/stay
        i = 0
        for player in self.allPlayers:
            request = input("Player {}, would you like to hit or stay? ".format(player.name))
            print("\n")
            while request == "hit":
                self.hit(i)
                print("\n")
                # has anyone got 21? -> give winning statment + points, remove their cards
                # has anyone gone bust? -> give bust statement, remove their cards
                if player.player_status == True:
                    print(player.showHand())
                    request = input("\nPlayer {}, would you like to hit or stay? ".format(player.name))
                else:
                    break
            # no more hits means player is staying now
            self.stay(i)
            i += 1
         
        # once all players are stay (but not at 21) let dealer hit (has to hit if below 17)
        self.hitDealer()
 
        # compare remaining players (>21) to dealer. 
        self.compare2dealer()
        
        # show player points as a list
        print("\nList of player and their points:")
        for player in self.allPlayers:
            print("{} - {}".format(player.name, player.points))
        print("\n")
        self.clearHands()
        self.resetDeck()

# --------------------------------------------------------
# -------------- RESET FOR A NEW GAME ---------------
# --------------------------------------------------------

    # delete() - reset all assets to zero, gameCount to 0 and delete all players/dealers
    def delete(self):
        # reset the dealer
        self.dealer = Dealer()
        # reset the player
        self.allPlayers = []
        # reset game count
        self.gameCount = 0



# Test Aug 21st 2021
# Testing newGame()
g = BlackJack()
g.newGame()
request = input('What would you like to do now? Type "help" if you need help. Type "exit" if you want to exit: ')
while request != "exit":
    if request == "help":
        print("Here is a list of commands you can type:\nnew game\tStart another game with existing players\ndelete player\tDelete a player\ndelete\tDelete game and clear all assests to default")
    elif request == "new game":
        g.newGame()
    elif request == "delete player":
        name = input("Provide the player's name you wish to delete: ")
        g.deletePlayer(name)
    elif request == "delete":
        g.delete()
    request = input('What would you like to do now? Type "help" if you need help. Type "exit" if you want to exit: ')
    