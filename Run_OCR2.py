from OCR2 import *
from PeterPokerBot3 import *

filename = r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (655).png'
hole_cards = find_hole_cards(filename)


def run_OCR2(filename, seat1_hand):
    seats, self_index, self_chips, self_hand = creating_seats(filename, seat1_hand)
    call_amount = find_call_amount(filename)
    pot = find_total_pot(filename)
    com_cards = find_com_cards(filename)
    table = Table(2, 4)
    table.POT = pot
    table.SHARED_CARDS_SHOWING = com_cards
    self = CPUPlayer3(self_chips, 'Self')
    self.HAND = self_hand
    print(self_hand)
    print('betting round:', len(com_cards))
    print(com_cards)
    print('self index:', self_index)
    decision, raise_amount = self.decide(table, BettingRound(len(com_cards)), call_amount, seats, self_index)
    return decision, raise_amount, call_amount, self_chips, pot, self_index, len(seats)


if __name__ == '__main__':
    print(run_OCR2(filename, hole_cards))
