from typing import List

from game2 import *
from poker5 import get_score
from poker5 import Score
from poker5 import get_deck
import copy

PLAYER_NAME_MAX_LENGTH = 20


class TableState:
    def __init__(self, table: Table, players: List[Player], betting_round: BettingRound):
        self.TABLE = table
        self.PLAYERS = players.copy()
        self.BETTING_ROUND = betting_round
        self.SEATS = [Seat(player) for player in players]
        self.NUM_PLAYERS = len(players)

    def update_blinds(self, index_of_sb, index_of_bb):
        sb = self.PLAYERS[index_of_sb]
        sb.CHIPS -= self.TABLE.SMALL_BLIND
        self.TABLE.POT += self.TABLE.SMALL_BLIND
        print(f'Action: {sb.NAME} | SMALL BLIND | Chips Left: {sb.CHIPS} | Pot={self.TABLE.POT}')

        bb = self.PLAYERS[index_of_bb]
        bb.CHIPS -= self.TABLE.BIG_BLIND
        self.TABLE.POT += self.TABLE.BIG_BLIND
        print(f'Action: {bb.NAME} | BIG BLIND | Chips Left: {bb.CHIPS} | Pot={self.TABLE.POT}')

        for i in range(0, self.NUM_PLAYERS):
            if i == index_of_sb:
                self.SEATS[i].AMOUNT_NEEDED_TO_CALL = self.TABLE.BIG_BLIND - self.TABLE.SMALL_BLIND
            elif i == index_of_bb:
                self.SEATS[i].AMOUNT_NEEDED_TO_CALL = 0
            else:
                self.SEATS[i].AMOUNT_NEEDED_TO_CALL = self.TABLE.BIG_BLIND

    def find_index_of_next_player(self, index_of_last_player):
        index_of_next_player = -1

        remaining_players = 0
        for seat in self.SEATS:
            if seat.NOT_FOLDED:
                remaining_players += 1

        if remaining_players > 1:
            for i in range(1, self.NUM_PLAYERS):
                j = (index_of_last_player + i) % self.NUM_PLAYERS
                seat = self.SEATS[j]
                if seat.NOT_FOLDED:
                    if (not seat.HAD_CHANCE_TO_ACT) or (seat.AMOUNT_NEEDED_TO_CALL > 0):
                        index_of_next_player = j
                        break

        return index_of_next_player

    # returns the index of the next player to play, or -1 if the betting round is over
    def play(self, index_of_player) -> int:
        # initialize things
        seat = self.SEATS[index_of_player]
        player = seat.PLAYER

        # make sure this player should be allowed to play
        if not seat.NOT_FOLDED:
            raise Exception("Illegal State - this player can't play, he already folded or has no chips")
        elif seat.HAD_CHANCE_TO_ACT and seat.AMOUNT_NEEDED_TO_CALL == 0:
            raise Exception("Illegal State - This player can't play - he had his chance and there is no bet to call")

        # play
        choice, raze = player.decide(self.TABLE, self.BETTING_ROUND, seat.AMOUNT_NEEDED_TO_CALL, self.SEATS, index_of_player)
        if choice == Action.RAISE and raze <= 0:
            raise Exception(f"Illegal action, a raise must be a positive amount. raise={raze}, player={player.NAME}")
        seat.HAD_CHANCE_TO_ACT = True
        if choice == Action.FOLD:
            seat.NOT_FOLDED = False
        elif choice == Action.CALL:
            if seat.AMOUNT_NEEDED_TO_CALL <= player.CHIPS:
                player.CHIPS -= seat.AMOUNT_NEEDED_TO_CALL
                player.CHIPS_IN += seat.AMOUNT_NEEDED_TO_CALL
                self.TABLE.POT += seat.AMOUNT_NEEDED_TO_CALL
                seat.AMOUNT_NEEDED_TO_CALL = 0
            else:
                player.CHIPS -= player.CHIPS
                player.CHIPS_IN += player.CHIPS
                self.TABLE.POT += player.CHIPS
                seat.AMOUNT_NEEDED_TO_CALL = 0
        elif choice == Action.RAISE:
            if seat.AMOUNT_NEEDED_TO_CALL + raze <= player.CHIPS:
                player.CHIPS -= seat.AMOUNT_NEEDED_TO_CALL + raze
                player.CHIPS_IN += seat.AMOUNT_NEEDED_TO_CALL + raze
                self.TABLE.POT += seat.AMOUNT_NEEDED_TO_CALL + raze
                seat.AMOUNT_NEEDED_TO_CALL = 0
            else:
                player.CHIPS -= player.CHIPS
                player.CHIPS_IN += player.CHIPS
                self.TABLE.POT += player.CHIPS
                seat.AMOUNT_NEEDED_TO_CALL = 0
            for i in range(self.NUM_PLAYERS):
                if i != index_of_player:
                    self.SEATS[i].AMOUNT_NEEDED_TO_CALL += raze
        else:
            raise Exception(f"Player's choice not recognized. Choice={choice}, player={player.NAME}")

        # output what happened
        x = str(choice)
        if choice == Action.RAISE:
            x = x + ' ' + str(raze)
        print(f'Action: {player.NAME} | {x} | Chips Left: {player.CHIPS} | Pot={self.TABLE.POT}')

        # return the index of the next player to play, or -1 if the betting round is over
        return self.find_index_of_next_player(index_of_player)

    # returns an ordered list of the players that have not folded yet
    def play_betting_round(self) -> List[Player]:
        print()
        print(f'Betting round: {self.BETTING_ROUND}')

        # pre-flop setup: small_blind, big_blind, figure out who goes first
        if self.BETTING_ROUND == BettingRound.PRE_FLOP:
            if self.NUM_PLAYERS == 2:
                # Remember, in pre-flop betting, when there are only 2 players, order of play is reversed.
                self.update_blinds(1, 0)
                index_of_next_player = 1
            elif self.NUM_PLAYERS > 2:
                self.update_blinds(0, 1)
                index_of_next_player = 2
            else:
                raise Exception("Illegal state")
        else:
            index_of_next_player = 0

        # do all the betting
        while index_of_next_player != -1:
            index_of_next_player = self.play(index_of_next_player)

        # return list of players who haven't folded yet
        to_return = []
        for i in range(self.NUM_PLAYERS):
            if self.SEATS[i].NOT_FOLDED:
                to_return.append(self.PLAYERS[i])
        return to_return


