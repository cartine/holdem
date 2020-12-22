# from game import *
# from HeadsupGame import play_holdem
from game2 import *
from multiplayer_holdem_game import play_holdem

# todo z
#
# Tell the program what cards were dealt to us and what the shared cards are
#
# make the game let players come and go during the game
#
# add all the callbacks to Players so they have all the information they need
#
# write results to file
#
# allow players to buy back in
#
# make it impossible to go below zero chips (remember case where chips > 0 but chips < big blind for bb player)
#
# change poker5 so it uses a 'card' object (make it into poker6?)
#
# make poker5 work for less than 7 cards
#
#
# refactor so we don't inherit Player; we use a strategy pattern instead
#
# what should we do when one player bets more than the other player has?
# currently we let a player go into the negative.
#
# don't let players bet money they don't have
#
# handle the case where a player doesn't have enough chips to call
#
# we currently don't show any of the cards till the hand is over. Should we show the players cards
# so we can follow the game better?
# - Maybe whether to show a player's card on the screen is a game option?
#
# we don't show the flop, turn or river on the screen. Should we?
#
# make the game run as a service somehow, and attach a UI to it
#
# learn the correct conventions for naming files, classes, etc, and start using them
#
# figure out how people organize python files into packages, and start doing that
#
#
# At some point Peter's bot will need more information than it is getting. It will need to know
# how many players already called before him, how many players will get to bet after him, how
# many players already folded, stuff like that. Work out the details with Peter.
# One idea I have is passing in a history object, showing everything that happened in this betting
# round so far. Another is to have callbacks to other players when a player makes a decision.
#
# check that a player's name has no newlines or line returns, and has a maximum length. In the Player class


def run():
    # player0 = CPUPlayer(5000, "Player 0")
    # player1 = CPUPlayer(5000, "Player 1")
    # player2 = CPUPlayer(5000, "Player 2")
    # player3 = CPUPlayer(5000, "Player 3")
    # player4 = CPUPlayer(5000, "Player 4")
    # player5 = CPUPlayer(5000, "Player 5")
    # player6 = CPUPlayer(5000, "Player 6")
    # player7 = CPUPlayer(5000, "Player 7")
    # player8 = CPUPlayer(5000, "Player 8")
    # player9 = CPUPlayer(5000, "Player 9")
    # player10 = CPUPlayer(5000, "Player 10")
    # player11 = CPUPlayer(5000, "Player 11")
    # player12 = CPUPlayer(5000, "Player 12")
    # player13 = CPUPlayer(5000, "Player 13")
    # player14 = CPUPlayer(5000, "Player 14")
    # player15 = CPUPlayer(5000, "Player 15")
    # player16 = CPUPlayer(5000, "Player 16")
    # player17 = CPUPlayer(5000, "Player 17")
    # player18 = CPUPlayerWhoDoesNotFold(5000, "Player 18")
    # player19 = CPUPlayerWhoDoesNotFold(5000, "Player 19")
    # x = [player0, player1, player2, player3, player4, player5, player6, player7, player8, player9]
    # y = [player10, player11, player12, player13, player14, player15, player16, player17, player18, player19]
    # players = x + y

    player0 = CPUPlayer(50, "Player 0")
    player1 = CPUPlayer(50, "Player 1")
    player2 = CPUPlayer(50, "Player 2")
    player3 = CPUPlayer(50, "Player 3")
    players = [player0, player1, player2, player3]

    play_holdem(players, 1, 2)


if __name__ == '__main__':
    run()
