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

#~~~~ Might want to change it to player_name instead of index for easier use. Names are unique in game already so loop through, find name and index and delete player
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

#~~~~ Does it need to return self.checktotal()? or can you just call self.checktotal?
        return self.checkTotal(player_index)


    
    # hit(player_index) - get the top card (via deck.topCard) and add it to player hand (player.addHand). Then check if player's count goes above 21
    def hit(self, player_index):
# Ignore late comment about changing else to elif. this whole things needs to change!! The following is how it should go:
# if player_status == true: +card to player hand. If hand <= 2, checktotal
# else (player_status = false): return or print error error message

        if self.allPlayers[player_index].player_status == True:
            # give the player a card
            self.allPlayers[player_index].addHand(self.deck.topCard())
            if len(self.allPlayers[player_index].hand) > 1:
                return self.checkTotal(player_index)
        
        else:
            return ("Error: Player '{}' can NOT recieve anymore cards".format(self.allPlayers[player_index].name))


# NEED TO ADD STATEMENT OF >=17. MAKE THIS A LOOP FOR MORE THAN 2 CARDS
    def hitDealer(self):
        # if dealer has <2 cards (0 or 1 card), just give the dealer another card
        if len(self.dealer.hand) < 2:
            self.dealer.addHand(self.deck.topCard())
        else:
            # if dealer has 2 cards, keep giving dealer cards until total >= 17
            while self.dealer.total < 17:
                self.dealer.addHand(self.deck.topCard())
                # if dealer holds ace and total currently >21
                if self.dealer.ace == True:
                    self.dealerTotal()
#~~~~ this is the end of the dealer getting cards (when they reach >17, so you probably want to show dealer's hand here, or call a function that does that
    
    def dealerTotal(self):
        self.dealer.ace = False
        if self.dealer.total > 21:
            self.dealer.total -= 10
            
         

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
        if self.allPlayers[player_index].total > 21:
            # check if player holds an ace (double value of 11 and 1)
            if ace == True:
                # if there is an ace (and total > 21), has double value of 11 and 1. Add -10 to total
                self.allPlayers[player_index].total += (-10)
                # check again if over 21 with new total
                if self.allPlayers[player_index].total > 21:
                    # over 21 so bust
                    #self.allPlayers[player_index].player_status = False
                    return (self.bust(player_index))

                elif self.allPlayers[player_index].total == 21:
                    # got to 21
                    return (self.winner(player_index))
            else:
                # if over 21 but no ace, then change player status to false
                #self.allPlayers[player_index].player_status = False
                return (self.bust(player_index))
        
        # 21 is a winner
        elif self.allPlayers[player_index].total == 21:
            return (self.winner(player_index))

        # # less than 21, do nothing
        # else:
        #     pass

#~~~~ group together the first bit of winner() amd bust() cuz they are the same. call the helper function win_bust_prep()
    def win_bust_prep(self, player_index):
        # print hand
        print(self.allPlayers[player_index].showHand())
        # store total
        total =  self.allPlayers[player_index].total
        # change status to false and delete hand
        self.allPlayers[player_index].player_status = False
        self.allPlayers[player_index].deleteHand()
        # return total
        return total

    # win(player) - When player gets 21: give message for winning player, remove their cards, and add 3 points to Player.points
    def winner(self, player_index):
        total = self.win_bust_prep(player_index)
        # check which winning message to give (based on total == 21 or <21). Give point appropriately 
        if total == 21:
            # give 3 points
            self.allPlayers[player_index].points += 3
            return ("Player '{}' has {}, you're a winner!\n".format(self.allPlayers[player_index].name, 21))

#~~~~~ should it be dealer<=21? If dealer gets 21 doesnt that mean player's without 21 loose?
#~~~ SHouls you check dealer<21 (first and then check rest) and total > dealer
        elif total > self.dealer.total and self.dealer.total <= 21:
            # give 1 point
            self.allPlayers[player_index].points += 1
            return ("Player's {}, to Dealer's {}\nPlayer '{}' has won against the Dealer!\n".format(total, self.dealer.total, self.allPlayers[player_index].name))

#~~~ leave this else statement as a catch for now but honestly if code is working this should never show up
        else:
            return "Error: This player is not a winner\n"

    # bust(player) - When player goes bust: remove their hand and give bust message. No points given
    def bust(self, player_index):
        total = self.win_bust_prep(player_index)
#~~~~ might want to store player total before deleting (so your code is similar to winner)
        return ("Player '{}' has {}, it's a bust!\n".format(self.allPlayers[player_index].name, total))

   # call() - check all Player.total to determine winner against the dealer
    def compare2dealer(self):
