from random import shuffle

from poker5 import Pip
from poker5 import Suit


class Card:
    def __init__(self, uid, pip, suit):
        self.UID = uid
        self.PIP = pip
        self.SUIT = suit


# The UIDs of the cards are integers in increasing order from 0 to 51; returns identical deck every time
def get_ordered_deck():
    deck = []
    uid = 0
    for pip in Pip:
        for suit in Suit:
            card = Card(uid, pip, suit)
            deck.append(card)
    return deck


# calls get_ordered_deck() and shuffles
def get_shuffled_deck():
    deck = get_ordered_deck()
    shuffle(deck)
    return deck

