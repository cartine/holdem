import random
from poker5 import Ranking
from poker5 import Score


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
hands = random.sample(deck, 14)
hand_1 = hands[:7]
hand_2 = hands[7:]
card_1 = hand_1[0]
card_1_pip = card_1[0]
card_1_suit = card_1[1]
card_2 = hand_1[1]
card_2_pip = card_2[0]
card_2_suit = card_2[1]
card_3 = hand_1[2]
card_3_pip = card_3[0]
card_3_suit = card_3[1]
card_4 = hand_1[3]
card_4_pip = card_4[0]
card_4_suit = card_4[1]
card_5 = hand_1[4]
card_5_pip = card_5[0]
card_5_suit = card_5[1]
card_6 = hand_1[5]
card_6_pip = card_6[0]
card_6_suit = card_6[1]
card_7 = hand_1[6]
card_7_pip = card_7[0]
card_7_suit = card_7[1]
card_8 = hand_2[0]
card_8_pip = card_8[0]
card_8_suit = card_8[1]
card_9 = hand_2[1]
card_9_pip = card_9[0]
card_9_suit = card_9[1]
card_10 = hand_2[2]
card_10_pip = card_10[0]
card_10_suit = card_10[1]
card_11 = hand_2[3]
card_11_pip = card_11[0]
card_11_suit = card_11[1]
card_12 = hand_2[4]
card_12_pip = card_12[0]
card_12_suit = card_12[1]
card_13 = hand_2[5]
card_13_pip = card_13[0]
card_13_suit = card_13[1]
card_14 = hand_2[6]
card_14_pip = card_14[0]
card_14_suit = card_14[1]


def face_cards(face_card):
    if face_card == '2':
        return 2
    if face_card == '3':
        return 3
    if face_card == '4':
        return 4
    if face_card == '5':
        return 5
    if face_card == '6':
        return 6
    if face_card == '7':
        return 7
    if face_card == '8':
        return 8
    if face_card == '9':
        return 9
    if face_card == 'T':
        return 10
    if face_card == 'J':
        return 11
    if face_card == 'Q':
        return 12
    if face_card == 'K':
        return 13
    if face_card == 'A':
        return 14
    return face_card


def reverse_face_cards(rev_face_card):
    if rev_face_card == 10:
        return 'T'
    if rev_face_card == 11:
        return 'J'
    if rev_face_card == 12:
        return 'Q'
    if rev_face_card == 13:
        return 'K'
    if rev_face_card == 14:
        return 'A'
    if rev_face_card != 10 or 11 or 12 or 13 or 14:
        return rev_face_card


def high_cards(pip1, pip2, pip3, pip4, pip5, pip6, pip7):
    new_pip1 = face_cards(pip1)
    new_pip2 = face_cards(pip2)
    new_pip3 = face_cards(pip3)
    new_pip4 = face_cards(pip4)
    new_pip5 = face_cards(pip5)
    new_pip6 = face_cards(pip6)
    new_pip7 = face_cards(pip7)
    in_order = sorted([new_pip1, new_pip2, new_pip3, new_pip4, new_pip5, new_pip6, new_pip7], reverse=True)
    high_card = in_order[0]
    return high_card


def second_high_cards(pip1, pip2, pip3, pip4, pip5, pip6, pip7):
    new_pip1 = face_cards(pip1)
    new_pip2 = face_cards(pip2)
    new_pip3 = face_cards(pip3)
    new_pip4 = face_cards(pip4)
    new_pip5 = face_cards(pip5)
    new_pip6 = face_cards(pip6)
    new_pip7 = face_cards(pip7)
    in_order = sorted([new_pip1, new_pip2, new_pip3, new_pip4, new_pip5, new_pip6, new_pip7], reverse=True)
    second_high_card = in_order[1]
    return second_high_card


def third_high_cards(pip1, pip2, pip3, pip4, pip5, pip6, pip7):
    new_pip1 = face_cards(pip1)
    new_pip2 = face_cards(pip2)
    new_pip3 = face_cards(pip3)
    new_pip4 = face_cards(pip4)
    new_pip5 = face_cards(pip5)
    new_pip6 = face_cards(pip6)
    new_pip7 = face_cards(pip7)
    in_order = sorted([new_pip1, new_pip2, new_pip3, new_pip4, new_pip5, new_pip6, new_pip7], reverse=True)
    third_high_card = in_order[2]
    return third_high_card


def fourth_high_cards(pip1, pip2, pip3, pip4, pip5, pip6, pip7):
    new_pip1 = face_cards(pip1)
    new_pip2 = face_cards(pip2)
    new_pip3 = face_cards(pip3)
    new_pip4 = face_cards(pip4)
    new_pip5 = face_cards(pip5)
    new_pip6 = face_cards(pip6)
    new_pip7 = face_cards(pip7)
    in_order = sorted([new_pip1, new_pip2, new_pip3, new_pip4, new_pip5, new_pip6, new_pip7], reverse=True)
    fourth_high_card = in_order[3]
    return fourth_high_card


def fifth_high_cards(pip1, pip2, pip3, pip4, pip5, pip6, pip7):
    new_pip1 = face_cards(pip1)
    new_pip2 = face_cards(pip2)
    new_pip3 = face_cards(pip3)
    new_pip4 = face_cards(pip4)
    new_pip5 = face_cards(pip5)
    new_pip6 = face_cards(pip6)
    new_pip7 = face_cards(pip7)
    in_order = sorted([new_pip1, new_pip2, new_pip3, new_pip4, new_pip5, new_pip6, new_pip7], reverse=True)
    fifth_high_card = in_order[4]
    return fifth_high_card


def sixth_high_cards(pip1, pip2, pip3, pip4, pip5, pip6, pip7):
    new_pip1 = face_cards(pip1)
    new_pip2 = face_cards(pip2)
    new_pip3 = face_cards(pip3)
    new_pip4 = face_cards(pip4)
    new_pip5 = face_cards(pip5)
    new_pip6 = face_cards(pip6)
    new_pip7 = face_cards(pip7)
    in_order = sorted([new_pip1, new_pip2, new_pip3, new_pip4, new_pip5, new_pip6, new_pip7], reverse=True)
    sixth_high_card = in_order[5]
    return sixth_high_card

def seventh_high_cards(pip1, pip2, pip3, pip4, pip5, pip6, pip7):
    new_pip1 = face_cards(pip1)
    new_pip2 = face_cards(pip2)
    new_pip3 = face_cards(pip3)
    new_pip4 = face_cards(pip4)
    new_pip5 = face_cards(pip5)
    new_pip6 = face_cards(pip6)
    new_pip7 = face_cards(pip7)
    in_order = sorted([new_pip1, new_pip2, new_pip3, new_pip4, new_pip5, new_pip6, new_pip7], reverse=True)
    seventh_high_card = in_order[6]
    return seventh_high_card


def pairs(pip1, pip2, pip3, pip4, pip5, pip6, pip7):
    new_pip1 = face_cards(pip1)
    new_pip2 = face_cards(pip2)
    new_pip3 = face_cards(pip3)
    new_pip4 = face_cards(pip4)
    new_pip5 = face_cards(pip5)
    new_pip6 = face_cards(pip6)
    new_pip7 = face_cards(pip7)
    pair = 0
    if new_pip1 == new_pip2:
        pair = new_pip1
    if new_pip1 == new_pip3:
        pair = new_pip1
    if new_pip1 == new_pip4:
        pair = new_pip1
    if new_pip1 == new_pip5:
        pair = new_pip1
    if new_pip1 == new_pip6:
        pair = new_pip1
    if new_pip1 == new_pip7:
        pair = new_pip1
    if new_pip2 == new_pip3:
        pair = new_pip2
    if new_pip2 == new_pip4:
        pair = new_pip2
    if new_pip2 == new_pip5:
        pair = new_pip2
    if new_pip2 == new_pip6:
        pair = new_pip2
    if new_pip2 == new_pip7:
        pair = new_pip2
    if new_pip3 == new_pip4:
        pair = new_pip3
    if new_pip3 == new_pip5:
        pair = new_pip3
    if new_pip3 == new_pip6:
        pair = new_pip3
    if new_pip3 == new_pip7:
        pair = new_pip3
    if new_pip4 == new_pip5:
        pair = new_pip4
    if new_pip4 == new_pip6:
        pair = new_pip4
    if new_pip4 == new_pip7:
        pair = new_pip4
    if new_pip5 == new_pip6:
        pair = new_pip5
    if new_pip5 == new_pip7:
        pair = new_pip5
    if new_pip6 == new_pip7:
        pair = new_pip6
    return pair


def two_pairs(pip1, pip2, pip3, pip4, pip5, pip6, pip7):
    new_pip1 = face_cards(pip1)
    new_pip2 = face_cards(pip2)
    new_pip3 = face_cards(pip3)
    new_pip4 = face_cards(pip4)
    new_pip5 = face_cards(pip5)
    new_pip6 = face_cards(pip6)
    new_pip7 = face_cards(pip7)
    two_pair = 0
    if (new_pip1 == new_pip2) and (new_pip3 == new_pip4):
        two_pair = new_pip1
        if new_pip3 > new_pip1:
            two_pair = new_pip3
    if (new_pip1 == new_pip2) and (new_pip3 == new_pip5):
        two_pair = new_pip1
        if new_pip3 > new_pip1:
            two_pair = new_pip3
    if (new_pip1 == new_pip2) and (new_pip3 == new_pip6):
        two_pair = new_pip1
        if new_pip3 > new_pip1:
            two_pair = new_pip3
    if (new_pip1 == new_pip2) and (new_pip3 == new_pip7):
        two_pair = new_pip1
        if new_pip3 > new_pip1:
            two_pair = new_pip3
    if (new_pip1 == new_pip2) and (new_pip4 == new_pip5):
        two_pair = new_pip1
        if new_pip4 > new_pip1:
            two_pair = new_pip4
    if (new_pip1 == new_pip2) and (new_pip4 == new_pip6):
        two_pair = new_pip1
        if new_pip4 > new_pip1:
            two_pair = new_pip4
    if (new_pip1 == new_pip2) and (new_pip4 == new_pip7):
        two_pair = new_pip1
        if new_pip4 > new_pip1:
            two_pair = new_pip4
    if (new_pip1 == new_pip2) and (new_pip5 == new_pip6):
        two_pair = new_pip1
        if new_pip5 > new_pip1:
            two_pair = new_pip5
    if (new_pip1 == new_pip2) and (new_pip5 == new_pip7):
        two_pair = new_pip1
        if new_pip5 > new_pip1:
            two_pair = new_pip5
    if (new_pip1 == new_pip2) and (new_pip6 == new_pip7):
        two_pair = new_pip1
        if new_pip6 > new_pip1:
            two_pair = new_pip6
    if (new_pip1 == new_pip3) and (new_pip4 == new_pip5):
        two_pair = new_pip1
        if new_pip4 > new_pip1:
            two_pair = new_pip4
    if (new_pip1 == new_pip3) and (new_pip4 == new_pip6):
        two_pair = new_pip1
        if new_pip4 > new_pip1:
            two_pair = new_pip4
    if (new_pip1 == new_pip3) and (new_pip4 == new_pip7):
        two_pair = new_pip1
        if new_pip4 > new_pip1:
            two_pair = new_pip4
    if (new_pip1 == new_pip3) and (new_pip5 == new_pip6):
        two_pair = new_pip1
        if new_pip5 > new_pip1:
            two_pair = new_pip5
    if (new_pip1 == new_pip3) and (new_pip5 == new_pip7):
        two_pair = new_pip1
        if new_pip5 > new_pip1:
            two_pair = new_pip5
    if (new_pip1 == new_pip3) and (new_pip6 == new_pip7):
        two_pair = new_pip1
        if new_pip6 > new_pip1:
            two_pair = new_pip6
    if (new_pip1 == new_pip3) and (new_pip2 == new_pip4):
        two_pair = new_pip1
        if new_pip2 > new_pip1:
            two_pair = new_pip2
    if (new_pip1 == new_pip3) and (new_pip2 == new_pip5):
        two_pair = new_pip1
        if new_pip2 > new_pip1:
            two_pair = new_pip2
    if (new_pip1 == new_pip3) and (new_pip2 == new_pip6):
        two_pair = new_pip1
        if new_pip2 > new_pip1:
            two_pair = new_pip2
    if (new_pip1 == new_pip3) and (new_pip2 == new_pip7):
        two_pair = new_pip1
        if new_pip2 > new_pip1:
            two_pair = new_pip2
    if (new_pip1 == new_pip4) and (new_pip2 == new_pip3):
        two_pair = new_pip1
        if new_pip2 > new_pip1:
            two_pair = new_pip2
    if (new_pip1 == new_pip4) and (new_pip2 == new_pip5):
        two_pair = new_pip1
        if new_pip2 > new_pip1:
            two_pair = new_pip2
    if (new_pip1 == new_pip4) and (new_pip2 == new_pip6):
        two_pair = new_pip1
        if new_pip2 > new_pip1:
            two_pair = new_pip2
    if (new_pip1 == new_pip4) and (new_pip2 == new_pip7):
        two_pair = new_pip1
        if new_pip2 > new_pip1:
            two_pair = new_pip2
    if (new_pip1 == new_pip4) and (new_pip3 == new_pip5):
        two_pair = new_pip1
        if new_pip3 > new_pip1:
            two_pair = new_pip3
    if (new_pip1 == new_pip4) and (new_pip3 == new_pip6):
        two_pair = new_pip1
        if new_pip3 > new_pip1:
            two_pair = new_pip3
    if (new_pip1 == new_pip4) and (new_pip3 == new_pip7):
        two_pair = new_pip1
        if new_pip3 > new_pip1:
            two_pair = new_pip3
    if (new_pip1 == new_pip4) and (new_pip5 == new_pip6):
        two_pair = new_pip1
        if new_pip5 > new_pip1:
            two_pair = new_pip5
    if (new_pip1 == new_pip4) and (new_pip5 == new_pip7):
        two_pair = new_pip1
        if new_pip5 > new_pip1:
            two_pair = new_pip5
    if (new_pip1 == new_pip4) and (new_pip6 == new_pip7):
        two_pair = new_pip1
        if new_pip6 > new_pip1:
            two_pair = new_pip6
    if (new_pip1 == new_pip5) and (new_pip2 == new_pip3):
        two_pair = new_pip1
        if new_pip2 > new_pip1:
            two_pair = new_pip2
    if (new_pip1 == new_pip5) and (new_pip2 == new_pip4):
        two_pair = new_pip1
        if new_pip2 > new_pip1:
            two_pair = new_pip2
    if (new_pip1 == new_pip5) and (new_pip2 == new_pip6):
        two_pair = new_pip1
        if new_pip2 > new_pip1:
            two_pair = new_pip2
    if (new_pip1 == new_pip5) and (new_pip2 == new_pip7):
        two_pair = new_pip1
        if new_pip2 > new_pip1:
            two_pair = new_pip2
    if (new_pip1 == new_pip5) and (new_pip3 == new_pip4):
        two_pair = new_pip1
        if new_pip3 > new_pip1:
            two_pair = new_pip3
    if (new_pip1 == new_pip5) and (new_pip3 == new_pip6):
        two_pair = new_pip1
        if new_pip3 > new_pip1:
            two_pair = new_pip3
    if (new_pip1 == new_pip5) and (new_pip3 == new_pip7):
        two_pair = new_pip1
        if new_pip3 > new_pip1:
            two_pair = new_pip3
    if (new_pip1 == new_pip5) and (new_pip4 == new_pip6):
        two_pair = new_pip1
        if new_pip4 > new_pip1:
            two_pair = new_pip4
    if (new_pip1 == new_pip5) and (new_pip4 == new_pip7):
        two_pair = new_pip1
        if new_pip4 > new_pip1:
            two_pair = new_pip4
    if (new_pip1 == new_pip5) and (new_pip6 == new_pip7):
        two_pair = new_pip1
        if new_pip6 > new_pip1:
            two_pair = new_pip6
    if (new_pip1 == new_pip6) and (new_pip2 == new_pip3):
        two_pair = new_pip1
        if new_pip2 > new_pip1:
            two_pair = new_pip2
    if (new_pip1 == new_pip6) and (new_pip2 == new_pip4):
        two_pair = new_pip1
        if new_pip2 > new_pip1:
            two_pair = new_pip2
    if (new_pip1 == new_pip6) and (new_pip2 == new_pip5):
        two_pair = new_pip1
        if new_pip2 > new_pip1:
            two_pair = new_pip2
    if (new_pip1 == new_pip6) and (new_pip2 == new_pip7):
        two_pair = new_pip1
        if new_pip2 > new_pip1:
            two_pair = new_pip2
    if (new_pip1 == new_pip6) and (new_pip3 == new_pip4):
        two_pair = new_pip1
        if new_pip3 > new_pip1:
            two_pair = new_pip3
    if (new_pip1 == new_pip6) and (new_pip3 == new_pip5):
        two_pair = new_pip1
        if new_pip3 > new_pip1:
            two_pair = new_pip3
    if (new_pip1 == new_pip6) and (new_pip3 == new_pip7):
        two_pair = new_pip1
        if new_pip3 > new_pip1:
            two_pair = new_pip3
    if (new_pip1 == new_pip6) and (new_pip4 == new_pip5):
        two_pair = new_pip1
        if new_pip4 > new_pip1:
            two_pair = new_pip4
    if (new_pip1 == new_pip6) and (new_pip4 == new_pip7):
        two_pair = new_pip1
        if new_pip4 > new_pip1:
            two_pair = new_pip4
    if (new_pip1 == new_pip6) and (new_pip5 == new_pip7):
        two_pair = new_pip1
        if new_pip5 > new_pip1:
            two_pair = new_pip5
    if (new_pip1 == new_pip7) and (new_pip2 == new_pip3):
        two_pair = new_pip1
        if new_pip2 > new_pip1:
            two_pair = new_pip2
    if (new_pip1 == new_pip7) and (new_pip2 == new_pip4):
        two_pair = new_pip1
        if new_pip2 > new_pip1:
            two_pair = new_pip2
    if (new_pip1 == new_pip7) and (new_pip2 == new_pip5):
        two_pair = new_pip1
        if new_pip2 > new_pip1:
            two_pair = new_pip2
    if (new_pip1 == new_pip7) and (new_pip2 == new_pip6):
        two_pair = new_pip1
        if new_pip2 > new_pip1:
            two_pair = new_pip2
    if (new_pip1 == new_pip7) and (new_pip3 == new_pip4):
        two_pair = new_pip1
        if new_pip3 > new_pip1:
            two_pair = new_pip3
    if (new_pip1 == new_pip7) and (new_pip3 == new_pip5):
        two_pair = new_pip1
        if new_pip3 > new_pip1:
            two_pair = new_pip3
    if (new_pip1 == new_pip7) and (new_pip3 == new_pip6):
        two_pair = new_pip1
        if new_pip3 > new_pip1:
            two_pair = new_pip3
    if (new_pip1 == new_pip7) and (new_pip4 == new_pip5):
        two_pair = new_pip1
        if new_pip4 > new_pip1:
            two_pair = new_pip4
    if (new_pip1 == new_pip7) and (new_pip4 == new_pip6):
        two_pair = new_pip1
        if new_pip4 > new_pip1:
            two_pair = new_pip4
    if (new_pip1 == new_pip7) and (new_pip5 == new_pip6):
        two_pair = new_pip1
        if new_pip5 > new_pip1:
            two_pair = new_pip5
    if (new_pip2 == new_pip3) and (new_pip4 == new_pip5):
        two_pair = new_pip2
        if new_pip4 > new_pip2:
            two_pair = new_pip4
    if (new_pip2 == new_pip3) and (new_pip4 == new_pip6):
        two_pair = new_pip2
        if new_pip4 > new_pip2:
            two_pair = new_pip4
    if (new_pip2 == new_pip3) and (new_pip4 == new_pip7):
        two_pair = new_pip2
        if new_pip4 > new_pip2:
            two_pair = new_pip4
    if (new_pip2 == new_pip3) and (new_pip5 == new_pip6):
        two_pair = new_pip2
        if new_pip5 > new_pip2:
            two_pair = new_pip5
    if (new_pip2 == new_pip3) and (new_pip5 == new_pip7):
        two_pair = new_pip2
        if new_pip5 > new_pip2:
            two_pair = new_pip5
    if (new_pip2 == new_pip3) and (new_pip6 == new_pip7):
        two_pair = new_pip2
        if new_pip6 > new_pip2:
            two_pair = new_pip6
    if (new_pip2 == new_pip4) and (new_pip3 == new_pip5):
        two_pair = new_pip2
        if new_pip3 > new_pip2:
            two_pair = new_pip3
    if (new_pip2 == new_pip4) and (new_pip3 == new_pip6):
        two_pair = new_pip2
        if new_pip3 > new_pip2:
            two_pair = new_pip3
    if (new_pip2 == new_pip4) and (new_pip3 == new_pip7):
        two_pair = new_pip2
        if new_pip3 > new_pip2:
            two_pair = new_pip3
    if (new_pip2 == new_pip4) and (new_pip5 == new_pip6):
        two_pair = new_pip2
        if new_pip5 > new_pip2:
            two_pair = new_pip5
    if (new_pip2 == new_pip4) and (new_pip5 == new_pip7):
        two_pair = new_pip2
        if new_pip5 > new_pip2:
            two_pair = new_pip5
    if (new_pip2 == new_pip4) and (new_pip6 == new_pip7):
        two_pair = new_pip2
        if new_pip6 > new_pip2:
            two_pair = new_pip6
    if (new_pip2 == new_pip5) and (new_pip3 == new_pip4):
        two_pair = new_pip2
        if new_pip3 > new_pip2:
            two_pair = new_pip3
    if (new_pip2 == new_pip5) and (new_pip3 == new_pip6):
        two_pair = new_pip2
        if new_pip3 > new_pip2:
            two_pair = new_pip3
    if (new_pip2 == new_pip5) and (new_pip3 == new_pip7):
        two_pair = new_pip2
        if new_pip3 > new_pip2:
            two_pair = new_pip3
    if (new_pip2 == new_pip5) and (new_pip4 == new_pip6):
        two_pair = new_pip2
        if new_pip4 > new_pip2:
            two_pair = new_pip4
    if (new_pip2 == new_pip5) and (new_pip4 == new_pip7):
        two_pair = new_pip2
        if new_pip4 > new_pip2:
            two_pair = new_pip4
    if (new_pip2 == new_pip5) and (new_pip6 == new_pip7):
        two_pair = new_pip2
        if new_pip6 > new_pip2:
            two_pair = new_pip6
    if (new_pip2 == new_pip6) and (new_pip3 == new_pip4):
        two_pair = new_pip2
        if new_pip3 > new_pip2:
            two_pair = new_pip3
    if (new_pip2 == new_pip6) and (new_pip3 == new_pip5):
        two_pair = new_pip2
        if new_pip3 > new_pip2:
            two_pair = new_pip3
    if (new_pip2 == new_pip6) and (new_pip3 == new_pip7):
        two_pair = new_pip2
        if new_pip3 > new_pip2:
            two_pair = new_pip3
    if (new_pip2 == new_pip6) and (new_pip4 == new_pip5):
        two_pair = new_pip2
        if new_pip4 > new_pip2:
            two_pair = new_pip4
    if (new_pip2 == new_pip6) and (new_pip4 == new_pip7):
        two_pair = new_pip2
        if new_pip4 > new_pip2:
            two_pair = new_pip4
    if (new_pip2 == new_pip6) and (new_pip5 == new_pip7):
        two_pair = new_pip2
        if new_pip5 > new_pip2:
            two_pair = new_pip5
    if (new_pip2 == new_pip7) and (new_pip3 == new_pip4):
        two_pair = new_pip2
        if new_pip3 > new_pip2:
            two_pair = new_pip3
    if (new_pip2 == new_pip7) and (new_pip3 == new_pip5):
        two_pair = new_pip2
        if new_pip3 > new_pip2:
            two_pair = new_pip3
    if (new_pip2 == new_pip7) and (new_pip3 == new_pip6):
        two_pair = new_pip2
        if new_pip3 > new_pip2:
            two_pair = new_pip3
    if (new_pip2 == new_pip7) and (new_pip4 == new_pip5):
        two_pair = new_pip2
        if new_pip4 > new_pip2:
            two_pair = new_pip4
    if (new_pip2 == new_pip7) and (new_pip4 == new_pip6):
        two_pair = new_pip2
        if new_pip4 > new_pip2:
            two_pair = new_pip4
    if (new_pip2 == new_pip7) and (new_pip5 == new_pip6):
        two_pair = new_pip2
        if new_pip5 > new_pip2:
            two_pair = new_pip5
    if (new_pip3 == new_pip4) and (new_pip5 == new_pip6):
        two_pair = new_pip3
        if new_pip5 > new_pip3:
            two_pair = new_pip5
    if (new_pip3 == new_pip4) and (new_pip5 == new_pip7):
        two_pair = new_pip3
        if new_pip5 > new_pip3:
            two_pair = new_pip5
    if (new_pip3 == new_pip4) and (new_pip6 == new_pip7):
        two_pair = new_pip3
        if new_pip6 > new_pip3:
            two_pair = new_pip6
    if (new_pip3 == new_pip5) and (new_pip4 == new_pip6):
        two_pair = new_pip3
        if new_pip4 > new_pip3:
            two_pair = new_pip4
    if (new_pip3 == new_pip5) and (new_pip4 == new_pip7):
        two_pair = new_pip3
        if new_pip4 > new_pip3:
            two_pair = new_pip4
    if (new_pip3 == new_pip5) and (new_pip6 == new_pip7):
        two_pair = new_pip3
        if new_pip6 > new_pip3:
            two_pair = new_pip6
    if (new_pip3 == new_pip6) and (new_pip4 == new_pip5):
        two_pair = new_pip3
        if new_pip4 > new_pip3:
            two_pair = new_pip4
    if (new_pip3 == new_pip6) and (new_pip4 == new_pip7):
        two_pair = new_pip3
        if new_pip4 > new_pip3:
            two_pair = new_pip4
    if (new_pip3 == new_pip6) and (new_pip5 == new_pip7):
        two_pair = new_pip3
        if new_pip5 > new_pip3:
            two_pair = new_pip5
    if (new_pip3 == new_pip7) and (new_pip4 == new_pip5):
        two_pair = new_pip3
        if new_pip4 > new_pip3:
            two_pair = new_pip4
    if (new_pip3 == new_pip7) and (new_pip4 == new_pip6):
        two_pair = new_pip3
        if new_pip4 > new_pip3:
            two_pair = new_pip4
    if (new_pip3 == new_pip7) and (new_pip5 == new_pip6):
        two_pair = new_pip3
        if new_pip4 > new_pip3:
            two_pair = new_pip4
    if (new_pip4 == new_pip5) and (new_pip6 == new_pip7):
        two_pair = new_pip4
        if new_pip6 > new_pip3:
            two_pair = new_pip6
    if (new_pip4 == new_pip6) and (new_pip5 == new_pip7):
        two_pair = new_pip4
        if new_pip5 > new_pip3:
            two_pair = new_pip5
    if (new_pip4 == new_pip7) and (new_pip5 == new_pip6):
        two_pair = new_pip4
        if new_pip5 > new_pip3:
            two_pair = new_pip5
    return two_pair


