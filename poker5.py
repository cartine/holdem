from enum import Enum
from enum import IntEnum
from random import shuffle


# Important to note!! 'hand' must be ordered from most important card
# to least important card
class Score:
    def __init__(self, ranking, hand):
        assert (isinstance(ranking, Ranking))
        validate_cards(hand, 5)
        self.RANKING = ranking
        self.HAND = hand

    def __str__(self):
        return self.RANKING.name + ", " + str(self.HAND)

    def compare(self, score2):
        r = self.RANKING - score2.RANKING
        if r == 0:
            for i in range(0, 5):
                r = get_pip_value(self.HAND[i]) - get_pip_value(score2.HAND[i])
                if r != 0:
                    break
        return r


def get_score(cards):
    validate_cards(cards, 7)
    flush = get_flush(cards)
    ordered_cards = get_ordered_cards(cards)
    if flush:
        straight_flush = get_straight_flush(ordered_cards, Suit(flush.HAND[0][1]))
        if straight_flush:
            return straight_flush

    match_ordered_cards = get_match_ordered_cards(ordered_cards)
    four_of_a_kind = get_four_of_a_kind(match_ordered_cards)
    if four_of_a_kind:
        return four_of_a_kind

    if flush:
        return flush

    straight = get_straight(ordered_cards)
    if straight:
        return straight

    full_house = get_full_house(match_ordered_cards)
    if full_house:
        return full_house

    three_of_a_kind = get_three_of_a_kind(match_ordered_cards)
    if three_of_a_kind:
        return three_of_a_kind

    two_pair = get_two_pair(match_ordered_cards)
    if two_pair:
        return two_pair

    pair = get_pair(match_ordered_cards)
    if pair:
        return pair

    return get_high_card(match_ordered_cards)


def get_deck(shuffled: bool = True):
    deck = []
    for pip in Pip:
        for suit in Suit:
            card = (pip.value + suit.value)
            deck.append(card)
    if shuffled:
        shuffle(deck)
    return deck


class Pip(Enum):
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = 'T'
    JACK = 'J'
    QUEEN = 'Q'
    KING = 'K'
    ACE = 'A'


class Suit(Enum):
    HEART = 'H'
    SPADE = 'S'
    CLUB = 'C'
    DIAMOND = 'D'


class Ranking(IntEnum):
    STRAIGHT_FLUSH = 8
    FOUR_OF_A_KIND = 7
    FULL_HOUSE = 6
    FLUSH = 5
    STRAIGHT = 4
    THREE_OF_A_KIND = 3
    TWO_PAIRS = 2
    PAIR = 1
    HIGH_CARD = 0


def get_pip_value(card):
#    assert (len(card) == 2)
    p = card[0]
    return get_pip(p)


def get_pip(pip):
    p = pip
    if p == '2':
        return 2
    elif p == '3':
        return 3
    elif p == '4':
        return 4
    elif p == '5':
        return 5
    elif p == '6':
        return 6
    elif p == '7':
        return 7
    elif p == '8':
        return 8
    elif p == '9':
        return 9
    elif p == 'T':
        return 10
    elif p == 'J':
        return 11
    elif p == 'Q':
        return 12
    elif p == 'K':
        return 13
    elif p == 'A':
        return 14
    else:
        raise Exception


def get_straight_flush(ordered_cards, suit: Suit):
    sorted_ordered_cards = list(filter(lambda x: Suit(x[1]) == suit, ordered_cards))
    ln = len(ordered_cards)
    if ln < 5:
        raise Exception("Don't call this method if you don't have a flush.")

    s = get_straight_not_ace_low(sorted_ordered_cards, 0)
    if not s and ln > 5:
        s = get_straight_not_ace_low(sorted_ordered_cards, 1)
    if not s and ln > 6:
        s = get_straight_not_ace_low(sorted_ordered_cards, 2)
    if not s:
        s = get_straight_ace_log(sorted_ordered_cards)
    if not s:
        return

    score = Score(Ranking.STRAIGHT_FLUSH, s.HAND)
    return score


def get_straight_not_ace_low(ordered_cards, pos):
    validate_cards(ordered_cards)
    assert (pos < 3)
    c = ordered_cards[0:]
    hand = []
    last_pip_val = get_pip_value(c[pos])
    hand.append(c.pop(pos))
    while len(hand) < 5 and pos < len(c):
        pip_val = get_pip_value(c[pos])
        if pip_val == last_pip_val:
            pos += 1
            if pos >= len(c):
                return
        elif pip_val == last_pip_val - 1:
            last_pip_val = pip_val
            hand.append(c.pop(pos))
        else:
            return
    if len(hand) < 5:
        return
    else:
        return Score(Ranking.STRAIGHT, hand)


def validate_cards(*args):
    assert (len(args) == 1 or len(args) == 2)
    if len(args) == 2:
        assert (len(args[0]) == args[1])
    for card in args[0]:
        assert (len(card) == 2)