# returns an ordered list of the players that have not folded yet
def play_betting_round(betting_round: BettingRound, table: Table, players: List[Player]) -> List[Player]:
    ts = TableState(table, players, betting_round)
    return ts.play_betting_round()


# Return a 1 or a 0 for each score; 1 means winner, 0 means loser
def find_results(scores: List[Score]) -> List[int]:
    to_return = [0] * len(scores)

    best_score = scores[0]
    to_return[0] = 1

    for i in range(1, len(scores)):
        check = best_score.compare(scores[i])
        if check == 0:
            to_return[i] = 1
        elif check < 0:
            to_return[i] = 1
            best_score = scores[i]
            for j in range(0, i):
                to_return[j] = 0

    return to_return


# remember that players[0] is the button.
# invariants that should have been checked before calling this function:
#  - there have to be at least 2 players
#  - each player has to have enough chips to cover the big blind
def play_hand(players: List[Player], table: Table, hand_number: int):

    # announce the hand number
    print()
    print(f'playing Hand #{hand_number}')
    for player in players:
        print('    ' + str(player))

    # initialize stuff
    table.reset()

    # deal the cards
    deck = get_deck(shuffled=True)
    n = len(players)
    for i in range(0, n):
        players[i].HAND = deck[2*i:(2*i)+2]
    shared_cards = deck[n*2:(n*2)+5]

    # play the betting rounds
    still_in = players
    for betting_round in BettingRound:
        table.SHARED_CARDS_SHOWING = shared_cards[0:betting_round.value]
        still_in = play_betting_round(betting_round, table, still_in)  # returns players who haven't folded (ordered)
        if len(still_in) <= 0:
            raise Exception("Internal Error - the players cannot all fold!")
        elif len(still_in) == 1:
            break

    # betting is done. If there's more than one player who stayed to the end, figure out who won
    if len(still_in) >= 1:
        # ordered list of Score objects; one for each player who stayed in
        scores = [get_score(player.HAND + shared_cards) for player in still_in]
        results = find_results(scores)  # list of 1's and 0's: A 1 means the player won, a 0 means the player lost
    else:
        raise Exception("Internal Error - there has to be at least one winner")

    # # output the result of the hand
    # # remember that it could be a tie, in which case there will be more than 1 winner
    print()
    print('The hand is over')
    print('The pot was: ' + str(table.POT))
    print(f'The shared cards showing were: {table.SHARED_CARDS_SHOWING}')
    print('The winners and losers (all the players who never folded) are:')
    for i in range(0, len(still_in)):
        if results[i] == 1:
            print(f'  Winner: {still_in[i].NAME}, cards: {still_in[i].HAND}, score: {scores[i]}')
        elif results[i] == 0:
            print(f'  Loser:  {still_in[i].NAME}, cards: {still_in[i].HAND}, score: {scores[i]}')
        else:
            raise Exception(f'Invalid state: results should be all 1s and 0s, but results={results}')

    # give the winner his winnings

    number_of_winners = sum(results)
    assert number_of_winners >= 1
    total = table.POT
    players_paid = 0
    amt_paid = 0
    for i in range(0, len(still_in)):
        if results[i] == 1:
            players_paid += 1
            total_paid = round(total * players_paid / number_of_winners)
            still_in[i].CHIPS += (total_paid - amt_paid)
            amt_paid = total_paid
    leftover = total - amt_paid
    if leftover != 0:
        raise Exception(f'"leftover" must be zero, but it is {leftover}')