def two_pair_kickers(pip1, pip2, pip3, pip4, pip5, pip6, pip7):
    new_pip1 = face_cards(pip1)
    new_pip2 = face_cards(pip2)
    new_pip3 = face_cards(pip3)
    new_pip4 = face_cards(pip4)
    new_pip5 = face_cards(pip5)
    new_pip6 = face_cards(pip6)
    new_pip7 = face_cards(pip7)
    two_pair_kicker = 0
    if (new_pip1 == new_pip2) and (new_pip3 == new_pip4):
        two_pair_kicker = new_pip1
        if new_pip3 < new_pip1:
            two_pair_kicker = new_pip3
    if (new_pip1 == new_pip2) and (new_pip3 == new_pip5):
        two_pair_kicker = new_pip1
        if new_pip3 < new_pip1:
            two_pair_kicker = new_pip3
    if (new_pip1 == new_pip2) and (new_pip3 == new_pip6):
        two_pair_kicker = new_pip1
        if new_pip3 < new_pip1:
            two_pair_kicker = new_pip3
    if (new_pip1 == new_pip2) and (new_pip3 == new_pip7):
        two_pair_kicker = new_pip1
        if new_pip3 < new_pip1:
            two_pair_kicker = new_pip3
    if (new_pip1 == new_pip2) and (new_pip4 == new_pip5):
        two_pair_kicker = new_pip1
        if new_pip4 < new_pip1:
            two_pair_kicker = new_pip4
    if (new_pip1 == new_pip2) and (new_pip4 == new_pip6):
        two_pair_kicker = new_pip1
        if new_pip4 < new_pip1:
            two_pair_kicker = new_pip4
    if (new_pip1 == new_pip2) and (new_pip4 == new_pip7):
        two_pair_kicker = new_pip1
        if new_pip4 < new_pip1:
            two_pair_kicker = new_pip4
    if (new_pip1 == new_pip2) and (new_pip5 == new_pip6):
        two_pair_kicker = new_pip1
        if new_pip5 < new_pip1:
            two_pair_kicker = new_pip5
    if (new_pip1 == new_pip2) and (new_pip5 == new_pip7):
        two_pair_kicker = new_pip1
        if new_pip5 < new_pip1:
            two_pair_kicker = new_pip5
    if (new_pip1 == new_pip2) and (new_pip6 == new_pip7):
        two_pair_kicker = new_pip1
        if new_pip6 < new_pip1:
            two_pair_kicker = new_pip6
    if (new_pip1 == new_pip3) and (new_pip4 == new_pip5):
        two_pair_kicker = new_pip1
        if new_pip4 < new_pip1:
            two_pair_kicker = new_pip4
    if (new_pip1 == new_pip3) and (new_pip4 == new_pip6):
        two_pair_kicker = new_pip1
        if new_pip4 < new_pip1:
            two_pair_kicker = new_pip4
    if (new_pip1 == new_pip3) and (new_pip4 == new_pip7):
        two_pair_kicker = new_pip1
        if new_pip4 < new_pip1:
            two_pair_kicker = new_pip4
    if (new_pip1 == new_pip3) and (new_pip5 == new_pip6):
        two_pair_kicker = new_pip1
        if new_pip5 < new_pip1:
            two_pair_kicker = new_pip5
    if (new_pip1 == new_pip3) and (new_pip5 == new_pip7):
        two_pair_kicker = new_pip1
        if new_pip5 < new_pip1:
            two_pair_kicker = new_pip5
    if (new_pip1 == new_pip3) and (new_pip6 == new_pip7):
        two_pair_kicker = new_pip1
        if new_pip6 < new_pip1:
            two_pair_kicker = new_pip6
    if (new_pip1 == new_pip3) and (new_pip2 == new_pip4):
        two_pair_kicker = new_pip1
        if new_pip2 < new_pip1:
            two_pair_kicker = new_pip2
    if (new_pip1 == new_pip3) and (new_pip2 == new_pip5):
        two_pair_kicker = new_pip1
        if new_pip2 < new_pip1:
            two_pair_kicker = new_pip2
    if (new_pip1 == new_pip3) and (new_pip2 == new_pip6):
        two_pair_kicker = new_pip1
        if new_pip2 < new_pip1:
            two_pair_kicker = new_pip2
    if (new_pip1 == new_pip3) and (new_pip2 == new_pip7):
        two_pair_kicker = new_pip1
        if new_pip2 < new_pip1:
            two_pair_kicker = new_pip2
    if (new_pip1 == new_pip4) and (new_pip2 == new_pip3):
        two_pair_kicker = new_pip1
        if new_pip2 < new_pip1:
            two_pair_kicker = new_pip2
    if (new_pip1 == new_pip4) and (new_pip2 == new_pip5):
        two_pair_kicker = new_pip1
        if new_pip2 < new_pip1:
            two_pair_kicker = new_pip2
    if (new_pip1 == new_pip4) and (new_pip2 == new_pip6):
        two_pair_kicker = new_pip1
        if new_pip2 < new_pip1:
            two_pair_kicker = new_pip2
    if (new_pip1 == new_pip4) and (new_pip2 == new_pip7):
        two_pair_kicker = new_pip1
        if new_pip2 < new_pip1:
            two_pair_kicker = new_pip2
    if (new_pip1 == new_pip4) and (new_pip3 == new_pip5):
        two_pair_kicker = new_pip1
        if new_pip3 < new_pip1:
            two_pair_kicker = new_pip3
    if (new_pip1 == new_pip4) and (new_pip3 == new_pip6):
        two_pair_kicker = new_pip1
        if new_pip3 < new_pip1:
            two_pair_kicker = new_pip3
    if (new_pip1 == new_pip4) and (new_pip3 == new_pip7):
        two_pair_kicker = new_pip1
        if new_pip3 < new_pip1:
            two_pair_kicker = new_pip3
    if (new_pip1 == new_pip4) and (new_pip5 == new_pip6):
        two_pair_kicker = new_pip1
        if new_pip5 < new_pip1:
            two_pair_kicker = new_pip5
    if (new_pip1 == new_pip4) and (new_pip5 == new_pip7):
        two_pair_kicker = new_pip1
        if new_pip5 < new_pip1:
            two_pair_kicker = new_pip5
    if (new_pip1 == new_pip4) and (new_pip6 == new_pip7):
        two_pair_kicker = new_pip1
        if new_pip6 < new_pip1:
            two_pair_kicker = new_pip6
    if (new_pip1 == new_pip5) and (new_pip2 == new_pip3):
        two_pair_kicker = new_pip1
        if new_pip2 < new_pip1:
            two_pair_kicker = new_pip2
    if (new_pip1 == new_pip5) and (new_pip2 == new_pip4):
        two_pair_kicker = new_pip1
        if new_pip2 < new_pip1:
            two_pair_kicker = new_pip2
    if (new_pip1 == new_pip5) and (new_pip2 == new_pip6):
        two_pair_kicker = new_pip1
        if new_pip2 < new_pip1:
            two_pair_kicker = new_pip2
    if (new_pip1 == new_pip5) and (new_pip2 == new_pip7):
        two_pair_kicker = new_pip1
        if new_pip2 < new_pip1:
            two_pair_kicker = new_pip2
    if (new_pip1 == new_pip5) and (new_pip3 == new_pip4):
        two_pair_kicker = new_pip1
        if new_pip3 < new_pip1:
            two_pair_kicker = new_pip3
    if (new_pip1 == new_pip5) and (new_pip3 == new_pip6):
        two_pair_kicker = new_pip1
        if new_pip3 < new_pip1:
            two_pair_kicker = new_pip3
    if (new_pip1 == new_pip5) and (new_pip3 == new_pip7):
        two_pair_kicker = new_pip1
        if new_pip3 < new_pip1:
            two_pair_kicker = new_pip3
    if (new_pip1 == new_pip5) and (new_pip4 == new_pip6):
        two_pair_kicker = new_pip1
        if new_pip4 < new_pip1:
            two_pair_kicker = new_pip4
    if (new_pip1 == new_pip5) and (new_pip4 == new_pip7):
        two_pair_kicker = new_pip1
        if new_pip4 < new_pip1:
            two_pair_kicker = new_pip4
    if (new_pip1 == new_pip5) and (new_pip6 == new_pip7):
        two_pair_kicker = new_pip1
        if new_pip6 < new_pip1:
            two_pair_kicker = new_pip6
    if (new_pip1 == new_pip6) and (new_pip2 == new_pip3):
        two_pair_kicker = new_pip1
        if new_pip2 < new_pip1:
            two_pair_kicker = new_pip2
    if (new_pip1 == new_pip6) and (new_pip2 == new_pip4):
        two_pair_kicker = new_pip1
        if new_pip2 < new_pip1:
            two_pair_kicker = new_pip2
    if (new_pip1 == new_pip6) and (new_pip2 == new_pip5):
        two_pair_kicker = new_pip1
        if new_pip2 < new_pip1:
            two_pair_kicker = new_pip2
    if (new_pip1 == new_pip6) and (new_pip2 == new_pip7):
        two_pair_kicker = new_pip1
        if new_pip2 < new_pip1:
            two_pair_kicker = new_pip2
    if (new_pip1 == new_pip6) and (new_pip3 == new_pip4):
        two_pair_kicker = new_pip1
        if new_pip3 < new_pip1:
            two_pair_kicker = new_pip3
    if (new_pip1 == new_pip6) and (new_pip3 == new_pip5):
        two_pair_kicker = new_pip1
        if new_pip3 < new_pip1:
            two_pair_kicker = new_pip3
    if (new_pip1 == new_pip6) and (new_pip3 == new_pip7):
        two_pair_kicker = new_pip1
        if new_pip3 < new_pip1:
            two_pair_kicker = new_pip3
    if (new_pip1 == new_pip6) and (new_pip4 == new_pip5):
        two_pair_kicker = new_pip1
        if new_pip4 < new_pip1:
            two_pair_kicker = new_pip4
    if (new_pip1 == new_pip6) and (new_pip4 == new_pip7):
        two_pair_kicker = new_pip1
        if new_pip4 < new_pip1:
            two_pair_kicker = new_pip4
    if (new_pip1 == new_pip6) and (new_pip5 == new_pip7):
        two_pair_kicker = new_pip1
        if new_pip5 < new_pip1:
            two_pair_kicker = new_pip5
    if (new_pip1 == new_pip7) and (new_pip2 == new_pip3):
        two_pair_kicker = new_pip1
        if new_pip2 < new_pip1:
            two_pair_kicker = new_pip2
    if (new_pip1 == new_pip7) and (new_pip2 == new_pip4):
        two_pair_kicker = new_pip1
        if new_pip2 < new_pip1:
            two_pair_kicker = new_pip2
    if (new_pip1 == new_pip7) and (new_pip2 == new_pip5):
        two_pair_kicker = new_pip1
        if new_pip2 < new_pip1:
            two_pair_kicker = new_pip2
    if (new_pip1 == new_pip7) and (new_pip2 == new_pip6):
        two_pair_kicker = new_pip1
        if new_pip2 < new_pip1:
            two_pair_kicker = new_pip2
    if (new_pip1 == new_pip7) and (new_pip3 == new_pip4):
        two_pair_kicker = new_pip1
        if new_pip3 < new_pip1:
            two_pair_kicker = new_pip3
    if (new_pip1 == new_pip7) and (new_pip3 == new_pip5):
        two_pair_kicker = new_pip1
        if new_pip3 < new_pip1:
            two_pair_kicker = new_pip3
    if (new_pip1 == new_pip7) and (new_pip3 == new_pip6):
        two_pair_kicker = new_pip1
        if new_pip3 < new_pip1:
            two_pair_kicker = new_pip3
    if (new_pip1 == new_pip7) and (new_pip4 == new_pip5):
        two_pair_kicker = new_pip1
        if new_pip4 < new_pip1:
            two_pair_kicker = new_pip4
    if (new_pip1 == new_pip7) and (new_pip4 == new_pip6):
        two_pair_kicker = new_pip1
        if new_pip4 < new_pip1:
            two_pair_kicker = new_pip4
    if (new_pip1 == new_pip7) and (new_pip5 == new_pip6):
        two_pair_kicker = new_pip1
        if new_pip5 < new_pip1:
            two_pair_kicker = new_pip5
    if (new_pip2 == new_pip3) and (new_pip4 == new_pip5):
        two_pair_kicker = new_pip2
        if new_pip4 < new_pip2:
            two_pair_kicker = new_pip4
    if (new_pip2 == new_pip3) and (new_pip4 == new_pip6):
        two_pair_kicker = new_pip2
        if new_pip4 < new_pip2:
            two_pair_kicker = new_pip4
    if (new_pip2 == new_pip3) and (new_pip4 == new_pip7):
        two_pair_kicker = new_pip2
        if new_pip4 < new_pip2:
            two_pair_kicker = new_pip4
    if (new_pip2 == new_pip3) and (new_pip5 == new_pip6):
        two_pair_kicker = new_pip2
        if new_pip5 < new_pip2:
            two_pair_kicker = new_pip5
    if (new_pip2 == new_pip3) and (new_pip5 == new_pip7):
        two_pair_kicker = new_pip2
        if new_pip5 < new_pip2:
            two_pair_kicker = new_pip5
    if (new_pip2 == new_pip3) and (new_pip6 == new_pip7):
        two_pair_kicker = new_pip2
        if new_pip6 < new_pip2:
            two_pair_kicker = new_pip6
    if (new_pip2 == new_pip4) and (new_pip3 == new_pip5):
        two_pair_kicker = new_pip2
        if new_pip3 < new_pip2:
            two_pair_kicker = new_pip3
    if (new_pip2 == new_pip4) and (new_pip3 == new_pip6):
        two_pair_kicker = new_pip2
        if new_pip3 < new_pip2:
            two_pair_kicker = new_pip3
    if (new_pip2 == new_pip4) and (new_pip3 == new_pip7):
        two_pair_kicker = new_pip2
        if new_pip3 < new_pip2:
            two_pair_kicker = new_pip3
    if (new_pip2 == new_pip4) and (new_pip5 == new_pip6):
        two_pair_kicker = new_pip2
        if new_pip5 < new_pip2:
            two_pair_kicker = new_pip5
    if (new_pip2 == new_pip4) and (new_pip5 == new_pip7):
        two_pair_kicker = new_pip2
        if new_pip5 < new_pip2:
            two_pair_kicker = new_pip5
    if (new_pip2 == new_pip4) and (new_pip6 == new_pip7):
        two_pair_kicker = new_pip2
        if new_pip6 < new_pip2:
            two_pair_kicker = new_pip6
    if (new_pip2 == new_pip5) and (new_pip3 == new_pip4):
        two_pair_kicker = new_pip2
        if new_pip3 < new_pip2:
            two_pair_kicker = new_pip3
    if (new_pip2 == new_pip5) and (new_pip3 == new_pip6):
        two_pair_kicker = new_pip2
        if new_pip3 < new_pip2:
            two_pair_kicker = new_pip3
    if (new_pip2 == new_pip5) and (new_pip3 == new_pip7):
        two_pair_kicker = new_pip2
        if new_pip3 < new_pip2:
            two_pair_kicker = new_pip3
    if (new_pip2 == new_pip5) and (new_pip4 == new_pip6):
        two_pair_kicker = new_pip2
        if new_pip4 < new_pip2:
            two_pair_kicker = new_pip4
    if (new_pip2 == new_pip5) and (new_pip4 == new_pip7):
        two_pair_kicker = new_pip2
        if new_pip4 < new_pip2:
            two_pair_kicker = new_pip4
    if (new_pip2 == new_pip5) and (new_pip6 == new_pip7):
        two_pair_kicker = new_pip2
        if new_pip6 < new_pip2:
            two_pair_kicker = new_pip6
    if (new_pip2 == new_pip6) and (new_pip3 == new_pip4):
        two_pair_kicker = new_pip2
        if new_pip3 < new_pip2:
            two_pair_kicker = new_pip3
    if (new_pip2 == new_pip6) and (new_pip3 == new_pip5):
        two_pair_kicker = new_pip2
        if new_pip3 < new_pip2:
            two_pair_kicker = new_pip3
    if (new_pip2 == new_pip6) and (new_pip3 == new_pip7):
        two_pair_kicker = new_pip2
        if new_pip3 < new_pip2:
            two_pair_kicker = new_pip3
    if (new_pip2 == new_pip6) and (new_pip4 == new_pip5):
        two_pair_kicker = new_pip2
        if new_pip4 < new_pip2:
            two_pair_kicker = new_pip4
    if (new_pip2 == new_pip6) and (new_pip4 == new_pip7):
        two_pair_kicker = new_pip2
        if new_pip4 < new_pip2:
            two_pair_kicker = new_pip4
    if (new_pip2 == new_pip6) and (new_pip5 == new_pip7):
        two_pair_kicker = new_pip2
        if new_pip5 < new_pip2:
            two_pair_kicker = new_pip5
    if (new_pip2 == new_pip7) and (new_pip3 == new_pip4):
        two_pair_kicker = new_pip2
        if new_pip3 < new_pip2:
            two_pair_kicker = new_pip3
    if (new_pip2 == new_pip7) and (new_pip3 == new_pip5):
        two_pair_kicker = new_pip2
        if new_pip3 < new_pip2:
            two_pair_kicker = new_pip3
    if (new_pip2 == new_pip7) and (new_pip3 == new_pip6):
        two_pair_kicker = new_pip2
        if new_pip3 < new_pip2:
            two_pair_kicker = new_pip3
    if (new_pip2 == new_pip7) and (new_pip4 == new_pip5):
        two_pair_kicker = new_pip2
        if new_pip4 < new_pip2:
            two_pair_kicker = new_pip4
    if (new_pip2 == new_pip7) and (new_pip4 == new_pip6):
        two_pair_kicker = new_pip2
        if new_pip4 < new_pip2:
            two_pair_kicker = new_pip4
    if (new_pip2 == new_pip7) and (new_pip5 == new_pip6):
        two_pair_kicker = new_pip2
        if new_pip5 < new_pip2:
            two_pair_kicker = new_pip5
    if (new_pip3 == new_pip4) and (new_pip5 == new_pip6):
        two_pair_kicker = new_pip3
        if new_pip5 < new_pip3:
            two_pair_kicker = new_pip5
    if (new_pip3 == new_pip4) and (new_pip5 == new_pip7):
        two_pair_kicker = new_pip3
        if new_pip5 < new_pip3:
            two_pair_kicker = new_pip5
    if (new_pip3 == new_pip4) and (new_pip6 == new_pip7):
        two_pair_kicker = new_pip3
        if new_pip6 < new_pip3:
            two_pair_kicker = new_pip6
    if (new_pip3 == new_pip5) and (new_pip4 == new_pip6):
        two_pair_kicker = new_pip3
        if new_pip4 < new_pip3:
            two_pair_kicker = new_pip4
    if (new_pip3 == new_pip5) and (new_pip4 == new_pip7):
        two_pair_kicker = new_pip3
        if new_pip4 < new_pip3:
            two_pair_kicker = new_pip4
    if (new_pip3 == new_pip5) and (new_pip6 == new_pip7):
        two_pair_kicker = new_pip3
        if new_pip6 < new_pip3:
            two_pair_kicker = new_pip6
    if (new_pip3 == new_pip6) and (new_pip4 == new_pip5):
        two_pair_kicker = new_pip3
        if new_pip4 < new_pip3:
            two_pair_kicker = new_pip4
    if (new_pip3 == new_pip6) and (new_pip4 == new_pip7):
        two_pair_kicker = new_pip3
        if new_pip4 < new_pip3:
            two_pair_kicker = new_pip4
    if (new_pip3 == new_pip6) and (new_pip5 == new_pip7):
        two_pair_kicker = new_pip3
        if new_pip5 < new_pip3:
            two_pair_kicker = new_pip5
    if (new_pip3 == new_pip7) and (new_pip4 == new_pip5):
        two_pair_kicker = new_pip3
        if new_pip4 < new_pip3:
            two_pair_kicker = new_pip4
    if (new_pip3 == new_pip7) and (new_pip4 == new_pip6):
        two_pair_kicker = new_pip3
        if new_pip4 < new_pip3:
            two_pair_kicker = new_pip4
    if (new_pip3 == new_pip7) and (new_pip5 == new_pip6):
        two_pair_kicker = new_pip3
        if new_pip4 < new_pip3:
            two_pair_kicker = new_pip4
    if (new_pip4 == new_pip5) and (new_pip6 == new_pip7):
        two_pair_kicker = new_pip4
        if new_pip6 < new_pip3:
            two_pair_kicker = new_pip6
    if (new_pip4 == new_pip6) and (new_pip5 == new_pip7):
        two_pair_kicker = new_pip4
        if new_pip5 < new_pip3:
            two_pair_kicker = new_pip5
    if (new_pip4 == new_pip7) and (new_pip5 == new_pip6):
        two_pair_kicker = new_pip4
        if new_pip5 < new_pip3:
            two_pair_kicker = new_pip5
    return two_pair_kicker


