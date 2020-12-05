from game import *
from poker5 import get_score
from poker5 import get_deck
import numpy as np


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
    elif choice == Choice.RAISE:
        if raze <= 0:
            raise Exception(f'A raise amount must be positive. Player {p1.NAME} raised "{raze}".')
        print(f'Action: {p1.NAME} | {choice.name} | amount={raze}')
    else:
        print(f'Action: {p1.NAME} | {choice.name}')


def play_betting_round(betting_round: BettingRound, table: Table, smallblind_player: Player, bigblind_player: Player):
    # 'small blind' is the dealer. dealer goes 1st in Pre-flop betting, last in the other rounds

    print()
    print(f'Betting round: {betting_round}')

    if betting_round == BettingRound.PRE_FLOP:
        check_and_announce(smallblind_player, Choice.RAISE, table.SMALL_BLIND)
        table.take_chips(smallblind_player, Choice.RAISE, table.SMALL_BLIND)
        check_and_announce(bigblind_player, Choice.RAISE, table.BIG_BLIND - table.SMALL_BLIND)
        table.take_chips(bigblind_player, Choice.RAISE, table.BIG_BLIND - table.SMALL_BLIND)
        p1, p2 = smallblind_player, bigblind_player
    else:
        p1, p2 = bigblind_player, smallblind_player

    choice, raze = p1.decide(table, betting_round)
    check_and_announce(p1, choice, raze)
    table.take_chips(p1, choice, raze)

    if choice != Choice.FOLD:
        p1, p2 = p2, p1
        choice, raze = p1.decide(table, betting_round)
        check_and_announce(p1, choice, raze)
        table.take_chips(p1, choice, raze)

    while choice == Choice.RAISE:
        p1, p2 = p2, p1
        choice, raze = p1.decide(table, betting_round)
        check_and_announce(p1, choice, raze)
        table.take_chips(p1, choice, raze)

    if choice == Choice.FOLD:
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
        # Todo uncomment when ready
        # assert(table.ACTIVE == 0)  # It should be impossible for it not to be zero here
        halfpot = table.POT/2
        # assert(2 * halfpot == table.POT)  # In 2 player game, if no one folds, the pot has to be an even number
        smallblind_player.CHIPS += halfpot
        bigblind_player.CHIPS += halfpot


# Play headsup (which means 2 players) until one player does not have enough chips at the end of a hand to cover
# the big blind in the next hand.
# Currently, the game does not stop a player from betting more chips than he has.
# There are no rules restricting raises.
def play_holdem(firstdealer: Player, otherguy: Player, small_blind: int, big_blind: int):
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
    while (smallblind_player.CHIPS >= big_blind) and (bigblind_player.CHIPS >= big_blind):
        hand_number += 1
        play_hand(smallblind_player, bigblind_player, table, hand_number)
        # switch smallblind and bigblind
        smallblind_player, bigblind_player = bigblind_player, smallblind_player

    # the game is over, so output the result
    print()
    print('========================')
    print(f'{hand_number} hands were played. Here is how the players fared:')
    print(firstdealer)
    print(otherguy)
    return hand_number


# if __name__ == '__main__':
#     hand_numbers = []
#     for x in range(0, 1000):
#         player1 = CPUPlayer(1000, "Player 1")
#         from PeterPokerBot2 import CPUPlayer2
#         player2 = CPUPlayer2(1000, "Player 2")
#         print()
#         print()
#         hand_numbers.append(play_holdem(player1, player2, 5, 10))
#     print(hand_numbers)
#     np.array(hand_numbers)
#     hn_mean = np.mean(hand_numbers)
#     print(hn_mean)
