from OCR import *
from PeterPokerBot3 import *
import cProfile

filename = r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (177).png'


def run_OCR(filename):
    seats, self_index, self_chips, self_hand = creating_seats(filename)
    call_amount = find_call_amount(filename)
    pot = find_total_pot(filename)
    com_cards = find_com_cards(filename)
    table = Table(2, 4)
    table.POT = pot
    table.SHARED_CARDS_SHOWING = com_cards
    self = CPUPlayer3(self_chips, 'Self')
    self.HAND = self_hand
    return self.decide(table, BettingRound(len(com_cards)), call_amount, seats, self_index)


if __name__ == '__main__':
    run_OCR(filename)