def trips(pip1, pip2, pip3, pip4, pip5, pip6, pip7):
    new_pip1 = face_cards(pip1)
    new_pip2 = face_cards(pip2)
    new_pip3 = face_cards(pip3)
    new_pip4 = face_cards(pip4)
    new_pip5 = face_cards(pip5)
    new_pip6 = face_cards(pip6)
    new_pip7 = face_cards(pip7)
    trip = 0
    if new_pip1 == new_pip2 == new_pip3:
        trip = new_pip1
    if new_pip1 == new_pip2 == new_pip4:
        trip = new_pip1
    if new_pip1 == new_pip2 == new_pip5:
        trip = new_pip1
    if new_pip1 == new_pip2 == new_pip6:
        trip = new_pip1
    if new_pip1 == new_pip2 == new_pip7:
        trip = new_pip1
    if new_pip1 == new_pip3 == new_pip4:
        trip = new_pip1
    if new_pip1 == new_pip3 == new_pip5:
        trip = new_pip1
    if new_pip1 == new_pip3 == new_pip6:
        trip = new_pip1
    if new_pip1 == new_pip3 == new_pip7:
        trip = new_pip1
    if new_pip1 == new_pip4 == new_pip5:
        trip = new_pip1
    if new_pip1 == new_pip4 == new_pip6:
        trip = new_pip1
    if new_pip1 == new_pip4 == new_pip7:
        trip = new_pip1
    if new_pip1 == new_pip5 == new_pip6:
        trip = new_pip1
    if new_pip1 == new_pip5 == new_pip7:
        trip = new_pip1
    if new_pip1 == new_pip6 == new_pip7:
        trip = new_pip1
    if new_pip2 == new_pip3 == new_pip4:
        trip = new_pip2
    if new_pip2 == new_pip3 == new_pip5:
        trip = new_pip2
    if new_pip2 == new_pip3 == new_pip6:
        trip = new_pip2
    if new_pip2 == new_pip3 == new_pip7:
        trip = new_pip2
    if new_pip2 == new_pip4 == new_pip5:
        trip = new_pip2
    if new_pip2 == new_pip4 == new_pip6:
        trip = new_pip2
    if new_pip2 == new_pip4 == new_pip7:
        trip = new_pip2
    if new_pip2 == new_pip5 == new_pip6:
        trip = new_pip2
    if new_pip2 == new_pip5 == new_pip7:
        trip = new_pip2
    if new_pip2 == new_pip6 == new_pip7:
        trip = new_pip2
    if new_pip3 == new_pip4 == new_pip5:
        trip = new_pip3
    if new_pip3 == new_pip4 == new_pip6:
        trip = new_pip3
    if new_pip3 == new_pip4 == new_pip7:
        trip = new_pip3
    if new_pip3 == new_pip5 == new_pip6:
        trip = new_pip3
    if new_pip3 == new_pip5 == new_pip7:
        trip = new_pip3
    if new_pip3 == new_pip6 == new_pip7:
        trip = new_pip3
    if new_pip4 == new_pip5 == new_pip6:
        trip = new_pip4
    if new_pip4 == new_pip5 == new_pip7:
        trip = new_pip4
    if new_pip4 == new_pip6 == new_pip7:
        trip = new_pip4
    if new_pip5 == new_pip6 == new_pip7:
        trip = new_pip5
    return trip


def straights(pip1, pip2, pip3, pip4, pip5, pip6, pip7):
    new_pip1 = face_cards(pip1)
    new_pip2 = face_cards(pip2)
    new_pip3 = face_cards(pip3)
    new_pip4 = face_cards(pip4)
    new_pip5 = face_cards(pip5)
    new_pip6 = face_cards(pip6)
    new_pip7 = face_cards(pip7)
    straight = 0
    high_straight = 0
    second_high_straight = 0
    third_high_straight = 0
    fourth_high_straight = 0
    fifth_high_straight = 0
    if new_pip1 - 1 == new_pip2:
        high_straight = new_pip1
        second_high_straight = new_pip2
    if new_pip1 - 1 == new_pip3:
        high_straight = new_pip1
        second_high_straight = new_pip3
    if new_pip1 - 1 == new_pip4:
        high_straight = new_pip1
        second_high_straight = new_pip4
    if new_pip1 - 1 == new_pip5:
        high_straight = new_pip1
        second_high_straight = new_pip5
    if new_pip1 - 1 == new_pip6:
        high_straight = new_pip1
        second_high_straight = new_pip6
    if new_pip1 - 1 == new_pip7:
        high_straight = new_pip1
        second_high_straight = new_pip7
    if new_pip1 + 1 == new_pip2:
        high_straight = new_pip2
        second_high_straight = new_pip1
    if new_pip1 + 1 == new_pip3:
        high_straight = new_pip3
        second_high_straight = new_pip1
    if new_pip1 + 1 == new_pip4:
        high_straight = new_pip4
        second_high_straight = new_pip1
    if new_pip1 + 1 == new_pip5:
        high_straight = new_pip5
        second_high_straight = new_pip1
    if new_pip1 + 1 == new_pip6:
        high_straight = new_pip6
        second_high_straight = new_pip1
    if new_pip1 + 1 == new_pip7:
        high_straight = new_pip7
        second_high_straight = new_pip1
    if high_straight == 0 and new_pip2 - 1 == new_pip3:
        high_straight = new_pip2
        second_high_straight = new_pip3
    if high_straight == 0 and new_pip2 - 1 == new_pip4:
        high_straight = new_pip2
        second_high_straight = new_pip4
    if high_straight == 0 and new_pip2 - 1 == new_pip5:
        high_straight = new_pip2
        second_high_straight = new_pip5
    if high_straight == 0 and new_pip2 - 1 == new_pip6:
        high_straight = new_pip2
        second_high_straight = new_pip6
    if high_straight == 0 and new_pip2 - 1 == new_pip7:
        high_straight = new_pip2
        second_high_straight = new_pip7
    if high_straight == 0 and new_pip2 + 1 == new_pip3:
        high_straight = new_pip3
        second_high_straight = new_pip2
    if high_straight == 0 and new_pip2 + 1 == new_pip4:
        high_straight = new_pip4
        second_high_straight = new_pip2
    if high_straight == 0 and new_pip2 + 1 == new_pip5:
        high_straight = new_pip5
        second_high_straight = new_pip2
    if high_straight == 0 and new_pip2 + 1 == new_pip6:
        high_straight = new_pip6
        second_high_straight = new_pip2
    if high_straight == 0 and new_pip2 + 1 == new_pip7:
        high_straight = new_pip7
        second_high_straight = new_pip2
    if high_straight == 0 and new_pip3 - 1 == new_pip4:
        high_straight = new_pip3
        second_high_straight = new_pip4
    if high_straight == 0 and new_pip3 - 1 == new_pip5:
        high_straight = new_pip3
        second_high_straight = new_pip5
    if high_straight == 0 and new_pip3 - 1 == new_pip6:
        high_straight = new_pip3
        second_high_straight = new_pip6
    if high_straight == 0 and new_pip3 - 1 == new_pip7:
        high_straight = new_pip3
        second_high_straight = new_pip7
    if high_straight == 0 and new_pip3 + 1 == new_pip4:
        high_straight = new_pip4
        second_high_straight = new_pip3
    if high_straight == 0 and new_pip3 + 1 == new_pip5:
        high_straight = new_pip5
        second_high_straight = new_pip3
    if high_straight == 0 and new_pip3 + 1 == new_pip6:
        high_straight = new_pip6
        second_high_straight = new_pip3
    if high_straight == 0 and new_pip3 + 1 == new_pip7:
        high_straight = new_pip7
        second_high_straight = new_pip3
    if second_high_straight - 1 == new_pip2:
        third_high_straight = new_pip2
    if second_high_straight - 1 == new_pip3:
        third_high_straight = new_pip3
    if second_high_straight - 1 == new_pip4:
        third_high_straight = new_pip4
    if second_high_straight - 1 == new_pip5:
        third_high_straight = new_pip5
    if second_high_straight - 1 == new_pip6:
        third_high_straight = new_pip6
    if second_high_straight - 1 == new_pip7:
        third_high_straight = new_pip7
    if third_high_straight - 1 == new_pip2:
        fourth_high_straight = new_pip2
    if third_high_straight - 1 == new_pip3:
        fourth_high_straight = new_pip3
    if third_high_straight - 1 == new_pip4:
        fourth_high_straight = new_pip4
    if third_high_straight - 1 == new_pip5:
        fourth_high_straight = new_pip5
    if third_high_straight - 1 == new_pip6:
        fourth_high_straight = new_pip6
    if third_high_straight - 1 == new_pip7:
        fourth_high_straight = new_pip7
    if fourth_high_straight - 1 == new_pip2:
        fifth_high_straight = new_pip2
    if fourth_high_straight - 1 == new_pip3:
        fifth_high_straight = new_pip3
    if fourth_high_straight - 1 == new_pip4:
        fifth_high_straight = new_pip4
    if fourth_high_straight - 1 == new_pip5:
        fifth_high_straight = new_pip5
    if fourth_high_straight - 1 == new_pip6:
        fifth_high_straight = new_pip6
    if fourth_high_straight - 1 == new_pip7:
        fifth_high_straight = new_pip7
    if high_straight + 1 == new_pip2:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip2
    if high_straight + 1 == new_pip3:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip3
    if high_straight + 1 == new_pip4:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip4
    if high_straight + 1 == new_pip5:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip5
    if high_straight + 1 == new_pip6:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip6
    if high_straight + 1 == new_pip7:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip7
    if high_straight + 1 == new_pip2:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip2
    if high_straight + 1 == new_pip3:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip3
    if high_straight + 1 == new_pip4:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip4
    if high_straight + 1 == new_pip5:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip5
    if high_straight + 1 == new_pip6:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip6
    if high_straight + 1 == new_pip7:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip7
    if high_straight + 1 == new_pip2:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip2
    if high_straight + 1 == new_pip3:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip3
    if high_straight + 1 == new_pip4:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip4
    if high_straight + 1 == new_pip5:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip5
    if high_straight + 1 == new_pip6:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip6
    if high_straight + 1 == new_pip7:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip7
    if high_straight and second_high_straight and third_high_straight and fourth_high_straight \
            and fifth_high_straight > 0:
        straight = high_straight
    if high_straight == 5 and fourth_high_straight == 2 and new_pip2 == 14:
        straight = 5
    if high_straight == 5 and fourth_high_straight == 2 and new_pip3 == 14:
        straight = 5
    if high_straight == 5 and fourth_high_straight == 2 and new_pip4 == 14:
        straight = 5
    if high_straight == 5 and fourth_high_straight == 2 and new_pip5 == 14:
        straight = 5
    if high_straight == 5 and fourth_high_straight == 2 and new_pip6 == 14:
        straight = 5
    if high_straight == 5 and fourth_high_straight == 2 and new_pip7 == 14:
        straight = 5
    if high_straight == 5 and fourth_high_straight == 2 and new_pip1 == 14:
        straight = 5
    return straight


def flushes(suit1, suit2, suit3, suit4, suit5, suit6, suit7):
    rand_var = 0
    flush = 0
# NEED TO FIX
    if suit1 == suit2:
        rand_var += 1
        if suit3 == suit1:
            rand_var += 1
            if suit4 == suit1:
                rand_var += 1
                if suit5 == suit1:
                    rand_var += 1
                if suit6 == suit1:
                    rand_var += 1
                if suit7 == suit1:
                    rand_var += 1
            if suit5 == suit1:
                rand_var += 1
                if suit6 == suit1:
                    rand_var += 1
                if suit7 == suit1:
                    rand_var += 1
            if suit6 == suit1:
                rand_var += 1
                if suit7 == suit1:
                    rand_var += 1
        if suit4 == suit1 and rand_var == 1:
            rand_var += 1
            if suit5 == suit1:
                rand_var += 1
                if suit6 == suit1:
                    rand_var += 1
                if suit7 == suit1:
                    rand_var += 1
            if suit6 == suit1 and rand_var == 2:
                rand_var += 1
                if suit7 == suit1:
                    rand_var += 1
        if suit5 == suit1 and rand_var == 1:
            rand_var += 1
            if suit6 == suit1:
                rand_var += 1
                if suit7 == suit1:
                    rand_var += 1
    if suit3 == suit1 and rand_var == 0:
        rand_var += 1
        if suit4 == suit1:
            rand_var += 1
            if suit5 == suit1:
                rand_var += 1
            if suit6 == suit1:
                rand_var += 1
            if suit7 == suit1:
                rand_var += 1
        if suit5 == suit1 and rand_var == 1:
            rand_var += 1
            if suit6 == suit1:
                rand_var += 1
            if suit7 == suit1:
                rand_var += 1
    if suit4 == suit1 and rand_var == 0:
        rand_var += 1
        if suit5 == suit1:
            rand_var += 1
            if suit6 == suit1:
                rand_var += 1
            if suit7 == suit1:
                rand_var += 1
    if suit2 == suit3 and rand_var == 0:
        rand_var += 1
        if suit4 == suit2:
            rand_var += 1
            if suit5 == suit2:
                rand_var += 1
                if suit6 == suit2:
                    rand_var += 1
                if suit7 == suit2:
                    rand_var += 1
            if suit6 == suit2 and rand_var == 2:
                rand_var += 1
                if suit7 == suit2:
                    rand_var += 1
        if suit5 == suit2 and rand_var == 1:
            rand_var += 1
            if suit6 == suit2:
                rand_var += 1
                if suit7 == suit2:
                    rand_var += 1
    if suit4 == suit2 and rand_var == 0:
        rand_var += 1
        if suit5 == suit2:
            rand_var += 1
            if suit6 == suit2:
                rand_var += 1
            if suit7 == suit2:
                rand_var += 1
    if suit3 == suit4 and rand_var == 0:
        rand_var += 1
        if suit5 == suit3:
            rand_var += 1
            if suit6 == suit3:
                rand_var += 1
            if suit7 == suit3:
                rand_var += 1
    if rand_var >= 4:
        flush += 1
    return flush


def flushes_kicker(suit1, suit2, suit3, suit4, suit5, suit6, suit7):
    rand_var = 0
    flush_kicker = 0
