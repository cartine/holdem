from Peter7CardBestHandRemastered2 import best_hands
from poker5 import *


def run_long_test():
    deck = get_deck()
    hand = deck[0:7]
    print('Hand: ', hand)
    score = get_score(hand)
    print(score)
    pips = [i for i, j in hand]
    suits = [j for i, j in hand]
    score2 = best_hands(*pips, *suits)
    print(score2)
    if score.RANKING != score2.RANKING:
        raise Exception("Rankings are not equal")
    for i in range(0, 5):
        if score2.HAND[i] != get_pip(score.HAND[i][0]):
            raise Exception("card " + str(i) + ": " + str(score2.HAND[i]) + " does not equal " + str(get_pip(score.HAND[i][0])))


if __name__ == '__main__':
    for x in range(0, 100):
        run_long_test()
        print()
        print()