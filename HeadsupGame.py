from poker5 import *
from MessAround import *
import random

# todo z
# move the classes out of the file with the program. Need to write multiple programs that access the classes.
#
# after I make the other changes, make a game that works for more than 2 players
#
# change poker5 so it uses a 'card' object (make it into poker6?)
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


class Choice(Enum):
    # Note that there is no 'pass' or 'check'. For that, use 'call'
    FOLD = "fold"
    CALL = "call"  # match the bet in the active pot (which could be zero or more), but do not raise
    RAISE = "raise"  # match the bet in the active pot, and also bet more


class Player:
    def __init__(self, chips, name):
        self.CHIPS = chips
        self.HAND = None
        self.NAME = name

    # This is what you override in a child class to make a Player useful
    # returns a Choice, and the raise amount.
    # The raise amount will be ignored if the Choice is not Choice.RAISE.
    def decide(self, the_table: Table, betting_round):
        return Choice.FOLD, 0

    def __str__(self):
        return f'player name = {self.NAME}, player type = ' + str(type(self)) + f', chips = {self.CHIPS}'


class CPUPlayer(Player):
    def decide(self, the_table: Table, betting_round):
        if the_table.ACTIVE > 0:
            decision = random.randint(1, 3)
        else:
            decision = random.randint(1, 2)
        if decision == 1:
            return Choice.CALL, 0
        elif decision == 2:
            raise_amount = random.randint(1, 10)
            return Choice.RAISE, raise_amount
        elif decision == 3:
            return Choice.FOLD, 0
        else:
            raise Exception('Illegal State')


class CLPlayer(Player):
    def decide(self, the_table: Table, betting_round):
        print()
        print(f'{self.HAND} -> cards dealt to {self.NAME}')
        print(f'{the_table.SHARED_CARDS_SHOWING} -> shared cards showing')
        print(f'{the_table.POT} -> the pot')
        print(f'{the_table.ACTIVE} -> the active pot')
        if the_table.ACTIVE > 0:
            choice = input(f'Enter decision for {self.NAME}: CALL, RAISE or FOLD? ')
            if choice.upper() == 'CALL':
                return Choice.CALL, 0
            elif choice.upper() == 'RAISE':
                raise_amount = int(input('Amount of raise: '))
                return Choice.RAISE, raise_amount
            else:
                return Choice.FOLD, 0
        else:
            choice = input(f'Enter decision for {self.NAME}: RAISE or CHECK? ')
            if choice.upper() == 'RAISE':
                raise_amount = int(input('Amount of raise: '))
                return Choice.RAISE, raise_amount
            else:
                return Choice.CALL, 0


class BettingRound(Enum):
    # value indicates the number of shared cards that are visible
    PRE_FLOP = 0
    POST_FLOP = 3
    POST_TURN = 4
    POST_RIVER = 5


class Table:
    def __init__(self, small_blind: int, big_blind: int):
        self.SMALL_BLIND = small_blind
        self.BIG_BLIND = big_blind
        self.ACTIVE = 0
        self.POT = 0
        self.SHARED_CARDS_SHOWING = None

    def reset(self):
        self.ACTIVE = 0
        self.POT = 0
        self.SHARED_CARDS_SHOWING = []

    def take_chips(self, p: Player, c: Choice, raze: int):
        if c is Choice.CALL:
            p.CHIPS -= self.ACTIVE
            self.POT += 2 * self.ACTIVE
            self.ACTIVE = 0
        elif c is Choice.RAISE:
            p.CHIPS -= self.ACTIVE + raze
            self.POT += 2 * self.ACTIVE
            self.ACTIVE = raze

    # def __str__(self):
    #     return self.POT + ", " + str(self.COM_CARDS)


# Return the winner and the loser. But if it is a tie, return None, None.
def find_winner_and_loser(p1, p2, shared_cards) -> [Player, Player]:
    score1 = get_score(p1.HAND + shared_cards)
    score2 = get_score(p2.HAND + shared_cards)
    print()
    print(f'{p1.NAME} has: {score1}')
    print(f'{p2.NAME} has: {score2}')
    c = score1.compare(score2)
    if c == 0:  # this is a tie!
        return None, None
    elif c > 0:
        return p1, p2
    else:
        return p2, p1


# If a player folds, return the winner and the loser. Otherwise, return None, None
def check_and_announce(p1, choice, raze):
    if choice is None:
        raise Exception("choice is 'None' - invalid")
    elif choice is Choice.RAISE:
        if raze <= 0:
            raise Exception(f'A raise amount must be positive. Player {p1.NAME} raised "{raze}".')
        print(f'Action: {p1.NAME} | {choice.name} | amount={raze}')
    else:
        print(f'Action: {p1.NAME} | {choice.name}')


