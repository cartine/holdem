import random
import numpy as np
from Peter7CardBestHand import flushes_kicker

if __name__ == '__main__':
    pips = [2, 3, 4, 5, 6, 7, 8, 9, 'T', 'J', 'Q', 'K', 'A']
    heart = ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H']
    spade = ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']
    club = ['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C']
    diamond = ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D']
    hearts = list(zip(pips, heart))
    spades = list(zip(pips, spade))
    clubs = list(zip(pips, club))
    diamonds = list(zip(pips, diamond))
    deck = hearts + spades + clubs + diamonds
    hands = random.sample(deck, 10)
    hand_1 = np.array(hands[:7])
    hand_2 = np.array(hands[7:])
    hand_1_pip = hand_1[:, 0]
    hand_1_suit = hand_1[:, 1]
    print(hand_1)
    print(hand_2)
    print(hand_1_pip)


if __name__ == '__main__':
    fring = flushes_kicker(*hand_1_suit)
    print(fring)

