from enum import Enum
import random


class Choice(Enum):
    # Note that there is no 'pass' or 'check'. For that, use 'call'
    FOLD = "fold"
    CALL = "call"
    RAISE = "raise"


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
        self.POT = 0
        self.SHARED_CARDS_SHOWING = None

    def reset(self):
        self.POT = 0
        self.SHARED_CARDS_SHOWING = []


class Player:
    def __init__(self, chips, name):
        self.CHIPS = chips
        self.HAND = None
        self.NAME = name

    # This is what you override in a child class to make a Player useful
    # returns a Choice, and the raise amount.
    # The raise amount will be ignored if the Choice is not Choice.RAISE.
    def decide(self, the_table, betting_round, call_amount):
        return Choice.FOLD, 0

    def __str__(self):
        return f'player name = {self.NAME}, player type = ' + str(type(self)) + f', chips = {self.CHIPS}'


class CPUPlayer(Player):
    def decide(self, the_table, betting_round, call_amount):
        if call_amount > 0:
            decision = random.randint(1, 4)
        else:
            decision = random.randint(2, 4)
        if decision == 1:
            return Choice.FOLD, 0
        elif decision == 2:
            raise_amount = random.randint(1, 10)
            return Choice.RAISE, raise_amount
        if decision >= 3:
            return Choice.CALL, 0
        else:
            raise Exception('Illegal State')


class CLPlayer(Player):
    def decide(self, the_table, betting_round, call_amount):
        print()
        print(f'{self.HAND} -> cards dealt to {self.NAME}')
        print(f'{the_table.SHARED_CARDS_SHOWING} -> shared cards showing')
        print(f'{the_table.POT} -> the pot')
        print(f'{call_amount} -> the amount needed to call')
        if call_amount > 0:
            choice = input(f'Enter decision for {self.NAME}: CALL, RAISE or FOLD? ')
            print()
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


class CPUPlayerWhoDoesNotFold(Player):
    def decide(self, the_table, betting_round, call_amount):
        decision = random.randint(1, 3)
        if decision == 1:
            raise_amount = random.randint(1, 10)
            return Choice.RAISE, raise_amount
        else:
            return Choice.CALL, 0