def play_betting_round(betting_round: BettingRound, table: Table, smallblind_player: Player, bigblind_player: Player):
    # 'small blind' is the dealer. dealer goes 1st in Pre-flop betting, last in the other rounds

    print()
    print(f'Betting round: {betting_round}')

    if betting_round is BettingRound.PRE_FLOP:
        table.take_chips(smallblind_player, Choice.RAISE, table.SMALL_BLIND)
        table.take_chips(bigblind_player, Choice.RAISE, table.BIG_BLIND - table.SMALL_BLIND)
        p1, p2 = smallblind_player, bigblind_player
    else:
        p1, p2 = bigblind_player, smallblind_player

    choice, raze = p1.decide(table, betting_round)
    check_and_announce(p1, choice, raze)
    table.take_chips(p1, choice, raze)

    if choice is not Choice.FOLD:
        p1, p2 = p2, p1
        choice, raze = p1.decide(table, betting_round)
        check_and_announce(p1, choice, raze)
        table.take_chips(p1, choice, raze)

    while choice is Choice.RAISE:
        p1, p2 = p2, p1
        choice, raze = p1.decide(table, betting_round)
        check_and_announce(p1, choice, raze)
        table.take_chips(p1, choice, raze)

    if choice is Choice.FOLD:
        return p2, p1
    else:
        return None, None


def play_hand(smallblind_player: Player, bigblind_player: Player, table: Table, hand_number: int):

    # announce the hand number
    print()
    print(f'playing Hand #{hand_number}')
    print('  smallblind:', smallblind_player)
    print('  bigblind:  ', bigblind_player)

    # initialize stuff
    table.reset()
    winner, loser = None, None

    # deal the cards
    deck = get_deck(True)
    smallblind_player.HAND = deck[0:2]
    bigblind_player.HAND = deck[2:4]
    shared_cards = deck[4:9]

    # play the betting rounds
    for round in BettingRound:
        table.SHARED_CARDS_SHOWING = shared_cards[0:round.value]
        winner, loser = play_betting_round(round, table, smallblind_player, bigblind_player)
        if winner is not None:
            break

    # betting is done
    # if a player folded, then we already have a winner.
    # Otherwise, we got through all betting rounds, and now we have to check the cards to see who won.
    if winner is None:
        winner, loser = find_winner_and_loser(smallblind_player, bigblind_player, shared_cards)

    # output the result of the hand
    # remember that it could be a tie, denoted by (winner is None)
    print()
    print('The hand is over')
    print('The pot was: ' + str(table.POT))
    print('The active pot was: ' + str(table.ACTIVE))
    if winner is None:
        print('It was a tie')
    else:
        print('The winner is:', winner.NAME)
    print('The cards were:')
    print(f'  {smallblind_player.HAND} -> {smallblind_player.NAME}')
    print(f'  {bigblind_player.HAND} -> {bigblind_player.NAME}')
    print(f'  {table.SHARED_CARDS_SHOWING} -> shared cards')

    # give the winner his winnings
    if winner is not None:
        winner.CHIPS += table.POT + table.ACTIVE
    else:
        # In this case we have a tie, and the pot has to  be split
        assert(table.ACTIVE == 0)  # It should be impossible for it not to be zero here
        halfpot = table.POT/2
        assert(2 * halfpot == table.POT)  # In 2 player game, if no one folds, the pot has to be an even number
        smallblind_player.CHIPS += halfpot
        bigblind_player.CHIPS += halfpot


# Play until one player has zero or less chips
def play_holdem(firstdealer: Player, otherguy: Player, small_blind: int, big_blind: int) -> None:
    assert(small_blind > 0)
    assert(big_blind > small_blind)
    assert(firstdealer.CHIPS >= big_blind)
    assert(otherguy.CHIPS >= big_blind)

    # initialize stuff
    print("Starting a Heads up game")
    print("========================")
    smallblind_player, bigblind_player = firstdealer, otherguy
    table = Table(small_blind, big_blind)
    hand_number = 0

    # play
    while (smallblind_player.CHIPS > big_blind) and (bigblind_player.CHIPS > big_blind):
        hand_number += 1
        play_hand(smallblind_player, bigblind_player, table, hand_number)
        # switch smallblind and bigblind
        smallblind_player, bigblind_player = bigblind_player, smallblind_player

    # the game is over, so output the result
    print()
    print('========================')
    print(f'{hand_number} hands were played. Here is how the players fared:')
    print(player1)
    print(player2)


if __name__ == '__main__':
    player1 = CPUPlayer(50, "Player 1")
    player2 = CPUPlayer2(25, "Player 2")
    play_holdem(player1, player2, 5, 10)