# NEED TO FIX
    if suit1 == suit2:
        rand_var += 1
        if suit3 == suit1:
            rand_var += 1
            if suit4 == suit1:
                rand_var += 1
                if suit5 == suit1:
                    rand_var += 1
                    flush_kicker = suit1
                if suit6 == suit1:
                    rand_var += 1
                    flush_kicker = suit1
                if suit7 == suit1:
                    rand_var += 1
                    flush_kicker = suit1
            if suit5 == suit1:
                rand_var += 1
                if suit6 == suit1:
                    rand_var += 1
                    flush_kicker = suit1
                if suit7 == suit1:
                    rand_var += 1
                    flush_kicker = suit1
            if suit6 == suit1:
                rand_var += 1
                if suit7 == suit1:
                    rand_var += 1
                    flush_kicker = suit1
        if suit4 == suit1 and rand_var == 1:
            rand_var += 1
            if suit5 == suit1:
                rand_var += 1
                if suit6 == suit1:
                    rand_var += 1
                    flush_kicker = suit1
                if suit7 == suit1:
                    rand_var += 1
                    flush_kicker = suit1
            if suit6 == suit1 and rand_var == 2:
                rand_var += 1
                if suit7 == suit1:
                    rand_var += 1
                    flush_kicker = suit1
        if suit5 == suit1 and rand_var == 1:
            rand_var += 1
            if suit6 == suit1:
                rand_var += 1
                if suit7 == suit1:
                    rand_var += 1
                    flush_kicker = suit1
    if suit3 == suit1 and rand_var == 0:
        rand_var += 1
        if suit4 == suit1:
            rand_var += 1
            if suit5 == suit1:
                rand_var += 1
            if suit6 == suit1:
                rand_var += 1
                flush_kicker = suit1
            if suit7 == suit1:
                rand_var += 1
                flush_kicker = suit1
        if suit5 == suit1 and rand_var == 1:
            rand_var += 1
            if suit6 == suit1:
                rand_var += 1
            if suit7 == suit1:
                rand_var += 1
                flush_kicker = suit1
    if suit4 == suit1 and rand_var == 0:
        rand_var += 1
        if suit5 == suit1:
            rand_var += 1
            if suit6 == suit1:
                rand_var += 1
            if suit7 == suit1:
                rand_var += 1
                flush_kicker = suit1
    if suit2 == suit3 and rand_var == 0:
        rand_var += 1
        if suit4 == suit2:
            rand_var += 1
            if suit5 == suit2:
                rand_var += 1
                if suit6 == suit2:
                    rand_var += 1
                    flush_kicker = suit2
                if suit7 == suit2:
                    rand_var += 1
                    flush_kicker = suit2
            if suit6 == suit2 and rand_var == 2:
                rand_var += 1
                if suit7 == suit2:
                    rand_var += 1
                    flush_kicker = suit2
        if suit5 == suit2 and rand_var == 1:
            rand_var += 1
            if suit6 == suit2:
                rand_var += 1
                if suit7 == suit2:
                    rand_var += 1
                    flush_kicker = suit2
    if suit4 == suit2 and rand_var == 0:
        rand_var += 1
        if suit5 == suit2:
            rand_var += 1
            if suit6 == suit2:
                rand_var += 1
            if suit7 == suit2:
                rand_var += 1
                flush_kicker = suit2
    if suit3 == suit4 and rand_var == 0:
        rand_var += 1
        if suit5 == suit3:
            rand_var += 1
            if suit6 == suit3:
                rand_var += 1
            if suit7 == suit3:
                rand_var += 1
                flush_kicker = suit3
    if rand_var >= 4:
        return flush_kicker


def full_houses(pip1, pip2, pip3, pip4, pip5, pip6, pip7):
    new_pip1 = face_cards(pip1)
    new_pip2 = face_cards(pip2)
    new_pip3 = face_cards(pip3)
    new_pip4 = face_cards(pip4)
    new_pip5 = face_cards(pip5)
    new_pip6 = face_cards(pip6)
    new_pip7 = face_cards(pip7)
    full_house = 0
    pair = 0
    trip = 0
    if new_pip1 == new_pip2 == new_pip3:
        trip = new_pip1
        if new_pip4 == new_pip5:
            pair = new_pip4
        if new_pip4 == new_pip6:
            pair = new_pip4
        if new_pip4 == new_pip7:
            pair = new_pip4
        if new_pip5 == new_pip6:
            pair = new_pip5
        if new_pip5 == new_pip7:
            pair = new_pip5
        if new_pip6 == new_pip7:
            pair = new_pip6
        if new_pip4 == new_pip5 == new_pip6 and new_pip4 > new_pip1:
            trip = new_pip4
            pair = new_pip1
        if new_pip4 == new_pip5 == new_pip7 and new_pip4 > new_pip1:
            trip = new_pip4
            pair = new_pip1
        if new_pip4 == new_pip6 == new_pip7 and new_pip4 > new_pip1:
            trip = new_pip4
            pair = new_pip1
        if new_pip5 == new_pip6 == new_pip7 and new_pip5 > new_pip1:
            trip = new_pip5
            pair = new_pip1
    if new_pip1 == new_pip2 == new_pip4:
        trip = new_pip1
        if new_pip3 == new_pip5:
            pair = new_pip3
        if new_pip3 == new_pip6:
            pair = new_pip3
        if new_pip3 == new_pip7:
            pair = new_pip3
        if new_pip5 == new_pip6:
            pair = new_pip5
        if new_pip5 == new_pip6:
            pair = new_pip5
        if new_pip6 == new_pip7:
            pair = new_pip6
        if new_pip3 == new_pip5 == new_pip6 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
        if new_pip3 == new_pip5 == new_pip7 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
        if new_pip3 == new_pip6 == new_pip7 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
        if new_pip5 == new_pip6 == new_pip7 and new_pip5 > new_pip1:
            trip = new_pip5
            pair = new_pip1
    if new_pip1 == new_pip2 == new_pip5:
        trip = new_pip1
        if new_pip3 == new_pip4:
            pair = new_pip3
        if new_pip3 == new_pip6:
            pair = new_pip3
        if new_pip3 == new_pip7:
            pair = new_pip3
        if new_pip4 == new_pip6:
            pair = new_pip4
        if new_pip4 == new_pip7:
            pair = new_pip4
        if new_pip6 == new_pip7:
            pair = new_pip6
        if new_pip3 == new_pip4 == new_pip6 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
        if new_pip3 == new_pip4 == new_pip7 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
        if new_pip3 == new_pip6 == new_pip7 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
        if new_pip4 == new_pip6 == new_pip7 and new_pip4 > new_pip1:
            trip = new_pip4
            pair = new_pip1
    if new_pip1 == new_pip2 == new_pip6:
        trip = new_pip1
        if new_pip3 == new_pip4:
            pair = new_pip3
        if new_pip3 == new_pip5:
            pair = new_pip3
        if new_pip3 == new_pip7:
            pair = new_pip3
        if new_pip4 == new_pip5:
            pair = new_pip4
        if new_pip4 == new_pip7:
            pair = new_pip4
        if new_pip5 == new_pip7:
            pair = new_pip5
        if new_pip3 == new_pip4 == new_pip5 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
        if new_pip3 == new_pip4 == new_pip7 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
        if new_pip3 == new_pip5 == new_pip7 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
        if new_pip4 == new_pip5 == new_pip7 and new_pip4 > new_pip1:
            trip = new_pip4
            pair = new_pip1
    if new_pip1 == new_pip2 == new_pip7:
        trip = new_pip1
        if new_pip3 == new_pip4:
            pair = new_pip3
        if new_pip3 == new_pip5:
            pair = new_pip3
        if new_pip3 == new_pip6:
            pair = new_pip3
        if new_pip4 == new_pip5:
            pair = new_pip4
        if new_pip4 == new_pip6:
            pair = new_pip4
        if new_pip5 == new_pip6:
            pair = new_pip5
        if new_pip3 == new_pip4 == new_pip5 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
        if new_pip3 == new_pip4 == new_pip6 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
        if new_pip3 == new_pip5 == new_pip6 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
        if new_pip4 == new_pip5 == new_pip6 and new_pip4 > new_pip1:
            trip = new_pip4
            pair = new_pip1
    if new_pip1 == new_pip3 == new_pip4:
        trip = new_pip1
        if new_pip2 == new_pip5:
            pair = new_pip2
        if new_pip2 == new_pip6:
            pair = new_pip2
        if new_pip2 == new_pip7:
            pair = new_pip2
        if new_pip5 == new_pip6:
            pair = new_pip5
        if new_pip5 == new_pip7:
            pair = new_pip5
        if new_pip6 == new_pip7:
            pair = new_pip6
        if new_pip2 == new_pip5 == new_pip6 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip5 == new_pip7 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip6 == new_pip7 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip5 == new_pip6 == new_pip7 and new_pip5 > new_pip1:
            trip = new_pip5
            pair = new_pip1
    if new_pip1 == new_pip3 == new_pip5:
        trip = new_pip1
        if new_pip2 == new_pip4:
            pair = new_pip2
        if new_pip2 == new_pip6:
            pair = new_pip2
        if new_pip2 == new_pip7:
            pair = new_pip2
        if new_pip4 == new_pip6:
            pair = new_pip4
        if new_pip4 == new_pip7:
            pair = new_pip4
        if new_pip6 == new_pip7:
            pair = new_pip6
        if new_pip2 == new_pip4 == new_pip6 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip4 == new_pip7 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip6 == new_pip7 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip4 == new_pip6 == new_pip7 and new_pip4 > new_pip1:
            trip = new_pip4
            pair = new_pip1
    if new_pip1 == new_pip3 == new_pip6:
        trip = new_pip1
        if new_pip2 == new_pip4:
            pair = new_pip2
        if new_pip2 == new_pip5:
            pair = new_pip2
        if new_pip2 == new_pip7:
            pair = new_pip2
        if new_pip4 == new_pip5:
            pair = new_pip4
        if new_pip4 == new_pip7:
            pair = new_pip4
        if new_pip5 == new_pip7:
            pair = new_pip5
        if new_pip2 == new_pip4 == new_pip5 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip4 == new_pip7 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip5 == new_pip7 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip4 == new_pip5 == new_pip7 and new_pip4 > new_pip1:
            trip = new_pip4
            pair = new_pip1
    if new_pip1 == new_pip3 == new_pip7:
        trip = new_pip1
        if new_pip2 == new_pip4:
            pair = new_pip2
        if new_pip2 == new_pip5:
            pair = new_pip2
        if new_pip2 == new_pip6:
            pair = new_pip2
        if new_pip4 == new_pip5:
            pair = new_pip4
        if new_pip4 == new_pip6:
            pair = new_pip4
        if new_pip5 == new_pip6:
            pair = new_pip5
        if new_pip2 == new_pip4 == new_pip5 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip4 == new_pip7 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip5 == new_pip7 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip4 == new_pip5 == new_pip7 and new_pip4 > new_pip1:
            trip = new_pip4
            pair = new_pip1
    if new_pip1 == new_pip4 == new_pip5:
        trip = new_pip1
        if new_pip2 == new_pip3:
            pair = new_pip2
        if new_pip2 == new_pip6:
            pair = new_pip2
        if new_pip2 == new_pip7:
            pair = new_pip2
        if new_pip3 == new_pip6:
            pair = new_pip3
        if new_pip3 == new_pip7:
            pair = new_pip3
        if new_pip6 == new_pip7:
            pair = new_pip6
        if new_pip2 == new_pip3 == new_pip6 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip3 == new_pip7 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip6 == new_pip7 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip3 == new_pip6 == new_pip7 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
    if new_pip1 == new_pip4 == new_pip6:
        trip = new_pip1
        if new_pip2 == new_pip3:
            pair = new_pip2
        if new_pip2 == new_pip5:
            pair = new_pip2
        if new_pip2 == new_pip7:
            pair = new_pip2
        if new_pip3 == new_pip5:
            pair = new_pip3
        if new_pip3 == new_pip7:
            pair = new_pip3
        if new_pip5 == new_pip7:
            pair = new_pip5
        if new_pip2 == new_pip3 == new_pip5 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip3 == new_pip7 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip5 == new_pip7 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip3 == new_pip5 == new_pip7 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
    if new_pip1 == new_pip4 == new_pip7:
        trip = new_pip1
        if new_pip2 == new_pip3:
            pair = new_pip2
        if new_pip2 == new_pip5:
            pair = new_pip2
        if new_pip2 == new_pip6:
            pair = new_pip2
        if new_pip3 == new_pip5:
            pair = new_pip3
        if new_pip3 == new_pip6:
            pair = new_pip3
        if new_pip5 == new_pip6:
            pair = new_pip5
        if new_pip2 == new_pip3 == new_pip5 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip3 == new_pip6 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip5 == new_pip6 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip3 == new_pip5 == new_pip6 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
    if new_pip1 == new_pip5 == new_pip6:
        trip = new_pip1
        if new_pip2 == new_pip3:
            pair = new_pip2
        if new_pip2 == new_pip4:
            pair = new_pip2
        if new_pip2 == new_pip7:
            pair = new_pip2
        if new_pip3 == new_pip4:
            pair = new_pip3
        if new_pip3 == new_pip7:
            pair = new_pip3
        if new_pip4 == new_pip7:
            pair = new_pip4
        if new_pip2 == new_pip3 == new_pip4 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip3 == new_pip7 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip4 == new_pip7 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip3 == new_pip4 == new_pip7 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
    if new_pip1 == new_pip5 == new_pip7:
        trip = new_pip1
        if new_pip2 == new_pip3:
            pair = new_pip2
        if new_pip2 == new_pip4:
            pair = new_pip2
        if new_pip2 == new_pip6:
            pair = new_pip2
        if new_pip3 == new_pip4:
            pair = new_pip3
        if new_pip3 == new_pip6:
            pair = new_pip3
        if new_pip4 == new_pip6:
            pair = new_pip4
        if new_pip2 == new_pip3 == new_pip4 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip3 == new_pip6 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip4 == new_pip6 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip3 == new_pip4 == new_pip6 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
    if new_pip1 == new_pip6 == new_pip7:
        trip = new_pip1
        if new_pip2 == new_pip3:
            pair = new_pip2
        if new_pip2 == new_pip4:
            pair = new_pip2
        if new_pip2 == new_pip5:
            pair = new_pip2
        if new_pip3 == new_pip4:
            pair = new_pip3
        if new_pip3 == new_pip5:
            pair = new_pip3
        if new_pip4 == new_pip5:
            pair = new_pip4
        if new_pip2 == new_pip3 == new_pip4 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip3 == new_pip5 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip4 == new_pip5 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip3 == new_pip4 == new_pip5 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
    if new_pip2 == new_pip3 == new_pip4:
        trip = new_pip2
        if new_pip1 == new_pip5:
            pair = new_pip1
        if new_pip1 == new_pip6:
            pair = new_pip1
        if new_pip1 == new_pip7:
            pair = new_pip1
        if new_pip5 == new_pip6:
            pair = new_pip5
        if new_pip5 == new_pip7:
            pair = new_pip5
        if new_pip6 == new_pip7:
            pair = new_pip6
        if new_pip5 == new_pip6 == new_pip7 and new_pip5 > new_pip2:
            trip = new_pip5
            pair = new_pip2
    if new_pip2 == new_pip3 == new_pip5:
        trip = new_pip2
        if new_pip1 == new_pip4:
            pair = new_pip1
        if new_pip1 == new_pip6:
            pair = new_pip1
        if new_pip1 == new_pip7:
            pair = new_pip1
        if new_pip4 == new_pip6:
            pair = new_pip4
        if new_pip4 == new_pip7:
            pair = new_pip4
        if new_pip6 == new_pip7:
            pair = new_pip6
        if new_pip4 == new_pip6 == new_pip7 and new_pip4 > new_pip2:
            trip = new_pip4
            pair = new_pip2
    if new_pip2 == new_pip3 == new_pip6:
        trip = new_pip2
        if new_pip1 == new_pip4:
            pair = new_pip1
        if new_pip1 == new_pip5:
            pair = new_pip1
        if new_pip1 == new_pip7:
            pair = new_pip1
        if new_pip4 == new_pip5:
            pair = new_pip4
        if new_pip4 == new_pip7:
            pair = new_pip4
        if new_pip5 == new_pip7:
            pair = new_pip5
        if new_pip4 == new_pip5 == new_pip7 and new_pip4 > new_pip2:
            trip = new_pip4
            pair = new_pip2
    if new_pip2 == new_pip3 == new_pip7:
        trip = new_pip2
        if new_pip1 == new_pip4:
            pair = new_pip1
        if new_pip1 == new_pip5:
            pair = new_pip1
        if new_pip1 == new_pip6:
            pair = new_pip1
        if new_pip4 == new_pip5:
            pair = new_pip4
        if new_pip4 == new_pip6:
            pair = new_pip4
        if new_pip5 == new_pip6:
            pair = new_pip5
        if new_pip4 == new_pip5 == new_pip6 and new_pip4 > new_pip2:
            trip = new_pip4
            pair = new_pip2
    if new_pip2 == new_pip4 == new_pip5:
        trip = new_pip2
        if new_pip1 == new_pip3:
            pair = new_pip1
        if new_pip1 == new_pip6:
            pair = new_pip1
        if new_pip1 == new_pip7:
            pair = new_pip1
        if new_pip3 == new_pip6:
            pair = new_pip4
        if new_pip3 == new_pip7:
            pair = new_pip4
        if new_pip6 == new_pip7:
            pair = new_pip6
        if new_pip3 == new_pip6 == new_pip7 and new_pip3 > new_pip2:
            trip = new_pip3
            pair = new_pip2
    if new_pip2 == new_pip4 == new_pip6:
        trip = new_pip2
        if new_pip1 == new_pip3:
            pair = new_pip1
        if new_pip1 == new_pip5:
            pair = new_pip1
        if new_pip1 == new_pip7:
            pair = new_pip1
        if new_pip3 == new_pip5:
            pair = new_pip4
        if new_pip3 == new_pip7:
            pair = new_pip4
        if new_pip5 == new_pip7:
            pair = new_pip5
        if new_pip3 == new_pip5 == new_pip7 and new_pip3 > new_pip2:
            trip = new_pip3
            pair = new_pip2
    if new_pip2 == new_pip4 == new_pip7:
        trip = new_pip2
        if new_pip1 == new_pip3:
            pair = new_pip1
        if new_pip1 == new_pip5:
            pair = new_pip1
        if new_pip1 == new_pip6:
            pair = new_pip1
        if new_pip3 == new_pip5:
            pair = new_pip5
        if new_pip3 == new_pip6:
            pair = new_pip5
        if new_pip5 == new_pip6:
            pair = new_pip5
        if new_pip3 == new_pip5 == new_pip6 and new_pip3 > new_pip2:
            trip = new_pip3
            pair = new_pip2
    if new_pip2 == new_pip5 == new_pip6:
        trip = new_pip2
        if new_pip1 == new_pip3:
            pair = new_pip1
        if new_pip1 == new_pip4:
            pair = new_pip1
        if new_pip1 == new_pip7:
            pair = new_pip1
        if new_pip3 == new_pip4:
            pair = new_pip3
        if new_pip3 == new_pip7:
            pair = new_pip3
        if new_pip4 == new_pip7:
            pair = new_pip4
        if new_pip3 == new_pip4 == new_pip7 and new_pip3 > new_pip2:
            trip = new_pip3
            pair = new_pip2
    if new_pip2 == new_pip5 == new_pip7:
        trip = new_pip2
        if new_pip1 == new_pip3:
            pair = new_pip1
        if new_pip1 == new_pip4:
            pair = new_pip1
        if new_pip1 == new_pip6:
            pair = new_pip1
        if new_pip3 == new_pip4:
            pair = new_pip3
        if new_pip3 == new_pip6:
            pair = new_pip3
        if new_pip4 == new_pip6:
            pair = new_pip4
        if new_pip3 == new_pip4 == new_pip6 and new_pip3 > new_pip2:
            trip = new_pip3
            pair = new_pip2
    if new_pip2 == new_pip6 == new_pip7:
        trip = new_pip2
        if new_pip1 == new_pip3:
            pair = new_pip1
        if new_pip1 == new_pip4:
            pair = new_pip1
        if new_pip1 == new_pip5:
            pair = new_pip1
        if new_pip3 == new_pip4:
            pair = new_pip3
        if new_pip3 == new_pip5:
            pair = new_pip3
        if new_pip4 == new_pip5:
            pair = new_pip4
        if new_pip3 == new_pip4 == new_pip5 and new_pip3 > new_pip2:
            trip = new_pip3
            pair = new_pip2
    if new_pip3 == new_pip4 == new_pip5:
        trip = new_pip3
        if new_pip1 == new_pip2:
            pair = new_pip1
        if new_pip1 == new_pip6:
            pair = new_pip1
        if new_pip1 == new_pip7:
            pair = new_pip1
        if new_pip2 == new_pip6:
            pair = new_pip2
        if new_pip2 == new_pip7:
            pair = new_pip2
        if new_pip6 == new_pip7:
            pair = new_pip6
    if new_pip3 == new_pip4 == new_pip6:
        trip = new_pip3
        if new_pip1 == new_pip2:
            pair = new_pip1
        if new_pip1 == new_pip5:
            pair = new_pip1
        if new_pip1 == new_pip7:
            pair = new_pip1
        if new_pip2 == new_pip5:
            pair = new_pip2
        if new_pip2 == new_pip7:
            pair = new_pip2
        if new_pip5 == new_pip7:
            pair = new_pip5
    if new_pip3 == new_pip4 == new_pip7:
        trip = new_pip3
        if new_pip1 == new_pip2:
            pair = new_pip1
        if new_pip1 == new_pip5:
            pair = new_pip1
        if new_pip1 == new_pip6:
            pair = new_pip1
        if new_pip2 == new_pip5:
            pair = new_pip2
        if new_pip2 == new_pip6:
            pair = new_pip2
        if new_pip5 == new_pip6:
            pair = new_pip5
    if new_pip3 == new_pip5 == new_pip6:
        trip = new_pip3
        if new_pip1 == new_pip2:
            pair = new_pip1
        if new_pip1 == new_pip4:
            pair = new_pip1
        if new_pip1 == new_pip7:
            pair = new_pip1
        if new_pip2 == new_pip4:
            pair = new_pip2
        if new_pip2 == new_pip7:
            pair = new_pip2
        if new_pip4 == new_pip7:
            pair = new_pip4
    if new_pip3 == new_pip5 == new_pip7:
        trip = new_pip3
        if new_pip1 == new_pip2:
            pair = new_pip1
        if new_pip1 == new_pip4:
            pair = new_pip1
        if new_pip1 == new_pip6:
            pair = new_pip1
        if new_pip2 == new_pip4:
            pair = new_pip2
        if new_pip2 == new_pip6:
            pair = new_pip2
        if new_pip4 == new_pip6:
            pair = new_pip4
    if new_pip3 == new_pip6 == new_pip7:
        trip = new_pip3
        if new_pip1 == new_pip2:
            pair = new_pip1
        if new_pip1 == new_pip4:
            pair = new_pip1
        if new_pip1 == new_pip5:
            pair = new_pip1
        if new_pip2 == new_pip4:
            pair = new_pip2
        if new_pip2 == new_pip5:
            pair = new_pip2
        if new_pip4 == new_pip5:
            pair = new_pip4
    if new_pip4 == new_pip5 == new_pip6:
        trip = new_pip4
        if new_pip1 == new_pip2:
            pair = new_pip1
        if new_pip1 == new_pip3:
            pair = new_pip1
        if new_pip1 == new_pip7:
            pair = new_pip1
        if new_pip2 == new_pip3:
            pair = new_pip2
        if new_pip2 == new_pip7:
            pair = new_pip2
        if new_pip3 == new_pip7:
            pair = new_pip3
    if new_pip4 == new_pip5 == new_pip7:
        trip = new_pip4
        if new_pip1 == new_pip2:
            pair = new_pip1
        if new_pip1 == new_pip3:
            pair = new_pip1
        if new_pip1 == new_pip6:
            pair = new_pip1
        if new_pip2 == new_pip3:
            pair = new_pip2
        if new_pip2 == new_pip6:
            pair = new_pip2
        if new_pip3 == new_pip6:
            pair = new_pip3
    if new_pip4 == new_pip6 == new_pip7:
        trip = new_pip4
        if new_pip1 == new_pip2:
            pair = new_pip1
        if new_pip1 == new_pip3:
            pair = new_pip1
        if new_pip1 == new_pip5:
            pair = new_pip1
        if new_pip2 == new_pip3:
            pair = new_pip2
        if new_pip2 == new_pip5:
            pair = new_pip2
        if new_pip3 == new_pip5:
            pair = new_pip3
    if new_pip5 == new_pip6 == new_pip7:
        trip = new_pip5
        if new_pip1 == new_pip2:
            pair = new_pip1
        if new_pip1 == new_pip3:
            pair = new_pip1
        if new_pip1 == new_pip4:
            pair = new_pip1
        if new_pip2 == new_pip3:
            pair = new_pip2
        if new_pip2 == new_pip4:
            pair = new_pip2
        if new_pip3 == new_pip4:
            pair = new_pip3
    if (trip > 0) and (pair > 0):
        full_house = trip
    return full_house


