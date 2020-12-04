from Peter7CardBestHandRemastered2 import *


def face_cards(face_card):
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
    if face_card != 'T' or 'J' or 'Q' or 'K' or 'A':
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


value = [2, 3, 4, 5, 6, 7, 8, 9, 'T', 'J', 'Q', 'K', 'A']
suit = ['H', 'D', 'S', 'C']


def Pair(pip1, pip2, pip3, pip4, pip5):
    new_pip1 = face_cards(pip1)
    new_pip2 = face_cards(pip2)
    new_pip3 = face_cards(pip3)
    new_pip4 = face_cards(pip4)
    new_pip5 = face_cards(pip5)
    pair = 0
    sorted_pips = sorted([new_pip1, new_pip2, new_pip3, new_pip4, new_pip5], reverse=True)
    if sorted_pips[0] == sorted_pips[1]:
        pair = sorted_pips[0]
    elif sorted_pips[1] == sorted_pips[2]:
        pair = sorted_pips[1]
    elif sorted_pips[2] == sorted_pips[3]:
        pair = sorted_pips[2]
    elif sorted_pips[3] == sorted_pips[4]:
        pair = sorted_pips[3]
    return pair


def Pair_kickers(pip1, pip2, pip3, pip4, pip5):
    new_pip1 = face_cards(pip1)
    new_pip2 = face_cards(pip2)
    new_pip3 = face_cards(pip3)
    new_pip4 = face_cards(pip4)
    new_pip5 = face_cards(pip5)
    pair_kickers = 0
    sorted_pips = sorted([new_pip1, new_pip2, new_pip3, new_pip4, new_pip5], reverse=True)
    if sorted_pips[0] == sorted_pips[1]:
        pair_kickers = [sorted_pips[2], sorted_pips[3], sorted_pips[4]]
    elif sorted_pips[1] == sorted_pips[2]:
        pair_kickers = [sorted_pips[0], sorted_pips[3], sorted_pips[4]]
    elif sorted_pips[2] == sorted_pips[3]:
        pair_kickers = [sorted_pips[0], sorted_pips[1], sorted_pips[4]]
    elif sorted_pips[3] == sorted_pips[4]:
        pair_kickers = [sorted_pips[0], sorted_pips[1], sorted_pips[2]]
    return pair_kickers


def Two_pair(pip1, pip2, pip3, pip4, pip5):
    new_pip1 = face_cards(pip1)
    new_pip2 = face_cards(pip2)
    new_pip3 = face_cards(pip3)
    new_pip4 = face_cards(pip4)
    new_pip5 = face_cards(pip5)
    two_pair = 0
    sorted_pips = sorted([new_pip1, new_pip2, new_pip3, new_pip4, new_pip5], reverse=True)
    if (sorted_pips[0] == sorted_pips[1]) and (sorted_pips[2] == sorted_pips[3]):
        two_pair = sorted_pips[0]
    elif (sorted_pips[0] == sorted_pips[1]) and (sorted_pips[3] == sorted_pips[4]):
        two_pair = sorted_pips[0]
    elif (sorted_pips[1] == sorted_pips[2]) and (sorted_pips[3] == sorted_pips[4]):
        two_pair = sorted_pips[1]
    return two_pair


def Two_pair_kicker(pip1, pip2, pip3, pip4, pip5):
    new_pip1 = face_cards(pip1)
    new_pip2 = face_cards(pip2)
    new_pip3 = face_cards(pip3)
    new_pip4 = face_cards(pip4)
    new_pip5 = face_cards(pip5)
    two_pair_kicker = 0
    sorted_pips = sorted([new_pip1, new_pip2, new_pip3, new_pip4, new_pip5], reverse=True)
    if (sorted_pips[0] == sorted_pips[1]) and (sorted_pips[2] == sorted_pips[3]):
        two_pair_kicker = sorted_pips[2]
    elif (sorted_pips[0] == sorted_pips[1]) and (sorted_pips[3] == sorted_pips[4]):
        two_pair_kicker = sorted_pips[3]
    elif (sorted_pips[1] == sorted_pips[2]) and (sorted_pips[3] == sorted_pips[4]):
        two_pair_kicker = sorted_pips[3]
    return two_pair_kicker