#~~~~ In the beginning dont worry about checking if all_player_status. Assume all the players have their status set at false before this function is called
# ~~~ you can deal with checking later or even before this function is called         
        # check that all player status is false
        # check each player's status. 
        i = 0
        for player in self.allPlayers:
            print(player.name)

#~~~ much simpler way of doing all of this
# if  player with hand.length = 0 -> continue and i++
# if dealer is bust (>21) and player is less than 21 (p<21) -> player won against dealer
# if dealer >=21: a) dealer < player -> player won against dealer. b) dealer > player -> dealer won against player
            if len(player.hand) == 0:
                i += 1
                continue
            else:
                if player.total <= 21 and self.dealer.total > 21:
                    # player won against dealer
                    self.winner(i)
                elif self.dealer.total <= 21:
                    if self.dealer.total < player.total:
                        # player won against dealer
                        self.winner(i)
                    elif self.dealer.total > player.total:
                        # dealer won against player
                        print("Dealer won against Player '{}'".format(player.name))
                i += 1

#~~~ game is over so you should probably be incrementing the game count orrrrrrrrrr it should be in newgame

        

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
# game = BlackJack()
# game.addPlayer()
# print("\n")
# # give player 2 cards then print their hand
# game.hit(0)
# game.hit(0)
# print(game.allPlayers[0].showHand())
# print(game.allPlayers[0].total)
# print("\n")
# # give player another card and print hand
# game.hit(0)
# print(game.allPlayers[0].showHand())
# print(game.allPlayers[0].total)
# print("\n")
# # give player another card and print hand
# game.hit(0)
# print(game.allPlayers[0].showHand())
# print(game.allPlayers[0].total)
# print("\n")

# now do the same but add 2 players
# game = BlackJack()
# game.addPlayer()
# game.addPlayer()
# print("\n")
# # give player 2 cards then print their hand
# game.hit(0)
# game.hit(1)
# game.hit(0)
# game.hit(1)
# print(game.allPlayers[0].showHand())
# print(game.allPlayers[0].total)
# print("\n")
# print(game.allPlayers[1].showHand())
# print(game.allPlayers[1].total)
# print("\n")
# # give player another card and print hand
# game.hit(0)
# game.hit(1)
# print(game.allPlayers[0].showHand())
# print(game.allPlayers[0].total)
# print("\n")
# print(game.allPlayers[1].showHand())
# print(game.allPlayers[1].total)
# print("\n")
# # give player another card and print hand
# print("Did anyone go bust:")
# game.hit(0)
# game.hit(1)
# print("\n")
# print(game.allPlayers[0].showHand())
# print(game.allPlayers[0].total)
# print("\n")
# print(game.allPlayers[1].showHand())
# print(game.allPlayers[1].total)
# print("\n")

# # Test a 3rd player with artifically manufactured 21
# game.addPlayer()
# ace = Card("Spades", "Ace", 11)
# royal = Card("Spades", "King", 10)
# game.allPlayers[2].addHand(ace)
# game.allPlayers[2].addHand(royal)
# print(game.allPlayers[2].showHand())
# print(game.allPlayers[2].total)

# game.checkTotal(2)

# # test with card values: 10, 10, 1
# game.addPlayer()
# ace = Ace("Spades", "Ace", 11, 1)
# ten = Card("Spades", "10", 10)
# royal = Card("Spades", "King", 10)
# game.allPlayers[2].addHand(ten)
# game.allPlayers[2].addHand(royal)
# game.allPlayers[2].addHand(ace)
# print(game.allPlayers[2].ace)
# print(game.allPlayers[2].showHand())
# print(game.allPlayers[2].total)

# game.checkTotal(2)

# Test July 22/2021
# test compare2dealer 
# create a game with 3 player
g = BlackJack()
g.addPlayer()
g.addPlayer()
g.addPlayer()
# give each player and dealer 2 cards
print("\n")
g.hitDealer()
g.hit(0)
g.hit(1)
g.hit(2)
g.hitDealer()
g.hit(0)
g.hit(1)
g.hit(2)
# give each player another cardA
print("\nGive players another card:")
print(g.hit(0))
print(g.hit(1))
print(g.hit(2))
# print(g.allPlayers[0].showHand())
# print(g.allPlayers[1].showHand())
# print(g.allPlayers[2].showHand())
# give dealer more cards
#g.hitDealer()

#print(g.dealer.showHand())
# compare to dealer to see winners
#print(g.compare2dealer())







    