def full_house_kickers(pip1, pip2, pip3, pip4, pip5, pip6, pip7):
    new_pip1 = face_cards(pip1)
    new_pip2 = face_cards(pip2)
    new_pip3 = face_cards(pip3)
    new_pip4 = face_cards(pip4)
    new_pip5 = face_cards(pip5)
    new_pip6 = face_cards(pip6)
    new_pip7 = face_cards(pip7)
    full_house_kicker = 0
    pair = 0
    trip = 0
    if new_pip1 == new_pip2 == new_pip3:
        trip = new_pip1
        if new_pip4 == new_pip5:
            pair = new_pip4
            if new_pip6 == new_pip7 and new_pip6 > new_pip4:
                pair = new_pip6
        if new_pip4 == new_pip6:
            pair = new_pip4
            if new_pip5 == new_pip7 and new_pip5 > new_pip4:
                pair = new_pip5
        if new_pip4 == new_pip7:
            pair = new_pip4
            if new_pip5 == new_pip6 and new_pip5 > new_pip4:
                pair = new_pip5
        if new_pip5 == new_pip6:
            pair = new_pip5
        if new_pip5 == new_pip7:
            pair = new_pip5
        if new_pip6 == new_pip7:
            pair = new_pip6
        if new_pip4 == new_pip5 == new_pip6 and new_pip4 > new_pip1:
            trip = new_pip4
            pair = new_pip1
        if new_pip4 == new_pip5 == new_pip7 and new_pip4 > new_pip1:
            trip = new_pip4
            pair = new_pip1
        if new_pip4 == new_pip6 == new_pip7 and new_pip4 > new_pip1:
            trip = new_pip4
            pair = new_pip1
        if new_pip5 == new_pip6 == new_pip7 and new_pip5 > new_pip1:
            trip = new_pip5
            pair = new_pip1
    if new_pip1 == new_pip2 == new_pip4:
        trip = new_pip1
        if new_pip3 == new_pip5:
            pair = new_pip3
            if new_pip6 == new_pip7 and new_pip6 > new_pip3:
                pair = new_pip6
        if new_pip3 == new_pip6:
            pair = new_pip3
            if new_pip5 == new_pip7 and new_pip5 > new_pip3:
                pair = new_pip5
        if new_pip3 == new_pip7:
            pair = new_pip3
            if new_pip5 == new_pip6 and new_pip5 > new_pip3:
                pair = new_pip5
        if new_pip5 == new_pip6:
            pair = new_pip5
        if new_pip5 == new_pip6:
            pair = new_pip5
        if new_pip6 == new_pip7:
            pair = new_pip6
        if new_pip3 == new_pip5 == new_pip6 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
        if new_pip3 == new_pip5 == new_pip7 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
        if new_pip3 == new_pip6 == new_pip7 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
        if new_pip5 == new_pip6 == new_pip7 and new_pip5 > new_pip1:
            trip = new_pip5
            pair = new_pip1
    if new_pip1 == new_pip2 == new_pip5:
        trip = new_pip1
        if new_pip3 == new_pip4:
            pair = new_pip3
            if new_pip6 == new_pip7 and new_pip6 > new_pip3:
                pair = new_pip6
        if new_pip3 == new_pip6:
            pair = new_pip3
            if new_pip4 == new_pip7 and new_pip4 > new_pip3:
                pair = new_pip4
        if new_pip3 == new_pip7:
            pair = new_pip3
            if new_pip4 == new_pip6 and new_pip4 > new_pip3:
                pair = new_pip4
        if new_pip4 == new_pip6:
            pair = new_pip4
        if new_pip4 == new_pip7:
            pair = new_pip4
        if new_pip6 == new_pip7:
            pair = new_pip6
        if new_pip3 == new_pip4 == new_pip6 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
        if new_pip3 == new_pip4 == new_pip7 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
        if new_pip3 == new_pip6 == new_pip7 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
        if new_pip4 == new_pip6 == new_pip7 and new_pip4 > new_pip1:
            trip = new_pip4
            pair = new_pip1
    if new_pip1 == new_pip2 == new_pip6:
        trip = new_pip1
        if new_pip3 == new_pip4:
            pair = new_pip3
            if new_pip5 == new_pip7 and new_pip5 > new_pip3:
                pair = new_pip5
        if new_pip3 == new_pip5:
            pair = new_pip3
            if new_pip4 == new_pip7 and new_pip4 > new_pip3:
                pair = new_pip4
        if new_pip3 == new_pip7:
            pair = new_pip3
            if new_pip4 == new_pip5 and new_pip4 > new_pip3:
                pair = new_pip4
        if new_pip4 == new_pip5:
            pair = new_pip4
        if new_pip4 == new_pip7:
            pair = new_pip4
        if new_pip5 == new_pip7:
            pair = new_pip5
        if new_pip3 == new_pip4 == new_pip5 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
        if new_pip3 == new_pip4 == new_pip7 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
        if new_pip3 == new_pip5 == new_pip7 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
        if new_pip4 == new_pip5 == new_pip7 and new_pip4 > new_pip1:
            trip = new_pip4
            pair = new_pip1
    if new_pip1 == new_pip2 == new_pip7:
        trip = new_pip1
        if new_pip3 == new_pip4:
            pair = new_pip3
            if new_pip5 == new_pip6 and new_pip5 > new_pip3:
                pair = new_pip5
        if new_pip3 == new_pip5:
            pair = new_pip3
            if new_pip4 == new_pip6 and new_pip4 > new_pip3:
                pair = new_pip4
        if new_pip3 == new_pip6:
            pair = new_pip3
            if new_pip4 == new_pip5 and new_pip4 > new_pip3:
                pair = new_pip4
        if new_pip4 == new_pip5:
            pair = new_pip4
        if new_pip4 == new_pip6:
            pair = new_pip4
        if new_pip5 == new_pip6:
            pair = new_pip5
        if new_pip3 == new_pip4 == new_pip5 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
        if new_pip3 == new_pip4 == new_pip6 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
        if new_pip3 == new_pip5 == new_pip6 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
        if new_pip4 == new_pip5 == new_pip6 and new_pip4 > new_pip1:
            trip = new_pip4
            pair = new_pip1
    if new_pip1 == new_pip3 == new_pip4:
        trip = new_pip1
        if new_pip2 == new_pip5:
            pair = new_pip2
            if new_pip6 == new_pip7 and new_pip6 > new_pip2:
                pair = new_pip6
        if new_pip2 == new_pip6:
            pair = new_pip2
            if new_pip5 == new_pip7 and new_pip5 > new_pip2:
                pair = new_pip5
        if new_pip2 == new_pip7:
            pair = new_pip2
            if new_pip5 == new_pip6 and new_pip5 > new_pip2:
                pair = new_pip5
        if new_pip5 == new_pip6:
            pair = new_pip5
        if new_pip5 == new_pip7:
            pair = new_pip5
        if new_pip6 == new_pip7:
            pair = new_pip6
        if new_pip2 == new_pip5 == new_pip6 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip5 == new_pip7 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip6 == new_pip7 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip5 == new_pip6 == new_pip7 and new_pip5 > new_pip1:
            trip = new_pip5
            pair = new_pip1
    if new_pip1 == new_pip3 == new_pip5:
        trip = new_pip1
        if new_pip2 == new_pip4:
            pair = new_pip2
            if new_pip6 == new_pip7 and new_pip6 > new_pip2:
                pair = new_pip6
        if new_pip2 == new_pip6:
            pair = new_pip2
            if new_pip4 == new_pip7 and new_pip4 > new_pip2:
                pair = new_pip4
        if new_pip2 == new_pip7:
            pair = new_pip2
            if new_pip4 == new_pip6 and new_pip4 > new_pip2:
                pair = new_pip4
        if new_pip4 == new_pip6:
            pair = new_pip4
        if new_pip4 == new_pip7:
            pair = new_pip4
        if new_pip6 == new_pip7:
            pair = new_pip6
        if new_pip2 == new_pip4 == new_pip6 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip4 == new_pip7 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip6 == new_pip7 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip4 == new_pip6 == new_pip7 and new_pip4 > new_pip1:
            trip = new_pip4
            pair = new_pip1
    if new_pip1 == new_pip3 == new_pip6:
        trip = new_pip1
        if new_pip2 == new_pip4:
            pair = new_pip2
            if new_pip5 == new_pip7 and new_pip5 > new_pip2:
                pair = new_pip5
        if new_pip2 == new_pip5:
            pair = new_pip2
            if new_pip4 == new_pip7 and new_pip4 > new_pip2:
                pair = new_pip4
        if new_pip2 == new_pip7:
            pair = new_pip2
            if new_pip4 == new_pip5 and new_pip4 > new_pip2:
                pair = new_pip4
        if new_pip4 == new_pip5:
            pair = new_pip4
        if new_pip4 == new_pip7:
            pair = new_pip4
        if new_pip5 == new_pip7:
            pair = new_pip5
        if new_pip2 == new_pip4 == new_pip5 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip4 == new_pip7 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip5 == new_pip7 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip4 == new_pip5 == new_pip7 and new_pip4 > new_pip1:
            trip = new_pip4
            pair = new_pip1
    if new_pip1 == new_pip3 == new_pip7:
        trip = new_pip1
        if new_pip2 == new_pip4:
            pair = new_pip2
            if new_pip5 == new_pip6 and new_pip5 > new_pip2:
                pair = new_pip5
        if new_pip2 == new_pip5:
            pair = new_pip2
            if new_pip4 == new_pip6 and new_pip4 > new_pip2:
                pair = new_pip4
        if new_pip2 == new_pip6:
            pair = new_pip2
            if new_pip4 == new_pip5 and new_pip5 > new_pip2:
                pair = new_pip5
        if new_pip4 == new_pip5:
            pair = new_pip4
        if new_pip4 == new_pip6:
            pair = new_pip4
        if new_pip5 == new_pip6:
            pair = new_pip5
        if new_pip2 == new_pip4 == new_pip5 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip4 == new_pip7 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip5 == new_pip7 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip4 == new_pip5 == new_pip7 and new_pip4 > new_pip1:
            trip = new_pip4
            pair = new_pip1
    if new_pip1 == new_pip4 == new_pip5:
        trip = new_pip1
        if new_pip2 == new_pip3:
            pair = new_pip2
            if new_pip6 == new_pip7 and new_pip6 > new_pip2:
                pair = new_pip6
        if new_pip2 == new_pip6:
            pair = new_pip2
            if new_pip3 == new_pip7 and new_pip3 > new_pip2:
                pair = new_pip6
        if new_pip2 == new_pip7:
            pair = new_pip2
            if new_pip3 == new_pip6 and new_pip3 > new_pip2:
                pair = new_pip3
        if new_pip3 == new_pip6:
            pair = new_pip3
        if new_pip3 == new_pip7:
            pair = new_pip3
        if new_pip6 == new_pip7:
            pair = new_pip6
        if new_pip2 == new_pip3 == new_pip6 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip3 == new_pip7 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip6 == new_pip7 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip3 == new_pip6 == new_pip7 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
    if new_pip1 == new_pip4 == new_pip6:
        trip = new_pip1
        if new_pip2 == new_pip3:
            pair = new_pip2
            if new_pip5 == new_pip7 and new_pip5 > new_pip2:
                pair = new_pip5
        if new_pip2 == new_pip5:
            pair = new_pip2
            if new_pip3 == new_pip7 and new_pip3 > new_pip2:
                pair = new_pip3
        if new_pip2 == new_pip7:
            pair = new_pip2
            if new_pip3 == new_pip5 and new_pip3 > new_pip2:
                pair = new_pip3
        if new_pip3 == new_pip5:
            pair = new_pip3
        if new_pip3 == new_pip7:
            pair = new_pip3
        if new_pip5 == new_pip7:
            pair = new_pip5
        if new_pip2 == new_pip3 == new_pip5 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip3 == new_pip7 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip5 == new_pip7 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip3 == new_pip5 == new_pip7 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
    if new_pip1 == new_pip4 == new_pip7:
        trip = new_pip1
        if new_pip2 == new_pip3:
            pair = new_pip2
            if new_pip5 == new_pip6 and new_pip5 > new_pip2:
                pair = new_pip5
        if new_pip2 == new_pip5:
            pair = new_pip2
            if new_pip3 == new_pip6 and new_pip3 > new_pip2:
                pair = new_pip3
        if new_pip2 == new_pip6:
            pair = new_pip2
            if new_pip3 == new_pip5 and new_pip3 > new_pip2:
                pair = new_pip3
        if new_pip3 == new_pip5:
            pair = new_pip3
        if new_pip3 == new_pip6:
            pair = new_pip3
        if new_pip5 == new_pip6:
            pair = new_pip5
        if new_pip2 == new_pip3 == new_pip5 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip3 == new_pip6 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip5 == new_pip6 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip3 == new_pip5 == new_pip6 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
    if new_pip1 == new_pip5 == new_pip6:
        trip = new_pip1
        if new_pip2 == new_pip3:
            pair = new_pip2
            if new_pip4 == new_pip7 and new_pip4 > new_pip2:
                pair = new_pip4
        if new_pip2 == new_pip4:
            pair = new_pip2
            if new_pip3 == new_pip7 and new_pip3 > new_pip2:
                pair = new_pip3
        if new_pip2 == new_pip7:
            pair = new_pip2
            if new_pip3 == new_pip4 and new_pip3 > new_pip2:
                pair = new_pip3
        if new_pip3 == new_pip4:
            pair = new_pip3
        if new_pip3 == new_pip7:
            pair = new_pip3
        if new_pip4 == new_pip7:
            pair = new_pip4
        if new_pip2 == new_pip3 == new_pip4 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip3 == new_pip7 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip4 == new_pip7 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip3 == new_pip4 == new_pip7 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
    if new_pip1 == new_pip5 == new_pip7:
        trip = new_pip1
        if new_pip2 == new_pip3:
            pair = new_pip2
            if new_pip4 == new_pip6 and new_pip4 > new_pip2:
                pair = new_pip4
        if new_pip2 == new_pip4:
            pair = new_pip2
            if new_pip3 == new_pip6 and new_pip3 > new_pip2:
                pair = new_pip3
        if new_pip2 == new_pip6:
            pair = new_pip2
            if new_pip3 == new_pip4 and new_pip3 > new_pip2:
                pair = new_pip3
        if new_pip3 == new_pip4:
            pair = new_pip3
        if new_pip3 == new_pip6:
            pair = new_pip3
        if new_pip4 == new_pip6:
            pair = new_pip4
        if new_pip2 == new_pip3 == new_pip4 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip3 == new_pip6 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip4 == new_pip6 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip3 == new_pip4 == new_pip6 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
    if new_pip1 == new_pip6 == new_pip7:
        trip = new_pip1
        if new_pip2 == new_pip3:
            pair = new_pip2
            if new_pip4 == new_pip5 and new_pip4 > new_pip2:
                pair = new_pip4
        if new_pip2 == new_pip4:
            pair = new_pip2
            if new_pip3 == new_pip5 and new_pip3 > new_pip2:
                pair = new_pip3
        if new_pip2 == new_pip5:
            pair = new_pip2
            if new_pip3 == new_pip4 and new_pip3 > new_pip2:
                pair = new_pip3
        if new_pip3 == new_pip4:
            pair = new_pip3
        if new_pip3 == new_pip5:
            pair = new_pip3
        if new_pip4 == new_pip5:
            pair = new_pip4
        if new_pip2 == new_pip3 == new_pip4 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip3 == new_pip5 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip2 == new_pip4 == new_pip5 and new_pip2 > new_pip1:
            trip = new_pip2
            pair = new_pip1
        if new_pip3 == new_pip4 == new_pip5 and new_pip3 > new_pip1:
            trip = new_pip3
            pair = new_pip1
    if new_pip2 == new_pip3 == new_pip4:
        trip = new_pip2
        if new_pip1 == new_pip5:
            pair = new_pip1
            if new_pip6 == new_pip7 and new_pip6 > new_pip1:
                pair = new_pip6
        if new_pip1 == new_pip6:
            pair = new_pip1
            if new_pip5 == new_pip7 and new_pip5 > new_pip1:
                pair = new_pip5
        if new_pip1 == new_pip7:
            pair = new_pip1
            if new_pip5 == new_pip6 and new_pip5 > new_pip1:
                pair = new_pip5
        if new_pip5 == new_pip6:
            pair = new_pip5
        if new_pip5 == new_pip7:
            pair = new_pip5
        if new_pip6 == new_pip7:
            pair = new_pip6
        if new_pip5 == new_pip6 == new_pip7 and new_pip5 > new_pip2:
            trip = new_pip5
            pair = new_pip2
    if new_pip2 == new_pip3 == new_pip5:
        trip = new_pip2
        if new_pip1 == new_pip4:
            pair = new_pip1
            if new_pip6 == new_pip7 and new_pip6 > new_pip1:
                pair = new_pip6
        if new_pip1 == new_pip6:
            pair = new_pip1
            if new_pip4 == new_pip7 and new_pip4 > new_pip1:
                pair = new_pip4
        if new_pip1 == new_pip7:
            pair = new_pip1
            if new_pip4 == new_pip6 and new_pip4 > new_pip1:
                pair = new_pip4
        if new_pip4 == new_pip6:
            pair = new_pip4
        if new_pip4 == new_pip7:
            pair = new_pip4
        if new_pip6 == new_pip7:
            pair = new_pip6
        if new_pip4 == new_pip6 == new_pip7 and new_pip4 > new_pip2:
            trip = new_pip4
            pair = new_pip2
    if new_pip2 == new_pip3 == new_pip6:
        trip = new_pip2
        if new_pip1 == new_pip4:
            pair = new_pip1
            if new_pip5 == new_pip7 and new_pip5 > new_pip1:
                pair = new_pip5
        if new_pip1 == new_pip5:
            pair = new_pip1
            if new_pip4 == new_pip7 and new_pip4 > new_pip1:
                pair = new_pip4
        if new_pip1 == new_pip7:
            pair = new_pip1
            if new_pip4 == new_pip5 and new_pip4 > new_pip1:
                pair = new_pip4
        if new_pip4 == new_pip5:
            pair = new_pip4
        if new_pip4 == new_pip7:
            pair = new_pip4
        if new_pip5 == new_pip7:
            pair = new_pip5
        if new_pip4 == new_pip5 == new_pip7 and new_pip4 > new_pip2:
            trip = new_pip4
            pair = new_pip2
    if new_pip2 == new_pip3 == new_pip7:
        trip = new_pip2
        if new_pip1 == new_pip4:
            pair = new_pip1
            if new_pip5 == new_pip6 and new_pip5 > new_pip1:
                pair = new_pip5
        if new_pip1 == new_pip5:
            pair = new_pip1
            if new_pip4 == new_pip6 and new_pip4 > new_pip1:
                pair = new_pip4
        if new_pip1 == new_pip6:
            pair = new_pip1
            if new_pip4 == new_pip5 and new_pip4 > new_pip1:
                pair = new_pip4
        if new_pip4 == new_pip5:
            pair = new_pip4
        if new_pip4 == new_pip6:
            pair = new_pip4
        if new_pip5 == new_pip6:
            pair = new_pip5
        if new_pip4 == new_pip5 == new_pip6 and new_pip4 > new_pip2:
            trip = new_pip4
            pair = new_pip2
    if new_pip2 == new_pip4 == new_pip5:
        trip = new_pip2
        if new_pip1 == new_pip3:
            pair = new_pip1
            if new_pip6 == new_pip7 and new_pip6 > new_pip1:
                pair = new_pip6
        if new_pip1 == new_pip6:
            pair = new_pip1
            if new_pip3 == new_pip7 and new_pip3 > new_pip1:
                pair = new_pip3
        if new_pip1 == new_pip7:
            pair = new_pip1
            if new_pip3 == new_pip6 and new_pip3 > new_pip1:
                pair = new_pip3
        if new_pip3 == new_pip6:
            pair = new_pip4
        if new_pip3 == new_pip7:
            pair = new_pip4
        if new_pip6 == new_pip7:
            pair = new_pip6
        if new_pip3 == new_pip6 == new_pip7 and new_pip3 > new_pip2:
            trip = new_pip3
            pair = new_pip2
    if new_pip2 == new_pip4 == new_pip6:
        trip = new_pip2
        if new_pip1 == new_pip3:
            pair = new_pip1
            if new_pip5 == new_pip7 and new_pip5 > new_pip1:
                pair = new_pip5
        if new_pip1 == new_pip5:
            pair = new_pip1
            if new_pip3 == new_pip7 and new_pip3 > new_pip1:
                pair = new_pip3
        if new_pip1 == new_pip7:
            pair = new_pip1
            if new_pip3 == new_pip5 and new_pip3 > new_pip1:
                pair = new_pip3
        if new_pip3 == new_pip5:
            pair = new_pip4
        if new_pip3 == new_pip7:
            pair = new_pip4
        if new_pip5 == new_pip7:
            pair = new_pip5
        if new_pip3 == new_pip5 == new_pip7 and new_pip3 > new_pip2:
            trip = new_pip3
            pair = new_pip2
    if new_pip2 == new_pip4 == new_pip7:
        trip = new_pip2
        if new_pip1 == new_pip3:
            pair = new_pip1
            if new_pip5 == new_pip6 and new_pip5 > new_pip1:
                pair = new_pip5
        if new_pip1 == new_pip5:
            pair = new_pip1
            if new_pip3 == new_pip6 and new_pip3 > new_pip1:
                pair = new_pip3
        if new_pip1 == new_pip6:
            pair = new_pip1
            if new_pip3 == new_pip5 and new_pip3 > new_pip1:
                pair = new_pip3
        if new_pip3 == new_pip5:
            pair = new_pip5
        if new_pip3 == new_pip6:
            pair = new_pip5
        if new_pip5 == new_pip6:
            pair = new_pip5
        if new_pip3 == new_pip5 == new_pip6 and new_pip3 > new_pip2:
            trip = new_pip3
            pair = new_pip2
    if new_pip2 == new_pip5 == new_pip6:
        trip = new_pip2
        if new_pip1 == new_pip3:
            pair = new_pip1
            if new_pip4 == new_pip7 and new_pip4 > new_pip1:
                pair = new_pip4
        if new_pip1 == new_pip4:
            pair = new_pip1
            if new_pip3 == new_pip7 and new_pip3 > new_pip1:
                pair = new_pip3
        if new_pip1 == new_pip7:
            pair = new_pip1
            if new_pip3 == new_pip4 and new_pip3 > new_pip1:
                pair = new_pip3
        if new_pip3 == new_pip4:
            pair = new_pip3
        if new_pip3 == new_pip7:
            pair = new_pip3
        if new_pip4 == new_pip7:
            pair = new_pip4
        if new_pip3 == new_pip4 == new_pip7 and new_pip3 > new_pip2:
            trip = new_pip3
            pair = new_pip2
    if new_pip2 == new_pip5 == new_pip7:
        trip = new_pip2
        if new_pip1 == new_pip3:
            pair = new_pip1
            if new_pip4 == new_pip6 and new_pip4 > new_pip1:
                pair = new_pip4
        if new_pip1 == new_pip4:
            pair = new_pip1
            if new_pip3 == new_pip6 and new_pip3 > new_pip1:
                pair = new_pip3
        if new_pip1 == new_pip6:
            pair = new_pip1
            if new_pip3 == new_pip4 and new_pip3 > new_pip1:
                pair = new_pip3
        if new_pip3 == new_pip4:
            pair = new_pip3
        if new_pip3 == new_pip6:
            pair = new_pip3
        if new_pip4 == new_pip6:
            pair = new_pip4
        if new_pip3 == new_pip4 == new_pip6 and new_pip3 > new_pip2:
            trip = new_pip3
            pair = new_pip2
    if new_pip2 == new_pip6 == new_pip7:
        trip = new_pip2
        if new_pip1 == new_pip3:
            pair = new_pip1
            if new_pip4 == new_pip5 and new_pip4 > new_pip1:
                pair = new_pip4
        if new_pip1 == new_pip4:
            pair = new_pip1
            if new_pip3 == new_pip5 and new_pip3 > new_pip1:
                pair = new_pip3
        if new_pip1 == new_pip5:
            pair = new_pip1
            if new_pip3 == new_pip4 and new_pip3 > new_pip1:
                pair = new_pip3
        if new_pip3 == new_pip4:
            pair = new_pip3
        if new_pip3 == new_pip5:
            pair = new_pip3
        if new_pip4 == new_pip5:
            pair = new_pip4
        if new_pip3 == new_pip4 == new_pip5 and new_pip3 > new_pip2:
            trip = new_pip3
            pair = new_pip2
    if new_pip3 == new_pip4 == new_pip5:
        trip = new_pip3
        if new_pip1 == new_pip2:
            pair = new_pip1
            if new_pip6 == new_pip7 and new_pip6 > new_pip1:
                pair = new_pip6
        if new_pip1 == new_pip6:
            pair = new_pip1
            if new_pip2 == new_pip7 and new_pip2 > new_pip1:
                pair = new_pip2
        if new_pip1 == new_pip7:
            pair = new_pip1
            if new_pip2 == new_pip6 and new_pip2 > new_pip1:
                pair = new_pip2
        if new_pip2 == new_pip6:
            pair = new_pip2
        if new_pip2 == new_pip7:
            pair = new_pip2
        if new_pip6 == new_pip7:
            pair = new_pip6
    if new_pip3 == new_pip4 == new_pip6:
        trip = new_pip3
        if new_pip1 == new_pip2:
            pair = new_pip1
            if new_pip5 == new_pip7 and new_pip5 > new_pip1:
                pair = new_pip5
        if new_pip1 == new_pip5:
            pair = new_pip1
            if new_pip2 == new_pip7 and new_pip2 > new_pip1:
                pair = new_pip2
        if new_pip1 == new_pip7:
            pair = new_pip1
            if new_pip2 == new_pip5 and new_pip2 > new_pip1:
                pair = new_pip2
        if new_pip2 == new_pip5:
            pair = new_pip2
        if new_pip2 == new_pip7:
            pair = new_pip2
        if new_pip5 == new_pip7:
            pair = new_pip5
    if new_pip3 == new_pip4 == new_pip7:
        trip = new_pip3
        if new_pip1 == new_pip2:
            pair = new_pip1
            if new_pip5 == new_pip6 and new_pip5 > new_pip1:
                pair = new_pip5
        if new_pip1 == new_pip5:
            pair = new_pip1
            if new_pip2 == new_pip6 and new_pip2 > new_pip1:
                pair = new_pip2
        if new_pip1 == new_pip6:
            pair = new_pip1
            if new_pip2 == new_pip5 and new_pip2 > new_pip1:
                pair = new_pip2
        if new_pip2 == new_pip5:
            pair = new_pip2
        if new_pip2 == new_pip6:
            pair = new_pip2
        if new_pip5 == new_pip6:
            pair = new_pip5
    if new_pip3 == new_pip5 == new_pip6:
        trip = new_pip3
        if new_pip1 == new_pip2:
            pair = new_pip1
            if new_pip4 == new_pip7 and new_pip4 > new_pip1:
                pair = new_pip4
        if new_pip1 == new_pip4:
            pair = new_pip1
            if new_pip2 == new_pip7 and new_pip2 > new_pip1:
                pair = new_pip2
        if new_pip1 == new_pip7:
            pair = new_pip1
            if new_pip2 == new_pip4 and new_pip2 > new_pip1:
                pair = new_pip2
        if new_pip2 == new_pip4:
            pair = new_pip2
        if new_pip2 == new_pip7:
            pair = new_pip2
        if new_pip4 == new_pip7:
            pair = new_pip4
    if new_pip3 == new_pip5 == new_pip7:
        trip = new_pip3
        if new_pip1 == new_pip2:
            pair = new_pip1
            if new_pip4 == new_pip6 and new_pip4 > new_pip1:
                pair = new_pip4
        if new_pip1 == new_pip4:
            pair = new_pip1
            if new_pip2 == new_pip6 and new_pip2 > new_pip1:
                pair = new_pip2
        if new_pip1 == new_pip6:
            pair = new_pip1
            if new_pip2 == new_pip4 and new_pip2 > new_pip1:
                pair = new_pip2
        if new_pip2 == new_pip4:
            pair = new_pip2
        if new_pip2 == new_pip6:
            pair = new_pip2
        if new_pip4 == new_pip6:
            pair = new_pip4
    if new_pip3 == new_pip6 == new_pip7:
        trip = new_pip3
        if new_pip1 == new_pip2:
            pair = new_pip1
            if new_pip4 == new_pip5 and new_pip4 > new_pip1:
                pair = new_pip4
        if new_pip1 == new_pip4:
            pair = new_pip1
            if new_pip2 == new_pip5 and new_pip2 > new_pip1:
                pair = new_pip2
        if new_pip1 == new_pip5:
            pair = new_pip1
            if new_pip2 == new_pip4 and new_pip2 > new_pip1:
                pair = new_pip2
        if new_pip2 == new_pip4:
            pair = new_pip2
        if new_pip2 == new_pip5:
            pair = new_pip2
        if new_pip4 == new_pip5:
            pair = new_pip4
    if new_pip4 == new_pip5 == new_pip6:
        trip = new_pip4
        if new_pip1 == new_pip2:
            pair = new_pip1
            if new_pip3 == new_pip7 and new_pip3 > new_pip1:
                pair = new_pip3
        if new_pip1 == new_pip3:
            pair = new_pip1
            if new_pip2 == new_pip7 and new_pip2 > new_pip1:
                pair = new_pip2
        if new_pip1 == new_pip7:
            pair = new_pip1
            if new_pip2 == new_pip3 and new_pip2 > new_pip1:
                pair = new_pip2
        if new_pip2 == new_pip3:
            pair = new_pip2
        if new_pip2 == new_pip7:
            pair = new_pip2
        if new_pip3 == new_pip7:
            pair = new_pip3
    if new_pip4 == new_pip5 == new_pip7:
        trip = new_pip4
        if new_pip1 == new_pip2:
            pair = new_pip1
            if new_pip3 == new_pip6 and new_pip3 > new_pip1:
                pair = new_pip3
        if new_pip1 == new_pip3:
            pair = new_pip1
            if new_pip2 == new_pip6 and new_pip2 > new_pip1:
                pair = new_pip2
        if new_pip1 == new_pip6:
            pair = new_pip1
            if new_pip2 == new_pip3 and new_pip2 > new_pip1:
                pair = new_pip2
        if new_pip2 == new_pip3:
            pair = new_pip2
        if new_pip2 == new_pip6:
            pair = new_pip2
        if new_pip3 == new_pip6:
            pair = new_pip3
    if new_pip4 == new_pip6 == new_pip7:
        trip = new_pip4
        if new_pip1 == new_pip2:
            pair = new_pip1
            if new_pip3 == new_pip5 and new_pip3 > new_pip1:
                pair = new_pip3
        if new_pip1 == new_pip3:
            pair = new_pip1
            if new_pip2 == new_pip5 and new_pip2 > new_pip1:
                pair = new_pip2
        if new_pip1 == new_pip5:
            pair = new_pip1
            if new_pip2 == new_pip3 and new_pip2 > new_pip1:
                pair = new_pip2
        if new_pip2 == new_pip3:
            pair = new_pip2
        if new_pip2 == new_pip5:
            pair = new_pip2
        if new_pip3 == new_pip5:
            pair = new_pip3
    if new_pip5 == new_pip6 == new_pip7:
        trip = new_pip5
        if new_pip1 == new_pip2:
            pair = new_pip1
            if new_pip3 == new_pip4 and new_pip3 > new_pip1:
                pair = new_pip3
        if new_pip1 == new_pip3:
            pair = new_pip1
            if new_pip2 == new_pip4 and new_pip2 > new_pip1:
                pair = new_pip2
        if new_pip1 == new_pip4:
            pair = new_pip1
            if new_pip2 == new_pip3 and new_pip2 > new_pip1:
                pair = new_pip2
        if new_pip2 == new_pip3:
            pair = new_pip2
        if new_pip2 == new_pip4:
            pair = new_pip2
        if new_pip3 == new_pip4:
            pair = new_pip3
    if (trip > 0) and (pair > 0):
        full_house_kicker = pair
    return full_house_kicker