def Two_pair_kicker_kicker(pip1, pip2, pip3, pip4, pip5):
    new_pip1 = face_cards(pip1)
    new_pip2 = face_cards(pip2)
    new_pip3 = face_cards(pip3)
    new_pip4 = face_cards(pip4)
    new_pip5 = face_cards(pip5)
    two_pair_kicker_kicker = 0
    sorted_pips = sorted([new_pip1, new_pip2, new_pip3, new_pip4, new_pip5], reverse=True)
    if (sorted_pips[0] == sorted_pips[1]) and (sorted_pips[2] == sorted_pips[3]):
        two_pair_kicker_kicker = sorted_pips[4]
    elif (sorted_pips[0] == sorted_pips[1]) and (sorted_pips[3] == sorted_pips[4]):
        two_pair_kicker_kicker = sorted_pips[2]
    elif (sorted_pips[1] == sorted_pips[2]) and (sorted_pips[3] == sorted_pips[4]):
        two_pair_kicker_kicker = sorted_pips[0]
    return two_pair_kicker_kicker


def Trips(pip1, pip2, pip3, pip4, pip5):
    new_pip1 = face_cards(pip1)
    new_pip2 = face_cards(pip2)
    new_pip3 = face_cards(pip3)
    new_pip4 = face_cards(pip4)
    new_pip5 = face_cards(pip5)
    trips = 0
    sorted_pips = sorted([new_pip1, new_pip2, new_pip3, new_pip4, new_pip5], reverse=True)
    if sorted_pips[0] == sorted_pips[1] == sorted_pips[2]:
        trips = sorted_pips[0]
    elif sorted_pips[1] == sorted_pips[2] == sorted_pips[3]:
        trips = sorted_pips[1]
    elif sorted_pips[2] == sorted_pips[3] == sorted_pips[4]:
        trips = sorted_pips[2]
    return trips


def Trips_kickers(pip1, pip2, pip3, pip4, pip5):
    new_pip1 = face_cards(pip1)
    new_pip2 = face_cards(pip2)
    new_pip3 = face_cards(pip3)
    new_pip4 = face_cards(pip4)
    new_pip5 = face_cards(pip5)
    trips_kickers = 0
    sorted_pips = sorted([new_pip1, new_pip2, new_pip3, new_pip4, new_pip5], reverse=True)
    if sorted_pips[0] == sorted_pips[1] == sorted_pips[2]:
        trips_kickers = [sorted_pips[3], sorted_pips[4]]
    elif sorted_pips[1] == sorted_pips[2] == sorted_pips[3]:
        trips_kickers = [sorted_pips[0], sorted_pips[4]]
    elif sorted_pips[2] == sorted_pips[3] == sorted_pips[4]:
        trips_kickers = [sorted_pips[0], sorted_pips[1]]
    return trips_kickers


def Straight(pip1, pip2, pip3, pip4, pip5):
    new_pip1 = face_cards(pip1)
    new_pip2 = face_cards(pip2)
    new_pip3 = face_cards(pip3)
    new_pip4 = face_cards(pip4)
    new_pip5 = face_cards(pip5)
    straight = 0
    sorted_pips = sorted([new_pip1, new_pip2, new_pip3, new_pip4, new_pip5], reverse=True)
    if sorted_pips[0] - 1 == sorted_pips[1]:
        if sorted_pips[1] - 1 == sorted_pips[2]:
            if sorted_pips[2] - 1 == sorted_pips[3]:
                if sorted_pips[3] - 1 == sorted_pips[4]:
                    straight = sorted_pips[0]
                    return straight
    elif sorted_pips[1] - 1 == sorted_pips[2]:
        if sorted_pips[2] - 1 == sorted_pips[3]:
            if sorted_pips[3] - 1 == sorted_pips[4]:
                if sorted_pips[4] - 1 == 1:
                    if sorted_pips[0] == 14:
                        straight = sorted_pips[1]
                        return straight
    return straight


def Flush(suit1, suit2, suit3, suit4, suit5):
    flush = 0
    if suit1 == suit2:
        if suit2 == suit3:
            if suit3 == suit4:
                if suit4 == suit5:
                    flush = 1
                    return flush
    return flush


def Full_house(pip1, pip2, pip3, pip4, pip5):
    new_pip1 = face_cards(pip1)
    new_pip2 = face_cards(pip2)
    new_pip3 = face_cards(pip3)
    new_pip4 = face_cards(pip4)
    new_pip5 = face_cards(pip5)
    full_house = 0
    sorted_pips = sorted([new_pip1, new_pip2, new_pip3, new_pip4, new_pip5], reverse=True)
    if sorted_pips[0] == sorted_pips[1] == sorted_pips[2]:
        if sorted_pips[3] == sorted_pips[4]:
            full_house = sorted_pips[0]
    elif sorted_pips[2] == sorted_pips[3] == sorted_pips[4]:
        if sorted_pips[0] == sorted_pips[1]:
            full_house = sorted_pips[2]
    return full_house