def check_params(starting_players: List[Player], small_blind: int, big_blind: int):
    assert len(starting_players) >= 2
    assert len(starting_players) <= 23
    assert small_blind > 0
    assert big_blind > small_blind
    for i in range(0, len(starting_players)):
        assert starting_players[i].CHIPS >= big_blind
        assert starting_players[i].NAME == starting_players[i].NAME.strip()
        assert len(starting_players[i].NAME) < PLAYER_NAME_MAX_LENGTH
        for j in range((i+1), len(starting_players)):
            assert starting_players[i].NAME != starting_players[j].NAME


# Remove players from the game if they don't have enough chips
def remove_losers(players: List[Player], big_blind: int) -> List[Player]:
    to_return = players.copy()
    any_removed = False
    for i in reversed(range(0, len(players))):
        if players[i].CHIPS < big_blind:
            if not any_removed:
                any_removed = True
                print()
                print('Removing 1 or more players for insufficient chips:')
            print('Removing: ', players[i])
            to_return.pop(i)

    # return
    return to_return


# Play a game of holdem. There are 23 seats (maximum). Players are removed when their chips are less than the big blind.
# The game ends when only 1 player is left.
# Currently, the game does not stop a player from betting more chips than he has. (So a player's chips can go negative.)
# There are no rules restricting raises.
#
# Params:
# The first param is a list of Players. The order of the list determines the order of play. The first Player in the list
# is the player immediately to the left of the dealer in the first hand.
#
# Returns: the number of hands played
def play_holdem(starting_players: List[Player], small_blind: int, big_blind: int) -> int:
    check_params(starting_players, small_blind, big_blind)

    # initialize stuff
    players = starting_players.copy()
    table = Table(small_blind, big_blind)
    hand_number = 0

    # play
    print("Starting a game of Texas Holdem")
    print("===============================")
    while len(players) >= 2:
        hand_number += 1
        play_hand(players, table, hand_number)
        players = players[1:] + players[0:1]  # move the button
        players = remove_losers(players, big_blind)

    # the game is over, so output the result
    print()
    print("===============================")
    print(f'{hand_number} hands were played. Here is the winner:')
    print(players[0])

    # return the number of hands played
    return hand_number
