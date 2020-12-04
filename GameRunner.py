from game import *
from HeadsupGame import play_holdem

# todo 1: make the game work with more players
# todo 2: make the game let players come and go during the game

# todo z
# after I make the other changes, make a game that works for more than 2 players
#
# change poker5 so it uses a 'card' object (make it into poker6?)
#
# make poker5 work for less than 7 cards
#
# make it impossible to go below zero chips (remember case where chips > 0 but chips < big blind for bb player)
#
# refactor so we don't inherit Player; we use a strategy pattern instead
#
# what should we do when one player bets more than the other player has?
# currently we let a player go into the negative.
#
# currently there is no way for a player to see how many chips the other player has, or who that
# player is. How can I show a player everything about the other players except his cards?
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
# write results to file
#
# make the game run as a service somehow, and attach a UI to it
#
# learn the correct conventions for naming files, classes, etc, and start using them
#
# figure out how people organize python files into packages, and start doing that
#
# Show the pot and the active pot every time we print a line that starts with "Action: "


if __name__ == '__main__':
    player1 = CPUPlayer(25, "Player 1")
    player2 = CLPlayerWhoDoesNotFold(55, "Player 2")
    play_holdem(player1, player2, 5, 10)
