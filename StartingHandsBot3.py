import numpy as np
from HeadsupGame import get_deck
from Peter7CardBestHand import face_cards


dealer_starting_hands_3bet = ['AA', 'KK', 'A5s']
dealer_starting_hands_call = ['QQ', 'JJ', 'TT', '99', '88', '77', '66', '55', '44', '33', '22', 'AKs', 'AQs', 'AJs', 'ATs', 'KQs', 'KJs', 'KTs', 'QJs', 'QTs', 'JTs', 'T9s', '98s', '87s', '76s', 'AK']
dealer_starting_hands_open_raise = ['A9s', 'A8s', 'A7s', 'A6s', 'A4s', 'A3s', 'A2s', 'K9s', 'K8s', 'K7s', 'K6s', 'K5s', 'K4s', 'K3s', 'K2s', 'Q9s', 'Q8s', 'Q7s', 'Q6s', 'Q5s', 'J9s', 'J8s', 'J7s', 'T8s', 'T7s', '97s', '96s', '86s', '75s', '65s', '64s', '54s', '53s', '43s', 'AQ', 'AJ', 'AT', 'A9', 'A8', 'A7', 'KQ', 'KJ', 'KT', 'K9', 'QJ', 'QT', 'JT']
cutoff_starting_hands_3bet = ['AA', 'KK', 'A5s']
cutoff_starting_hands_call = ['QQ', 'JJ', 'TT', '99', '88', '77', '66', '55', '44', '33', '22', 'AKs', 'AQs', 'AJs', 'ATs', 'KQs', 'KJs', 'KTs', 'QJs', 'QTs', 'JTs', 'T9s', '98s', '87s', '76s', 'AK']
cutoff_starting_hands_open_raise = ['A9s', 'A8s', 'A7s', 'A6s', 'A4s', 'A3s', 'A2s', 'K9s', 'K8s', 'K7s', 'Q9s', 'J9s', 'T8s', '97s', '86s', '75s', '65s', '64s', '54s', '53s', '43s', 'AQ', 'AJ', 'AT', 'KQ', 'KJ']
ep_and_blind_raise_starting_hands_3bet = ['AA', 'KK', 'A5s']
ep_and_blind_raise_starting_hands_call = ['QQ', 'JJ', 'TT', '99', '88', '77', '66', '55', '44', '33', '22', 'AKs', 'AQs', 'AJs', 'ATs', 'KQs', 'KJs', 'KTs', 'QJs', 'QTs', 'JTs', 'T9s', '98s', '87s', '76s', 'AK']
ep_starting_hands_open_raise = ['A9s', 'A8s', 'A7s', 'A6s', 'A4s', 'A3s', 'A2s', 'AQ']
blind_limp_starting_hands_open_raise = ['AA', 'KK', 'QQ', 'JJ', 'TT', '99', 'AKs', 'AQs', 'AJs', 'ATs', 'KQs', 'KJs', 'AK', 'AQ']


# if __name__ == '__main__':
#     deck = get_deck()
#     hand = deck[:2]
#     pips = []
#     suits = []
#     for e in hand:
#         pips.append(e[0])
#         suits.append(e[1])
#     print(hand)
#     print(pips)
#     print(suits)
#     pips = sorted(pips, key= lambda x: int(face_cards(x)), reverse=True)
#     if suits[0] == suits[1]:
#         hand = pips[0] + pips[1] + 's'
#     else:
#         hand = pips[0] + pips[1]
#         hand = str(hand)
#     print(hand)
#     hand_index = hand in dealer_starting_hands_open_raise
#     print(hand_index)