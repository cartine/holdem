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
    for x in range(0, 10000000):
        run_long_test()
        print()
        print()


#Hand:  ['4H', 'TH', 'TS', 'TD', 'AS', '4C', 'TC']
#FOUR_OF_A_KIND, ['TH', 'TS', 'TD', 'TC', '4H']
#FOUR_OF_A_KIND, [10, 10, 10, 10, 14]      ^^


#Hand:  ['3D', '4S', '4H', '3H', 'KH', '4D', '4C']
#FOUR_OF_A_KIND, ['4S', '4H', '4D', '4C', '3D']
#FOUR_OF_A_KIND, [4, 4, 4, 4, 13]


#Hand:  ['4S', '6C', '6D', '4D', '4H', '4C', 'TS']
#FOUR_OF_A_KIND, ['4S', '4D', '4H', '4C', '6C']
#FOUR_OF_A_KIND, [4, 4, 4, 4, 10]


#Hand:  ['9C', '4H', '4D', '9D', '9H', '9S', '6D']
#FOUR_OF_A_KIND, ['9C', '9D', '9H', '9S', '4H']
#FOUR_OF_A_KIND, [9, 9, 9, 9, 6]