def quads(pip1, pip2, pip3, pip4, pip5, pip6, pip7):
    new_pip1 = face_cards(pip1)
    new_pip2 = face_cards(pip2)
    new_pip3 = face_cards(pip3)
    new_pip4 = face_cards(pip4)
    new_pip5 = face_cards(pip5)
    new_pip6 = face_cards(pip6)
    new_pip7 = face_cards(pip7)
    quad = 0
    if new_pip1 == new_pip2 == new_pip3 == new_pip4:
        quad = new_pip1
    if new_pip1 == new_pip2 == new_pip3 == new_pip5:
        quad = new_pip1
    if new_pip1 == new_pip2 == new_pip3 == new_pip6:
        quad = new_pip1
    if new_pip1 == new_pip2 == new_pip3 == new_pip7:
        quad = new_pip1
    if new_pip1 == new_pip2 == new_pip4 == new_pip5:
        quad = new_pip1
    if new_pip1 == new_pip2 == new_pip4 == new_pip6:
        quad = new_pip1
    if new_pip1 == new_pip2 == new_pip4 == new_pip7:
        quad = new_pip1
    if new_pip1 == new_pip2 == new_pip5 == new_pip6:
        quad = new_pip1
    if new_pip1 == new_pip2 == new_pip5 == new_pip7:
        quad = new_pip1
    if new_pip1 == new_pip2 == new_pip6 == new_pip7:
        quad = new_pip1
    if new_pip1 == new_pip3 == new_pip4 == new_pip5:
        quad = new_pip1
    if new_pip1 == new_pip3 == new_pip4 == new_pip6:
        quad = new_pip1
    if new_pip1 == new_pip3 == new_pip4 == new_pip7:
        quad = new_pip1
    if new_pip1 == new_pip3 == new_pip5 == new_pip6:
        quad = new_pip1
    if new_pip1 == new_pip3 == new_pip5 == new_pip7:
        quad = new_pip1
    if new_pip1 == new_pip3 == new_pip6 == new_pip7:
        quad = new_pip1
    if new_pip1 == new_pip4 == new_pip5 == new_pip6:
        quad = new_pip1
    if new_pip1 == new_pip4 == new_pip5 == new_pip7:
        quad = new_pip1
    if new_pip1 == new_pip4 == new_pip6 == new_pip7:
        quad = new_pip1
    if new_pip1 == new_pip5 == new_pip6 == new_pip7:
        quad = new_pip1
    if new_pip2 == new_pip3 == new_pip4 == new_pip5:
        quad = new_pip2
    if new_pip2 == new_pip3 == new_pip4 == new_pip6:
        quad = new_pip2
    if new_pip2 == new_pip3 == new_pip4 == new_pip7:
        quad = new_pip2
    if new_pip2 == new_pip3 == new_pip5 == new_pip6:
        quad = new_pip2
    if new_pip2 == new_pip3 == new_pip5 == new_pip7:
        quad = new_pip2
    if new_pip2 == new_pip3 == new_pip6 == new_pip7:
        quad = new_pip2
    if new_pip2 == new_pip4 == new_pip5 == new_pip6:
        quad = new_pip2
    if new_pip2 == new_pip4 == new_pip5 == new_pip7:
        quad = new_pip2
    if new_pip2 == new_pip4 == new_pip6 == new_pip7:
        quad = new_pip2
    if new_pip2 == new_pip5 == new_pip6 == new_pip7:
        quad = new_pip2
    if new_pip3 == new_pip4 == new_pip5 == new_pip6:
        quad = new_pip3
    if new_pip3 == new_pip4 == new_pip5 == new_pip7:
        quad = new_pip3
    if new_pip3 == new_pip5 == new_pip6 == new_pip7:
        quad = new_pip3
    if new_pip4 == new_pip5 == new_pip6 == new_pip7:
        quad = new_pip4
    return quad