def get_flush(cards):
    clubs = []
    hearts = []
    diamonds = []
    spades = []
    for card in cards:
        if card[1] == 'C':
            clubs.append(card)
        elif card[1] == 'H':
            hearts.append(card)
        elif card[1] == 'D':
            diamonds.append(card)
        else:
            assert (card[1] == 'S')
            spades.append(card)
    flush = make_flush(clubs)
    if not flush:
        flush = make_flush(hearts)
    if not flush:
        flush = make_flush(diamonds)
    if not flush:
        flush = make_flush(spades)
    return flush


def make_flush(cards_of_one_suit):
    if len(cards_of_one_suit) < 5:
        return
    else:
        sorted_cards = sorted(cards_of_one_suit,
                              key=lambda c: get_pip_value(c),
                              reverse=True)
        score = Score(Ranking.FLUSH, sorted_cards[0:5])
        return score


def get_ordered_cards(cards):
    validate_cards(cards)
    ordered_cards = sorted(cards, key=lambda c: get_pip_value(c), reverse=True)
    return ordered_cards


def get_match_ordered_cards(ordered_cards):
    validate_cards(ordered_cards)
    a = []
    pos = 0
    while pos < len(ordered_cards):
        count = find_match_length(ordered_cards, pos)
        b = (count, pos)
        a.append(0)
        a[-1] = b
        pos += count
    a = sorted(a, key=lambda c: (100 * c[0]) - c[1], reverse=True)
    match_ordered_cards = []
    for count, pos in a:
        for i in range(pos, pos + count):
            match_ordered_cards.append(0)
            match_ordered_cards[-1] = ordered_cards[i]
    return match_ordered_cards


def find_match_length(ordered_cards, pos):
    assert (pos < len(ordered_cards))
    val = get_pip_value(ordered_cards[pos])
    count = 1
    pos += 1
    while pos < len(ordered_cards):
        if get_pip_value(ordered_cards[pos]) == val:
            count += 1
            pos += 1
        else:
            break
    return count


def get_four_of_a_kind(match_ordered_cards):
    m = match_ordered_cards
    if m[0][0] == m[1][0] == m[2][0] == m[3][0]:
        kicker = get_highest(m, 4)
        hand = m[0:4]
        hand.append(kicker)
        return Score(Ranking.FOUR_OF_A_KIND, hand)
    else:
        return None


def get_straight(ordered_cards):
    validate_cards(ordered_cards, 7)
    s = get_straight_not_ace_low(ordered_cards, 0)
    if not s:
        s = get_straight_not_ace_low(ordered_cards, 1)
    if not s:
        s = get_straight_not_ace_low(ordered_cards, 2)
    if not s:
        s = get_straight_ace_log(ordered_cards)
    return s


def get_straight_ace_log(ordered_cards):
    validate_cards(ordered_cards)
    if ordered_cards[0][0] != 'A':
        return
    ace = ordered_cards[0]
    hand = []
    c = ordered_cards[1:]
    # find the 5, 4, 3, and 2
    for i in range(5, 1, -1):
        success = find_next_card(hand, c, str(i))
        if not success:
            return
    assert (len(hand) == 4)
    # hand now has the 5, 4, 3, and 2. Stick the ace at the end.
    hand.append(ace)
    return Score(Ranking.STRAIGHT, hand)


def find_next_card(hand, c, pip):
    while len(c) > 0:
        if c[0][0] == pip:
            hand.append(c.pop(0))
            return 1
        else:
            c.pop(0)
    return 0


def get_full_house(match_ordered_cards):
    m = match_ordered_cards
    if m[0][0] == m[1][0] == m[2][0] and m[3][0] == m[4][0]:
        return Score(Ranking.FULL_HOUSE, m[0:5])
    else:
        return None


def get_three_of_a_kind(match_ordered_cards):
    m = match_ordered_cards
    if m[0][0] == m[1][0] == m[2][0]:
        return Score(Ranking.THREE_OF_A_KIND, m[0:5])
    else:
        return None


def get_two_pair(match_ordered_cards):
    m = match_ordered_cards
    if m[0][0] == m[1][0] and m[2][0] == m[3][0]:
        kicker = get_highest(m, 4)
        hand = m[0:4]
        hand.append(kicker)
        return Score(Ranking.TWO_PAIRS, hand)
    else:
        return None


def get_pair(match_ordered_cards):
    m = match_ordered_cards
    if m[0][0] == m[1][0]:
        return Score(Ranking.PAIR, m[0:5])
    else:
        return None


def get_high_card(match_ordered_cards):
    return Score(Ranking.HIGH_CARD, match_ordered_cards[0:5])


def get_highest(cards, pos):
    validate_cards(cards)
    assert (pos < len(cards))
    val = -1
    c = None
    for card in cards[pos: len(cards)]:
        x = get_pip_value(card)
        if x > val:
            c = card
            val = x
    return c