def Full_house_kicker(pip1, pip2, pip3, pip4, pip5):
    new_pip1 = face_cards(pip1)
    new_pip2 = face_cards(pip2)
    new_pip3 = face_cards(pip3)
    new_pip4 = face_cards(pip4)
    new_pip5 = face_cards(pip5)
    full_house_kicker = 0
    sorted_pips = sorted([new_pip1, new_pip2, new_pip3, new_pip4, new_pip5], reverse=True)
    if sorted_pips[0] == sorted_pips[1] == sorted_pips[2]:
        if sorted_pips[3] == sorted_pips[4]:
            full_house_kicker = sorted_pips[3]
    elif sorted_pips[2] == sorted_pips[3] == sorted_pips[4]:
        if sorted_pips[0] == sorted_pips[1]:
            full_house_kicker = sorted_pips[0]
    return full_house_kicker


def Quads(pip1, pip2, pip3, pip4, pip5):
    new_pip1 = face_cards(pip1)
    new_pip2 = face_cards(pip2)
    new_pip3 = face_cards(pip3)
    new_pip4 = face_cards(pip4)
    new_pip5 = face_cards(pip5)
    quads = 0
    sorted_pips = sorted([new_pip1, new_pip2, new_pip3, new_pip4, new_pip5], reverse=True)
    if sorted_pips[0] == sorted_pips[1] == sorted_pips[2] == sorted_pips[3]:
        quads = sorted_pips[0]
    elif sorted_pips[1] == sorted_pips[2] == sorted_pips[3] == sorted_pips[4]:
        quads = sorted_pips[1]
    return quads


def Quads_kicker(pip1, pip2, pip3, pip4, pip5):
    new_pip1 = face_cards(pip1)
    new_pip2 = face_cards(pip2)
    new_pip3 = face_cards(pip3)
    new_pip4 = face_cards(pip4)
    new_pip5 = face_cards(pip5)
    quads_kicker = 0
    sorted_pips = sorted([new_pip1, new_pip2, new_pip3, new_pip4, new_pip5], reverse=True)
    if sorted_pips[0] == sorted_pips[1] == sorted_pips[2] == sorted_pips[3]:
        quads_kicker = sorted_pips[4]
    elif sorted_pips[1] == sorted_pips[2] == sorted_pips[3] == sorted_pips[4]:
        quads_kicker = sorted_pips[0]
    return quads_kicker


def Straight_flush(pip1, pip2, pip3, pip4, pip5, suit1, suit2, suit3, suit4, suit5):
    new_pip1 = face_cards(pip1)
    new_pip2 = face_cards(pip2)
    new_pip3 = face_cards(pip3)
    new_pip4 = face_cards(pip4)
    new_pip5 = face_cards(pip5)
    flush = 0
    straight = 0
    sorted_pips = sorted([new_pip1, new_pip2, new_pip3, new_pip4, new_pip5], reverse=True)
    if sorted_pips[0] - 1 == sorted_pips[1]:
        if sorted_pips[1] - 1 == sorted_pips[2]:
            if sorted_pips[2] - 1 == sorted_pips[3]:
                if sorted_pips[3] - 1 == sorted_pips[4]:
                    straight = sorted_pips[0]
    elif sorted_pips[1] - 1 == sorted_pips[2]:
        if sorted_pips[2] - 1 == sorted_pips[3]:
            if sorted_pips[3] - 1 == sorted_pips[4]:
                if sorted_pips[4] - 1 == 1:
                    if sorted_pips[0] == 14:
                        straight = sorted_pips[1]
    if suit1 == suit2:
        if suit2 == suit3:
            if suit3 == suit4:
                if suit4 == suit5:
                    flush = 1
    if (flush > 0) and (straight > 0):
        return straight
    else: return 0