def quads_kickers(pip1, pip2, pip3, pip4, pip5, pip6, pip7):
    new_pip1 = face_cards(pip1)
    new_pip2 = face_cards(pip2)
    new_pip3 = face_cards(pip3)
    new_pip4 = face_cards(pip4)
    new_pip5 = face_cards(pip5)
    new_pip6 = face_cards(pip6)
    new_pip7 = face_cards(pip7)
    kicker = 0
    if new_pip1 == new_pip2 == new_pip3 == new_pip4:
        kicker = new_pip5
        if new_pip6 > new_pip5:
            kicker = new_pip6
            if new_pip7 > new_pip6:
                kicker = new_pip7
        if new_pip7 > new_pip5:
            kicker = new_pip7
    if new_pip1 == new_pip2 == new_pip3 == new_pip5:
        kicker = new_pip4
        if new_pip6 > new_pip4:
            kicker = new_pip6
            if new_pip7 > new_pip6:
                kicker = new_pip7
        if new_pip7 > new_pip4:
            kicker = new_pip7
    if new_pip1 == new_pip2 == new_pip3 == new_pip6:
        kicker = new_pip4
        if new_pip5 > new_pip4:
            kicker = new_pip5
            if new_pip7 > new_pip5:
                kicker = new_pip7
        if new_pip7 > new_pip4:
            kicker = new_pip7
    if new_pip1 == new_pip2 == new_pip3 == new_pip7:
        kicker = new_pip4
        if new_pip5 > new_pip4:
            kicker = new_pip5
            if new_pip6 > new_pip5:
                kicker = new_pip6
        if new_pip6 > new_pip4:
            kicker = new_pip6
    if new_pip1 == new_pip2 == new_pip4 == new_pip5:
        kicker = new_pip3
        if new_pip6 > new_pip3:
            kicker = new_pip6
            if new_pip7 > new_pip6:
                kicker = new_pip7
        if new_pip7 > new_pip3:
            kicker = new_pip7
    if new_pip1 == new_pip2 == new_pip4 == new_pip6:
        kicker = new_pip3
        if new_pip5 > new_pip3:
            kicker = new_pip5
            if new_pip7 > new_pip5:
                kicker = new_pip7
        if new_pip7 > new_pip3:
            kicker = new_pip7
    if new_pip1 == new_pip2 == new_pip4 == new_pip7:
        kicker = new_pip3
        if new_pip5 > new_pip3:
            kicker = new_pip5
            if new_pip6 > new_pip5:
                kicker = new_pip7
        if new_pip6 > new_pip3:
            kicker = new_pip6
    if new_pip1 == new_pip2 == new_pip5 == new_pip6:
        kicker = new_pip3
        if new_pip4 > new_pip3:
            kicker = new_pip4
            if new_pip7 > new_pip4:
                kicker = new_pip7
        if new_pip7 > new_pip3:
            kicker = new_pip7
    if new_pip1 == new_pip2 == new_pip5 == new_pip7:
        kicker = new_pip3
        if new_pip4 > new_pip3:
            kicker = new_pip4
            if new_pip6 > new_pip4:
                kicker = new_pip6
        if new_pip6 > new_pip3:
            kicker = new_pip6
    if new_pip1 == new_pip2 == new_pip6 == new_pip7:
        kicker = new_pip3
        if new_pip4 > new_pip3:
            kicker = new_pip4
            if new_pip5 > new_pip4:
                kicker = new_pip5
        if new_pip5 > new_pip3:
            kicker = new_pip5
    if new_pip1 == new_pip3 == new_pip4 == new_pip5:
        kicker = new_pip2
        if new_pip6 > new_pip2:
            kicker = new_pip6
            if new_pip7 > new_pip6:
                kicker = new_pip7
        if new_pip7 > new_pip2:
            kicker = new_pip7
    if new_pip1 == new_pip3 == new_pip4 == new_pip6:
        kicker = new_pip2
        if new_pip5 > new_pip2:
            kicker = new_pip5
            if new_pip7 > new_pip5:
                kicker = new_pip7
        if new_pip7 > new_pip2:
            kicker = new_pip7
    if new_pip1 == new_pip3 == new_pip4 == new_pip7:
        kicker = new_pip2
        if new_pip5 > new_pip2:
            kicker = new_pip5
            if new_pip6 > new_pip5:
                kicker = new_pip6
        if new_pip6 > new_pip2:
            kicker = new_pip6
    if new_pip1 == new_pip3 == new_pip5 == new_pip6:
        kicker = new_pip2
        if new_pip4 > new_pip2:
            kicker = new_pip4
            if new_pip7 > new_pip4:
                kicker = new_pip7
        if new_pip7 > new_pip2:
            kicker = new_pip7
    if new_pip1 == new_pip3 == new_pip5 == new_pip7:
        kicker = new_pip2
        if new_pip4 > new_pip2:
            kicker = new_pip4
            if new_pip6 > new_pip4:
                kicker = new_pip6
        if new_pip6 > new_pip2:
            kicker = new_pip6
    if new_pip1 == new_pip3 == new_pip6 == new_pip7:
        kicker = new_pip2
        if new_pip4 > new_pip2:
            kicker = new_pip4
            if new_pip5 > new_pip4:
                kicker = new_pip5
        if new_pip5 > new_pip2:
            kicker = new_pip5
    if new_pip1 == new_pip4 == new_pip5 == new_pip6:
        kicker = new_pip2
        if new_pip3 > new_pip2:
            kicker = new_pip3
            if new_pip7 > new_pip3:
                kicker = new_pip7
        if new_pip7 > new_pip2:
            kicker = new_pip7
    if new_pip1 == new_pip4 == new_pip5 == new_pip7:
        kicker = new_pip2
        if new_pip3 > new_pip2:
            kicker = new_pip3
            if new_pip6 > new_pip3:
                kicker = new_pip6
        if new_pip6 > new_pip2:
            kicker = new_pip6
    if new_pip1 == new_pip4 == new_pip6 == new_pip7:
        kicker = new_pip2
        if new_pip3 > new_pip2:
            kicker = new_pip3
            if new_pip5 > new_pip3:
                kicker = new_pip5
        if new_pip5 > new_pip2:
            kicker = new_pip5
    if new_pip1 == new_pip5 == new_pip6 == new_pip7:
        kicker = new_pip2
        if new_pip3 > new_pip2:
            kicker = new_pip3
            if new_pip4 > new_pip3:
                kicker = new_pip4
        if new_pip4 > new_pip2:
            kicker = new_pip4
    if new_pip2 == new_pip3 == new_pip4 == new_pip5:
        kicker = new_pip1
        if new_pip6 > new_pip1:
            kicker = new_pip6
            if new_pip7 > new_pip6:
                kicker = new_pip7
        if new_pip7 > new_pip1:
            kicker = new_pip7
    if new_pip2 == new_pip3 == new_pip4 == new_pip6:
        kicker = new_pip1
        if new_pip6 > new_pip5:
            kicker = new_pip6
            if new_pip7 > new_pip6:
                kicker = new_pip7
        if new_pip7 > new_pip5:
            kicker = new_pip7
    if new_pip2 == new_pip3 == new_pip4 == new_pip7:
        kicker = new_pip1
        if new_pip5 > new_pip1:
            kicker = new_pip5
            if new_pip6 > new_pip5:
                kicker = new_pip6
        if new_pip6 > new_pip1:
            kicker = new_pip6
    if new_pip2 == new_pip3 == new_pip5 == new_pip6:
        kicker = new_pip1
        if new_pip4 > new_pip1:
            kicker = new_pip4
            if new_pip7 > new_pip4:
                kicker = new_pip7
        if new_pip7 > new_pip1:
            kicker = new_pip7
    if new_pip2 == new_pip3 == new_pip5 == new_pip7:
        kicker = new_pip1
        if new_pip4 > new_pip1:
            kicker = new_pip4
            if new_pip6 > new_pip4:
                kicker = new_pip6
        if new_pip6 > new_pip1:
            kicker = new_pip6
    if new_pip2 == new_pip3 == new_pip6 == new_pip7:
        kicker = new_pip1
        if new_pip4 > new_pip1:
            kicker = new_pip4
            if new_pip5 > new_pip4:
                kicker = new_pip5
        if new_pip5 > new_pip1:
            kicker = new_pip5
    if new_pip2 == new_pip4 == new_pip5 == new_pip6:
        kicker = new_pip1
        if new_pip3 > new_pip1:
            kicker = new_pip3
            if new_pip7 > new_pip3:
                kicker = new_pip7
        if new_pip7 > new_pip1:
            kicker = new_pip7
    if new_pip2 == new_pip4 == new_pip5 == new_pip7:
        kicker = new_pip1
        if new_pip3 > new_pip1:
            kicker = new_pip3
            if new_pip6 > new_pip3:
                kicker = new_pip6
        if new_pip6 > new_pip1:
            kicker = new_pip6
    if new_pip2 == new_pip4 == new_pip6 == new_pip7:
        kicker = new_pip1
        if new_pip3 > new_pip1:
            kicker = new_pip3
            if new_pip5 > new_pip3:
                kicker = new_pip5
        if new_pip5 > new_pip1:
            kicker = new_pip5
    if new_pip2 == new_pip5 == new_pip6 == new_pip7:
        kicker = new_pip1
        if new_pip3 > new_pip1:
            kicker = new_pip3
            if new_pip4 > new_pip3:
                kicker = new_pip4
        if new_pip4 > new_pip1:
            kicker = new_pip4
    if new_pip3 == new_pip4 == new_pip5 == new_pip6:
        kicker = new_pip1
        if new_pip2 > new_pip1:
            kicker = new_pip2
            if new_pip7 > new_pip2:
                kicker = new_pip7
        if new_pip7 > new_pip1:
            kicker = new_pip7
    if new_pip3 == new_pip4 == new_pip5 == new_pip7:
        kicker = new_pip1
        if new_pip2 > new_pip1:
            kicker = new_pip2
            if new_pip6 > new_pip2:
                kicker = new_pip6
        if new_pip6 > new_pip1:
            kicker = new_pip6
    if new_pip3 == new_pip5 == new_pip6 == new_pip7:
        kicker = new_pip1
        if new_pip2 > new_pip1:
            kicker = new_pip2
            if new_pip4 > new_pip2:
                kicker = new_pip4
        if new_pip4 > new_pip1:
            kicker = new_pip4
    if new_pip4 == new_pip5 == new_pip6 == new_pip7:
        kicker = new_pip1
        if new_pip2 > new_pip1:
            kicker = new_pip2
            if new_pip3 > new_pip2:
                kicker = new_pip3
        if new_pip3 > new_pip1:
            kicker = new_pip3
    return kicker


def straight_flushes(pip1, pip2, pip3, pip4, pip5, pip6, pip7, suit1, suit2, suit3, suit4, suit5, suit6, suit7):
    new_pip1 = face_cards(pip1)
    new_pip2 = face_cards(pip2)
    new_pip3 = face_cards(pip3)
    new_pip4 = face_cards(pip4)
    new_pip5 = face_cards(pip5)
    new_pip6 = face_cards(pip6)
    new_pip7 = face_cards(pip7)
    is_flush = flushes(suit1, suit2, suit3, suit4, suit5, suit6, suit7)
    is_flush_kicker = flushes_kicker(suit1, suit2, suit3, suit4, suit5, suit6, suit7)
    straight_flush = 0
    straight = 0
    high_straight = 0
    second_high_straight = 0
    third_high_straight = 0
    fourth_high_straight = 0
    fifth_high_straight = 0
    if new_pip1 - 1 == new_pip2 and suit1 == is_flush_kicker and suit2 == is_flush_kicker:
        high_straight = new_pip1
        second_high_straight = new_pip2
    if new_pip1 - 1 == new_pip3 and suit1 == is_flush_kicker and suit3 == is_flush_kicker:
        high_straight = new_pip1
        second_high_straight = new_pip3
    if new_pip1 - 1 == new_pip4 and suit1 == is_flush_kicker and suit4 == is_flush_kicker:
        high_straight = new_pip1
        second_high_straight = new_pip4
    if new_pip1 - 1 == new_pip5 and suit1 == is_flush_kicker and suit5 == is_flush_kicker:
        high_straight = new_pip1
        second_high_straight = new_pip5
    if new_pip1 - 1 == new_pip6 and suit1 == is_flush_kicker and suit6 == is_flush_kicker:
        high_straight = new_pip1
        second_high_straight = new_pip6
    if new_pip1 - 1 == new_pip7 and suit1 == is_flush_kicker and suit7 == is_flush_kicker:
        high_straight = new_pip1
        second_high_straight = new_pip7
    if new_pip1 + 1 == new_pip2 and suit1 == is_flush_kicker and suit2 == is_flush_kicker:
        high_straight = new_pip2
        second_high_straight = new_pip1
    if new_pip1 + 1 == new_pip3 and suit1 == is_flush_kicker and suit3 == is_flush_kicker:
        high_straight = new_pip3
        second_high_straight = new_pip1
    if new_pip1 + 1 == new_pip4 and suit1 == is_flush_kicker and suit4 == is_flush_kicker:
        high_straight = new_pip4
        second_high_straight = new_pip1
    if new_pip1 + 1 == new_pip5 and suit1 == is_flush_kicker and suit5 == is_flush_kicker:
        high_straight = new_pip5
        second_high_straight = new_pip1
    if new_pip1 + 1 == new_pip6 and suit1 == is_flush_kicker and suit6 == is_flush_kicker:
        high_straight = new_pip6
        second_high_straight = new_pip1
    if new_pip1 + 1 == new_pip7 and suit1 == is_flush_kicker and suit7 == is_flush_kicker:
        high_straight = new_pip7
        second_high_straight = new_pip1
    if high_straight == 0 and new_pip2 - 1 == new_pip3 and suit2 == is_flush_kicker and suit3 == is_flush_kicker:
        high_straight = new_pip2
        second_high_straight = new_pip3
    if high_straight == 0 and new_pip2 - 1 == new_pip4 and suit2 == is_flush_kicker and suit4 == is_flush_kicker:
        high_straight = new_pip2
        second_high_straight = new_pip4
    if high_straight == 0 and new_pip2 - 1 == new_pip5 and suit2 == is_flush_kicker and suit5 == is_flush_kicker:
        high_straight = new_pip2
        second_high_straight = new_pip5
    if high_straight == 0 and new_pip2 - 1 == new_pip6 and suit2 == is_flush_kicker and suit6 == is_flush_kicker:
        high_straight = new_pip2
        second_high_straight = new_pip6
    if high_straight == 0 and new_pip2 - 1 == new_pip7 and suit2 == is_flush_kicker and suit7 == is_flush_kicker:
        high_straight = new_pip2
        second_high_straight = new_pip7
    if high_straight == 0 and new_pip2 + 1 == new_pip3 and suit2 == is_flush_kicker and suit3 == is_flush_kicker:
        high_straight = new_pip3
        second_high_straight = new_pip2
    if high_straight == 0 and new_pip2 + 1 == new_pip4 and suit2 == is_flush_kicker and suit4 == is_flush_kicker:
        high_straight = new_pip4
        second_high_straight = new_pip2
    if high_straight == 0 and new_pip2 + 1 == new_pip5 and suit2 == is_flush_kicker and suit5 == is_flush_kicker:
        high_straight = new_pip5
        second_high_straight = new_pip2
    if high_straight == 0 and new_pip2 + 1 == new_pip6 and suit2 == is_flush_kicker and suit6 == is_flush_kicker:
        high_straight = new_pip6
        second_high_straight = new_pip2
    if high_straight == 0 and new_pip2 + 1 == new_pip7 and suit2 == is_flush_kicker and suit7 == is_flush_kicker:
        high_straight = new_pip7
        second_high_straight = new_pip2
    if high_straight == 0 and new_pip3 - 1 == new_pip4 and suit3 == is_flush_kicker and suit4 == is_flush_kicker:
        high_straight = new_pip3
        second_high_straight = new_pip4
    if high_straight == 0 and new_pip3 - 1 == new_pip5 and suit3 == is_flush_kicker and suit5 == is_flush_kicker:
        high_straight = new_pip3
        second_high_straight = new_pip5
    if high_straight == 0 and new_pip3 - 1 == new_pip6 and suit3 == is_flush_kicker and suit6 == is_flush_kicker:
        high_straight = new_pip3
        second_high_straight = new_pip6
    if high_straight == 0 and new_pip3 - 1 == new_pip7 and suit3 == is_flush_kicker and suit7 == is_flush_kicker:
        high_straight = new_pip3
        second_high_straight = new_pip7
    if high_straight == 0 and new_pip3 + 1 == new_pip4 and suit3 == is_flush_kicker and suit4 == is_flush_kicker:
        high_straight = new_pip4
        second_high_straight = new_pip3
    if high_straight == 0 and new_pip3 + 1 == new_pip5 and suit3 == is_flush_kicker and suit5 == is_flush_kicker:
        high_straight = new_pip5
        second_high_straight = new_pip3
    if high_straight == 0 and new_pip3 + 1 == new_pip6 and suit3 == is_flush_kicker and suit6 == is_flush_kicker:
        high_straight = new_pip6
        second_high_straight = new_pip3
    if high_straight == 0 and new_pip3 + 1 == new_pip7 and suit3 == is_flush_kicker and suit7 == is_flush_kicker:
        high_straight = new_pip7
        second_high_straight = new_pip3
    if second_high_straight - 1 == new_pip2 and suit2 == is_flush_kicker:
        third_high_straight = new_pip2
    if second_high_straight - 1 == new_pip3 and suit3 == is_flush_kicker:
        third_high_straight = new_pip3
    if second_high_straight - 1 == new_pip4 and suit4 == is_flush_kicker:
        third_high_straight = new_pip4
    if second_high_straight - 1 == new_pip5 and suit5 == is_flush_kicker:
        third_high_straight = new_pip5
    if second_high_straight - 1 == new_pip6 and suit6 == is_flush_kicker:
        third_high_straight = new_pip6
    if second_high_straight - 1 == new_pip7 and suit7 == is_flush_kicker:
        third_high_straight = new_pip7
    if third_high_straight - 1 == new_pip2 and suit2 == is_flush_kicker:
        fourth_high_straight = new_pip2
    if third_high_straight - 1 == new_pip3 and suit3 == is_flush_kicker:
        fourth_high_straight = new_pip3
    if third_high_straight - 1 == new_pip4 and suit4 == is_flush_kicker:
        fourth_high_straight = new_pip4
    if third_high_straight - 1 == new_pip5 and suit5 == is_flush_kicker:
        fourth_high_straight = new_pip5
    if third_high_straight - 1 == new_pip6 and suit6 == is_flush_kicker:
        fourth_high_straight = new_pip6
    if third_high_straight - 1 == new_pip7 and suit7 == is_flush_kicker:
        fourth_high_straight = new_pip7
    if fourth_high_straight - 1 == new_pip2 and suit2 == is_flush_kicker:
        fifth_high_straight = new_pip2
    if fourth_high_straight - 1 == new_pip3 and suit3 == is_flush_kicker:
        fifth_high_straight = new_pip3
    if fourth_high_straight - 1 == new_pip4 and suit4 == is_flush_kicker:
        fifth_high_straight = new_pip4
    if fourth_high_straight - 1 == new_pip5 and suit5 == is_flush_kicker:
        fifth_high_straight = new_pip5
    if fourth_high_straight - 1 == new_pip6 and suit6 == is_flush_kicker:
        fifth_high_straight = new_pip6
    if fourth_high_straight - 1 == new_pip7 and suit7 == is_flush_kicker:
        fifth_high_straight = new_pip7
    if high_straight + 1 == new_pip2 and suit2 == is_flush_kicker:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip2
    if high_straight + 1 == new_pip3 and suit3 == is_flush_kicker:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip3
    if high_straight + 1 == new_pip4 and suit4 == is_flush_kicker:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip4
    if high_straight + 1 == new_pip5 and suit5 == is_flush_kicker:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip5
    if high_straight + 1 == new_pip6 and suit6 == is_flush_kicker:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip6
    if high_straight + 1 == new_pip7 and suit7 == is_flush_kicker:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip7
    if high_straight + 1 == new_pip2 and suit2 == is_flush_kicker:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip2
    if high_straight + 1 == new_pip3 and suit3 == is_flush_kicker:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip3
    if high_straight + 1 == new_pip4 and suit4 == is_flush_kicker:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip4
    if high_straight + 1 == new_pip5 and suit5 == is_flush_kicker:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip5
    if high_straight + 1 == new_pip6 and suit6 == is_flush_kicker:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip6
    if high_straight + 1 == new_pip7 and suit7 == is_flush_kicker:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip7
    if high_straight + 1 == new_pip2 and suit2 == is_flush_kicker:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip2
    if high_straight + 1 == new_pip3 and suit3 == is_flush_kicker:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip3
    if high_straight + 1 == new_pip4 and suit4 == is_flush_kicker:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip4
    if high_straight + 1 == new_pip5 and suit5 == is_flush_kicker:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip5
    if high_straight + 1 == new_pip6 and suit6 == is_flush_kicker:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip6
    if high_straight + 1 == new_pip7 and suit7 == is_flush_kicker:
        fifth_high_straight = fourth_high_straight
        fourth_high_straight = third_high_straight
        third_high_straight = second_high_straight
        second_high_straight = high_straight
        high_straight = new_pip7
    if high_straight and second_high_straight and third_high_straight and fourth_high_straight \
            and fifth_high_straight > 0:
        straight = high_straight
    if high_straight == 5 and fourth_high_straight == 2 and new_pip2 == 14 and suit2 == is_flush_kicker:
        straight = 5
    if high_straight == 5 and fourth_high_straight == 2 and new_pip3 == 14 and suit3 == is_flush_kicker:
        straight = 5
    if high_straight == 5 and fourth_high_straight == 2 and new_pip4 == 14 and suit4 == is_flush_kicker:
        straight = 5
    if high_straight == 5 and fourth_high_straight == 2 and new_pip5 == 14 and suit5 == is_flush_kicker:
        straight = 5
    if high_straight == 5 and fourth_high_straight == 2 and new_pip6 == 14 and suit6 == is_flush_kicker:
        straight = 5
    if high_straight == 5 and fourth_high_straight == 2 and new_pip7 == 14 and suit7 == is_flush_kicker:
        straight = 5
    if high_straight == 5 and fourth_high_straight == 2 and new_pip1 == 14 and suit1 == is_flush_kicker:
        straight = 5
    if is_flush and straight > 0:
        straight_flush = straight
    return straight_flush