def Best_Hand(pip1, pip2, pip3, pip4, pip5, suit1, suit2, suit3, suit4, suit5):
    score = 0
    new_pip1 = face_cards(pip1)
    new_pip2 = face_cards(pip2)
    new_pip3 = face_cards(pip3)
    new_pip4 = face_cards(pip4)
    new_pip5 = face_cards(pip5)
    ordered_cards = sorted([new_pip1, new_pip2, new_pip3, new_pip4, new_pip5], reverse=True)
    straight_flush = Straight_flush(pip1, pip2, pip3, pip4, pip5, suit1, suit2, suit3, suit4, suit5)
    if straight_flush > 0:
        if straight_flush == 5:
            ordered_cards = [5, 4, 3, 2, 14]
        else:
            ordered_cards = sorted([pip1, pip2, pip3, pip4, pip5], reverse=True)
        score = Score(Ranking.STRAIGHT_FLUSH, ordered_cards)
        return score
    else:
        quads = Quads(pip1, pip2, pip3, pip4, pip5)
        quads_kicker = Quads_kicker(pip1, pip2, pip3, pip4, pip5)
        if quads > 0:
            ordered_cards = [quads, quads, quads, quads, quads_kicker]
            score = Score(Ranking.FOUR_OF_A_KIND, ordered_cards)
            return score
        else:
            full_house = Full_house(pip1, pip2, pip3, pip4, pip5)
            full_house_kicker = Full_house_kicker(pip1, pip2, pip3, pip4, pip5)
            if full_house > 0:
                ordered_cards = [full_house, full_house, full_house, full_house_kicker, full_house_kicker]
                score = Score(Ranking.FULL_HOUSE, ordered_cards)
                return score
            else:
                flush = Flush(suit1, suit2, suit3, suit4, suit5)
                if flush > 0:
                    score = Score(Ranking.FLUSH, ordered_cards)
                    return score
                else:
                    straight = Straight(pip1, pip2, pip3, pip4, pip5)
                    if straight > 0:
                        if straight == 5:
                            ordered_cards = [5, 4, 3, 2, 14]
                            score = Score(Ranking.STRAIGHT, ordered_cards)
                        else:
                            score = Score(Ranking.STRAIGHT, ordered_cards)
                        return score
                    else:
                        trips = Trips(pip1, pip2, pip3, pip4, pip5)
                        trips_kicker = Trips_kickers(pip1, pip2, pip3, pip4, pip5)
                        if trips > 0:
                            ordered_cards = [trips, trips, trips]
                            for e in trips_kicker:
                                ordered_cards.append(e)
                            score = Score(Ranking.THREE_OF_A_KIND, ordered_cards)
                            return score
                        else:
                            two_pair = Two_pair(pip1, pip2, pip3, pip4, pip5)
                            two_pair_kicker = Two_pair_kicker(pip1, pip2, pip3, pip4, pip5)
                            two_pair_kicker_kicker = Two_pair_kicker_kicker(pip1, pip2, pip3, pip4, pip5)
                            if two_pair > 0:
                                ordered_cards = [two_pair, two_pair, two_pair_kicker, two_pair_kicker, two_pair_kicker_kicker]
                                score = Score(Ranking.TWO_PAIRS, ordered_cards)
                                return score
                            else:
                                pair = Pair(pip1, pip2, pip3, pip4, pip5)
                                pair_kickers = Pair_kickers(pip1, pip2, pip3, pip4, pip5)
                                if pair > 0:
                                    ordered_cards = [pair, pair]
                                    for e in pair_kickers:
                                        ordered_cards.append(e)
                                    score = Score(Ranking.PAIR, ordered_cards)
                                    return score
                                else:
                                    score = Score(Ranking.HIGH_CARD, ordered_cards)
                                    return score


if __name__ == '__main__':
    for e in range(0, 100000):
        card_1_value = random.choice(value)
        card_1_suit = random.choice(suit)
        card_1 = [card_1_value, card_1_suit]
        card_2_value = random.choice(value)
        card_2_suit = random.choice(suit)
        card_2 = [card_2_value, card_2_suit]
        card_3_value = random.choice(value)
        card_3_suit = random.choice(suit)
        card_3 = [card_3_value, card_3_suit]
        card_4_value = random.choice(value)
        card_4_suit = random.choice(suit)
        card_4 = [card_4_value, card_4_suit]
        card_5_value = random.choice(value)
        card_5_suit = random.choice(suit)
        card_5 = [card_5_value, card_5_suit]
        hand_1 = [card_1, card_2, card_3, card_4, card_5]
        print(hand_1)
        card_6_value = random.choice(value)
        card_6_suit = random.choice(suit)
        card_6 = [card_6_value, card_6_suit]
        card_7_value = random.choice(value)
        card_7_suit = random.choice(suit)
        card_7 = [card_7_value, card_7_suit]
        card_8_value = random.choice(value)
        card_8_suit = random.choice(suit)
        card_8 = [card_8_value, card_8_suit]
        card_9_value = random.choice(value)
        card_9_suit = random.choice(suit)
        card_9 = [card_9_value, card_9_suit]
        card_10_value = random.choice(value)
        card_10_suit = random.choice(suit)
        card_10 = [card_10_value, card_10_suit]
        hand_2 = [card_6, card_7, card_8, card_9, card_10]
        print(hand_2)
        print(Best_Hand(card_1_value, card_2_value, card_3_value, card_4_value, card_5_value, card_1_suit, card_2_suit,
                  card_3_suit, card_4_suit, card_5_suit))


def changeParams(hand):
    a = [hand[0][0], hand[1][0], hand[2][0], hand[3][0], hand[4][0], hand[0][1], hand[1][1], hand[2][1], hand[3][1],
         hand[4][1]]
    for i in range(0, len(a)):
        if a[i].isdigit():
            a[i] = int(a[i])

    return a