def best_hands(pip1, pip2, pip3, pip4, pip5, pip6, pip7, suit1, suit2, suit3, suit4, suit5, suit6, suit7):
    hand1_pip1 = face_cards(pip1)
    hand1_pip2 = face_cards(pip2)
    hand1_pip3 = face_cards(pip3)
    hand1_pip4 = face_cards(pip4)
    hand1_pip5 = face_cards(pip5)
    hand1_pip6 = face_cards(pip6)
    hand1_pip7 = face_cards(pip7)
    hand1_suit1 = face_cards(suit1)
    hand1_suit2 = face_cards(suit2)
    hand1_suit3 = face_cards(suit3)
    hand1_suit4 = face_cards(suit4)
    hand1_suit5 = face_cards(suit5)
    hand1_suit6 = face_cards(suit6)
    hand1_suit7 = face_cards(suit7)
    hand_1_straight_flush = straight_flushes(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5, hand1_pip6,
                                             hand1_pip7, hand1_suit1, hand1_suit2, hand1_suit3, hand1_suit4,
                                             hand1_suit5, hand1_suit6, hand1_suit7)
    score = 0
    ordered_cards = []
    if hand_1_straight_flush > 0:
        ordered_cards.append(hand_1_straight_flush)
        ordered_cards.append(hand_1_straight_flush - 1)
        ordered_cards.append(hand_1_straight_flush - 2)
        ordered_cards.append(hand_1_straight_flush - 3)
        ordered_cards.append(hand_1_straight_flush - 4)
        score = Score(Ranking.STRAIGHT_FLUSH, ordered_cards)
    if hand_1_straight_flush == 0:
        hand_1_quads = quads(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5, hand1_pip6, hand1_pip7)
        if hand_1_quads > 0:
            ordered_cards.append(hand_1_quads)
            ordered_cards.append(hand_1_quads)
            ordered_cards.append(hand_1_quads)
            ordered_cards.append(hand_1_quads)
            if high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5, hand1_pip6, hand1_pip7) != hand_1_quads:
                ordered_cards.append(high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5, hand1_pip6, hand1_pip7))
            elif second_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5, hand1_pip6, hand1_pip7) != hand_1_quads:
                ordered_cards.append(second_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5, hand1_pip6, hand1_pip7))
            elif third_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5, hand1_pip6, hand1_pip7) != hand_1_quads:
                ordered_cards.append(third_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5, hand1_pip6, hand1_pip7))
            elif fourth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5, hand1_pip6, hand1_pip7) != hand_1_quads:
                ordered_cards.append(fourth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5, hand1_pip6, hand1_pip7))
            else:
                ordered_cards.append(fifth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5, hand1_pip6, hand1_pip7))
            score = Score(Ranking.FOUR_OF_A_KIND, ordered_cards)
        if hand_1_quads == 0:
            hand_1_full_house = full_houses(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5, hand1_pip6,
                                            hand1_pip7)
            hand_1_full_house_kicker = full_house_kickers(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4,
                                                          hand1_pip5, hand1_pip6, hand1_pip7)
            if hand_1_full_house > 0:
                ordered_cards.append(hand_1_full_house)
                ordered_cards.append(hand_1_full_house)
                ordered_cards.append(hand_1_full_house)
                ordered_cards.append(hand_1_full_house_kicker)
                ordered_cards.append(hand_1_full_house_kicker)
                score = Score(Ranking.FULL_HOUSE, ordered_cards)
            if hand_1_full_house == 0:
                hand_1_flush = flushes(hand1_suit1, hand1_suit2, hand1_suit3, hand1_suit4, hand1_suit5, hand1_suit6,
                                       hand1_suit7)
                hand_1_flush_suit = flushes_kicker(hand1_suit1, hand1_suit2, hand1_suit3, hand1_suit4, hand1_suit5,
                                                   hand1_suit6, hand1_suit7)
                if hand_1_flush > 0:
                    hand_1_flush_kicker1 = high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5,
                                                      hand1_pip6, hand1_pip7)
                    hand_1_flush_kicker2 = second_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5,
                                                      hand1_pip6, hand1_pip7)
                    hand_1_flush_kicker3 = third_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5,
                                                      hand1_pip6, hand1_pip7)
                    hand_1_flush_kicker4 = fourth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5,
                                                      hand1_pip6, hand1_pip7)
                    hand_1_flush_kicker5 = fifth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5,
                                                      hand1_pip6, hand1_pip7)
                    if hand_1_flush_kicker1 == hand1_pip1 and hand1_suit1 != hand_1_flush_suit:
                        hand_1_flush_kicker1 = second_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5,
                                                          hand1_pip6, hand1_pip7)
                        hand_1_flush_kicker2 = third_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4,
                                                                 hand1_pip5,
                                                                 hand1_pip6, hand1_pip7)
                        hand_1_flush_kicker3 = fourth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4,
                                                                hand1_pip5,
                                                                hand1_pip6, hand1_pip7)
                        hand_1_flush_kicker4 = fifth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4,
                                                                 hand1_pip5,
                                                                 hand1_pip6, hand1_pip7)
                        hand_1_flush_kicker5 = sixth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4,
                                                                hand1_pip5,
                                                                hand1_pip6, hand1_pip7)
                    if hand_1_flush_kicker1 == hand1_pip2 and hand1_suit2 != hand_1_flush_suit:
                        hand_1_flush_kicker1 = second_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5,
                                                          hand1_pip6, hand1_pip7)
                        hand_1_flush_kicker2 = third_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4,
                                                                 hand1_pip5,
                                                                 hand1_pip6, hand1_pip7)
                        hand_1_flush_kicker3 = fourth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4,
                                                                hand1_pip5,
                                                                hand1_pip6, hand1_pip7)
                        hand_1_flush_kicker4 = fifth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4,
                                                                 hand1_pip5,
                                                                 hand1_pip6, hand1_pip7)
                        hand_1_flush_kicker5 = sixth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4,
                                                                hand1_pip5,
                                                                hand1_pip6, hand1_pip7)
                    if hand_1_flush_kicker1 == hand1_pip3 and hand1_suit3 != hand_1_flush_suit:
                        hand_1_flush_kicker1 = second_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5,
                                                          hand1_pip6, hand1_pip7)
                        hand_1_flush_kicker2 = third_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4,
                                                                 hand1_pip5,
                                                                 hand1_pip6, hand1_pip7)
                        hand_1_flush_kicker3 = fourth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4,
                                                                hand1_pip5,
                                                                hand1_pip6, hand1_pip7)
                        hand_1_flush_kicker4 = fifth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4,
                                                                 hand1_pip5,
                                                                 hand1_pip6, hand1_pip7)
                        hand_1_flush_kicker5 = sixth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4,
                                                                hand1_pip5,
                                                                hand1_pip6, hand1_pip7)
                    if hand_1_flush_kicker1 == hand1_pip4 and hand1_suit4 != hand_1_flush_suit:
                        hand_1_flush_kicker1 = second_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5,
                                                          hand1_pip6, hand1_pip7)
                        hand_1_flush_kicker2 = third_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4,
                                                                 hand1_pip5,
                                                                 hand1_pip6, hand1_pip7)
                        hand_1_flush_kicker3 = fourth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4,
                                                                hand1_pip5,
                                                                hand1_pip6, hand1_pip7)
                        hand_1_flush_kicker4 = fifth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4,
                                                                 hand1_pip5,
                                                                 hand1_pip6, hand1_pip7)
                        hand_1_flush_kicker5 = sixth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4,
                                                                hand1_pip5,
                                                                hand1_pip6, hand1_pip7)
                    if hand_1_flush_kicker1 == hand1_pip5 and hand1_suit5 != hand_1_flush_suit:
                        hand_1_flush_kicker1 = second_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5,
                                                          hand1_pip6, hand1_pip7)
                        hand_1_flush_kicker2 = third_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4,
                                                                 hand1_pip5,
                                                                 hand1_pip6, hand1_pip7)
                        hand_1_flush_kicker3 = fourth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4,
                                                                hand1_pip5,
                                                                hand1_pip6, hand1_pip7)
                        hand_1_flush_kicker4 = fifth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4,
                                                                 hand1_pip5,
                                                                 hand1_pip6, hand1_pip7)
                        hand_1_flush_kicker5 = sixth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4,
                                                                hand1_pip5,
                                                                hand1_pip6, hand1_pip7)
                    if hand_1_flush_kicker1 == hand1_pip6 and hand1_suit6 != hand_1_flush_suit:
                        hand_1_flush_kicker1 = second_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5,
                                                          hand1_pip6, hand1_pip7)
                        hand_1_flush_kicker2 = third_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4,
                                                                 hand1_pip5,
                                                                 hand1_pip6, hand1_pip7)
                        hand_1_flush_kicker3 = fourth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4,
                                                                hand1_pip5,
                                                                hand1_pip6, hand1_pip7)
                        hand_1_flush_kicker4 = fifth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4,
                                                                 hand1_pip5,
                                                                 hand1_pip6, hand1_pip7)
                        hand_1_flush_kicker5 = sixth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4,
                                                                hand1_pip5,
                                                                hand1_pip6, hand1_pip7)
                    if hand_1_flush_kicker1 == hand1_pip7 and hand1_suit7 != hand_1_flush_suit:
                        hand_1_flush_kicker1 = second_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5,
                                                          hand1_pip6, hand1_pip7)
                        hand_1_flush_kicker2 = third_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4,
                                                                 hand1_pip5,
                                                                 hand1_pip6, hand1_pip7)
                        hand_1_flush_kicker3 = fourth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4,
                                                                hand1_pip5,
                                                                hand1_pip6, hand1_pip7)
                        hand_1_flush_kicker4 = fifth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4,
                                                                 hand1_pip5,
                                                                 hand1_pip6, hand1_pip7)
                        hand_1_flush_kicker5 = sixth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4,
                                                                hand1_pip5,
                                                                hand1_pip6, hand1_pip7)
                    ordered_cards.append(hand_1_flush_kicker1)
                    ordered_cards.append(hand_1_flush_kicker2)
                    ordered_cards.append(hand_1_flush_kicker3)
                    ordered_cards.append(hand_1_flush_kicker4)
                    ordered_cards.append(hand_1_flush_kicker5)
                    score = Score(Ranking.FLUSH, ordered_cards)
                if hand_1_flush == 0:
                    hand_1_straight = straights(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5, hand1_pip6,
                                                hand1_pip7)
                    if hand_1_straight > 0:
                        ordered_cards.append(hand_1_straight)
                        ordered_cards.append(hand_1_straight - 1)
                        ordered_cards.append(hand_1_straight - 2)
                        ordered_cards.append(hand_1_straight - 3)
                        ordered_cards.append(hand_1_straight - 4)
                        score = Score(Ranking.STRAIGHT, ordered_cards)
                    if hand_1_straight == 0:
                        hand_1_trips = trips(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5, hand1_pip6,
                                             hand1_pip7)
                        hand_1_trips_kicker = 0
                        if hand_1_trips > 0:
                            ordered_cards.append(hand_1_trips)
                            ordered_cards.append(hand_1_trips)
                            ordered_cards.append(hand_1_trips)
                            if high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5, hand1_pip6,
                                             hand1_pip7) != hand_1_trips:
                                hand_1_trips_kicker = high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4,
                                                                 hand1_pip5, hand1_pip6, hand1_pip7)
                            elif second_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5,
                                                   hand1_pip6, hand1_pip7) != hand_1_trips:
                                hand_1_trips_kicker = second_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4,
                                                                        hand1_pip5, hand1_pip6, hand1_pip7)
                            elif third_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5,
                                                  hand1_pip6, hand1_pip7) != hand_1_trips:
                                hand_1_trips_kicker = third_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4,
                                                                       hand1_pip5, hand1_pip6, hand1_pip7)
                            elif fourth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5,
                                                   hand1_pip6, hand1_pip7) != hand_1_trips:
                                hand_1_trips_kicker = fourth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4,
                                                                        hand1_pip5, hand1_pip6, hand1_pip7)
                            else:
                                hand_1_trips_kicker = fifth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4,
                                                                        hand1_pip5, hand1_pip6, hand1_pip7)
                            ordered_cards.append(hand_1_trips_kicker)
                            if second_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5, hand1_pip6,
                                                 hand1_pip7) < hand_1_trips_kicker and second_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5, hand1_pip6, hand1_pip7) != hand_1_trips:
                                ordered_cards.append(second_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5,
                                                   hand1_pip6, hand1_pip7))
                            elif third_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5, hand1_pip6,
                                                 hand1_pip7) < hand_1_trips_kicker and third_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5, hand1_pip6, hand1_pip7) != hand_1_trips:
                                ordered_cards.append(third_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5,
                                                   hand1_pip6, hand1_pip7))
                            elif fourth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5, hand1_pip6,
                                                 hand1_pip7) < hand_1_trips_kicker and fourth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5, hand1_pip6, hand1_pip7) != hand_1_trips:
                                ordered_cards.append(fourth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5,
                                                   hand1_pip6, hand1_pip7))
                            else:
                                ordered_cards.append(fifth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5,
                                                   hand1_pip6, hand1_pip7))
                            score = Score(Ranking.THREE_OF_A_KIND, ordered_cards)
                        if hand_1_trips == 0:
                            hand_1_two_pair = two_pairs(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5,
                                                        hand1_pip6, hand1_pip7)
                            if hand_1_two_pair > 0:
                                hand_1_two_pair_kicker = two_pair_kickers(hand1_pip1, hand1_pip2, hand1_pip3,
                                                                          hand1_pip4, hand1_pip5, hand1_pip6,
                                                                          hand1_pip7)
                                ordered_cards.append(hand_1_two_pair)
                                ordered_cards.append(hand_1_two_pair)
                                ordered_cards.append(hand_1_two_pair_kicker)
                                ordered_cards.append(hand_1_two_pair_kicker)
                                if high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5,
                                              hand1_pip6, hand1_pip7) != hand_1_two_pair and high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5, hand1_pip6, hand1_pip7) != hand_1_two_pair_kicker:
                                    ordered_cards.append(high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5,
                                              hand1_pip6, hand1_pip7))
                                elif second_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5,
                                              hand1_pip6, hand1_pip7) != hand_1_two_pair and second_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5, hand1_pip6, hand1_pip7) != hand_1_two_pair_kicker:
                                    ordered_cards.append(second_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5,
                                              hand1_pip6, hand1_pip7))
                                elif third_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5,
                                              hand1_pip6, hand1_pip7) != hand_1_two_pair and third_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5, hand1_pip6, hand1_pip7) != hand_1_two_pair_kicker:
                                    ordered_cards.append(third_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5,
                                              hand1_pip6, hand1_pip7))
                                elif fourth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5,
                                              hand1_pip6, hand1_pip7) != hand_1_two_pair and fourth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5, hand1_pip6, hand1_pip7) != hand_1_two_pair_kicker:
                                    ordered_cards.append(fourth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5,
                                              hand1_pip6, hand1_pip7))
                                else:
                                    ordered_cards.append(fifth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5,
                                              hand1_pip6, hand1_pip7))
                                score = Score(Ranking.TWO_PAIRS, ordered_cards)
                            if hand_1_two_pair == 0:
                                hand_1_pair = pairs(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4, hand1_pip5,
                                                    hand1_pip6, hand1_pip7)
                                if hand_1_pair > 0:
                                    ordered_cards.append(hand_1_pair)
                                    ordered_cards.append(hand_1_pair)
                                    hand_1_pair_kicker1 = high_cards(hand1_pip1, hand1_pip2, hand1_pip3, hand1_pip4,
                                                                     hand1_pip5, hand1_pip6, hand1_pip7)
                                    hand_1_pair_kicker2 = second_high_cards(hand1_pip1, hand1_pip2, hand1_pip3,
                                                                            hand1_pip4, hand1_pip5, hand1_pip6,
                                                                            hand1_pip7)
                                    hand_1_pair_kicker3 = third_high_cards(hand1_pip1, hand1_pip2, hand1_pip3,
                                                                           hand1_pip4, hand1_pip5, hand1_pip6,
                                                                           hand1_pip7)
                                    if hand_1_pair_kicker1 == hand_1_pair:
                                        hand_1_pair_kicker1 = second_high_cards(hand1_pip1, hand1_pip2, hand1_pip3,
                                                                                hand1_pip4, hand1_pip5, hand1_pip6,
                                                                                hand1_pip7)
                                        hand_1_pair_kicker2 = third_high_cards(hand1_pip1, hand1_pip2, hand1_pip3,
                                                                               hand1_pip4, hand1_pip5, hand1_pip6,
                                                                               hand1_pip7)
                                        hand_1_pair_kicker3 = fourth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3,
                                                                                hand1_pip4, hand1_pip5, hand1_pip6,
                                                                                hand1_pip7)
                                        if hand_1_pair_kicker1 == hand_1_pair:
                                            hand_1_pair_kicker1 = third_high_cards(hand1_pip1, hand1_pip2, hand1_pip3,
                                                                                   hand1_pip4, hand1_pip5, hand1_pip6,
                                                                                   hand1_pip7)
                                            hand_1_pair_kicker2 = fourth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3,
                                                                                    hand1_pip4, hand1_pip5, hand1_pip6,
                                                                                    hand1_pip7)
                                            hand_1_pair_kicker3 = fifth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3,
                                                                                   hand1_pip4, hand1_pip5, hand1_pip6,
                                                                                   hand1_pip7)
                                    if hand_1_pair_kicker2 == hand_1_pair:
                                        hand_1_pair_kicker2 = third_high_cards(hand1_pip1, hand1_pip2, hand1_pip3,
                                                                               hand1_pip4, hand1_pip5, hand1_pip6,
                                                                               hand1_pip7)
                                        hand_1_pair_kicker3 = fourth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3,
                                                                                hand1_pip4, hand1_pip5, hand1_pip6,
                                                                                hand1_pip7)
                                        if hand_1_pair_kicker2 == hand_1_pair:
                                            hand_1_pair_kicker2 = fourth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3,
                                                                                    hand1_pip4, hand1_pip5, hand1_pip6,
                                                                                    hand1_pip7)
                                            hand_1_pair_kicker3 = fifth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3,
                                                                                   hand1_pip4, hand1_pip5, hand1_pip6,
                                                                                   hand1_pip7)
                                    if hand_1_pair_kicker3 == hand_1_pair:
                                        hand_1_pair_kicker3 = fourth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3,
                                                                                hand1_pip4, hand1_pip5, hand1_pip6,
                                                                                hand1_pip7)
                                        if hand_1_pair_kicker3 == hand_1_pair:
                                            hand_1_pair_kicker3 = fifth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3,
                                                                                    hand1_pip4, hand1_pip5, hand1_pip6,
                                                                                    hand1_pip7)
                                        if hand_1_pair_kicker1 == hand_1_pair:
                                            hand_1_pair_kicker3 = fifth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3,
                                                                                   hand1_pip4, hand1_pip5, hand1_pip6,
                                                                                   hand1_pip7)
                                    ordered_cards.append(hand_1_pair_kicker1)
                                    ordered_cards.append(hand_1_pair_kicker2)
                                    ordered_cards.append(hand_1_pair_kicker3)
                                    score = Score(Ranking.PAIR, ordered_cards)
                                if hand_1_pair == 0:
                                    hand_1_high_card_kicker1 = high_cards(hand1_pip1, hand1_pip2, hand1_pip3,
                                                                          hand1_pip4, hand1_pip5, hand1_pip6,
                                                                          hand1_pip7)
                                    hand_1_high_card_kicker2 = second_high_cards(hand1_pip1, hand1_pip2, hand1_pip3,
                                                                                 hand1_pip4, hand1_pip5, hand1_pip6,
                                                                                 hand1_pip7)
                                    hand_1_high_card_kicker3 = third_high_cards(hand1_pip1, hand1_pip2, hand1_pip3,
                                                                                hand1_pip4, hand1_pip5, hand1_pip6,
                                                                                hand1_pip7)
                                    hand_1_high_card_kicker4 = fourth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3,
                                                                                 hand1_pip4, hand1_pip5, hand1_pip6,
                                                                                 hand1_pip7)
                                    hand_1_high_card_kicker5 = fifth_high_cards(hand1_pip1, hand1_pip2, hand1_pip3,
                                                                                hand1_pip4, hand1_pip5, hand1_pip6,
                                                                                hand1_pip7)
                                    ordered_cards.append(hand_1_high_card_kicker1)
                                    ordered_cards.append(hand_1_high_card_kicker2)
                                    ordered_cards.append(hand_1_high_card_kicker3)
                                    ordered_cards.append(hand_1_high_card_kicker4)
                                    ordered_cards.append(hand_1_high_card_kicker5)
                                    score = Score(Ranking.HIGH_CARD, ordered_cards)
    return score


if __name__ == '__main__':
    print(hand_1)
    print(hand_2)
    print(best_hands(card_1_pip, card_2_pip, card_3_pip, card_4_pip, card_5_pip, card_6_pip, card_7_pip, card_1_suit,
              card_2_suit, card_3_suit, card_4_suit, card_5_suit, card_6_suit, card_7_suit))